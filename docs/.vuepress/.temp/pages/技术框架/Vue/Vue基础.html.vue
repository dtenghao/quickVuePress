<template><div><h1 id="起步" tabindex="-1"><a class="header-anchor" href="#起步" aria-hidden="true">#</a> 起步</h1>
<ol>
<li>先引入Vue</li>
</ol>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>https://cdn.jsdelivr.net/npm/vue/dist/vue.js<span class="token punctuation">"</span></span><span class="token punctuation">></span></span><span class="token script"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><ol start="2">
<li>创建vue实例</li>
</ol>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">var</span> app <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">Vue</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
    el<span class="token operator">:</span> <span class="token string">"#app"</span><span class="token punctuation">,</span>
    data<span class="token operator">:</span> <span class="token punctuation">{</span>
      message<span class="token operator">:</span> <span class="token string">"Hello Vue！"</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><code v-pre>#app</code> ：id		<strong>常用</strong></p>
<p><code v-pre>.app</code>: class</p>
<p><code v-pre>div</code>:组件名</p>
<ol start="3">
<li>使用</li>
</ol>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token operator">&lt;</span>div id<span class="token operator">=</span><span class="token string">"app"</span><span class="token operator">></span>
    <span class="token punctuation">{</span><span class="token punctuation">{</span>message<span class="token punctuation">}</span><span class="token punctuation">}</span>
 <span class="token operator">&lt;</span><span class="token operator">/</span>div<span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="v-text指令" tabindex="-1"><a class="header-anchor" href="#v-text指令" aria-hidden="true">#</a> v-text指令</h1>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">v-text</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>msg<span class="token punctuation">"</span></span><span class="token punctuation">></span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">></span></span>
<span class="token comment">&lt;!-- same as --></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">></span></span>{{msg}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="v-html指令" tabindex="-1"><a class="header-anchor" href="#v-html指令" aria-hidden="true">#</a> v-html指令</h1>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-html</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>html<span class="token punctuation">"</span></span><span class="token punctuation">></span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><code v-pre>html</code>会被以html格式解析。</p>
<h1 id="v-on-指令" tabindex="-1"><a class="header-anchor" href="#v-on-指令" aria-hidden="true">#</a> v-on 指令</h1>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>doThis<span class="token punctuation">"</span></span><span class="token punctuation">></span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>绑定事件，也可以用@click代替</p>
<p>事件绑定的方法写成函数调用的形式，可以传入自定义参数</p>
<p>定义方法时需要定义形参来接收传入的实参</p>
<p>事件的后面跟上.修饰符可以为事件进行限制</p>
<p>.enter可以限制触发的按键为回车</p>
<h1 id="v-show-指令" tabindex="-1"><a class="header-anchor" href="#v-show-指令" aria-hidden="true">#</a> v-show 指令</h1>
<p>根据表达值的真假，切换元素的显示和隐藏。</p>
<p>原理是修改元素的display，实现显示隐藏</p>
<p>指令后面的内容，最终都会解析为<strong>布尔值</strong></p>
<h1 id="v-if-指令" tabindex="-1"><a class="header-anchor" href="#v-if-指令" aria-hidden="true">#</a> v-if 指令</h1>
<p>根据表达式的真假切换元素的显示状态</p>
<p>本质是通过操作dom元素来切换显示状态</p>
<p>表达式的值为true，元素存在于dom树中，为false，从dom树中移除。</p>
<p>当我们需要经常切换某个元素的显示/隐藏时，使用v-show会更加节省性能上的开销。</p>
<p>如果在运行时条件很少改变，则使用 v-if 较好。</p>
<h1 id="v-bind-指令" tabindex="-1"><a class="header-anchor" href="#v-bind-指令" aria-hidden="true">#</a> v-bind 指令</h1>
<p>为元素绑定属性</p>
<p>完整写法是v-bind:属性名</p>
<p>简写的话可以直接省略v-bind，只保留<code v-pre>:属性名</code></p>
<p>需要动态的增删class建议使用对象的方式 {classname:isactive}</p>
<h1 id="v-for-指令" tabindex="-1"><a class="header-anchor" href="#v-for-指令" aria-hidden="true">#</a> v-for 指令</h1>
<p>v-for 指令的作用是：根据数据生成列表结构</p>
<p>数组经常和v-for结合使用</p>
<p>语法是(item,index) in 数据</p>
<p>item和index 可以结合其他指令一起使用</p>
<p>数组长度的更新会同步到页面上，是响应式的</p>
<h1 id="v-model-指令" tabindex="-1"><a class="header-anchor" href="#v-model-指令" aria-hidden="true">#</a> v-model 指令</h1>
<p>便捷的设置和获取表单元素的值</p>
<p>绑定的数据会和表单元素值相关联</p>
<p>绑定的数据&lt;——&gt;表单元素的值</p>
<h1 id="axios-网络请求库" tabindex="-1"><a class="header-anchor" href="#axios-网络请求库" aria-hidden="true">#</a> axios 网络请求库</h1>
<p>导包</p>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>https://unpkg.com/axios/dist/axios.min.js<span class="token punctuation">"</span></span><span class="token punctuation">></span></span><span class="token script"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>或者下载</p>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>cnpm install axios --save
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>使用</p>
<div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>axios.get(地址?key=value).then(function(response){},function(err){})
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><div class="language-vue line-numbers-mode" data-ext="vue"><pre v-pre class="language-vue"><code>axios.post(地址,{key:value,key2:value2}).then(function(response){},function(err){})
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></div></template>


