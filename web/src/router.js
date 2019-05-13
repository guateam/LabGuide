import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    routes: [
        {path: '/', name: 'login', component: () => import('./view/login.vue')},
        {path: '/register', name: 'register', component: () => import('./view/register.vue')},
        {path: '/main', name: 'mainpage', component: () => import('./view/mainpage.vue')},
        {path: '/add_article', name: 'add_article', component: () => import('./view/add_article.vue')},
        {path: '/article', name: 'article', component: () => import('./view/article.vue')},
        {path: '/add_student', name: 'add_student', component: () => import('./view/add_student.vue')},
    ],
});
