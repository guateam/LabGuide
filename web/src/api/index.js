import base from './base'
import qs from 'qs'
import axios from './http'
import Cookies from 'js-cookie'

const index = {
    user: {
        login(data) {
            //return axios.get(`${base.homepage}/get_recommend`, {params: {page: page}})
            return axios.post(`${base.user}/login`, qs.stringify(data))
        },
        check_s_num(s_num) {
            return axios.get(`${base.user}/check_s_num`, {params: {s_num: s_num}})
        },
        register(data) {
            return axios.post(`${base.user}/register`, qs.stringify(data))
        },
        get_info() {
            let ck = Cookies.get('token')
            return axios.get(`${base.user}/get_user`, {params: {token: ck}})

        },
        change_head(data) {
            return axios.post(`${base.user}/change_head`, qs.stringify(data))
        },
        get_face_vector(data) {
            return axios.post(`${base.user}/get_face_vector`, qs.stringify(data))
        },
        change_face_vector(data) {
            return axios.post(`${base.user}/change_face_vector`, qs.stringify(data))
        },
        update_api(data) {
            return axios.post(`${base.user}/update_new_api`, qs.stringify(data))
        },
        get_users() {
            let ck = Cookies.get('token');
            return axios.get(`${base.user}/get_users`, {params: {token: ck}})
        },
        delete_user(user_id) {
            let data = {
                token: Cookies.get('token'),
                user_id: user_id
            };
            return axios.post(`${base.user}/delete_user`, qs.stringify(data))
        },
        add_user(data) {
            return axios.post(`${base.user}/add_user`, qs.stringify(data))
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
    },
    notice: {
        get_notice() {
            return axios.get(`${base.notice}/get_notice`)
        }
    },
    right: {
        get_right(right, target) {
            return axios.get(`${base.right}/get_right`, {
                params: {
                    token: Cookies.get('token'),
                    right_id: right,
                    target: target
                }
            })
        },
        get_right_groups() {
            return axios.get(`${base.right}/get_right_groups`, {params: {token: Cookies.get('token')}})
        }
    }
};

export default index;
