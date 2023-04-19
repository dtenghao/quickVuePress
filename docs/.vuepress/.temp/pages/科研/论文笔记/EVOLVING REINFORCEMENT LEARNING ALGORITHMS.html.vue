<template><div><h1 id="evolving-reinforcement-learning-algorithms" tabindex="-1"><a class="header-anchor" href="#evolving-reinforcement-learning-algorithms" aria-hidden="true">#</a> EVOLVING REINFORCEMENT LEARNING ALGORITHMS</h1>
<p>作者: John D. Co-Reyes</p>
<h1 id="摘要" tabindex="-1"><a class="header-anchor" href="#摘要" aria-hidden="true">#</a> <strong>摘要</strong></h1>
<p>本文提出使用<code v-pre>元学习</code>来学习<code v-pre>强化学习算法</code>的方法，通过搜索计算图的空间，计算出基于价值的无模型 RL agent的损失函数来进行优化。所学习到的函数具有很强的泛化性。函数既可以从头开始学习，也可以在已知算法（如DQN）的基础上进行。从新开始学习，算法重新发现了时序差分（TD）算法，从DQN开始，算法学习到了两种表现非常好的函数。</p>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> <strong>介绍</strong></h1>
<p>对于深度强化学习来说，设计一个对于各种环境具有很强泛化性的损失函数需要大量的人工努力，如果让算法自己学会设计，有助于减轻这种负担，还可能产生比研究人员手动设计更好的算法。</p>
<p>论文把上述想法用两层循环来表达：</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>
for i = 1...M    tournament选择，选择表现最优的损失函数，变异进化    for j = 1...N        训练筛选出来的函数，使得loss尽可能地小    endend
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p>算法可以不依赖任何已知损失函数，从头开始学习，但将人类现有的知识编码到学习过程中可以加快优化速度，也可以使学到的算法更容易解释。通过比较从头开始和从现有算法中进化，发现虽然从头开始可以学习现有的算法，但从现有的知识开始会学习到新的RL算法，这些算法可以超越初始程序，文章举例了两种新的RL算法，它们在训练和测试环境中的采样效率和最终性能都优于现有算法。</p>
<h1 id="方法" tabindex="-1"><a class="header-anchor" href="#方法" aria-hidden="true">#</a> <strong>方法</strong></h1>
<h2 id="评价" tabindex="-1"><a class="header-anchor" href="#评价" aria-hidden="true">#</a> <strong>评价</strong></h2>
<p>首先是内循环是如何评估一个新学习到的RL算法的：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/19/image-20221119235755219.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/19/image-20221119235755219.png"></p>
<p>这里是跟nndl书中的带经验回放的深度Q网络算法14.5一致。这里对reward进行了归一化，原因是要在不同的环境env中比较，reward的范围可能会有很大的不同，因此对于每个环境的reward进行了归一化。</p>
<h2 id="变异" tabindex="-1"><a class="header-anchor" href="#变异" aria-hidden="true">#</a> <strong>变异</strong></h2>
<p>函数该如何变异，对函数L的搜索程序应该有足够的表现力，以表示现有的函数，同时能够学习新的函数，这些算法可以在广泛的环境中获得良好的泛化性能。对于DQN损失函数：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120001015344.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120001015344.png"></p>
<p>表示为一个计算图或有向无环图（DAG），其节点具有类型化的输入和输出。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120001108009.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120001108009.png"></p>
<p>输入节点：蓝色；表示程序的输入，包括来自转移的元素（st, at, st+1, rt）和常数，如折扣系数γ。</p>
<p>参数节点：灰色；是神经网络的权重</p>
<p>运算节点：橙色；计算来自父结点的输入的输出</p>
<p>输出节点：绿色；</p>
<h2 id="搜索" tabindex="-1"><a class="header-anchor" href="#搜索" aria-hidden="true">#</a> <strong>搜索</strong></h2>
<p>保持一个初始算法集合P，每个周期随机挑选一个T&lt;P的的算法集合T，并选择T中最好的算法作为父算法。父算法被变异为子算法,被添加到集合P中，而P中最古老的算法被移除。使用单一类型的变异，首先选择图中的哪个节点进行变异，然后用一个随机的运算节点代替它，其输入从所有可能的输入中均匀抽取。</p>
<p>对于每个变异生成的算法，如果都进行完整的内循环评估，会占用大量的时间，加快搜索速度和避免无谓的计算是使问题更容易解决的需要，共有四种方式：</p>
<ul>
<li><strong>等价性检测</strong>：在进入内循环前，检查与之前评估的算法在功能上是否等同。这个检查是通过对随机输入的10个值的程序的拼接输出进行hashing来完成的。如果一个变异的算法在功能上等同于一个较早的算法，我们仍然将其加入到集合中，但使用较早集合保存的分数。</li>
<li><strong>早期障碍</strong>：希望表现不佳的程序能够提前终止，这样我们就可以避免不需要的计算。使用简单的环境CartPole作为障碍环境，如果算法在CartPole上表现不佳，表现&lt;阈值a，则直接不进入内循环评估了。</li>
<li><strong>程序检查</strong>：变异的算法是无效的，就直接跳过，比如损失函数需要是一个标量值，检查出函数的输出类型不是一个浮点。</li>
<li><strong>从现有方法开始变异</strong>：从一个更好的起点开始，可以用更少的时间收敛到一个合理的算法，比如用DQN的损失函数初始化计算图，因此前7个节点代表标准的DQN损失，而其余的节点是随机初始化的。</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004148928.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004148928.png"></p>
<p>算法示意图：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/19/谷歌实现2种新的强化学习算法，“比肩”DQN，泛化性能更佳！.gif" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/19/%E8%B0%B7%E6%AD%8C%E5%AE%9E%E7%8E%B02%E7%A7%8D%E6%96%B0%E7%9A%84%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%EF%BC%8C%E2%80%9C%E6%AF%94%E8%82%A9%E2%80%9DDQN%EF%BC%8C%E6%B3%9B%E5%8C%96%E6%80%A7%E8%83%BD%E6%9B%B4%E4%BD%B3%EF%BC%81.gif"></p>
<h1 id="结果分析" tabindex="-1"><a class="header-anchor" href="#结果分析" aria-hidden="true">#</a> <strong>结果分析</strong></h1>
<p>使用了CartPole、Acrobat、MountainCar、LunarLander四种环境和来自MiniGrid的十二个环境。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004404893.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004404893.png"></p>
<p>这些环境在计算上非常的快，也覆盖到了多样的情况。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004706286.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120004706286.png"></p>
<ul>
<li>训练使用的环境越多，表现越好</li>
<li>从现有算法开始比从零开始表现更好</li>
<li>单一环境CartPole，从头开始，学习到的是简化版的DQN损失——没有衰减参数</li>
<li>两个环境CartPole和LunarLander，从头开始，学习到了DQN损失。</li>
</ul>
<hr>
<p>文章学习到了两个有趣的损失函数：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005119477.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005119477.png"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005126129.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005126129.png"></p>
<p>对于Clipped的直观感知，如果Q值很大，损失函数将作用于Q值，而不是δ</p>
<p>2损失（DQN）。Q=δ+Y_t,对于Q&gt;δ</p>
<p>2+Y_t，就意味着</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005324857.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005324857.png"></p>
<p>， δ非常的小，Q接近于目标Q，那么只需要最小化Q即可。</p>
<p>当Clipped训练开始时强烈低估Q值时，因此DQN损失函数会发挥作用，当随着训练进行，高估Q值时，正则化Q值会起作用。</p>
<hr>
<p>第二个损失函数reg：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005716554.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005716554.png"></p>
<p>直接用一个始终有效的加权项来规范Q值。我们注意到，这两个损失函数都修改了原始的DQN损失函数，将Q值正则化为较低的值。虽然DQNReg相当简单，但它在所有的训练和测试环境中，表现都特别好。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005821170.png" alt="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/11/20/image-20221120005821170.png"></p>
<hr>
<p>最近提出的一些RL算法：保守Q-learning（CQL）通过用一个简单的Q值正则化项增加标准的贝尔曼误差目标来学习一个保守的Q函数，M-DQN修改了DQN，在即时奖励中加入了缩放的对数策略（使用softmax Q-values），这两种方法都可以被看作是使基于价值的策略正规化的方法。这与论文自动学习到的算法改进方向类似，表明方法可以自动找到目前正在人工探索的有用结构，并且可以用来为研究人员提出新的探索领域。</p>
</div></template>


