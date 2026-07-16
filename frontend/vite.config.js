import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Base path matches the GitHub Pages site (https://<user>.github.io/geo-ml/).
// In dev (`npm run dev`) Vite ignores the base prefix.
export default defineConfig({
  base: '/geo-ml/',
  plugins: [react()],
  optimizeDeps: {
    // onnxruntime-web ships its own WASM - leave it untouched at bundle time.
    exclude: ['onnxruntime-web']
  }
})
