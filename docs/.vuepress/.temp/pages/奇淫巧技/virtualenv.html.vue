<template><div><h1 id="venv虚拟环境创建" tabindex="-1"><a class="header-anchor" href="#venv虚拟环境创建" aria-hidden="true">#</a> venv虚拟环境创建</h1>
<p>建议使用Python的虚拟环境（virtual environment）。虚拟环境允许您在单个Docker容器中为每个项目创建一个独立的Python环境，这样您就可以为每个项目安装特定的依赖，而不会影响其他项目。</p>
<ol>
<li>
<p>安装virtualenv工具</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>pip <span class="token function">install</span> virtualenv
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>在项目目录下，使用命令创建一个新的虚拟环境</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>virtualenv venv
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>这将在项目目录中创建一个名为**<code v-pre>venv</code>**的文件夹，其中包含一个独立的Python环境。</p>
</li>
<li>
<p>激活环境</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">source</span> venv/bin/activate
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>安装项目所需的依赖项</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>pip <span class="token function">install</span> <span class="token parameter variable">-r</span> requirements.txt
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>要停用虚拟环境并返回到系统默认的Python环境，请运行：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>deactivate
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
</div></template>


