import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/um_safe_computing_data_scraping",
  plugins: [react()],
});
