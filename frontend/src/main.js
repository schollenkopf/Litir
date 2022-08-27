import { createApp } from 'vue'
import Backend from './services/backend'
import axios from 'axios'
import router from './router'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const app = createApp(App)

app.use(vuetify)
app.use(router)
app.config.globalProperties.axios = axios
app.config.globalProperties.$backend = new Backend();
  
app.mount('#app')







