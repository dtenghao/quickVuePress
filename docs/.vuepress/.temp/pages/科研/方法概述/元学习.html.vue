<template><div><h1 id="元学习" tabindex="-1"><a class="header-anchor" href="#元学习" aria-hidden="true">#</a> 元学习</h1>
<p>Time: April 10, 2023 8:30 AM</p>
<h1 id="概述" tabindex="-1"><a class="header-anchor" href="#概述" aria-hidden="true">#</a> <strong>概述</strong></h1>
<p>元学习的目的是从已有任务中学习一种学习方法或元知识，可以加速新任务的学习</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113221118285.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113221118285.png"></p>
<p>从熟悉的机器学习出发，机器学习就是找到一个函数f，传入输入后经过一系列运算得到输出，比如对于猫狗分类任务，我们需要找到一个函数，使得输入猫的图片，可以输出“cat”。而元学习，是学习到一个函数F，它可以找到解决任务的函数f，函数F也被称为学习算法，输入需要解决任务的训练数据，可以得到解决任务的函数f。也就是说，机器学习是人为手动的找到解决问题的函数，而元学习，是人为手动的找到一个学习算法F，由它来找函数f，这样以后遇到一个新的类似任务，就不需要人为手动的去寻找函数f了。</p>
<p>更细节的，对于解决机器学习问题，主要分为三步：</p>
<ol>
<li>确定未知函数f</li>
<li>定义损失函数</li>
<li>定义优化算法</li>
</ol>
<p>对于元学习，也是大致如此</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113215424732.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113215424732.png"></p>
<p>对于学习算法，可以选择学习函数f的网络结构，初始化参数值，学习率（优化算法）</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113233421221.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113233421221.png"></p>
<p>损失函数上，机器学习是通过训练数据计算损失值，元学习是“学习算法”F根据训练数据得到函数f，然后函数f使用测试数据来计算损失。由于元学习的训练阶段通常会有很多个任务，因此损失也是多个任务的损失相加之和。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113222305380.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113222305380.png"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113233538604.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113233538604.png"></p>
<p>因此元学习的大致细节如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113220942115.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113220942115.png"></p>
<p>首先我们有大量的训练任务，比如苹果-橙子分类任务或者自行车-汽车分类任务，然后用这些任务来学习“学习算法”F，直到损失函数最小化。</p>
<p>有了好的“学习算法”F，它可以比较好的找到解决这类任务比较好的网络结构，初始化参数值，学习率等，再将我们真正关心的测试任务的训练数据输入到“学习算法”F中去train，生成函数f，再将测试数据输入到函数f来测试函数f的表现。</p>
<p>论文中常常将任务中的train data称为support set，test data成为query set。</p>
<p>最后可以从下面的示意图对比元学习和机器学习间的区别</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113221823480.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/13/image-20230113221823480.png"></p>
<p>可以看到机器学习的训练过程训练数据和测试数据都是属于同一个任务，这个任务就是我们要解决的任务，比如始终是猫狗分类任务。</p>
<p>而对于元学习，训练数据和测试数据属于不同的任务，相互没有联系的任务，比如训练任务可以是自行车-汽车分类任务和苹果-橙子分类任务，这些任务我们并不关心，而我们真正关心、真正待解决的任务是猫狗分类任务</p>
<hr>
<p>机器学习的很多方法，也可以应用在元学习上，比如在训练任务上过拟合，可以提供更多的训练任务来提高表现，也可以像样本增强一样使用任务增强；学习“学习算法”的过程往往也需要调整超参数，因此机器学习的调参技巧同样可以应用在元学习上，但相比于机器学习遇到一个任务就要调整一次参数，元学习只需要调整一次参数，找到一个好的“学习算法”后，它可以用到任何一个新的任务上，再也不需要调参数了，一劳永逸。</p>
<h1 id="参数初始值" tabindex="-1"><a class="header-anchor" href="#参数初始值" aria-hidden="true">#</a> <strong>参数初始值</strong></h1>
<p>设想是训练<strong>一组初始化参数</strong>，模型面对一个新任务，通过初始化参数，仅用少量数据就能实现快速收敛的效果。为了达到这一目的，模型需要大量的<strong>先验知识</strong>来不停修正初始化参数，使其能够适应不同种类的数据。</p>
<h2 id="maml" tabindex="-1"><a class="header-anchor" href="#maml" aria-hidden="true">#</a> <strong>MAML</strong></h2>
<blockquote>
<p>Chelsea Finn, Pieter Abbeel, and Sergey Levine, &quot;Model- Agnostic Meta-Learning for Fast Adaptation of Deep Networks&quot;, ICML, 2017</p>
</blockquote>
<p>MAML关注的不是在某一个任务上参数达到最优，而是综合所有的任务，找到一个合理的初始化值，使得参数以后在面对某个特定的新任务时，能够经过少量的迭代，甚至是单步迭代，就可以达到一个非常好的性能。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114170121051.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114170121051.png"></p>
<p>算法的流程如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114170524688.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114170524688.png"></p>
<p>实际中进行梯度下降时，会需要计算二阶微分，很花费时间，论文中将二阶微分舍去，这也会带来一些稳定性的问题。在论文How to train your maml中对maml进行了一些改进。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114171643765.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114171643765.png"></p>
<p>一般MAML只会更新一次参数，因为任务数较多，更新一次需要耗费的时间长；像few-shot learning数据量较少，多次更新容易过拟合。</p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/28/image-20230114161927782.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/03/28/image-20230114161927782.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM5MjQ1NA==,size_16,color_FFFFFF,t_70.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM5MjQ1NA==,size_16,color_FFFFFF,t_70.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114162123279.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114162123279.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114171124716.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114171124716.png"></p>
<h2 id="reptile" tabindex="-1"><a class="header-anchor" href="#reptile" aria-hidden="true">#</a> <strong>Reptile</strong></h2>
<blockquote>
<p>Alex Nichol, Joshua Achiam, John Schulman, On First- Order Meta-Learning Algorithms, arXiv, 2018</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114190744245.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114190744245.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114190830462.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114190830462.png"></p>
<h1 id="网络结构" tabindex="-1"><a class="header-anchor" href="#网络结构" aria-hidden="true">#</a> <strong>网络结构</strong></h1>
<h2 id="基于强化学习" tabindex="-1"><a class="header-anchor" href="#基于强化学习" aria-hidden="true">#</a> <strong>基于强化学习</strong></h2>
<blockquote>
<p>Barret Zoph, et al, Neural Architecture Search with Reinforcement Learning, ICLR 2017</p>
</blockquote>
<p>作者用一个controller RNN(作为父网络)来预测一个子网络(child network)，在训练集上训练子网络，在验证集上获得子网络的accuracy，再利用accuracy更新controller的参数，如此循环，直到获得一个较好的子网络结构。而由于用RNN作为controller，此方法能较为灵活地在变长的网络结构空间中进行搜索</p>
<p>由于accuracy对于controller的参数不直接可导，作者提出利用强化学习的方法，根据controller生成多个不同子网络的样本，将这些样本的准确率作为reward，计算controller参数的policy gradient，并由此更新参数。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114223244584.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114223244584.png"></p>
<p>更具体的controller（RNN）的设计如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114223424929.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114223424929.png"></p>
<p>论文中RNN使用的是LSTM模型，只是生成卷积层的参数，注意这里生成的参数并不是确定的值，而是一个概率分布。比如第m层的Filter Height参数，对应[3,5,7,9]的概率可能是[0.1, 0.5, 0.2, 0.2]。controller将会根据这些概率分布采样出多个子网络，将这些子网络训练后得到的accuracy当作reward，计算policy gradient，以此来更新controller的参数。</p>
<p>将controller生成的一系列cnn模型参数作为动作a，controller的模型参数作为状态theta。那么当前controller得到的期望可以表示成</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225007440.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225007440.png"></p>
<p>根据<a href="https://link.zhihu.com/?target=https%3A//spinningup.openai.com/en/latest/spinningup/rl_intro3.html%23deriving-the-simplest-policy-gradient" target="_blank" rel="noopener noreferrer">REINFORCE rule<ExternalLinkIcon/></a>计算policy gradient：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225055968.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225055968.png"></p>
<blockquote>
<p>推导过程</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225155697.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225155697.png"></p>
</blockquote>
<p>上式又可近似为</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225322187.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225322187.png"></p>
<p>其中 m 为controller在一个batch中采样的子网络个数， T 为controller预测的模型参数个数。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225525086.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114225525086.png"></p>
<h2 id="基于进化算法" tabindex="-1"><a class="header-anchor" href="#基于进化算法" aria-hidden="true">#</a> <strong>基于进化算法</strong></h2>
<blockquote>
<p>Esteban Real, et al, Large-Scale Evolution of Image Classifiers, ICML 2017</p>
</blockquote>
<p>文章采用遗传算法进行网络的搜索。首先，作者进化出一个神经网络模型的<strong>种群</strong>，这个种群会包含很多不同的网络模型，其中每个模型即为一个<strong>个体</strong>。这个模型被训练后在验证集上的准确率为此个体的<strong>适应度评估</strong>。在每一个进化步中，<strong>worker</strong>（即计算机）从种群中随机选择两个个体，然后计算并比较其适应度。适应度较差的个体从种群中被移除，较好的个体留下来作为<strong>亲本</strong>进行下一步的<strong>繁殖</strong>。繁殖过程中，worker复制这个亲本，然后对其进行<strong>变异</strong>，即对其进行结构上的修改，比如神经元数量等，修改后的模型称为<strong>后代</strong>。这个后代被训练然后得到在验证集上的准确率，最后被放回到种群里。</p>
<p>这种方式的思路和之前看过的EVOLVING REINFORCEMENT LEARNING ALGORITHMS非常的相似，总体思路就是生成多个模型，随机挑选出几个模型，将表现最好的模型进行修改，再放回到模型池中，多次循环下来就能找到不错的网络结构。</p>
<h2 id="可微分" tabindex="-1"><a class="header-anchor" href="#可微分" aria-hidden="true">#</a> <strong>可微分</strong></h2>
<p>前面两种做法都不是直接对Network Architecture 的loss进行微分的。</p>
<blockquote>
<p>Hanxiao Liu, et al., DARTS: Differentiable Architecture Search ICLR, 2019</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115115722158.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115115722158.png"></p>
<h1 id="学习率" tabindex="-1"><a class="header-anchor" href="#学习率" aria-hidden="true">#</a> <strong>学习率</strong></h1>
<blockquote>
<p>Marcin Andrychowicz, et al., Learning to learn by gradient descent by gradient descent, NIPS, 2016</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114235906208.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/14/image-20230114235906208.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000122237.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000122237.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000308101.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000308101.png"></p>
<p>这里的forget gate类似于weight decay。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000523282.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115000523282.png"></p>
<p>总的流程如下：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115001341809.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115001341809.png"></p>
<p>这里需要注意传统的LSTM的信息C跟输入是没有关系的，而在这个问题中，权重会参与损失的计算，所以在反向传播时会计算这条路径的梯度，非常的麻烦，因此论文计算梯度时将这条路径删掉了，还是像LSTM一样，直接训练。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115002116336.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115002116336.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115002133974.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115002133974.png"></p>
<h1 id="应用" tabindex="-1"><a class="header-anchor" href="#应用" aria-hidden="true">#</a> <strong>应用</strong></h1>
<p>人类非常擅长通过极少量的样本识别一类物体，比如小孩子只需要书中的一些图片就可以认识什么是“斑马”，什么是“犀牛”。在这种人类的快速学习能力的启发下，我们希望模型在大量类别中学会通过少量数据正确地分类后，对于新的类别，我们也只需要少量的样本就能快速学习，这就是Few-shot learning 要解决的问题。</p>
<p>训练数据有多个类别，每个类别下有多个样本。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115091727201.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115091727201.png"></p>
<p>利用这些数据生成数据量相当的正样本和负样本</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115092139005.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115092139005.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115092306827.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115092306827.png"></p>
<p>希望学习到一个网络f，它可以学习到图片的一种embedding，然后比较两者的embedding，判断是否是同一类物体。</p>
<p>学习的内容可以用到前面提到的网络结构，初始化参数，学习率等。</p>
<p>整个网络也被称为孪生网络。</p>
<hr>
<p>预测是给出了6个类别的动物，每个类别只有一个样本，也就是six-way one-shot</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115101337098.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115101337098.png"></p>
<p>将Support Set中的样本分别与Query输入到网络中，判断与哪种类别最相近。</p>
<p>如果一个类别有多个样本，可以将类别的embedding表示成所有样本的均值</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115104113439.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115104113439.png"></p>
<hr>
<p>实际使用时，可以提前计算好Support Set中类别的embedding，将它们排列好组成矩阵W，以后来一个新的query，就可以快速的对类别进行判断。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115102635082.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115102635082.png"></p>
<p>近期的论文显示，对模型进行fineTuning可以使表现提升好几个百分点</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115103210766.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115103210766.png"></p>
<blockquote>
<p>Dhillon, Chaudhari, Ravichandran, &amp; Soatto. A baseline for few-shot image classification. In ICLR 2020.</p>
</blockquote>
<ul>
<li>
<p>将权重W初始化为M，b初始化为0</p>
</li>
<li>
<p>使用熵正则化（Entropy Regularization）</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115103729330.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115103729330.png"></p>
</li>
<li>
<p>对embedding进行归一化</p>
</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115104150944.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/01/15/image-20230115104150944.png"></p>
<h1 id="与迁移学习的区别" tabindex="-1"><a class="header-anchor" href="#与迁移学习的区别" aria-hidden="true">#</a> <strong>与迁移学习的区别</strong></h1>
<p>两者都是讨论从旧任务中学习如何高效地学会新任务</p>
<ul>
<li>Meta-learning 更侧重学习常规学习任务中需要人为调的<strong>超参数</strong>，比如模型结构，损失函数，优化方式等。而Transfer Learning更侧重学习任务中需要学习的<strong>常规参数</strong>，比如神经网络的权重等。</li>
<li>学习方式上，Meta-learning更侧重于多任务的概念，即模型表现在多个任务间保持一种均衡的状态，使得模型遇到新任务时，具有较强的鲁棒性。</li>
<li>Meta-learing更侧重于如何从头开始学一个模型，而非在一个pretrain的模型上finetune；而Transfer Learning 则侧重先pretrain再finetune这样的训练模式。</li>
</ul>
</div></template>


