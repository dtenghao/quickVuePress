<template><div><p>JDBC：Java database controller</p>
<p>依赖：</p>
<ul>
<li>java.sql</li>
<li>javax.sql</li>
<li>mysql-conneter-java...  连接驱动（必须）</li>
</ul>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token comment">//配置信息</span>
<span class="token comment">//useUnicode=true&amp;characterEncoding=utf-8解决中文乱码</span>
<span class="token class-name">String</span> url <span class="token operator">=</span> <span class="token string">"jdbc:mysql://localhost:3308/light?useUnicode=true&amp;characterEncoding=utf-8&amp;serverTimezone=UTC"</span><span class="token punctuation">;</span>
<span class="token class-name">String</span> username <span class="token operator">=</span> <span class="token string">"root"</span><span class="token punctuation">;</span>
<span class="token class-name">String</span> password <span class="token operator">=</span> <span class="token string">"admin888"</span><span class="token punctuation">;</span>

<span class="token comment">//1.加载驱动</span>
<span class="token class-name">Class</span><span class="token punctuation">.</span><span class="token function">forName</span><span class="token punctuation">(</span><span class="token string">"com.mysql.cj.jdbc.Driver"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">//2.连接数据库，代表数据库</span>
<span class="token class-name">Connection</span> connection <span class="token operator">=</span> <span class="token class-name">DriverManager</span><span class="token punctuation">.</span><span class="token function">getConnection</span><span class="token punctuation">(</span>url<span class="token punctuation">,</span> username<span class="token punctuation">,</span> password<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">//3.向数据库发送SQL的对象Statement，PreparedStatement：CRUD</span>
<span class="token class-name">Statement</span> statement <span class="token operator">=</span> connection<span class="token punctuation">.</span><span class="token function">createStatement</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">//4.编写SQL</span>
<span class="token class-name">String</span> sql <span class="token operator">=</span> <span class="token string">"select * from test"</span><span class="token punctuation">;</span>

<span class="token comment">//5.执行SQL，返回一个ResultSet：结果集</span>
<span class="token class-name">ResultSet</span> rs <span class="token operator">=</span> statement<span class="token punctuation">.</span><span class="token function">executeQuery</span><span class="token punctuation">(</span>sql<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">while</span> <span class="token punctuation">(</span>rs<span class="token punctuation">.</span><span class="token function">next</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"id="</span><span class="token operator">+</span>rs<span class="token punctuation">.</span><span class="token function">getObject</span><span class="token punctuation">(</span><span class="token string">"id"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span><span class="token string">"name="</span><span class="token operator">+</span>rs<span class="token punctuation">.</span><span class="token function">getObject</span><span class="token punctuation">(</span><span class="token string">"name"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">//6.关闭连接，释放资源（一定要做） 先开后关</span>
rs<span class="token punctuation">.</span><span class="token function">close</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
statement<span class="token punctuation">.</span><span class="token function">close</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
connection<span class="token punctuation">.</span><span class="token function">close</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>==注意:==</p>
<p>增删改不使用<code v-pre>executeQuery</code>都是使用<code v-pre>executeUpdate</code></p>
<p>==通知数据库开启事务==</p>
<p>默认是未开启事务的，如果我们需要使用到事务，则需要在代码中添加一行代码：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code>connection<span class="token punctuation">.</span><span class="token function">setAutoCommit</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></div></template>


