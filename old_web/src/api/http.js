import axios from 'axios'


const instance = axios.create({timeout: 1000 * 12});
instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
instance.defaults.responseType = 'json';
instance.defaults.withCredentials = true;

export default instance;
