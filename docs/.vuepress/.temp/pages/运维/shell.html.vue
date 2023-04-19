<template><div><h1 id="shell" tabindex="-1"><a class="header-anchor" href="#shell" aria-hidden="true">#</a> shell</h1>
<h1 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍" aria-hidden="true">#</a> 介绍</h1>
<p>Shell 是一种计算机操作系统的用户界面，它是一种命令行界面，可以通过输入命令来控制计算机。Shell 可以与操作系统进行交互，使用户能够执行各种操作，例如创建、删除和修改文件，以及管理进程等。本文将介绍 Shell 的基础知识，以帮助初学者快速入门。</p>
<h1 id="shell-的类型" tabindex="-1"><a class="header-anchor" href="#shell-的类型" aria-hidden="true">#</a> Shell 的类型</h1>
<p>Shell 有许多不同的类型，其中最常用的是 Bash，它是 Linux 和 macOS 等操作系统默认的 Shell。其他常见的 Shell 类型包括 Zsh 和 Ksh 等。每种 Shell 都有自己的命令和语法，但大多数命令都是相同的。在本文中，我们将使用 Bash 作为示例。</p>
<h1 id="脚本执行方式" tabindex="-1"><a class="header-anchor" href="#脚本执行方式" aria-hidden="true">#</a> 脚本执行方式</h1>
<p>Shell 脚本可以通过 <code v-pre>bash</code> 命令或<code v-pre>source</code>命令或 <code v-pre>./</code> 运算符来执行，<code v-pre>./</code>使用的更多。</p>
<table>
<thead>
<tr>
<th>命令</th>
<th>特点</th>
</tr>
</thead>
<tbody>
<tr>
<td>bash</td>
<td>在新的 Shell 中执行脚本，不会影响当前 Shell 的环境变量和工作目录</td>
</tr>
<tr>
<td>source</td>
<td>在当前 Shell 中执行脚本，会影响当前 Shell 的环境变量和工作目录</td>
</tr>
<tr>
<td>./</td>
<td>在新的 Shell 中执行脚本，不会影响当前 Shell 的环境变量和工作目录</td>
</tr>
</tbody>
</table>
<p>也就是说<code v-pre>source</code>会使用当前shell环境的变量，<code v-pre>bash</code>和<code v-pre>./</code>则不会，需要当前环境变量为<code v-pre>export</code></p>
<p>Shell 中的 <code v-pre>export</code> 命令用于将值分配给变量，同时将变量标记为环境变量，这意味着它们在脚本中的所有命令都可用，并且在子 Shell 中也可用。没有使用 <code v-pre>export</code> 命令的变量仅在当前 Shell 会话中可用，并且在子 Shell 中不可用。</p>
<h1 id="shell变量" tabindex="-1"><a class="header-anchor" href="#shell变量" aria-hidden="true">#</a> Shell变量</h1>
<h3 id="shell-变量的命名要求" tabindex="-1"><a class="header-anchor" href="#shell-变量的命名要求" aria-hidden="true">#</a> Shell 变量的命名要求</h3>
<p>Shell 变量的命名遵循以下规则：</p>
<ul>
<li>变量名以字母或下划线开头，不能以数字开头。</li>
<li>变量名中可以包含字母、数字和下划线。</li>
<li>变量名必须是大小写敏感的。</li>
<li>变量名不能是 Shell 的关键字。</li>
</ul>
<p>赋值时等号两边不能有空格</p>
<h3 id="shell-变量的类型" tabindex="-1"><a class="header-anchor" href="#shell-变量的类型" aria-hidden="true">#</a> Shell 变量的类型</h3>
<p>Shell 变量的类型包括：</p>
<ul>
<li>环境变量：使用 <code v-pre>export</code> 命令将值分配给变量，同时将变量标记为环境变量，这意味着它们在脚本中的所有命令都可用，并且在子 Shell 中也可用。</li>
<li>局部变量：变量在 Shell 脚本中定义，但未使用 <code v-pre>export</code> 命令分配给它们，这意味着它们仅在当前 Shell 会话中可用，并且在子 Shell 中不可用。</li>
<li>Shell 变量：Shell 变量是由 Shell 已定义的变量，例如 Shell 的特殊变量 <code v-pre>$0</code>、<code v-pre>$1</code> 、$HOME、$PWD、$SHELL、$USER等。这些变量在 Shell 脚本中具有不同的作用和范围，可以根据需要选择使用。</li>
</ul>
<p>Shell 变量的类型包括以下几种：</p>
<ul>
<li>字符串：默认类型，用于存储文本。可以使用单引号或双引号来定义字符串变量。<strong>使用双引号时，可以在字符串中使用变量，变量会在字符串中被替换为其值。</strong></li>
<li>整数：用于存储整数。整数变量可以使用 <code v-pre>declare</code> 或 <code v-pre>typeset</code> 命令定义，也可以使用赋值语句定义。</li>
<li>数组：用于存储多个值。数组变量使用小括号来定义，其中每个值之间用空格分隔。可以使用下标来访问数组变量中的值，下标从 0 开始。</li>
</ul>
<p>在 Shell 中，变量无需事先声明其类型。根据变量的值，Shell 会自动确定其类型。</p>
<hr>
<p>Shell 中的数组变量可以存储多个值。数组变量的定义格式如下：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token assign-left variable">array_name</span><span class="token operator">=</span><span class="token punctuation">(</span>value1 value2 <span class="token punctuation">..</span>. valuen<span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>array_name</code> 是数组变量的名称，<code v-pre>value1</code>、<code v-pre>value2</code> 等是数组变量中的值，多个值之间用空格分隔。</p>
<p>访问数组变量的值可以使用下标，下标从 0 开始。例如，要访问数组变量 <code v-pre>array_name</code> 中的第一个值，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">${array_name<span class="token punctuation">[</span>0<span class="token punctuation">]</span>}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>使用 <code v-pre>${#array_name[@]}</code> 来输出数组变量的长度。例如，要输出数组变量 <code v-pre>array_name</code> 的长度，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">${<span class="token operator">#</span>array_name<span class="token punctuation">[</span>@<span class="token punctuation">]</span>}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><hr>
<p>Shell 中有一些特殊变量，用于保存 Shell 的状态和其他信息。以下是一些常见的特殊变量：</p>
<ul>
<li><code v-pre>$0</code>：Shell 脚本的名称。</li>
<li><code v-pre>$1</code>、<code v-pre>$2</code>、<code v-pre>$3</code> 等：Shell 脚本的参数。</li>
<li><code v-pre>$#</code>：Shell 脚本的参数个数。</li>
<li><code v-pre>$*</code>：所有参数列表。把所有参数看成一个整体</li>
<li><code v-pre>$@</code>：所有参数列表，每个参数都用双引号括起来。分开对待</li>
<li><code v-pre>$?</code>：上一个命令的退出状态。</li>
</ul>
<h2 id="变量的执行方式" tabindex="-1"><a class="header-anchor" href="#变量的执行方式" aria-hidden="true">#</a> 变量的执行方式</h2>
<p>变量可以通过 <code v-pre>$</code> 符号和变量名来调用。例如，要调用变量 <code v-pre>my_var</code>，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">$my_var</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>在字符串中使用变量可以使用双引号来定义字符串变量，变量会在字符串中被替换为其值。例如，要在字符串中使用变量 <code v-pre>my_var</code>，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token string">"Hello, <span class="token variable">$my_var</span>!"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>如果不希望变量在字符串中被替换为其值，可以使用单引号来定义字符串变量。例如，要在字符串中使用变量 <code v-pre>my_var</code>，但不希望它在字符串中被替换为其值，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token string">'Hello, $my_var!'</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>可以使用 <code v-pre>${#variable}</code> 来输出变量的长度。例如，要输出变量 <code v-pre>my_var</code> 的长度，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">${<span class="token operator">#</span>my_var}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>可以使用 <code v-pre>${variable:start:length}</code> 来截取变量。其中，<code v-pre>start</code> 表示要截取的起始位置，<code v-pre>length</code> 表示要截取的长度。例如，要从变量 <code v-pre>my_var</code> 中截取前 5 个字符，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">${my_var<span class="token operator">:</span>0<span class="token operator">:</span>5}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>要截取从第 5 个字符开始的后面的所有字符，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token variable">${my_var<span class="token operator">:</span>4}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，数字 4 表示从第 5 个字符开始。</p>
<h2 id="只读变量" tabindex="-1"><a class="header-anchor" href="#只读变量" aria-hidden="true">#</a> 只读变量</h2>
<p>在 Shell 中，可以使用 <code v-pre>readonly</code> 命令将变量标记为只读。一旦变量被标记为只读，就不能再次分配给它。使用 <code v-pre>readonly</code> 命令的语法如下：</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>readonly variable_name
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>variable_name</code> 是要标记为只读的变量的名称。</p>
<p>标记为只读的变量在 Shell 脚本中非常有用，可以防止不小心更改变量的值。</p>
<h1 id="注释" tabindex="-1"><a class="header-anchor" href="#注释" aria-hidden="true">#</a> 注释</h1>
<p>在 Shell 中，单行注释以 <code v-pre>#</code> 开头，多行注释可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>:<span class="token operator">&lt;</span>EOF
这是一个多行注释。
这里可以写多行注释内容。
EOF
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><code v-pre>:&lt;EOF</code> 表示开始多行注释，<code v-pre>EOF</code> 表示结束多行注释。在 <code v-pre>:&lt;EOF</code> 和 <code v-pre>EOF</code> 之间的所有内容都将被视为注释，不会被 Shell 解释或执行。这种语法非常有用，可以帮助开发人员在代码中添加注释和文档，提高代码的可读性和可维护性。</p>
<h1 id="shell运算" tabindex="-1"><a class="header-anchor" href="#shell运算" aria-hidden="true">#</a> Shell运算</h1>
<p>在 Shell 中，运算符用于执行各种算术和逻辑运算。以下是一些常用的 Shell 运算符：</p>
<ul>
<li>算术运算符：用于执行算术运算，例如加、减、乘、除等。常见的算术运算符包括 <code v-pre>+</code>、<code v-pre>、</code>、<code v-pre>/</code>、<code v-pre>%</code> 等。</li>
<li>关系运算符：用于比较两个值之间的关系，例如相等、大于、小于等。常见的关系运算符包括 <code v-pre>=</code>、<code v-pre>!=</code>、<code v-pre>eq</code>、<code v-pre>ne</code>、<code v-pre>gt</code>、<code v-pre>lt</code>、<code v-pre>ge</code>、<code v-pre>le</code> 等。</li>
<li>布尔运算符：用于执行布尔运算，例如逻辑与、逻辑或、逻辑非等。常见的布尔运算符包括 <code v-pre>&amp;&amp;</code>、<code v-pre>||</code>、<code v-pre>!</code> 等。</li>
<li>位运算符：用于执行位运算，例如按位与、按位或、按位异或等。常见的位运算符包括 <code v-pre>&amp;</code>、<code v-pre>|</code>、<code v-pre>^</code> 等。</li>
<li>赋值运算符：用于将值分配给变量。常见的赋值运算符包括 <code v-pre>=</code>、<code v-pre>+=</code>、<code v-pre>=</code>、<code v-pre>=</code>、<code v-pre>/=</code>、<code v-pre>%=</code> 等。</li>
</ul>
<p>除了这些常见的运算符之外，Shell 还有许多其他类型的运算符，例如字符串运算符、文件测试运算符等。</p>
<p>在 Shell 脚本中使用运算符时，需要注意运算符周围的空格。<strong>一般来说，运算符两侧应该留出空格</strong>，以使代码更易于阅读和理解。例如，以下是一个使用算术运算符的示例：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token assign-left variable">result</span><span class="token operator">=</span><span class="token variable"><span class="token variable">$((</span>$a <span class="token operator">+</span> $b<span class="token variable">))</span></span>
<span class="token assign-left variable">result</span><span class="token operator">=</span><span class="token variable"><span class="token variable">`</span><span class="token function">expr</span> $a + $b<span class="token variable">`</span></span>
<span class="token assign-left variable">result</span><span class="token operator">=</span>$<span class="token punctuation">[</span>a + b<span class="token punctuation">]</span>

<span class="token builtin class-name">echo</span> <span class="token variable">$result</span>   <span class="token comment"># 输出 3</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在这个示例中，<code v-pre>$((1 + 2))</code> 使用算术运算符将 1 和 2 相加，然后将结果分配给变量 <code v-pre>result</code>。</p>
<p><strong>注意</strong></p>
<ul>
<li>乘号(*)前边必须加反斜杠()才能实现乘法运算；</li>
<li><code v-pre>expr</code> 不支持浮点数运算。如果需要进行浮点数计算，可能需要使用其他工具，比如 <code v-pre>bc</code>。</li>
</ul>
<p>而逻辑运算符需要使用[]来调用，如<code v-pre>if [$a -ge $b]</code>，也可以使用<code v-pre>test</code> :</p>
<p><code v-pre>test</code>命令在Shell中用于检查文件的类型和比较值。它可以测试文件是否存在（<code v-pre>-e</code>），是否为普通文件（<code v-pre>-f</code>），是否为目录（<code v-pre>-d</code>），是否为空（<code v-pre>-s</code>），是否可读（<code v-pre>-r</code>），是否可写（<code v-pre>-w</code>），是否可执行（<code v-pre>-x</code>），以及比较运算符（<code v-pre>-eq</code>，<code v-pre>-ne</code>，<code v-pre>-gt</code>，<code v-pre>-lt</code>，<code v-pre>-ge</code>，<code v-pre>-le</code>）。可以使用<code v-pre>[ ]</code>或<code v-pre>[[ ]]</code>替代，但需要在中间留出空格。</p>
<h1 id="echo" tabindex="-1"><a class="header-anchor" href="#echo" aria-hidden="true">#</a> echo</h1>
<p><code v-pre>echo</code> 命令用于在 Shell 中打印文本。例如，要打印 &quot;Hello, world!&quot;，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">echo</span> <span class="token string">"Hello, world!"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p><code v-pre>echo</code> 命令还可以使用转义字符来打印特殊字符，例如换行符和制表符。以下是一些常用的转义字符：</p>
<ul>
<li><code v-pre>\\n</code>：换行符</li>
<li><code v-pre>\\t</code>：制表符</li>
<li><code v-pre>\\\\</code>：反斜杠</li>
<li><code v-pre>\\&quot;</code>：双引号</li>
</ul>
<p>例如，要打印一个包含制表符和换行符的字符串，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">echo</span> <span class="token string">"Hello,<span class="token entity" title="\\">\\</span>tworld!<span class="token entity" title="\\">\\</span>nHow are you today?"</span>
<span class="token builtin class-name">echo</span> <span class="token variable"><span class="token variable">`</span><span class="token builtin class-name">pwd</span><span class="token variable">`</span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="shell-流程控制" tabindex="-1"><a class="header-anchor" href="#shell-流程控制" aria-hidden="true">#</a> Shell 流程控制</h1>
<p>在 Shell 中，可以使用各种控制结构来控制程序的流程。以下是一些常见的控制结构：</p>
<h2 id="if-语句" tabindex="-1"><a class="header-anchor" href="#if-语句" aria-hidden="true">#</a> if 语句</h2>
<p><code v-pre>if</code> 语句用于测试一个条件，并根据条件的结果执行不同的命令。以下是一个 <code v-pre>if</code> 语句的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">if</span> <span class="token punctuation">[</span> condition1 <span class="token punctuation">]</span>
<span class="token keyword">then</span>
    command1
<span class="token keyword">elif</span> <span class="token punctuation">[</span> condition2 <span class="token punctuation">]</span>
<span class="token keyword">then</span>
		command2
<span class="token keyword">else</span>
    command3
<span class="token keyword">fi</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="for-循环" tabindex="-1"><a class="header-anchor" href="#for-循环" aria-hidden="true">#</a> for 循环</h2>
<p><code v-pre>for</code> 循环用于在 Shell 中迭代一个列表，并执行相应的命令。以下是一个 <code v-pre>for</code> 循环的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">for</span> <span class="token for-or-select variable">variable</span> <span class="token keyword">in</span> item1 item2 <span class="token punctuation">..</span>. itemN
<span class="token keyword">do</span>
    command1
    command2
    <span class="token punctuation">..</span>.
<span class="token keyword">done</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>其中，<code v-pre>variable</code> 是要迭代的变量，<code v-pre>list</code> 是要迭代的列表，<code v-pre>command1</code>、<code v-pre>command2</code> 等是要在每次迭代时执行的命令。</p>
<h2 id="while-循环" tabindex="-1"><a class="header-anchor" href="#while-循环" aria-hidden="true">#</a> while 循环</h2>
<p><code v-pre>while</code> 循环用于在 Shell 中重复执行命令，直到条件为假。以下是一个 <code v-pre>while</code> 循环的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">while</span> condition
<span class="token keyword">do</span>
    command1
    command2
    <span class="token punctuation">..</span>.
<span class="token keyword">done</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="until-循环" tabindex="-1"><a class="header-anchor" href="#until-循环" aria-hidden="true">#</a> until 循环</h2>
<p><code v-pre>until</code> 循环用于在 Shell 中重复执行命令，直到条件为真。以下是一个 <code v-pre>until</code> 循环的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">until</span> condition
<span class="token keyword">do</span>
    command1
    command2
    <span class="token punctuation">..</span>.
<span class="token keyword">done</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="case-语句" tabindex="-1"><a class="header-anchor" href="#case-语句" aria-hidden="true">#</a> case 语句</h2>
<p><code v-pre>case</code> 语句用于测试一个变量，并根据变量的值执行不同的命令。以下是一个 <code v-pre>case</code> 语句的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">case</span> variable <span class="token keyword">in</span>
value1<span class="token punctuation">)</span>
    command1
    command2
    <span class="token punctuation">..</span>.
    <span class="token punctuation">;</span><span class="token punctuation">;</span>
value2<span class="token punctuation">)</span>
    command3
    command4
    <span class="token punctuation">..</span>.
    <span class="token punctuation">;</span><span class="token punctuation">;</span>
*<span class="token punctuation">)</span>
    command5
    command6
    <span class="token punctuation">..</span>.
    <span class="token punctuation">;</span><span class="token punctuation">;</span>
<span class="token keyword">esac</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>其中，<code v-pre>variable</code> 是要测试的变量，<code v-pre>value1</code>、<code v-pre>value2</code> 等是变量可能的值，可以用read来读取变量，如<code v-pre>read variable</code></p>
<h2 id="break-和-continue" tabindex="-1"><a class="header-anchor" href="#break-和-continue" aria-hidden="true">#</a> break 和 continue</h2>
<p>在 Shell 中，可以使用 <code v-pre>break</code> 和 <code v-pre>continue</code> 命令来控制循环的执行。</p>
<h1 id="shell函数" tabindex="-1"><a class="header-anchor" href="#shell函数" aria-hidden="true">#</a> Shell函数</h1>
<h2 id="basename-和-dirname-函数" tabindex="-1"><a class="header-anchor" href="#basename-和-dirname-函数" aria-hidden="true">#</a> basename 和 dirname 函数</h2>
<h2 id="basename-和-dirname-函数-1" tabindex="-1"><a class="header-anchor" href="#basename-和-dirname-函数-1" aria-hidden="true">#</a> basename 和 dirname 函数</h2>
<p><code v-pre>basename</code> 函数用于获取指定路径中的文件名部分，<code v-pre>dirname</code> 函数用于获取指定路径中的目录部分。</p>
<h3 id="basename-函数" tabindex="-1"><a class="header-anchor" href="#basename-函数" aria-hidden="true">#</a> basename 函数</h3>
<p><code v-pre>basename</code> 函数的语法如下：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">basename</span> path <span class="token punctuation">[</span>suffix<span class="token punctuation">]</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>path</code> 表示要获取文件名的路径，<code v-pre>suffix</code> 表示要去除的后缀。</p>
<p>如果不指定 <code v-pre>suffix</code> 参数，则 <code v-pre>basename</code> 函数会返回 <code v-pre>path</code> 中的文件名部分。</p>
<p>如果指定 <code v-pre>suffix</code> 参数，则 <code v-pre>basename</code> 函数会从 <code v-pre>path</code> 中去除指定的后缀，然后返回剩余的部分。</p>
<h3 id="dirname-函数" tabindex="-1"><a class="header-anchor" href="#dirname-函数" aria-hidden="true">#</a> dirname 函数</h3>
<p><code v-pre>dirname</code> 函数的语法如下：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">dirname</span> path
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>path</code> 表示要获取目录的路径。</p>
<p><code v-pre>dirname</code> 函数会返回 <code v-pre>path</code> 中的目录部分。</p>
<p>如果 <code v-pre>path</code> 中不包含目录部分，则 <code v-pre>dirname</code> 函数会返回 <code v-pre>.</code>。</p>
<p><code v-pre>basename</code> 和 <code v-pre>dirname</code> 函数在 Shell 脚本中非常有用，可以帮助开发人员处理文件和路径相关的任务，提高代码的可读性和可维护性。</p>
<h2 id="自定义函数" tabindex="-1"><a class="header-anchor" href="#自定义函数" aria-hidden="true">#</a> 自定义函数</h2>
<p>在 Shell 中，可以使用函数来组织和重用代码。以下是一个函数的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function-name function">function_name</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    command1
    command2
    <span class="token punctuation">..</span>.
    <span class="token builtin class-name">return</span> value
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>其中，<code v-pre>function_name</code> 是函数的名称，<code v-pre>command1</code>、<code v-pre>command2</code> 等是要在函数中执行的命令，<code v-pre>value</code> 是函数的返回值。</p>
<p>要调用函数，可以使用以下语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>function_name arg1 arg2 <span class="token punctuation">..</span>.
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>arg1</code>、<code v-pre>arg2</code> 等是函数的参数。调用时使用$1,$2,${10}来调用</p>
<hr>
<p>函数还可以使用局部变量。局部变量只在函数内部可见，并在函数执行完毕后被删除。要定义局部变量，可以使用 <code v-pre>local</code> 命令。例如：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token keyword">function</span> <span class="token function-name function">my_func</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token builtin class-name">local</span> <span class="token assign-left variable">my_var</span><span class="token operator">=</span><span class="token number">123</span>
    <span class="token builtin class-name">echo</span> <span class="token string">"my_var is <span class="token variable">$my_var</span>"</span>
<span class="token punctuation">}</span>

my_func   <span class="token comment"># 输出 "my_var is 123"</span>
<span class="token builtin class-name">echo</span> <span class="token string">"my_var is <span class="token variable">$my_var</span>"</span>   <span class="token comment"># 报错：my_var: 未找到命令</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="shell-脚本" tabindex="-1"><a class="header-anchor" href="#shell-脚本" aria-hidden="true">#</a> Shell 脚本</h1>
<h2 id="开机运行" tabindex="-1"><a class="header-anchor" href="#开机运行" aria-hidden="true">#</a> 开机运行</h2>
<ol>
<li>
<p>创建一个需要运行的脚本，确保脚本具有可执行权限</p>
</li>
<li>
<ol>
<li>创建一个新的 Systemd 服务文件。请使用文本编辑器创建一个新文件，例如 <strong><code v-pre>/etc/systemd/system/my_script.service</code></strong>，并添加以下内容：</li>
</ol>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token punctuation">[</span>Unit<span class="token punctuation">]</span>
<span class="token assign-left variable">Description</span><span class="token operator">=</span>My custom startup script
<span class="token assign-left variable">After</span><span class="token operator">=</span>network.target

<span class="token punctuation">[</span>Service<span class="token punctuation">]</span>
<span class="token assign-left variable">ExecStart</span><span class="token operator">=</span>/path/to/your/script.sh
<span class="token assign-left variable">Type</span><span class="token operator">=</span>oneshot
<span class="token assign-left variable">RemainAfterExit</span><span class="token operator">=</span>yes

<span class="token punctuation">[</span>Install<span class="token punctuation">]</span>
<span class="token assign-left variable">WantedBy</span><span class="token operator">=</span>multi-user.target
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>请确保将 **<code v-pre>ExecStart</code>**的路径替换为您的实际脚本路径。</p>
</li>
<li>
<p>通知 Systemd 重新加载配置：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sudo</span> systemctl daemon-reload
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>启用新创建的服务，使其在开机时自动运行：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sudo</span> systemctl <span class="token builtin class-name">enable</span> my_script.service
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
<p>现在，每次系统启动时，<strong><code v-pre>/path/to/your/script.sh</code></strong> 都会自动运行。如果您需要手动启动、停止或查看服务状态，可以使用以下命令：</p>
<ul>
<li>启动服务：<strong><code v-pre>sudo systemctl start my_script.service</code></strong></li>
<li>停止服务：<strong><code v-pre>sudo systemctl stop my_script.service</code></strong></li>
<li>查看服务状态：<strong><code v-pre>sudo systemctl status my_script.service</code></strong></li>
</ul>
<h2 id="sed命令" tabindex="-1"><a class="header-anchor" href="#sed命令" aria-hidden="true">#</a> sed命令</h2>
<p><code v-pre>sed</code> 命令用于在 Shell 中对文本文件进行替换和编辑操作。以下是 <code v-pre>sed</code> 命令的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sed</span> <span class="token punctuation">[</span>options<span class="token punctuation">]</span> <span class="token string">'command'</span> <span class="token function">file</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>options</code> 是一些可选的命令行选项，<code v-pre>command</code> 是要执行的 <code v-pre>sed</code> 命令，<code v-pre>file</code> 是要处理的文件名。</p>
<p><code v-pre>sed</code> 命令支持许多不同的命令，以下是一些常用的命令：</p>
<ul>
<li><code v-pre>s/regexp/replacement/g</code>：用 <code v-pre>replacement</code> 替换匹配到的 <code v-pre>regexp</code>。</li>
<li><code v-pre>d</code>：删除匹配到的行。</li>
<li><code v-pre>p</code>：打印匹配到的行。</li>
<li><code v-pre>i</code>：在匹配到的行之前插入新行。</li>
<li><code v-pre>a</code>：在匹配到的行之后添加新行。</li>
<li><code v-pre>r</code>：读取文件并将其内容附加到匹配到的行。</li>
<li><code v-pre>w</code>：将匹配到的行写入到另一个文件中。</li>
<li><code v-pre>y/source/dest/</code>：将 <code v-pre>source</code> 中的字符替换为 <code v-pre>dest</code> 中的字符。</li>
</ul>
<p>例如，以下 <code v-pre>sed</code> 命令将替换 <code v-pre>file.txt</code> 中的所有 <code v-pre>foo</code> 为 <code v-pre>bar</code> 并将结果打印到终端：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sed</span> <span class="token string">'s/foo/bar/g'</span> file.txt
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>可以使用 <code v-pre>sed</code> 命令来添加新行</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sed</span> <span class="token parameter variable">-i</span> <span class="token string">'/pattern/a new line'</span> file.txt
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>pattern</code> 是要查找的模式，<code v-pre>new line</code> 是要添加的新行内容，<code v-pre>file.txt</code> 是要处理的文件名。该命令将在 <code v-pre>file.txt</code> 中查找包含 <code v-pre>pattern</code> 的行，并在其后面添加一行 <code v-pre>new line</code>。</p>
<p>使用 <code v-pre>sed</code> 命令来删除匹配到的行的语法如下：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sed</span> <span class="token string">'/pattern/d'</span> file.txt
<span class="token function">sed</span> <span class="token string">'5d'</span> file.txt
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p>其中，<code v-pre>pattern</code> 是要匹配的模式，<code v-pre>file.txt</code> 是要处理的文件名。该命令将在 <code v-pre>file.txt</code> 中查找包含 <code v-pre>pattern</code> 的行，并删除这些行。第二个命令是删除第五行</p>
<h2 id="sort" tabindex="-1"><a class="header-anchor" href="#sort" aria-hidden="true">#</a> Sort</h2>
<p><code v-pre>sort</code> 命令用于在 Linux 中对文本文件进行排序。以下是 <code v-pre>sort</code> 命令的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">sort</span> <span class="token punctuation">[</span>options<span class="token punctuation">]</span> <span class="token function">file</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>options</code> 是一些可选的命令行选项，<code v-pre>file</code> 是要排序的文件名。</p>
<p><code v-pre>sort</code> 命令支持许多不同的选项，以下是一些常用的选项：</p>
<ul>
<li><code v-pre>r</code>：反向排序。</li>
<li><code v-pre>n</code>：按数字顺序排序。</li>
<li><code v-pre>u</code>：去重排序，仅输出不同的行。</li>
<li><code v-pre>k</code>：按指定字段进行排序。</li>
<li><code v-pre>t</code>：指定字段分隔符。</li>
</ul>
<p><code v-pre>sort</code> 命令非常有用，可以帮助开发人员处理文本文件相关的任务，提高代码的可读性和可维护性。</p>
<h2 id="wget" tabindex="-1"><a class="header-anchor" href="#wget" aria-hidden="true">#</a> wget</h2>
<p><code v-pre>wget</code> 命令用于在 Shell 中下载文件。以下是 <code v-pre>wget</code> 命令的基本语法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">wget</span> <span class="token punctuation">[</span>options<span class="token punctuation">]</span> url
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>其中，<code v-pre>options</code> 是一些可选的命令行选项，<code v-pre>url</code> 是要下载的文件的 URL。</p>
<p><code v-pre>wget</code> 命令支持许多不同的选项，以下是一些常用的选项：</p>
<ul>
<li><code v-pre>O</code>：指定下载文件的名称。</li>
<li><code v-pre>q</code>：安静模式，不输出任何信息。</li>
<li><code v-pre>c</code>：继续下载未完成的文件。</li>
<li><code v-pre>r</code>：递归下载。</li>
<li><code v-pre>np</code>：不下载父级链接。</li>
<li><code v-pre>nH</code>：不创建主机名目录。</li>
</ul>
<p>例如，以下命令将下载 URL 为 <code v-pre>http://example.com/file.zip</code> 的文件并将其保存为 <code v-pre>myfile.zip</code>：</p>
<div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>wget -O myfile.zip &lt;http://example.com/file.zip>

</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="定时脚本" tabindex="-1"><a class="header-anchor" href="#定时脚本" aria-hidden="true">#</a> 定时脚本</h2>
<ol>
<li>
<p>输入**<code v-pre>crontab -e</code><strong>命令以编辑当前用户的</strong><code v-pre>cron</code>**表。这将打开一个文本编辑器，您可以在其中添加或修改定时任务。</p>
</li>
<li>
<p>在编辑器中，添加一行来定义您的定时任务。这一行应包含五个时间字段，后跟要执行的命令或脚本。时间字段的顺序如下：</p>
<ul>
<li>分钟（0-59）</li>
<li>小时（0-23）</li>
<li>月份的第几天（1-31）</li>
<li>月份（1-12）</li>
<li>星期几（0-7，其中0和7都表示星期日）</li>
</ul>
<p>例如，如果您想要每天早上9点运行名为**<code v-pre>my_script.sh</code>**的脚本，您应该添加以下行（假设脚本位于您的主目录中）：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">0</span> <span class="token number">9</span> * * * /bin/bash /path/to/your/script/my_script.sh
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>如果要定时一次，如每两小时执行一次</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">0</span> */2 * * * /bin/bash /path/to/your/script/my_script.sh
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>保存并关闭编辑器。**<code v-pre>cron</code><strong>将自动加载更新后的</strong><code v-pre>cron</code>**表，并按照您定义的时间间隔执行Shell脚本。</p>
</li>
</ol>
<p>在某些Linux系统（如某些Docker容器和轻量级发行版）中，**<code v-pre>cron</code><strong>和</strong><code v-pre>crontab</code><strong>命令可能未安装。在这种情况下，您需要手动安装</strong><code v-pre>cron</code><strong>包。以下是在Debian或Ubuntu系统上安装</strong><code v-pre>cron</code>**的方法：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">apt-get</span> update
<span class="token function">apt-get</span> <span class="token function">install</span> <span class="token function">cron</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p>对于CentOS或RHEL系统：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>yum <span class="token function">install</span> cronie
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></div></template>


