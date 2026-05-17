/**
 * API Configuration
 * 
 * In development, we use the local FastAPI server (http://localhost:8000).
 * In production (Vercel), all /api/* requests are proxied to the Vultr backend
 * via vercel.json rewrites — so we use a relative path '' to avoid Mixed Content errors.
 */

const getApiBaseUrl = () => {
  // Use VITE_API_URL if explicitly provided (e.g. in local .env)
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl) return envUrl;

  // In dev mode, point directly to local backend
  if (import.meta.env.DEV) return 'http://localhost:8000';

  // In production (HTTPS on Vercel), always use relative path ''
  // so requests go through vercel.json proxy rewrites → Vultr backend
  return '';
};

export const API_BASE_URL = getApiBaseUrl();

// Helper to construct API endpoints
export const apiPath = (path: string) => {
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  return `${API_BASE_URL}${cleanPath}`;
};
