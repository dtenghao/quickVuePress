<template><div><h1 id="adapters" tabindex="-1"><a class="header-anchor" href="#adapters" aria-hidden="true">#</a> Adapters</h1>
<p>Time: April 14, 2023 9:24 AM</p>
<blockquote>
<p><strong>Gao, Peng, et al. &quot;Clip-adapter: Better vision-language models with feature adapters.&quot; <em>arXiv preprint arXiv:2110.04544</em> (2021).</strong></p>
</blockquote>
<ul>
<li>在transformer中每个layers后面加一个Adapter（Houlsby et al., 2019）</li>
<li>将clip的zero-shot的模型权重和常规finetune（只finetune了image branch）的模型权重进行线性组合（Wortsman et al., 2021）</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled.png" alt="Untitled"></p>
<p>融合参数是可学习的</p>
<p><strong>实验设置：</strong></p>
<ul>
<li>训练在1，2，4，8，16shot，在整个测试集上测试（oxford_flowers101）</li>
<li>使用一块A100</li>
<li>batchsize为32</li>
<li>学习率为$1\times10^{-5}$（$1\times10^{-4}$）</li>
<li>隐藏层大小为256</li>
<li>prompt设置为a photo of a {CLASS}</li>
<li>visual encoder使用ResNet50，textual使用BERT</li>
</ul>
<p><strong>代码细节：</strong></p>
<ul>
<li>只对visual encoder或者textual encoder进行Adapter，二选一</li>
</ul>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token assign-left variable">CUDA_VISIBLE_DEVICES</span><span class="token operator">=</span><span class="token number">2</span> python main.py <span class="token parameter variable">--config</span> configs/oxford_flowers.yaml
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 1.png" alt="Untitled"></p>
<p>与论文结果差了2-3个点</p>
<blockquote>
<p><strong>Zhang, Renrui, et al. &quot;Tip-adapter: Training-free adaption of clip for few-shot classification.&quot; <em>Computer Vision–ECCV 2022: 17th European Conference, Tel Aviv, Israel, October 23–27, 2022, Proceedings, Part XXXV</em>. Cham: Springer Nature Switzerland, 2022.</strong></p>
</blockquote>
<p>过去的工作中，CoOp，CLIP-Adapter针对少量样本，对模型进行微调，实现性能的提升；Zero-shot CLIP，Linearprobe CLIP则不需要训练，也能达到很好的效果。</p>
<p>作者希望模型能利用到CLIP在Zero-Shot上的强大能力和Few-Shot上的优越性能。本文模型能够在不训练的情况下，表现与微调过的CoOp，CLIP-Adapter相当。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 2.png" alt="Untitled"></p>
<p>Cache Model，键值缓存存储了从Few-Shot训练集中提取的所有新知识，用于更新预训练CLIP中编码的先验知识。</p>
<p>$$
\varphi(x)=\exp (-\beta(1-x))
$$</p>
<p>$\beta$是超参数，用于控制相似度的趋势。exp保证相似度不为负。</p>
<p>最后再与CLIP的pre-train的知识进行结合，得到最终结果。前者自适应地总结来自Few-Shot训练数据集的信息，后者保留先验知识。</p>
<p>这两项由权值α平衡。根据经验，如果预训练的和下游的Few-Shot任务之间的domain差距很大，α被设置为大，因为需要从Few-Shot集中获得更多的知识，否则α被设置为小。</p>
<p>但Few-Shot的数量增加，TIP会逐渐落后于finetune模型。因此将Cache Keys作为可学习的参数，还可以显著的提升模型性能，而且它只需要20 epochs在ImageNet上，而CoOp和CLIP-Adapter需要200 epochs。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 3.png" alt="Untitled"></p>
<p><strong>实验设置：</strong></p>
<ul>
<li>使用1, 2, 4, 8, 16 few-shot</li>
<li>visual encoder使用ResNet50，text encoder使用transformer</li>
<li>batchSize为256（内存不够，设置为32）</li>
<li>学习率0.001</li>
<li>AdamW优化器</li>
<li>训练20个epoch</li>
<li>对图片进行10次数据增强，取平均特征</li>
</ul>
<p><strong>代码：</strong></p>
<p><a href="https://github.com/gaopengcuhk/Tip-Adapter" target="_blank" rel="noopener noreferrer">https://github.com/gaopengcuhk/Tip-Adapter<ExternalLinkIcon/></a></p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">git</span> clone https://github.com/gaopengcuhk/Tip-Adapter.git
<span class="token builtin class-name">cd</span> Tip-Adapter

conda create <span class="token parameter variable">-n</span> tip_adapter <span class="token assign-left variable">python</span><span class="token operator">=</span><span class="token number">3.7</span>
conda activate tip_adapter

pip <span class="token function">install</span> <span class="token parameter variable">-r</span> requirements.txt

<span class="token comment"># Install the according versions of torch and torchvision</span>
conda <span class="token function">install</span> pytorch torchvision
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>datasets文件夹是关于如何处理数据集，并返回处理好后的数据</p>
<p>config中存放着训练的基本设置，包括数据集的位置，backbone的选择，一些超参数的设置</p>
<p>在根目录创建一个data文件夹，将下载好的数据集放到文件夹中，对于ImageNet数据集，文件结构应该为：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>imagenet/
<span class="token operator">|</span>–– images/
<span class="token operator">|</span>   <span class="token operator">|</span>–– train/ <span class="token comment"># contains 1,000 folders like n01440764, n01443537, etc.</span>
<span class="token operator">|</span>   <span class="token operator">|</span>–– val/
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>将classnames.txt放置在imagenet/目录下。如果要使用其他数据集，可以参考：</p>
<p><a href="https://github.com/gaopengcuhk/Tip-Adapter/blob/main/DATASET.md" target="_blank" rel="noopener noreferrer">Tip-Adapter/DATASET.md at main · gaopengcuhk/Tip-Adapter<ExternalLinkIcon/></a></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 4.png" alt="Untitled"></p>
<p>运行代码时，对于ImageNet数据集，指定使用第一个GPU，配置文件为imagenet.yaml</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token assign-left variable">CUDA_VISIBLE_DEVICES</span><span class="token operator">=</span><span class="token number">0</span> python main_imagenet.py <span class="token parameter variable">--config</span> configs/imagenet.yaml
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其他十种数据集如oxford_flowers，多了个搜索最佳$\alpha$和$\beta$的步骤：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token assign-left variable">CUDA_VISIBLE_DEVICES</span><span class="token operator">=</span><span class="token number">2</span> python main.py <span class="token parameter variable">--config</span> configs/oxford_flowers.yaml
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><ul>
<li>
<p>加载CLIP模型</p>
</li>
<li>
<p>准备数据集（cache Model，训练集，测试集，验证集），16-shot，</p>
</li>
<li>
<p>计算text features</p>
</li>
<li>
<p>对cache Model数据集进行10次数据增强，特征取这10次的平均，构建cache Model</p>
</li>
<li>
<p>在验证集上搜索最佳$\alpha$和$\beta$</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 5.png" alt="Untitled"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 6.png" alt="Untitled"></p>
</li>
<li>
<p>在测试上评估模型</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 7.png" alt="Untitled"></p>
</li>
<li>
<p>使用训练集训练cache Model</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 8.png" alt="Untitled"></p>
</li>
<li>
<p>同样在验证集上搜索最佳$\alpha$和$\beta$，在测试集上评估模型</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 9.png" alt="Untitled"></p>
</li>
</ul>
<p>结果与论文基本一致</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 10.png" alt="Untitled"></p>
<blockquote>
<p>Pan, Junting, et al. &quot;ST-Adapter: Parameter-Efficient Image-to-Video Transfer Learning.&quot; <em>Advances in Neural Information Processing Systems</em> 35 (2022): 26462-26477.</p>
</blockquote>
<p>现有的方法都是关注相同模态中的迁移任务，预训练模型和下游任务是相同类型的任务，但是在某些特定模态（如视频理解）中受到限制，因为在这些领域，很难找到具有足够知识的强大预训练模型。</p>
<p>论文探讨了一种新颖的跨模态转移学习设置，叫作parameter-efficient image-to-video transfer learning，提出了一个新的Spatio-Temporal Adapter，这个模块可以使得一个没有时间知识的预训练图像模型能够以较小的（约8%）任务参数成本理解动态视频内容，与之前的工作相比，需要更新的参数减少了大约20倍。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 11.png" alt="Untitled"></p>
<p>在NLP中，Adapter通常结构如下：</p>
<p>$$
\text{Addapter}(\mathbf X)=\mathbf X+f(\mathbf X\mathbf W_{down})\mathbf W_{up}
$$</p>
<p>论文目标是将Adapter的成功从NLP推广到计算机视觉，特别是前面讨论的图像-视频迁移学习问题。</p>
<p>$$
\text{ST-Adapter}(\mathbf{X})=\mathbf{X}+f\Big(\text{DWConv3D}(\mathbf{X}\mathbf{W}<em>{down})\Big)\mathbf{W}</em>{up}
$$</p>
<p>因为channel维度小（128），因此depth-wise convolution可以非常的高效，与NLP Adapter差距不大。</p>
<p>之前在NLP领域已经讨论了Adapter应该放在哪里，一开始在每一个encoder中都部署了两个Adapter模块，一个跟在多头自注意力（MHSA）之后，另一个跟在前馈神经网络（FFN）之后。然而，后面有人提出仅在 FFN 之后添加一个Adapter模块就足够了。类似地，ST-Adapter（SpatioTemporal Adapter）也可以被集成在不同的位置。根据实验证据，作者发现在每个 Transformer 块的 MHSA 之前放置一个 ST-Adapter 就能达到不错的性能。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 12.png" alt="Untitled"></p>
<blockquote>
<p><strong>Chen, Zhe, et al. &quot;Vision transformer adapter for dense predictions.&quot; <em>arXiv preprint arXiv:2205.08534</em> (2022).</strong></p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 13.png" alt="Untitled"></p>
<p>与最近发展的将视觉特定归纳偏置引入模型的Swin等相比，普通ViT在密集预测上的性能较差，原因在于较弱的先验假设。为解决这一问题，作者提出了ViT-Adapter，使普通ViT能够在性能上与视觉特定的Transformer相媲美。</p>
<p><strong>为什么要在plain ViT上改</strong>：trnsformer对于输入没有assumption，无论是patch embedding、3D patch embedding还是token embedding，plain ViT都可以将他们作为输入，因此作者认为plain ViT在多模态训练上有非常好的优势。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 14.png" alt="Untitled"></p>
<ul>
<li>ViT将输入图片分为16$\times$ 16大小的多个patch，然后每个patch转化为D维embedding，经过L个encoder层。</li>
<li>首先将图片输入到空间先验模块，得到1/8，1/16，1/32分辨率，维度为D的三张特征图，再将三张特征图进行flattened和concatenated，设置N个interaction模块（通常N=4），将L个transformer encoders均匀地划分到N个interaction模块中。在interaction模块前后都进行空间先验特征的inject和extract层次特征，经过N个模块后，就可以获得高质量的多尺度特征，从而进行相应的下游任务。</li>
</ul>
<p><strong>SPATIAL PRIOR MODULE</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 15.png" alt="Untitled"></p>
<p>Stem的思想是从ResNet借鉴过来的，包含了三个3$\times$3，步长为2的卷积，channel都进行翻倍，以及一个最大池化层，最后通过一些1$\times$1的卷积，来使得最后的channel数为D，这样就得到了三个大小为1/8, 1/16和1/32的特征图，最后对它们进行flatten 和 concatenate，最后得到了</p>
<p>$$
\mathcal{F}_{\mathrm{sp}}^{1} \in \mathbb{R}^{\left(\frac{H W}{8^{2}}+\frac{H W}{16^{2}}+\frac{H W}{32^{2}}\right) \times D}
$$</p>
<p><strong>Spatial Feature Injector</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 16.png" alt="Untitled"></p>
<p>$$
\mathcal{F}_{\text{rit}}^i \in \mathbb{R}^{\frac{HW}{16^2}\times D}
$$</p>
<p>$$
\mathcal{F}_{\text{sp}}^{i}\in\mathbb{R}^{(\frac{HW}{8^{2}}+\frac{HW}{16^{2}}+\frac{HH}{32^{2}})\times D}
$$</p>
<p>$$
\hat{\mathcal{F}}^i_{\text{vit}}=\mathcal{F}^i_{\text{vit}}+\gamma^i\text{Attention}(\text{norm}(\mathcal{F}^i_\text{vit}),\text{norm}(\mathcal F^i_{\text{sp}}))
$$</p>
<p>$\gamma^i \in \mathbb{R}^D$是可学习向量，初始化为0，</p>
<p><strong>Multi-Scale Feature Extractor</strong></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 17.png" alt="Untitled"></p>
<p>将得到的$\hat{\mathcal{F}}^i_{\text{vit}}$经过ViT中第i个interaction模块后，得到$\mathcal{F}_{\text{vit}}^{i+1}$，然后继续使用cross-attention层和FFN来提取多尺度特征</p>
<p>$$
\begin{matrix}\mathcal{F}<em>{\text{sp}}^{i+1}=\hat{\mathcal{F}}</em>{\text{sp}}^i+\mathrm{FFN}(\text{norm}(\hat{\mathcal{F}}^i_\text{sp})),\ \hat{\mathcal{F}}<em>\text{sp}^i=\mathcal{F}</em>\text{sp}^{i}+\mathrm{Attention}(\text{norm}(\mathcal{F}^i_\text{sp}),\hom(\mathcal{F}^{i+1})),\end{matrix}
$$</p>
<p>作者构建了四种不同大小的ViT-Adapter，分别基于ViT-T, ViT-S, ViT-B, 和 ViT-L。这些模型的Adapters参数数量分别为2.5M（百万），5.8M，14.0M，和23.7M。</p>
<p>在方法中，默认使用可变形注意力（deformable attention，Zhu et al., 2020）作为稀疏注意力。其中，采样点的数量固定为4，不同模型的注意力头数分别设置为6, 6, 12, 和 16。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 18.png" alt="Untitled"></p>
<p><a href="https://github.com/czczup/ViT-Adapter" target="_blank" rel="noopener noreferrer">https://github.com/czczup/ViT-Adapter<ExternalLinkIcon/></a></p>
<p>实验设置：</p>
<ul>
<li>代码基于MMDetection，数据集为COCO2014</li>
<li>预训练在ImageNet-1K的DeiT作为backbone</li>
<li>使用四种主流检测头：Mask R-CNN , Cascade Mask R-CNN , ATSS and GFL</li>
<li>36 epoch</li>
<li>batch size为16</li>
<li>AdamW优化器，学习率$1\times10^{-4}$，衰减0.05</li>
</ul>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>pip <span class="token function">install</span> torch torchvision torchaudio
pip <span class="token function">install</span> openmim
mim <span class="token function">install</span> mmcv-full<span class="token operator">==</span><span class="token number">1.5</span>.0
mim <span class="token function">install</span> <span class="token assign-left variable">mmdet</span><span class="token operator">==</span><span class="token number">2.22</span>.0
pip <span class="token function">install</span> <span class="token assign-left variable">timm</span><span class="token operator">==</span><span class="token number">0.4</span>.12
pip <span class="token function">install</span> instaboostfast
<span class="token builtin class-name">cd</span> ops <span class="token operator">&amp;</span> <span class="token function">sh</span> make.sh
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>代码细节：</p>
<ul>
<li>extractor层的FFN使用的是深度可分离卷积(DW)，它会对输入的x重新进行划分为三个尺度，分别对他们进行卷积操作，最后在合并</li>
</ul>
<p>使用了MMDetection工具，只需要定义model(backbone,neck)，数据集位置，一些环境设置(GPU数量，checkpoint文件位置)，就可以进行训练。</p>
<p>训练：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment"># 配置文件为configs/mask_rcnn/mask_rcnn_deit_adapter_tiny_fpn_3x_coco.py</span>
<span class="token comment"># GPU数量为2</span>
<span class="token function">sh</span> dist_train.sh configs/mask_rcnn/mask_rcnn_deit_adapter_tiny_fpn_3x_coco.py <span class="token number">2</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 19.png" alt="Untitled"></p>
<p>大概要训练一两天。</p>
<p>测试：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sh</span> dist_test.sh configs/mask_rcnn/mask_rcnn_deit_adapter_base_fpn_3x_coco.py /data/dth/ViT_Adapter/pretrained/deit_base_patch16_224-b5f2ef4d.pth <span class="token number">2</span> <span class="token parameter variable">--eval</span> bbox segm
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><blockquote>
<p>Yang, Taojiannan, et al. &quot;AIM: Adapting Image Models for Efficient Video Action Recognition.&quot; <em>arXiv preprint arXiv:2302.03024</em> (2023).</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 20.png" alt="Untitled"></p>
<p>实验设置：</p>
<ul>
<li>使用Diving-48数据集</li>
<li>使用CLIP预训练模型，ViT-B/16</li>
<li>AdamW优化器，学习率3e-4，衰减0.05</li>
<li>训练 50 epoch，batch size为64</li>
</ul>
<p>代码细节：</p>
<ul>
<li>S_Adapter使用了残差连接，而MLP_Adapter和T_Adapter没有使用残差连接</li>
</ul>
<p>使用了MMaction框架，只需要定义model，数据集位置，一些环境设置(GPU数量，checkpoint文件位置)，就可以进行训练。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">bash</span> tools/dist_train.sh configs/recognition/vit/vitclip_base_diving48.py <span class="token number">2</span> --test-last <span class="token parameter variable">--validate</span> --cfg-options <span class="token assign-left variable">work_dir</span><span class="token operator">=</span>./work_dir --resume-from /data/dth/diving48/vit_b_clip_32frame_diving48.pth
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 21.png" alt="Untitled"></p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment"># 使用官方pth</span>
<span class="token function">bash</span> tools/dist_test.sh configs/recognition/vit/vitclip_base_diving48.py /data/dth/diving48/vit_b_clip_32frame_diving48.pth <span class="token number">2</span> <span class="token parameter variable">--eval</span> top_k_accuracy
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment"># 使用自己训练的pth</span>
<span class="token function">bash</span> tools/dist_test.sh configs/recognition/vit/vitclip_base_diving48.py /code/dth/adapt-image-models/work_dir/best_top1_acc_epoch_40.pth <span class="token number">2</span> <span class="token parameter variable">--eval</span> top_k_accuracy
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 22.png" alt="Untitled"></p>
<blockquote>
<p><strong>Mou, Chong, et al. &quot;T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models.&quot; <em>arXiv preprint arXiv:2302.08453</em> (2023).</strong></p>
</blockquote>
<p>T2I模型需要精心设计文本prompts才能生成较好的图片，导致用户很难引导模型生成想象中的图片。作者认为，这并不意味着T2I模型不具备生成能力，只是文本不能提供准确的结构指导，也就是模型是有较强的生成能力的，但是缺乏指导它生成的能力（文本不能准确地完成）。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 23.png" alt="Untitled"></p>
<p>因此作者提出了T2I-Adapter，这是一个轻量级模型，可以用相对少量的数据来学习为预先训练好的T2I扩散模型(即SD[32])提供额外的指导。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 24.png" alt="Untitled"></p>
<p>Adapter包含了四个特征提取块和三个下采样块，最终将四个多尺度特征图与SD模型中每个UNet denoiser相加。这样adapters就可以提取不同类型condition的指导特征，与输入的文本特征一起参与到SD的图片生成中了。</p>
<p>$$
\mathbf{F}<em>c=\sum</em>{k=1}^K\omega_k\mathcal{F}^k_{AD}(\mathbf{C}_k),
$$</p>
<p>因此可以使用草图、mask、keypose、语义分割图、深度图等condition，指导T2I模型生成图片。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 25.png" alt="Untitled"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 26.png" alt="Untitled"></p>
<p>这些论文探讨了将Adapter应用于不同模型和任务的各种方法，包括视觉-语言模型、少样本分类、图像到视频迁移学习、密集预测以及文本到图像扩散模型。Adapter为将预训练模型的知识迁移到新任务提供了一种高效的方式，通过最小化参数更新来实现更好的性能和对模型输出的细粒度控制。</p>
<ol>
<li>在CLIP的输出后加上Adapter，同时使用残差连接线性组合预训练模型和微调模型的权重，以改进视觉-语言任务。</li>
<li>Tip-Adapter在不经过训练的情况下实现了与微调过的CoOp和CLIP-Adapter模型相当的性能，充分利用了CLIP的零样本能力和少样本性能。如果对Cache Model中的key进行训练，还可进一步大幅提高模型性能。</li>
<li>ST-Adapter通过时空Adapter模块实现了高效的图像到视频迁移学习，显著减少了参数更新所需的数量。</li>
<li>将Adapter用于plain ViTs，通过加入空间先验模块和多尺度特征提取，提高了模型的性能，使其可以与Swin等对视觉先验信息有特殊设计的模型表现相当。同时还可用于各种密集预测任务</li>
<li>T2i-Adapter旨在为文本到图像扩散模型提供更可控的能力，使用户能够更好地根据文本、草图、mask等提示引导模型的输出。</li>
</ol>
<p><a href="https://github.com/taoyang1122/adapt-image-models" target="_blank" rel="noopener noreferrer">https://github.com/taoyang1122/adapt-image-models<ExternalLinkIcon/></a></p>
<blockquote>
<p>He, Junxian, et al. &quot;Towards a unified view of parameter-efficient transfer learning.&quot; <em>arXiv preprint arXiv:2110.04366</em> (2021).</p>
</blockquote>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 27.png" alt="Untitled"></p>
<p><strong>Adapters：将特征向量经过一个下采样、非线性激活层、上采样后，再残差连接</strong></p>
<p>$$
h\leftarrow h+f(hW_{\text{down}})W_{\text{up}}
$$</p>
<p><strong>Prefix Tuning：将原始的key和value前加上可学习的prompt</strong></p>
<p>$$
\text{head}_i=\text{Atn}(\pmb{x}\pmb{W}_q^{(i)},\text{const}(\pmb{P}_k^{(i)},\pmb{C}\pmb{W}_k^{(i)}),\pmb{\text{const}}(\pmb{P}_v^{(i)},\boldsymbol{CW}_v^{(i)}))
$$</p>
<p><strong>LoRA：将可训练的低秩矩阵注入到transformer中，以近似权值更新</strong></p>
<p>$$
h\leftarrow h+s\cdot x\boldsymbol{W}<em>{\text{down}}W</em>{\text{up}},
$$</p>
<p>对于prefix tunning，对公式进行拆开：</p>
<p>$$
(1-\lambda(\boldsymbol x))\text{Atn}(\boldsymbol x\boldsymbol W_q,\boldsymbol CW_k,\boldsymbol CW_v)+\lambda(\boldsymbol x)\text{A}\text{tn}(\boldsymbol x\textbf{W}_q,\boldsymbol P_k,\boldsymbol P_v)
$$</p>
<p>令$\textbf{W}_1\textbf{=}W_q\textbf{P}_k^\top,\textbf{W}_2\textbf{=}P_v$</p>
<p>$$
\pmb{h}\leftarrow(1-\lambda(\pmb{x}))h+\lambda(\pmb{x})f(\pmb{x}\pmb{W}_1)\pmb{W}_2
$$</p>
<p>因此可以把三个方法归纳为：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 28.png" alt="Untitled"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/Untitled 29.png" alt="Untitled"></p>
<p><strong>结论：</strong></p>
<ul>
<li>并联方式</li>
<li>将adapter中0.1%的参数放在attn，剩余的参数放在FFN（通常adapter放在FFN后效果更好，但当参数量较少，放在attn后提升更大）</li>
<li>使用$\boldsymbol{h}\leftarrow h+s\cdot\Delta h$结构</li>
</ul>
</div></template>


