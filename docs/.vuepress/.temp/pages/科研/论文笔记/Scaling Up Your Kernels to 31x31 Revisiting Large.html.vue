<template><div><h1 id="scaling-up-your-kernels-to-31x31-revisiting-large-kernel-design-in-cnns" tabindex="-1"><a class="header-anchor" href="#scaling-up-your-kernels-to-31x31-revisiting-large-kernel-design-in-cnns" aria-hidden="true">#</a> Scaling Up Your Kernels to 31x31/ Revisiting Large Kernel Design in CNNs</h1>
<p>作者: Ding, Xiaohan</p>
<blockquote>
<p>Ding, Xiaohan, et al. &quot;Scaling up your kernels to 31x31: Revisiting large kernel design in cnns.&quot; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.</p>
</blockquote>
<h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> <strong>概述</strong></h1>
<p>作者重新研究了大卷积核的设计，提出了使用<strong>少量的大卷积核</strong>代替<strong>多个小卷积核</strong>的堆叠，可以使模型具有更好的表现。</p>
<p>文章提出了五条经验性方法，例如使用<strong>重参数化</strong>（re-parameterized）的大<strong>深度卷积</strong>(depth-wise convolutions)来设计大核CNNs。</p>
<p>提出了RepLKNet，一种纯粹的CNN网络，它的卷积核大小可以达到31×31</p>
<p>RepLKNet可以使CNNs接近ViTs的表现，在ImageNet和ADE20K数据集上的表现相比于相同模型大小的最新模型非常的有竞争力。</p>
<p>大核CNNs比小核CNNs有更大的有效感受野(effective receptive fields)，更高的形状偏置（而不是纹理偏置）</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/08/image-20230208194132965.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/08/image-20230208194132965.png"></p>
<hr>
<p>ViTs中的多头注意力机制(MHSA)层可以获取更大的区域信息，而CNNs却更习惯使用小核，思考能不能使用更大的核来使得CNNs表现接近ViTs。</p>
<p>使用大的深度卷积核(depth-wise convolutions)来代替传统卷积，经过一系列实验，得出了五条经验性的方针：</p>
<ol>
<li>在实践中，大卷积核依旧是有效的</li>
<li>identity shortcut 对于大卷积核网络非常的重要</li>
<li>小卷积核的重参数(re-parameterizing)化有助于解决优化问题</li>
<li>大卷积核对于下游任务的帮助比ImageNet更大</li>
<li>大卷积核对于小特征图依旧非常的有效</li>
</ol>
<p>论文发现大卷积核对下游任务特别有用，比如对于COCO检测数据集和ADE20K分割数据集，模型更小的情况下甚至比Swin Transformers表现更好。</p>
<p>作者认为原因在于大卷积核拥有更大的有效感受野(effective receptive fields)。</p>
<h1 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> <strong>相关工作</strong></h1>
<h2 id="大卷积核" tabindex="-1"><a class="header-anchor" href="#大卷积核" aria-hidden="true">#</a> <strong>大卷积核</strong></h2>
<p>自从VGG-Net之后，大核卷积如Inceptions、GCNs变得不再受欢迎，因为大家认为大核卷积在ImageNet的表现不好。</p>
<p>LR-Net提出了空间聚合操作（动态卷积核）来代替传统卷积，但是在卷积核大小达到7×7以后，再增大就会导致表现下降。</p>
<p>Swin Transformers使用了移动窗口注意力，它的窗口大小在7至12之间，可以视为大卷积核。因此有工作使用动态7×7深度卷积核来代替Swin Transformers的多头注意力层。虽然它的思路跟本文很像，但是他没有探究ERFs、大核卷积、表现它们之间的关系，相反，他将ViTs的优越性归结于稀疏连接，共享参数以及动态机制。</p>
<p>还有三个代表性的工作是Global Filter Networks (GFNets)，CKConv和FlexConv。GFNet优化了傅里叶域中的空间连接权值，相当于空间域中的圆形全局卷积。CKConv将卷积核定义为处理顺序数据的连续函数，可以构造任意大的卷积核。FlexConv为不同的层学习不同的卷积核大小，可以像特征映射一样大。虽然他们使用了大核卷积，但是他们没有试图去回答：为什么传统卷积网络比ViTs弱，如何在卷积网络中使用大核卷积。</p>
<p>另外，他们的工作也没有与Swin Transformer进行充分的比较，因此不清楚大核卷积能否像transformers一样具有良好的扩展性。</p>
<p>还有一些同期工作，他们的模型虽然有优越的表现，但是并没有展示更大的卷积核(31×31)的优越性。</p>
<h2 id="模型缩放-model-scaling" tabindex="-1"><a class="header-anchor" href="#模型缩放-model-scaling" aria-hidden="true">#</a> <strong>模型缩放(Model Scaling)</strong></h2>
<p>目前模型缩放的重点都还是模型的深度、宽度、输入分辨率、瓶颈比等，而卷积核大小总是被忽略。本文将会说明卷积核大小同样也是一个重要的技巧，特别是对于处理下游任务。</p>
<h1 id="如何应用大卷积核" tabindex="-1"><a class="header-anchor" href="#如何应用大卷积核" aria-hidden="true">#</a> <strong>如何应用大卷积核</strong></h1>
<h2 id="guideline-1-dw" tabindex="-1"><a class="header-anchor" href="#guideline-1-dw" aria-hidden="true">#</a> <strong>Guideline 1:DW</strong></h2>
<p>可以使用深度卷积核来解决大卷积核带来的计算量大问题。本文提出的RepLKNet的四个阶段卷积核大小从3,3,3,3变为31,29,27,13，参数量只增多了10.4%。</p>
<p>这也带来了一个问题：DW卷积在GPUs上计算不高效，原因在于DW操作的计算和内存访问比例较低。然而作者发现当核变大时，计算密度也会增加。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209104839961.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209104839961.png"></p>
<p>然而作者发现Pytorch等深度学习框架对大核的DW卷积支持不好，因此</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209105500027.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209105500027.png"></p>
<p>对比</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209105539768.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209105539768.png"></p>
<h2 id="guideline-2-shortcut" tabindex="-1"><a class="header-anchor" href="#guideline-2-shortcut" aria-hidden="true">#</a> <strong>Guideline 2: shortcut</strong></h2>
<p>identity shortcut对于大卷积核网络非常的有效。作者将MobileNet V2作为基准模型，将它的3×3 layers 改为 13×13，两个模型都训练在ImageNet上，同样的设置，训练100 epochs</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209110223732.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209110223732.png"></p>
<h2 id="guideline-3-re-parameterizing" tabindex="-1"><a class="header-anchor" href="#guideline-3-re-parameterizing" aria-hidden="true">#</a> <strong>Guideline 3: re-parameterizing</strong></h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209121628050.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209121628050.png"></p>
<p>使用并行3×3卷积核来进行结构重参数。</p>
<p>具体方式是，训练时将大核上并行一个3×3卷积核，两个核经过BN后相加。</p>
<p>训练完成后，将小核和BN参数一起合并到大核中，只保留大核。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209122354261.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209122354261.png"></p>
<p>使用了这样简单的重参数，增大核大小从9到13不再会降低模型表现了（ImageNet核Cityscapes）</p>
<h2 id="guideline-4-downstream-tasks" tabindex="-1"><a class="header-anchor" href="#guideline-4-downstream-tasks" aria-hidden="true">#</a> <strong>Guideline 4:downstream tasks</strong></h2>
<p>大核卷积对于下游任务的表现比在ImageNet分类任务上的表现更出色。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209124506916.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209124506916.png"></p>
<p>作者认为大的卷积核拥有更大的ERFs，而大的ERFs对于一些下游任务如目标检测、语义分割等非常重要。大的卷积可以获取更多的形状偏置，ImageNet 的图片正确分类同时需要纹理和形状信息，然而人类识别对象更多基于形状信息而不是纹理，因此模型拥有很强的形状偏置对下游任务更加的有效。最近的一些工作也指出ViTs也有很强的形状偏置。</p>
<h2 id="guideline-5-small-feature-maps" tabindex="-1"><a class="header-anchor" href="#guideline-5-small-feature-maps" aria-hidden="true">#</a> <strong>Guideline 5:small feature maps</strong></h2>
<p>就算卷积核比feature maps大，更大的卷积也依旧更有效。</p>
<p>MobileNet V2 最后一阶段的feature map为7×7</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209125432294.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209125432294.png"></p>
<h1 id="replknet" tabindex="-1"><a class="header-anchor" href="#replknet" aria-hidden="true">#</a> <strong>RepLKNet</strong></h1>
<p><strong>Stem</strong> 为模型第一层，希望通过多个conv layers捕捉更多的细节。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209131230917.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209131230917.png"></p>
<p><strong>Stages 1-4</strong> 包含了多个RepLK块，DW卷积使用一个5×5的卷积核用来重参数，1×1 layers来增加通道深度，提高非线性，每个RepLK Block后面都跟着一个ConvFFN</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209131627066.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209131627066.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209133428127.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209133428127.png"></p>
<p><strong>Transition Blocks</strong> 负责增大通道数和下采样</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209130342177.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209130342177.png"></p>
<p>模型可以设置三个超参数，B(RepLK Blocks的数量)，C(通道数)，K(核大小)</p>
<h1 id="实验" tabindex="-1"><a class="header-anchor" href="#实验" aria-hidden="true">#</a> <strong>实验</strong></h1>
<h2 id="增大卷积核" tabindex="-1"><a class="header-anchor" href="#增大卷积核" aria-hidden="true">#</a> <strong>增大卷积核</strong></h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209134304799.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209134304799.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209134933665.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209134933665.png"></p>
<p>在下游任务上提升明显，模型规模小。</p>
<h2 id="imagenet-分类" tabindex="-1"><a class="header-anchor" href="#imagenet-分类" aria-hidden="true">#</a> <strong>ImageNet 分类</strong></h2>
<p>将上面的RepLKNet-31模型作为B(base)模型</p>
<p>C = [192, 384, 768, 1536]作为L(Large)</p>
<p>C = [256, 512, 1024, 2048]为XL</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209135944717.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209135944717.png"></p>
<h2 id="语义分割" tabindex="-1"><a class="header-anchor" href="#语义分割" aria-hidden="true">#</a> <strong>语义分割</strong></h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140438542.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140438542.png"></p>
<p>在1K 预训练的31B比其他Backbone表现高出好几个点，甚至比在22K预训练的Swin-L更强。</p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140636617.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140636617.png"></p>
<h2 id="目标检测" tabindex="-1"><a class="header-anchor" href="#目标检测" aria-hidden="true">#</a> <strong>目标检测</strong></h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140913492.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/09/image-20230209140913492.png"></p>
<h1 id="总结" tabindex="-1"><a class="header-anchor" href="#总结" aria-hidden="true">#</a> <strong>总结</strong></h1>
<p>虽然大卷积核可以显著提高CNNs在ImageNet和下游任务上的表现，但是随着数据和模型规模的进一步扩大，RepLKNets的表现开始落后于Swin Transformers。目前还不清楚这种差距是由次优超参数调优导致的，还是当数据/模型规模扩大时cnn出现的其他一些基本缺陷造成的。作者正在努力解决这个问题。</p>
<p>本文重新讨论了在设计CNN结构时长期被忽视的卷积核大小。作者证明，使用几个大卷积核而不是许多小卷积核可以更有效地获取更大的有效感受野，极大地提高CNN的性能，特别是在下游任务上的性能，并在数据和模型规模扩大时大大缩小CNN和ViTs之间的性能差距。文章的工作能够同时促进CNN和ViTs的研究。一方面，对于CNN，发现表明应该特别关注ERFs，这可能是高性能的关键。另一方面，对于ViT来说，由于大卷积可以替代具有相似行为的多头自关注，这可能有助于理解自关注的内在机制。</p>
</div></template>


