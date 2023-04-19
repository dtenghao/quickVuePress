<template><div><p>理解我们之前讨论过的不同作用域和生命周期类别是至关重要的，因为错误的使用会导致非常严重的并发问题。</p>
<p><strong>SqlSessionFactoryBuilder</strong></p>
<ul>
<li>一旦创建了<strong>SqlSessionFactory</strong>，就不再需要它了</li>
<li>局部变量</li>
</ul>
<p><strong>SqlSessionFactory</strong></p>
<ul>
<li>说白了就是可以想象为：数据库连接池</li>
<li>SqlSessionFactory 一旦被创建就应该在应用的运行期间一直存在，没有任何理由丢弃它或重新创建另一个实例。</li>
<li>因此SqlSessionFactory 的最佳作用域是应用作用域。</li>
<li>最简单的就是使用单例模式或者静态单例模式。</li>
</ul>
<p><strong>SqlSession</strong></p>
<ul>
<li>连接到连接池的一个请求！</li>
<li><strong>SqlSession</strong>的实例不是线程安全的，因此是不能被共享的，所以它的最佳的作用域是请求或方法作用域</li>
<li>用完之后需要赶紧关闭，否则资源被占用！</li>
</ul>
</div></template>


