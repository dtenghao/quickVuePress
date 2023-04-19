<template><div><h1 id="环境配置" tabindex="-1"><a class="header-anchor" href="#环境配置" aria-hidden="true">#</a> 环境配置</h1>
<p>安装Node.js 全部使用默认的配置，一路下一步即可</p>
<p>打开命令行工具，输入命令 node -v 以及npm -v检查是否安装成功</p>
<p>通过命令 <code v-pre>npm install -g @vue/cli-service-global</code>安装一个小工具</p>
<p>在<code v-pre>.vue</code>文件所在路径下打开终端 输入 <code v-pre>vue serve 文件名</code></p>
<p>等待 解析，然后在浏览器访问出现的地址即可</p>
<p><strong>注意：</strong></p>
<ol>
<li>template中必须有一个根节点</li>
<li>script中的data写成函数，内部返回一个对象</li>
<li>如果要使用写好的样式，直接import即可</li>
</ol>
<h1 id="基本结构" tabindex="-1"><a class="header-anchor" href="#基本结构" aria-hidden="true">#</a> 基本结构</h1>
<p>后缀名是<code v-pre>.vue</code>，可以同时编写结构，逻辑和样式</p>
<p><code v-pre>template</code>标签中写结构</p>
<p><code v-pre>script</code>标签中写逻辑</p>
<p><code v-pre>style</code>标签中写样式</p>
<hr>
<h1 id="使用外部组件" tabindex="-1"><a class="header-anchor" href="#使用外部组件" aria-hidden="true">#</a> 使用外部组件</h1>
<p>不再像之前用&lt;script&gt;引入，而是</p>
<p>使用npm 下载别人写好的包（模块，库）</p>
<p>比如 axios，下载的命令是<code v-pre>npm install axios</code> 或者缩写为<code v-pre>npm i axios</code></p>
<p>在要使用的组件中，使用import导入下载的包（模块，库）</p>
<p>比如 axios：导入的代码是import axios from 'axios'</p>
<h1 id="组件抽取" tabindex="-1"><a class="header-anchor" href="#组件抽取" aria-hidden="true">#</a> 组件抽取</h1>
<p>写好.vue代码</p>
<p>在另一个文件中使用import导入</p>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>import player from '路径.vue'
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>在<code v-pre>components</code>中添加（注册）</p>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>//在export default中写入
components:{
	player:player
}
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>页面上使用注册的名字当作标签名即可使用</p>
</div></template>


