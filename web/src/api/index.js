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
        get_info(){
            let ck = Cookies.get('token')
            return axios.post(`${base.account}/get_basic_info`, qs.stringify({token:ck}))
        },
        get_all_student(){
            let ck =  Cookies.get('token')
            return axios.get(`${base.account}/get_all_student_info`,{params:{token:ck}})
        },
        add_student(data){
            return axios.post(`${base.account}/add_new_student`, qs.stringify(data))
        },
        admin_modify_info(data){
            return axios.post(`${base.account}/admin_modify_info`, qs.stringify(data))
        },
        admin_delete_student(data){
            return axios.post(`${base.account}/delete_account`, qs.stringify(data))
        }
    },
    article: {
        add_article(data){
            return axios.post(`${base.article}/add_article`,qs.stringify(data))
        },
        change_article(data){
            return axios.post(`${base.article}/change_article`,qs.stringify(data))
        },
        delete_article(data){
            return axios.post(`${base.article}/delete_article`,qs.stringify(data))
        },
        get_article(id){
            let ck = Cookies.get('token');
            return axios.get(`${base.article}/get_article`, {params: {token: ck,article_id:id}})
        },
    },
    tag:{
        get_tag_tree(){
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_tag_tree`, {params: {token: ck}})
        },
        get_articles(id){
            let ck = Cookies.get('token')
            return axios.get(`${base.tag}/get_articles`,{params: {token: ck,tag_id:id}})
        },
        add_tag(data){
            return axios.post(`${base.tag}/add_tag`,qs.stringify(data))
        },
        change_tag(data){
            return axios.post(`${base.tag}/change_tag`,qs.stringify(data))
        },
        delete_tag(data){
            return axios.post(`${base.tag}/delete_tag`,qs.stringify(data))
        }

    },
    face:{
        check(data){
            return axios.post(`${base.face}/face_check`, qs.stringify(data))
        },
        exist(data){
            return axios.post(`${base.face}/face_exist`, qs.stringify(data))
        }
    },
};

export default index;
