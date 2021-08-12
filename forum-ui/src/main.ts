import { createApp } from 'vue'
import vuetify from './plugins/vuetify'
import router from './router'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Swal from './plugins/swal';
import 'sweetalert2/dist/sweetalert2.min.css';

import "bootstrap"

const app = createApp(App)
app.use(vuetify)
app.use(router)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)
app.use(Swal);

app.mount('#app')
