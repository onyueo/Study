import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

// app.use(createPinia())
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

app.mount('#app')
