(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6ce62ac8"],{"02f4":function(e,t,n){var a=n("4588"),o=n("be13");e.exports=function(e){return function(t,n){var r,i,c=String(o(t)),u=a(n),s=c.length;return u<0||u>=s?e?"":void 0:(r=c.charCodeAt(u),r<55296||r>56319||u+1===s||(i=c.charCodeAt(u+1))<56320||i>57343?e?c.charAt(u):r:e?c.slice(u,u+2):i-56320+(r-55296<<10)+65536)}}},"0390":function(e,t,n){"use strict";var a=n("02f4")(!0);e.exports=function(e,t,n){return t+(n?a(e,t).length:1)}},"07e3":function(e,t){var n={}.hasOwnProperty;e.exports=function(e,t){return n.call(e,t)}},"09e7":function(e,t,n){"use strict";var a=n("f023"),o=n.n(a);o.a},"0bfb":function(e,t,n){"use strict";var a=n("cb7c");e.exports=function(){var e=a(this),t="";return e.global&&(t+="g"),e.ignoreCase&&(t+="i"),e.multiline&&(t+="m"),e.unicode&&(t+="u"),e.sticky&&(t+="y"),t}},"1bc3":function(e,t,n){var a=n("f772");e.exports=function(e,t){if(!a(e))return e;var n,o;if(t&&"function"==typeof(n=e.toString)&&!a(o=n.call(e)))return o;if("function"==typeof(n=e.valueOf)&&!a(o=n.call(e)))return o;if(!t&&"function"==typeof(n=e.toString)&&!a(o=n.call(e)))return o;throw TypeError("Can't convert object to primitive value")}},"1ec9":function(e,t,n){var a=n("f772"),o=n("e53d").document,r=a(o)&&a(o.createElement);e.exports=function(e){return r?o.createElement(e):{}}},"214f":function(e,t,n){"use strict";n("b0c5");var a=n("2aba"),o=n("32e9"),r=n("79e5"),i=n("be13"),c=n("2b4c"),u=n("520a"),s=c("species"),l=!r(function(){var e=/./;return e.exec=function(){var e=[];return e.groups={a:"7"},e},"7"!=="".replace(e,"$<a>")}),d=function(){var e=/(?:)/,t=e.exec;e.exec=function(){return t.apply(this,arguments)};var n="ab".split(e);return 2===n.length&&"a"===n[0]&&"b"===n[1]}();e.exports=function(e,t,n){var f=c(e),p=!r(function(){var t={};return t[f]=function(){return 7},7!=""[e](t)}),h=p?!r(function(){var t=!1,n=/a/;return n.exec=function(){return t=!0,null},"split"===e&&(n.constructor={},n.constructor[s]=function(){return n}),n[f](""),!t}):void 0;if(!p||!h||"replace"===e&&!l||"split"===e&&!d){var v=/./[f],g=n(i,f,""[e],function(e,t,n,a,o){return t.exec===u?p&&!o?{done:!0,value:v.call(t,n,a)}:{done:!0,value:e.call(n,t,a)}:{done:!1}}),m=g[0],b=g[1];a(String.prototype,e,m),o(RegExp.prototype,f,2==t?function(e,t){return b.call(e,this,t)}:function(e){return b.call(e,this)})}}},"294c":function(e,t){e.exports=function(e){try{return!!e()}catch(t){return!0}}},"35e8":function(e,t,n){var a=n("d9f6"),o=n("aebd");e.exports=n("8e60")?function(e,t,n){return a.f(e,t,o(1,n))}:function(e,t,n){return e[t]=n,e}},4009:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"bg",attrs:{id:"login"}},[n("card",{class:{login:!e.login_hidden,loginCamera:!e.photo_hidden},attrs:{bordered:!1}},[n("p",{attrs:{slot:"title"},slot:"title"},[e._v(e._s(e.login_hidden?"人脸验证":"登录实验室"))]),n("i-form",{ref:"login_form",attrs:{model:e.info,rules:e.rule,hidden:e.login_hidden},nativeOn:{submit:function(e){e.preventDefault()}}},[n("form-item",{attrs:{label:"登录方式",prop:"way"}},[n("br"),n("RadioGroup",{model:{value:e.info.way,callback:function(t){e.$set(e.info,"way",t)},expression:"info.way"}},[n("Radio",{attrs:{label:"用户名"}}),n("Radio",{attrs:{label:"学号"}})],1)],1),n("form-item",{attrs:{label:e.info.way,prop:"username"}},[n("i-input",{attrs:{size:"large",placeholder:"输入"+e.info.way},model:{value:e.info.username,callback:function(t){e.$set(e.info,"username",t)},expression:"info.username"}})],1),n("form-item",{attrs:{label:"密码",prop:"password"}},[n("i-input",{attrs:{type:"password",size:"large",placeholder:"输入密码"},model:{value:e.info.password,callback:function(t){e.$set(e.info,"password",t)},expression:"info.password"}})],1),n("form-item",{staticStyle:{"text-align":"center"}},[n("i-button",{staticStyle:{width:"40%","margin-top":"1%"},attrs:{size:"large",type:"primary"},on:{click:e.check_account}},[e._v("登录\n                ")]),n("i-button",{staticStyle:{width:"40%","margin-top":"1%","margin-left":"1%"},attrs:{size:"large",type:"success"},on:{click:e.jump}},[e._v("注册\n                ")])],1)],1),n("i-form",{attrs:{hidden:e.photo_hidden},nativeOn:{submit:function(e){e.preventDefault()}}},[n("FormItem",[n("video",{staticStyle:{"max-width":"100%","max-height":"50vh"},attrs:{height:"auto",width:"100%",autoplay:"autoplay"}}),n("canvas",{staticStyle:{width:"100%"},attrs:{id:"canvas1",hidden:!0}})]),n("FormItem",[n("i-button",{attrs:{type:"primary",disabled:!e.button_enable,size:"large"},domProps:{textContent:e._s(e.button_text)},on:{click:e.draw_photo}}),e.open_camera?n("i-button",{staticStyle:{"margin-left":"1%"},attrs:{type:"primary",size:"large"},on:{click:e.getMedia}},[e._v("\n                    开启摄像头\n                ")]):e._e(),e.exArray.length>1?n("i-button",{staticStyle:{"margin-left":"1%"},attrs:{type:"success",size:"large"},on:{click:e.change_camera}},[e._v("\n                    切换摄像头\n                ")]):e._e()],1)],1)],1),n("modal",{attrs:{title:"提示"},model:{value:e.closable_modal,callback:function(t){e.closable_modal=t},expression:"closable_modal"}},[n("p",{domProps:{textContent:e._s(e.alert_info)}})]),n("modal",{attrs:{title:"请稍候",closable:!1,"mask-closable":!1,loading:!0},model:{value:e.loading_modal,callback:function(t){e.loading_modal=t},expression:"loading_modal"}},[n("p",[e._v("正在进行人脸检测...")])])],1)},o=[],r=n("85f2"),i=n.n(r);function c(e,t,n){return t in e?i()(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}n("a481");var u,s={name:"login",data:function(){return{open_camera:!1,info:{username:"",password:"",way:"用户名"},rule:{username:[{required:!0,message:"用户名不能为空",trigger:"blur"}],password:[{required:!0,message:"密码不能为空",trigger:"blur"},{type:"string",min:6,message:"密码长度必须大于6位",trigger:"blur"}],way:[{required:!0,message:"登录方式不能为空",trigger:"blur"}]},login_hidden:!1,photo_hidden:!0,video:null,exArray:[],canvas:null,context:null,button_text:"人脸识别",button_enable:!1,alert_info:"",closable_modal:!1,loading_modal:!1,exnum:0}},methods:(u={check_account:function(){var e=this,t=this;this.$refs["login_form"].validate(function(n){n&&e.$api.account.check_account(e.info).then(function(e){1===e.data.code?t.goto_photo():(t.alert_info="用户名或密码错误",t.closable_modal=!0,t.loading_modal=!1)})})},goto_photo:function(){this.login_hidden=!0,this.photo_hidden=!1,this.getMedia()},goto_login:function(){this.login_hidden=!1,this.photo_hidden=!0},change_camera:function(){this.exnum<this.exArray.length?(this.exnum++,this.getMedia()):(this.exnum=0,this.getMedia())},getMedia:function(){var e=this;navigator.getUserMedia=navigator.getUserMedia||navigator.webkitGetUserMedia||navigator.mozGetUserMedia||navigator.msGetUserMedia,window.URL=window.URL||window.webkitURL||window.mozURL||window.msURL,navigator.mediaDevices.enumerateDevices().then(function(t){for(var n=0;n!=t.length;++n){var a=t[n];"video"===a.kind&&e.exArray.push(a.id)}}),navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:e.exArray[this.exnum]}]},audio:!1},e.successFunc,e.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser.")},successFunc:function(e){void 0!==this.video.mozSrcObject?this.video.mozSrcObject=e:this.video.srcObject=e,this.video.play(),this.button_enable=!0},errorFunc:function(e){this.closable_modal=!0,this.alert_info="错误:"+e},draw_photo:function(){var e=this;e.button_text="正在检测",e.button_enable=!1,setTimeout(function(){e.button_enable=!0,e.button_text="请重新识别"},5e3),console.info(this.video.offsetHeight),e.context.drawImage(e.video,0,0,1e3,800);var t=e.canvas.toDataURL("image/png",1);t=t.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,"");var a={username:e.info.username,face:t};this.$api.face.check(a).then(function(t){1===t.data.code&&t.data.data>80&&e.$api.account.login(e.info).then(function(t){1===t.data.code&&Promise.resolve().then(n.t.bind(null,"a78e",7)).then(function(n){n.set("token",t.data.data.token),e.$store.commit("save",t.data.data),e.$store.commit("update_token",t.data.data.token),e.loading_modal=!1,e.$router.push({name:"mainpage"})})})}),navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:e.exArray[this.exnum]}]},audio:!1},e.successFunc,e.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser.")}},c(u,"successFunc",function(e){void 0!==this.video.mozSrcObject?this.video.mozSrcObject=e:this.video.srcObject=e,this.video.play(),this.button_enable=!0}),c(u,"errorFunc",function(e){alert("Error！"+e),this.open_camera=!0}),c(u,"draw_photo",function(){var e=this;e.button_text="正在检测",e.button_enable=!1,setTimeout(function(){e.button_enable=!0},5e3),document.getElementById("canvas1").height=this.video.offsetHeight,e.context.drawImage(e.video,0,0,this.video.offsetWidth,this.video.offsetHeight);var t=e.canvas.toDataURL("image/png",1);t=t.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,"");var a={username:e.info.username,face:t};this.$api.face.check(a).then(function(t){1===t.data.code?t.data.data>80?e.$api.account.login(e.info).then(function(t){1===t.data.code&&Promise.resolve().then(n.t.bind(null,"a78e",7)).then(function(n){n.set("token",t.data.data.token),n.set("group",t.data.data.group),e.$store.commit("save",t.data.data),e.$store.commit("update_token",t.data.data.token),e.loading_modal=!1,e.$router.push({name:"default"})})}):(e.alert_info="人脸相似度为"+parseInt(t.data.data)+"%,过低，请重新校验",e.closable_modal=!0,e.loading_modal=!1,e.button_enable=!0):0===t.data.code?(e.alert_info="百度人脸验证提供的ACCESS TOKEN已过期，请通知管理员进行更新",e.closable_modal=!0,e.loading_modal=!1,e.button_enable=!0):-1===t.data.code?(e.alert_info="人脸识别服务器繁忙，请重试",e.closable_modal=!0,e.loading_modal=!1,e.button_enable=!0):(e.alert_info="验证失败，请重试",e.closable_modal=!0,e.loading_modal=!1,e.button_enable=!0)})}),c(u,"jump",function(){this.$router.push({name:"register"})}),u),mounted:function(){this.video=document.querySelector("video"),this.canvas=document.getElementById("canvas1"),this.context=this.canvas.getContext("2d")}},l=s,d=(n("09e7"),n("2877")),f=Object(d["a"])(l,a,o,!1,null,"6a1a9261",null);t["default"]=f.exports},"454f":function(e,t,n){n("46a7");var a=n("584a").Object;e.exports=function(e,t,n){return a.defineProperty(e,t,n)}},"46a7":function(e,t,n){var a=n("63b6");a(a.S+a.F*!n("8e60"),"Object",{defineProperty:n("d9f6").f})},"520a":function(e,t,n){"use strict";var a=n("0bfb"),o=RegExp.prototype.exec,r=String.prototype.replace,i=o,c="lastIndex",u=function(){var e=/a/,t=/b*/g;return o.call(e,"a"),o.call(t,"a"),0!==e[c]||0!==t[c]}(),s=void 0!==/()??/.exec("")[1],l=u||s;l&&(i=function(e){var t,n,i,l,d=this;return s&&(n=new RegExp("^"+d.source+"$(?!\\s)",a.call(d))),u&&(t=d[c]),i=o.call(d,e),u&&i&&(d[c]=d.global?i.index+i[0].length:t),s&&i&&i.length>1&&r.call(i[0],n,function(){for(l=1;l<arguments.length-2;l++)void 0===arguments[l]&&(i[l]=void 0)}),i}),e.exports=i},"584a":function(e,t){var n=e.exports={version:"2.6.5"};"number"==typeof __e&&(__e=n)},"5f1b":function(e,t,n){"use strict";var a=n("23c6"),o=RegExp.prototype.exec;e.exports=function(e,t){var n=e.exec;if("function"===typeof n){var r=n.call(e,t);if("object"!==typeof r)throw new TypeError("RegExp exec method returned something other than an Object or null");return r}if("RegExp"!==a(e))throw new TypeError("RegExp#exec called on incompatible receiver");return o.call(e,t)}},"63b6":function(e,t,n){var a=n("e53d"),o=n("584a"),r=n("d864"),i=n("35e8"),c=n("07e3"),u="prototype",s=function(e,t,n){var l,d,f,p=e&s.F,h=e&s.G,v=e&s.S,g=e&s.P,m=e&s.B,b=e&s.W,_=h?o:o[t]||(o[t]={}),x=_[u],y=h?a:v?a[t]:(a[t]||{})[u];for(l in h&&(n=t),n)d=!p&&y&&void 0!==y[l],d&&c(_,l)||(f=d?y[l]:n[l],_[l]=h&&"function"!=typeof y[l]?n[l]:m&&d?r(f,a):b&&y[l]==f?function(e){var t=function(t,n,a){if(this instanceof e){switch(arguments.length){case 0:return new e;case 1:return new e(t);case 2:return new e(t,n)}return new e(t,n,a)}return e.apply(this,arguments)};return t[u]=e[u],t}(f):g&&"function"==typeof f?r(Function.call,f):f,g&&((_.virtual||(_.virtual={}))[l]=f,e&s.R&&x&&!x[l]&&i(x,l,f)))};s.F=1,s.G=2,s.S=4,s.P=8,s.B=16,s.W=32,s.U=64,s.R=128,e.exports=s},"794b":function(e,t,n){e.exports=!n("8e60")&&!n("294c")(function(){return 7!=Object.defineProperty(n("1ec9")("div"),"a",{get:function(){return 7}}).a})},"79aa":function(e,t){e.exports=function(e){if("function"!=typeof e)throw TypeError(e+" is not a function!");return e}},"85f2":function(e,t,n){e.exports=n("454f")},"8e60":function(e,t,n){e.exports=!n("294c")(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},a481:function(e,t,n){"use strict";var a=n("cb7c"),o=n("4bf8"),r=n("9def"),i=n("4588"),c=n("0390"),u=n("5f1b"),s=Math.max,l=Math.min,d=Math.floor,f=/\$([$&`']|\d\d?|<[^>]*>)/g,p=/\$([$&`']|\d\d?)/g,h=function(e){return void 0===e?e:String(e)};n("214f")("replace",2,function(e,t,n,v){return[function(a,o){var r=e(this),i=void 0==a?void 0:a[t];return void 0!==i?i.call(a,r,o):n.call(String(r),a,o)},function(e,t){var o=v(n,e,this,t);if(o.done)return o.value;var d=a(e),f=String(this),p="function"===typeof t;p||(t=String(t));var m=d.global;if(m){var b=d.unicode;d.lastIndex=0}var _=[];while(1){var x=u(d,f);if(null===x)break;if(_.push(x),!m)break;var y=String(x[0]);""===y&&(d.lastIndex=c(f,r(d.lastIndex),b))}for(var w="",k=0,S=0;S<_.length;S++){x=_[S];for(var $=String(x[0]),M=s(l(i(x.index),f.length),0),j=[],E=1;E<x.length;E++)j.push(h(x[E]));var R=x.groups;if(p){var O=[$].concat(j,M,f);void 0!==R&&O.push(R);var U=String(t.apply(void 0,O))}else U=g($,f,M,j,R,t);M>=k&&(w+=f.slice(k,M)+U,k=M+$.length)}return w+f.slice(k)}];function g(e,t,a,r,i,c){var u=a+e.length,s=r.length,l=p;return void 0!==i&&(i=o(i),l=f),n.call(c,l,function(n,o){var c;switch(o.charAt(0)){case"$":return"$";case"&":return e;case"`":return t.slice(0,a);case"'":return t.slice(u);case"<":c=i[o.slice(1,-1)];break;default:var l=+o;if(0===l)return n;if(l>s){var f=d(l/10);return 0===f?n:f<=s?void 0===r[f-1]?o.charAt(1):r[f-1]+o.charAt(1):n}c=r[l-1]}return void 0===c?"":c})}})},aebd:function(e,t){e.exports=function(e,t){return{enumerable:!(1&e),configurable:!(2&e),writable:!(4&e),value:t}}},b0c5:function(e,t,n){"use strict";var a=n("520a");n("5ca1")({target:"RegExp",proto:!0,forced:a!==/./.exec},{exec:a})},d864:function(e,t,n){var a=n("79aa");e.exports=function(e,t,n){if(a(e),void 0===t)return e;switch(n){case 1:return function(n){return e.call(t,n)};case 2:return function(n,a){return e.call(t,n,a)};case 3:return function(n,a,o){return e.call(t,n,a,o)}}return function(){return e.apply(t,arguments)}}},d9f6:function(e,t,n){var a=n("e4ae"),o=n("794b"),r=n("1bc3"),i=Object.defineProperty;t.f=n("8e60")?Object.defineProperty:function(e,t,n){if(a(e),t=r(t,!0),a(n),o)try{return i(e,t,n)}catch(c){}if("get"in n||"set"in n)throw TypeError("Accessors not supported!");return"value"in n&&(e[t]=n.value),e}},e4ae:function(e,t,n){var a=n("f772");e.exports=function(e){if(!a(e))throw TypeError(e+" is not an object!");return e}},e53d:function(e,t){var n=e.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=n)},f023:function(e,t,n){},f772:function(e,t){e.exports=function(e){return"object"===typeof e?null!==e:"function"===typeof e}}}]);