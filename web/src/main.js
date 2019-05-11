import Vue from 'vue'
import App from './App.vue'
import iView from 'iview';
import axios from 'axios';
import api from './api';

import 'iview/dist/styles/iview.css';

Vue.config.productionTip = false;
Vue.use(iView);
Vue.prototype.$axios = axios;
new Vue({
  render: h => h(App),
}).$mount('#app')
