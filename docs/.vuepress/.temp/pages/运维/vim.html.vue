<template><div><p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/vim-vi-workmodel.png" alt="img"></p>
<table>
<thead>
<tr>
<th>命令</th>
<th>功能</th>
</tr>
</thead>
<tbody>
<tr>
<td>[Ctrl] + [f]</td>
<td>屏幕『向下』移动一页，相当于 [Page Down]按键 (常用)</td>
</tr>
<tr>
<td>[Ctrl] + [b]</td>
<td>屏幕『向上』移动一页，相当于 [Page Up] 按键 (常用)</td>
</tr>
<tr>
<td>0 或功能键[Home]</td>
<td>这是数字『 0 』：移动到这一行的最前面字符处 (常用)</td>
</tr>
<tr>
<td>$ 或功能键[End]</td>
<td>移动到这一行的最后面字符处(常用)</td>
</tr>
<tr>
<td>G</td>
<td>移动到这个档案的最后一行(常用)</td>
</tr>
<tr>
<td>gg</td>
<td>移动到这个档案的第一行，相当于 1G 啊！ (常用)</td>
</tr>
<tr>
<td>n</td>
<td>n 为数字。光标向下移动 n 行(常用)</td>
</tr>
<tr>
<td>/word</td>
<td>向光标之下寻找一个名称为 word 的字符串。例如要在档案内搜寻 vbird 这个字符串，就输入 /vbird 即可！ (常用)</td>
</tr>
<tr>
<td>:n1,n2s/word1/word2/g</td>
<td>n1 与 n2 为数字。在第 n1 与 n2 行之间寻找 word1 这个字符串，并将该字符串取代为 word2 ！举例来说，在 100 到 200 行之间搜寻 vbird 并取代为 VBIRD 则： 『:100,200s/vbird/VBIRD/g』。(常用)</td>
</tr>
<tr>
<td><strong>:1,$s/word1/word2/g</strong> 或 <strong>:%s/word1/word2/g</strong></td>
<td>从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！(常用)</td>
</tr>
<tr>
<td><strong>:1,$s/word1/word2/gc</strong> 或 <strong>:%s/word1/word2/gc</strong></td>
<td>从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 (confirm) 是否需要取代！(常用)</td>
</tr>
<tr>
<td>dd</td>
<td>删除游标所在的那一整行(常用)</td>
</tr>
<tr>
<td>ndd</td>
<td>n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 (常用)</td>
</tr>
<tr>
<td>yy</td>
<td>复制游标所在的那一行(常用)</td>
</tr>
<tr>
<td>nyy</td>
<td>n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行(常用)</td>
</tr>
<tr>
<td>p, P</td>
<td>p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！ 举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？ 那么原本的第 20 行会被推到变成 30 行。 (常用)</td>
</tr>
<tr>
<td>u</td>
<td>复原前一个动作。(常用)</td>
</tr>
<tr>
<td>[Ctrl]+r</td>
<td>重做上一个动作。(常用)</td>
</tr>
<tr>
<td>.</td>
<td>不要怀疑！这就是小数点！意思是重复前一个动作的意思。 如果你想要重复删除、重复贴上等等动作，按下小数点『.』就好了！ (常用)</td>
</tr>
</tbody>
</table>
</div></template>


