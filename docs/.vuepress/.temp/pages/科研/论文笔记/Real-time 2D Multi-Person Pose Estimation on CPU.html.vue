<template><div><h1 id="real-time-2d-multi-person-pose-estimation-on-cpu-lightweight-openpose" tabindex="-1"><a class="header-anchor" href="#real-time-2d-multi-person-pose-estimation-on-cpu-lightweight-openpose" aria-hidden="true">#</a> Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose</h1>
<p>作者: Daniil Osokin</p>
<h1 id="openpose" tabindex="-1"><a class="header-anchor" href="#openpose" aria-hidden="true">#</a> <strong>OpenPose</strong></h1>
<p>openpose算法能够有效的检测一个图像中的多人。通过两个分支来学习到部位的位置和关联性。</p>
<p>自顶向下的单人pose估计，当人的检测器失败后，无法做下一步了，另外时间复杂度会随着人数的增加而增加。因此自底向上的方法能够解耦这样问题</p>
<p>openpose就是自底向上的方法，先检测出所有人的关节点，再将关节点分配给每一个对应的人进行连接形成图。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/q8oZz0.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/q8oZz0.jpg"></p>
<p>模型大致如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/04/r1k88h.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/04/r1k88h.jpg"></p>
<p>feature maps F采用VGG-19前10层提取的特征，然后进入多阶段的网络，branch1就是生成关节点的confidence map。</p>
<p>branch2生成关节间的关联度。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/v2-944228be69ac0b0b97ee7a8a13917b7a_1440w.webp" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/v2-944228be69ac0b0b97ee7a8a13917b7a_1440w.webp"></p>
<p>比如对于第k个人他的j1和j2节点间的像素点，属于limb c，它们都会有向量值v，如果不在这两个关节间则为0</p>
<p><img src="https://pic3.zhimg.com/80/v2-30b7c944c98c4468400dae5cf10b32e2_1440w.webp" alt="https://pic3.zhimg.com/80/v2-30b7c944c98c4468400dae5cf10b32e2_1440w.webp"></p>
<p>然后将limb c的所有像素点向量进行求平均操作，就得到了这个limb它的关联性。</p>
<p>然后就可以对关节进行分配连接，这实际上是二分图（可以被划分为两个部分，每个部分内的点互不相连）问题，可以使用匈牙利算法求解，最终合并为多个人的骨架。</p>
<h1 id="lightweight-openpose" tabindex="-1"><a class="header-anchor" href="#lightweight-openpose" aria-hidden="true">#</a> <strong>Lightweight OpenPose</strong></h1>
<p>对openpose算法进行了改进，减少了计算量，提升了算法效率，同时准确率只有1%不到的下降。</p>
<p>主要的改进的地方在于：</p>
<ul>
<li>
<p>只保留了1、2两个stage</p>
</li>
<li>
<p>backbone从VGG19换成了Mobile v1（v2效果不好），同时对它卷积层的步长和空洞参数进行了一定的调整</p>
</li>
<li>
<p>合并branch1、2的部分卷积层</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221104105532602.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221104105532602.png"></p>
</li>
<li>
<p>将7<em>7卷积核换成1</em>1、3<em>3、3</em>3，最后的卷积核空洞参数设为2，来保持一致的感受野（复杂度减少2.5倍），再加上残差连接来缓解网络深度的问题</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221104105837898.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221104105837898.png"></p>
</li>
</ul>
<p>改进后的算法复杂度减少了6.5倍，可以在相同计算资源下实现每秒更多帧的姿态检测。</p>
<h1 id="mobilenet-v1" tabindex="-1"><a class="header-anchor" href="#mobilenet-v1" aria-hidden="true">#</a> <strong>MobileNet v1</strong></h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/3jqza1.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/3jqza1.jpg"></p>
<p>Conv dw 就是Depthwise Convolutions（深度卷积）</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/eaUiBC.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/eaUiBC.jpg"></p>
<p>每个卷积核作用于一个通道。</p>
<p>可以发现MobileNet v1主要基础模块就是：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/DVGFed.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/DVGFed.jpg"></p>
<p>这就是Depthwise Separable Convolutions（深度可分离卷积）</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/1s4ngi.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/03/1s4ngi.jpg"></p>
<p>一个常规的 3x3 Conv 被拆分成了两个部分： 3x3 Depthwise Conv（深度卷积层）和 1x1 Conv（Pointwise逐点卷积层）。</p>
<p>Depthwise没有充分利用不同通道间的信息，因此需要 Pointwise 来将这些特征重新整合。</p>
<p>这样就可以大大减少参数个数，减少运算量。这就是MobileNet v1 相比VGG减少运算量的主要操作，如果愿意牺牲部分性能进一步减少运算量。</p>
</div></template>


