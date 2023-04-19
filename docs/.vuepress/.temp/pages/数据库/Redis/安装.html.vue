<template><div><h1 id="安装配置" tabindex="-1"><a class="header-anchor" href="#安装配置" aria-hidden="true">#</a> 安装配置</h1>
<p>下载地址</p>
<p>https://redis.io/download</p>
<p>在linux服务器上安装</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>yum <span class="token function">install</span> gcc-c++

<span class="token function">make</span> <span class="token assign-left variable">MALLOC</span><span class="token operator">=</span>libc

<span class="token builtin class-name">cd</span> src

<span class="token function">chmod</span> +x mkreleasehdr.sh

<span class="token function">make</span>

<span class="token function">make</span> <span class="token function">install</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>Redis的默认安装路径<code v-pre>/usr/local/bin</code></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926101026971.png" alt="image-20200926101026971"></p>
<p>可以在该文件夹下创建一个配置文件夹，以后redis的配置都在这里面配置就可以了。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">mkdir</span> econfig

<span class="token function">cp</span> /tmp/redis-6.0.8/redis.conf econfig
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>进而修改该配置文件，保持后台启动</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926101726193.png" alt="image-20200926101726193"></p>
<h1 id="启动" tabindex="-1"><a class="header-anchor" href="#启动" aria-hidden="true">#</a> 启动</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926102302794.png" alt="image-20200926102302794"></p>
<p>另外启动一个客户端，<code v-pre>ps -ef|grep redis</code></p>
<h1 id="关闭" tabindex="-1"><a class="header-anchor" href="#关闭" aria-hidden="true">#</a> 关闭</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926102755366.png" alt="image-20200926102755366"></p>
</div></template>


