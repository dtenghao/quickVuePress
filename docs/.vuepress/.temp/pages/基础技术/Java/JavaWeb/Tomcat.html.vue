<template><div><h1 id="开启" tabindex="-1"><a class="header-anchor" href="#开启" aria-hidden="true">#</a> 开启</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200811195823608.png" alt="image-20200811195823608"></p>
<p>访问测试http://localhost:8080/</p>
<h1 id="配置" tabindex="-1"><a class="header-anchor" href="#配置" aria-hidden="true">#</a> 配置</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200811200022784.png" alt="image-20200811200022784"></p>
<p>可以配置启动的端口号</p>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>Connector</span> <span class="token attr-name">port</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>8080<span class="token punctuation">"</span></span> <span class="token attr-name">protocol</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>HTTP/1.1<span class="token punctuation">"</span></span>
	<span class="token attr-name">connectionTimeout</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>20000<span class="token punctuation">"</span></span>
	<span class="token attr-name">redirectPort</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>8443<span class="token punctuation">"</span></span> <span class="token punctuation">/></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>可以配置主机的名称</p>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>Host</span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>localhost<span class="token punctuation">"</span></span>  <span class="token attr-name">appBase</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>webapps<span class="token punctuation">"</span></span>
      <span class="token attr-name">unpackWARs</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span> <span class="token attr-name">autoDeploy</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812110107346.png" alt="image-20200812110107346"></p>
<p>大概在50行左右将<code v-pre>java.util.logging.ConsoleHandler.encoding = UTF-8</code>改为<code v-pre>java.util.logging.ConsoleHandler.encoding = GBK</code></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812110235620.png" alt="image-20200812110235620"></p>
<p><strong>网站是如何访问的：</strong></p>
<ol>
<li>
<p>输入一个域名：回车</p>
</li>
<li>
<p>检查本机的C:\Windows\System32\drivers\etc\hosts配置文件下有没有这个域名映射</p>
<ol>
<li>
<p>有就直接返回对应的ip地址，这个地址中，有我们需要访问的web程序，可以直接访问</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>127.0.0.1		www.dth.com
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>没有就去DNS服务器（全世界的域名都在这里管理）找</p>
</li>
</ol>
</li>
</ol>
<h1 id="响应状态码" tabindex="-1"><a class="header-anchor" href="#响应状态码" aria-hidden="true">#</a> 响应状态码</h1>
<p>200：请求响应成功</p>
<p>3xx：请求重定向</p>
<p>4xx：找不到资源  	404</p>
<p>5xx：服务器代码错误	500   502（网关错误）</p>
</div></template>


