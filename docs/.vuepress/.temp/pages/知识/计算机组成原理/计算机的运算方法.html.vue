<template><div><h1 id="无符号数和有符号数" tabindex="-1"><a class="header-anchor" href="#无符号数和有符号数" aria-hidden="true">#</a> 无符号数和有符号数</h1>
<h2 id="无符号数" tabindex="-1"><a class="header-anchor" href="#无符号数" aria-hidden="true">#</a> 无符号数</h2>
<h2 id="有符号数" tabindex="-1"><a class="header-anchor" href="#有符号数" aria-hidden="true">#</a> 有符号数</h2>
<h3 id="机器数与真值" tabindex="-1"><a class="header-anchor" href="#机器数与真值" aria-hidden="true">#</a> 机器数与真值</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200820193255237.png" alt="image-20200820193255237"></p>
<h3 id="原码表示法" tabindex="-1"><a class="header-anchor" href="#原码表示法" aria-hidden="true">#</a> 原码表示法</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200820193928956.png" alt="image-20200820193928956"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200820204536743.png" alt="image-20200820204536743"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200820205216449.png" alt="image-20200820205216449"></p>
<h3 id="补码表示法" tabindex="-1"><a class="header-anchor" href="#补码表示法" aria-hidden="true">#</a> 补码表示法</h3>
<ul>
<li>一个负数加上“模”即得该负数的补数</li>
<li>一个正数和一个负数互为补数时，它们==绝对值之和==即为模数</li>
<li>一个正数的补码就是它本身</li>
<li>一个负数的补码就是各位取反再加1</li>
<li>小数正数的补码就是它本身</li>
<li>小数负数的补码就是2+它本身</li>
</ul>
<p>当真值为负时，补码转为原码同样适用：符号位不变，各位取反再加1</p>
<p>小数-1没有原码形式。</p>
<h3 id="反码表示法" tabindex="-1"><a class="header-anchor" href="#反码表示法" aria-hidden="true">#</a> 反码表示法</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200824180551028.png" alt="image-20200824180551028"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200824180817816.png" alt="image-20200824180817816"></p>
<hr>
<p>==三种机器数的小结==</p>
<ul>
<li>
<p>最高位为符号位，书写上用“，”（整数）或“.”（小数）将数值部分和符号位隔开</p>
</li>
<li>
<p>对于正数，原码=补码=反码</p>
</li>
<li>
<p>对于负数，符号位为1，其数值部分</p>
<p>原码除符号位外每位取反末位加1---&gt;补码</p>
<p>原码除符号位外每位取反---&gt;反码</p>
</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200824182701338.png" alt="image-20200824182701338"></p>
<h3 id="移码表示法" tabindex="-1"><a class="header-anchor" href="#移码表示法" aria-hidden="true">#</a> 移码表示法</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200824183345438.png" alt="image-20200824183345438"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200824183615320.png" alt="image-20200824183615320"></p>
<h1 id="数的定点表示和浮点表示" tabindex="-1"><a class="header-anchor" href="#数的定点表示和浮点表示" aria-hidden="true">#</a> 数的定点表示和浮点表示</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200827202711613.png" alt="image-20200827202711613"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200827203738002.png" alt="image-20200827203738002"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200827204521907.png" alt="image-20200827204521907"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200830110223228.png" alt="image-20200830110223228"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200830110824534.png" alt="image-20200830110824534"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200830111732372.png" alt="image-20200830111732372"></p>
<h1 id="定点运算" tabindex="-1"><a class="header-anchor" href="#定点运算" aria-hidden="true">#</a> 定点运算</h1>
<h2 id="移位运算" tabindex="-1"><a class="header-anchor" href="#移位运算" aria-hidden="true">#</a> 移位运算</h2>
<p>在计算机中，小数点位置不变，仅仅对数值进行移动。</p>
<p>移位与加减配合，能够实现乘除运算</p>
<h3 id="算术移位规则" tabindex="-1"><a class="header-anchor" href="#算术移位规则" aria-hidden="true">#</a> 算术移位规则</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200831135817454.png" alt="image-20200831135817454"></p>
<h3 id="算术移位和逻辑移位的区别" tabindex="-1"><a class="header-anchor" href="#算术移位和逻辑移位的区别" aria-hidden="true">#</a> 算术移位和逻辑移位的区别</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200831141601584.png" alt="image-20200831141601584"></p>
<h2 id="加减法运算" tabindex="-1"><a class="header-anchor" href="#加减法运算" aria-hidden="true">#</a> 加减法运算</h2>
<h3 id="补码加减运算公式" tabindex="-1"><a class="header-anchor" href="#补码加减运算公式" aria-hidden="true">#</a> 补码加减运算公式</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200904103421262.png" alt="image-20200904103421262"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200904103924524.png" alt="image-20200904103924524"></p>
<h3 id="溢出判断" tabindex="-1"><a class="header-anchor" href="#溢出判断" aria-hidden="true">#</a> 溢出判断</h3>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200904105156058.png" alt="image-20200904105156058"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200904110435516.png" alt="image-20200904110435516"></p>
<h1 id="补码加减法的硬件配置" tabindex="-1"><a class="header-anchor" href="#补码加减法的硬件配置" aria-hidden="true">#</a> 补码加减法的硬件配置</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200904111352264.png" alt="image-20200904111352264"></p>
<h1 id="浮点四则运算" tabindex="-1"><a class="header-anchor" href="#浮点四则运算" aria-hidden="true">#</a> 浮点四则运算</h1>
<p><strong>浮点数的加减运算</strong>：</p>
<ul>
<li>
<p>对阶</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921194819517.png" alt="image-20200921194819517"></p>
</li>
<li>
<p>尾数求和</p>
</li>
<li>
<p>规格化</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921195711801.png" alt="image-20200921195711801"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921200249574.png" alt="image-20200921200249574"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921200732852.png" alt="image-20200921200732852"></p>
</li>
<li>
<p>舍入</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921201650839.png" alt="image-20200921201650839"></p>
</li>
<li>
<p>溢出判断</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200921203120148.png" alt="image-20200921203120148"></p>
</li>
</ul>
<h1 id="算术逻辑单元" tabindex="-1"><a class="header-anchor" href="#算术逻辑单元" aria-hidden="true">#</a> 算术逻辑单元</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201005130431199.png" alt="image-20201005130431199"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201005131222034.png" alt="image-20201005131222034"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201005131255771.png" alt="image-20201005131255771"></p>
</div></template>


