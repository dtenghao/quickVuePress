<template><div><h1 id="对比学习" tabindex="-1"><a class="header-anchor" href="#对比学习" aria-hidden="true">#</a> 对比学习</h1>
<p>Time: March 24, 2023 3:48 PM</p>
<h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> <strong>概述</strong></h1>
<p>深度学习通常依赖于海量的标注数据进行模型训练, 才能获得较好的性能表现. 当可用的标注数据较少、而无标注数据较多时, 如何提高深度学习的特征表达能力是亟需解决的重要现实需求。</p>
<p>对比学习是一种自监督学习方法，用于在没有标签的情况下，<strong>通过让模型学习哪些数据点相似或不同来学习数据集的一般特征</strong>。</p>
<p>从一个简单的例子开始。一个试图理解世界的新生婴儿。在家里，假设有两只猫和一只狗。</p>
<p>即使没有人告诉他，它们是“猫”和“狗”，但他仍可能会意识到，与狗相比，这两只猫看起来很相似。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205113108312.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205113108312.png"></p>
<p>本质上，对比学习允许我们的机器学习模型做同样的事情。它会观察哪些数据点对“相似”和“不同”，以便在执行分类或分割等任务之前了解数据更高阶的特征。</p>
<h2 id="instdisc" tabindex="-1"><a class="header-anchor" href="#instdisc" aria-hidden="true">#</a> <strong>InstDisc</strong></h2>
<blockquote>
<p>Wu, Zhirong, et al. &quot;Unsupervised feature learning via non-parametric instance discrimination.&quot; Proceedings of the IEEE conference on computer vision and pattern recognition. 2018.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204100842012.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204100842012.png"></p>
<p>这篇论文提出了个体判别任务（Instance Discrimination）。如上图所示，作者说他们的方法是受到了有监督学习结果的启发，如果我们把一张豹子的图片喂给一个已经用有监督学习训练好的分类器，我们会发现它的结果排名前几的全是和豹子相关的，总之在图片来看这些物体都是长得很相近的。通过这个现象作者认为并不是因为这些标签有相似的语义信息，而是因为它们这些照片长得很像。所以作者根据这个观察提出了个体判别的任务。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204095015571.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204095015571.png"></p>
<p>作者提出无监督学习的方法把每张图片都看成是一个类别，目标就是做到一个特征能把每一个图片都区分开来。</p>
<p>想通过一个卷积神经网络，把一张图片编码成一个特征，他们希望这个特征在最后的特征空间里能尽可能分开。训练的方式使用的就是对比学习，正样本就是每张图本身，再经过一些数据增强，负样本就是数据集里其他的图片，为了防止反复计算图片的特征，论文用了memory bank的形式。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204141422870.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204141422870.png"></p>
<p>即把所有图片的特征全都存到了这个memory bank里，首先每个前向会获取一批数据作为正样本，然后在memory bank里抽一些负样本出来，然后用NCE loss作为对比学习的目标函数进行模型更新。</p>
<p>更新完之后就可以把这个mini-batch的数据样本对应的特征到memory bank里更换，更新memory bank。</p>
<p>迭代过程中损失非常的不平稳，使用Proximal Regularization技巧，给损失函数函数加一个约束，从而能让memory bank里的那些特征进行动量式的更新，后面的moco模型也借用了这种思想</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204142112230.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204142112230.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204142126949.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204142126949.png"></p>
<p>这篇论文实验时的一些参数设置，如学习率、温度tao、训练次数等，后面的moco模型都进行了沿用</p>
<h2 id="invaspread" tabindex="-1"><a class="header-anchor" href="#invaspread" aria-hidden="true">#</a> <strong>InvaSpread</strong></h2>
<blockquote>
<p>Ye, Mang, et al. &quot;Unsupervised embedding learning via invariant and spreading instance feature.&quot; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.</p>
</blockquote>
<p>这篇论文可以理解为SimCLR的一个前身，它没有使用额外的数据结构去存储大量的负样本，它的正负样本就是来自于同一个minibatch,而且只使用一个编码器去进行端到端的学习。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204143003699.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204143003699.png"></p>
<p>论文最基本的思想就是对比学习，即同样的图片通过一个CNN的编码器以后它的特征应该很类似，不同的图片应该不类似。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204143242222.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204143242222.png"></p>
<p>文章的方法效果之所以没有那么好，主要是在做对比学习时负样本最好是足够多，但在这里作者是没有TPU的，所以batch size只能取256，意味着负样本只有500多个，再加上他没有SimCLR那么多的数据增广和mlp projector，所以结果就没有那么好了。</p>
<h2 id="cpc" tabindex="-1"><a class="header-anchor" href="#cpc" aria-hidden="true">#</a> <strong>CPC</strong></h2>
<blockquote>
<p>Oord, Aaron van den, Yazhe Li, and Oriol Vinyals. &quot;Representation learning with contrastive predictive coding.&quot; arXiv preprint arXiv:1807.03748 (2018).</p>
</blockquote>
<p>前两个工作都是用个体判别这个代理任务去做对比学习，接下来就提一个用别的代理任务做对比学习的工作。个体判别属于判别式的代理任务，CPC这种预测就属于生成式的代理任务。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204144359798.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204144359798.png"></p>
<p>CPC提出了一个很通用的结构，它不光可以处理音频，还可以处理图片，文字以及可以在强化学习里面使用。</p>
<h2 id="cmc" tabindex="-1"><a class="header-anchor" href="#cmc" aria-hidden="true">#</a> <strong>CMC</strong></h2>
<blockquote>
<p>Tian, Yonglong, Dilip Krishnan, and Phillip Isola. &quot;Contrastive multiview coding.&quot; Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XI 16. Springer International Publishing, 2020.</p>
</blockquote>
<p>论文的核心观点就是，一个物体的很多个视角都可以被当做正样本。比如一只狗，它可以被视觉视角判断出来，也可以被听觉视角判断出来，即不管你给我看哪个视角，到底是看到了一只狗，还是听到了狗叫声，我都能判断出这是一只狗。所以CMC这篇文章就是想增大这个互信息，如果能学到一种特征，可以抓到所有视角下的这个关键因素，那这个特征就很好了。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204145712404.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204145712404.png"></p>
<p>CMC选取正负样本的方式如上图所示，它选取的是NYU RGBD这个数据集，这个数据集同时有4个view，分别是原始图像，这个图像对应的深度信息，surface normal和语义分割后的图像。cmc就是说虽然这些不同的输入来自不同的传感器，或者说不同的模态，但是所有的输入其实对应的都是一张图片，都是一个东西，所以应该互为正样本。这时候再随机挑一个其他图片，这时候这个图片的特征应该和那四个视角的图片特征尽量远离。</p>
<p>CMC是比较早的工作去做这种多视角的对比学习，它不仅证明了对比学习的这个灵活性，而且证明了多视角多模态的可行性，所以openAI很快就出了CLIP模型。即如果有一个图片，还有描述这个图片的文本，那这个图像和文本就可以当成是一个正样本对，就可以做多模态的对比学习了。同时CMC团队用对比学习还做了一篇蒸馏的工作，意思就是无论用什么网络，只要输入是同一张图片，那么得到的特征应该尽可能相似，也就意味着我们想让teacher模型的输出跟student模型的输出尽可能相似，它就通过这种方式把teacher和student的输出做成了一个正样本对，从而可以做对比学习。</p>
<h1 id="主流模型" tabindex="-1"><a class="header-anchor" href="#主流模型" aria-hidden="true">#</a> <strong>主流模型</strong></h1>
<h2 id="simclr" tabindex="-1"><a class="header-anchor" href="#simclr" aria-hidden="true">#</a> <strong>SimCLR</strong></h2>
<blockquote>
<p>Chen, Ting, et al. &quot;A simple framework for contrastive learning of visual representations.&quot; International conference on machine learning. PMLR, 2020.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204151053523.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204151053523.png"></p>
<p>SimCLR的一个重大创新点就是在这个特征之后，又加了一个叫projector的东西，即g函数，就是一个全连接层跟了一个relu函数。就是这么一个简单的mlp，可以让最后学到的特征在ImageNet上提点将近10个点。我们可以想象有了一个特征h之后，再做一个非线性的变化，就得到另外一个特征z，一般这个z会维度小一点，最后就衡量一下正样本之间是不是能达到最大的一致性。它们采用的是一个叫normalized temperature-scaled的交叉熵函数。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204151543760.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204151543760.png"></p>
<p>需要注意的是projection head只是在训练时被使用，在做下游任务时，使用的是h特征。</p>
<p>SimCLR的主要贡献有：</p>
<ol>
<li>
<p>用了更多的数据增广技术，对对比学习十分有益。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204152034990.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204152034990.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204152832243.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204152832243.png"></p>
</li>
<li>
<p>加了g函数这个可以学习非线性变化的层。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153010910.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153010910.png"></p>
</li>
<li>
<p>用了更大的batch size来让字典更大，而且训练的更久。</p>
</li>
</ol>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153132510.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153132510.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153423282.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204153423282.png"></p>
<hr>
<blockquote>
<p>Chen, Ting, et al. &quot;Big self-supervised models are strong semi-supervised learners.&quot; Advances in neural information processing systems 33 (2020): 22243-22255.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204160437307.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204160437307.png"></p>
<p>重点关注SimCLR v2的升级，主要从这三方面提升：</p>
<ol>
<li>第一方面是大家都公认，无监督学习在模型越大的时候表现会越好，所以这里就换了一个更大的模型，使用了152层的ResNet和selective kernels，来让骨干网络变强。</li>
<li>SimCLR v1提出了projector层，MoCo v2也证明了这个层确实有用，所以SimCLR v2的作者就想这个层变深会不会更有用，于是经过实验发现2层的projector层最好。</li>
<li>使用动量编码器。但是动量编码器在SimCLR v2的提升在一个点以内，主要原因就是SimCLR本身已经有很多的负样本了，所以无论从字典大小和一致性来说已经很好了。</li>
</ol>
<h2 id="moco" tabindex="-1"><a class="header-anchor" href="#moco" aria-hidden="true">#</a> <strong>MoCo</strong></h2>
<blockquote>
<p>He, Kaiming, et al. &quot;Momentum contrast for unsupervised visual representation learning.&quot; Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204165643174.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204165643174.png"></p>
<p>MoCo v1的主要贡献就是把之前的对比学习的一些方法归纳总结成字典查询问题，它提出了两个东西：一个是队列，一个是动量编码器，从而形成了一个又大又一致的字典帮助对比学习。MoCo v1和InstDisc是非常像的，比如它就是用这个队列去取代了原来的memory bank作为一个额外的数据结构去存这个负样本。然后用动量编码器去取代原来loss的约束项从而达到动量更新编码器的目的，而不是动量的去更新那个特征，从而得到更好的结果。</p>
<p>相对于InstDisc维持一个非常大的memory bank，MoCo使用的是一个队列，这个队列通常比batch size大很多，队列的大小作为超参数，队列中的特征是动态更新的，当前batch的特征入队，相对较旧的batch特征出队。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204171316484.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204171316484.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204171350866.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/24/image-20230204171350866.png"></p>
<p>因此key编码器的参数更新会比query编码器的更新更加的平滑，实验发现相对更大的动量，如m=0.999，模型的表现比m=0.9更好。</p>
<p>MoCo的主要优势在于不需要像SimCLR一样使用非常大的batch size，因此计算更加的高效、轻量，同时模型表现非常的好。</p>
<hr>
<blockquote>
<p>Chen, Xinlei, et al. &quot;Improved baselines with momentum contrastive learning.&quot; arXiv preprint arXiv:2003.04297 (2020).</p>
</blockquote>
<p>MoCo团队借鉴了SimCLR模型中即插即用的技术，在MoCo上做很简单的改动，把mlp projectioin head以及更多的数据增强的trick也加进来。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204202000363.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204202000363.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204202120540.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204202120540.png"></p>
<p>最后作者再强调了一下使用MoCo相比于SimCLR的这个优越性，MoCo在普通batch size256就能训练，训练一个模型也只需要53个小时；而SimCLR这种end to end的方式用小的batch效果是很差的，但是消耗的资源和时间也比MoCo多，就更不要说SimCLR用4096的batch size的话，对硬件要求就太高了。</p>
<hr>
<blockquote>
<p>Chen, Xinlei, Saining Xie, and Kaiming He. &quot;An empirical study of training self-supervised vision transformers.&quot; Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112027207.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112027207.png"></p>
<p>可以发现，MoCo v3其实就相当于是MoCo v2和SimSiam的合体，整体还是有2个网络，而且key网络是动量编码器，而且最后的目标函数用的是对比学习的loss，所以从这个角度来讲，它是个MoCo v2。但是query还有projection和predictor，而且目标函数用的是一个对称项，也就是算query1到key2，也算query2到key1，从这个角度讲又是SimSiam。</p>
<p>因为Vision Transformer的爆火，所以作者也将主干网络换为了ViT。但是从实验结果来看，batch size小的时候不会出现什么问题，但是当这个batch size变大了以后，这个曲线会训练训着训着就掉了，最后效果也差了，一般越大的batch size效果应该最好，但在这里却更差了。所以作者认为要解决这个问题，Vision transformer才会发挥它真正的力量。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112322892.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112322892.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/apJONs.jpg" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/apJONs.jpg"></p>
<p>这里论文提出了一个小trick</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112613891.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205112613891.png"></p>
<h2 id="swav" tabindex="-1"><a class="header-anchor" href="#swav" aria-hidden="true">#</a> <strong>SwAV</strong></h2>
<blockquote>
<p>Caron, Mathilde, et al. &quot;Unsupervised learning of visual features by contrasting cluster assignments.&quot; Advances in neural information processing systems 33 (2020): 9912-9924.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204205048432.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204205048432.png"></p>
<ol>
<li>之前的对比学习需要不断计算样本间的相似度，随着batch size的增长，计算负担大大增加。</li>
<li>更多的视角可以提高模型的表现。</li>
</ol>
<p>论文用聚类中心c代替大量的负样本，维度为D*K，D是特征维度，K是聚类中心的个数，让特征Z与C相乘，得到了K维的特征Q。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204211342266.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204211342266.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204211353075.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204211353075.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204212850130.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204212850130.png"></p>
<p>当然SwAV有那么好的性能，不光是因为和聚类的方法融合在了一起，另一个主要的性能提升点是使用了multi-crop技术。</p>
<p>之前的对比学习可能是一张256<em>256，随机crop成2个224</em>224的图片成为一个正样本。这种crop重叠区域非常多，关注是整个场景的特征，作者希望使用更多正样本，关注到一些局部的特征。但是更多的正样本，模型计算量会大大增加，论文的方法是原本crop 2个224<em>224的图片，现在可以把crop变小一点，把原来2个224</em>224的图片区域改成160<em>160的图片，为了关注局部特征，再随机去crop4个96</em>96的图片。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204213952041.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/04/image-20230204213952041.png"></p>
<h2 id="byol" tabindex="-1"><a class="header-anchor" href="#byol" aria-hidden="true">#</a> <strong>BYOL</strong></h2>
<p>对比学习中负样本数越多，模型效果越好，但是负样本数越多模型的计算负担也越大，所以想到能不能不用负样本。上面提到的SwAV就已经有这个趋势了，它使用计算量更小的聚类中心来代替负样本，但接下来要说的BYOL和SimSiam完全就只有正样本，没有负样本和聚类中心。</p>
<blockquote>
<p>Grill, Jean-Bastien, et al. &quot;Bootstrap your own latent-a new approach to self-supervised learning.&quot; Advances in neural information processing systems 33 (2020): 21271-21284.</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205004524620.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205004524620.png"></p>
<p>首先说明为什么没有负样本这么稀奇，因为在对比学习中，负样本是一个约束，如果在算目标函数的时候只有正样本，那其实目的就只有一个，那就是让所有相似的物体它们的特征也尽可能相似，那这个时候就有一个很明显的捷径解：即一个模型不论什么输入，都给你返回同样的输出，那这样模型出来的所有特征都是一模一样的，那拿这个去算对比学习的loss就都是0，这就是所谓的模型坍塌。因此必须加上负样本的约束模型才能继续，样本在对比学习里面是一个必须的东西，防止模型学到一个捷径解。</p>
<p>而BYOL模型与SimCLP很像，但是下面的编码器使用动量更新，而且在上面的projection head 后面又加了一个prediction，它的网络结构也是一个mlp，用来预测下面的动量编码器的输出，用上面的视角来预测下面的视角，希望query和key尽可能的相似。</p>
<p>而且目标函数也非常不同，直接用的mse loss。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205010210104.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205010210104.png"></p>
<hr>
<p>后面有人发现原因是BYOL的Projection和Prediction中有Batch Norm导致的，认为在计算BN的时候使用到了一个batch的所有数据来计算均值和方差，然后用这个均值和方差做归一化，那这也就意味着你在算某个正样本的loss的时候，你也看到了其他样本的这个特征，也就是说这里是有信息泄露的，因为有这个信息泄露的存在，所以可以把这个batch里面的其他样本，想象成一个隐式的这个负样本。</p>
<p><img src="https://pic4.zhimg.com/80/v2-543bce7d50ad8d87b1e95bdae3f85817_1440w.webp" alt="https://pic4.zhimg.com/80/v2-543bce7d50ad8d87b1e95bdae3f85817_1440w.webp"></p>
<blockquote>
<p>Richemond, Pierre H., et al. &quot;Byol works even without batch statistics.&quot; arXiv preprint arXiv:2010.10241 (2020).</p>
</blockquote>
<p>后面BYOL的作者也做出了回应，做了一系列的消融实验</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205010831638.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205010831638.png"></p>
<p>他发现即使有些地方有BN，BYOL还是训练失败了。包括SimCLP在没有提供归一化时也会训练失败，因此作者认为BN的作用还是能帮助这个模型稳定训练，但是不是模型成功的关键。</p>
<p>他使用了group norm和weight standardization，换成这种没有计算统计量的初始化方式之后，模型也可以训练到差不多的效果。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205011107131.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205011107131.png"></p>
<h2 id="simsiam" tabindex="-1"><a class="header-anchor" href="#simsiam" aria-hidden="true">#</a> <strong>SimSiam</strong></h2>
<blockquote>
<p>Chen, Xinlei, and Kaiming He. &quot;Exploring simple siamese representation learning.&quot; Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.</p>
</blockquote>
<p>BYOL出来之后，就有很多分析型的工作在分析对比学习的成功，因为很多对比学习的工作，好像都是被很多改进堆起来的这个性能，比如projection head，动量编码器等等。这样其实不太好，因为我们不知道这么多点到底每个点带来了哪些贡献。</p>
<p>论文证明了即使不引入负样本，不需要大的batch size，不需要使用动量编码器，SimSiam也能取得很好的结果。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205014933331.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205014933331.png"></p>
<p>模型的损失函数为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015204179.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015204179.png"></p>
<p>作者证明一个非常重要的、能让模型work的操作是stop-gradient操作，这样，上面的损失变成了：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015252776.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015252776.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015312877.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015312877.png"></p>
<ul>
<li>证明stop-grad的重要性</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015331376.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015331376.png"></p>
<ul>
<li>证明pred的重要性</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015556582.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015556582.png"></p>
<ul>
<li>batch size 不重要</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015626657.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015626657.png"></p>
<ul>
<li>证明在projection（ResNet内）网络中的隐层和输出层，在predictor网络中的隐层加BN效果最好</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015704736.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205015704736.png"></p>
<ul>
<li>。。。</li>
</ul>
<p>作者认为SimSiam类似于EM（Expectation-Maximization）算法，它隐式地和两组参数相关联，并通过一种迭代的方式分别优化这两组参数。stop-gradient存在的作用就是引入第二组可优化参数。</p>
<p>考虑如下的损失函数形式：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205102541046.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205102541046.png"></p>
<p>优化目标：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205102612093.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205102612093.png"></p>
<p>theta和eta关联，这与k-means相似，k-means也有两个需要优化的参数：一个是聚类中心，类似于优化目标中的theta，一个是“每个样本属于哪个聚类”，这类似于eta，优化两个参数迭代进行，即交替地计算每个类别的聚类中心，随后计算每个样本的聚类所属情况，直到训练稳定。上面的优化目标也类似，迭代进行以下两步：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103046066.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103046066.png"></p>
<p>上面的式子就是使用梯度回传、更新，下面的式子就使用如下的重新计算、赋值更新操作：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103148988.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103148988.png"></p>
<p>作者认为SimSiam实际上模拟了上面的交替更新的过程，只不过eta的采样只做一次：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103342700.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103342700.png"></p>
<p>带入得到：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103407808.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103407808.png"></p>
<p>上面的公式其实就是SimSiam的结构加上stop-gradient操作。</p>
<p>作者接下来阐述了引入predictor h的目的，根据定义，期望最小化：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103624349.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103624349.png"></p>
<p>最优的h需要满足：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103648335.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205103648335.png"></p>
<p>因为SimSam只采样一次，所以期望被忽略了，而引入h就可能通过神经网络的拟合能力去学习“预测期望”。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205104132790.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205104132790.png"></p>
<h1 id="应用" tabindex="-1"><a class="header-anchor" href="#应用" aria-hidden="true">#</a> <strong>应用</strong></h1>
<blockquote>
<p>Kumar, Sateesh, et al. &quot;Unsupervised action segmentation by joint representation learning and online clustering.&quot; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.</p>
</blockquote>
<p>论文提出基于对比学习的无监督视频动作分割方法。该方法对 SwAV 算法进行改进，且不需要图像增广，利用 “视频数据的相邻帧为同类样本”这一假设，将相邻帧 的图像作为正样本对进行对比学习，完成视频动作分割任务。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125618509.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125618509.png"></p>
<p>以往的无监督动作分割方法通常将表征学习和聚类按顺序进行，这阻止了聚类步骤的反馈回到表征学习。此外，它们需要先存储整个数据集的特征，然后再以离线方式对它们进行聚类，从而导致内存使用效率低下。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125810430.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125810430.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125949056.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205125949056.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130003566.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130003566.png"></p>
<p>为了进一步利用视频中的时间信息，该文添加另一个时间一致性损失。它学习一个遵循时间一致性约束的嵌入空间，其中时间距离接近的帧应该映射到附近的点，时间距离遥远的帧应该映射到遥远的点。</p>
<p>将每个视频分为N个有序帧的子集，对于每个子集，lambda时间窗口内采样一个正样本，不在窗口内的为负样本。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130124440.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130124440.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130350709.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130350709.png"></p>
<p>伪标签Q使用Sinkhorn- Knopp算法求解：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130459130.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130459130.png"></p>
<p>利用视频数据中的时间线索进行无监督的动作分割。因此这篇文章中加入了一个时间正则化项。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130857204.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130857204.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130846018.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/02/05/image-20230205130846018.png"></p>
</div></template>


