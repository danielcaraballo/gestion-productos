import { defineConfig } from 'vite';

export default defineConfig({
  base: '/',
  build: {
    outDir: 'dist',
  },
  server: {
    historyApiFallback: true,  // Maneja las rutas para la SPA
  }
});
