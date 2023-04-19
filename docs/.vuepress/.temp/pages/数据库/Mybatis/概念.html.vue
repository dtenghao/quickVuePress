<template><div><h1 id="什么是mybatis" tabindex="-1"><a class="header-anchor" href="#什么是mybatis" aria-hidden="true">#</a> 什么是MyBatis</h1>
<p>MyBatis 是一款优秀的持久层框架，它支持自定义 SQL、存储过程以及高级映射。MyBatis免除了几乎所有的 JDBC 代码以及设置参数和获取结果集的工作。MyBatis可以通过简单的 XML 或注解来配置和映射原始类型、接口和 Java POJO（Plain Old Java Objects，普通老式 Java 对象）为数据库中的记录。</p>
<h1 id="如何获得mybatis" tabindex="-1"><a class="header-anchor" href="#如何获得mybatis" aria-hidden="true">#</a> 如何获得Mybatis？</h1>
<ul>
<li>maven仓库：</li>
</ul>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token comment">&lt;!-- https://mvnrepository.com/artifact/org.mybatis/mybatis --></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.mybatis<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>mybatis<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>3.4.6<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>
<p>github https://github.com/mybatis/mybatis-3</p>
</li>
<li>
<p>中文文档 https://mybatis.org/mybatis-3/zh/index.html</p>
</li>
</ul>
<h1 id="持久化" tabindex="-1"><a class="header-anchor" href="#持久化" aria-hidden="true">#</a> 持久化</h1>
<p>数据持久化</p>
<ul>
<li>持久化就是将程序的数据在持久状态和瞬时状态转化的过程</li>
<li>内存：断电即失</li>
<li>数据库(Jdbc)，io文件持久化</li>
</ul>
<p><strong>为什么需要持久化？</strong></p>
<ul>
<li>有一些对象，不能让他丢掉</li>
<li>内存太贵了</li>
</ul>
<h1 id="持久层" tabindex="-1"><a class="header-anchor" href="#持久层" aria-hidden="true">#</a> 持久层</h1>
<p>Dao层，Service层，Controller层...</p>
<ul>
<li>完成持久化工作的代码块</li>
<li>层界限十分明显</li>
</ul>
<h1 id="为什么需要mybatis" tabindex="-1"><a class="header-anchor" href="#为什么需要mybatis" aria-hidden="true">#</a> 为什么需要Mybatis？</h1>
<ul>
<li>简单易学</li>
<li>灵活</li>
<li>sql和代码的分离，提高了可维护性</li>
<li>提供映射标签，支持对象与数据库的orm字段关系映射</li>
<li>提供对象关系映射标签，支持对象关系组件维护</li>
<li>提供xml标签，支持编写动态sql</li>
<li>使用的人多！</li>
</ul>
</div></template>


