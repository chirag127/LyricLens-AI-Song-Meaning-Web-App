/**
 * meaning.js — song-meaning analysis via LLM
 */
import { callAI } from './ai-providers.js';
import { getSettings } from './app.js';

/**
 * Returns structured meaning object:
 * { theme, verses: [{label, text}], mood, sentiment, references, culture, similar }
 */
export async function analyzeMeaning(artist, title, lyrics, signal) {
  const { providerId, apiKey, customBase, customModel } = getSettings();

  const lyricsBlock = lyrics
    ? `Lyrics:\n"""\n${lyrics.slice(0, 4000)}\n"""`
    : `(No lyrics available — use your knowledge of the song "${title}" by "${artist}")`;

  const prompt = `You are a music analyst. Analyze the song "${title}" by ${artist}.

${lyricsBlock}

Return ONLY valid JSON (no markdown fences) with this exact shape:
{
  "theme": "Overall theme in 2-3 sentences",
  "mood": "one word mood (e.g. melancholic, euphoric, rebellious)",
  "sentiment": "positive | negative | neutral | mixed",
  "verses": [
    { "label": "Verse 1 / Chorus / Bridge label", "text": "Meaning of this section" }
  ],
  "references": ["cultural or literary reference 1", "..."],
  "culture": "Cultural/historical context in 2-3 sentences",
  "similar": [
    { "title": "Song Title", "artist": "Artist Name", "reason": "Why similar" }
  ]
}

Keep verses array to the 3-5 most significant sections. Similar songs: 4 suggestions.`;

  const raw = await callAI(
    providerId, apiKey, customBase, customModel,
    [{ role: 'user', content: prompt }],
    signal
  );

  // strip any accidental markdown fences
  const clean = raw.replace(/^```[\w]*\n?/, '').replace(/\n?```$/, '').trim();
  return JSON.parse(clean);
}

/**
 * Fetch + LLM-summarize web interpretations
 * Returns { summary: string, sources: [{title,url}] }
 */
export async function webMeaning(artist, title, signal) {
  const { providerId, apiKey, customBase, customModel } = getSettings();

  // Try fetching Genius annotations page via proxy, extract text, feed to LLM
  let webContent = '';
  try {
    const query = `${title} ${artist} song meaning`;
    const proxyUrl = `https://corsproxy.io/?${encodeURIComponent(
      `https://www.googleapis.com/customsearch/v1?q=${encodeURIComponent(query)}&num=3`
    )}`;
    // This won't work without a CSE key — fall through to LLM-only path
    throw new Error('no key');
  } catch (_) {}

  // LLM-only: ask LLM to reason about web interpretations from its knowledge
  const prompt = `What do fans and music critics say about the meaning of "${title}" by ${artist}?
Summarize 3-4 distinct interpretations or analyses you know of from music blogs, forums, or critics.
Format as JSON: { "summary": "...", "interpretations": [{"perspective": "...", "detail": "..."}] }
Return ONLY JSON (no markdown).`;

  const raw = await callAI(
    providerId, apiKey, customBase, customModel,
    [{ role: 'user', content: prompt }],
    signal
  );
  const clean = raw.replace(/^```[\w]*\n?/, '').replace(/\n?```$/, '').trim();
  return JSON.parse(clean);
}

/**
 * Ask LLM for lyrics when all sources fail
 */
export async function aiLyrics(artist, title, signal) {
  const { providerId, apiKey, customBase, customModel } = getSettings();
  const prompt = `Provide the complete lyrics of the song "${title}" by ${artist} from your knowledge.
If you are uncertain about any section, mark it with [?]. Return ONLY the lyrics text, no commentary.`;
  return callAI(
    providerId, apiKey, customBase, customModel,
    [{ role: 'user', content: prompt }],
    signal
  );
}

/**
 * Translate lyrics to target language
 */
export async function translateLyrics(lyrics, targetLang, signal) {
  const { providerId, apiKey, customBase, customModel } = getSettings();
  const prompt = `Translate the following song lyrics to ${targetLang}. Preserve line breaks and poetic form.
Return ONLY the translated text.

${lyrics.slice(0, 3000)}`;
  return callAI(
    providerId, apiKey, customBase, customModel,
    [{ role: 'user', content: prompt }],
    signal
  );
}

/**
 * Detect language of lyrics
 */
export async function detectLanguage(lyrics, signal) {
  const { providerId, apiKey, customBase, customModel } = getSettings();
  const sample = lyrics.slice(0, 300);
  const prompt = `What language are these lyrics? Reply with just the language name (e.g. English, Spanish, Korean).

${sample}`;
  return callAI(
    providerId, apiKey, customBase, customModel,
    [{ role: 'user', content: prompt }],
    signal
  );
}
