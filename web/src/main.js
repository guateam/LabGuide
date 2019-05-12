import Vue from 'vue'
import App from './App.vue'
import iView from 'iview';
import axios from 'axios';
import api from './api';
import router from './router';
import Cookies from 'js-cookie';
import 'iview/dist/styles/iview.css';

Vue.config.productionTip = false;
Vue.use(iView);
Vue.prototype.$axios = axios;
Vue.prototype.$api = api;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
