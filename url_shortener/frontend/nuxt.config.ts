// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      SHORTENER_SERVICE_URL: process.env.NUXT_PUBLIC_SHORTENER_SERVICE_URL || 'http://localhost:8000',
      REDIRECT_SERVICE_URL: process.env.NUXT_PUBLIC_REDIRECT_SERVICE_URL || 'http://localhost:8001'
    }
  },

  modules: ['@nuxtjs/tailwindcss']
})