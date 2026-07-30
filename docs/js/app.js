/**
 * app.js — UI orchestration + state + localStorage
 */
import { fetchLyrics, searchGenius, parseLrc, SOURCE_LABELS } from './lyrics-sources.js';
import { getProviderList, getProviderInfo } from './ai-providers.js';
import { analyzeMeaning, webMeaning, aiLyrics, translateLyrics, detectLanguage } from './meaning.js';
import {
  showToast, showSkeletons, setLoading, renderLyrics, renderMeaning,
  renderWebMeaning, moodColor, escHtml
} from './ui.js';

// ── State ────────────────────────────────────────────────────────────────────
let state = {
  artist: '', title: '',
  lyrics: null, synced: null, source: null,
  meaning: null, webMeaningData: null,
  lang: null,
  translatedLyrics: null,
  activeTab: 'lyrics',
  lrcTimer: null,
  abortCtrl: null,
};

// ── Settings (localStorage) ──────────────────────────────────────────────────
const SETTINGS_KEY = 'lyriclens_settings';

export function getSettings() {
  try {
    return JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}');
  } catch (_) { return {}; }
}

function saveSettings(obj) {
  const cur = getSettings();
  localStorage.setItem(SETTINGS_KEY, JSON.stringify({ ...cur, ...obj }));
}

// ── Recent / Favorites ───────────────────────────────────────────────────────
function getList(key) {
  try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch (_) { return []; }
}
function saveList(key, arr) { localStorage.setItem(key, JSON.stringify(arr)); }

function addRecent(artist, title) {
  const list = getList('ll_recent').filter(
    (x) => !(x.artist === artist && x.title === title)
  );
  list.unshift({ artist, title, ts: Date.now() });
  saveList('ll_recent', list.slice(0, 20));
}

function isFav(artist, title) {
  return getList('ll_favs').some((x) => x.artist === artist && x.title === title);
}

function toggleFav(artist, title) {
  const list = getList('ll_favs');
  const idx = list.findIndex((x) => x.artist === artist && x.title === title);
  if (idx >= 0) { list.splice(idx, 1); } else { list.unshift({ artist, title }); }
  saveList('ll_favs', list);
  renderHomeLists();
  updateFavBtn();
}

// ── DOM refs ─────────────────────────────────────────────────────────────────
const $ = (sel) => document.querySelector(sel);
const artistInput = () => $('#artist-input');
const titleInput = () => $('#title-input');
const searchBtn = () => $('#search-btn');
const resultArea = () => $('#result-area');
const homeLists = () => $('#home-lists');

// ── Boot ─────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  populateProviders();
  loadSettingsIntoPanel();
  renderHomeLists();
  checkUrlParams();
  bindEvents();
});

// ── URL params (share link) ───────────────────────────────────────────────────
function checkUrlParams() {
  const p = new URLSearchParams(location.search);
  const a = p.get('artist'), t = p.get('title');
  if (a && t) {
    artistInput().value = a;
    titleInput().value = t;
    const banner = $('#share-banner');
    if (banner) {
      banner.querySelector('.share-info').textContent = `Shared: "${t}" by ${a}`;
      banner.classList.add('visible');
    }
    doSearch(a, t);
  }
}

// ── Autocomplete ─────────────────────────────────────────────────────────────
let acTimer = null;

function bindAutocomplete(input) {
  input.addEventListener('input', () => {
    clearTimeout(acTimer);
    const q = (artistInput().value + ' ' + titleInput().value).trim();
    if (q.length < 3) { closeAC(input); return; }
    acTimer = setTimeout(() => runAC(input, q), 350);
  });
  input.addEventListener('keydown', (e) => {
    const list = input.parentElement.querySelector('.autocomplete-list');
    if (!list) return;
    const items = list.querySelectorAll('.autocomplete-item');
    let active = list.querySelector('.autocomplete-item.active');
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (!active) { items[0]?.classList.add('active'); }
      else {
        active.classList.remove('active');
        const next = active.nextElementSibling;
        if (next) next.classList.add('active');
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (active) {
        active.classList.remove('active');
        const prev = active.previousElementSibling;
        if (prev) prev.classList.add('active');
      }
    } else if (e.key === 'Enter') {
      if (active) { e.preventDefault(); active.click(); }
    } else if (e.key === 'Escape') { closeAC(input); }
  });
  input.addEventListener('blur', () => setTimeout(() => closeAC(input), 200));
}

async function runAC(input, q) {
  const results = await searchGenius(q);
  if (!results.length) { closeAC(input); return; }
  let list = input.parentElement.querySelector('.autocomplete-list');
  if (!list) {
    list = document.createElement('div');
    list.className = 'autocomplete-list';
    input.parentElement.appendChild(list);
  }
  list.innerHTML = results.map((r) => `
    <div class="autocomplete-item" data-title="${escHtml(r.title)}" data-artist="${escHtml(r.artist)}">
      <div><div class="autocomplete-title">${escHtml(r.title)}</div>
      <div class="autocomplete-artist">${escHtml(r.artist)}</div></div>
    </div>`).join('');
  list.querySelectorAll('.autocomplete-item').forEach((item) => {
    item.addEventListener('click', () => {
      titleInput().value = item.dataset.title;
      artistInput().value = item.dataset.artist;
      closeAC(input);
      doSearch(item.dataset.artist, item.dataset.title);
    });
  });
}

function closeAC(input) {
  input?.parentElement?.querySelector('.autocomplete-list')?.remove();
}

// ── Events ────────────────────────────────────────────────────────────────────
function bindEvents() {
  bindAutocomplete(artistInput());
  bindAutocomplete(titleInput());

  searchBtn().addEventListener('click', () => {
    const a = artistInput().value.trim();
    const t = titleInput().value.trim();
    if (!a || !t) { showToast('Enter artist and title', 'error'); return; }
    doSearch(a, t);
  });

  [artistInput(), titleInput()].forEach((inp) => {
    inp.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') searchBtn().click();
    });
  });

  // Tab switching
  document.addEventListener('click', (e) => {
    const tb = e.target.closest('.tab-btn');
    if (tb) {
      document.querySelectorAll('.tab-btn').forEach((b) => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach((p) => p.classList.remove('active'));
      tb.classList.add('active');
      document.getElementById(tb.dataset.panel)?.classList.add('active');
      state.activeTab = tb.dataset.panel;
    }
  });

  // Meaning btn
  document.addEventListener('click', (e) => {
    if (e.target.closest('#explain-btn')) doExplainMeaning();
    if (e.target.closest('#web-meaning-btn')) doWebMeaning();
    if (e.target.closest('#copy-btn')) copyLyrics();
    if (e.target.closest('#share-btn')) shareLink();
    if (e.target.closest('#fav-btn')) toggleFav(state.artist, state.title);
    if (e.target.closest('#translate-btn')) doTranslate();
  });

  // Similar song click
  document.addEventListener('click', (e) => {
    const item = e.target.closest('.similar-item');
    if (item) {
      artistInput().value = item.dataset.artist;
      titleInput().value = item.dataset.title;
      doSearch(item.dataset.artist, item.dataset.title);
    }
  });

  // Theme toggle
  $('#theme-toggle')?.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next === 'dark' ? '' : 'light');
    saveSettings({ theme: next });
  });

  // Settings
  $('#settings-btn')?.addEventListener('click', () => {
    $('#settings-overlay')?.classList.add('open');
  });
  $('#settings-overlay')?.addEventListener('click', (e) => {
    if (e.target === e.currentTarget) e.currentTarget.classList.remove('open');
  });
  $('#settings-close')?.addEventListener('click', () => {
    $('#settings-overlay')?.classList.remove('open');
  });
  $('#settings-form')?.addEventListener('change', saveSettingsFromForm);
  $('#settings-form')?.addEventListener('input', saveSettingsFromForm);

  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      titleInput().focus();
      titleInput().select();
    }
    if (e.key === 'Escape') {
      $('#settings-overlay')?.classList.remove('open');
    }
  });

  // Apply saved theme
  const { theme } = getSettings();
  if (theme === 'light') document.documentElement.setAttribute('data-theme', 'light');
}

// ── Settings form ─────────────────────────────────────────────────────────────
function populateProviders() {
  const sel = document.getElementById('provider-select');
  if (!sel) return;
  getProviderList().forEach(({ id, label }) => {
    const opt = document.createElement('option');
    opt.value = id; opt.textContent = label;
    sel.appendChild(opt);
  });
}

function loadSettingsIntoPanel() {
  const s = getSettings();
  const sel = document.getElementById('provider-select');
  if (sel && s.providerId) sel.value = s.providerId;
  const keyInp = document.getElementById('api-key-input');
  if (keyInp && s.apiKey) keyInp.value = s.apiKey;
  const baseInp = document.getElementById('custom-base-input');
  if (baseInp && s.customBase) baseInp.value = s.customBase;
  const modelInp = document.getElementById('custom-model-input');
  if (modelInp && s.customModel) modelInp.value = s.customModel;
  const geniusInp = document.getElementById('genius-key-input');
  if (geniusInp && s.geniusKey) geniusInp.value = s.geniusKey;
}

function saveSettingsFromForm() {
  const s = {
    providerId: document.getElementById('provider-select')?.value,
    apiKey: document.getElementById('api-key-input')?.value,
    customBase: document.getElementById('custom-base-input')?.value,
    customModel: document.getElementById('custom-model-input')?.value,
    geniusKey: document.getElementById('genius-key-input')?.value,
  };
  saveSettings(s);
}

// ── Main search ───────────────────────────────────────────────────────────────
async function doSearch(artist, title) {
  if (state.abortCtrl) state.abortCtrl.abort();
  state.abortCtrl = new AbortController();

  state.artist = artist; state.title = title;
  state.lyrics = null; state.synced = null; state.source = null;
  state.meaning = null; state.webMeaningData = null;
  state.lang = null; state.translatedLyrics = null;

  // update URL
  const url = new URL(location.href);
  url.searchParams.set('artist', artist);
  url.searchParams.set('title', title);
  history.replaceState({}, '', url);

  addRecent(artist, title);
  renderHomeLists();

  const area = resultArea();
  area.innerHTML = '';
  area.classList.remove('hidden');

  // show skeleton
  area.innerHTML = `
    <div class="result-header">
      <div class="song-info">
        <div class="skeleton skel-line medium" style="height:2rem;margin-bottom:.5rem"></div>
        <div class="skeleton skel-line short" style="height:1rem"></div>
      </div>
    </div>
    <div class="lyrics-view">${Array.from({length:12}).map((_,i)=>`<div class="skeleton skel-line ${i%3===0?'short':i%2===0?'medium':'full'}"></div>`).join('')}</div>`;

  setLoading(searchBtn(), true, `<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/></svg> Search`);

  try {
    let result = await fetchLyrics(artist, title);

    if (!result) {
      // LLM fallback
      showToast('No lyrics source found — asking AI…');
      try {
        const text = await aiLyrics(artist, title, state.abortCtrl.signal);
        result = { lyrics: text, source: 'ai', synced: null };
      } catch (err) {
        if (err.name === 'AbortError') return;
        showToast('Could not fetch lyrics', 'error');
        area.innerHTML = `<div class="lyrics-view"><p class="text-muted">No lyrics found for "${title}" by ${artist}.</p></div>`;
        return;
      }
    }

    state.lyrics = result.lyrics;
    state.synced = result.synced;
    state.source = result.source;

    // detect lang async (no await — non-blocking)
    detectLanguage(result.lyrics, state.abortCtrl.signal)
      .then((lang) => {
        state.lang = lang;
        const el = document.getElementById('lang-badge');
        if (el) el.textContent = lang;
      })
      .catch(() => {});

    renderResult();
  } catch (err) {
    if (err.name === 'AbortError') return;
    showToast('Search failed: ' + err.message, 'error');
  } finally {
    setLoading(searchBtn(), false, `<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4-816A6 6 0 012 8z" clip-rule="evenodd"/></svg> Search`);
    setLoading(searchBtn(), false, `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/></svg> Search`);
  }
}

function renderResult() {
  const { artist, title, lyrics, synced, source } = state;
  const area = resultArea();

  const sourceLabel = SOURCE_LABELS[source] || source;
  const isAI = source === 'ai';

  area.innerHTML = `
    <div class="share-banner" id="share-banner">
      <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z"/></svg>
      <span class="share-info"></span>
    </div>
    <div class="result-header">
      <div class="song-info">
        <h2>${escHtml(title)}</h2>
        <div class="artist-name">${escHtml(artist)}</div>
        <div class="badge-row">
          <span class="badge ${isAI ? 'badge-ai' : 'badge-source'}">${escHtml(sourceLabel)}</span>
          <span class="badge badge-mood" id="mood-badge" style="display:none"></span>
          <span class="badge badge-lang" id="lang-badge" style="display:none"></span>
        </div>
      </div>
      <div class="result-actions">
        <button class="btn-icon" id="fav-btn" title="Favorite">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"/></svg>
          Save
        </button>
        <button class="btn-icon" id="copy-btn" title="Copy lyrics (Alt+C)">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"/><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"/></svg>
          Copy
        </button>
        <button class="btn-icon" id="share-btn" title="Share link">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z"/></svg>
          Share
        </button>
        <button class="btn-icon" id="translate-btn" title="Translate lyrics">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7 2a1 1 0 011 1v1h3a1 1 0 110 2H9.578a18.87 18.87 0 01-1.724 4.153c.254.212.502.431.743.657a1 1 0 01-1.364 1.463 17.96 17.96 0 00-.573-.514A18.832 18.832 0 013.33 14.58a1 1 0 01-1.26-1.551A16.833 16.833 0 005.593 10.5a17.01 17.01 0 01-1.385-2.48 1 1 0 011.832-.802c.3.686.659 1.348 1.07 1.973A16.87 16.87 0 009.5 6H3a1 1 0 110-2h3V3a1 1 0 011-1zm6 6a1 1 0 01.894.553l2.991 5.982a.869.869 0 01.02.037l.99 1.98a1 1 0 11-1.79.895L15.383 16h-4.764l-.724 1.447a1 1 0 11-1.788-.894l.99-1.98.019-.038 2.99-5.982A1 1 0 0113 8zm-1.382 6h2.764L13 11.236 11.618 14z" clip-rule="evenodd"/></svg>
          Translate
        </button>
      </div>
    </div>

    <div class="tab-bar">
      <button class="tab-btn active" data-panel="panel-lyrics">Lyrics</button>
      <button class="tab-btn" data-panel="panel-meaning">Meaning</button>
      <button class="tab-btn" data-panel="panel-web">Web Analysis</button>
    </div>

    <div id="panel-lyrics" class="tab-panel active">
      <div class="lyrics-view">
        ${renderLyrics(lyrics, synced)}
      </div>
      <div id="translation-area"></div>
    </div>

    <div id="panel-meaning" class="tab-panel">
      <div class="flex gap-2 mt-2" style="margin-bottom:1rem">
        <button class="btn-primary" id="explain-btn" style="width:auto;padding:.6rem 1.4rem">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"/></svg>
          Explain Meaning
        </button>
      </div>
      <div id="meaning-content"></div>
    </div>

    <div id="panel-web" class="tab-panel">
      <div class="flex gap-2 mt-2" style="margin-bottom:1rem">
        <button class="btn-primary" id="web-meaning-btn" style="width:auto;padding:.6rem 1.4rem">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z" clip-rule="evenodd"/></svg>
          Search Web Meanings
        </button>
      </div>
      <div id="web-meaning-content"></div>
    </div>`;

  updateFavBtn();
  initLrcSync();
}

// ── Fav button ────────────────────────────────────────────────────────────────
function updateFavBtn() {
  const btn = document.getElementById('fav-btn');
  if (!btn) return;
  btn.classList.toggle('is-fav', isFav(state.artist, state.title));
}

// ── Synced lyrics ──────────────────────────────────────────────────────────────
function initLrcSync() {
  if (!state.synced) return;
  const audio = new Audio();
  // No audio source — just demonstrate time-based sync via play
  // User can interact with lines manually
  document.querySelectorAll('.lrc-line').forEach((line) => {
    line.addEventListener('click', () => {
      document.querySelectorAll('.lrc-line').forEach((l) => l.classList.remove('lrc-active'));
      line.classList.add('lrc-active');
    });
  });
}

// ── Meaning ───────────────────────────────────────────────────────────────────
async function doExplainMeaning() {
  const btn = document.getElementById('explain-btn');
  if (!btn) return;
  const orig = btn.innerHTML;
  setLoading(btn, true, orig);

  try {
    const m = await analyzeMeaning(state.artist, state.title, state.lyrics, state.abortCtrl?.signal);
    state.meaning = m;

    const moodBadge = document.getElementById('mood-badge');
    if (moodBadge && m.mood) {
      moodBadge.textContent = m.mood;
      moodBadge.style.display = '';
      moodBadge.style.background = moodColor(m.mood) + '22';
      moodBadge.style.color = moodColor(m.mood);
      moodBadge.style.borderColor = moodColor(m.mood) + '55';
    }

    document.getElementById('meaning-content').innerHTML = renderMeaning(m);
    showToast('Meaning analyzed', 'success');
  } catch (err) {
    if (err.name === 'AbortError') return;
    showToast('Analysis failed: ' + err.message, 'error');
    document.getElementById('meaning-content').innerHTML =
      `<p class="text-muted">Could not analyze meaning. Check AI provider settings.</p>`;
  } finally {
    setLoading(btn, false, orig);
  }
}

async function doWebMeaning() {
  const btn = document.getElementById('web-meaning-btn');
  if (!btn) return;
  const orig = btn.innerHTML;
  setLoading(btn, true, orig);
  const container = document.getElementById('web-meaning-content');
  showSkeletons(container, 5);

  try {
    const data = await webMeaning(state.artist, state.title, state.abortCtrl?.signal);
    state.webMeaningData = data;
    container.innerHTML = renderWebMeaning(data);
    showToast('Web analysis complete', 'success');
  } catch (err) {
    if (err.name === 'AbortError') return;
    // fallback: open Google search
    const q = encodeURIComponent(`${state.title} ${state.artist} meaning`);
    container.innerHTML = `<div class="text-muted" style="padding:1rem">
      AI web analysis failed.
      <a href="https://www.google.com/search?q=${q}" target="_blank" rel="noopener" style="color:var(--accent)">Open Google search</a>
    </div>`;
    showToast('Opening Google search as fallback', 'error');
  } finally {
    setLoading(btn, false, orig);
  }
}

// ── Translate ─────────────────────────────────────────────────────────────────
async function doTranslate() {
  const btn = document.getElementById('translate-btn');
  if (!btn || !state.lyrics) { showToast('Search for a song first', 'error'); return; }

  const lang = prompt('Translate to language (e.g. Spanish, Hindi, French):');
  if (!lang) return;

  const orig = btn.innerHTML;
  setLoading(btn, true, orig);

  try {
    const translated = await translateLyrics(state.lyrics, lang, state.abortCtrl?.signal);
    state.translatedLyrics = translated;
    const area = document.getElementById('translation-area');
    area.innerHTML = `<div class="translation-panel">
      <h4>Translation — ${escHtml(lang)}</h4>
      <div class="translated-text">${escHtml(translated)}</div>
    </div>`;
    showToast('Translation complete', 'success');
  } catch (err) {
    showToast('Translation failed: ' + err.message, 'error');
  } finally {
    setLoading(btn, false, orig);
  }
}

// ── Copy ──────────────────────────────────────────────────────────────────────
function copyLyrics() {
  if (!state.lyrics) return;
  navigator.clipboard.writeText(state.lyrics).then(() => showToast('Lyrics copied', 'success'));
}

// ── Share ─────────────────────────────────────────────────────────────────────
function shareLink() {
  const url = new URL(location.href);
  url.searchParams.set('artist', state.artist);
  url.searchParams.set('title', state.title);
  navigator.clipboard.writeText(url.toString()).then(() => showToast('Link copied', 'success'));
}

// ── Home lists ────────────────────────────────────────────────────────────────
function renderHomeLists() {
  const el = homeLists();
  if (!el) return;

  const recent = getList('ll_recent');
  const favs = getList('ll_favs');

  let html = '';

  if (favs.length) {
    html += `<div class="section-header mt-6"><h2>Favorites</h2>
      <button class="btn-icon" id="clear-favs-btn">Clear all</button></div>
      <div class="cards-grid">
        ${favs.slice(0, 8).map((x) => `
          <div class="mini-card" data-artist="${escHtml(x.artist)}" data-title="${escHtml(x.title)}">
            <button class="mc-del" data-artist="${escHtml(x.artist)}" data-title="${escHtml(x.title)}" title="Remove">x</button>
            <div class="mc-title">${escHtml(x.title)}</div>
            <div class="mc-artist">${escHtml(x.artist)}</div>
          </div>`).join('')}
      </div>`;
  }

  if (recent.length) {
    html += `<div class="section-header mt-6"><h2>Recent</h2>
      <button class="btn-icon" id="clear-recent-btn">Clear</button></div>
      <div class="cards-grid">
        ${recent.slice(0, 8).map((x) => `
          <div class="mini-card" data-artist="${escHtml(x.artist)}" data-title="${escHtml(x.title)}">
            <div class="mc-title">${escHtml(x.title)}</div>
            <div class="mc-artist">${escHtml(x.artist)}</div>
          </div>`).join('')}
      </div>`;
  }

  el.innerHTML = html;

  el.querySelectorAll('.mini-card').forEach((c) => {
    c.addEventListener('click', (e) => {
      if (e.target.closest('.mc-del')) return;
      artistInput().value = c.dataset.artist;
      titleInput().value = c.dataset.title;
      doSearch(c.dataset.artist, c.dataset.title);
    });
  });

  el.querySelectorAll('.mc-del').forEach((b) => {
    b.addEventListener('click', (e) => {
      e.stopPropagation();
      const list = getList('ll_favs').filter(
        (x) => !(x.artist === b.dataset.artist && x.title === b.dataset.title)
      );
      saveList('ll_favs', list);
      renderHomeLists();
    });
  });

  document.getElementById('clear-favs-btn')?.addEventListener('click', () => {
    saveList('ll_favs', []);
    renderHomeLists();
  });
  document.getElementById('clear-recent-btn')?.addEventListener('click', () => {
    saveList('ll_recent', []);
    renderHomeLists();
  });
}
