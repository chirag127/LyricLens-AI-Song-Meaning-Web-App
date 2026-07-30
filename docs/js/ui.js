/**
 * ui.js — render, loading states, error handling
 */

export function showToast(msg, type = '') {
  const c = document.getElementById('toast-container');
  const t = document.createElement('div');
  t.className = 'toast' + (type ? ` ${type}` : '');
  t.textContent = msg;
  c.appendChild(t);
  setTimeout(() => t.remove(), 3300);
}

export function showSkeletons(container, lines = 8) {
  container.innerHTML = Array.from({ length: lines })
    .map((_, i) => {
      const w = i % 3 === 0 ? 'short' : i % 2 === 0 ? 'medium' : 'full';
      return `<div class="skeleton skel-line ${w}"></div>`;
    })
    .join('');
}

export function setLoading(btn, loading, originalText) {
  if (loading) {
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span> Loading…`;
  } else {
    btn.disabled = false;
    btn.innerHTML = originalText;
  }
}

export function renderLyrics(lyrics, synced) {
  if (synced && synced.length) {
    return `<div class="lrc-container" id="lrc-container">
      ${synced.map((l, i) =>
        `<div class="lrc-line" data-idx="${i}" data-time="${l.time}">${escHtml(l.text)}</div>`
      ).join('')}
    </div>`;
  }
  return `<div class="lyrics-plain">${escHtml(lyrics)}</div>`;
}

export function renderMeaning(m) {
  const verses = (m.verses || [])
    .map((v) => `<div class="verse-item"><div class="verse-label">${escHtml(v.label)}</div><p>${escHtml(v.text)}</p></div>`)
    .join('');

  const refs = (m.references || [])
    .map((r) => `<li>${escHtml(r)}</li>`)
    .join('');

  const similar = (m.similar || [])
    .map((s) => `<div class="similar-item" data-title="${escAttr(s.title)}" data-artist="${escAttr(s.artist)}">
      <div><div class="sim-title">${escHtml(s.title)}</div><div class="sim-artist">${escHtml(s.artist)}</div></div>
      <small class="text-muted">${escHtml(s.reason || '')}</small>
    </div>`)
    .join('');

  return `
    <div class="meaning-card">
      <div class="meaning-section">
        <h3>Overall Theme</h3>
        <p>${escHtml(m.theme || '')}</p>
      </div>
      ${verses ? `<div class="meaning-section"><h3>Breakdown</h3>${verses}</div>` : ''}
      ${refs ? `<div class="meaning-section"><h3>References &amp; Allusions</h3><ul>${refs}</ul></div>` : ''}
      ${m.culture ? `<div class="meaning-section"><h3>Cultural Context</h3><p>${escHtml(m.culture)}</p></div>` : ''}
      ${similar ? `<div class="meaning-section"><h3>Similar Songs</h3><div class="similar-list">${similar}</div></div>` : ''}
    </div>`;
}

export function renderWebMeaning(data) {
  if (!data) return '<p class="text-muted">No web results available.</p>';
  const interps = (data.interpretations || [])
    .map((i) => `<div class="web-result-card"><h4>${escHtml(i.perspective || '')}</h4><p>${escHtml(i.detail || '')}</p></div>`)
    .join('');
  return `
    <div class="meaning-section" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;">
      <div style="padding:1.25rem 1.5rem;border-bottom:1px solid var(--border)">
        <h3 style="font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin-bottom:.6rem">AI Summary</h3>
        <p style="color:var(--text2);font-size:.95rem;line-height:1.7">${escHtml(data.summary || '')}</p>
      </div>
      ${interps ? `<div style="padding:1.25rem 1.5rem"><h3 style="font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin-bottom:.75rem">Interpretations</h3><div class="web-results">${interps}</div></div>` : ''}
    </div>`;
}

export function moodColor(mood) {
  const map = {
    melancholic: '#60a5fa', sad: '#60a5fa', dark: '#8b5cf6',
    euphoric: '#fbbf24', happy: '#34d399', joyful: '#34d399',
    angry: '#f87171', rebellious: '#f87171',
    romantic: '#f472b6', love: '#f472b6',
    nostalgic: '#a78bfa', reflective: '#a78bfa',
  };
  const key = (mood || '').toLowerCase();
  for (const [k, v] of Object.entries(map)) {
    if (key.includes(k)) return v;
  }
  return 'var(--accent)';
}

export function escHtml(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function escAttr(s) { return escHtml(s); }
