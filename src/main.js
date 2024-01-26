import { createApp } from 'vue'

import App from './App.vue'

// Asegúrate de que google charts esté instalado en tu proyecto
import { VueGoogleCharts  } from './components/loader.js';

const app = createApp(App);
app.provide(VueGoogleCharts);
app.mount('#app');