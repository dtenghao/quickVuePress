<template><div><h1 id="a-convnet-for-the-2020s" tabindex="-1"><a class="header-anchor" href="#a-convnet-for-the-2020s" aria-hidden="true">#</a> A convnet for the 2020s</h1>
<p>作者: Liu, Zhuang</p>
<h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> <strong>概述</strong></h1>
<p>2020年后Vison Transformers(ViTs)快速的代替ConvNets成为最先进的图像分类模型，但基础的ViT很难处理目标检测和语义分割任务，Swin Transformers的出现，让Transformers 成为了视觉任务中优秀的backbone。</p>
<p>然而这种模型的成功很大程度在于Transformers自身的内在优势，而不是卷积所拥有的固有归纳偏置。</p>
<p>本文的工作是，受ViTs的设计启发，逐步“现代化”一个标准的ResNet，并且发现了很多关键的引起性能差异的组件。这个模型是纯粹的ConvNet，因此被称为ConvNeXt。</p>
<p>ConvNeXt在准确率和扩展性上可以与Transformers竞争，在一些任务上可以超越Swin Transformers的表现，是一个简单且高效的模型。</p>
<hr>
<p>普通的ViTs处理不了目标检测和语义分割等任务，且它的计算复杂度会随图片尺寸的增大呈二次方的速度增长，因此Swin Transfomers出现了，它的滑动窗口等设计理念和卷积网络非常相似，它们所具备的归纳偏置非常的相似，但是Swin Transformers在训练过程和模型宏观微观的结构设计上又与ConvNet非常的不同。因此作者就希望学习借鉴Swin Transformers的设计，使纯粹的卷积网络在性能和效率上能够接近Transformers。</p>
<h1 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> <strong>相关工作</strong></h1>
<p>过去的工作都是想着如何将卷积和自注意力机制结合起来。</p>
<p>ConvMixer使用了动态深度卷积核(dynamic depthwise conv)来代替ViTs中的自注意力模块，证明了使用动态深度卷积核可以达到与Swin差不多的表现，在小规模的情况下，ConvMixer表现更好，计算速度更快。</p>
<p>GFNet使用傅立叶变换处理来代替ViTs中的注意力机制，其中二维离散傅里叶变换将输入的空间特征转换为频域特征，然后通过全局滤波处理，最后反变换映射回空间域。解决了token大小改变带来的计算量问题，同时可以具有全局核的视野。</p>
<p>与许多最近的Transformer或ConvNet设计不同，本文研究的一个主要目标是深入了解标准ResNet的“现代化”过程并实现最先进的性能。</p>
<h1 id="模型设计" tabindex="-1"><a class="header-anchor" href="#模型设计" aria-hidden="true">#</a> <strong>模型设计</strong></h1>
<p>作者在ResNet-50的基础上对模型进行修改。</p>
<p>[data:image/svg+xml,%3Csvg xmlns=&quot;http://www.w3.org/2000/svg&quot; viewBox=&quot;0 0 1434 1816&quot;%3E%3C/svg%3E](data:image/svg+xml,%3Csvg xmlns=&quot;http://www.w3.org/2000/svg&quot; viewBox=&quot;0 0 1434 1816&quot;%3E%3C/svg%3E)</p>
<p>蓝色的bar表示ResNet-50/Swin-T，灰色表示ResNet-200/Swin-B。所有的模型都训练和测试在ImageNet-1K数据集上。</p>
<h2 id="training-techniques" tabindex="-1"><a class="header-anchor" href="#training-techniques" aria-hidden="true">#</a> <strong>Training Techniques</strong></h2>
<p>训练次数从原来的90到300，使用AdamW optimizer，数据增强技术（Mixup, Cutmix, RandAugment, Random Erasing），正则化策略（Stochastic Depth） ，标签平滑。</p>
<p>这一系列的技巧可以让ResNet-50表现从76.1% to 78.8% (+2.7%)</p>
<h2 id="changing-stage-compute-ratio" tabindex="-1"><a class="header-anchor" href="#changing-stage-compute-ratio" aria-hidden="true">#</a> <strong>Changing stage compute ratio</strong></h2>
<p>Swin-T每个stage中block数量的比率为1:1:3:1。因此将原来的比率3:4:6:3调整为3:3:9:3。</p>
<p>这使得准确率从78.8% to 79.4%</p>
<h2 id="changing-stem-to-patchify" tabindex="-1"><a class="header-anchor" href="#changing-stem-to-patchify" aria-hidden="true">#</a> <strong>Changing stem to “Patchify”</strong></h2>
<p>原来的ResNet stem cell 包含了7×7，步长为2的卷积，一个最大池化层，下采样4倍。</p>
<p>ViT相当于使用更大的kernel size（14 or 16），Swin Transformer使用的是4，因此将原来的stem cell 改为4×4，步长为4的卷积层。</p>
<p>准确率从79.4% to 79.5%</p>
<h2 id="resnext-ify" tabindex="-1"><a class="header-anchor" href="#resnext-ify" aria-hidden="true">#</a> <strong>ResNeXt-ify</strong></h2>
<p>ResNeXt使用了分组卷积(grouped convolution)，可以减少模型参数，加快计算。因此作者使用了深度卷积(depth wise convolution，组数等于通道数)。</p>
<p>因为作者注意到了深度卷积与自注意的权重相加操作很像（操作每一个通道的偏置，即只是在空间维度混合信息），后面再接1×1卷积也与ViTs非常相似。</p>
<p>模型的准确率也来到了80.5%。</p>
<h2 id="inverted-bottleneck" tabindex="-1"><a class="header-anchor" href="#inverted-bottleneck" aria-hidden="true">#</a> <strong>Inverted Bottleneck</strong></h2>
<p>MobileNetV2以及Transformer都使用到了Inverted Bottleneck，1:4:1，这样做可以减少下采样块的参数，从而减小模型规模。</p>
<p>模型表现也从80.5% to 80.6%，在ResNet-200 / Swin-B上，模型表现更是从81.9% to 82.6%。</p>
<h2 id="large-kernel-sizes" tabindex="-1"><a class="header-anchor" href="#large-kernel-sizes" aria-hidden="true">#</a> <strong>Large Kernel Sizes</strong></h2>
<p>启发在于ViTs可以获取全局的感受野，即使Swin Transformers改用了窗口自注意力，它的窗口大小也至少是7×7，远比ResNe(X)t的3×3大。</p>
<p>首先为了增大卷积核，需要将深度卷积层上移，因为使用到了Inverted Bottleneck，上移大卷积核可以有效的减少模型参数，Transformers也是这样做的。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/12/image-20230212125309615.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/12/image-20230212125309615.png"></p>
<p>模型表现暂时降到了79.9%。</p>
<p>作者尝试了很多尺寸的卷积核，最后发现7×7是表现最好的，准确率从79.9% (3×3) to 80.6% (7×7)。</p>
<h2 id="replacing-relu-with-gelu" tabindex="-1"><a class="header-anchor" href="#replacing-relu-with-gelu" aria-hidden="true">#</a> <strong>Replacing ReLU with GELU</strong></h2>
<p>一些先进的Transformers如BERT、GPT-2已经开始使用GELU激活函数（被认为是ReLU的更平滑版），作者实验也发现GELU可以用来替代ReLU，尽管准确率没有变化，依旧是80.6%。</p>
<h2 id="fewer-activation-functions" tabindex="-1"><a class="header-anchor" href="#fewer-activation-functions" aria-hidden="true">#</a> <strong>Fewer activation functions</strong></h2>
<p>Transformer和ResNet相比激活函数更少，Transformer只在MLP block后面有一个激活函数，因此作者学习transformer只在两个1×1层间夹了一个激活函数。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211123944766.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211123944766.png"></p>
<h2 id="fewer-normalization-layers" tabindex="-1"><a class="header-anchor" href="#fewer-normalization-layers" aria-hidden="true">#</a> <strong>Fewer normalization layers</strong></h2>
<p>作者只在进入1×1层加了归一化层，准确率已经来到了81.4%。</p>
<p>也尝试了像transformers一样在开始时加一个归一化层，但是对表现并没有提升。</p>
<h2 id="substituting-bn-with-ln" tabindex="-1"><a class="header-anchor" href="#substituting-bn-with-ln" aria-hidden="true">#</a> <strong>Substituting BN with LN</strong></h2>
<p>尽管BN对于大多数视觉任务是首选，但是Transformers改用了LN，也取得了非常好的效果。</p>
<p>传统的ResNet将BN换为LN会使表现下降，但幸运的是，随着网络结构和训练结构的更改，将BN替换LN为不会使模型训练变得困难，准确率甚至更好，来到了81.5%。</p>
<h2 id="separate-downsampling-layers" tabindex="-1"><a class="header-anchor" href="#separate-downsampling-layers" aria-hidden="true">#</a> <strong>Separate downsampling layers</strong></h2>
<p>在Swin Transformers中使用了patch merging层来进行下采样，因此作者在每个block后面都加了一个LN层和一个2×2，步长2。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211131952878.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211131952878.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211132006686.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211132006686.png"></p>
<p>以上的技巧并不新颖，但是并没有工作将它们全部整合到一起。</p>
<p>这些发现非常令人振奋，但是从业者关心的是ConvNeXt相比于Swin Transformers在如目标检测，语义分割等下游任务上的表现，在下一章节，作者将会增大ConvNeXt模型的规模和数据量，评估它们在视觉任务上的表现。</p>
<h1 id="实验" tabindex="-1"><a class="header-anchor" href="#实验" aria-hidden="true">#</a> <strong>实验</strong></h1>
<p>设计不同的模型规模</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211134531617.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211134531617.png"></p>
<hr>
<h2 id="imagenet的表现" tabindex="-1"><a class="header-anchor" href="#imagenet的表现" aria-hidden="true">#</a> <strong>ImageNet的表现</strong></h2>
<p>在ImageNet-1K上实验，在模型大小相近、输入图片大小相同的情况下，ConvNeXt无论是准确率还是速度都有一定的优势。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211134805588.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211134805588.png"></p>
<hr>
<p>有一种主流的观点认为Transformers携带的归纳偏置少，因此当模型规模和数据量变大时，Transformers可以学习到更优秀的信息。</p>
<p>在ImageNet-22k上，实验证明了即使数据量很大，但是ConvNets经过一些恰当的设计，也可以表现的不亚于ViTs，甚至更强。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211135244900.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211135244900.png"></p>
<hr>
<p>作者还讨论了ConvNeXt和ViT之间的表现。</p>
<p>将ConvNeXt变得更像普通的ViT，去掉了下采样层和在所有深度上，保持相同的特征大小(14×14)，其余的结构和之前一样。</p>
<p>ViT-S/B使用的是DeiT的结果，ViT-L使用MAE。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211140707312.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211140707312.png"></p>
<p>可以看到两个模型的表现都非常的相近，因此认为ConvNeXt block的设计非常有竞争力。</p>
<h2 id="下游任务的表现" tabindex="-1"><a class="header-anchor" href="#下游任务的表现" aria-hidden="true">#</a> <strong>下游任务的表现</strong></h2>
<p><strong>Object detection and segmentation on COCO</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211142547393.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211142547393.png"></p>
<p>实验发现ConvNeXt的表现比Swin Transformer相近，甚至更出色。</p>
<p>当在ImageNet-22K上使用更大的模型，一些情况下ConvNeXt会比Swin Transformer在box和maskAP上高出1个点。</p>
<hr>
<p><strong>Semantic segmentation on ADE20K</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211142755513.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/11/image-20230211142755513.png"></p>
<h1 id="总结" tabindex="-1"><a class="header-anchor" href="#总结" aria-hidden="true">#</a> <strong>总结</strong></h1>
<p>文章提出了ConvNeXt，一个纯粹的ConvNet模型，可以在多个视觉任务基准上与最先进的Swin Transformers竞争，同时保留标准ConvNets的简单性和效率。ConvNeXT的表现令人惊讶，但ConvNeXt模型本身并不是全新的，在过去十年中，其中的许多模型设计都是单独研究的，并没有整合到一起来研究。作者希望这项研究的新结果能够挑战几个大众广泛持有的观点，并促使人们重新思考卷积在计算机视觉中的重要性。</p>
</div></template>


