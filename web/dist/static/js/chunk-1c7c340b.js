(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1c7c340b"],{"02f4":function(t,e,n){var r=n("4588"),o=n("be13");t.exports=function(t){return function(e,n){var a,i,c=String(o(e)),u=r(n),s=c.length;return u<0||u>=s?t?"":void 0:(a=c.charCodeAt(u),a<55296||a>56319||u+1===s||(i=c.charCodeAt(u+1))<56320||i>57343?t?c.charAt(u):a:t?c.slice(u,u+2):i-56320+(a-55296<<10)+65536)}}},"0390":function(t,e,n){"use strict";var r=n("02f4")(!0);t.exports=function(t,e,n){return e+(n?r(t,e).length:1)}},"07e3":function(t,e){var n={}.hasOwnProperty;t.exports=function(t,e){return n.call(t,e)}},"0bfb":function(t,e,n){"use strict";var r=n("cb7c");t.exports=function(){var t=r(this),e="";return t.global&&(e+="g"),t.ignoreCase&&(e+="i"),t.multiline&&(e+="m"),t.unicode&&(e+="u"),t.sticky&&(e+="y"),e}},"1bc3":function(t,e,n){var r=n("f772");t.exports=function(t,e){if(!r(t))return t;var n,o;if(e&&"function"==typeof(n=t.toString)&&!r(o=n.call(t)))return o;if("function"==typeof(n=t.valueOf)&&!r(o=n.call(t)))return o;if(!e&&"function"==typeof(n=t.toString)&&!r(o=n.call(t)))return o;throw TypeError("Can't convert object to primitive value")}},"1ec9":function(t,e,n){var r=n("f772"),o=n("e53d").document,a=r(o)&&r(o.createElement);t.exports=function(t){return a?o.createElement(t):{}}},"214f":function(t,e,n){"use strict";n("b0c5");var r=n("2aba"),o=n("32e9"),a=n("79e5"),i=n("be13"),c=n("2b4c"),u=n("520a"),s=c("species"),l=!a(function(){var t=/./;return t.exec=function(){var t=[];return t.groups={a:"7"},t},"7"!=="".replace(t,"$<a>")}),d=function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var n="ab".split(t);return 2===n.length&&"a"===n[0]&&"b"===n[1]}();t.exports=function(t,e,n){var f=c(t),p=!a(function(){var e={};return e[f]=function(){return 7},7!=""[t](e)}),v=p?!a(function(){var e=!1,n=/a/;return n.exec=function(){return e=!0,null},"split"===t&&(n.constructor={},n.constructor[s]=function(){return n}),n[f](""),!e}):void 0;if(!p||!v||"replace"===t&&!l||"split"===t&&!d){var h=/./[f],g=n(i,f,""[t],function(t,e,n,r,o){return e.exec===u?p&&!o?{done:!0,value:h.call(e,n,r)}:{done:!0,value:t.call(n,e,r)}:{done:!1}}),m=g[0],b=g[1];r(String.prototype,t,m),o(RegExp.prototype,f,2==e?function(t,e){return b.call(t,this,e)}:function(t){return b.call(t,this)})}}},"294c":function(t,e){t.exports=function(t){try{return!!t()}catch(e){return!0}}},"35e8":function(t,e,n){var r=n("d9f6"),o=n("aebd");t.exports=n("8e60")?function(t,e,n){return r.f(t,e,o(1,n))}:function(t,e,n){return t[e]=n,t}},4009:function(t,e,n){"use strict";n.r(e);var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"bg",attrs:{id:"login"}},[n("card",{class:{login:!t.login_hidden,loginCamera:!t.photo_hidden},attrs:{bordered:!1}},[n("p",{attrs:{slot:"title"},slot:"title"},[t._v(t._s(t.login_hidden?"人脸验证":"登录实验室"))]),n("i-form",{ref:"login_form",attrs:{model:t.info,rules:t.rule,hidden:t.login_hidden}},[n("form-item",{attrs:{label:"用户名",prop:"username"}},[n("i-input",{attrs:{size:"large",placeholder:"输入用户名"},model:{value:t.info.username,callback:function(e){t.$set(t.info,"username",e)},expression:"info.username"}})],1),n("form-item",{attrs:{label:"密码",prop:"password"}},[n("i-input",{attrs:{type:"password",size:"large",placeholder:"输入密码"},model:{value:t.info.password,callback:function(e){t.$set(t.info,"password",e)},expression:"info.password"}})],1),n("form-item",[n("i-button",{staticStyle:{width:"120px"},attrs:{size:"large",type:"primary"},on:{click:t.check_account}},[t._v("登录")]),n("i-button",{staticStyle:{"margin-left":"10px",width:"120px"},attrs:{size:"large",type:"success"},on:{click:t.jump}},[t._v("注册\n                ")])],1)],1),n("i-form",{attrs:{hidden:t.photo_hidden}},[n("FormItem",[n("video",{staticStyle:{"max-width":"100%","max-height":"50vh"},attrs:{height:"auto",width:"100%",autoplay:"autoplay"}}),n("canvas",{attrs:{id:"canvas1",hidden:!0,width:"1000px",height:"800px"}})]),n("FormItem",[n("i-button",{attrs:{type:"primary",disabled:!t.button_enable,size:"large"},domProps:{textContent:t._s(t.button_text)},on:{click:t.draw_photo}}),t.open_camera?n("i-button",{staticStyle:{"margin-left":"8px"},attrs:{type:"primary",size:"large"},on:{click:t.getMedia}},[t._v("\n                    开启摄像头\n                ")]):t._e()],1)],1)],1),n("modal",{attrs:{title:"提示"},model:{value:t.closable_modal,callback:function(e){t.closable_modal=e},expression:"closable_modal"}},[n("p",{domProps:{textContent:t._s(t.alert_info)}})]),n("modal",{attrs:{title:"请稍候",closable:!1,"mask-closable":!1,loading:!0},model:{value:t.loading_modal,callback:function(e){t.loading_modal=e},expression:"loading_modal"}},[n("p",[t._v("正在进行人脸检测...")])])],1)},o=[],a=n("85f2"),i=n.n(a);function c(t,e,n){return e in t?i()(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}n("a481");var u,s={name:"login",data:function(){return{open_camera:!1,info:{username:"",password:""},rule:{username:[{required:!0,message:"用户名不能为空",trigger:"blur"}],password:[{required:!0,message:"密码不能为空",trigger:"blur"},{type:"string",min:6,message:"密码长度必须大于6位",trigger:"blur"}]},login_hidden:!1,photo_hidden:!0,video:null,exArray:[],canvas:null,context:null,button_text:"人脸识别",button_enable:!1,alert_info:"",closable_modal:!1,loading_modal:!1}},methods:(u={check_account:function(){var t=this,e=this;this.$refs["login_form"].validate(function(n){n&&t.$api.account.check_account(t.info).then(function(t){1===t.data.code?e.goto_photo():(e.alert_info="用户名或密码错误",e.closable_modal=!0,e.loading_modal=!1)})})},goto_photo:function(){this.login_hidden=!0,this.photo_hidden=!1,this.getMedia()},goto_login:function(){this.login_hidden=!1,this.photo_hidden=!0},getMedia:function(){var t=this;navigator.getUserMedia=navigator.getUserMedia||navigator.webkitGetUserMedia||navigator.mozGetUserMedia||navigator.msGetUserMedia,window.URL=window.URL||window.webkitURL||window.mozURL||window.msURL,navigator.mediaDevices.enumerateDevices().then(function(e){for(var n=0;n!=e.length;++n){var r=e[n];"video"===r.kind&&t.exArray.push(r.id)}}),navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:t.exArray[0]}]},audio:!1},t.successFunc,t.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser.")},successFunc:function(t){void 0!==this.video.mozSrcObject?this.video.mozSrcObject=t:this.video.srcObject=t,this.video.play(),this.button_enable=!0},errorFunc:function(t){this.closable_modal=!0,this.alert_info="错误:"+t},draw_photo:function(){var t=this;t.button_text="正在检测",t.button_enable=!1,setTimeout(function(){t.button_enable=!0,t.button_text="请重新识别"},5e3),t.context.drawImage(t.video,0,0,1e3,800);var e=t.canvas.toDataURL("image/png",1);e=e.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,"");var r={username:t.info.username,face:e};this.$api.face.check(r).then(function(e){1===e.data.code&&e.data.data>80&&t.$api.account.login(t.info).then(function(e){1===e.data.code&&Promise.resolve().then(n.t.bind(null,"a78e",7)).then(function(n){n.set("token",e.data.data.token),t.$store.commit("save",e.data.data),t.$store.commit("update_token",e.data.data.token),t.loading_modal=!1,t.$router.push({name:"mainpage"})})})}),navigator.getUserMedia?navigator.getUserMedia({video:{optional:[{sourceId:t.exArray[0]}]},audio:!1},t.successFunc,t.errorFunc):alert("Native device media streaming (getUserMedia) not supported in this browser.")}},c(u,"successFunc",function(t){void 0!==this.video.mozSrcObject?this.video.mozSrcObject=t:this.video.srcObject=t,this.video.play(),this.button_enable=!0}),c(u,"errorFunc",function(t){alert("Error！"+t),this.open_camera=!0}),c(u,"draw_photo",function(){var t=this;t.button_text="正在检测",t.button_enable=!1,setTimeout(function(){t.button_enable=!0},5e3),t.context.drawImage(t.video,0,0,160,120);var e=t.canvas.toDataURL("image/png",1);e=e.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,"");var r={username:t.info.username,face:e};this.$api.face.check(r).then(function(e){1===e.data.code?e.data.data>80?t.$api.account.login(t.info).then(function(e){1===e.data.code&&Promise.resolve().then(n.t.bind(null,"a78e",7)).then(function(n){n.set("token",e.data.data.token),n.set("group",e.data.data.group),t.$store.commit("save",e.data.data),t.$store.commit("update_token",e.data.data.token),t.loading_modal=!1,t.$router.push({name:"default"})})}):(t.alert_info="人脸相似度过低，请重新校验",t.closable_modal=!0,t.loading_modal=!1,t.button_enable=!0):(t.alert_info="人脸校验失败",t.closable_modal=!0,t.loading_modal=!1,t.button_enable=!0)})}),c(u,"jump",function(){this.$router.push({name:"register"})}),u),mounted:function(){this.video=document.querySelector("video"),this.canvas=document.getElementById("canvas1"),this.context=this.canvas.getContext("2d")}},l=s,d=(n("70f4"),n("2877")),f=Object(d["a"])(l,r,o,!1,null,"346ed752",null);e["default"]=f.exports},"454f":function(t,e,n){n("46a7");var r=n("584a").Object;t.exports=function(t,e,n){return r.defineProperty(t,e,n)}},"46a7":function(t,e,n){var r=n("63b6");r(r.S+r.F*!n("8e60"),"Object",{defineProperty:n("d9f6").f})},"520a":function(t,e,n){"use strict";var r=n("0bfb"),o=RegExp.prototype.exec,a=String.prototype.replace,i=o,c="lastIndex",u=function(){var t=/a/,e=/b*/g;return o.call(t,"a"),o.call(e,"a"),0!==t[c]||0!==e[c]}(),s=void 0!==/()??/.exec("")[1],l=u||s;l&&(i=function(t){var e,n,i,l,d=this;return s&&(n=new RegExp("^"+d.source+"$(?!\\s)",r.call(d))),u&&(e=d[c]),i=o.call(d,t),u&&i&&(d[c]=d.global?i.index+i[0].length:e),s&&i&&i.length>1&&a.call(i[0],n,function(){for(l=1;l<arguments.length-2;l++)void 0===arguments[l]&&(i[l]=void 0)}),i}),t.exports=i},"584a":function(t,e){var n=t.exports={version:"2.6.5"};"number"==typeof __e&&(__e=n)},"5f1b":function(t,e,n){"use strict";var r=n("23c6"),o=RegExp.prototype.exec;t.exports=function(t,e){var n=t.exec;if("function"===typeof n){var a=n.call(t,e);if("object"!==typeof a)throw new TypeError("RegExp exec method returned something other than an Object or null");return a}if("RegExp"!==r(t))throw new TypeError("RegExp#exec called on incompatible receiver");return o.call(t,e)}},"63b6":function(t,e,n){var r=n("e53d"),o=n("584a"),a=n("d864"),i=n("35e8"),c=n("07e3"),u="prototype",s=function(t,e,n){var l,d,f,p=t&s.F,v=t&s.G,h=t&s.S,g=t&s.P,m=t&s.B,b=t&s.W,_=v?o:o[e]||(o[e]={}),x=_[u],y=v?r:h?r[e]:(r[e]||{})[u];for(l in v&&(n=e),n)d=!p&&y&&void 0!==y[l],d&&c(_,l)||(f=d?y[l]:n[l],_[l]=v&&"function"!=typeof y[l]?n[l]:m&&d?a(f,r):b&&y[l]==f?function(t){var e=function(e,n,r){if(this instanceof t){switch(arguments.length){case 0:return new t;case 1:return new t(e);case 2:return new t(e,n)}return new t(e,n,r)}return t.apply(this,arguments)};return e[u]=t[u],e}(f):g&&"function"==typeof f?a(Function.call,f):f,g&&((_.virtual||(_.virtual={}))[l]=f,t&s.R&&x&&!x[l]&&i(x,l,f)))};s.F=1,s.G=2,s.S=4,s.P=8,s.B=16,s.W=32,s.U=64,s.R=128,t.exports=s},"70f4":function(t,e,n){"use strict";var r=n("c1c1"),o=n.n(r);o.a},"794b":function(t,e,n){t.exports=!n("8e60")&&!n("294c")(function(){return 7!=Object.defineProperty(n("1ec9")("div"),"a",{get:function(){return 7}}).a})},"79aa":function(t,e){t.exports=function(t){if("function"!=typeof t)throw TypeError(t+" is not a function!");return t}},"85f2":function(t,e,n){t.exports=n("454f")},"8e60":function(t,e,n){t.exports=!n("294c")(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},a481:function(t,e,n){"use strict";var r=n("cb7c"),o=n("4bf8"),a=n("9def"),i=n("4588"),c=n("0390"),u=n("5f1b"),s=Math.max,l=Math.min,d=Math.floor,f=/\$([$&`']|\d\d?|<[^>]*>)/g,p=/\$([$&`']|\d\d?)/g,v=function(t){return void 0===t?t:String(t)};n("214f")("replace",2,function(t,e,n,h){return[function(r,o){var a=t(this),i=void 0==r?void 0:r[e];return void 0!==i?i.call(r,a,o):n.call(String(a),r,o)},function(t,e){var o=h(n,t,this,e);if(o.done)return o.value;var d=r(t),f=String(this),p="function"===typeof e;p||(e=String(e));var m=d.global;if(m){var b=d.unicode;d.lastIndex=0}var _=[];while(1){var x=u(d,f);if(null===x)break;if(_.push(x),!m)break;var y=String(x[0]);""===y&&(d.lastIndex=c(f,a(d.lastIndex),b))}for(var w="",k=0,S=0;S<_.length;S++){x=_[S];for(var $=String(x[0]),j=s(l(i(x.index),f.length),0),M=[],E=1;E<x.length;E++)M.push(v(x[E]));var U=x.groups;if(p){var R=[$].concat(M,j,f);void 0!==U&&R.push(U);var O=String(e.apply(void 0,R))}else O=g($,f,j,M,U,e);j>=k&&(w+=f.slice(k,j)+O,k=j+$.length)}return w+f.slice(k)}];function g(t,e,r,a,i,c){var u=r+t.length,s=a.length,l=p;return void 0!==i&&(i=o(i),l=f),n.call(c,l,function(n,o){var c;switch(o.charAt(0)){case"$":return"$";case"&":return t;case"`":return e.slice(0,r);case"'":return e.slice(u);case"<":c=i[o.slice(1,-1)];break;default:var l=+o;if(0===l)return n;if(l>s){var f=d(l/10);return 0===f?n:f<=s?void 0===a[f-1]?o.charAt(1):a[f-1]+o.charAt(1):n}c=a[l-1]}return void 0===c?"":c})}})},aebd:function(t,e){t.exports=function(t,e){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:e}}},b0c5:function(t,e,n){"use strict";var r=n("520a");n("5ca1")({target:"RegExp",proto:!0,forced:r!==/./.exec},{exec:r})},c1c1:function(t,e,n){},d864:function(t,e,n){var r=n("79aa");t.exports=function(t,e,n){if(r(t),void 0===e)return t;switch(n){case 1:return function(n){return t.call(e,n)};case 2:return function(n,r){return t.call(e,n,r)};case 3:return function(n,r,o){return t.call(e,n,r,o)}}return function(){return t.apply(e,arguments)}}},d9f6:function(t,e,n){var r=n("e4ae"),o=n("794b"),a=n("1bc3"),i=Object.defineProperty;e.f=n("8e60")?Object.defineProperty:function(t,e,n){if(r(t),e=a(e,!0),r(n),o)try{return i(t,e,n)}catch(c){}if("get"in n||"set"in n)throw TypeError("Accessors not supported!");return"value"in n&&(t[e]=n.value),t}},e4ae:function(t,e,n){var r=n("f772");t.exports=function(t){if(!r(t))throw TypeError(t+" is not an object!");return t}},e53d:function(t,e){var n=t.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=n)},f772:function(t,e){t.exports=function(t){return"object"===typeof t?null!==t:"function"===typeof t}}}]);