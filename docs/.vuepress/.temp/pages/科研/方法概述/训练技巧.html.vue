<template><div><h1 id="训练技巧" tabindex="-1"><a class="header-anchor" href="#训练技巧" aria-hidden="true">#</a> 训练技巧</h1>
<p>Time: March 28, 2023 11:33 AM</p>
<h1 id="学习率" tabindex="-1"><a class="header-anchor" href="#学习率" aria-hidden="true">#</a> 学习率</h1>
<ul>
<li>使用周期性学习策略，如one cycle学习率策略（线性递增+线性递减+退火阶段，有规律的改变学习率有助于更快越过鞍点），pytorch中也已经有了相应的实现torch.optim.lr_scheduler.OneCycleLR()</li>
<li>使用权重衰减而不是L2正则化的AdamW在训练时间与出现错误的情况都优于Adam</li>
</ul>
<h1 id="batchsize" tabindex="-1"><a class="header-anchor" href="#batchsize" aria-hidden="true">#</a> BatchSize</h1>
<ul>
<li>更大的BatchSize可以使得训练速度更快，但是也会导致训练效果比小的BatchSize更差。</li>
<li>调整了BatchSize还需要同步学习率等超参，一个经验之谈是BatchSize加倍时，学习率也需要加倍</li>
</ul>
<h1 id="dataloader" tabindex="-1"><a class="header-anchor" href="#dataloader" aria-hidden="true">#</a> DataLoader</h1>
<ul>
<li>num_worker是开启子进程用来加载数据到内存，设置过大也会使内存开销变大，加重CPU负担。一个常见经验是设置为可用GPU的4倍</li>
<li>将pin_memory设置为True，可以把数据存储在固定（pinned）内存中，加速数据从CPU内存传输到GPU内存的过程</li>
</ul>
<h1 id="自动混合精度训练" tabindex="-1"><a class="header-anchor" href="#自动混合精度训练" aria-hidden="true">#</a> 自动混合精度训练</h1>
<p>在某些操作时，使用半精度FP16，而不是一味的使用FP32，AMP会自动决定使用哪种格式，在不损失精度的前提下达到更快的训练速度与占用更小内存的目的。</p>
<div class="language-python line-numbers-mode" data-ext="py"><pre v-pre class="language-python"><code><span class="token keyword">from</span> torch<span class="token punctuation">.</span>cuda<span class="token punctuation">.</span>amp <span class="token keyword">import</span> GradScaler

<span class="token comment"># 创建一个GradScaler对象</span>
scaler <span class="token operator">=</span> GradScaler<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token keyword">for</span> epoch <span class="token keyword">in</span> <span class="token builtin">range</span><span class="token punctuation">(</span><span class="token number">10</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    optimizer<span class="token punctuation">.</span>zero_grad<span class="token punctuation">(</span><span class="token punctuation">)</span>

    <span class="token comment"># 使用autocast上下文管理器自动选择精度</span>
    <span class="token keyword">with</span> autocast<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        outputs <span class="token operator">=</span> model<span class="token punctuation">(</span>data<span class="token punctuation">)</span>
        loss <span class="token operator">=</span> criterion<span class="token punctuation">(</span>outputs<span class="token punctuation">,</span> labels<span class="token punctuation">)</span>

    <span class="token comment"># 使用GradScaler来缩放梯度以防止梯度下溢</span>
    scaler<span class="token punctuation">.</span>scale<span class="token punctuation">(</span>loss<span class="token punctuation">)</span><span class="token punctuation">.</span>backward<span class="token punctuation">(</span><span class="token punctuation">)</span>
    scaler<span class="token punctuation">.</span>step<span class="token punctuation">(</span>optimizer<span class="token punctuation">)</span>
    scaler<span class="token punctuation">.</span>update<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="benchmark" tabindex="-1"><a class="header-anchor" href="#benchmark" aria-hidden="true">#</a> Benchmark</h1>
<p>在输入数据大小固定，显存资源充足时，可将**<code v-pre>torch.backends.cudnn.benchmark</code><strong>设置为</strong><code v-pre>True</code>**</p>
<div class="language-python line-numbers-mode" data-ext="py"><pre v-pre class="language-python"><code><span class="token comment"># 确保使用的是CUDA设备且已安装CuDNN</span>
<span class="token keyword">assert</span> torch<span class="token punctuation">.</span>cuda<span class="token punctuation">.</span>is_available<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">and</span> torch<span class="token punctuation">.</span>backends<span class="token punctuation">.</span>cudnn<span class="token punctuation">.</span>enabled
<span class="token comment"># 启用CuDNN基准测试</span>
torch<span class="token punctuation">.</span>backends<span class="token punctuation">.</span>cudnn<span class="token punctuation">.</span>benchmark <span class="token operator">=</span> <span class="token boolean">True</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="分布式训练" tabindex="-1"><a class="header-anchor" href="#分布式训练" aria-hidden="true">#</a> 分布式训练</h1>
<p>推荐使用**<code v-pre>DistributedDataParallel</code><strong>（DDP）而不是</strong><code v-pre>DataParallel</code>**（DP）</p>
<ol>
<li><strong>性能优势</strong>：与**<code v-pre>DataParallel</code><strong>相比，</strong><code v-pre>DistributedDataParallel</code><strong>在多GPU训练中具有更好的性能。</strong><code v-pre>DataParallel</code><strong>在多GPU之间复制模型和梯度时，会在主设备上产生瓶颈。而</strong><code v-pre>DistributedDataParallel</code>**使用多进程和异步通信机制，可以更高效地在多个设备之间分发任务和同步梯度。</li>
<li><strong>灵活性</strong>：**<code v-pre>DistributedDataParallel</code><strong>支持不同类型的分布式训练设置，包括单节点多卡、多节点多卡等。这使得</strong><code v-pre>DistributedDataParallel</code>**适用于更广泛的场景。</li>
<li><strong>扩展性</strong>：**<code v-pre>DistributedDataParallel</code>**具有很好的扩展性。随着GPU数量的增加，训练速度和吞吐量也会相应提高。这对于大型模型和数据集的训练尤为重要。</li>
<li><strong>容错性</strong>：**<code v-pre>DistributedDataParallel</code>**提供了一定程度的容错性。当某个训练进程因某种原因失败时，其他进程可以继续执行，训练不会被中断。</li>
</ol>
<div class="language-python line-numbers-mode" data-ext="py"><pre v-pre class="language-python"><code><span class="token comment"># 初始化分布式训练</span>
dist<span class="token punctuation">.</span>init_process_group<span class="token punctuation">(</span>backend<span class="token operator">=</span><span class="token string">"nccl"</span><span class="token punctuation">,</span> init_method<span class="token operator">=</span><span class="token string">"env://"</span><span class="token punctuation">)</span>
rank <span class="token operator">=</span> dist<span class="token punctuation">.</span>get_rank<span class="token punctuation">(</span><span class="token punctuation">)</span>
torch<span class="token punctuation">.</span>manual_seed<span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span>

device <span class="token operator">=</span> torch<span class="token punctuation">.</span>device<span class="token punctuation">(</span><span class="token string-interpolation"><span class="token string">f"cuda:</span><span class="token interpolation"><span class="token punctuation">{</span>rank<span class="token punctuation">}</span></span><span class="token string">"</span></span><span class="token punctuation">)</span>
model <span class="token operator">=</span> SimpleModel<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>to<span class="token punctuation">(</span>device<span class="token punctuation">)</span>
ddp_model <span class="token operator">=</span> DDP<span class="token punctuation">(</span>model<span class="token punctuation">,</span> device_ids<span class="token operator">=</span><span class="token punctuation">[</span>device<span class="token punctuation">]</span><span class="token punctuation">,</span> output_device<span class="token operator">=</span>device<span class="token punctuation">)</span>

<span class="token comment"># 使用DistributedSampler进行数据分发</span>
train_sampler <span class="token operator">=</span> DistributedSampler<span class="token punctuation">(</span>trainset<span class="token punctuation">)</span>
trainloader <span class="token operator">=</span> torch<span class="token punctuation">.</span>utils<span class="token punctuation">.</span>data<span class="token punctuation">.</span>DataLoader<span class="token punctuation">(</span>trainset<span class="token punctuation">,</span> batch_size<span class="token operator">=</span><span class="token number">100</span><span class="token punctuation">,</span> sampler<span class="token operator">=</span>train_sampler<span class="token punctuation">,</span> num_workers<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="梯度累加" tabindex="-1"><a class="header-anchor" href="#梯度累加" aria-hidden="true">#</a> 梯度累加</h1>
<p>将一个大batch分为多个小batch，多次backward()，当读完了一个大batch之后再进行梯度更新，该方法主要是为了规避GPU内存限制而设计。</p>
<h1 id="bn层" tabindex="-1"><a class="header-anchor" href="#bn层" aria-hidden="true">#</a> BN层</h1>
<p>如果在conv2d后紧跟BN层，需要将conv2d中的bias设置为false</p>
<h1 id="小技巧" tabindex="-1"><a class="header-anchor" href="#小技巧" aria-hidden="true">#</a> 小技巧</h1>
<ul>
<li>不要频繁使用<code v-pre>torch.cpu()</code>和<code v-pre>torch.cuda()</code>，在CPU和GPU间移动数据是非常昂贵的</li>
<li>将numpy数据转换为tensor时，使用<code v-pre>torch.as_tensor()</code>和<code v-pre>torch.from_numpy()</code>而不是<code v-pre>torch.tensor()</code>，因为他会执行复制数据的操作，效率低下</li>
</ul>
</div></template>


