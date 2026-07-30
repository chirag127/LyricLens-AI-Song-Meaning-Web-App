/**
 * lyrics-sources.js — multi-source lyrics fetcher
 * Sources (in order): lyrics.ovh → LRCLIB → Genius (via CORS proxy) → LLM fallback
 */

const CORS = 'https://corsproxy.io/?';

export const SOURCE_LABELS = {
  lyricsovh: 'lyrics.ovh',
  lrclib: 'LRCLIB',
  genius: 'Genius',
  ai: 'AI knowledge',
};

/**
 * @returns {{ lyrics: string, source: string, synced: Array|null, error?: string }|null}
 */
export async function fetchLyrics(artist, title) {
  // 1. lyrics.ovh
  try {
    const r = await fetch(
      `https://api.lyrics.ovh/v1/${encodeURIComponent(artist)}/${encodeURIComponent(title)}`
    );
    if (r.ok) {
      const d = await r.json();
      if (d.lyrics && d.lyrics.trim()) {
        return { lyrics: d.lyrics.trim(), source: 'lyricsovh', synced: null };
      }
    }
  } catch (_) {}

  // 2. LRCLIB
  try {
    const r = await fetch(
      `https://lrclib.net/api/search?artist_name=${encodeURIComponent(artist)}&track_name=${encodeURIComponent(title)}`
    );
    if (r.ok) {
      const results = await r.json();
      const match = results[0];
      if (match) {
        // prefer synced; fall back to plain
        if (match.syncedLyrics) {
          const parsed = parseLrc(match.syncedLyrics);
          return {
            lyrics: match.plainLyrics || lrcToPlain(parsed),
            source: 'lrclib',
            synced: parsed,
          };
        }
        if (match.plainLyrics) {
          return { lyrics: match.plainLyrics.trim(), source: 'lrclib', synced: null };
        }
      }
    }
  } catch (_) {}

  // 3. Genius via corsproxy
  try {
    const searchUrl = `https://api.genius.com/search?q=${encodeURIComponent(artist + ' ' + title)}`;
    const r = await fetch(CORS + encodeURIComponent(searchUrl), {
      headers: { Accept: 'application/json' },
    });
    if (r.ok) {
      const d = await r.json();
      const hit = d?.response?.hits?.[0]?.result;
      if (hit?.url) {
        const page = await fetch(CORS + encodeURIComponent(hit.url));
        if (page.ok) {
          const html = await page.text();
          const lyrics = extractGeniusLyrics(html);
          if (lyrics) {
            return { lyrics, source: 'genius', synced: null, geniusUrl: hit.url };
          }
        }
      }
    }
  } catch (_) {}

  // LLM fallback handled by caller
  return null;
}

/**
 * Genius search — returns [{title, artist, url}] for autocomplete
 */
export async function searchGenius(query) {
  try {
    const r = await fetch(
      CORS + encodeURIComponent(`https://api.genius.com/search?q=${encodeURIComponent(query)}`),
      { headers: { Accept: 'application/json' } }
    );
    if (!r.ok) return [];
    const d = await r.json();
    return (d?.response?.hits || []).slice(0, 6).map((h) => ({
      title: h.result.title,
      artist: h.result.primary_artist.name,
      url: h.result.url,
    }));
  } catch (_) {
    return [];
  }
}

/** Parse LRC format into [{time, text}] */
export function parseLrc(lrc) {
  const lines = lrc.split('\n');
  const result = [];
  const timeRe = /\[(\d+):(\d+\.\d+)\]/g;
  for (const line of lines) {
    const text = line.replace(/\[\d+:\d+\.\d+\]/g, '').trim();
    if (!text) continue;
    let m;
    while ((m = timeRe.exec(line)) !== null) {
      result.push({ time: parseInt(m[1]) * 60 + parseFloat(m[2]), text });
    }
    timeRe.lastIndex = 0;
  }
  return result.sort((a, b) => a.time - b.time);
}

function lrcToPlain(parsed) {
  return parsed.map((l) => l.text).join('\n');
}

function extractGeniusLyrics(html) {
  const div = document.createElement('div');
  div.innerHTML = html;
  // Genius uses data-lyrics-container attribute
  const containers = div.querySelectorAll('[data-lyrics-container="true"]');
  if (containers.length) {
    return Array.from(containers)
      .map((c) => {
        // replace <br> with newline
        c.querySelectorAll('br').forEach((br) => br.replaceWith('\n'));
        return c.innerText || c.textContent;
      })
      .join('\n')
      .trim();
  }
  // fallback: look for .lyrics class
  const lyricsEl = div.querySelector('.lyrics');
  if (lyricsEl) return (lyricsEl.innerText || lyricsEl.textContent || '').trim();
  return null;
}
