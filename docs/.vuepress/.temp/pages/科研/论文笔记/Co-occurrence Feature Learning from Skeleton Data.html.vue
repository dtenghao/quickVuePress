<template><div><h1 id="co-occurrence-feature-learning-from-skeleton-data-for-action-recognition-and-detection-with-hierarchical-aggregation" tabindex="-1"><a class="header-anchor" href="#co-occurrence-feature-learning-from-skeleton-data-for-action-recognition-and-detection-with-hierarchical-aggregation" aria-hidden="true">#</a> Co-occurrence Feature Learning from Skeleton Data for Action Recognition and Detection with Hierarchical Aggregation</h1>
<p>作者: Chao Li</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>本文提出了一个端到端的共现特征学习卷积框架。共现特征被分层的策略学习，局部信息逐渐聚合为全局信息。</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>先前的工作使用配对相关位置关节、配对关节的空间方向、基于统计的特征Cov3DJ和HOJ3D。</p>
<p>LSTM虽然可以学习到时间上的关系，但是它很难学习到更深层次的特征</p>
<p>而CNN模型在提取深度特征信息有非常不错的表现，有些工作将时间和关节编码为图片的行和列，但是这样只有卷积核内的相邻关节学习到了共现特征，尽管后面感受野会逐步增大，但还是很难挖掘所有关节的共现信息。</p>
<p>又因为CNN模型在空间上的权重共享机制，模型不能为每个关节单独学习参数。这启发了我们设计一个模型，它能够获得所有关节的全局响应来挖掘不同关节间的关联性。</p>
<p>将每个关节作为一个通道，这样卷积层就可以很容易地学习到所有关节的共现信息。</p>
<p>具体的做法是将输入表示为frames<em>joints</em>3，3是关节的xyz坐标，先使用1<em>1和n</em>1卷积核，学习点层面的特征。然后对输出进行转置，将关节作为通道，这样后续的卷积层就可以分层的聚合所有关节的全局特征。</p>
<h1 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> <strong>方法</strong></h1>
<p>对于输入tensor的维度d1，d2，d3，任何通道的信息都可以被全局的聚合，剩下的两个维度作为局部的上下文内容。</p>
<p>以前的工作都是将关节的坐标作为通道，这样会导致共现特征只是被局部的聚合。</p>
<p>尽管CNN和隐式的学习时间上的特征，但是本文还是专门提出了提取时间特征的模型。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221105113831247.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221105113831247.png"></p>
<p>卷积层的最后一个维度是输出的通道，/2表示最大池化层的步长为2，relu激活函数被添加中conv1，conv5，conv6，fc7后面。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221105114154916.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221105114154916.png"></p>
<p>在stage1，点层面的特征被11和n1卷积层学习，这些卷积核大小被设为1，因此是学习每个关节的3d坐标点层面的特征。</p>
<p>然后进行转置，因此关节维度变成了通道。</p>
<p>stage2，所有接下来的卷积层都来提取所有节点的全局共现特征。</p>
<p>最后feature map被flattened 成一个向量，再经过两个全连接层来进行最后的分类。</p>
<p>这个网络有0.8百万的参数，非常的小，因此容易训练。</p>
</div></template>


