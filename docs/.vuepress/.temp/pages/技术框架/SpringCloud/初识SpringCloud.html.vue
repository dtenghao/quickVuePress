<template><div><h1 id="文档" tabindex="-1"><a class="header-anchor" href="#文档" aria-hidden="true">#</a> 文档</h1>
<ul>
<li>Spring Cloud Netflix https://www.springcloud.cc/spring-cloud-netflix.html</li>
<li>中文API文档 https://www.springcloud.cc/spring-cloud-dalston.html</li>
<li>SpringCloud中国社区 http://springcloud.cn/</li>
<li>SpringCloud中文网 https://www.springcloud.cc/</li>
</ul>
<h1 id="springcloud和springboot关系" tabindex="-1"><a class="header-anchor" href="#springcloud和springboot关系" aria-hidden="true">#</a> SpringCloud和SpringBoot关系</h1>
<ul>
<li>SpringBoot专注于快速方便的开发单个个体微服务</li>
<li>SpringCloud是关注全局的微服务协调整理治理框架，它将SpringBoot开发的一个个单体微服务整合并管理起来，为各个微服务之间提供：配置管理，服务发现，断路器，路由，微代理，事件总线，全局锁，决策竞选，分布式会话等等集成服务。</li>
<li>SpringBoot可以离开SpringCloud独立使用，开发项目，但是SpringCloud离不开SpringBoot，属于依赖关系</li>
<li>SpringBoot专注于快速、方便的开发单个个体微服务，SpringCloud关注全局的服务治理框架</li>
</ul>
<h1 id="导入依赖" tabindex="-1"><a class="header-anchor" href="#导入依赖" aria-hidden="true">#</a> 导入依赖</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token generics"><span class="token punctuation">&lt;</span>dependencyManagement<span class="token punctuation">></span></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>dependencies<span class="token punctuation">></span></span>
        <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span>            springCloud的依赖<span class="token operator">--</span><span class="token operator">></span>
        <span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>cloud<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>cloud<span class="token operator">-</span>dependencies<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
       		<span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token class-name">Greenwich</span><span class="token punctuation">.</span><span class="token constant">SR1</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>type<span class="token punctuation">></span></span>pom<span class="token operator">&lt;</span><span class="token operator">/</span>type<span class="token operator">></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>scope<span class="token punctuation">></span></span><span class="token keyword">import</span><span class="token operator">&lt;</span><span class="token operator">/</span>scope<span class="token operator">></span>
        <span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>

        <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span>            <span class="token class-name">SpringBoot</span><span class="token operator">--</span><span class="token operator">></span>
        <span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>boot<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>boot<span class="token operator">-</span>dependencies<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
        	<span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token number">2.1</span><span class="token number">.4</span><span class="token punctuation">.</span><span class="token constant">RELEASE</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
        <span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>
    <span class="token operator">&lt;</span><span class="token operator">/</span>dependencies<span class="token operator">></span>
<span class="token operator">&lt;</span><span class="token operator">/</span>dependencyManagement<span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="使用" tabindex="-1"><a class="header-anchor" href="#使用" aria-hidden="true">#</a> 使用</h1>
<p>将<code v-pre>RestTemplate</code>注册为Bean</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Configuration</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">RestConfig</span> <span class="token punctuation">{</span>

    <span class="token annotation punctuation">@Bean</span>
    <span class="token keyword">public</span> <span class="token class-name">RestTemplate</span> <span class="token function">getRestTemplate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">RestTemplate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">//提供多种便捷访问远程http服务的方法，简单的Restful服务模板~</span>
<span class="token annotation punctuation">@Autowired</span>
<span class="token keyword">private</span> <span class="token class-name">RestTemplate</span> restTemplate<span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><code v-pre>RestTemplate</code>使用方法非常简单，使用以下方法，参数 (url，[实体:Map],Class&lt;T&gt; responseType)</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200907220352809.png" alt="image-20200907220352809"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200907220408087.png" alt="image-20200907220408087"></p>
</div></template>


