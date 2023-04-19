<template><div><h1 id="线性代数" tabindex="-1"><a class="header-anchor" href="#线性代数" aria-hidden="true">#</a> 线性代数</h1>
<p>线性代数主要包含向量、向量空间（或称线性空间）以及向量的线性变换和 有限维的线性方程组．</p>
<h2 id="向量和向量空间" tabindex="-1"><a class="header-anchor" href="#向量和向量空间" aria-hidden="true">#</a> 向量和向量空间</h2>
<h3 id="向量" tabindex="-1"><a class="header-anchor" href="#向量" aria-hidden="true">#</a> 向量</h3>
<p>向量（Vector）是由一组实数组成的有序数组，同时具有<strong>大小</strong>和<strong>方向</strong></p>
<p><strong>one-hot 向量</strong>为有且只有一个元素为 1，其余元素都为 0 的向量．one-hot 向 量是在数字电路中的一种状态编码，指对任意给定的状态，状态寄存器中只有 l 位为 1，其余位都为 0．</p>
<h3 id="向量空间" tabindex="-1"><a class="header-anchor" href="#向量空间" aria-hidden="true">#</a> 向量空间</h3>
<p>向量空间（Vector Space），也称线性空间（Linear Space），是指由向量组成的集合，并满足以下两个条件：</p>
<ol>
<li>向量加法+：向量空间 𝒱 中的两个向量 𝒂 和 𝒃，它们的和 𝒂 + 𝒃 也属于 空间 𝒱 ；</li>
<li>标量乘法⋅：向量空间 𝒱 中的任一向量 𝒂 和任一标量 𝑐，它们的乘积 𝑐⋅𝒂 也属于空间 𝒱 ．</li>
</ol>
<p>**线性子空间：**向量空间 𝒱 的线性子空间 𝒰 是 𝒱 的一个子集，并且满足向量空间 的条件（向量加法和标量乘法）．</p>
<p><strong>线性无关：</strong> 线性空间 𝒱 中的 𝑀 个向量 {𝒗 1 , 𝒗 2 , ⋯ , 𝒗 𝑀 }，如果对任意的一组标量𝜆 1 , 𝜆 2 , ⋯ , 𝜆 𝑀 ，满足 𝜆 1 𝒗 1 +𝜆 2 𝒗 2 +⋯+𝜆 𝑀 𝒗 𝑀 = 0，则必然 𝜆 1 = 𝜆 2 = ⋯ = 𝜆 𝑀 =0，那么 {𝒗 1 , 𝒗 2 , ⋯ , 𝒗 𝑀 } 是线性无关的，也称为线性独立的．</p>
<p><strong>基向量：</strong> 𝑁 维向量空间 𝒱 的基（Base）ℬ = {𝒆 1 , 𝒆 2 , ⋯ , 𝒆 𝑁 } 是 𝒱 的有限子集，其元素之间线性无关．向量空间 𝒱 中所有的向量都可以按唯一的方式表达为 ℬ 中 向量的线性组合．对任意 𝑣 ∈ 𝒱 ，存在一组标量 (𝜆 1 , 𝜆 2 , ⋯ , 𝜆 𝑁 ) 使得
$$
𝒗 = 𝜆_1 𝒆_1 + 𝜆_2 𝒆_2 + ⋯ + 𝜆_𝑁 𝒆_𝑁
$$
其中基 ℬ 中的向量称为基向量（Base Vector）．如果基向量是有序的，则标量 (𝜆 1 , 𝜆 2 , ⋯ , 𝜆 𝑁 ) 称为向量 𝒗 关于基 ℬ 的坐标（Coordinate）． 𝑁 维空间 𝒱 的一组标准基（Standard Basis）为</p>
<p>𝒆 1 = [1, 0, 0, ⋯ , 0],</p>
<p>𝒆 2 = [0, 1, 0, ⋯ , 0],</p>
<p>⋯</p>
<p>𝒆 𝑁 = [0, 0, 0, ⋯ , 1],</p>
<p>𝒱 中的任一向量 𝒗 = [𝑣 1 , 𝑣 2 , ⋯ , 𝑣 𝑁 ] 可以唯一地表示为</p>
<p>[𝑣 1 , 𝑣 2 , ⋯ , 𝑣 𝑁 ] = 𝑣 1 𝒆 1 + 𝑣 2 𝒆 2 + ⋯ + 𝑣 𝑁 𝒆 𝑁 ,</p>
<p>𝑣 1 , 𝑣 2 , ⋯ , 𝑣 𝑁 也称为向量 𝒗 的笛卡尔坐标（Cartesian Coordinate）．</p>
<p>向量空间中的每个向量可以看作一个线性空间中的笛卡尔坐标．</p>
<p><strong>内积：</strong> 一个 𝑁 维线性空间中的两个向量 𝒂 和 𝒃，其内积（Inner Product）为
$$
𝑁 ⟨𝒂, 𝒃⟩ = ∑ 𝑎_𝑛  𝑏_𝑛
$$
内积也称为点积（Dot Product）或标量积（Scalar Product）．</p>
<p><strong>正交：</strong> 如果向量空间中两个向量的内积为 0，则它们正交（Orthogonal）．如果 向量空间中一个向量 𝒗 与子空间 𝒰 中的每个向量都正交，那么向量 𝒗 和子空间 𝒰 正交．</p>
<h3 id="范数" tabindex="-1"><a class="header-anchor" href="#范数" aria-hidden="true">#</a> 范数</h3>
<p>范数（Norm）是一个表示向量“长度”的函数，为向量空间内的所有向量赋 予非零的正长度或大小．</p>
<p><strong>ℓ1 范数：</strong> ℓ1 范数为向量的各个元素的绝对值之和．</p>
<p>**ℓ2 范数：**ℓ2 范数为向量的各个元素的平方和再开平方．ℓ 2 范数又称为Euclidean 范数或者Frobenius 范数．从几何角度，向量也可以表示为从原点出发的一个带箭头的有向线段，其 ℓ 2 范数为线段的长度，也常称 为向量的模．</p>
<p><strong>ℓ∞</strong> 范数 ℓ ∞ 范数为向量的各个元素的最大绝对值，</p>
<p>图给出了常见范数的示例，其中红线表示不同范数的 ℓ𝑝 = 1 的点．</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2022/07/20/9ma8cB.png" alt="9ma8cB"></p>
<h2 id="矩阵" tabindex="-1"><a class="header-anchor" href="#矩阵" aria-hidden="true">#</a> 矩阵</h2>
<h3 id="线性映射" tabindex="-1"><a class="header-anchor" href="#线性映射" aria-hidden="true">#</a> 线性映射</h3>
<p>线性映射（Linear Mapping） 是指从线性空间 𝒳 到线性空间 𝒴 的一个映射 函数 𝑓 ∶ 𝒳 → 𝒴 ，并满足：对于 𝒳 中任何两个向量 𝒖 和 𝒗 以及任何标量 𝑐，有
$$
𝑓(𝒖 + 𝒗) = 𝑓(𝒖) + 𝑓(𝒗),\</p>
<p>𝑓(𝑐𝒗) = 𝑐𝑓(𝒗).
$$</p>
<h3 id="仿射变换" tabindex="-1"><a class="header-anchor" href="#仿射变换" aria-hidden="true">#</a> 仿射变换</h3>
<p>仿射变换（Affine Transformation）是指通过一个线性变换和一个平移，将 一个向量空间变换成另一个向量空间的过程．</p>
<p>令 𝑨 ∈ ℝ 𝑁×𝑁 为 𝑁 × 𝑁 的实数矩阵，𝒙 ∈ ℝ 𝑁 是 𝑁 维向量空间中的点，仿射变换可以表示为
$$
𝒚 = 𝑨𝒙 + 𝒃,
$$
其中 𝒃 ∈ ℝ 𝑁 为平移项．当 𝒃 = 0 时，仿射变换就退化为线性变换．</p>
<p>仿射变换可以实现线性空间中的旋转、平移、缩放变换．仿射变换不改变原 始空间的相对位置关系，具有以下性质．</p>
<ol>
<li>**共线性（Collinearity）不变：**在同一 条直线上的三个或三个以上的点，在变换后依然在一条直线上；</li>
<li>**比例不变：**不 同点之间的距离比例在变换后不变；</li>
<li>**平行性不变：**两条平行线在转换后依然平行；</li>
<li>**凸性不变：**一个凸集（Convex Set）在转换后依然是凸的.</li>
</ol>
<h3 id="矩阵操作" tabindex="-1"><a class="header-anchor" href="#矩阵操作" aria-hidden="true">#</a> 矩阵操作</h3>
<p>矩阵的乘法满足结合律和分配律，不满足交换律。</p>
<p><strong>Hadamard 积：</strong> 矩阵 𝑨 和矩阵 𝑩 的Hadamard 积（Hadamard Product）也称 为逐点乘积，为 𝑨 和 𝑩 中对应的元素相乘．
$$
[𝑨 ⊙ 𝑩] <em>{𝑚𝑛} = 𝑎 <em>{𝑚𝑛} 𝑏 <em>{𝑚𝑛} .
$$
<strong>Kronecker 积：</strong> 如果 𝑨 是 𝑀×𝑁 的矩阵，𝑩 是 𝑆×𝑇 的矩阵，那么它们的Kronecker 积（Kronecker Product）是一个 𝑀𝑆 × 𝑁𝑇 的矩阵：
$$
\left [ A\otimes B  \right ] =\begin{bmatrix}
a</em>{11}B &amp;a</em>{12}B  &amp;...  &amp;a</em>{1N}B \
a_{21}B&amp; a_{22}B &amp; ... &amp;a_{2N}B \
\vdots &amp; \vdots  &amp; \ddots  &amp;\vdots  \
a_{M1}B &amp;  a_{M2}B &amp;...  &amp; a_{MN}B
\end{bmatrix}
$$</p>
</div></template>


