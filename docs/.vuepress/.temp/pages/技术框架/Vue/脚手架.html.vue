<template><div><h1 id="vue-cli-安装" tabindex="-1"><a class="header-anchor" href="#vue-cli-安装" aria-hidden="true">#</a> vue-cli 安装</h1>
<p>确保Node.js安装成功</p>
<p>通过命令<code v-pre>npm install -g @vue/cli</code>安装一个小工具</p>
<p>创建项目<code v-pre>vue create play</code></p>
<h1 id="vue-router-安装" tabindex="-1"><a class="header-anchor" href="#vue-router-安装" aria-hidden="true">#</a> vue-router 安装</h1>
<p>在项目的根目录打开终端</p>
<p>通过命令 <code v-pre>cnpm install vue-router --save</code> 下载</p>
<p><code v-pre>main.js</code> 中</p>
<ol>
<li>导入</li>
<li>use 一下</li>
<li>创建路由</li>
<li>挂载到Vue实例上</li>
</ol>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>import VueRouter from 'vue-router'
Vue.use(VueRouter)

let router = new VueRouter({
})
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="配置规则" tabindex="-1"><a class="header-anchor" href="#配置规则" aria-hidden="true">#</a> 配置规则</h2>
<p><code v-pre>main.js</code>中</p>
<ol>
<li>导入组件</li>
<li>routes 属性中进行配置关系</li>
<li>path:设置地址</li>
<li>component：设置组件</li>
<li>可以配置多个</li>
</ol>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>import VueRouter from 'vue-router'
Vue.use(VueRouter)

import test from './components/test.vue'
let router = new VueRouter({
  routes: [
    {
      path: "/test",
      component: test
    }
  ]
})
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在页面中定义标签<code v-pre>&lt;router-view&gt;&lt;/router-view&gt;</code></p>
<p>在当前页面下访问该路由，该组件就会被切换</p>
<h2 id="声明式导航" tabindex="-1"><a class="header-anchor" href="#声明式导航" aria-hidden="true">#</a> 声明式导航</h2>
<p>通过<code v-pre>router-link</code>标签 设置to属性为地址 可以实现点击切换</p>
<h2 id="编程式导航" tabindex="-1"><a class="header-anchor" href="#编程式导航" aria-hidden="true">#</a> 编程式导航</h2>
<p>组件中通过 this.$router.push(地址) 可以通过代码实现切换</p>
<h2 id="路由传参" tabindex="-1"><a class="header-anchor" href="#路由传参" aria-hidden="true">#</a> 路由传参</h2>
<p>在地址的后面 写上？分隔</p>
<p>通过 key=value&amp;key2=value 的方式添加参数</p>
<p>组件中通过<code v-pre>this.$route.query</code> 访问对应的key即可获得数据</p>
<hr>
<h1 id="element-ui" tabindex="-1"><a class="header-anchor" href="#element-ui" aria-hidden="true">#</a> Element-ui</h1>
<p>在项目的根目录打开终端</p>
<p>通过命令 <code v-pre>cnpm i element-ui --save</code>下载</p>
<p><code v-pre>main.js中</code></p>
<ol>
<li>导入Element-ui</li>
<li>导入样式</li>
<li>use 一下</li>
</ol>
<div class="language-javascript line-numbers-mode" data-ext="js"><pre v-pre class="language-javascript"><code><span class="token comment">// 导入element-ui</span>
<span class="token keyword">import</span> ElementUI <span class="token keyword">from</span> <span class="token string">'element-ui'</span><span class="token punctuation">;</span>
<span class="token comment">// 导入element-ui的样式</span>
<span class="token keyword">import</span> <span class="token string">'element-ui/lib/theme-chalk/index.css'</span>
Vue<span class="token punctuation">.</span><span class="token function">use</span><span class="token punctuation">(</span>ElementUI<span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="基本目录结构" tabindex="-1"><a class="header-anchor" href="#基本目录结构" aria-hidden="true">#</a> 基本目录结构</h1>
<p>public/favicon.icon     图标</p>
<p>public/index.html      页面模板，不用管</p>
<p>src/assets          静态资源</p>
<p>src/components          组件</p>
<p>src/App.vue            顶级组件</p>
<h1 id="props-emit" tabindex="-1"><a class="header-anchor" href="#props-emit" aria-hidden="true">#</a> props&amp;emit</h1>
<p>props 在 子组件中 设置，作用是定义允许父组件传入的值</p>
<p>emit 在 子组件 中触发，通过他可以触发父组件中注册的事件，甚至 传递参数</p>
</div></template>


