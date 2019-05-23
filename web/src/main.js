import Vue from 'vue'
import App from './App.vue'
import iView from 'iview'
import axios from 'axios'
import api from './api'
import router from './router'
import Cookies from 'js-cookie'
import store from './store'
import '../my-theme/index.less'
import 'iview/dist/styles/iview.css'
import hljs from 'highlight.js'
import 'highlight.js/styles/monokai-sublime.css'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import 'katex/dist/katex.css'
import VueQuillEditor from 'vue-quill-editor'
import MarkdownShortcuts from 'quill-markdown-shortcuts-for-vue-quill-editor';

Quill.register('modules/markdownShortcuts', MarkdownShortcuts);

Vue.use(VueQuillEditor);
Vue.use(iView);
Vue.prototype.$axios = axios;
Vue.prototype.$api = api;
Vue.prototype.$Cookies = Cookies;
Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app');
