(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-749d6659"],{"3e10":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("Card",{staticClass:"card-top"},[n("div",{attrs:{slot:"title"},slot:"title"},[n("h3",{staticStyle:{"margin-bottom":"5px"}},[t._v(t._s(t.content.title))]),n("span",{staticStyle:{"margin-top":"5px"}},[t._v("更新日期："+t._s(t.content.time)+" 作者："+t._s(t.content.author)+" "),""!=t.content.changer?n("span",[t._v("修改人："+t._s(t.content.changer))]):t._e()])]),t.width?n("div",{attrs:{slot:"extra"},slot:"extra"},[0==t.$Cookies.get("group")?n("Button",{attrs:{type:"warning",size:"large"},on:{click:function(e){return t.$router.push({name:"change_article",query:{id:t.$route.query.id}})}}},[t._v("修改文章\n        ")]):t._e(),0==t.$Cookies.get("group")?n("Button",{staticStyle:{"margin-left":"8px"},attrs:{type:"error",size:"large"},on:{click:t.delete_article}},[t._v("清除文章\n        ")]):t._e()],1):t._e(),t.width?t._e():n("div",{staticStyle:{margin:"5px","text-align":"center"}},[0==t.$Cookies.get("group")?n("Button",{attrs:{type:"warning",size:"large"},on:{click:function(e){return t.$router.push({name:"change_article",query:{id:t.$route.query.id}})}}},[t._v("修改文章\n        ")]):t._e(),0==t.$Cookies.get("group")?n("Button",{staticStyle:{"margin-left":"8px"},attrs:{type:"error",size:"large"},on:{click:function(e){t.show_delete=!0}}},[t._v("清除文章\n        ")]):t._e()],1),n("div",[n("div",{attrs:{id:"toolbar",hidden:""}}),n("quill-editor",{attrs:{options:t.options,disabled:""},model:{value:t.content.content,callback:function(e){t.$set(t.content,"content",e)},expression:"content.content"}})],1),n("Modal",{attrs:{title:"是否清除"},on:{"on-ok":t.delete_article,"on-cancel":function(e){t.show_delete=!1}},model:{value:t.show_delete,callback:function(e){t.show_delete=e},expression:"show_delete"}},[n("p",[t._v("你确定要清除这篇文章吗")])])],1)},i=[],o=n("1487"),r=n.n(o),c=(n("6e2e"),n("9339")),l=n("f318"),s=n.n(l),u=n("5dde"),d=n("3b2f");window.katex=d;var g=n("06ea");c["register"](g.TableCell),c["register"](g.TableRow),c["register"](g.Table),c["register"](g.Contain),c["register"]("modules/table",g.TableModule),c["register"]("modules/imageResize",s.a),c["register"]("modules/ImageExtend",u["a"]);for(var _=10,h=5,p=[],f=1;f<=_;f++)for(var v=1;v<=h;v++)p.push("newtable_"+f+"_"+v);var m={name:"article_view",data:function(){return{show_delete:!1,width:!0,content:{title:"加载中",content:"<p>Loading...</p>"},options:{readOnly:!0,modules:{formula:!0,syntax:{highlight:function(t){return r.a.highlightAuto(t).value}},table:{},toolbar:"#toolbar"}}}},watch:{$route:"get_article"},methods:{delete_article:function(){var t=this,e={article_id:this.$route.query.id,token:this.$Cookies.get("token")};this.$api.article.delete_article(e).then(function(e){1===e.data.code&&(t.get_tag_tree(),t.$router.back())})},get_tag_tree:function(){var t=this;this.$api.tag.get_tag_tree().then(function(e){1===e.data.code&&t.$store.commit("update_tag",e.data.data)})},get_article:function(){var t=this;this.content="<p>加载中...</p>";var e=this.$route.query.id;this.$api.article.get_article(e).then(function(e){1===e.data.code?t.content=e.data.data:t.$router.back()})}},mounted:function(){this.get_article(),this.width=document.documentElement.clientWidth>900}},w=m,b=(n("6d57"),n("598a"),n("2877")),k=Object(b["a"])(w,a,i,!1,null,"ebd0653a",null);e["default"]=k.exports},"598a":function(t,e,n){"use strict";var a=n("601e"),i=n.n(a);i.a},"601e":function(t,e,n){},"6d57":function(t,e,n){"use strict";var a=n("7712"),i=n.n(a);i.a},7712:function(t,e,n){}}]);