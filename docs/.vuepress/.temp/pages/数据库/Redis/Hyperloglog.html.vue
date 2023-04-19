<template><div><p>优点：占用的内存是固定的，只需要占用12KB内存！</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFadd mykey a b c d e f g h i j
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFCOUNT mykey
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">10</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFadd mykey2 i j z x c <span class="token function">v</span> b n m
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFCOUNT mykey2
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">9</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFMERGE mykey3 mykey mykey2
OK
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> PFCOUNT mykey3
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">15</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>有0.81%的错误率！ 统计UV任务，可以忽略不计！</p>
<p>如果允许容错，那么一定可以使用Hyperloglog</p>
</div></template>


