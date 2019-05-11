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
        }
    },
    article: {
        register(data) {
            return axios.post(`${base.account}/register`, qs.stringify(data))
        },  
    },
    tag:{

    },
    face:{
        check(data){
            return axios.post(`${base.face}/check_face`, qs.stringify(data))
        }
    },
};

export default index;
