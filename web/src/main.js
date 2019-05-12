import Vue from 'vue'
import App from './App.vue'
import iView from 'iview';
import axios from 'axios';
import api from './api';
import router from './router';
import Cookies from 'js-cookie';
import 'iview/dist/styles/iview.css';
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import VueQuillEditor from 'vue-quill-editor'
Vue.use(VueQuillEditor);

Vue.config.productionTip = false;
Vue.use(iView);
Vue.prototype.$axios = axios;
Vue.prototype.$api = api;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
