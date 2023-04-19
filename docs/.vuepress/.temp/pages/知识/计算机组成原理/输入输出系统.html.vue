<template><div><h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> 概述</h1>
<h2 id="输入输出系统的组成" tabindex="-1"><a class="header-anchor" href="#输入输出系统的组成" aria-hidden="true">#</a> 输入输出系统的组成</h2>
<ul>
<li>
<p>I/O软件</p>
<ul>
<li>
<p>I/O指令（操作码、命令码、设备码）	CPU指令的一部分</p>
</li>
<li>
<p>通道指令   通道自身的指令</p>
<p>指出数组的首地址、传送字数、操作命令</p>
</li>
</ul>
</li>
<li>
<p>I/O硬件</p>
<ul>
<li>设备</li>
<li>I/O接口</li>
</ul>
</li>
</ul>
<h2 id="i-o设备与主机的联系方式" tabindex="-1"><a class="header-anchor" href="#i-o设备与主机的联系方式" aria-hidden="true">#</a> I/O设备与主机的联系方式</h2>
<ol>
<li>
<p>I/O设备编址方式</p>
<ul>
<li>
<p>统一编址</p>
<p>用取数、存数指令</p>
</li>
<li>
<p>不统一编址</p>
<p>有专门的I/O指令</p>
</li>
</ul>
</li>
<li>
<p>设备选址</p>
<p>用设备选择电路识别是否被选中</p>
</li>
<li>
<p>传送方式</p>
<ul>
<li>串行</li>
<li>并行</li>
</ul>
</li>
<li>
<p>联络方式</p>
<ul>
<li>立即响应</li>
<li>异步工作采用应答信号</li>
<li>同步工作采用同步时标</li>
</ul>
</li>
<li>
<p>I/O设备与主机的连接方式</p>
<ul>
<li>
<p>辐射式连接</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200814105123250.png" alt="image-20200814105123250"></p>
</li>
<li>
<p>总线连接</p>
</li>
</ul>
</li>
</ol>
<h2 id="i-o设备与主机信息传送的控制方式" tabindex="-1"><a class="header-anchor" href="#i-o设备与主机信息传送的控制方式" aria-hidden="true">#</a> I/O设备与主机信息传送的控制方式</h2>
<ol>
<li>
<p>程序查询方式</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200814105749999.png" alt="image-20200814105749999"></p>
</li>
<li>
<p>程序中断方式</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200814110308568.png" alt="image-20200814110308568"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200814110845597.png" alt="image-20200814110845597"></p>
</li>
<li>
<p>DMA方式</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200814111220530.png" alt="image-20200814111220530"></p>
</li>
</ol>
<h1 id="外部设备" tabindex="-1"><a class="header-anchor" href="#外部设备" aria-hidden="true">#</a> 外部设备</h1>
<h1 id="i-o接口" tabindex="-1"><a class="header-anchor" href="#i-o接口" aria-hidden="true">#</a> I/O接口</h1>
<p>为什么要设置接口？</p>
<ol>
<li>实现设备的选择</li>
<li>实现数据缓冲达到速度匹配</li>
<li>实现数据串--并格式转换</li>
<li>实现电平转换</li>
<li>传送控制命令</li>
<li>反映设备的状态（“忙”、“就绪”、“中断请求”）</li>
</ol>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200815112321271.png" alt="image-20200815112321271"></p>
<h1 id="程序查询方式" tabindex="-1"><a class="header-anchor" href="#程序查询方式" aria-hidden="true">#</a> 程序查询方式</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816100130455.png" alt="image-20200816100130455"><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816100614899.png" alt="image-20200816100614899"></p>
<h1 id="程序中断方式" tabindex="-1"><a class="header-anchor" href="#程序中断方式" aria-hidden="true">#</a> 程序中断方式</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816101849921.png" alt="image-20200816101849921"></p>
<ol>
<li>
<p>配置中断请求触发器和中断屏蔽触发器</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816102120826.png" alt="image-20200816102120826"></p>
</li>
<li>
<p>排队器</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816102628529.png" alt="image-20200816102628529"></p>
</li>
<li>
<p>中断向量地址形成部件</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816103451601.png" alt="image-20200816103451601"></p>
</li>
<li>
<p>程序中断方式接口电路的基本组成</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816103721054.png" alt="image-20200816103721054"></p>
</li>
</ol>
<p>中断服务程序的流程</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816104731495.png" alt="image-20200816104731495"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816105012181.png" alt="image-20200816105012181"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200816105509108.png" alt="image-20200816105509108"></p>
<h1 id="dma方式" tabindex="-1"><a class="header-anchor" href="#dma方式" aria-hidden="true">#</a> DMA方式</h1>
<h2 id="dma与主存交换数据的三种方式" tabindex="-1"><a class="header-anchor" href="#dma与主存交换数据的三种方式" aria-hidden="true">#</a> DMA与主存交换数据的三种方式</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818140217740.png" alt="image-20200818140217740"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818140247065.png" alt="image-20200818140247065"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818140308394.png" alt="image-20200818140308394"></p>
<h2 id="dma接口的功能和组成" tabindex="-1"><a class="header-anchor" href="#dma接口的功能和组成" aria-hidden="true">#</a> DMA接口的功能和组成</h2>
<ol>
<li>
<p>DMA接口功能</p>
<ul>
<li>向CPU申请DMA传送</li>
<li>处理总线控制权的转交</li>
<li>管理系统总线、控制数据传送</li>
<li>确定数据传送的首地址和长度</li>
<li>修正传送过程中的数据地址和长度</li>
<li>DMA传送结束时，给出操作完成信号</li>
</ul>
</li>
<li>
<p>DMA接口组成</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818142238584.png" alt="image-20200818142238584"></p>
</li>
<li>
<p>DMA的工作过程</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818190039434.png" alt="image-20200818190039434"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200818202240571.png" alt="image-20200818202240571"></p>
</li>
</ol>
</div></template>


