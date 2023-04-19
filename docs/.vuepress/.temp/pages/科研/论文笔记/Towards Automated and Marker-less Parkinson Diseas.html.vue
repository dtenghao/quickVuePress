<template><div><h1 id="towards-automated-and-marker-less-parkinson-disease-assessment-predicting-updrs-scores-using-sit-stand-videos" tabindex="-1"><a class="header-anchor" href="#towards-automated-and-marker-less-parkinson-disease-assessment-predicting-updrs-scores-using-sit-stand-videos" aria-hidden="true">#</a> Towards Automated and Marker-less Parkinson Disease Assessment  Predicting UPDRS Scores using Sit-stand videos</h1>
<p>作者: Deval Mehta</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>通过视频分析深度学习框架来对帕金森UPDRS评估表进行打分评估，效果比临床医生的判断更准确。</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>现在对患者帕金森症状的评估都是靠医生每半年或每年进行评估，而且不同的医生的症状的严重程度理解不同，缺乏可靠性。</p>
<p>于是出现了些方法：如患者可以每天自我诊断，但是这样准确度不高；还有使用可穿戴设备，虽然这样可以给出身体可量化的数据，但是这要求患者每天都要花时间去穿戴。</p>
<p>因此本文提出了基于视频来进行诊断，这种方法患者不需要主动去配合，是一种无接触，被动的方式，输入坐着和站立的运动视频片段，就可以输出预测的UPDRS评估表中的BRADPY和PIGD两项分数。</p>
<h1 id="相关工作" tabindex="-1"><a class="header-anchor" href="#相关工作" aria-hidden="true">#</a> <strong>相关工作</strong></h1>
<p>大多数的技术依靠穿戴设备收集加速度来生成相关的特征来描述运动特征。</p>
<p>基于穿戴的方法有两种：</p>
<ol>
<li>使用全身的穿戴设备来捕捉手腕、腰、脚踝等重要位置的加速度，但这样太麻烦臃肿</li>
<li>使用更简便的手腕佩戴传感器来评估症状</li>
</ol>
<p>目前也出现了一些基于摄像的方法，大多依赖深感摄像头来输出患者的3D骨骼关键点来分析。</p>
<p>而本文是使用RGB摄像头</p>
<h1 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> <strong>方法</strong></h1>
<p>算法流程就是输入一个视频，人体检测器提取人体的边界，并输入到二维姿势评估模型，它可以评估人体关节在2维空间中的位置。接下来三维姿势评估模型会预测关节在三维坐标系的位置。然后输入到一个集成模型中，它包含三个模型来对UPDRS分数进行预测。</p>
<p>关于集成模型中模型的选取，有用到四层感知机、长短期记忆网络LSTMs、时间卷积网络TCN、以及在骨骼动作识别上取得最新进展的分层卷积网络HCN、时空图卷积网络ST-GCN和残差网络Resnet50</p>
<p>数据表示：</p>
<p>对于前面提到的这么多模型，需要根据模型可接受的数据形状来修改输入数据</p>
<p>集成模型中，每个子模型单独进行训练，然后将每个子模型的到的logits相加</p>
<p>更具体的，每个模型会生成一个</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023100702083.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023100702083.png"></p>
<p>的特征，然后需要将其输入到一w个M</p>
<p><em>K的矩阵，得到1</em></p>
<p>K维的输出，K维就代表K个类，分别对应UPDRS的输出分数</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023101026237.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023101026237.png"></p>
<p>然后将每个模型的输出进行相加就得到了总的特征表示</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023101641085.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023101641085.png"></p>
<p>损失函数为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023103912175.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023103912175.png"></p>
<h1 id="实验" tabindex="-1"><a class="header-anchor" href="#实验" aria-hidden="true">#</a> <strong>实验</strong></h1>
<p>共有32个对象，对他们进行测试，一个医生现场打分，作为样本的y值，另外两个医生通过录下来的视频进行打分，待会会跟本文模型的准确率进行对比。对症状打分，文章把它作为分类任务，BRADY有0到3的程度等级，因此共分为4类，PIGD也是同理</p>
<hr>
<p>数据集划分上使用5折交叉验证，然后使用分层，来保留类的分布。</p>
<hr>
<p>验证类特征的分布，使用UMAP对特征进行降维并可视化，可以发现不管是2D还是3D特征，对于不同类它们的特征分布都非常的分散，特征分布不能够很好表现类的分布。</p>
<hr>
<p>训练上，使用Adam梯度下降，特征的时间长度为150。</p>
<p>为了防止过拟合，使用标签平滑策略，它可以使得原先的0值也能拥有较小的值，平滑因子a=0.2模型得到最好的表现。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023110713418.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/10/23/image-20221023110713418.png"></p>
<hr>
<p>实验结果比对，采用f1分数，现实对基础模型的效果进行对比，得出简单的模型如MLP、LSTM、TCN不能完成任务，相对复杂的模型如HCN、ST-GCN、Resnet50对于学习有关的特征表现的更好；</p>
<p>3D特征比2D特征表现更好</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023111827427.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023111827427.png"></p>
<p>再次通过UMAP降维可视化模型倒数第二层的256维特征，可以发现经过模型学习后的特征比原始未学习过的2D、3D特征分布更集中；复杂的Resnet50比简单的TCN学习的特征更好更聚类。</p>
<hr>
<p>将各个模型联合起来建立集成模型，与打分医生的准确率进行对比，发现本文的模型表现更好</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023114126184.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/21/image-20221023114126184.png"></p>
</div></template>


