<template><div><h1 id="maven项目的优势" tabindex="-1"><a class="header-anchor" href="#maven项目的优势" aria-hidden="true">#</a> maven项目的优势</h1>
<ol>
<li>
<p>减少包大小</p>
<p>使用maven构建的项目文件占用内存较小，因为maven项目是通过jar包坐标去jar包仓库寻找jar包的，jar包并不会存放在项目中。</p>
</li>
<li>
<p>项目一键构建</p>
<p>我们的项目，往往都要经历编译、测试、运行、打包、安装，部署等一系列过程。</p>
<p>而maven项目从编译、测试、运行、打包、安装、部署整个过程都交给maven进行管理，这个过程称为构建。</p>
</li>
</ol>
<h1 id="maven仓库的种类和彼此关系" tabindex="-1"><a class="header-anchor" href="#maven仓库的种类和彼此关系" aria-hidden="true">#</a> maven仓库的种类和彼此关系</h1>
<p>仓库分三类：本地仓库、远程仓库【私服】、中央仓库。</p>
<h1 id="maven目录结构" tabindex="-1"><a class="header-anchor" href="#maven目录结构" aria-hidden="true">#</a> maven目录结构</h1>
<p>maven 项目标准目录结构</p>
<p>src/main/java目录 	核心代码部分</p>
<p>src/main/resources	配置文件部分</p>
<p>src/test/java	测试代码部分</p>
<p>src/test/resources	测试配置文件</p>
<p>src/main/webapp	页面资源，js、css、图片等等</p>
<h1 id="maven常用命令" tabindex="-1"><a class="header-anchor" href="#maven常用命令" aria-hidden="true">#</a> maven常用命令</h1>
<table>
<thead>
<tr>
<th style="text-align:center">命令</th>
<th style="text-align:center">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">mvn clean</td>
<td style="text-align:center">清除已经编译好的文件夹target</td>
</tr>
<tr>
<td style="text-align:center">mvn compile</td>
<td style="text-align:center">编译项目，生成target文件夹</td>
</tr>
<tr>
<td style="text-align:center">mvn test</td>
<td style="text-align:center">将测试代码也一同编译</td>
</tr>
<tr>
<td style="text-align:center">mvn package</td>
<td style="text-align:center">编译项目并生成war(jar)包</td>
</tr>
<tr>
<td style="text-align:center">mvn install</td>
<td style="text-align:center">package+将生成的war(jar)文件复制到本地仓库中，其他项目可以使用这个jar包</td>
</tr>
</tbody>
</table>
<h1 id="maven-生命周期" tabindex="-1"><a class="header-anchor" href="#maven-生命周期" aria-hidden="true">#</a> maven 生命周期</h1>
</div></template>


