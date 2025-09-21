import axios from 'axios'

// In browser: use same-origin ('') so Vite proxy works; in SSR/node: use env or localhost
const isBrowser = typeof window !== 'undefined'
const baseURL = isBrowser ? '' : ((import.meta as any).env?.VITE_API_BASE || 'http://127.0.0.1:8000')

export const api = axios.create({ baseURL })
