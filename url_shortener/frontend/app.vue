<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900 text-white font-sans">
    <Transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="transform translate-y-2 opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform translate-y-2 opacity-0"
    >
      <div
        v-if="showToast"
        class="fixed bottom-4 right-4 px-4 py-2 bg-purple-500 text-white rounded-lg shadow-lg flex items-center gap-2 z-50"
      >
        <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
        </svg>
        Copied to clipboard!
      </div>
    </Transition>

    <div class="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))]"></div>
    
    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80">
        <div class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-purple-500 to-blue-600 opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"></div>
      </div>

      <div class="mx-auto max-w-3xl py-16 sm:py-24">
        <div class="text-center mb-16">
          <h1 class="text-4xl font-bold tracking-tight sm:text-6xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 mb-4">
            URL Shortener
          </h1>
          <p class="text-lg leading-8 text-gray-300">
            Transform your long URLs into short, shareable links in seconds
          </p>
        </div>

        <div class="backdrop-blur-lg bg-white/10 rounded-2xl shadow-2xl p-6 sm:p-8 border border-white/10">
          <form @submit.prevent="shortenUrl" class="space-y-4">
            <div class="relative">
              <input
                type="url"
                v-model="url"
                placeholder="Enter your URL here..."
                class="w-full px-4 py-4 rounded-xl bg-white/5 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 border border-white/10 transition-all"
                required
              />
            </div>
            
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-gradient-to-r from-purple-500 to-blue-500 hover:from-purple-600 hover:to-blue-600 px-4 py-4 rounded-xl font-medium transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-purple-500/25"
            >
              <span v-if="isLoading" class="flex items-center justify-center gap-2">
                <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" />
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                </svg>
                Shortening...
              </span>
              <span v-else>Shorten URL</span>
            </button>
          </form>

          <div v-if="error" class="mt-4 p-4 bg-red-500/10 border border-red-500/50 rounded-xl text-red-200 backdrop-blur-sm">
            <p class="flex items-center gap-2">
              <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clip-rule="evenodd" />
              </svg>
              {{ error }}
            </p>
          </div>

          <div v-if="shortUrl" class="mt-6 space-y-4">
            <div class="h-px bg-gradient-to-r from-transparent via-white/25 to-transparent"></div>
            <div class="p-6 bg-white/5 rounded-xl border border-white/10 backdrop-blur-sm">
              <h2 class="text-xl font-semibold mb-4 text-purple-200">Your shortened URL</h2>
              <div class="flex items-center gap-3">
                <input
                  type="text"
                  :value="shortUrl"
                  readonly
                  class="flex-1 px-4 py-3 rounded-lg bg-white/5 text-white border border-white/10"
                />
                <button
                  @click="copyToClipboard"
                  class="px-4 py-3 bg-purple-500 hover:bg-purple-600 rounded-lg transition-colors flex items-center gap-2"
                >
                  <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M7 9a2 2 0 012-2h6a2 2 0 012 2v6a2 2 0 01-2 2H9a2 2 0 01-2-2V9z" />
                    <path d="M5 3a2 2 0 00-2 2v6a2 2 0 002 2V5h8a2 2 0 00-2-2H5z" />
                  </svg>
                  Copy
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const url = ref('')
const shortUrl = ref('')
const isLoading = ref(false)
const error = ref('')
const showToast = ref(false)
let toastTimeout = null

const config = useRuntimeConfig()
const SHORTENER_SERVICE_URL = config.public.SHORTENER_SERVICE_URL
const REDIRECT_SERVICE_URL = config.public.REDIRECT_SERVICE_URL

const shortenUrl = async () => {
  isLoading.value = true
  error.value = ''

  try {
    const response = await fetch(`${SHORTENER_SERVICE_URL}/shorten`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ long_url: url.value }),
    })

    if (!response.ok) throw new Error('Failed to shorten URL')

    const data = await response.json()
    shortUrl.value = `${REDIRECT_SERVICE_URL}/redirect/${data.short_url}`
  } catch {
    error.value = 'Failed to shorten URL. Please try again.'
  } finally {
    isLoading.value = false
  }
}

const copyToClipboard = async () => {
  await navigator.clipboard.writeText(shortUrl.value)
  
  // Clear any existing timeout
  if (toastTimeout) clearTimeout(toastTimeout)
  
  // Show toast
  showToast.value = true
  
  // Hide toast after 2 seconds
  toastTimeout = setTimeout(() => {
    showToast.value = false
  }, 2000)
}

// Clean up timeout on component unmount
onUnmounted(() => {
  if (toastTimeout) clearTimeout(toastTimeout)
})
</script>
