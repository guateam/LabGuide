(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-07d37d82"],{"02f4":function(t,e,a){var n=a("4588"),r=a("be13");t.exports=function(t){return function(e,a){var o,i,c=String(r(e)),s=n(a),l=c.length;return s<0||s>=l?t?"":void 0:(o=c.charCodeAt(s),o<55296||o>56319||s+1===l||(i=c.charCodeAt(s+1))<56320||i>57343?t?c.charAt(s):o:t?c.slice(s,s+2):i-56320+(o-55296<<10)+65536)}}},"0390":function(t,e,a){"use strict";var n=a("02f4")(!0);t.exports=function(t,e,a){return e+(a?n(t,e).length:1)}},"0bfb":function(t,e,a){"use strict";var n=a("cb7c");t.exports=function(){var t=n(this),e="";return t.global&&(e+="g"),t.ignoreCase&&(e+="i"),t.multiline&&(e+="m"),t.unicode&&(e+="u"),t.sticky&&(e+="y"),e}},"214f":function(t,e,a){"use strict";a("b0c5");var n=a("2aba"),r=a("32e9"),o=a("79e5"),i=a("be13"),c=a("2b4c"),s=a("520a"),l=c("species"),u=!o(function(){var t=/./;return t.exec=function(){var t=[];return t.groups={a:"7"},t},"7"!=="".replace(t,"$<a>")}),d=function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var a="ab".split(t);return 2===a.length&&"a"===a[0]&&"b"===a[1]}();t.exports=function(t,e,a){var f=c(t),h=!o(function(){var e={};return e[f]=function(){return 7},7!=""[t](e)}),p=h?!o(function(){var e=!1,a=/a/;return a.exec=function(){return e=!0,null},"split"===t&&(a.constructor={},a.constructor[l]=function(){return a}),a[f](""),!e}):void 0;if(!h||!p||"replace"===t&&!u||"split"===t&&!d){var v=/./[f],g=a(i,f,""[t],function(t,e,a,n,r){return e.exec===s?h&&!r?{done:!0,value:v.call(e,a,n)}:{done:!0,value:t.call(a,e,n)}:{done:!1}}),m=g[0],b=g[1];n(String.prototype,t,m),r(RegExp.prototype,f,2==e?function(t,e){return b.call(t,this,e)}:function(t){return b.call(t,this)})}}},4009:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"bg",attrs:{id:"login"}},[a("card",{class:{login:t.photo_hidden,loginCamera:!t.photo_hidden},attrs:{bordered:!1}},[a("p",{attrs:{slot:"title"},domProps:{textContent:t._s(t.photo_hidden?"登录实验室":"人脸验证")},slot:"title"}),a("i-form",{ref:"login_form",attrs:{model:t.info,rules:t.rule,hidden:!t.photo_hidden},nativeOn:{submit:function(t){t.preventDefault()}}},[a("form-item",{attrs:{label:"用户名或学号",prop:"username"}},[a("i-input",{attrs:{size:"large",placeholder:"输入用户名或学号"},model:{value:t.info.username,callback:function(e){t.$set(t.info,"username",e)},expression:"info.username"}})],1),a("form-item",{attrs:{label:"密码",prop:"password"}},[a("i-input",{attrs:{type:"password",size:"large",placeholder:"输入密码"},model:{value:t.info.password,callback:function(e){t.$set(t.info,"password",e)},expression:"info.password"}})],1),a("form-item",{staticStyle:{"text-align":"center"}},[a("i-button",{staticStyle:{width:"40%","margin-top":"1%"},attrs:{size:"large",type:"primary"},on:{click:t.check_account}},[t._v("登录\n                ")]),a("i-button",{staticStyle:{width:"40%","margin-top":"1%","margin-left":"1%"},attrs:{size:"large",type:"success"},on:{click:t.jump}},[t._v("注册\n                ")])],1)],1),a("i-form",{attrs:{hidden:t.photo_hidden},nativeOn:{submit:function(t){t.preventDefault()}}},[a("FormItem",[a("video",{staticStyle:{"max-width":"100%","max-height":"50vh"},attrs:{height:"auto",width:"100%",autoplay:"autoplay"}}),a("canvas",{staticStyle:{width:"100%"},attrs:{id:"canvas1",hidden:!0}})]),a("FormItem",[a("i-button",{attrs:{type:"primary",disabled:!t.button_enable,size:"large"},domProps:{textContent:t._s("手动拍照")},on:{click:t.draw_photo}}),t.open_camera?t._e():a("i-button",{staticStyle:{"margin-left":"1%"},attrs:{type:"primary",size:"large"},on:{click:t.getMedia}},[t._v("\n                    开启摄像头\n                ")]),t.exArray.length>1?a("i-button",{staticStyle:{"margin-left":"1%"},attrs:{type:"success",size:"large"},on:{click:t.change_camera}},[t._v("\n                    切换摄像头\n                ")]):t._e(),a("p",{domProps:{textContent:t._s(t.alert_info)}})],1)],1)],1),a("modal",{attrs:{title:"提示"},model:{value:t.closable_modal,callback:function(e){t.closable_modal=e},expression:"closable_modal"}},[a("p",{domProps:{textContent:t._s(t.alert_info)}})])],1)},r=[],o=(a("a481"),{name:"login",data:function(){return{open_camera:!1,info:{username:"",password:""},rule:{username:[{required:!0,message:"用户名不能为空",trigger:"blur"}],password:[{required:!0,message:"密码不能为空",trigger:"blur"},{type:"string",min:6,message:"密码长度必须大于6位",trigger:"blur"}]},video:null,exArray:[],canvas:null,context:null,button_text:"人脸识别",button_enable:!1,alert_info:"开启摄像头后自动检测",closable_modal:!1,exnum:0,interval_id:"",photo_num:0,photo_hidden:!0}},methods:{check_account:function(){var t=this,e=this;this.$refs["login_form"].validate(function(a){a&&t.$api.account.check_account(e.info).then(function(t){1===t.data.code?(e.photo_hidden=!1,e.getMedia()):(e.alert_info="用户名或密码错误",e.closable_modal=!0)})})},change_camera:function(){this.exnum<this.exArray.length?this.exnum++:this.exnum=0,navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:that.exArray[this.exnum]}]},audio:!1},that.successFunc,that.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser.")},getMedia:function(){var t=this;t.open_camera||""===t.info.username||(navigator.getUserMedia=navigator.getUserMedia||navigator.webkitGetUserMedia||navigator.mozGetUserMedia||navigator.msGetUserMedia,window.URL=window.URL||window.webkitURL||window.mozURL||window.msURL,navigator.mediaDevices.enumerateDevices().then(function(e){for(var a=0;a!=e.length;++a){var n=e[a];"video"===n.kind&&t.exArray.push(n.id)}}),navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:t.exArray[this.exnum]}]},audio:!1},t.successFunc,t.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser."))},successFunc:function(t){var e=this;void 0!==this.video.mozSrcObject?this.video.mozSrcObject=t:this.video.srcObject=t,""==e.interval_id&&(e.interval_id=setInterval(e.draw_photo,2500)),this.open_camera=!0,this.video.play()},errorFunc:function(t){this.closable_modal=!0,this.alert_info="错误:"+t},draw_photo:function(){var t=this,e=this;if(""!==e.info.username){e.photo_num+=1,e.photo_num>3&&(e.button_enable=!1,setTimeout(function(){e.button_enable=!0},5e3)),e.alert_info="正在检测...",document.getElementById("canvas1").height=this.video.offsetHeight,e.context.drawImage(e.video,0,0,this.video.offsetWidth,this.video.offsetHeight);var n=e.canvas.toDataURL("image/png",1);n=n.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,"");var r={username:e.info.username,face:n};this.$api.face.check(r).then(function(n){1===n.data.code?n.data.data>80?(e.alert_info="人脸认证通过",e.stop_auto_check(),e.$api.account.login(t.info).then(function(t){1===t.data.code?Promise.resolve().then(a.t.bind(null,"a78e",7)).then(function(a){a.set("token",t.data.data.token),a.set("group",t.data.data.group),e.$store.commit("save",t.data.data),e.$store.commit("update_token",t.data.data.token),e.$router.push({name:"default"})}):(e.alert_info="用户名或密码错误",e.closable_modal=!0)})):(e.alert_info="人脸相似度为"+parseInt(n.data.data)+"%,过低，请重新校验",e.button_enable=!0):0===n.data.code?(e.alert_info="百度人脸验证提供的ACCESS TOKEN已过期，请通知管理员进行更新",e.button_enable=!0):-1===n.data.code?(e.alert_info="人脸识别服务器繁忙，请重试",e.button_enable=!0):(e.alert_info="验证失败，请重试",e.button_enable=!0,console.log(n.data.data)),(1!==n.data.code||1===n.data.code&&n.data.data<=80)&&3==e.photo_num&&(e.stop_auto_check(),e.button_enable=!0,e.closable_modal=!0,e.alert_info="自动检测失败次数过多，请手动检测")})}},stop_auto_check:function(){clearInterval(this.interval_id)},jump:function(){this.$router.push({name:"register"})}},mounted:function(){this.video=document.querySelector("video"),this.canvas=document.getElementById("canvas1"),this.context=this.canvas.getContext("2d")}}),i=o,c=(a("54ae"),a("2877")),s=Object(c["a"])(i,n,r,!1,null,"5f509af7",null);e["default"]=s.exports},"520a":function(t,e,a){"use strict";var n=a("0bfb"),r=RegExp.prototype.exec,o=String.prototype.replace,i=r,c="lastIndex",s=function(){var t=/a/,e=/b*/g;return r.call(t,"a"),r.call(e,"a"),0!==t[c]||0!==e[c]}(),l=void 0!==/()??/.exec("")[1],u=s||l;u&&(i=function(t){var e,a,i,u,d=this;return l&&(a=new RegExp("^"+d.source+"$(?!\\s)",n.call(d))),s&&(e=d[c]),i=r.call(d,t),s&&i&&(d[c]=d.global?i.index+i[0].length:e),l&&i&&i.length>1&&o.call(i[0],a,function(){for(u=1;u<arguments.length-2;u++)void 0===arguments[u]&&(i[u]=void 0)}),i}),t.exports=i},"54ae":function(t,e,a){"use strict";var n=a("fc74"),r=a.n(n);r.a},"5f1b":function(t,e,a){"use strict";var n=a("23c6"),r=RegExp.prototype.exec;t.exports=function(t,e){var a=t.exec;if("function"===typeof a){var o=a.call(t,e);if("object"!==typeof o)throw new TypeError("RegExp exec method returned something other than an Object or null");return o}if("RegExp"!==n(t))throw new TypeError("RegExp#exec called on incompatible receiver");return r.call(t,e)}},a481:function(t,e,a){"use strict";var n=a("cb7c"),r=a("4bf8"),o=a("9def"),i=a("4588"),c=a("0390"),s=a("5f1b"),l=Math.max,u=Math.min,d=Math.floor,f=/\$([$&`']|\d\d?|<[^>]*>)/g,h=/\$([$&`']|\d\d?)/g,p=function(t){return void 0===t?t:String(t)};a("214f")("replace",2,function(t,e,a,v){return[function(n,r){var o=t(this),i=void 0==n?void 0:n[e];return void 0!==i?i.call(n,o,r):a.call(String(o),n,r)},function(t,e){var r=v(a,t,this,e);if(r.done)return r.value;var d=n(t),f=String(this),h="function"===typeof e;h||(e=String(e));var m=d.global;if(m){var b=d.unicode;d.lastIndex=0}var _=[];while(1){var x=s(d,f);if(null===x)break;if(_.push(x),!m)break;var w=String(x[0]);""===w&&(d.lastIndex=c(f,o(d.lastIndex),b))}for(var y="",k=0,S=0;S<_.length;S++){x=_[S];for(var $=String(x[0]),M=l(u(i(x.index),f.length),0),U=[],E=1;E<x.length;E++)U.push(p(x[E]));var I=x.groups;if(h){var R=[$].concat(U,M,f);void 0!==I&&R.push(I);var A=String(e.apply(void 0,R))}else A=g($,f,M,U,I,e);M>=k&&(y+=f.slice(k,M)+A,k=M+$.length)}return y+f.slice(k)}];function g(t,e,n,o,i,c){var s=n+t.length,l=o.length,u=h;return void 0!==i&&(i=r(i),u=f),a.call(c,u,function(a,r){var c;switch(r.charAt(0)){case"$":return"$";case"&":return t;case"`":return e.slice(0,n);case"'":return e.slice(s);case"<":c=i[r.slice(1,-1)];break;default:var u=+r;if(0===u)return a;if(u>l){var f=d(u/10);return 0===f?a:f<=l?void 0===o[f-1]?r.charAt(1):o[f-1]+r.charAt(1):a}c=o[u-1]}return void 0===c?"":c})}})},b0c5:function(t,e,a){"use strict";var n=a("520a");a("5ca1")({target:"RegExp",proto:!0,forced:n!==/./.exec},{exec:n})},fc74:function(t,e,a){}}]);