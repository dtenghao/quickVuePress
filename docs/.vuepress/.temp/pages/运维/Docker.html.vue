<template><div><h1 id="docker" tabindex="-1"><a class="header-anchor" href="#docker" aria-hidden="true">#</a> Docker</h1>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/OtSBhD.png" alt="OtSBhD"></p>
<table>
<thead>
<tr>
<th>特性</th>
<th>普通虚拟机</th>
<th>Docker</th>
</tr>
</thead>
<tbody>
<tr>
<td>跨平台</td>
<td>通常只能在桌面级系统运行，例如 Windows/Mac，无法在不带图形界面的服务器上运行</td>
<td>支持的系统非常多，各类 windows 和 Linux 都支持</td>
</tr>
<tr>
<td>性能</td>
<td>性能损耗大，内存占用高，因为是把整个完整系统都虚拟出来了</td>
<td>性能好，只虚拟软件所需运行环境，最大化减少没用的配置</td>
</tr>
<tr>
<td>自动化</td>
<td>需要手动安装所有东西</td>
<td>一个命令就可以自动部署好所需环境</td>
</tr>
<tr>
<td>稳定性</td>
<td>稳定性不高，不同系统差异大</td>
<td>稳定性好，不同系统都一样部署方式</td>
</tr>
</tbody>
</table>
<h1 id="常用命令" tabindex="-1"><a class="header-anchor" href="#常用命令" aria-hidden="true">#</a> 常用命令</h1>
<h2 id="docker-version" tabindex="-1"><a class="header-anchor" href="#docker-version" aria-hidden="true">#</a> <strong>docker version</strong></h2>
<p>查看版本信息</p>
<p>用法: <strong><code v-pre>docker version</code></strong></p>
<h2 id="docker-info" tabindex="-1"><a class="header-anchor" href="#docker-info" aria-hidden="true">#</a> <strong>docker info</strong></h2>
<p>查看docker的系统信息,包括镜像和容器的数量</p>
<p>用法: <strong><code v-pre>docker info</code></strong></p>
<h2 id="docker-search" tabindex="-1"><a class="header-anchor" href="#docker-search" aria-hidden="true">#</a> <strong>docker search</strong></h2>
<p>搜索镜像</p>
<p>示例：<strong><code v-pre>docker search mysql</code></strong></p>
<h2 id="docker-run" tabindex="-1"><a class="header-anchor" href="#docker-run" aria-hidden="true">#</a> <strong>docker run</strong></h2>
<p>运行一个新的容器</p>
<p>用法: <strong><code v-pre>docker run [OPTIONS] IMAGE [COMMAND] [ARG...]</code></strong></p>
<p>示例: <strong><code v-pre>docker run -it ubuntu /bin/bash</code></strong></p>
<h2 id="docker-start" tabindex="-1"><a class="header-anchor" href="#docker-start" aria-hidden="true">#</a> <strong>docker start</strong></h2>
<p>启动一个或多个已经被停止的容器</p>
<p>用法: <strong><code v-pre>docker start [OPTIONS] CONTAINER [CONTAINER...]</code></strong></p>
<p>示例: <strong><code v-pre>docker start my_container</code></strong></p>
<h2 id="docker-stop" tabindex="-1"><a class="header-anchor" href="#docker-stop" aria-hidden="true">#</a> <strong>docker stop</strong></h2>
<p>停止一个或多个正在运行的容器</p>
<p>用法: <strong><code v-pre>docker stop [OPTIONS] CONTAINER [CONTAINER...]</code></strong></p>
<p>示例: <strong><code v-pre>docker stop my_container</code></strong></p>
<h2 id="docker-restart" tabindex="-1"><a class="header-anchor" href="#docker-restart" aria-hidden="true">#</a> <strong>docker restart</strong></h2>
<p>重启一个或多个容器</p>
<p>用法: <strong><code v-pre>docker restart [OPTIONS] CONTAINER [CONTAINER...]</code></strong></p>
<p>示例: <strong><code v-pre>docker restart my_container</code></strong></p>
<h2 id="docker-ps" tabindex="-1"><a class="header-anchor" href="#docker-ps" aria-hidden="true">#</a> <strong>docker ps</strong></h2>
<p>列出所有正在运行的容器</p>
<p>用法: <strong><code v-pre>docker ps [OPTIONS]</code></strong></p>
<p>示例: <strong><code v-pre>docker ps -a</code></strong></p>
<h2 id="docker-images" tabindex="-1"><a class="header-anchor" href="#docker-images" aria-hidden="true">#</a> <strong>docker images</strong></h2>
<p>列出所有本地镜像</p>
<p>用法: <strong><code v-pre>docker images [OPTIONS] [REPOSITORY[:TAG]]</code></strong></p>
<p>示例: <strong><code v-pre>docker images</code></strong></p>
<h2 id="docker-rm" tabindex="-1"><a class="header-anchor" href="#docker-rm" aria-hidden="true">#</a> <strong>docker rm</strong></h2>
<p>删除一个或多个容器</p>
<p>用法: <strong><code v-pre>docker rm [OPTIONS] CONTAINER [CONTAINER...]</code></strong></p>
<p>示例: <strong><code v-pre>docker rm my_container</code></strong></p>
<h2 id="docker-rmi" tabindex="-1"><a class="header-anchor" href="#docker-rmi" aria-hidden="true">#</a> <strong>docker rmi</strong></h2>
<p>删除一个或多个镜像</p>
<p>用法: <strong><code v-pre>docker rmi [OPTIONS] IMAGE [IMAGE...]</code></strong></p>
<p>示例: <strong><code v-pre>docker rmi my_image</code></strong></p>
<h1 id="镜像命令" tabindex="-1"><a class="header-anchor" href="#镜像命令" aria-hidden="true">#</a> 镜像命令</h1>
<h2 id="docker-build" tabindex="-1"><a class="header-anchor" href="#docker-build" aria-hidden="true">#</a> <strong>docker build</strong></h2>
<p>通过 Dockerfile 构建镜像</p>
<p>用法：<strong><code v-pre>docker build [OPTIONS] PATH | URL | -</code></strong></p>
<p>示例：<strong><code v-pre>docker build -t my_image:latest .</code></strong></p>
<h2 id="docker-push" tabindex="-1"><a class="header-anchor" href="#docker-push" aria-hidden="true">#</a> <strong>docker push</strong></h2>
<p>将镜像推送到 Docker Hub</p>
<p>用法：<strong><code v-pre>docker push [OPTIONS] NAME[:TAG]</code></strong></p>
<p>示例：<strong><code v-pre>docker push my_image:latest</code></strong></p>
<h2 id="docker-pull" tabindex="-1"><a class="header-anchor" href="#docker-pull" aria-hidden="true">#</a> <strong>docker pull</strong></h2>
<p>从 Docker Hub 拉取镜像</p>
<p>用法：<strong><code v-pre>docker pull [OPTIONS] NAME[:TAG|@DIGEST]</code></strong></p>
<p>示例：<strong><code v-pre>docker pull my_image:latest</code></strong></p>
<h2 id="docker-tag" tabindex="-1"><a class="header-anchor" href="#docker-tag" aria-hidden="true">#</a> <strong>docker tag</strong></h2>
<p>给镜像打标签</p>
<p>用法：<strong><code v-pre>docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]</code></strong></p>
<p>示例：<strong><code v-pre>docker tag my_image:latest my_user/my_image:latest</code></strong></p>
<h2 id="docker-commit" tabindex="-1"><a class="header-anchor" href="#docker-commit" aria-hidden="true">#</a> docker commit</h2>
<p>用于将容器保存为新的镜像</p>
<p>用法：<code v-pre>docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]</code></p>
<p>示例：<code v-pre>docker commit my_container my_image:1.0</code></p>
<h1 id="容器命令" tabindex="-1"><a class="header-anchor" href="#容器命令" aria-hidden="true">#</a> 容器命令</h1>
<h2 id="docker-exec" tabindex="-1"><a class="header-anchor" href="#docker-exec" aria-hidden="true">#</a> <strong>docker exec</strong></h2>
<p>在正在运行的容器中执行命令</p>
<p>用法：<strong><code v-pre>docker exec [OPTIONS] CONTAINER COMMAND [ARG...]</code></strong></p>
<p>示例：<strong><code v-pre>docker exec -it my_container /bin/bash</code></strong></p>
<h2 id="docker-logs" tabindex="-1"><a class="header-anchor" href="#docker-logs" aria-hidden="true">#</a> <strong>docker logs</strong></h2>
<p>查看容器日志</p>
<p>用法：<strong><code v-pre>docker logs [OPTIONS] CONTAINER</code></strong></p>
<p>示例：<strong><code v-pre>docker logs my_container</code></strong></p>
<h2 id="docker-inspect" tabindex="-1"><a class="header-anchor" href="#docker-inspect" aria-hidden="true">#</a> <strong>docker inspect</strong></h2>
<p>查看容器详细信息</p>
<p>用法：<strong><code v-pre>docker inspect [OPTIONS] NAME|ID [NAME|ID...]</code></strong></p>
<p>示例：<strong><code v-pre>docker inspect my_container</code></strong></p>
<h2 id="docker-attach" tabindex="-1"><a class="header-anchor" href="#docker-attach" aria-hidden="true">#</a> <strong>docker attach</strong></h2>
<p>进入正在运行的容器</p>
<p>用法：<strong><code v-pre>docker attach [OPTIONS] CONTAINER</code></strong></p>
<p>示例：<strong><code v-pre>docker attach my_container</code></strong></p>
<h2 id="docker-cp" tabindex="-1"><a class="header-anchor" href="#docker-cp" aria-hidden="true">#</a> <strong>docker cp</strong></h2>
<p>在容器和主机之间复制文件</p>
<p>用法：<strong><code v-pre>docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|- docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH</code></strong></p>
<p>示例：<strong><code v-pre>docker cp my_container:/root/test.txt /tmp</code></strong></p>
<h1 id="dockerfile" tabindex="-1"><a class="header-anchor" href="#dockerfile" aria-hidden="true">#</a> Dockerfile</h1>
<p>Dockerfile 是一个文本文件，用于定义构建 Docker 镜像的步骤和规则。Dockerfile 中包含了一系列指令，Docker 使用这些指令按顺序执行，从基础镜像开始，逐步添加修改，最终生成一个新的镜像。以下是一些常用的 Dockerfile 指令及其用途：</p>
<ol>
<li><strong><code v-pre>FROM</code></strong>：指定基础镜像。这是 Dockerfile 的第一条指令，指明从哪个镜像开始构建。例如：<strong><code v-pre>FROM ubuntu:20.04</code></strong>。</li>
<li><strong><code v-pre>MAINTAINER</code></strong>：指定镜像的维护者信息。虽然这个指令已被弃用，但仍然可以使用。推荐使用 <strong><code v-pre>LABEL</code></strong> 代替。例如：<strong><code v-pre>MAINTAINER John Doe &lt;john.doe@example.com&gt;</code></strong>。</li>
<li><strong><code v-pre>LABEL</code></strong>：为镜像添加元数据，可以设置多个键值对。例如：<strong><code v-pre>LABEL maintainer=&quot;John Doe &lt;john.doe@example.com&gt;&quot; version=&quot;1.0&quot;</code></strong>。</li>
<li><strong><code v-pre>RUN</code></strong>：执行命令，并将结果提交为新的镜像层。常用于安装软件包、创建目录等操作。例如：<strong><code v-pre>RUN apt-get update &amp;&amp; apt-get install -y nginx</code></strong>。</li>
<li><strong><code v-pre>CMD</code></strong>：指定容器启动时默认执行的命令。一个 Dockerfile 中只能有一个 CMD 指令。如果指定了多个，只有最后一个会生效。如果在运行容器时提供了命令，则会覆盖 CMD 指令。例如：<strong><code v-pre>CMD [&quot;nginx&quot;, &quot;-g&quot;, &quot;daemon off;&quot;]</code></strong>。</li>
<li><strong><code v-pre>ENTRYPOINT</code></strong>：配置容器启动时执行的命令。与 CMD 类似，但 ENTRYPOINT 不会被 <strong><code v-pre>docker run</code></strong> 提供的命令覆盖。可以与 CMD 结合使用，CMD 中的命令会作为 ENTRYPOINT 的参数。例如：<strong><code v-pre>ENTRYPOINT [&quot;java&quot;, &quot;-jar&quot;]</code></strong> 和 <strong><code v-pre>CMD [&quot;my-app.jar&quot;]</code></strong>。</li>
<li><strong><code v-pre>WORKDIR</code></strong>：设置后续 RUN、CMD、ENTRYPOINT、COPY 和 ADD 指令的工作目录。例如：<strong><code v-pre>WORKDIR /app</code></strong>。</li>
<li><strong><code v-pre>COPY</code></strong>：将宿主机上的文件或目录复制到镜像中。例如：<strong><code v-pre>COPY ./app /app</code></strong>。</li>
<li><strong><code v-pre>ADD</code></strong>：与 COPY 类似，但可以解压 TAR 文件，或者从 URL 下载文件。例如：<strong><code v-pre>ADD https://example.com/myfile.tar.gz /app</code></strong>。</li>
<li><strong><code v-pre>EXPOSE</code></strong>：声明容器运行时监听的端口。注意，这不会自动映射端口到宿主机，需要使用 <strong><code v-pre>docker run -p</code></strong> 参数映射。例如：<strong><code v-pre>EXPOSE 80</code></strong>。</li>
<li><strong><code v-pre>VOLUME</code></strong>：在容器中创建挂载点。这允许将宿主机上的目录或文件挂载到容器中。例如：<strong><code v-pre>VOLUME /data</code></strong>。</li>
<li><strong><code v-pre>USER</code></strong>：指定后续 RUN、CMD 和 ENTRYPOINT 指令使用的用户。例如：<code v-pre>USER myuser</code>。</li>
<li><strong><code v-pre>ARG</code></strong>：定义构建参数。这些参数在构建过程中可以使用，也可以在运行时通过 <strong><code v-pre>-build-arg</code></strong> 参数设置。例如：<strong><code v-pre>ARG DEBIAN_FRONTEND=noninteractive</code></strong>。</li>
<li><strong><code v-pre>ENV</code></strong>：设置环境变量。这些变量将在容器运行时生效，也可以在构建过程中使用。例如：<strong><code v-pre>ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk</code></strong>。</li>
<li><strong><code v-pre>SHELL</code></strong>：指定后续 RUN 指令使用的默认 shell。例如：<strong><code v-pre>SHELL [&quot;/bin/bash&quot;, &quot;-c&quot;]</code></strong>。</li>
<li><strong><code v-pre>ONBUILD</code></strong>：为基础镜像设置触发器。当有其他镜像以当前镜像为基础镜像时，ONBUILD 指令将被执行。例如：<strong><code v-pre>ONBUILD RUN npm install</code></strong>。</li>
<li><strong><code v-pre>HEALTHCHECK</code></strong>：用于检查容器内服务的健康状况。可以指定一个命令，定期执行以检查服务是否正常运行。例如：<strong><code v-pre>HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:80/ || exit 1</code></strong>。</li>
<li><strong><code v-pre>STOPSIGNAL</code></strong>：设置停止容器时发送给容器内主进程的信号。例如：<strong><code v-pre>STOPSIGNAL SIGTERM</code></strong>。</li>
</ol>
<ul>
<li>使用 <strong><code v-pre>RUN</code></strong> 在构建过程中执行命令，例如安装依赖、创建文件等。</li>
<li>使用 <strong><code v-pre>CMD</code></strong> 设置容器默认行为，当用户没有提供特定命令时执行。</li>
<li>使用 <strong><code v-pre>ENTRYPOINT</code></strong> 将镜像作为可执行程序，接受用户提供的参数。可以与 <strong><code v-pre>CMD</code></strong> 结合使用，提供默认参数。</li>
</ul>
<p>要编写 Dockerfile，首先确定基础镜像，然后根据需求添加各种指令。一个典型的 Dockerfile 可能包括：</p>
<ul>
<li>选择基础镜像（FROM）</li>
<li>设置工作目录（WORKDIR）</li>
<li>复制或添加文件（COPY 或 ADD）</li>
<li>运行命令，例如安装依赖（RUN）</li>
<li>暴露端口（EXPOSE）</li>
<li>设置环境变量（ENV）</li>
<li>指定启动命令（CMD 或 ENTRYPOINT）</li>
</ul>
<p>以下是一个简单的示例：</p>
<p>要编写一个 Dockerfile 为 Python 项目安装依赖，可以参考以下步骤：</p>
<ol>
<li>选择一个基础镜像。通常，可以使用官方的 Python 镜像，例如 <strong><code v-pre>python:3.8</code></strong> 或 <strong><code v-pre>python:3.9</code></strong>。</li>
<li>设置工作目录，以便在容器中创建一个目录来存放项目文件。</li>
<li>复制 <strong><code v-pre>requirements.txt</code></strong> 文件到容器中的工作目录。</li>
<li>使用 <strong><code v-pre>RUN</code></strong> 指令安装 <strong><code v-pre>requirements.txt</code></strong> 中的依赖。</li>
<li>复制项目的其他文件到工作目录。</li>
<li>暴露需要的端口（如果有）。</li>
<li>设置项目的启动命令。</li>
</ol>
<div class="language-docker line-numbers-mode" data-ext="docker"><pre v-pre class="language-docker"><code><span class="token comment"># 基础镜像</span>
<span class="token instruction"><span class="token keyword">FROM</span> python:3.9</span>

<span class="token comment"># 设置工作目录</span>
<span class="token instruction"><span class="token keyword">WORKDIR</span> /app</span>

<span class="token comment"># 复制 requirements.txt</span>
<span class="token instruction"><span class="token keyword">COPY</span> requirements.txt .</span>

<span class="token comment"># 安装依赖</span>
<span class="token instruction"><span class="token keyword">RUN</span> pip install --no-cache-dir -r requirements.txt</span>

<span class="token comment"># 复制项目文件</span>
<span class="token instruction"><span class="token keyword">COPY</span> . .</span>

<span class="token comment"># 暴露端口（如果有）</span>
<span class="token instruction"><span class="token keyword">EXPOSE</span> 8000</span>

<span class="token comment"># 启动命令</span>
<span class="token instruction"><span class="token keyword">CMD</span> [<span class="token string">"python"</span>, <span class="token string">"app.py"</span>]</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>根据你的项目情况进行调整，例如使用不同的 Python 版本、暴露其他端口或者使用不同的启动命令。确保在 Dockerfile 所在目录运行 <strong><code v-pre>docker build</code></strong> 命令时，<strong><code v-pre>requirements.txt</code></strong> 和其他项目文件也在该目录中。</p>
<h1 id="目录挂载" tabindex="-1"><a class="header-anchor" href="#目录挂载" aria-hidden="true">#</a> 目录挂载</h1>
<ul>
<li>Docker运行后，本地修改了项目代码需要同步到docker容器中</li>
<li>容器中产生的log文件、数据库备份文件需要在本地同步保存，避免容器删除后导致文件的丢失</li>
</ul>
<p>几种挂载方式：</p>
<ul>
<li><code v-pre>bind mount</code> 可以将宿主机目录直接映射到容器内，适合挂载代码目录和配置文件。例如：<code v-pre>docker run -v /host/path:/container/path image_name</code>，其中 <code v-pre>/host/path</code> 是宿主机目录，<code v-pre>/container/path</code> 是容器内目录。</li>
<li><code v-pre>volume</code> 由 Docker 创建和管理，创建在宿主机上，因此删除容器时不会丢失数据。它们更高效，适用于存储数据库数据。例如：<strong><code v-pre>docker run -v volume_name:/container/path image_name</code></strong>，其中 <code v-pre>volume_name</code> 是卷的名称，<code v-pre>/container/path</code> 是容器内目录。</li>
<li><code v-pre>tmpfs mount</code> 适合存储临时文件，将数据存储在宿主机内存中。不适合多个容器共享。例如：<strong><code v-pre>docker run --mount type=tmpfs,destination=/container/path image_name</code></strong>，其中 <code v-pre>/container/path</code> 是容器内目录。</li>
</ul>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/RILtQt.png" alt="RILtQt"></p>
<h1 id="多容器通信" tabindex="-1"><a class="header-anchor" href="#多容器通信" aria-hidden="true">#</a> 多容器通信</h1>
<p>创建一个自定义网络</p>
<div class="language-docker line-numbers-mode" data-ext="docker"><pre v-pre class="language-docker"><code>docker network create my-network
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>接下来，运行第一个容器（例如，一个名为**<code v-pre>container-1</code><strong>的Redis容器）并将其连接到</strong><code v-pre>my-network</code>**网络：</p>
<div class="language-docker line-numbers-mode" data-ext="docker"><pre v-pre class="language-docker"><code>docker run -d --name container-1 --net my-network redis
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>然后，运行第二个容器（例如，一个名为**<code v-pre>container-2</code><strong>的Python容器），并将其连接到</strong><code v-pre>my-network</code>**网络：</p>
<div class="language-docker line-numbers-mode" data-ext="docker"><pre v-pre class="language-docker"><code>docker run -it --name container-2 --net my-network python bash
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>现在，这两个容器都连接到了同一个网络**<code v-pre>my-network</code><strong>。在</strong><code v-pre>container-2</code><strong>内部，可以使用</strong><code v-pre>container-1</code><strong>的容器名作为其主机名来访问</strong><code v-pre>container-1</code>**提供的服务。</p>
<div class="language-python line-numbers-mode" data-ext="py"><pre v-pre class="language-python"><code><span class="token keyword">import</span> redis

<span class="token comment"># 使用container-1的名称作为主机名</span>
<span class="token comment"># 如果容器连接到网络时设置了--network-alias参数，则使用这个别名进行访问</span>
client <span class="token operator">=</span> redis<span class="token punctuation">.</span>Redis<span class="token punctuation">(</span>host<span class="token operator">=</span><span class="token string">'container-1'</span><span class="token punctuation">,</span> port<span class="token operator">=</span><span class="token number">6379</span><span class="token punctuation">)</span>

client<span class="token punctuation">.</span><span class="token builtin">set</span><span class="token punctuation">(</span><span class="token string">'key'</span><span class="token punctuation">,</span> <span class="token string">'value'</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>client<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">'key'</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="docker-compose" tabindex="-1"><a class="header-anchor" href="#docker-compose" aria-hidden="true">#</a> Docker-Compose</h1>
<p>当项目需要多个依赖时，需要管理的容器就更加多，可以使用 docker-compose 把项目的多个服务集合到一起，一键运行，统一管理。</p>
<p>要把项目依赖的多个服务集合到一起，需要编写一个<code v-pre>docker-compose.yml</code>文件，描述依赖哪些服务。</p>
<div class="language-yaml line-numbers-mode" data-ext="yml"><pre v-pre class="language-yaml"><code><span class="token key atrule">version</span><span class="token punctuation">:</span> <span class="token string">"3.7"</span>  <span class="token comment"># 指定docker-compose文件的版本为3.7</span>

<span class="token key atrule">services</span><span class="token punctuation">:</span>  <span class="token comment"># 定义服务部分</span>
  <span class="token key atrule">app</span><span class="token punctuation">:</span>  <span class="token comment"># 定义名为app的服务</span>
    <span class="token key atrule">build</span><span class="token punctuation">:</span> ./  <span class="token comment"># 从当前目录（包含Dockerfile）构建app服务的镜像</span>
    <span class="token key atrule">ports</span><span class="token punctuation">:</span>  <span class="token comment"># 定义端口映射</span>
      <span class="token punctuation">-</span> 80<span class="token punctuation">:</span><span class="token number">8080</span>  <span class="token comment"># 将容器内的8080端口映射到宿主机的80端口</span>
    <span class="token key atrule">volumes</span><span class="token punctuation">:</span>  <span class="token comment"># 定义数据卷</span>
      <span class="token punctuation">-</span> ./<span class="token punctuation">:</span>/app  <span class="token comment"># 将当前目录（宿主机）挂载到容器的/app目录</span>
    <span class="token key atrule">environment</span><span class="token punctuation">:</span>  <span class="token comment"># 定义环境变量</span>
      <span class="token punctuation">-</span> TZ=Asia/Shanghai  <span class="token comment"># 设置时区为亚洲/上海</span>
  <span class="token key atrule">redis</span><span class="token punctuation">:</span>  <span class="token comment"># 定义名为redis的服务</span>
    <span class="token key atrule">image</span><span class="token punctuation">:</span> redis<span class="token punctuation">:</span>5.0.13  <span class="token comment"># 指定使用redis:5.0.13镜像</span>
    <span class="token key atrule">volumes</span><span class="token punctuation">:</span>  <span class="token comment"># 定义数据卷</span>
      <span class="token punctuation">-</span> redis<span class="token punctuation">:</span>/data  <span class="token comment"># 将名为redis的数据卷挂载到容器的/data目录</span>
    <span class="token key atrule">environment</span><span class="token punctuation">:</span>  <span class="token comment"># 定义环境变量</span>
      <span class="token punctuation">-</span> TZ=Asia/Shanghai  <span class="token comment"># 设置时区为亚洲/上海</span>

<span class="token key atrule">volumes</span><span class="token punctuation">:</span>  <span class="token comment"># 定义数据卷部分</span>
  <span class="token key atrule">redis</span><span class="token punctuation">:</span>  <span class="token comment"># 定义名为redis的数据卷</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在<code v-pre>docker-compose.yml</code> 文件所在目录，执行：<code v-pre>docker-compose up</code>就可以跑起来了。加上<code v-pre>-d</code>参数可以在后台运行</p>
<p>要停止并删除所有服务，使用：<code v-pre>docker-compose down</code></p>
<h1 id="数据备份与迁移" tabindex="-1"><a class="header-anchor" href="#数据备份与迁移" aria-hidden="true">#</a> 数据备份与迁移</h1>
<p>如果是用<code v-pre>bind mount</code>直接把宿主机的目录挂进去容器，那迁移数据很方便，直接复制目录就好了</p>
<p>如果是用<code v-pre>volume</code>方式挂载的，由于数据是由容器创建和管理的，需要用特殊的方式把数据弄出来。</p>
<p>备份：</p>
<ul>
<li>运行一个 ubuntu 的容器，挂载需要备份的 volume 到容器，并且挂载宿主机目录到容器里的备份目录。</li>
<li>运行 tar 命令把数据压缩为一个文件</li>
<li>把备份文件复制到需要导入的机器</li>
</ul>
<p>导入：</p>
<ul>
<li>运行 ubuntu 容器，挂载容器的 volume，并且挂载宿主机备份文件所在目录到容器里</li>
<li>运行 tar 命令解压备份文件到指定目录</li>
</ul>
</div></template>


