<template><div><h1 id="为什么用cache" tabindex="-1"><a class="header-anchor" href="#为什么用cache" aria-hidden="true">#</a> 为什么用Cache</h1>
<p>提供“缓存”的目的是为了让数据访问的速度适应CPU的处理速度，其基于的原理是内存中“程序执行与数据访问的局域性行为”，即一定程序执行时间和空间内，被访问的代码集中于一部分。</p>
<p>为了充分发挥缓存的作用，不仅依靠“暂存刚刚访问过的数据”，还要使用硬件实现的指令预测与数据预取技术——尽可能把将要使用的数据预先从内存中取到缓存里。</p>
<h1 id="cache的工作原理" tabindex="-1"><a class="header-anchor" href="#cache的工作原理" aria-hidden="true">#</a> Cache的工作原理</h1>
<h2 id="主存和缓存的编址" tabindex="-1"><a class="header-anchor" href="#主存和缓存的编址" aria-hidden="true">#</a> 主存和缓存的编址</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812225056715.png" alt="image-20200812225056715"></p>
<p>主存和缓存按块存储，块的大小相同</p>
<p>标记用来标记该Cache缓存子块属于哪块主存块号</p>
<h2 id="命中与未命中" tabindex="-1"><a class="header-anchor" href="#命中与未命中" aria-hidden="true">#</a> 命中与未命中</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812225547832.png" alt="image-20200812225547832"></p>
<h2 id="cache的命中率" tabindex="-1"><a class="header-anchor" href="#cache的命中率" aria-hidden="true">#</a> Cache的命中率</h2>
<p>==CPU预访问的信息在Cache中的比率==</p>
<p>命中率与Cache的<strong>容量</strong>与<strong>块长</strong>有关</p>
<p>块长取一个存储周期内从主存调出的信息长度（一般每块可取4~8个字）</p>
<h2 id="cache-主存系统的效率" tabindex="-1"><a class="header-anchor" href="#cache-主存系统的效率" aria-hidden="true">#</a> Cache-主存系统的效率</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812230218299.png" alt="image-20200812230218299"></p>
<h1 id="cache的基本结构" tabindex="-1"><a class="header-anchor" href="#cache的基本结构" aria-hidden="true">#</a> Cache的基本结构</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200812231033175.png" alt="image-20200812231033175"></p>
<p>地址映射：主存的块可以存放在Cache中的哪些块中</p>
<p>变换机构：主存的块在Cache的查找操作</p>
<p>替换机构：由替换算法来决定哪些Cache块被丢弃</p>
<h1 id="cache的读写操作" tabindex="-1"><a class="header-anchor" href="#cache的读写操作" aria-hidden="true">#</a> Cache的读写操作</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200813102529868.png" alt="image-20200813102529868"><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200813103000817.png" alt="image-20200813103000817"></p>
<h1 id="cache的改进" tabindex="-1"><a class="header-anchor" href="#cache的改进" aria-hidden="true">#</a> Cache的改进</h1>
<ol>
<li>增加Cache的级数
<ol>
<li>片载（片内）Cache</li>
<li>片外Cache</li>
</ol>
</li>
<li>统一缓存和分立缓存（与指令执行的控制方式有关，如是否流水）
<ol>
<li>指令Cache</li>
<li>数据Cache</li>
</ol>
</li>
</ol>
<h1 id="cache-主存的地址映射" tabindex="-1"><a class="header-anchor" href="#cache-主存的地址映射" aria-hidden="true">#</a> Cache-主存的地址映射</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200813104101900.png" alt="image-20200813104101900"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200813104445911.png" alt="image-20200813104445911"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200813105039559.png" alt="image-20200813105039559"></p>
<p><strong>小结：</strong></p>
<p>直接	某一主存块只能固定映射到某一缓冲块</p>
<p>全相联	某一主存块能映射到任一缓存块</p>
<p>组相联	某一主存块只能映射到某一缓存组中的几个缓存块中</p>
<h1 id="替换算法" tabindex="-1"><a class="header-anchor" href="#替换算法" aria-hidden="true">#</a> 替换算法</h1>
<ol>
<li>先进先出（FIFO）算法</li>
<li>近期最少使用（LRU）算法</li>
</ol>
</div></template>


