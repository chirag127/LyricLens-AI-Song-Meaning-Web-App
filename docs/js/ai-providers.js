/**
 * ai-providers.js — multi-provider AI abstraction
 * Free default: Pollinations (no key).
 * Paid/keyed: Groq, Cerebras, Gemini, OpenRouter, Mistral, custom OpenAI-compat.
 */

const PROVIDERS = {
  pollinations: {
    label: 'Pollinations (free, no key)',
    baseUrl: 'https://text.pollinations.ai/openai',
    model: 'openai',
    requiresKey: false,
  },
  groq: {
    label: 'Groq',
    baseUrl: 'https://api.groq.com/openai/v1',
    model: 'llama-3.3-70b-versatile',
    requiresKey: true,
  },
  cerebras: {
    label: 'Cerebras',
    baseUrl: 'https://api.cerebras.ai/v1',
    model: 'llama3.1-70b',
    requiresKey: true,
  },
  gemini: {
    label: 'Google Gemini',
    baseUrl: 'https://generativelanguage.googleapis.com/v1beta/openai',
    model: 'gemini-2.0-flash',
    requiresKey: true,
  },
  openrouter: {
    label: 'OpenRouter',
    baseUrl: 'https://openrouter.ai/api/v1',
    model: 'google/gemma-3-27b-it:free',
    requiresKey: true,
  },
  mistral: {
    label: 'Mistral',
    baseUrl: 'https://api.mistral.ai/v1',
    model: 'mistral-small-latest',
    requiresKey: true,
  },
  custom: {
    label: 'Custom (OpenAI-compat)',
    baseUrl: '',
    model: '',
    requiresKey: false,
  },
};

export function getProviderList() {
  return Object.entries(PROVIDERS).map(([id, p]) => ({ id, ...p }));
}

export function getProviderInfo(id) {
  return PROVIDERS[id] || PROVIDERS.pollinations;
}

/**
 * @param {string} providerId
 * @param {string} apiKey
 * @param {string} customBase
 * @param {string} customModel
 * @param {{ role:string, content:string }[]} messages
 * @param {AbortSignal} [signal]
 * @returns {Promise<string>}
 */
export async function callAI(providerId, apiKey, customBase, customModel, messages, signal) {
  const p = PROVIDERS[providerId] || PROVIDERS.pollinations;
  const baseUrl = providerId === 'custom' ? customBase : p.baseUrl;
  const model = providerId === 'custom' ? customModel : p.model;

  const headers = { 'Content-Type': 'application/json' };
  if (apiKey) headers['Authorization'] = `Bearer ${apiKey}`;

  const body = JSON.stringify({ model, messages, temperature: 0.7, max_tokens: 2048 });

  const r = await fetch(`${baseUrl}/chat/completions`, { method: 'POST', headers, body, signal });

  if (!r.ok) {
    const err = await r.text().catch(() => r.statusText);
    throw new Error(`AI error ${r.status}: ${err}`);
  }
  const d = await r.json();
  return d.choices?.[0]?.message?.content?.trim() || '';
}
