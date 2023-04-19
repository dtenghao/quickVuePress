<template><div><h1 id="two-stream-convolutional-networks-for-action-recognition-in-videos" tabindex="-1"><a class="header-anchor" href="#two-stream-convolutional-networks-for-action-recognition-in-videos" aria-hidden="true">#</a> Two-Stream Convolutional Networks for Action Recognition in Videos</h1>
<p>作者: Karen Simonyan</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>在动作识别任务的一个挑战是捕捉静态帧和动态帧之间的互补信息。</p>
<p>本论文的主要工作有：</p>
<ol>
<li>提出了一个融合空间和时间的双流convNet结构</li>
<li>证明了ConvNet训练在多帧密度光流下可以达到非常好的表现</li>
<li>使用了多任务学习，应用在两个动作数据集上，可以用来增加训练数据和提高表现</li>
</ol>
<p>时间和空间网络的解藕可以使得空间网络利用大量已标注的数据进行预训练，提高表现</p>
<h1 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> <strong>相关工作</strong></h1>
<p>有大量的视频动作识别方法是基于局部时空特征的浅层高纬编码，比如有算法算法检测稀疏的时空兴趣点，并将它们用局部时空特征（定向梯度直方图和光流直方图）来表述，然后将这些特征编码为特征袋（在几个时空网格中汇聚，并与SVM分类器结合）。在这之后的工作说明密集的局部特征采样的表现比稀疏兴趣点好</p>
<p>最新的方法不是在时空长方体上计算局部视频特征，而是采用密集的点轨迹。最好表现的表示是运动边界直方图(MBH)，它是基于梯度的特征，分别计算了水平和垂直分布的光流，如果结合更多特征可以进一步提升效果。</p>
<p>在之前的多数工作中，网络的输入都是堆叠的连续视频帧，这意味着需要网络的第一层来学习视频的时空相关的特征，这非常的困难。一种视频识别的HMAX架构是在网络第一层预先定义了一个时空过滤器，然后与空间HMAX模型结合，形成了空间和时间的识别流。而本文是手动制作的。大量动作识别的ConvNet架构对于单个视频帧和一叠帧的表现相似，这意味着学习到的时空特征不能很好地捕捉动作。</p>
<p>本文的时间流ConvNet使用的是多帧的密集光流，它是在能力最小化框架中求解位移场得到的。采用的方法是基于强度和梯度的恒定假设以及位移场的平滑性来计算能量。</p>
<h1 id="双流架构" tabindex="-1"><a class="header-anchor" href="#双流架构" aria-hidden="true">#</a> <strong>双流架构</strong></h1>
<p>单帧空间部分可以体现情景、对象；</p>
<p>多帧时间部分可以描述相机和对象的运动状态。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221022200225123.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221022200225123.png"></p>
<h2 id="空间流convnet" tabindex="-1"><a class="header-anchor" href="#空间流convnet" aria-hidden="true">#</a> <strong>空间流ConvNet</strong></h2>
<p>这个网络本文使用的是现有的网络，因为现有的网络已经被提前用大量的数据集训练过了。</p>
<h2 id="时间流convnet" tabindex="-1"><a class="header-anchor" href="#时间流convnet" aria-hidden="true">#</a> <strong>时间流ConvNet</strong></h2>
<p>不同于前面提到的网络，本文的输入是一些连续帧的光流位移场，网络不再需要去感受运动的变化了，运动已经被我们描述好了。</p>
<p>d_t(u,v) 表示了坐标为u、v的在t时刻的位移方向向量，将这些方向堆叠就得到了2L长的输入，2k-1是奇数，放入x方向的方向向量，2k偶数放入y方向的。I则表示tao帧之后的L帧的的运动状况</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022200753846.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022200753846.png"></p>
<hr>
<p>还有一种运动表示方法，即轨迹堆叠</p>
<p>既然有了运动方向，那不如直接把点的运动轨迹计算出来</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022201636827.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022201636827.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022201859747.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/22/image-20221022201859747.png"></p>
<hr>
<p>双向光流就是考虑tao帧前的L/2帧以及以后的L/2帧</p>
<hr>
<p>Mean flow subtraction平均流相减：</p>
<p>对于本文的问题，位移向量可能会被相机移动等全局运动所影响，通常需要减去。本文用位移向量d减去平均向量这样一种很简单的方式来调整。</p>
<hr>
<p>前面的方法与本文提出的时间流ConvNet的联系</p>
<p>基于特征编码的特征表达方式是由光流中计算出来的，因此可以被我们的网络捕捉。</p>
<p>HOF和MBH和一些运动特征都是根据光流或者它的梯度计算出来的，因此也可以被我们的网络捕捉</p>
<p>在3.3节，可视化了卷积滤波器学习到的轨迹特征，来证明我们的特征很好的学习到了运动特征</p>
<p>然后提到了双HMAX模型，不如我们经过区分训练的模型深度大。</p>
<p>而对于不解耦时空的模型，依赖于运动敏感的卷积滤波器，不好</p>
<p>最后是提到了一些关于光流位移场的假设，这些应用到模型中都可以提高模型的性能</p>
<h1 id="多任务学习" tabindex="-1"><a class="header-anchor" href="#多任务学习" aria-hidden="true">#</a> <strong>多任务学习</strong></h1>
<p>有两个数据集，希望都利用起来，如果只是简单的合并会由于两个集合类有交集显得不那么直接了当；如果仅仅添加原数据集没有的类，需要手动添加比较的麻烦。</p>
<p>所以想到多任务学习，模型对两个数据集分别进行学习，最后对它们两个的损失函数进行合并。</p>
<h1 id="应用细节" tabindex="-1"><a class="header-anchor" href="#应用细节" aria-hidden="true">#</a> <strong>应用细节</strong></h1>
<p>训练细节上，</p>
<p>所有的隐藏层都使用到了relu激活函数，3*3大小的最大池化层，步长为2</p>
<p>使用小批量梯度下降，对图像进行剪裁，进行反转，RGB抖动等数据增强</p>
<p>在imageNet数据集上进行预训练</p>
<p>梯度下降上使用多GPU训练</p>
<p>提前计算光流来加快计算</p>
<h1 id="测试" tabindex="-1"><a class="header-anchor" href="#测试" aria-hidden="true">#</a> <strong>测试</strong></h1>
<p>使用UCF-101和HMDB=51数据集</p>
<p>对于空间流网络，检验了三种情况：</p>
<ol>
<li>直接在UCF-101上训练</li>
<li>先在ILSVRC-2012上训练，然后到UCF-101训练</li>
<li>也是ILSVRC-2012上训练，只使用UCF-101训练最后一层</li>
</ol>
<p>可以发现重新训练全参数和只训练最后一层的参数结果差不多，因此后面都是使用第三种训练方式</p>
<hr>
<p>对于时间流网络：</p>
<p>对光流堆叠的长度，光流堆叠和轨迹堆叠，以及是否使用Mean subtraction的表现进行了检验</p>
<p>得出光流堆叠，长度为10，双向堆叠，使用mean subtraction表现最好，同时时间流网络比空间流网络的表现更好</p>
<hr>
<p>对多任务学习的表现进行了检验</p>
<p>得出多任务学习表现更好</p>
<hr>
<p>然后是关于两个网络融合方式对性能带来的影响进行了检验</p>
<hr>
<p>最后对比了当先最新的技术</p>
</div></template>


