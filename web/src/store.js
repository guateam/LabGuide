import Vue from 'vue'
import Vuex from 'vuex'
import Cookies from 'js-cookie'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: Cookies.get('token'),
    userInfo: {
      user_id: "",
      username:"",
      group: {text: '', value: null},  // 用户组
      phonenumber:null,
      face:"",
    },
  },
  mutations:{
    save(state,data){
      state.userInfo.user_id = data.id;
      state.userInfo.username = data.username;
    },
    update_token(state,token){
      state.token = token;
    }
  },
})
