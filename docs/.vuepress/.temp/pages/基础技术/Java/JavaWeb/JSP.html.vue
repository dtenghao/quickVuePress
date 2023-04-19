<template><div><h1 id="导入依赖" tabindex="-1"><a class="header-anchor" href="#导入依赖" aria-hidden="true">#</a> 导入依赖</h1>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>javax.servlet<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>javax.servlet-api<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>4.0.1<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>

<span class="token comment">&lt;!--    JSP依赖--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>javax.servlet.jsp<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>javax.servlet.jsp-api<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>2.3.3<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
<span class="token comment">&lt;!--    JSTL表达式的依赖--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>Javax.servlet.jsp.jstl<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>jstl-api<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>1.2<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
<span class="token comment">&lt;!--    standard标签库--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>taglibs<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>standard<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>1.1.2<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="jsp表达式" tabindex="-1"><a class="header-anchor" href="#jsp表达式" aria-hidden="true">#</a> jsp表达式</h1>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;%--JSP表达式
    作用：用来将程序输出，输出到客户端
    &lt;%= 变量或者表达式%&gt;
--%&gt;
&lt;%= new java.util.Date()%&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<p>但是实际中一般还是使用EL表达式</p>
<div class="language-html line-numbers-mode" data-ext="html"><pre v-pre class="language-html"><code>${new java.util.Date()}
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><h1 id="jsp脚本片段" tabindex="-1"><a class="header-anchor" href="#jsp脚本片段" aria-hidden="true">#</a> jsp脚本片段</h1>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;%--jsp脚本片段--%&gt;
&lt;%
    int sum=0;
    for(int i=1;i&lt;=100;i++){
        sum+=i;
    }
    out.println(&quot;&lt;h1&gt;Sum=&quot;+sum+&quot;&lt;/h1&gt;&quot;);
%&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>脚本片段的再实现：</strong></p>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;%--在代码嵌入HTML元素--%&gt;
&lt;%
    for (int i = 0; i &lt; 5; i++) {
%&gt;
&lt;h1&gt;Hello,World &lt;%=i%&gt;
&lt;/h1&gt;
&lt;%
    }
%&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="jsp声明" tabindex="-1"><a class="header-anchor" href="#jsp声明" aria-hidden="true">#</a> jsp声明</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token operator">&lt;</span><span class="token operator">%</span><span class="token operator">!</span>
    <span class="token keyword">static</span> <span class="token punctuation">{</span>
        <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"Loading Servlet!"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    <span class="token keyword">private</span> <span class="token keyword">int</span> globalVar <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">;</span>
    
    <span class="token keyword">public</span> <span class="token keyword">void</span> <span class="token function">func</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"func!"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
<span class="token operator">%</span><span class="token operator">></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>JSP声明：会被编译到JSP生成Java的类中！其他的，会被生成到_jspService方法中！</p>
<h1 id="_9大内置对象" tabindex="-1"><a class="header-anchor" href="#_9大内置对象" aria-hidden="true">#</a> 9大内置对象</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">final</span> <span class="token class-name"><span class="token namespace">javax<span class="token punctuation">.</span>servlet<span class="token punctuation">.</span>jsp<span class="token punctuation">.</span></span>PageContext</span> pageContext<span class="token punctuation">;</span> <span class="token comment">//页面上下文</span>
<span class="token class-name"><span class="token namespace">javax<span class="token punctuation">.</span>servlet<span class="token punctuation">.</span>http<span class="token punctuation">.</span></span>HttpSession</span> session <span class="token operator">=</span> <span class="token keyword">null</span><span class="token punctuation">;</span> <span class="token comment">//session</span>
<span class="token keyword">final</span> <span class="token class-name"><span class="token namespace">javax<span class="token punctuation">.</span>servlet<span class="token punctuation">.</span></span>ServletContext</span> application<span class="token punctuation">;</span> <span class="token comment">//applicationContext</span>
<span class="token keyword">final</span> <span class="token class-name"><span class="token namespace">javax<span class="token punctuation">.</span>servlet<span class="token punctuation">.</span></span>ServletConfig</span> config<span class="token punctuation">;</span>       <span class="token comment">//config</span>
<span class="token class-name"><span class="token namespace">javax<span class="token punctuation">.</span>servlet<span class="token punctuation">.</span>jsp<span class="token punctuation">.</span></span>JspWriter</span> out <span class="token operator">=</span> <span class="token keyword">null</span><span class="token punctuation">;</span>         <span class="token comment">//out</span>
<span class="token keyword">final</span> <span class="token class-name"><span class="token namespace">java<span class="token punctuation">.</span>lang<span class="token punctuation">.</span></span>Object</span> page <span class="token operator">=</span> <span class="token keyword">this</span><span class="token punctuation">;</span>             <span class="token comment">//page:几乎不用</span>
<span class="token class-name">HttpServletRequest</span> request<span class="token punctuation">;</span>                     <span class="token comment">//请求</span>
<span class="token class-name">HttpServletResponse</span> response<span class="token punctuation">;</span>                   <span class="token comment">//响应</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="jsp标签、jstl标签、el表达式" tabindex="-1"><a class="header-anchor" href="#jsp标签、jstl标签、el表达式" aria-hidden="true">#</a> JSP标签、JSTL标签、EL表达式</h1>
<h2 id="el表达式" tabindex="-1"><a class="header-anchor" href="#el表达式" aria-hidden="true">#</a> EL表达式：	${}</h2>
<ul>
<li>获取数据</li>
<li>执行运算</li>
<li>获取web开发的常用对象</li>
</ul>
<h2 id="jsp标签" tabindex="-1"><a class="header-anchor" href="#jsp标签" aria-hidden="true">#</a> JSP标签</h2>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;jsp:forward page=&quot;Success.jsp&quot;&gt;
    &lt;jsp:param name=&quot;name&quot; value=&quot;邓腾浩&quot;/&gt;
&lt;/jsp:forward&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="jstl标签" tabindex="-1"><a class="header-anchor" href="#jstl标签" aria-hidden="true">#</a> JSTL标签</h2>
<p>JSTL标签库的使用就是为了弥补HTML标签的不足；它自定义许多标签，可以供我们使用，标签的功能和Java代码一样！</p>
<p><strong>核心标签</strong>（掌握部分）</p>
<ol>
<li>
<p>引入标签库</p>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;%@ taglib prefix=&quot;c&quot; uri=&quot;http://java.sun.com/jsp/jstl/core&quot; %&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>使用其中的方法</p>
<div class="language-jsp line-numbers-mode" data-ext="jsp"><pre v-pre class="language-jsp"><code>&lt;form action=&quot;index.jsp&quot;&gt;
&lt;%--
    EL表达式获取表单中的数据
    ${param.参数名}}
--%&gt;
    &lt;input type=&quot;text&quot; name=&quot;username&quot; value=&quot;${param.username}&quot;&gt;
    &lt;input type=&quot;submit&quot; value=&quot;登录&quot;&gt;
&lt;/form&gt;
&lt;%--判断如果提交的用户名是管理员,成功--%&gt;
&lt;c:if test=&quot;${param.username=='admin'}&quot; var=&quot;isAdmin&quot;&gt;
    &lt;c:out value=&quot;管理员欢迎您&quot;/&gt;
&lt;/c:if&gt;
&lt;c:out value=&quot;${isAdmin}&quot;/&gt;
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></li>
</ol>
<p><strong>格式化标签</strong></p>
<p><strong>SQL标签</strong></p>
<p><strong>XML标签</strong></p>
<hr>
<h1 id="mvc三层架构" tabindex="-1"><a class="header-anchor" href="#mvc三层架构" aria-hidden="true">#</a> MVC三层架构</h1>
<p>虽然Servlet和Jsp 都可以写Java代码，为了易于维护和使用</p>
<p>Servlet专注于处理请求，以及控制视图跳转</p>
<p>JSP专注于显示数据</p>
<p>==Model==</p>
<ul>
<li>业务处理：业务逻辑（Service）</li>
<li>数据持久层：CRUD（Dao）</li>
</ul>
<p>==View==</p>
<ul>
<li>展示数据</li>
<li>提供链接发起Servlet请求（a，form，img...）</li>
</ul>
<p>==Controller==（Servelet）</p>
<ul>
<li>接收用户的请求：（req：请求参数、Session信息）</li>
<li>交给业务层处理对应的代码</li>
<li>控制视图跳转</li>
</ul>
<h1 id="设置首页" tabindex="-1"><a class="header-anchor" href="#设置首页" aria-hidden="true">#</a> 设置首页</h1>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token comment">&lt;!--    设置欢迎界面--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>welcome-file-list</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>welcome-file</span><span class="token punctuation">></span></span>login.jsp<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>welcome-file</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>welcome-file-list</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


