(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-664f6263"],{2985:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("Card",{staticStyle:{"margin-top":"20px"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("\n        添加文章\n    ")]),a("Form",{attrs:{"label-width":100}},[a("FormItem",{attrs:{label:"标题"}},[a("Input",{model:{value:t.title,callback:function(e){t.title=e},expression:"title"}})],1),a("FormItem",{attrs:{label:"标签"}},[a("Input",{model:{value:t.tag,callback:function(e){t.tag=e},expression:"tag"}})],1),a("FormItem",{attrs:{label:"正文"}},[a("div",{staticStyle:{height:"70vh"}},[a("quill-editor",{staticStyle:{height:"90%"},attrs:{options:t.options},model:{value:t.content,callback:function(e){t.content=e},expression:"content"}})],1)]),a("FormItem",[a("Button",{attrs:{type:"primary"},on:{click:t.add_article}},[t._v("提交")]),a("Button",{staticStyle:{"margin-left":"8px"},on:{click:function(e){return t.$router.back()}}},[t._v("取消")])],1)],1)],1)},n=[],o=a("9339"),l=a("f318"),r=a.n(l),c=a("5dde");o["register"]("modules/imageResize",r.a),o["register"]("modules/ImageExtend",c["a"]);var s={name:"change_article",data:function(){return{content:"",title:"",query:"",tag:"",options:{modules:{ImageExtend:{loading:!0,name:"picture",size:3,action:"http://localhost:5000/api/upload/upload_picture",response:function(t){return t.data}},imageResize:{modules:["Resize","DisplaySize","Toolbar"]},toolbar:{container:[["bold","italic","underline","strike"],[{header:[1,2,3,4,!1]},{list:"ordered"},{list:"bullet"}],[{indent:"-1"},{indent:"+1"},{align:[]}],["blockquote","code-block","link","image","formula"],[{color:[]},{background:[]}]],handlers:{image:function(){c["b"].emit(this.quill.id)}}}},placeholder:"请在此输入内容"}}},methods:{add_article:function(){var t=this,e=this,a={title:e.title,content:e.content,tag:this.tag,token:e.$Cookies.get("token"),article_id:this.query.id};this.$api.article.change_article(a).then(function(e){1===e.data.code&&t.$router.back()})}},mounted:function(){var t=this;this.query=this.$route.query,this.$api.article.get_article(this.$route.query.id).then(function(e){1===e.data.code?(t.content=e.data.data.content,t.title=e.data.data.title,t.tag=e.data.data.tag):t.$router.push({name:"login"})})}},u=s,d=(a("f568"),a("2877")),m=Object(d["a"])(u,i,n,!1,null,"612ce1e4",null);e["default"]=m.exports},"9c05":function(t,e,a){},f568:function(t,e,a){"use strict";var i=a("9c05"),n=a.n(i);n.a}}]);