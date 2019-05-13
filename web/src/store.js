import Vue from 'vue'
import Vuex from 'vuex'
import Cookies from 'js-cookie'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        token: Cookies.get('token'),
        userInfo: {
            user_id: "",
            username: "",
            group: {text: '', value: null},  // 用户组
            phonenumber: null,
            face: "",

        },
        tag: []
    },
    mutations: {
        save(state, data) {
            state.userInfo.user_id = data.id;
            state.userInfo.username = data.username;
            state.userInfo.group.value = data.group;
        },
        update_token(state, token) {
            state.token = token;
        },
        update_tag(state, tag) {
            state.tag = tag;
        }
    },
})
