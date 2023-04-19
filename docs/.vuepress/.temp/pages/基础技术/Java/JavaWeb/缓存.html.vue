<template><div><h1 id="会话" tabindex="-1"><a class="header-anchor" href="#会话" aria-hidden="true">#</a> 会话</h1>
<p>用户打开浏览器，点击了很多超链接，访问多个web资源，关闭浏览器，这个过程可以称之为会话。如果web会对用户访问信息进行保存，我们称之为<strong>有状态会话</strong></p>
<h1 id="保存会话的两个技术" tabindex="-1"><a class="header-anchor" href="#保存会话的两个技术" aria-hidden="true">#</a> 保存会话的两个技术</h1>
<h2 id="cookie" tabindex="-1"><a class="header-anchor" href="#cookie" aria-hidden="true">#</a> cookie</h2>
<ul>
<li>客户端技术（响应，请求）</li>
</ul>
<ol>
<li>从请求中拿到cookie信息</li>
<li>服务器响应给客户端cookie</li>
</ol>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token class-name">Cookie</span><span class="token punctuation">[</span><span class="token punctuation">]</span> cookies <span class="token operator">=</span> req<span class="token punctuation">.</span><span class="token function">getCookies</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//获得cookie</span>
cookie<span class="token punctuation">.</span><span class="token function">getName</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//获得cookie中的key</span>
cookie<span class="token punctuation">.</span><span class="token function">getValue</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//获得cookie中的value</span>
<span class="token keyword">new</span> <span class="token class-name">Cookie</span><span class="token punctuation">(</span><span class="token string">"lastLoginTime"</span><span class="token punctuation">,</span> <span class="token class-name">System</span><span class="token punctuation">.</span><span class="token function">currentTimeMillis</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">+</span><span class="token string">""</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">//新建一个cookie</span>
cookie<span class="token punctuation">.</span><span class="token function">setMaxAge</span><span class="token punctuation">(</span><span class="token number">24</span><span class="token operator">*</span><span class="token number">60</span><span class="token operator">*</span><span class="token number">60</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//设置cookie的有效期为一天</span>
resp<span class="token punctuation">.</span><span class="token function">addCookie</span><span class="token punctuation">(</span>cookie<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//响应给客户端cookie</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>设置中文cookies时可能会存在<strong>乱码</strong></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token class-name">String</span> s <span class="token operator">=</span> <span class="token class-name">URLEncoder</span><span class="token punctuation">.</span><span class="token function">encode</span><span class="token punctuation">(</span><span class="token string">"中文"</span><span class="token punctuation">,</span> <span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//编码</span>
<span class="token class-name">URLDecoder</span><span class="token punctuation">.</span><span class="token function">decode</span><span class="token punctuation">(</span>s<span class="token punctuation">,</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>	<span class="token comment">//解码</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="session" tabindex="-1"><a class="header-anchor" href="#session" aria-hidden="true">#</a> session</h2>
<ul>
<li>服务器技术，利用这个技术，可以保存用户的会话信息，我们可以把信息或者数据放到Session中</li>
<li>服务器会给每个用户（浏览器）创建一个Session对象</li>
<li>一个Session独占一个浏览器，只要浏览器没有关闭，这个Session就存在</li>
<li>用户登录之后，整个网站它都可以访问！</li>
</ul>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">//得到Session</span>
<span class="token class-name">HttpSession</span> session <span class="token operator">=</span> req<span class="token punctuation">.</span><span class="token function">getSession</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//给Session中存东西</span>
session<span class="token punctuation">.</span><span class="token function">setAttribute</span><span class="token punctuation">(</span><span class="token string">"name"</span><span class="token punctuation">,</span><span class="token string">"邓腾浩"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//获取Session的ID</span>
<span class="token class-name">String</span> id <span class="token operator">=</span> session<span class="token punctuation">.</span><span class="token function">getId</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//移除某个session属性</span>
session<span class="token punctuation">.</span><span class="token function">removeAttribute</span><span class="token punctuation">(</span><span class="token string">"name"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//手动注销Session</span>
session<span class="token punctuation">.</span><span class="token function">invalidate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token comment">&lt;!--设置Session默认的失效时间--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>session-config</span><span class="token punctuation">></span></span>
    <span class="token comment">&lt;!--以分钟为单位--></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>session-timeout</span><span class="token punctuation">></span></span>1<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>session-timeout</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>session-config</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>这段代码意味着一分钟后session将过期。</p>
<h2 id="区别" tabindex="-1"><a class="header-anchor" href="#区别" aria-hidden="true">#</a> 区别</h2>
<ul>
<li>Cookie是把用户的数据写给用户的浏览器，浏览器保存（可以保存多个）</li>
<li>Session把用户的数据写到用户独占Session中，服务器端保存</li>
<li>Session对象由服务器创建，</li>
</ul>
</div></template>


