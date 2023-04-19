<template><div><p><code v-pre>var</code> 关键字声明变量会提升到当前作用域的顶端，而<code v-pre>let</code>不行</p>
<h1 id="对象简化赋值" tabindex="-1"><a class="header-anchor" href="#对象简化赋值" aria-hidden="true">#</a> 对象简化赋值</h1>
<p>如果属性名和变量名相同，可以简写</p>
<p>方法可以省略function 关键字</p>
<h1 id="箭头函数" tabindex="-1"><a class="header-anchor" href="#箭头函数" aria-hidden="true">#</a> 箭头函数</h1>
<p>function 省略掉，替换为=&gt;</p>
<div class="language-javascript line-numbers-mode" data-ext="js"><pre v-pre class="language-javascript"><code><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">=></span><span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">"邓腾浩在奔跑"</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>参数只有一个时，可以省略()</p>
<div class="language-javascript line-numbers-mode" data-ext="js"><pre v-pre class="language-javascript"><code><span class="token parameter">p</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>p<span class="token punctuation">)</span>
  <span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>函数体只有一行时，可以省略{}</p>
<div class="language-javascript line-numbers-mode" data-ext="js"><pre v-pre class="language-javascript"><code><span class="token parameter">p</span> <span class="token operator">=></span> console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>p<span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>函数体只有一行，并且有返回值时，如果省略了{}，必须省略return</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>let func = () => '邓腾浩在奔跑'
console.log(func());
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


