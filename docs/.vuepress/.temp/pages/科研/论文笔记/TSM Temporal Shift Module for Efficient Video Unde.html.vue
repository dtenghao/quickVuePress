<template><div><h1 id="tsm-temporal-shift-module-for-efficient-video-understanding" tabindex="-1"><a class="header-anchor" href="#tsm-temporal-shift-module-for-efficient-video-understanding" aria-hidden="true">#</a> TSM: Temporal Shift Module for Efficient Video Understanding</h1>
<p>作者: Ji Lin</p>
<h2 id="简介" tabindex="-1"><a class="header-anchor" href="#简介" aria-hidden="true">#</a> 简介</h2>
<ul>
<li>视频理解的重要性简要说明</li>
<li>当前视频理解面临的挑战的解释</li>
</ul>
<h2 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> 相关工作</h2>
<ul>
<li>先前视频理解方法的概述</li>
<li>先前方法的局限性</li>
</ul>
<p><strong>TSN</strong> 是一种基于时间分段的网络模型，它通过将视频分成若干个时间段，然后对每个时间段内的帧进行分类，最终将这些分类结果融合起来得到最终的分类结果。TSN 主要解决的问题是在时间维度上的信息获取问题，它通过时间分段的方式，使得网络能够更好地利用视频序列中的时序信息。在实验中，TSN 取得了较好的分类性能。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic1/main/2023/04/18/Untitled.png" alt="Untitled"></p>
<blockquote>
<ol>
<li>对视频分为若干个时间段，每个时间段由随机采样帧组成</li>
</ol>
</blockquote>
<ol start="2">
<li>对时间段中的帧进行双流分类</li>
<li>对每个片段的的结果进行融合，如平均、最大值等，最后再进行输出</li>
</ol>
<blockquote></blockquote>
<p>TSM的<strong>主要改进</strong>如下：</p>
<ol>
<li>引入Temporal Shift Module：TSM通过在原有卷积神经网络的内部引入时间位移模块，使得模型可以在时间维度上学习局部的时间信息。具体来说，Temporal Shift Module会将输入特征的一部分通道向前（过去）或向后（未来）移动一帧。这种简单的操作能够使网络在不增加额外计算复杂度的情况下，学习到更丰富的时间信息。</li>
<li>端到端训练：与TSN类似，TSM也采用了端到端的训练框架，可以在训练过程中直接学习视频中的时间信息。Temporal Shift Module可以与各种卷积神经网络（如ResNet、Inception等）无缝集成，使得整个模型可以一次性训练。</li>
</ol>
<h2 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> 方法</h2>
<ul>
<li>时间移位模块（TSM）的解释</li>
<li>TSM的技术细节</li>
<li>TSM与先前方法的比较</li>
</ul>
<h2 id="实验" tabindex="-1"><a class="header-anchor" href="#实验" aria-hidden="true">#</a> 实验</h2>
<ul>
<li>实验中使用的数据集的描述</li>
<li>实验设置的解释</li>
<li>实验结果和分析</li>
</ul>
<h2 id="结论" tabindex="-1"><a class="header-anchor" href="#结论" aria-hidden="true">#</a> 结论</h2>
<ul>
<li>发现的总结</li>
<li>TSM对未来视频理解研究的影响和启示</li>
</ul>
<h2 id="复现" tabindex="-1"><a class="header-anchor" href="#复现" aria-hidden="true">#</a> 复现</h2>
<p>我们需要先将视频提取成帧以实现快速读取。请参考 <a href="https://github.com/yjxiong/temporal-segment-networks" target="_blank" rel="noopener noreferrer">TSN<ExternalLinkIcon/></a> 仓库的数据预处理详细指南。</p>
<p>我们已经成功地使用此代码库在 Kinetics、UCF101、HMDB51、Something-Something-V1 和 V2 以及 Jester 数据集上进行了训练。视频数据的处理基本上可以归结为三个步骤:</p>
<ul>
<li>从视频中提取帧 (参见 <a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/tools/vid2img_kinetics.py" target="_blank" rel="noopener noreferrer">tools/vid2img_kinetics.py<ExternalLinkIcon/></a> 中的 Kinetics 示例和 <a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/tools/vid2img_sthv2.py" target="_blank" rel="noopener noreferrer">tools/vid2img_sthv2.py<ExternalLinkIcon/></a> 中的 Something-Something-V2 示例)</li>
<li>生成数据加载器所需的标注 (参见 <a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/tools/gen_label_kinetics.py" target="_blank" rel="noopener noreferrer">tools/gen_label_kinetics.py<ExternalLinkIcon/></a> 中的 Kinetics 示例、<a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/tools/gen_label_sthv1.py" target="_blank" rel="noopener noreferrer">tools/gen_label_sthv1.py<ExternalLinkIcon/></a> 中的 Something-Something-V1 示例以及 <a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/tools/gen_label_sthv2.py" target="_blank" rel="noopener noreferrer">tools/gen_label_sthv2.py<ExternalLinkIcon/></a> 中的 Something-Something-V2 示例)</li>
<li>将信息添加到 <a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/ops/dataset_configs.py" target="_blank" rel="noopener noreferrer">ops/dataset_configs.py<ExternalLinkIcon/></a> 中</li>
</ul>
<p>此代码基于<a href="https://github.com/yjxiong/temporal-segment-networks" target="_blank" rel="noopener noreferrer">TSN<ExternalLinkIcon/></a>代码库。实现时间移位模块的核心代码是<a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/ops/temporal_shift.py" target="_blank" rel="noopener noreferrer">ops/temporal_shift.py<ExternalLinkIcon/></a>。这是一个即插即用的模块，可以实现时间推理，代价是<em>零参数</em>和<em>零FLOPs</em>。</p>
<p>请注意，基础的实现（对x进行左右位移）涉及大量数据复制，在训练期间增加内存消耗。建议使用TSM的<strong>in-place</strong>版本以提高速度（有关详细信息，请参见<a href="https://github.com/0Eumenides/temporal-shift-module/blob/master/ops/temporal_shift.py" target="_blank" rel="noopener noreferrer">ops/temporal_shift.py<ExternalLinkIcon/></a>第12行。）</p>
</div></template>


