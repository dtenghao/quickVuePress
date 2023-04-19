<template><div><h1 id="依赖" tabindex="-1"><a class="header-anchor" href="#依赖" aria-hidden="true">#</a> 依赖</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>cloud<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>cloud<span class="token operator">-</span>starter<span class="token operator">-</span>netflix<span class="token operator">-</span>ribbon<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token number">2.2</span><span class="token number">.5</span><span class="token punctuation">.</span><span class="token constant">RELEASE</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
<span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="添加注解" tabindex="-1"><a class="header-anchor" href="#添加注解" aria-hidden="true">#</a> 添加注解</h1>
<p>在<code v-pre>RestTemplate</code>上添加注解<code v-pre>@LoadBalanced</code></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">//配置负载均衡实现RestTemplate</span>
<span class="token comment">// IRule</span>
<span class="token comment">//  RoundRobinRule 轮询</span>
<span class="token comment">//  RandomRule 随机</span>
<span class="token comment">// AvailabilityFilteringRule: 会先过滤掉，跳闸，访问故障的服务~，对剩下的进行轮询</span>
<span class="token comment">// RetryRule： 会先按照轮询获取服务~，如果服务获取失败，则会在指定的时间内进行，重试</span>
<span class="token annotation punctuation">@Bean</span>
<span class="token annotation punctuation">@LoadBalanced</span>
<span class="token keyword">public</span> <span class="token class-name">RestTemplate</span> <span class="token function">getRestTemplate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">RestTemplate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>以后的访问就是添加了负载均衡机制了</p>
<h1 id="自定义负载均衡算法" tabindex="-1"><a class="header-anchor" href="#自定义负载均衡算法" aria-hidden="true">#</a> 自定义负载均衡算法</h1>
<p>在<code v-pre>com</code>文件夹下创建文件<code v-pre>MyRule.FooConfiguration</code>，写入：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Configuration</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">FooConfiguration</span> <span class="token punctuation">{</span>
    <span class="token comment">//具体使用哪种算法可以自定义，这里用的轮询</span>
    <span class="token annotation punctuation">@Bean</span>
    <span class="token keyword">public</span> <span class="token class-name">RoundRobinRule</span> <span class="token class-name">MyRule</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">RoundRobinRule</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>再在<code v-pre>SpringBootApplication</code>启动类上添加注解</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@RibbonClient</span><span class="token punctuation">(</span>name <span class="token operator">=</span> <span class="token string">"SPRINGCLOUD-PROVIDER-DEPT8001"</span><span class="token punctuation">,</span>configuration <span class="token operator">=</span> <span class="token class-name">FooConfiguration</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><code v-pre>SPRINGCLOUD-PROVIDER-DEPT8001</code>是服务名</p>
<p><strong>注意</strong>FooConfiguration必须是<code v-pre>@Configuration</code>，但请注意，它不在主应用程序上下文的<code v-pre>@ComponentScan</code>中，否则将由所有<code v-pre>@RibbonClients</code>共享，因此需要将其放在一个单独的，不重叠的包</p>
</div></template>


