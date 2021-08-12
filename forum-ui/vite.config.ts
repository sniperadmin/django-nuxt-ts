import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

// https://vitejs.dev/config/
export default ({ mode }) => {
  import.meta.env = { ...loadEnv(mode, process.cwd()) }

  return defineConfig({
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    plugins: [vue()],
    server: {
      cors: true,
      port: 4000,
      strictPort: true,
    }
  })
}
