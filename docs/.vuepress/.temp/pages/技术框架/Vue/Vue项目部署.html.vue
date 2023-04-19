<template><div><h1 id="项目build" tabindex="-1"><a class="header-anchor" href="#项目build" aria-hidden="true">#</a> 项目build</h1>
<ol>
<li>在项目根目录下，也就是和<code v-pre>package.json</code>同级的目录下新建一个文件<code v-pre>vue.config.js</code>，在里面写入(有特殊需求可根据注释做相关修改，一般来说下面的配置可以直接用)：</li>
</ol>
<div class="language-javascript line-numbers-mode" data-ext="js"><pre v-pre class="language-javascript"><code>module<span class="token punctuation">.</span>exports <span class="token operator">=</span> <span class="token punctuation">{</span>
  <span class="token literal-property property">publicPath</span><span class="token operator">:</span> process<span class="token punctuation">.</span>env<span class="token punctuation">.</span><span class="token constant">NODE_ENV</span> <span class="token operator">===</span> <span class="token string">"production"</span> <span class="token operator">?</span> <span class="token string">"./"</span> <span class="token operator">:</span> <span class="token string">"./"</span><span class="token punctuation">,</span>
  <span class="token literal-property property">outputDir</span><span class="token operator">:</span> <span class="token string">"dist"</span><span class="token punctuation">,</span>
  <span class="token literal-property property">assetsDir</span><span class="token operator">:</span> <span class="token string">"static"</span><span class="token punctuation">,</span>
  <span class="token literal-property property">indexPath</span><span class="token operator">:</span> <span class="token string">'index.html'</span><span class="token punctuation">,</span>
  <span class="token comment">// eslint-loader 是否在保存的时候检查</span>
  <span class="token literal-property property">lintOnSave</span><span class="token operator">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
  <span class="token comment">// 生产环境是否生成 sourceMap 文件</span>
  <span class="token literal-property property">productionSourceMap</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
  <span class="token comment">// css相关配置</span>
  <span class="token literal-property property">css</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token comment">// 是否使用css分离插件 ExtractTextPlugin</span>
    <span class="token literal-property property">extract</span><span class="token operator">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
    <span class="token comment">// 开启 CSS source maps?</span>
    <span class="token literal-property property">sourceMap</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">// webpack-dev-server 相关配置</span>
  <span class="token literal-property property">devServer</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token literal-property property">open</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span><span class="token comment">//open 在devServer启动且第一次构建完成时，自动用我们的系统的默认浏览器去打开要开发的网页</span>
    <span class="token literal-property property">host</span><span class="token operator">:</span> <span class="token string">'0.0.0.0'</span><span class="token punctuation">,</span><span class="token comment">//默认是 localhost。如果你希望服务器外部可访问，指定如下 host: '0.0.0.0'，设置之后之后可以访问ip地址</span>
    <span class="token literal-property property">port</span><span class="token operator">:</span> <span class="token number">8080</span><span class="token punctuation">,</span>
    <span class="token literal-property property">hot</span><span class="token operator">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span><span class="token comment">//hot配置是否启用模块的热替换功能，devServer的默认行为是在发现源代码被变更后，通过自动刷新整个页面来做到事实预览，开启hot后，将在不刷新整个页面的情况下通过新模块替换老模块来做到实时预览。</span>
    <span class="token literal-property property">https</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token literal-property property">hotOnly</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span><span class="token comment">// hot 和 hotOnly 的区别是在某些模块不支持热更新的情况下，前者会自动刷新页面，后者不会刷新页面，而是在控制台输出热更新失败</span>
    <span class="token literal-property property">proxy</span><span class="token operator">:</span> <span class="token punctuation">{</span>
      <span class="token string-property property">'/apis'</span><span class="token operator">:</span> <span class="token punctuation">{</span>
        <span class="token literal-property property">target</span><span class="token operator">:</span> <span class="token string">'http://xxxx:8080'</span><span class="token punctuation">,</span> <span class="token comment">//目标接口域名</span>
        <span class="token literal-property property">secure</span><span class="token operator">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span> <span class="token comment">//false为http访问，true为https访问</span>
        <span class="token literal-property property">changeOrigin</span><span class="token operator">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span> <span class="token comment">//是否跨域</span>
        <span class="token literal-property property">pathRewrite</span><span class="token operator">:</span> <span class="token punctuation">{</span>
          <span class="token string-property property">'^/apis'</span><span class="token operator">:</span> <span class="token string">'/'</span> <span class="token comment">//重写接口</span>
        <span class="token punctuation">}</span>
      <span class="token punctuation">}</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token comment">// 设置代理</span>
    <span class="token function-variable function">before</span><span class="token operator">:</span> <span class="token parameter">app</span> <span class="token operator">=></span> <span class="token punctuation">{</span> <span class="token punctuation">}</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">// 第三方插件配置</span>
  <span class="token literal-property property">pluginOptions</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token comment">// ...</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="2">
<li>在项目根目录中，对项目进行打包<code v-pre>npm  run build</code>，大多编译器都可以直接打包，如vscode。打包完成后，会在项目根目录下生成一个dist文件夹</li>
</ol>
<h1 id="nginx配置文件修改" tabindex="-1"><a class="header-anchor" href="#nginx配置文件修改" aria-hidden="true">#</a> Nginx配置文件修改</h1>
<p>在你想使用的域名下添加一段代码</p>
<div class="language-nginx line-numbers-mode" data-ext="nginx"><pre v-pre class="language-nginx"><code><span class="token directive"><span class="token keyword">server</span></span> <span class="token punctuation">{</span>
	<span class="token directive"><span class="token keyword">server_name</span> www.xxx.com</span><span class="token punctuation">;</span> <span class="token comment">#你的域名</span>
    <span class="token directive"><span class="token keyword">location</span> /project/</span> <span class="token punctuation">{</span>  <span class="token comment">#设置根目录，访问方式 域名/project </span>
            <span class="token directive"><span class="token keyword">root</span> /usr/share/nginx/html/</span><span class="token punctuation">;</span>  <span class="token comment">#存放项目代码的位置，任意</span>
            <span class="token directive"><span class="token keyword">index</span>  index.html index.htm</span><span class="token punctuation">;</span>
            <span class="token directive"><span class="token keyword">try_files</span> <span class="token variable">$uri</span> <span class="token variable">$uri</span>/ /index.html</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token comment"># 是否需要跨域，不需要就不用管</span>
    <span class="token comment">#location /apis {</span>
        <span class="token comment">#    rewrite  ^.+apis/?(.*)$ /$1 break;</span>
        <span class="token comment">#    proxy_pass  http://xxxx:8080;</span>
        <span class="token comment">#    proxy_redirect off;</span>
        <span class="token comment">#    proxy_set_header Host $host;</span>
        <span class="token comment">#    proxy_set_header X-Real-IP $remote_addr;</span>
        <span class="token comment">#    proxy_set_header X-Forwarded-For 	</span>
        <span class="token comment">#    $proxy_add_x_forwarded_for;</span>
     <span class="token comment"># }</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><code v-pre>nginx -s reload</code>重启下nginx</p>
<p>差不多已经完成了</p>
<p>接下来就只需在服务器上的<code v-pre>/usr/share/nginx/html/</code>文件夹下新建文件夹<code v-pre>project</code>，将刚刚打包好的dist文件夹中的三个文件放到<code v-pre>/usr/share/nginx/html/project</code>下。</p>
<p>ok，现在通过<code v-pre>域名/project</code>访问你的项目吧！</p>
</div></template>


