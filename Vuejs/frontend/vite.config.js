import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: fileURLToPath(new URL('../backend/static/dist', import.meta.url)),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL('./src/main.js', import.meta.url)),
      },
      // output: {
      //   // chunkFileNames: undefined,
      //   assetFileNames: (assetInfo) => {
      //     let [name, extType] = assetInfo.name.split('.');
      //     if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
      //       return `static/[name]-[hash][extname]`;
      //     }
      //     if (/css|js/i.test(extType) && name !== "main") {
      //       return `static/[name]-[hash][extname]`;
      //     }
      //     return `[name]-[hash][extname]`;
      //   },
      // },
    },
    modulePreload: false
  },
})
