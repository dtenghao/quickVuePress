<template><div><h1 id="什么是总线" tabindex="-1"><a class="header-anchor" href="#什么是总线" aria-hidden="true">#</a> 什么是总线</h1>
<p>总线是连接各个部件的信息传输线，是各个部件共享的传输介质。</p>
<h1 id="总线上信息传送的方式" tabindex="-1"><a class="header-anchor" href="#总线上信息传送的方式" aria-hidden="true">#</a> 总线上信息传送的方式</h1>
<ol>
<li>串行		传输距离长</li>
<li>并行       如果传输频率高的画，数据线之间会产生很大的干扰，PATA接口的最高传输频率为33MHz，这几乎已经达到了并行接口的极限，传输距离短</li>
</ol>
<h1 id="总线的分类" tabindex="-1"><a class="header-anchor" href="#总线的分类" aria-hidden="true">#</a> 总线的分类</h1>
<ol>
<li>
<p>片内总线</p>
<p>芯片内部的总线</p>
</li>
<li>
<p>系统总线</p>
<p>计算机各部件之间的信息传输线</p>
<ol>
<li>
<p>数据总线</p>
<p>双向 与机器字长、存储字长有关</p>
</li>
<li>
<p>地址总线</p>
<p>单向 与存储地址、I/O地址有关</p>
</li>
<li>
<p>控制总线</p>
<p>有出 有入，如（存储器读、存储器写、总线允许、中断确认）</p>
</li>
</ol>
</li>
<li>
<p>通信总线</p>
<p>用于计算机系统之间 或 计算机系统与其他系统（如控制仪表、移动通信等）之间的通信</p>
</li>
</ol>
<h1 id="总线特性及性能指标" tabindex="-1"><a class="header-anchor" href="#总线特性及性能指标" aria-hidden="true">#</a> 总线特性及性能指标</h1>
<h2 id="总线特性" tabindex="-1"><a class="header-anchor" href="#总线特性" aria-hidden="true">#</a> 总线特性</h2>
<ol>
<li>
<p>机械特性</p>
<p>尺寸、形状、管脚数及排列顺序</p>
</li>
<li>
<p>电气特性</p>
<p>传输方向 和有效的电平范围</p>
</li>
<li>
<p>功能特性</p>
<p>每根传输线的功能，如地址、数据、控制</p>
</li>
<li>
<p>时间特性</p>
<p>信号的时序关系</p>
</li>
</ol>
<h2 id="性能指标" tabindex="-1"><a class="header-anchor" href="#性能指标" aria-hidden="true">#</a> 性能指标</h2>
<ol>
<li>
<p>总线宽度</p>
<p>数据线的根数</p>
</li>
<li>
<p>标准传输率</p>
<p>每秒传输的最大字节数（MBps）</p>
</li>
<li>
<p>时钟同步/异步</p>
<p>同步、不同步</p>
</li>
<li>
<p>总线复用</p>
<p>地址线与数据线复用</p>
</li>
<li>
<p>信号线数</p>
<p>地址线、数据线和控制线的总和</p>
</li>
<li>
<p>总线控制方式</p>
<p>突发、自动、仲裁、逻辑、计数</p>
</li>
<li>
<p>其他指标</p>
<p>负载能力</p>
</li>
</ol>
<h1 id="总线标准" tabindex="-1"><a class="header-anchor" href="#总线标准" aria-hidden="true">#</a> 总线标准</h1>
<h1 id="多总线结构" tabindex="-1"><a class="header-anchor" href="#多总线结构" aria-hidden="true">#</a> 多总线结构</h1>
<h1 id="总线控制" tabindex="-1"><a class="header-anchor" href="#总线控制" aria-hidden="true">#</a> 总线控制</h1>
<h2 id="总线判优控制" tabindex="-1"><a class="header-anchor" href="#总线判优控制" aria-hidden="true">#</a> 总线判优控制</h2>
<h3 id="基本概念" tabindex="-1"><a class="header-anchor" href="#基本概念" aria-hidden="true">#</a> 基本概念</h3>
<p>主设备（模块） 对总线有控制权</p>
<p>从设备（模块）响应从主设备发来的总线命令</p>
<h2 id="总线通信控制" tabindex="-1"><a class="header-anchor" href="#总线通信控制" aria-hidden="true">#</a> 总线通信控制</h2>
<h3 id="目的" tabindex="-1"><a class="header-anchor" href="#目的" aria-hidden="true">#</a> 目的</h3>
<p>为了解决通信双方协调配合问题</p>
<h3 id="总线传输周期" tabindex="-1"><a class="header-anchor" href="#总线传输周期" aria-hidden="true">#</a> 总线传输周期</h3>
<ol>
<li>
<p>申请分配阶段</p>
<p><strong>主模块申请</strong>，总线仲裁决定</p>
</li>
<li>
<p>寻址阶段</p>
<p>主模块向从模块 <strong>给出地址</strong> 和 <strong>命令</strong></p>
</li>
<li>
<p>传数阶段</p>
<p>主模块和从模块 <strong>交换数据</strong></p>
</li>
<li>
<p>结束阶段</p>
<p>主模块 <strong>撤销有关信息</strong></p>
</li>
</ol>
<h3 id="总线通信的四种方式" tabindex="-1"><a class="header-anchor" href="#总线通信的四种方式" aria-hidden="true">#</a> 总线通信的四种方式</h3>
<ol>
<li>
<p>同步通信</p>
<p>由<strong>统一时标</strong>控制数据传送</p>
</li>
<li>
<p>异步通信</p>
<p>采用<strong>应答方式</strong>，没有公共时钟标准</p>
</li>
<li>
<p>半同步通信</p>
<p><strong>同步、异步结合</strong></p>
</li>
<li>
<p>分离式通信</p>
<p>充分 <strong>挖掘</strong> 系统 <strong>总线每个瞬间</strong> 的 <strong>潜力</strong></p>
<ol>
<li>各模块有权申请占用总线</li>
<li>采用同步方式通信，不等对方回答</li>
<li>各模块准备数据时，不占用总线</li>
<li>总线被占用时，无空闲</li>
</ol>
</li>
</ol>
</div></template>


