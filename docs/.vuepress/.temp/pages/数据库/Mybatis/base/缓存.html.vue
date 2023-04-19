<template><div><ol>
<li>什么是缓存【Cache】？
<ul>
<li>存在内存中的临时数据</li>
<li>将用户经常查询的数据放在缓存（内存）中，用户去查询数据就不用从磁盘上（关系型数据库文件）查询，从而提高查询效率，解决了高并发系统的性能问题</li>
</ul>
</li>
<li>为什么使用缓存？
<ul>
<li>减少和数据库的交互次数，减少系统开销，提高系统效率</li>
</ul>
</li>
<li>什么样的数据能使用缓存？
<ul>
<li>经常查询并且不经常改变的数据。【可以使用缓存】</li>
</ul>
</li>
</ol>
<h1 id="mybatis缓存" tabindex="-1"><a class="header-anchor" href="#mybatis缓存" aria-hidden="true">#</a> Mybatis缓存</h1>
<ul>
<li>MyBatis包含一个非常强大的查询缓存特性，它可以非常方便地定制和配置缓存。缓存可以极大的提升查询效率。</li>
<li>MyBatis系统中默认定义了两级缓存：一级缓存和二级缓存
<ul>
<li>默认情况下，只有一级缓存开启。（SqlSession级别的缓存，也成为本地缓存）</li>
<li>二级缓存需要手动开启和配置，他是基于namespace级别的缓存</li>
<li>为了提高扩展线，MyBatis定义了缓存接口Cache。我们可以通过实现Cache接口来自定义二级缓存</li>
</ul>
</li>
</ul>
<h1 id="一级缓存" tabindex="-1"><a class="header-anchor" href="#一级缓存" aria-hidden="true">#</a> 一级缓存</h1>
<ul>
<li>映射语句文件中的所有 select 语句的结果将会被缓存。</li>
<li>映射语句文件中的所有 insert、update 和 delete 语句会刷新缓存。</li>
<li>缓存会使用最近最少使用算法（LRU, Least Recently Used）算法来清除不需要的缓存。</li>
<li>缓存不会定时进行刷新（也就是说，没有刷新间隔）。</li>
<li>缓存会保存列表或对象（无论查询方法返回哪种）的 1024 个引用。</li>
<li>缓存会被视为读/写缓存，这意味着获取到的对象并不是共享的，可以安全地被调用者修改，而不干扰其他调用者或线程所做的潜在修改。</li>
</ul>
<p>缓存失效的情况：</p>
<ol>
<li>
<p>查询不同的东西</p>
</li>
<li>
<p>增删改操作，可能会改变原来的数据，所以必定会刷新缓存！</p>
</li>
<li>
<p>查询不同的Mapper.xml</p>
</li>
<li>
<p>手动清理缓存</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code>sqlSession<span class="token punctuation">.</span><span class="token function">clearCache</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
<p>小结：一级缓存默认是开启的，只在一次SqlSession中有效，也就是拿到连接到关闭连接这个区间段！</p>
<h1 id="二级缓存" tabindex="-1"><a class="header-anchor" href="#二级缓存" aria-hidden="true">#</a> 二级缓存</h1>
<ul>
<li>二级缓存也叫全局缓存，一级缓存作用域太低了，所以诞生了二级缓存</li>
<li>基于namespace级别的缓存，一个名称空间，对应一个二级缓存</li>
<li>工作机制
<ul>
<li>一个会话查询一条数据，这个数据就会被放在当前会话的一级缓存中</li>
<li>如果当前会话关闭了，这个会话对应的一级缓存就没了；但是我们想要的是，会话关闭了，一级缓存中的数据被保存到二级缓存中；</li>
<li>新的会话查询信息，就可以从二级缓存中获取内容；</li>
<li>不同的mapper查出的数据会放在自己对应的缓存（map）中</li>
</ul>
</li>
</ul>
<p>默认情况下，只启用了本地的会话缓存，它仅仅对一个会话中的数据进行缓存。 要启用全局的二级缓存：</p>
<p>步骤：</p>
<ol>
<li>开启全局缓存</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token comment">&lt;!-- 显式的开启全局缓存--></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>setting</span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>cacheEnabled<span class="token punctuation">"</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">/></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><ol start="2">
<li>在要使用二级缓存的Mapper中开启</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>cache</span>
  <span class="token attr-name">eviction</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>FIFO<span class="token punctuation">"</span></span>
  <span class="token attr-name">flushInterval</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>60000<span class="token punctuation">"</span></span>
  <span class="token attr-name">size</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>512<span class="token punctuation">"</span></span>
  <span class="token attr-name">readOnly</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">/></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>这个更高级的配置创建了一个 FIFO 缓存，每隔 60 秒刷新，最多可以存储结果对象或列表的 512个引用，而且返回的对象被认为是只读的，因此对它们进行修改可能会在不同线程中的调用者产生冲突。</p>
<ul>
<li><code v-pre>LRU</code> – 最近最少使用：移除最长时间不被使用的对象。</li>
<li><code v-pre>FIFO</code> – 先进先出：按对象进入缓存的顺序来移除它们。</li>
<li><code v-pre>SOFT</code> – 软引用：基于垃圾回收器状态和软引用规则移除对象。</li>
<li><code v-pre>WEAK</code> – 弱引用：更积极地基于垃圾收集器状态和弱引用规则移除对象。</li>
</ul>
<p>readOnly默认为false，为false时需要实体类进行序列化</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">User</span> <span class="token keyword">implements</span> <span class="token class-name">Serializable</span> <span class="token punctuation">{</span>
    <span class="token keyword">private</span> <span class="token keyword">int</span> id<span class="token punctuation">;</span>
    <span class="token keyword">private</span> <span class="token class-name">String</span> userName<span class="token punctuation">;</span>
    <span class="token keyword">private</span> <span class="token class-name">String</span> password<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>小结：</p>
<ul>
<li>只要开启了二级缓存，在同一个Mapper下就有效</li>
<li>所有数据都会先放在一级缓存中；</li>
<li>只有当会话提交，或者关闭的时候，才会提交到二级缓存中！</li>
</ul>
<h1 id="原理" tabindex="-1"><a class="header-anchor" href="#原理" aria-hidden="true">#</a> 原理</h1>
<ol>
<li>先看二级缓存中有没有</li>
<li>再看一级缓存中有没有</li>
<li>查询数据库</li>
</ol>
</div></template>


