import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  // base: "/static/",
  build: {
    manifest: true,
    outDir: fileURLToPath(new URL('../tutorial/static/', import.meta.url)),
    rollupOptions: {
      input: './index.html',
    }
  }
})

// const { resolve } = require('path');

// module.exports = {
//    plugins: [
//     vue(),
//     vueJsx(),
//   ],
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     },
//     // extensions: ['.js', '.json'],
//   },
//   server: {
//     host: 'localhost',
//     port: 3000,
//     open: false,
//     watch: {
//       usePolling: true,
//       disableGlobbing: false,
//     },
//   },
//   // resolve: {
//   //   extensions: ['.js', '.json'],
//   // },
//   build: {
//     outDir: resolve('../tutorial/static/dist'),
//     assetsDir: '',
//     manifest: true,
//     emptyOutDir: true,
//     target: 'es2015',
//     // rollupOptions: {
//     //   input: {
//     //     main: resolve('./static/src/js/main.js'),
//     //   },
//     //   output: {
//     //     chunkFileNames: undefined,
//     //   },
//     // },
//   },
// };
