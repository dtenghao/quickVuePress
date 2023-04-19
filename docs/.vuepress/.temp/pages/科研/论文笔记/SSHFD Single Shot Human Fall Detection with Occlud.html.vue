<template><div><h1 id="sshfd-single-shot-human-fall-detection-with-occluded-joints-resilience" tabindex="-1"><a class="header-anchor" href="#sshfd-single-shot-human-fall-detection-with-occluded-joints-resilience" aria-hidden="true">#</a> SSHFD Single Shot Human Fall Detection with Occluded Joints Resilience</h1>
<p>作者: Umar Asif</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>跌倒对于老人来说非常的致命，现有的跌倒检测算法缺乏对（外表，不同的摄像头视角，遮挡，背景杂乱）环境的鲁棒性。</p>
<p>因此本文提出了Single Shot Human Fall Detector（SSHFD）算法，即通过一张图片对人是否跌倒进行检测，本文的主要创新有：首先，识别了人体的姿势（不会因为外表而改变）；使用神经网络模型来进行3d姿态估计和跌倒检测，它对于关节缺少（遮挡）也具有鲁棒性</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>基于视频的跌倒检测算法不会像<strong>穿戴设备</strong>一样影响到老人的日常生活；一些方法使用的基于外表的特征在现实中因为外表的多样化、不同的摄像头视角、背景杂乱而难以泛化。还有就是由于缺乏跌倒的大规模公开数据集，因此这些方法不能保证对于现实世界的跌倒环境具有充分的泛化性。</p>
<p>主要的工作有：基于2d和3d表示了人体姿势，它具有很好的表现和很强的鲁棒性；模型对于遮挡导致的数据缺失有很好的识别性。</p>
<h1 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> <strong>相关工作</strong></h1>
<ul>
<li>通过前后景相减生成人体边界框，并且比较连续帧之间的边界框来检测跌倒</li>
<li>比较多个边界框来区分不同的事件</li>
<li>采用模糊神经网络分类器</li>
<li>使用运动分割结合外观、形状信息来学习特征</li>
</ul>
<p>然而，方法一和方法四由于相邻帧之间改变较小，导致精度不高，因此有方法提出使用多视角来进行投票决策；但是这种方法需要不同视角间的同步。</p>
<p>还有方法使用kinect深度地图学习3d特征来进行检测，但是这种方法对硬件的限制导致部署较难。</p>
<h1 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> <strong>方法</strong></h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/29/image-20221029225211147.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/29/image-20221029225211147.png"></p>
<ol>
<li>2d姿态估计。从RGB图像中生存身体关节位置的2d图像</li>
<li>3d姿势估计。以上一步得到的2d图像作为输入预测关节在3d坐标系下的位置</li>
<li>跌倒检测。联合2d姿态和3d姿态预测是否跌倒</li>
</ol>
<h2 id="_2d姿态估计" tabindex="-1"><a class="header-anchor" href="#_2d姿态估计" aria-hidden="true">#</a> <strong>2D姿态估计</strong></h2>
<p>使用了一个人体检测库，对图像中的人物进行识别并生成边界框。</p>
<p>使用Stacked Hourglass (SH) network来从RGB图像中获取关节位置的热力图</p>
<hr>
<p>stacked hourglass model（以下简写做SHM）的主要贡献在于利用多尺度特征来识别姿态。以前估计姿态的网络结构，大多只使用最后一层的卷积特征，这样会造成信息的丢失。事实上，对于姿态估计这种关联型任务，全身不同的关节点，并不是在相同的feature map上具有最好的识别精度。举例来说，胳膊可能在第3层的feature map上容易识别，而头部在第5层上更容易识别，见下图。所以，需要设计一种可以同时使用多个feature map的网络结构。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/7Bt6kZ.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/7Bt6kZ.jpg"></p>
<p>stack意味着对多个hourglass model进行了堆叠。下面这是hourglass model模型</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/UdAi3n.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/UdAi3n.jpg"></p>
<p>左边进行下采样，利用卷积和最大池化层(max pooling)将特征下降到一个很低的分辨率(4x4)；右边进行上采样，使用最邻近插值。左边和右边像沙漏。</p>
<p>Hourglass模块则是采用单一的带有skip layers的管道来为每个分辨率保存空间信息。网络达到其最低分辨率为4x4像素，这样可以通过更小的空间滤波来比较整个图像空间的特征。</p>
<p>对于模块中的每个方框实际上也是一组CNN网络。在论文中，作者有说明这一组CNN网络架构的不同选择会对整体网络的效果会有不同的影响。作者尝试了很多选择，最终作者使用的残差模块(Residual module)作为方框的具体网络架构。从图中可以看到，并没有使用超过3*3大小的卷积核，是因为最近研究发现多个小卷积比单个大卷积能更好的捕捉特征。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/PHGe24.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/PHGe24.jpg"></p>
<p>需要注意的是hourglass处理的是64<em>64大小的图片，因为原本的256</em>256要求大量的GPU资源，因此会在网络开始时使用7*7大小，步长为2的卷积核、残差模块和最大池化层来使图片降为64大小，这不会影响网络对关节的预测能力。</p>
<p>在达到网络的输出分辨率后，会再使用连续两个1×1的卷积层来进行最终的预测，网络的输出是一组热力图(heatmaps)。网络通过每一个heatmap来预测每一个像素上存在人体某一关节点的概率。比如heatmaps的第一个channel的热力图代表人体第一个关节点在整张图上每个像素点上的概率。红黄色意味着这个位置关节的概率很高。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/IU3zo9.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/IU3zo9.jpg"></p>
<p>热力图代表了输入对象的所有关节点，那么热力图就包含了所有关节点的相互关系，可以看作是图模型。所以将第一个沙漏网络给出的热力图作为下一个沙漏网络的输入，就意味着第二个沙漏网络可以使用关节点件的相互关系，从而提升了关节点的预测精度。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/YjXzBJ.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/YjXzBJ.jpg"></p>
<p>模型训练采用了中间监督的方式。传统的识别或者检测网络，loss只比较最后的预测与ground truth之间的差异。因为堆叠沙漏网络的每一个子沙漏网络都会有heat map作为预测，所以将每个沙漏输出的heat map参与到loss中，实验证实，预测精确度要远远好于只考虑最后一个沙漏预测的loss。</p>
<hr>
<p>真正的热力图H_k使用高斯核可以表示为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030094802396.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030094802396.png"></p>
<p>k是表示kth关节，x_k，y_k是真正的关节位置，sigma是超参数，通常设置为4。</p>
<p>因此损失函数为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030095124068.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030095124068.png"></p>
<h2 id="_3d姿态估计" tabindex="-1"><a class="header-anchor" href="#_3d姿态估计" aria-hidden="true">#</a> <strong>3D姿态估计</strong></h2>
<p>需要从2D的关节位置P计算3D关节位置Q。损失函数为</p>
<p>其中L_{3d}是均方误差。</p>
<p>网络结构中有多个全连接层，每个连接层跟着一个批归一化、激活函数relu、dropout层，还使用到了残差连接。</p>
<h2 id="跌倒检测" tabindex="-1"><a class="header-anchor" href="#跌倒检测" aria-hidden="true">#</a> <strong>跌倒检测</strong></h2>
<p>跌掉检测网络由两个子网络F、G组成，F分别利用3D关节和2D关节来生成1024维的特征，输出的两个特征相加后再输入到G网络，来生成类的概率分布。因此网络的损失函数如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030100920357.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030100920357.png"></p>
<p>P*表示真实的label，Lcls是交叉熵损失函数：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030100927161.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/30/image-20221030100927161.png"></p>
<p>y是指示函数，c是真实的概率分布，p是预测概率。</p>
<h2 id="遮挡关节恢复ojd" tabindex="-1"><a class="header-anchor" href="#遮挡关节恢复ojd" aria-hidden="true">#</a> <strong>遮挡关节恢复OJD</strong></h2>
<p>由于一些因素如图片不完美、遮挡、背景杂乱或者不正确的关节标注会造成2D姿态输出的不正确从而影响整个模型的性能，因此本文提出了OJR方法来创建一个遮挡的模式M，它将原始的姿态数据转化为遮挡的姿态数据。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221030101624585.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221030101624585.png"></p>
<p>J_i表示第i个关节的位置，v_i是一个二元变量，表示该关节是否可见。</p>
<p>在训练中OJR生成了一个丰富的数据库，它可以大大提高网络在遮挡情况下的鲁棒性。</p>
<h1 id="实验" tabindex="-1"><a class="header-anchor" href="#实验" aria-hidden="true">#</a> <strong>实验</strong></h1>
<p>在MS COCO Keypoints 数据集上训练2d姿态网络。</p>
<p>在合成的人体跌倒数据集上训练3d姿态网络。</p>
<p>对于3D姿态估计和跌倒检测，训练的细节：</p>
<ul>
<li>权重初始化使用零均值高斯分布</li>
<li>训练迭代次数为300次</li>
<li>学习率为0.01，当迭代次数达到50%、75%时缩小10倍</li>
<li>drouptout率设为0.5</li>
<li>使用adam优化方法</li>
</ul>
<p>因为数据集中跌倒类别相对于未跌倒数量较少，所以将跌倒类别的权重增大来平衡这种分布均衡的情况。</p>
<hr>
<p>实验结果：</p>
<ul>
<li>使用2d和3d数据可以使得模型在两个数据集上表现更好，而跌倒检测网络使用ResNet(RGB)在其中一个数据集表现更好，但是在外表和背景变化大的情况下表现很差。这意味着我们的模型可以在现实情景中有很好的泛化性，也说明3d特征是对2d特征很好的补充</li>
<li>使用OJR模型可以提高模型表现，2d3d的姿态表示方法也可以提高表现</li>
<li>使用OJR可以使得模型预测值和实际值的平均欧氏距离更小，OJR能够很好的恢复2d姿态中缺失的信息</li>
</ul>
</div></template>


