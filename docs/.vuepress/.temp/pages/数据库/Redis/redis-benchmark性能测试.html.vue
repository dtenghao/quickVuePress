<template><div><p><strong>redis-benchmark</strong>是一个官方自带压力测试工具</p>
<table>
<thead>
<tr>
<th>序号</th>
<th>选项</th>
<th>描述</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>-h</strong></td>
<td>指定服务器主机名</td>
<td>127.0.0.1</td>
</tr>
<tr>
<td>2</td>
<td><strong>-p</strong></td>
<td>指定服务器端口</td>
<td>6379</td>
</tr>
<tr>
<td>3</td>
<td><strong>-s</strong></td>
<td>指定服务器 socket</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td><strong>-c</strong></td>
<td>指定并发连接数</td>
<td>50</td>
</tr>
<tr>
<td>5</td>
<td><strong>-n</strong></td>
<td>指定请求数</td>
<td>10000</td>
</tr>
<tr>
<td>6</td>
<td><strong>-d</strong></td>
<td>以字节的形式指定 SET/GET 值的数据大小</td>
<td>2</td>
</tr>
<tr>
<td>7</td>
<td><strong>-k</strong></td>
<td>1=keep alive 0=reconnect</td>
<td>1</td>
</tr>
<tr>
<td>8</td>
<td><strong>-r</strong></td>
<td>SET/GET/INCR 使用随机 key, SADD 使用随机值</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td><strong>-P</strong></td>
<td>通过管道传输&lt;numreq&gt; 请求</td>
<td>1</td>
</tr>
<tr>
<td>10</td>
<td><strong>-q</strong></td>
<td>强制退出 redis。仅显示 query/sec 值</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td><strong>--csv</strong></td>
<td>以 CSV 格式输出</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td><strong>-l</strong></td>
<td>生成循环，永久执行测试</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td><strong>-t</strong></td>
<td>仅运行以逗号分隔的测试命令列表。</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td><strong>-I</strong></td>
<td>Idle 模式。仅打开 N 个 idle 连接并等待。</td>
<td></td>
</tr>
</tbody>
</table>
<p>运行命令：</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>redis-benchmark <span class="token parameter variable">-h</span> localhost <span class="token parameter variable">-p</span> <span class="token number">6379</span> <span class="token parameter variable">-c</span> <span class="token number">100</span> <span class="token parameter variable">-n</span> <span class="token number">100000</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>指定100个客户端共100000次请求</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926103722342.png" alt="image-20200926103722342"></p>
</div></template>


