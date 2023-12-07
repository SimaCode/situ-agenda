// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'

import App from './App.vue'
import router from './router'

// Vuetify
import 'vuetify/styles'
import 'vuetify/dist/vuetify.min.css'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

axios.defaults.baseURL = 'http://localhost:4000/api';
axios.defaults.withCredentials = true;

const app = createApp(App)

app.use(createPinia())
app.use(router)

const vuetify = createVuetify({
  components,
  directives,
})

app.use(vuetify)

app.mount('#app')