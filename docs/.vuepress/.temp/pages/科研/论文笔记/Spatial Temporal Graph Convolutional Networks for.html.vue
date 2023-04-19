<template><div><h1 id="spatial-temporal-graph-convolutional-networks-for-skeleton-based-action-recognition" tabindex="-1"><a class="header-anchor" href="#spatial-temporal-graph-convolutional-networks-for-skeleton-based-action-recognition" aria-hidden="true">#</a> Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition</h1>
<p>作者: Sijie Yan</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>本文提出了一个SpatialTemporal Graph Convolutional Networks (ST-GCN)，它可以学习到数据中的空间和时间信息，使学习到的特征具有更强的表达性和更好的泛化性。</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>过去的研究都集中在外表轮廓、光流、身体关节(skeletons)来识别动作，通常skeletons会包含更多的信息。研究的重点主要在轮廓和光流。本文将会使用skeletons。</p>
<p>早先的方法直接将单帧的关节坐标作为特征向量，并对它进行时间分析，这种方式不能很好的探索关节的空间信息。</p>
<p>大多数的方法都依赖手动划分区域和规则来分析空间信息，因此模型对于一些特殊的应用很难泛化。</p>
<p>本文使用了图来代替2D和3D坐标。先前的很多工作假设输入为固定的图，而GCNs网络可以对大量数据集建模动态的图。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109135952967.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109135952967.png"></p>
<p>edge共有两种类型，spatial edges和temporal edges</p>
<p>ST-GCN模型不需要手动制作特征，而且还能达到很好的特征表达效果和更好的表现。</p>
<p>模型是基于GCN模型提出的，设计了一个新的图卷积核。</p>
<p>论文的主要工作：</p>
<ol>
<li>ST-GCN是第一个在动作识别上应用图神经网络的模型</li>
<li>设计了很多种卷积核来满足不同的要求</li>
</ol>
<p>模型可以通过图卷积的局部性结合时间上的动态性很好的学习到局部信息。</p>
<h1 id="模型" tabindex="-1"><a class="header-anchor" href="#模型" aria-hidden="true">#</a> <strong>模型</strong></h1>
<p>模型能够关注到局部信息很大的原因是对局部地区的关节轨迹进行了建模。这些表达方式可以被CNN网络很好的学习到。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109141525833.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109141525833.png"></p>
<p>模型的输入是关节的坐标向量</p>
<p>关节集合被表达<code v-pre>v_{ti}</code> ，其中t是帧时间，i是第几个关节。</p>
<p>特征向量<code v-pre>F(v_{ti})</code>由坐标向量和置信度组成。</p>
<p>这样模型可以应用在任何数据集中，不会受关节数量或连接的不同影响。</p>
<p>对于边E，包含了两部分，空间边和时间边。</p>
<hr>
<p>对于局部需要关注到的关节，关注关节v_{ti}周围长度距离D=1的部分关节。</p>
<p>因此<strong>采样函数</strong>可以设计为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109143930970.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109143930970.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109144010531.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109144010531.png"></p>
<hr>
<p>不需要给所有邻居节点一个独立的标签，我们可以简化的采用某种划分策略，将邻居节点划分为固定的K两个子集。所以所有的邻居节点都会被0-K数字进行标签。</p>
<p>然后对于每个标签l_{ti}(v_{tj})，权重函数的定义如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109145505342.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109145505342.png"></p>
<p>每个子集的权重都是相同的，w的shape是(c,K)，c是特征长度，K是类的数量。</p>
<hr>
<p>对于<strong>空间图卷积</strong>可以表示为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109145753982.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109145753982.png"></p>
<p>其中z是子集的节点数量，它可以平衡不同子集输出的分布</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109150026674.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109150026674.png"></p>
<p>进一步的，可以将公式使用上面提到的采样函数和权重函数表示为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109150258064.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109150258064.png"></p>
<p>这其实和普通的卷积核非常的相似，可以应用在标准的2D卷积，只需要将采样函数改为获取9像素的3乘3的网格，将其划分为9个子集。</p>
<hr>
<p><strong>空间时间建模</strong></p>
<p>前面的工作已经建模了空间图CNN，接下来我们要利用关节序列建模空间和时间的动态关系。</p>
<p>这里将邻居节点定义为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109150904533.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109150904533.png"></p>
<p>对于v_{ti}，它的邻居节点为空间上的距离小于K的节点，以及时间上这些节点时间距离小于T/2的节点。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109151059766.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109151059766.png"></p>
<p>如上图红色虚线框中的节点所示。</p>
<p>因为时间轴上是有序的，因此直接修改label map l_{ST}为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109151413404.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109151413404.png"></p>
<p>这表示对于每帧都有k个子集，共有T/2 * k个子集</p>
<hr>
<p><strong>划分策略</strong></p>
<p>文章提出了三种：</p>
<ul>
<li>
<p>Uni-labeling</p>
<p>这种方式直接将整个区域划分为一种类别，不管是节点本身还是它的邻居节点，都同属一个类，因此K=1</p>
</li>
<li>
<p>Distance partitioning</p>
<p>将节点本身作为一个子集，然后它的邻居节点作为一个子集，因此K=2</p>
</li>
<li>
<p>Spatial configuration partitioning</p>
<p>节点本身作为一个子集，然后考虑身体的重心，对于相比节点本身，更靠近重心的节点，将其作为一个子集；更远离重心的节点，将其作为一个节点。</p>
<p>这一策略的灵感来自于身体部位的运动可以被广泛地归类为同心运动和离心运动,通常距离重心越近,运动幅度越小,同时能更好地区分向心运动和离心运动</p>
</li>
</ul>
<p>下图就是三种策略的图像表示：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109152323915.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109152323915.png"></p>
<p>图b，c，d就是三种策略</p>
<hr>
<p><strong>对于第一种划分策略</strong>，ST-GCN可以表达为以下公式：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109233952744.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109233952744.png"></p>
<p>f_in是所有关节的特征矩阵，A是节点的邻接矩阵，I是单位对角矩阵，因此A+I就是节点间的连接情况，W是1<em>1</em>channel的2d卷积，对节点的特征长度进行调整。</p>
<p>A+I就是图卷积核</p>
<p>(A+I)*f_in相当于将节点的特征表示成它的邻接节点特征的聚合</p>
<p>lambda矩阵的ii位置数值是节点i连接的节点数量，然后对lambda -1次就是数值取倒数，左乘行归一化，右乘列归一化</p>
<p>为什么这么做呢？举个例子，如果一个节点它的连接节点非常多，那么它的特征的数值就会相对来说更大一些，这会影响特征分布，因此进行归一化操作。</p>
<p><strong>对于另外两种策略</strong>，公式可以表达为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109235711339.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109235711339.png"></p>
<p>其中：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109235737167.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221109235737167.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109235751074.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/09/image-20221109235751074.png"></p>
<p>这里令alpha=0.001来避免Aj中出现空行。</p>
<p>理解：对于一个节点的特征，它邻接节点间的贡献度（相关度）是不同的，因此将邻接节点按照一定的规则划分为多个子集，比如spatial configuration partitioning策略，将节点划分为三个子集，用三个图卷积核A（邻接矩阵）来提取，这些子集分别乘以各自的2d卷积Wj，来得到新的聚合特征，然后进行加权相加。</p>
<p>即使是相同子集的不同的节点对于运动识别的重要性也是不同的，因此可以考虑<strong>注意力机制</strong>，将邻接矩阵乘以一个可学习的权重矩阵，这样就可以对不同邻接节点产生不同的关注度，不过文章没有详细说明，将这部分作为未来的工作。</p>
<hr>
<p>最后是TCN，</p>
<p>就是（temporal_kernel_size, 1)的卷积核对时间维度进行卷积运算。</p>
<h1 id="训练" tabindex="-1"><a class="header-anchor" href="#训练" aria-hidden="true">#</a> <strong>训练</strong></h1>
<p>最后的模型是9层ST-GCN 单元堆叠，前三层输出64个通道，后面的三层输出128个通道，最后输出256个通道；考虑9帧；每个单元都会加入一个残差网络和dropout层，参数是0.5，然后第4层和第7层加入池化层。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/7b2e57439e2e663dcf898a87e708e333_副本.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/7b2e57439e2e663dcf898a87e708e333_%E5%89%AF%E6%9C%AC.png"></p>
</div></template>


