import base from './base'
import qs from 'qs'
import axios from './http'


const index = {
    account: {
        login(data) {
            //return axios.get(`${base.homepage}/get_recommend`, {params: {page: page}})
            return axios.post(`${base.account}/login`, qs.stringify(data))
        },
        logout(data){
            return axios.post(`${base.account}/logout`, qs.stringify(data))
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

    },
    tag:{

    },
    face:{
        check(data){
            return axios.post(`${base.face}/face_check`, qs.stringify(data))
        }
    },
};

export default index;
