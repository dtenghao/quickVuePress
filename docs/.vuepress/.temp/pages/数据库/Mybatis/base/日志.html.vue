<template><div><h1 id="日志工厂" tabindex="-1"><a class="header-anchor" href="#日志工厂" aria-hidden="true">#</a> 日志工厂</h1>
<p>如果一个数据库操作，出现了异常，我们需要排错。日志就是最好的助手！</p>
<p>曾经：sout、debug</p>
<p>现在日志工厂！</p>
<ul>
<li>SLF4J</li>
<li>LOG4J【掌握】</li>
<li>LOG4J2</li>
<li>JDK_LOGGING</li>
<li>COMMONS_LOGGING</li>
<li>STDOUT_LOGGING 【掌握】</li>
<li>NO_LOGGING</li>
</ul>
<p>在Mybatis中具体使用哪个日志实现，在设置中设定！</p>
<h1 id="stdout-logging" tabindex="-1"><a class="header-anchor" href="#stdout-logging" aria-hidden="true">#</a> STDOUT_LOGGING</h1>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>&lt;settings>
	&lt;!--标准日志工厂实现-->
	&lt;setting name="logImpl" value="STDOUT_LOGGING"/>
&lt;/settings>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="log4j" tabindex="-1"><a class="header-anchor" href="#log4j" aria-hidden="true">#</a> LOG4J</h1>
<ul>
<li>Log4j是<a href="https://baike.baidu.com/item/Apache/8512995" target="_blank" rel="noopener noreferrer">Apache<ExternalLinkIcon/></a>的一个开源项目，通过使用Log4j，我们可以控制日志信息输送的目的地是<a href="https://baike.baidu.com/item/%E6%8E%A7%E5%88%B6%E5%8F%B0/2438626" target="_blank" rel="noopener noreferrer">控制台<ExternalLinkIcon/></a>、文件、<a href="https://baike.baidu.com/item/GUI" target="_blank" rel="noopener noreferrer">GUI<ExternalLinkIcon/></a>组件</li>
<li>我们可以控制每一条日志的输出格式</li>
<li>通过定义每一条日志信息的级别，我们能够更加细致地控制日志的生成过程</li>
<li>通过一个<a href="https://baike.baidu.com/item/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6/286550" target="_blank" rel="noopener noreferrer">配置文件<ExternalLinkIcon/></a>来灵活地进行配置，而不需要修改应用的代码。</li>
</ul>
<ol>
<li>导入LOG4J</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>log4j<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>log4j<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>1.2.17<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="2">
<li>log4j.properties</li>
</ol>
<div class="language-properties line-numbers-mode" data-ext="properties"><pre v-pre class="language-properties"><code><span class="token comment">#将等级为DEBUG的日志信息输出到console和file这两个目的地，console和file的定义在下面的代码</span>
<span class="token key attr-name">log4j.rootLogger</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG,console,file</span>

<span class="token comment">#控制台输出的相关设置</span>
<span class="token key attr-name">log4j.appender.console</span> <span class="token punctuation">=</span> <span class="token value attr-value">org.apache.log4j.ConsoleAppender</span>
<span class="token key attr-name">log4j.appender.console.Target</span> <span class="token punctuation">=</span> <span class="token value attr-value">System.out</span>
<span class="token key attr-name">log4j.appender.console.Threshold</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.appender.console.layout</span> <span class="token punctuation">=</span> <span class="token value attr-value">org.apache.log4j.PatternLayout</span>
<span class="token key attr-name">log4j.appender.console.layout.ConversionPattern</span><span class="token punctuation">=</span><span class="token value attr-value">[%c]-%m%n</span>

<span class="token comment">#文件输出的相关设置</span>
<span class="token key attr-name">log4j.appender.file</span> <span class="token punctuation">=</span> <span class="token value attr-value">org.apache.log4j.RollingFileAppender</span>
<span class="token key attr-name">log4j.appender.file.File</span><span class="token punctuation">=</span><span class="token value attr-value">./log/dth.log</span>
<span class="token key attr-name">log4j.appender.file.MaxFileSize</span><span class="token punctuation">=</span><span class="token value attr-value">10mb</span>
<span class="token key attr-name">log4j.appender.file.Threshold</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.appender.file.layout</span><span class="token punctuation">=</span><span class="token value attr-value">org.apache.log4j.PatternLayout</span>
<span class="token key attr-name">log4j.appender.file.layout.ConversionPattern</span><span class="token punctuation">=</span><span class="token value attr-value">[%p][%d{yy-MM-dd}][%c]%m%n</span>

<span class="token comment">#日志输出级别</span>
<span class="token key attr-name">log4j.logger.org.mybatis</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.logger.java.sql</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.logger.java.sql.Statement</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.logger.java.sql.ResultSet</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
<span class="token key attr-name">log4j.logger.java.sql.PreparedStatement</span><span class="token punctuation">=</span><span class="token value attr-value">DEBUG</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="3">
<li>配置log4j为日志实现</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>settings</span><span class="token punctuation">></span></span>
	<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>setting</span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>logImpl<span class="token punctuation">"</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>LOG4J<span class="token punctuation">"</span></span><span class="token punctuation">/></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>settings</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="4">
<li>Log4j的使用：直接运行代码就行，控制台打印信息会多出许多日志</li>
</ol>
<p><strong>简单使用</strong></p>
<ol>
<li>在要使用Log4j的类中，导入包import org.apache.log4j.Logger;</li>
<li>日志对象，参数为当前类的class</li>
</ol>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token class-name">Logger</span> logger <span class="token operator">=</span> <span class="token class-name">Logger</span><span class="token punctuation">.</span><span class="token function">getLogger</span><span class="token punctuation">(</span><span class="token class-name">UserDaoTest</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><ol start="3">
<li>日志级别</li>
</ol>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code>logger<span class="token punctuation">.</span><span class="token function">info</span><span class="token punctuation">(</span><span class="token string">"info:进入了testLog4j"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
logger<span class="token punctuation">.</span><span class="token function">debug</span><span class="token punctuation">(</span><span class="token string">"debug:进入了testLog4j"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
logger<span class="token punctuation">.</span><span class="token function">error</span><span class="token punctuation">(</span><span class="token string">"error:进入了testLog4j"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


