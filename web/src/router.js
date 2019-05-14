import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    routes: [
        {path: '/', name: 'login', component: () => import('./view/login.vue')},
        {path: '/register', name: 'register', component: () => import('./view/register.vue')},
        {
            path: '/main', name: 'mainpage', component: () => import('./view/mainpage.vue'), children: [
                {path: 'default', name: 'default', component: () => import('./view/default.vue')},
                {path: 'article_view', name: 'article_view', component: () => import('./view/article_view.vue')},
                {path: 'article_list', name: 'article_list', component: () => import('./view/article_list.vue')},
                {path: 'tag_tree', name: 'tag_tree', component: () => import('./view/tag_tree.vue')},
                {path: 'add_article', name: 'add_article', component: () => import('./view/add_article.vue')},
                {path: 'add_student', name: 'add_student', component: () => import('./view/add_student.vue')},
                {path: 'change_article', name: 'change_article', component: () => import('./view/change_article.vue')},
                {path: 'modify_student', name: 'modify_student', component: () => import('./view/modify_student.vue')},
            ]
        },



    ],
});
