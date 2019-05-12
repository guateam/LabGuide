import base from './base'
import qs from 'qs'
import axios from './http'
import Cookies from 'js-cookie'

const index = {
    account: {
        login(data) {
            //return axios.get(`${base.homepage}/get_recommend`, {params: {page: page}})
            return axios.post(`${base.account}/login`, qs.stringify(data))
        },
        check_snum(data){
            return axios.post(`${base.account}/check_snum`, qs.stringify(data))
        },
        check_account(data){
            return axios.post(`${base.account}/check_account`, qs.stringify(data))
        },
        register(data) {
            return axios.post(`${base.account}/register`, qs.stringify(data))
        },
    },
    article: {
        add_article(data){
            return axios.post(`${base.article}/add_article`,qs.stringify(data))
        },
        get_article(id){
            let ck = Cookies.get('token')
            return axios.get(`${base.article}/get_article`, {params: {token: ck,article_id:id}})
        }
    },
    tag:{
        get_tag_tree(){
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_tag_tree`, {params: {token: ck}})
        },
        get_articles(id){
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_articles`,{params: {token: ck,tag_id:id}})
        }
    },
    face:{
        check(data){
            return axios.post(`${base.face}/face_check`, qs.stringify(data))
        }
    },
};

export default index;
