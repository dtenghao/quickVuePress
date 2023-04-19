<template><div><h1 id="概念" tabindex="-1"><a class="header-anchor" href="#概念" aria-hidden="true">#</a> 概念</h1>
<p>Nginx (engine x) 是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的，第一个公开版本0.1.0发布于2004年10月4日。2011年6月1日，nginx 1.0.4发布。</p>
<p>其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。在全球活跃的网站中有12.18%的使用比率，大约为2220万个网站。</p>
<p>Nginx 是一个安装非常的简单、配置文件非常简洁（还能够支持perl语法）、Bug非常少的服务。Nginx 启动特别容易，并且几乎可以做到7*24不间断运行，即使运行数个月也不需要重新启动。你还能够不间断服务的情况下进行软件版本的升级。</p>
<p>Nginx代码完全用C语言从头写成。官方数据测试表明能够支持高达 50,000 个并发连接数的响应。</p>
<h1 id="作用" tabindex="-1"><a class="header-anchor" href="#作用" aria-hidden="true">#</a> 作用</h1>
<h2 id="反向代理" tabindex="-1"><a class="header-anchor" href="#反向代理" aria-hidden="true">#</a> 反向代理</h2>
<blockquote>
<p>Http代理，反向代理：作为web服务器最常用的功能之一，尤其是反向代理。</p>
</blockquote>
<p>正向代理</p>
<p>代理服务器代理客户端的请求，常见的应用有VPN。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/82ybBZ.jpg" alt="82ybBZ"></p>
<p>反向代理</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/lZALRC.jpg" alt="lZALRC"></p>
<h2 id="负载均衡" tabindex="-1"><a class="header-anchor" href="#负载均衡" aria-hidden="true">#</a> 负载均衡</h2>
<blockquote>
<p>Nginx提供的负载均衡策略有2种：内置策略和扩展策略。内置策略为轮询，加权轮询，Ip hash。扩展策略，就天马行空，只有你想不到的没有他做不到的。</p>
</blockquote>
<p>轮询</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/X6Z37D.jpg" alt="X6Z37D"></p>
<p>加权轮询</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/DtNUlv.jpg" alt="DtNUlv"></p>
<p>iphash对客户端请求的ip进行hash操作，然后根据hash结果将同一个客户端ip的请求分发给同一台服务器进行处理，可以解决session不共享的问题。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/P7HAp3.jpg" alt="P7HAp3"></p>
<h2 id="动静分离" tabindex="-1"><a class="header-anchor" href="#动静分离" aria-hidden="true">#</a> 动静分离</h2>
<blockquote>
<p>动静分离，在我们的软件开发中，有些请求是需要后台处理的，有些请求是不需要经过后台处理的（如：css、html、jpg、js等等文件），这些不需要经过后台处理的文件称为静态文件。让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作。提高资源响应的速度。</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/25/IrrsKz.jpg" alt="IrrsKz"></p>
<p>目前，通过使用Nginx大大提高了我们网站的响应速度，优化了用户体验，让网站的健壮性更上一层楼！</p>
<h1 id="安装" tabindex="-1"><a class="header-anchor" href="#安装" aria-hidden="true">#</a> 安装</h1>
<p>这里在docker中安装使用</p>
<p>下载镜像</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">docker</span> pull nginx
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>启动nginx</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">docker</span> run <span class="token parameter variable">-d</span> <span class="token parameter variable">--name</span> nginx01 <span class="token parameter variable">-p</span> <span class="token number">3334</span>:80 nginx

<span class="token parameter variable">-d</span> 后台运行
<span class="token parameter variable">--name</span> 给容器命名
<span class="token parameter variable">-p</span> <span class="token number">3334</span>:80 将宿主机的端口3334映射到该容器的80端口
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>访问nginx</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>http://localhost:3344/
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/06/26/P87iv5.png" alt="P87iv5"></p>
<h1 id="常用命令" tabindex="-1"><a class="header-anchor" href="#常用命令" aria-hidden="true">#</a> 常用命令</h1>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">cd</span> /usr/local/nginx/sbin/
./nginx  启动
./nginx <span class="token parameter variable">-s</span> stop  停止
./nginx <span class="token parameter variable">-s</span> quit  安全退出
./nginx <span class="token parameter variable">-s</span> reload  重新加载配置文件
<span class="token function">ps</span> aux<span class="token operator">|</span><span class="token function">grep</span> nginx  查看nginx进程
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="配置文件" tabindex="-1"><a class="header-anchor" href="#配置文件" aria-hidden="true">#</a> 配置文件</h1>
<div class="language-nginx line-numbers-mode" data-ext="nginx"><pre v-pre class="language-nginx"><code><span class="token directive"><span class="token keyword">http</span></span> <span class="token punctuation">{</span>
    ...
	<span class="token directive"><span class="token keyword">upstream</span> cvzhanshi</span><span class="token punctuation">{</span>    <span class="token comment"># 配置负载均衡</span>
		<span class="token directive"><span class="token keyword">server</span> 127.0.0.1:8082/ weight=1</span><span class="token punctuation">;</span>  <span class="token comment"># 权重</span>
		<span class="token directive"><span class="token keyword">server</span> 127.0.0.1:8081/ weight=1</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>


    <span class="token directive"><span class="token keyword">server</span></span> <span class="token punctuation">{</span>
        <span class="token directive"><span class="token keyword">listen</span>       <span class="token number">80</span></span><span class="token punctuation">;</span>
        <span class="token directive"><span class="token keyword">server_name</span>  localhost</span><span class="token punctuation">;</span>

        <span class="token directive"><span class="token keyword">location</span> /</span> <span class="token punctuation">{</span>
            <span class="token directive"><span class="token keyword">root</span>   html</span><span class="token punctuation">;</span>
            <span class="token directive"><span class="token keyword">index</span>  index.html index.htm</span><span class="token punctuation">;</span>
			<span class="token directive"><span class="token keyword">proxy_pass</span> http://cvzhanshi</span><span class="token punctuation">;</span>   <span class="token comment"># 80端口</span>
      															<span class="token comment"># 反向代理</span>
        <span class="token punctuation">}</span>
        ...
<span class="token punctuation">}</span>

</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


