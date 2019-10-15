import base from './base'
import qs from 'qs'
import axios from './http'
import Cookies from 'js-cookie'

const index = {
    user: {
        login(data) {
            //return axios.get(`${base.homepage}/get_recommend`, {params: {page: page}})
            return axios.post(`${base.account}/login`, qs.stringify(data))
        },
        check_snum(data) {
            return axios.post(`${base.account}/check_snum`, qs.stringify(data))
        },
        check_account(data) {
            return axios.post(`${base.account}/check_account`, qs.stringify(data))
        },
        register(data) {
            return axios.post(`${base.account}/register`, qs.stringify(data))
        },
        get_info() {
            let ck = Cookies.get('token')
            return axios.post(`${base.account}/get_basic_info`, qs.stringify({token: ck}))
        },
        get_all_student() {
            let ck = Cookies.get('token')
            return axios.get(`${base.account}/get_all_student_info`, {params: {token: ck}})
        },
        add_student(data) {
            return axios.post(`${base.account}/add_new_student`, qs.stringify(data))
        },
        admin_modify_info(data) {
            return axios.post(`${base.account}/admin_modify_info`, qs.stringify(data))
        },
        admin_delete_student(data) {
            return axios.post(`${base.account}/delete_account`, qs.stringify(data))
        },
        change_head(data) {
            return axios.post(`${base.account}/change_head`, qs.stringify(data))
        },
        get_face_vector(){
            return axios.post()
        }
    },
    article: {
        add_article(data) {
            return axios.post(`${base.article}/add_article`, qs.stringify(data))
        },
        change_article(data) {
            return axios.post(`${base.article}/change_article`, qs.stringify(data))
        },
        delete_article(data) {
            return axios.post(`${base.article}/delete_article`, qs.stringify(data))
        },
        get_article(id) {
            let ck = Cookies.get('token');
            return axios.get(`${base.article}/get_article`, {params: {token: ck, article_id: id}})
        },
        get_article_tag(id) {
            let ck = Cookies.get('token');
            return axios.get(`${base.article}/get_article_tag`, {params: {token: ck, article_id: id}})
        },
        add_article_tag(data) {
            return axios.post(`${base.article}/add_article_tag`, qs.stringify(data))
        },
        change_article_tag(data) {
            return axios.post(`${base.article}/change_article_tag`, qs.stringify(data))
        },
        delete_article_tag(data) {
            return axios.post(`${base.article}/delete_article_tag`, qs.stringify(data))
        },
        get_history(id) {
            let ck = Cookies.get('token');
            return axios.get(`${base.article}/get_history`, {params: {token: ck, article_id: id}})
        },
        get_history_article(id) {
            let ck = Cookies.get('token');
            return axios.get(`${base.article}/get_history_article`, {params: {token: ck, history_id: id}})
        },
    },
    tag: {
        get_tag_tree() {
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_tag_tree`, {params: {token: ck}})
        },
        get_articles(id) {
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_articles`, {params: {token: ck, tag_id: id}})
        },
        add_tag(data) {
            return axios.post(`${base.tag}/add_tag`, qs.stringify(data))
        },
        change_tag(data) {
            return axios.post(`${base.tag}/change_tag`, qs.stringify(data))
        },
        delete_tag(data) {
            return axios.post(`${base.tag}/delete_tag`, qs.stringify(data))
        },
        get_tag_list(tag_id) {
            let ck = Cookies.get('token');
            return axios.get(`${base.tag}/get_tag_list`, {params: {token: ck, tag_id: tag_id}})
        }

    },
    face: {
        check(data) {
            return axios.post(`${base.face}/face_check`, qs.stringify(data))
        },
        exist(data) {
            return axios.post(`${base.face}/face_exist`, qs.stringify(data))
        }
    },
    comment: {
        get_comment(article_id) {
            return axios.get(`${base.comment}/get_comment`, {
                params: {
                    token: Cookies.get('token'),
                    article_id: article_id
                }
            })
        },
        add_comment(data) {
            return axios.post(`${base.comment}/add_comment`, qs.stringify(data))
        }
    }
};

export default index;
