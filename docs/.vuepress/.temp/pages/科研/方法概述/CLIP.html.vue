<template><div><h1 id="clip" tabindex="-1"><a class="header-anchor" href="#clip" aria-hidden="true">#</a> CLIP</h1>
<p>Time: March 24, 2023 9:22 PM</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/53uQ5Y.png" alt="53uQ5Y"></p>
<p>CLIP迁移到其他大多数数据集（不需要额外的训练）可以跟有监督的baseline竞争，比如在ImageNet上训练的ResNet50，CLIP不需要额外的训练就可以达到相同的表现</p>
<p>**数据集：**WebImageText(WIT)， 4亿个图片-文本对</p>
<p>**模型：**ResNets和VIT，规模越大，表现越好，基本成正相关增长</p>
<p>**训练方式：**对比学习，让图片输出的特征与文本输出的特征尽可能相似</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic1/main/2023/04/18/Untitled 1.png" alt="Untitled"></p>
<p><strong>局限性：</strong></p>
<ol>
<li>尽管可以其他数据集上的baseline模型如ResNet50媲美，但是和state-of-the-art还是差了很远，如果想要靠增大模型和数据规模来弥补这部分的差距，是不切实际的，还需要新的方法。</li>
<li>对于细分类的任务，或者更难的任务（数图片有多少个物体，判断监控中的帧是否异常），都没有很好的效果，说明CLIP并不是个万能的模型。</li>
<li>对于out of distribution的数据，比如mnist，CLIP只要88%的准确率，还没有一个简单的逻辑回归模型表现好。</li>
<li>还是要人为给出文本，CLIP判断图片是否跟文本一致，而不能让CLIP自动根据图片生成文本，真正让模型“自动化”，因此作者思考未来能否将对比式学习和生成式学习结合起来</li>
<li>数据利用率低，训练用了32个epoch，相当于看了128亿张图片</li>
</ol>
</div></template>


