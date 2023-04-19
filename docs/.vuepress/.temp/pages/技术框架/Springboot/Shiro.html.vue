<template><div><h1 id="依赖" tabindex="-1"><a class="header-anchor" href="#依赖" aria-hidden="true">#</a> 依赖</h1>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>&lt;dependency>
&lt;groupId>org.apache.shiro&lt;/groupId>
&lt;artifactId>shiro-spring&lt;/artifactId>
&lt;version>1.6.0&lt;/version>
&lt;/dependency>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="自定义realm" tabindex="-1"><a class="header-anchor" href="#自定义realm" aria-hidden="true">#</a> 自定义realm</h1>
<p>自定义realm一般继承AuthorizingRealm，然后实现getAuthenticationInfo和getAuthorizationInfo方法，来完成登录和权限的验证。</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">MyRealm</span>  <span class="token keyword">extends</span> <span class="token class-name">AuthorizingRealm</span> <span class="token punctuation">{</span>
    <span class="token annotation punctuation">@Override</span>
    <span class="token keyword">protected</span> <span class="token class-name">AuthorizationInfo</span> <span class="token function">doGetAuthorizationInfo</span><span class="token punctuation">(</span><span class="token class-name">PrincipalCollection</span> principalCollection<span class="token punctuation">{</span>
        <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"执行了=>授权doGetAuthorizationInfo方法"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token keyword">null</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token annotation punctuation">@Override</span>
    <span class="token keyword">protected</span> <span class="token class-name">AuthenticationInfo</span> <span class="token function">doGetAuthenticationInfo</span><span class="token punctuation">(</span><span class="token class-name">AuthenticationToken</span> authenticationToken<span class="token punctuation">)</span> <span class="token keyword">throws</span> <span class="token class-name">AuthenticationException</span> <span class="token punctuation">{</span>
        <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"执行了=>认证doGetAuthenticationInfo方法"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token keyword">null</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
    
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="shiro配置类" tabindex="-1"><a class="header-anchor" href="#shiro配置类" aria-hidden="true">#</a> Shiro配置类</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Configuration</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">ShiroConfig</span> <span class="token punctuation">{</span>


    <span class="token annotation punctuation">@Bean</span>
    <span class="token keyword">public</span> <span class="token class-name">ShiroFilterFactoryBean</span> <span class="token function">userShiroFilterFactoryBean</span><span class="token punctuation">(</span><span class="token annotation punctuation">@Qualifier</span><span class="token punctuation">(</span><span class="token string">"userSecurityManager"</span><span class="token punctuation">)</span>
                                                             <span class="token class-name">DefaultWebSecurityManager</span> defaultWebSecurityManager<span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token class-name">ShiroFilterFactoryBean</span> bean <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">ShiroFilterFactoryBean</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">//设置安全管理器</span>
        bean<span class="token punctuation">.</span><span class="token function">setSecurityManager</span><span class="token punctuation">(</span>defaultWebSecurityManager<span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token comment">//添加shiro的内置过滤器</span>
        <span class="token comment">/*
            anon：无需认证就可以访问
            authc：必须认证了才能访问
            user：必须拥有 记住我 功能才能用
            perms: 拥有对某个资源的权限才能访问
            role：拥有某个角色权限才能访问
         */</span>
        <span class="token class-name">Map</span><span class="token generics"><span class="token punctuation">&lt;</span><span class="token class-name">String</span><span class="token punctuation">,</span> <span class="token class-name">String</span><span class="token punctuation">></span></span> filterMap <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">LinkedHashMap</span><span class="token generics"><span class="token punctuation">&lt;</span><span class="token punctuation">></span></span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">//过滤了/add接口和/delete接口</span>
        filterMap<span class="token punctuation">.</span><span class="token function">put</span><span class="token punctuation">(</span><span class="token string">"/add"</span><span class="token punctuation">,</span><span class="token string">"authc"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>   
        filterMap<span class="token punctuation">.</span><span class="token function">put</span><span class="token punctuation">(</span><span class="token string">"/delete"</span><span class="token punctuation">,</span><span class="token string">"authc"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        bean<span class="token punctuation">.</span><span class="token function">setFilterChainDefinitionMap</span><span class="token punctuation">(</span>filterMap<span class="token punctuation">)</span><span class="token punctuation">;</span>
        
        <span class="token comment">//认证失败会转到/toLogin接口</span>
        bean<span class="token punctuation">.</span><span class="token function">setLoginUrl</span><span class="token punctuation">(</span><span class="token string">"/toLogin"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        
        <span class="token keyword">return</span> bean<span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token annotation punctuation">@Bean</span>
    <span class="token keyword">public</span> <span class="token class-name">DefaultWebSecurityManager</span> <span class="token function">userSecurityManager</span><span class="token punctuation">(</span><span class="token annotation punctuation">@Qualifier</span><span class="token punctuation">(</span><span class="token string">"userRealm"</span><span class="token punctuation">)</span> <span class="token class-name">MyRealm</span> myRealm<span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token class-name">DefaultWebSecurityManager</span> bean <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">DefaultWebSecurityManager</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">//关联UserRealm</span>
        bean<span class="token punctuation">.</span><span class="token function">setRealm</span><span class="token punctuation">(</span>myRealm<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> bean<span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token annotation punctuation">@Bean</span>
    <span class="token keyword">public</span> <span class="token class-name">MyRealm</span> <span class="token function">userRealm</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">MyRealm</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="使用" tabindex="-1"><a class="header-anchor" href="#使用" aria-hidden="true">#</a> 使用</h1>
<h2 id="认证" tabindex="-1"><a class="header-anchor" href="#认证" aria-hidden="true">#</a> 认证</h2>
<p>先编写一个login登录接口</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@RequestMapping</span><span class="token punctuation">(</span><span class="token string">"/login"</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token class-name">String</span> <span class="token function">login</span><span class="token punctuation">(</span><span class="token annotation punctuation">@RequestParam</span><span class="token punctuation">(</span><span class="token string">"username"</span><span class="token punctuation">)</span> <span class="token class-name">String</span> username<span class="token punctuation">,</span>
                    <span class="token annotation punctuation">@RequestParam</span><span class="token punctuation">(</span><span class="token string">"password"</span><span class="token punctuation">)</span> <span class="token class-name">String</span> passwrod<span class="token punctuation">,</span>
                    <span class="token class-name">Model</span> model<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">//获取当前用户</span>
    <span class="token class-name">Subject</span> subject <span class="token operator">=</span> <span class="token class-name">SecurityUtils</span><span class="token punctuation">.</span><span class="token function">getSubject</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">//封装用户的登录数据</span>
    <span class="token class-name">UsernamePasswordToken</span> <span class="token class-name">Token</span> <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">UsernamePasswordToken</span><span class="token punctuation">(</span>username<span class="token punctuation">,</span> passwrod<span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token keyword">try</span> <span class="token punctuation">{</span>
        subject<span class="token punctuation">.</span><span class="token function">login</span><span class="token punctuation">(</span><span class="token class-name">Token</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">//登录成功则转到主页，失败则返回到登录界面</span>
        <span class="token keyword">return</span> <span class="token string">"test"</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token keyword">catch</span> <span class="token punctuation">(</span><span class="token class-name">UnknownAccountException</span> e<span class="token punctuation">)</span><span class="token punctuation">{</span>
        model<span class="token punctuation">.</span><span class="token function">addAttribute</span><span class="token punctuation">(</span><span class="token string">"msg"</span><span class="token punctuation">,</span><span class="token string">"用户名错误"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token string">"user/login"</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token keyword">catch</span> <span class="token punctuation">(</span><span class="token class-name">IncorrectCredentialsException</span> e<span class="token punctuation">)</span><span class="token punctuation">{</span>
        model<span class="token punctuation">.</span><span class="token function">addAttribute</span><span class="token punctuation">(</span><span class="token string">"msg"</span><span class="token punctuation">,</span><span class="token string">"密码错误"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token string">"user/login"</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>当执行代码<code v-pre>subject.login(Token);</code>会执行前面自定义realm中<code v-pre>doGetAuthenticationInfo</code>认证方法，我们可以获取传递过来的Token，并与数据库中的用户进行比较，判断是否登录成功：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Override</span>
<span class="token keyword">protected</span> <span class="token class-name">AuthenticationInfo</span> <span class="token function">doGetAuthenticationInfo</span><span class="token punctuation">(</span><span class="token class-name">AuthenticationToken</span> authenticationToken<span class="token punctuation">)</span> <span class="token keyword">throws</span> <span class="token class-name">AuthenticationException</span> <span class="token punctuation">{</span>
    <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"执行了=>认证doGetAuthenticationInfo方法"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">//这里固定了用户名和密码，实际中可以从数据库中获取</span>
    <span class="token class-name">String</span> name <span class="token operator">=</span><span class="token string">"root"</span><span class="token punctuation">;</span>
    <span class="token class-name">String</span> password<span class="token operator">=</span> <span class="token string">"123456"</span><span class="token punctuation">;</span>

    <span class="token class-name">UsernamePasswordToken</span> token <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token class-name">UsernamePasswordToken</span><span class="token punctuation">)</span> authenticationToken<span class="token punctuation">;</span>

    <span class="token keyword">if</span> <span class="token punctuation">(</span><span class="token operator">!</span>token<span class="token punctuation">.</span><span class="token function">getUsername</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">equals</span><span class="token punctuation">(</span>name<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token keyword">return</span> <span class="token keyword">null</span><span class="token punctuation">;</span>   <span class="token comment">//比较用户名，错误则抛出异常UnknownAccountException</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment">//自动将token中的密码与password进行比较，错误则抛出异常IncorrectCredentialsException</span>
    <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">SimpleAuthenticationInfo</span><span class="token punctuation">(</span><span class="token string">""</span><span class="token punctuation">,</span>password<span class="token punctuation">,</span><span class="token string">""</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="授权" tabindex="-1"><a class="header-anchor" href="#授权" aria-hidden="true">#</a> 授权</h2>
<p>在<code v-pre>ShiroConfig</code>Shiro配置类中添加过滤规则：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">// 访问/add接口需要用户拥有user:add权限</span>
filterMap<span class="token punctuation">.</span><span class="token function">put</span><span class="token punctuation">(</span><span class="token string">"/add"</span><span class="token punctuation">,</span><span class="token string">"perms[user:add]"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
bean<span class="token punctuation">.</span><span class="token function">setFilterChainDefinitionMap</span><span class="token punctuation">(</span>filterMap<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//授权失败会转到/noauth接口</span>
bean<span class="token punctuation">.</span><span class="token function">setUnauthorizedUrl</span><span class="token punctuation">(</span><span class="token string">"/noauth"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">return</span> bean<span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在实际情况中，<strong>认证</strong>时我们会对表单中传来的数据与数据库中的User进行比较，我们需要先根据token中的username去数据库中拿到user，再在<code v-pre>SimpleAuthenticationInfo</code>类中传入这个user</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">SimpleAuthenticationInfo</span><span class="token punctuation">(</span>user<span class="token punctuation">,</span>password<span class="token punctuation">,</span><span class="token string">""</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>这样我们就可以在授权时通过</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">//拿到当前登录的这个对象</span>
<span class="token class-name">Subject</span> subject <span class="token operator">=</span> <span class="token class-name">SecurityUtils</span><span class="token punctuation">.</span><span class="token function">getSubject</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token class-name">User</span> currentUser <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token class-name">User</span><span class="token punctuation">)</span> subject<span class="token punctuation">.</span><span class="token function">getPrincipal</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//拿到User对象</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>拿到当前的用户，再根据用户在数据库中的权限来判断是否能访问该页面，授权完整代码如下</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Override</span>
<span class="token keyword">protected</span> <span class="token class-name">AuthorizationInfo</span> <span class="token function">doGetAuthorizationInfo</span><span class="token punctuation">(</span><span class="token class-name">PrincipalCollection</span> principalCollection<span class="token punctuation">)</span> 	<span class="token punctuation">{</span>
    <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"执行了=>授权doGetAuthorizationInfo方法"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token class-name">SimpleAuthorizationInfo</span> info <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">SimpleAuthorizationInfo</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">//拿到当前登录的这个对象</span>
    <span class="token class-name">Subject</span> subject <span class="token operator">=</span> <span class="token class-name">SecurityUtils</span><span class="token punctuation">.</span><span class="token function">getSubject</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token class-name">User</span> currentUser <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token class-name">User</span><span class="token punctuation">)</span> subject<span class="token punctuation">.</span><span class="token function">getPrincipal</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//拿到User对象</span>

    <span class="token comment">//设置当前用户的权限，currentUser.getPerms()对应User类中的get方法，返回用户的权限</span>
    info<span class="token punctuation">.</span><span class="token function">addStringPermission</span><span class="token punctuation">(</span>currentUser<span class="token punctuation">.</span><span class="token function">getPerms</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> info<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="注意" tabindex="-1"><a class="header-anchor" href="#注意" aria-hidden="true">#</a> 注意</h1>
<p>Shiro在进行第一次重定向时会在url后携带jsessionid，导致访问400。实力有限，就不分析源码了，需要了解原因的可以查看<code v-pre>ShiroHttpServletResponse</code>类中<code v-pre>encodeRedirectURL</code>、<code v-pre>encodeRedirectUrl</code>、<code v-pre>toEncoded</code>等方法，直接说下解决办法</p>
<p>解决办法：</p>
<ol>
<li>创建一个<code v-pre>DefaultWebSessionManager</code>类实例，并将它的<code v-pre>sessionIdUrlRewritingEnabled</code>属性设置成false</li>
<li>再在<code v-pre>DefaultWebSecurityManager</code>类中将上面的实例设置为它的<code v-pre>SessionManager</code></li>
</ol>
<p>具体代码如下：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Autowired</span>
<span class="token class-name">DefaultWebSessionManager</span> defaultSessionManager<span class="token punctuation">;</span>

<span class="token annotation punctuation">@Autowired</span>
<span class="token class-name">MyRealm</span> myRealm<span class="token punctuation">;</span>

<span class="token annotation punctuation">@Bean</span>
<span class="token keyword">public</span> <span class="token class-name">DefaultWebSecurityManager</span> <span class="token function">userSecurityManager</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token class-name">DefaultWebSecurityManager</span> bean <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">DefaultWebSecurityManager</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">//将下面的bean设置为DefaultWebSecurityManager的SessionManager</span>
    bean<span class="token punctuation">.</span><span class="token function">setSessionManager</span><span class="token punctuation">(</span>defaultSessionManager<span class="token punctuation">)</span><span class="token punctuation">;</span>
    bean<span class="token punctuation">.</span><span class="token function">setRealm</span><span class="token punctuation">(</span>myRealm<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> bean<span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">//创建DefaultWebSessionManager类，并DI注入到IOC容器中</span>
<span class="token annotation punctuation">@Bean</span>
<span class="token keyword">public</span> <span class="token class-name">DefaultWebSessionManager</span> <span class="token function">mySessionManager</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token class-name">DefaultWebSessionManager</span> defaultSessionManager <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">DefaultWebSessionManager</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">//将sessionIdUrlRewritingEnabled属性设置成false</span>
    defaultSessionManager<span class="token punctuation">.</span><span class="token function">setSessionIdUrlRewritingEnabled</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> defaultSessionManager<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span class="token annotation punctuation">@Bean</span>
<span class="token keyword">public</span> <span class="token class-name">MyRealm</span> <span class="token function">userRealm</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">MyRealm</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


