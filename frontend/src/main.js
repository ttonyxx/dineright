import Vue from 'vue'
import App from './App.vue'
//import Vuetify from 'vuetify/lib'
import vuetify from './plugins/vuetify'
import router from './router'

// const vuetify = new Vuetify({
//   theme: {
//     themes: {
//       light: {
//         primary: '#90ACE0',
//         secondary: '#FCD47C',
//         accent: '#FFD15C',
//         error: '#b71c1c',
//       },
//     },
//   },
// })

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

