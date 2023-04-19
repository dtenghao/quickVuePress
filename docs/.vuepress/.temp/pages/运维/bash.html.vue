<template><div><h1 id="which" tabindex="-1"><a class="header-anchor" href="#which" aria-hidden="true">#</a> which</h1>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">which</span> bash指令
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>该指令可以查看指令“bash”的绝对路径。</p>
<h1 id="man" tabindex="-1"><a class="header-anchor" href="#man" aria-hidden="true">#</a> man</h1>
<p>man属于线上查询</p>
<p>查询指令的使用方法与参数说明</p>
<h1 id="查看历史记录" tabindex="-1"><a class="header-anchor" href="#查看历史记录" aria-hidden="true">#</a> 查看历史记录</h1>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">cat</span> ~/.bash_history	
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>可以查看以往所使用的命令。</p>
<p>注意，文件中记录的是前一次登陆以前所执行过的指令，而至于这一次登陆所执行的指令都被暂存在内存中，当你成功的登出系统后，该指令记忆才会记录到.bash_history当中！</p>
<hr>
<h1 id="别名设置" tabindex="-1"><a class="header-anchor" href="#别名设置" aria-hidden="true">#</a> 别名设置</h1>
<h2 id="编写临时别称" tabindex="-1"><a class="header-anchor" href="#编写临时别称" aria-hidden="true">#</a> 编写临时别称</h2>
<p>输入<code v-pre>alias</code>可以直接查看当前系统中有哪些别名，设置别名，可以输入</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">alias</span> <span class="token assign-left variable">lm</span><span class="token operator">=</span><span class="token string">'ls-al'</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>以后输入<code v-pre>lm</code>就会执行<code v-pre>ls-al</code>了，不过这只是暂时的，退出当前shell 就无法使用了。</p>
<h2 id="编写特定用户别称" tabindex="-1"><a class="header-anchor" href="#编写特定用户别称" aria-hidden="true">#</a> 编写特定用户别称</h2>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">vim</span> ~/.bashrc
<span class="token comment"># 将别称写入</span>
<span class="token comment"># 重新调用</span>
<span class="token builtin class-name">source</span> ~/.bashrc
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="编写系统级别称" tabindex="-1"><a class="header-anchor" href="#编写系统级别称" aria-hidden="true">#</a> 编写系统级别称</h2>
<p>与用户级编写过程相同，只是在<code v-pre>/etc/profile</code>中写入</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">vim</span> /etc/profile
<span class="token builtin class-name">source</span> /etc/profile
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="type" tabindex="-1"><a class="header-anchor" href="#type" aria-hidden="true">#</a> type</h1>
<p>输入<code v-pre>man bash提供的命令</code>，就可以查看命令的使用文档。</p>
<p>使用<code v-pre>type 命令</code>就可以查看该命令是内置在bash当中，还是来自外部指令。</p>
<h1 id="换行进行编辑" tabindex="-1"><a class="header-anchor" href="#换行进行编辑" aria-hidden="true">#</a> 换行进行编辑</h1>
<p>在需要换行的位置打印<code v-pre>/</code>，再敲击回车即可</p>
<h1 id="组合键" tabindex="-1"><a class="header-anchor" href="#组合键" aria-hidden="true">#</a> 组合键</h1>
<p><code v-pre>ctrl + u/ctrl + k</code>  从光标处向前（向后）删除指令符</p>
<p><code v-pre>ctrl + a/ctrl + e</code>  让光标移动到整个指令符的最前面（最后面）</p>
<h1 id="shell-变量" tabindex="-1"><a class="header-anchor" href="#shell-变量" aria-hidden="true">#</a> shell 变量</h1>
<p><code v-pre>mail</code>指令会主动的取用<code v-pre>MAIL</code>这个变量。</p>
<p>不同用户的<code v-pre>MAIL</code>变量值是不同的，比如用户vbird，他取得变量值就是<code v-pre>/var/spool/mail/vbird</code></p>
<hr>
<p>变量内容若有空白字符可使用双引号“”或单引号''将变量内容结合起来</p>
<p><strong>区别：</strong></p>
<p>双引号内的特殊字符如$等，可以保有原本的特性。</p>
<p>单引号内的特殊字符则仅为一般字符（纯文本）</p>
<p>在一串指令的执行中，还需要借由其他额外的指令所提供的信息时，可以用反单引号。</p>
<hr>
<p>如果该变量需要在其他子程序执行，则需要以export来使变量变成环境变量<code v-pre>export 变量名</code></p>
<p>取消变量的方法为使用unset：<code v-pre>unset 变量名称</code>，例如取消<code v-pre>myname</code>的设置：<code v-pre>unset myname</code></p>
<hr>
<p>输入<code v-pre>env</code>，可以查看当前的环境变量与常见环境变量说明</p>
<hr>
<h1 id="指令搜索顺序" tabindex="-1"><a class="header-anchor" href="#指令搜索顺序" aria-hidden="true">#</a> 指令搜索顺序</h1>
<ol>
<li>以相对/绝对路径执行指令，例如“/bin/ls”或“./ls”；</li>
<li>由alias找到该指令来执行</li>
<li>由bash内置的（builtin）指令来执行；</li>
<li>通过$PATH这个变量的顺序搜寻到第一个指令来执行。</li>
</ol>
<h1 id="bash的进站与欢迎讯息" tabindex="-1"><a class="header-anchor" href="#bash的进站与欢迎讯息" aria-hidden="true">#</a> bash的进站与欢迎讯息</h1>
<p>可以将linux登录提示字符串写在/etc/issue中，比如可以返回系统的版本信息，当前时间等。</p>
<table>
<thead>
<tr>
<th>issue内的各代码意义</th>
</tr>
</thead>
<tbody>
<tr>
<td>\d 本地端时间的日期；</td>
</tr>
<tr>
<td>\l 显示第几个终端机接口；</td>
</tr>
<tr>
<td>\m 显示硬件的等级（i386/i486/i586/i686...）；</td>
</tr>
<tr>
<td>\n 显示主机的网络名称；</td>
</tr>
<tr>
<td>\O 显示domain name；</td>
</tr>
<tr>
<td>\r 操作系统的版本（相当于uname-r）;</td>
</tr>
<tr>
<td>\t 显示本地端时间的时间；</td>
</tr>
<tr>
<td>\S 操作系统的名称；</td>
</tr>
<tr>
<td>\v 操作系统的版本</td>
</tr>
</tbody>
</table>
<p>例：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token punctuation">\</span>S	（terminal:	<span class="token punctuation">\</span>l）
Date:	<span class="token punctuation">\</span>d	<span class="token punctuation">\</span>t 
Kernel	<span class="token punctuation">\</span>r	on	an	<span class="token punctuation">\</span>m 
Welcome<span class="token operator">!</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<p>欢迎信息或通知讯息可以写在/etc/motd中，这样当使用者（包括所有的一般账号与root）登录主机后，就会显示讯息。</p>
</div></template>


