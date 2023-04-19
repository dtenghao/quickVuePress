<template><div><h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> 概述</h1>
<p>一个时间序列往往是以下几类变化形式的叠加或耦合</p>
<ul>
<li>长期趋势变动</li>
<li>季节变动</li>
<li>循环变动</li>
<li>不规则变动</li>
</ul>
<h1 id="简单移动平均法" tabindex="-1"><a class="header-anchor" href="#简单移动平均法" aria-hidden="true">#</a> 简单移动平均法</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829084945068.png" alt="image-20200829084945068"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829085000303.png" alt="image-20200829085000303"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829085011960.png" alt="image-20200829085011960">一般N取值在5到200之间。当历史序列的基本趋势变化不大且序列中随机变化成分较多时，N的取值应较大些。</p>
<p>简单移动平均法只适合做近期预测，而且是预测目标的==发展趋势变化不大==的情况。 如果目标的发展趋势存在其它的变化，采用简单移动平均法就会产生较大的预测偏差和 滞后。</p>
<h1 id="加权移动平均法" tabindex="-1"><a class="header-anchor" href="#加权移动平均法" aria-hidden="true">#</a> 加权移动平均法</h1>
<p>相比简单移动平均法，加权移动平均法考虑各期数据的重要性，对近期数据给予较大的权重。</p>
<p><strong>预测值修正：</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829090109205.png" alt="image-20200829090109205"></p>
<p>w的选择具有一定的==经验性==，至于大到什么程度和小到什么程度，则需要按照预测者对序列的了解和分析来确定</p>
<h1 id="二次移动平均" tabindex="-1"><a class="header-anchor" href="#二次移动平均" aria-hidden="true">#</a> 二次移动平均</h1>
<p>在一次移动平均的基础上再进行一次移动平均就是二次移动平均</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829090606567.png" alt="image-20200829090606567"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829090613979.png" alt="image-20200829090613979"></p>
<p>趋势移动平均法对于同时存在直线趋势与周期波动的序列，是一种既能反映趋势变 化，又可以有效地分离出来周期变动的方法。</p>
<p>==总结：==</p>
<p>移动平均最好预测没有明显上升或下降趋势的序列</p>
<h1 id="指数平滑" tabindex="-1"><a class="header-anchor" href="#指数平滑" aria-hidden="true">#</a> 指数平滑</h1>
<ul>
<li>
<p>一次指数平滑</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829091535920.png" alt="image-20200829091535920"></p>
</li>
<li>
<p>二次指数平滑</p>
</li>
<li>
<p>三次指数平滑（常用）</p>
</li>
</ul>
<p>在实用上，类似移动平均法，多取几个α 值进行试算，看哪个预测误差小，就采用哪个。</p>
<p>出了确定α 外还需要==确定初始值==$S_0$ ，当时间序列的数据较多，比如在 20 个以上时，初始值对以后的预测值影响很少，可选用第一期数据为初始值。如果时间序列的数据较少，在 20 个以下时，初始值对以后的预测值影响很大，这时，就必须认真研究如何正确确定初始值。一般以初几期实际值的平均值作为初始值</p>
<p>==α 的选取准则：==</p>
<ul>
<li>如果序列的基本趋势比较稳，预测偏差由随机因素造成，则α 值应取小一些，以减少修正幅度，使预测模型能包含更多历史数据的信息。</li>
<li>如果预测目标的基本趋势已发生系统地变化，则α 值应取得大一些。这样，可以偏重新数据地信息对原模型进行大幅度修正，以使预测模型适应预测目标地新变化。</li>
</ul>
<h1 id="自适应滤波法" tabindex="-1"><a class="header-anchor" href="#自适应滤波法" aria-hidden="true">#</a> 自适应滤波法</h1>
<p>自适应滤波法与移动平均法、指数平滑法一样，也是以时间序列的历史观测值进行 某种加权平均来预测的，它要寻找一组“佳”的权数，其办法是先用一组给定的权数 来计算一个预测值，然后计算预测误差，再根据预测误差调整权数以减少误差。这样反 复进行，直至找出一组“佳”权数，使误差减少到低限度。由于这种调整权数的过 程与通讯工程中的传输噪声过滤过程极为接近，故称为自适应滤波法。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829094549119.png" alt="image-20200829094549119"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829094605009.png" alt="image-20200829094605009"></p>
<p>具体计算方法可看<code v-pre>第24章 时间序列模型</code>第16页的例子</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200829095211106.png" alt="image-20200829095211106"></p>
</div></template>


