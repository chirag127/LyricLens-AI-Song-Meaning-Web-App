# LyricLens

[![Stars](https://img.shields.io/github/stars/chirag127/LyricLens-AI-Song-Meaning-Web-App?style=flat-square)](https://github.com/chirag127/LyricLens-AI-Song-Meaning-Web-App/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

**Live app: [lyriclens.oriz.in](https://lyriclens.oriz.in)**

Client-side AI song-meaning + multi-source lyrics web app. Searches lyrics.ovh, LRCLIB, Genius, and LLM knowledge; explains meanings with verse-by-verse breakdowns; searches the web for fan interpretations. 100% client-side — your API keys never leave your browser.

---

## Features

- **Multi-source lyrics** — queries lyrics.ovh, LRCLIB, Genius (via CORS proxy), then LLM knowledge as fallback; shows which source delivered the result
- **Synced lyrics** — if LRCLIB returns an LRC file, lyrics highlight line-by-line
- **Explain meaning** — one click: overall theme, verse-by-verse breakdown, mood/sentiment badge, cultural references, allusions
- **Web analysis** — automates fan/critic interpretation lookup; summarizes via LLM; falls back to Google search if blocked
- **Similar songs** — LLM suggests 4 related songs; click any to search instantly
- **Language detection** — auto-detects lyrics language; badge in UI
- **Translate lyrics** — translate to any language via LLM (prompt for target language)
- **Autocomplete** — Genius-powered song/artist suggestions as you type
- **Recent searches** — last 20 searches stored in localStorage
- **Favorites** — save/unsave songs; persisted in localStorage
- **Share link** — URL params `?artist=&title=` for direct deep links; copy link button
- **Copy lyrics** — one-click clipboard copy
- **Dark/light theme** — toggle + persisted preference
- **Settings panel** — pick AI provider + API key (stored locally only) + optional Genius token
- **Keyboard shortcuts** — `Ctrl+K` focuses search; `Esc` closes panels
- **Loading skeletons** + graceful error toasts
- **Responsive** — mobile-first design

---

## AI providers

| Provider | Free? | Key required |
|---|---|---|
| **Pollinations** | Yes (default) | No |
| Groq | Free tier | Yes |
| Cerebras | Free tier | Yes |
| Google Gemini | Free tier | Yes |
| OpenRouter | Free models | Yes |
| Mistral | Free tier | Yes |
| Custom OpenAI-compat | — | Optional |

Configure in Settings (gear icon). Keys stored in `localStorage` only.

---

## How multi-source lyrics works

1. **lyrics.ovh** — free, no key, CORS-ok
2. **LRCLIB** — free, no key, returns synced (LRC) + plain lyrics
3. **Genius** — public search + page scrape via `corsproxy.io`; add a Genius client token in Settings for better results
4. **LLM knowledge fallback** — if all sources fail, asks the selected AI for lyrics from its training data (labeled "AI knowledge")

---

## Privacy

- Zero backend. No server receives your queries or keys.
- API keys stored in browser `localStorage`. Clear site data to remove.
- Lyrics fetched directly from public APIs from your browser.

---

## Dataset

The original scraped lyrics dataset (CSV + per-song txt files, ~24 MB) has been moved out of the repo to keep it lean.

[Download dataset (GitHub Releases)](https://github.com/chirag127/LyricLens-AI-Song-Meaning-Web-App/releases/tag/dataset-v1)

---

## Scripts (optional data tooling)

`scripts/` contains the original Python scrapers, cleaned up and env-var'd:

```bash
GENIUS_TOKEN=your_token ARTIST="Taylor Swift" python scripts/genius_api.py
OPENAI_API_KEY=sk-... SONG="Bohemian Rhapsody" ARTIST="Queen" python scripts/cgpt.py
```

These are standalone data-generation tools, not part of the web app.

---

## License

MIT
