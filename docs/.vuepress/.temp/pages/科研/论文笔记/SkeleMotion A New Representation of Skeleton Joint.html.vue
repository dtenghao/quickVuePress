<template><div><h1 id="skelemotion-a-new-representation-of-skeleton-joint-sequences-based-on-motion-information-for-3d-action-recognition" tabindex="-1"><a class="header-anchor" href="#skelemotion-a-new-representation-of-skeleton-joint-sequences-based-on-motion-information-for-3d-action-recognition" aria-hidden="true">#</a> SkeleMotion A New Representation of Skeleton Joint Sequences Based on Motion Information for 3D Action Recognition</h1>
<p>作者: Carlos Caetano</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>本文提出了一个新的骨架图像表示方法SkeleMotion，通过计算运动幅度和方向来编码时间方向上的信息。再通过设置不同时间尺度来捕捉聚合更多的时间信息，使得特征能够捕捉到更长时间关节间的联系。</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>相比RGB图像和光流，骨架数据量少，计算效率更高，对不同情景下的鲁棒性更高。</p>
<p>RNN方法在建模运动的时间序列上有很好的优势，但是不能很好的学习到关节的空间关系。</p>
<p>有些算法与本文很像，都考虑编码运动信息，可是它们只考虑了连续帧间的运动。</p>
<h1 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> <strong>方法</strong></h1>
<p>首先得到矩阵S（C<em>T</em>3），c是关节数，t是帧，3是3d坐标，于是就可以计算出t时间关节和t+d时间关节间的移动方向</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233555973.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233555973.png"></p>
<p>所以D矩阵的大小为（C，T-d，3）</p>
<p>在通过D矩阵来计算幅度和角度：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233716029.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233716029.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233729781.png" alt="image-20221110233729781"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233729781.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233729781.png"></p>
<p>有的关节可能没移动，但由于识别的问题，有了微小的偏差，为了消除噪声的影响，设定了阈值m</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233956650.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221110233956650.png"></p>
<p>对于移动小于m的关节，令其为0，最后对矩阵固定到C*100的大小。</p>
<hr>
<p>文章中还为了更加能够捕获到长距离关节间的联系，使用了不同的d分别生成一个M和S，再对他们进行堆叠，这样消除噪声的阈值也要随着d的大小而更改</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/10/image-20221110235505040.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/10/image-20221110235505040.png"></p>
<hr>
<p><strong>Resnet50</strong></p>
<p>resnet50有50层，为了解决深度带来的梯度问题，为网络引入了残差结构</p>
<p>网络结构如下</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/11/ResNet.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/11/ResNet.png"></p>
<p>数据input进来，经过5个stage，得到输出</p>
<p>这里可以注意到网络使用了多个bottleneck残差块，bottleneck用1<em>1，3</em>3，1<em>1卷积核实现了3</em>3卷积核的功能，通过先降维再升维的操作大大减少了参数数量，还一定程度上增加了网络的非线性。</p>
<p>bottleneck也分为两种结构，其中结构1也称为Convolutional block，对输入维度进行了下采样，结构2称为Identity Block，提高输入的channel。</p>
</div></template>


