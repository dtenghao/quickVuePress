<template><div><h1 id="概念" tabindex="-1"><a class="header-anchor" href="#概念" aria-hidden="true">#</a> 概念</h1>
<p>https://github.com/Netflix/Hystrix/wiki</p>
<h1 id="依赖" tabindex="-1"><a class="header-anchor" href="#依赖" aria-hidden="true">#</a> 依赖</h1>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.springframework.cloud<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>spring-cloud-starter-netflix-hystrix<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>2.2.5.RELEASE<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="服务熔断" tabindex="-1"><a class="header-anchor" href="#服务熔断" aria-hidden="true">#</a> 服务熔断</h1>
<p>服务熔断的作用类似于我们家用的保险丝，当某服务出现不可用或响应超时的情况时，为了防止整个系统出现雪崩，暂时停止对该服务的调用，使用备选方案。</p>
<p>在服务端需要熔断的方法上加注解：<code v-pre>@HystrixCommand()</code></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@RequestMapping</span><span class="token punctuation">(</span><span class="token string">"/feign"</span><span class="token punctuation">)</span>
<span class="token comment">// fallbackMethod指明备案方法</span>
<span class="token annotation punctuation">@HystrixCommand</span><span class="token punctuation">(</span>fallbackMethod <span class="token operator">=</span> <span class="token string">"errorFall"</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">feign</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token keyword">int</span> num<span class="token operator">=</span><span class="token number">1</span><span class="token operator">/</span><span class="token number">0</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token string">"feign"</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">errorFall</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token string">"error"</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>进而在启动类上加上注解<code v-pre>@EnableCircuitBreaker</code></p>
<p>访问<code v-pre>http://localhost:8001/feign</code>会因为<code v-pre>1/0</code>出错而抛出异常，转而执行<code v-pre>errorFall</code></p>
<h1 id="服务降级" tabindex="-1"><a class="header-anchor" href="#服务降级" aria-hidden="true">#</a> 服务降级</h1>
<p>服务降级是从整个系统的负荷情况出发和考虑的，对某些负荷会比较高的情况，为了预防某些功能（业务场景）出现负荷过载或者响应慢的情况，在其内部暂时舍弃对一些非核心的接口和数据的请求，而直接返回一个提前准备好的fallback（退路）错误处理信息。这样，虽然提供的是一个有损的服务，但却保证了整个系统的稳定性和可用性。</p>
<p>服务熔断是作用在生产者上的，服务降级是作用在消费者上的。</p>
<p>先创建一个<code v-pre>DeptClientServiceFallbackFactory</code>类</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">// 注册到IOC容器中</span>
<span class="token annotation punctuation">@Component</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">DeptClientServiceFallbackFactory</span>  <span class="token keyword">implements</span> <span class="token class-name">FallbackFactory</span> <span class="token punctuation">{</span>
    <span class="token annotation punctuation">@Override</span>
    <span class="token keyword">public</span> <span class="token class-name">Object</span> <span class="token function">create</span><span class="token punctuation">(</span><span class="token class-name">Throwable</span> throwable<span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">//	FeignService是我们之前创建的feign服务</span>
        <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">FeignService</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token annotation punctuation">@Override</span>
            <span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">getfeign1</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token keyword">return</span> <span class="token string">"hello1"</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>

            <span class="token annotation punctuation">@Override</span>
            <span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">getfeign2</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token keyword">return</span> <span class="token string">"hello2"</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>再在<code v-pre>feign</code>服务类上引入上文创建的<code v-pre>DeptClientServiceFallbackFactory</code></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@FeignClient</span><span class="token punctuation">(</span>name<span class="token operator">=</span><span class="token string">"SPRINGCLOUD-PROVIDER-DEPT8001"</span><span class="token punctuation">,</span>fallbackFactory <span class="token operator">=</span> <span class="token class-name">DeptClientServiceFallbackFactory</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token keyword">interface</span> <span class="token class-name">FeignService</span> <span class="token punctuation">{</span>
    <span class="token annotation punctuation">@RequestMapping</span><span class="token punctuation">(</span><span class="token string">"/test1"</span><span class="token punctuation">)</span>
    <span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">getfeign1</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token annotation punctuation">@RequestMapping</span><span class="token punctuation">(</span><span class="token string">"/test2"</span><span class="token punctuation">)</span>
    <span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">getfeign2</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>如果<code v-pre>SPRINGCLOUD-PROVIDER-DEPT8001</code>服务被异常关闭了，那么消费者使用方法<code v-pre>getfeign1</code>、<code v-pre>getfeign2</code>就会访问失败，转而去访问<code v-pre>DeptClientServiceFallbackFactory</code>中的替代方法</p>
<h1 id="熔断vs降级" tabindex="-1"><a class="header-anchor" href="#熔断vs降级" aria-hidden="true">#</a> 熔断VS降级</h1>
<p>==相同点：==</p>
<p>目标一致 都是从可用性和可靠性出发，为了防止系统崩溃；</p>
<p>用户体验类似 最终都让用户体验到的是某些功能暂时不可用；</p>
<p>==不同点：==</p>
<p>触发原因不同 服务熔断一般是某个服务（下游服务）故障引起，而服务降级一般是从整体负荷考虑；</p>
<h1 id="dashboard流监控" tabindex="-1"><a class="header-anchor" href="#dashboard流监控" aria-hidden="true">#</a> Dashboard流监控</h1>
<h2 id="创建监控平台" tabindex="-1"><a class="header-anchor" href="#创建监控平台" aria-hidden="true">#</a> 创建监控平台</h2>
<p>创建一个新的springboot项目</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>cloud<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>cloud<span class="token operator">-</span>starter<span class="token operator">-</span>netflix<span class="token operator">-</span>hystrix<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token number">2.2</span><span class="token number">.5</span><span class="token punctuation">.</span><span class="token constant">RELEASE</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
<span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>

<span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>cloud<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>cloud<span class="token operator">-</span>starter<span class="token operator">-</span>netflix<span class="token operator">-</span>hystrix<span class="token operator">-</span>dashboard<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token number">2.2</span><span class="token number">.5</span><span class="token punctuation">.</span><span class="token constant">RELEASE</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
<span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>再在启动类上开启<code v-pre>dashboard</code></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@EnableHystrixDashboard</span> <span class="token comment">//开启</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>在<code v-pre>application.yml</code>中配置</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code>hystrix<span class="token operator">:</span>
  dashboard<span class="token operator">:</span>
	<span class="token comment">//被监控服务的ip地址</span>
    proxy<span class="token operator">-</span>stream<span class="token operator">-</span>allow<span class="token operator">-</span>list<span class="token operator">:</span> <span class="token string">"localhost"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>访问http://localhost:9001/hystrix即可看到监控平台</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200910015037798.png" alt="image-20200910015037798"></p>
<h2 id="创建被监控的服务" tabindex="-1"><a class="header-anchor" href="#创建被监控的服务" aria-hidden="true">#</a> 创建被监控的服务</h2>
<p>引入依赖</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token generics"><span class="token punctuation">&lt;</span>dependency<span class="token punctuation">></span></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>groupId<span class="token punctuation">></span></span>org<span class="token punctuation">.</span>springframework<span class="token punctuation">.</span>boot<span class="token operator">&lt;</span><span class="token operator">/</span>groupId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>artifactId<span class="token punctuation">></span></span>spring<span class="token operator">-</span>boot<span class="token operator">-</span>starter<span class="token operator">-</span>actuator<span class="token operator">&lt;</span><span class="token operator">/</span>artifactId<span class="token operator">></span>
    <span class="token generics"><span class="token punctuation">&lt;</span>version<span class="token punctuation">></span></span><span class="token number">2.3</span><span class="token number">.3</span><span class="token punctuation">.</span><span class="token constant">RELEASE</span><span class="token operator">&lt;</span><span class="token operator">/</span>version<span class="token operator">></span>
<span class="token operator">&lt;</span><span class="token operator">/</span>dependency<span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在启动类中注册servlet服务bean</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Bean</span>
<span class="token keyword">public</span> <span class="token class-name">ServletRegistrationBean</span> <span class="token function">hystrixMetricsStreamServlet</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token class-name">ServletRegistrationBean</span> registration <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">ServletRegistrationBean</span><span class="token punctuation">(</span><span class="token keyword">new</span> <span class="token class-name">HystrixMetricsStreamServlet</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    registration<span class="token punctuation">.</span><span class="token function">addUrlMappings</span><span class="token punctuation">(</span><span class="token string">"/actuator/hystrix.stream"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> registration<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>这样我们就可以对服务进行监控了！</p>
<p>访问 http://localhost:8001/actuator/hystrix.stream</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200910015003806.png" alt="image-20200910015003806"></p>
<p>可以看到当前服务的状态，当然这里是以json对象的格式显示，我们可以通过上文创建的监控平台，图形化的查看服务状态</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200910015224501.png" alt="image-20200910015224501"></p>
<p>点击<code v-pre>Monitor Stream</code>进入平台</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200910015358292.png" alt="image-20200910015358292"></p>
<p>==注意==，dashboard只能监控带有<code v-pre>@HystrixCommand</code>注解的方法，也就是配有服务熔断的方法。</p>
</div></template>


