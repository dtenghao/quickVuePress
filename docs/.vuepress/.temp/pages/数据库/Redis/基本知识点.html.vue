<template><div><h1 id="前言" tabindex="-1"><a class="header-anchor" href="#前言" aria-hidden="true">#</a> 前言</h1>
<p>redis默认有16个数据库</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926143728810.png" alt="image-20200926143728810"></p>
<p>默认使用的是第0个</p>
<p>可以使用select进行切换数据库</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926144021411.png" alt="image-20200926144021411"></p>
<p>使用命令<code v-pre>FLUSHDB</code>清空数据库</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926144453914.png" alt="image-20200926144453914"></p>
<hr>
<p>Redis是单线程的，是基于内存操作，CPU不是Redis性能瓶颈，Redis的瓶颈是根据机器的内存和网络带宽。</p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926154405818.png" alt="image-20200926154405818"></p>
<p>查看是否存在</p>
<hr>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>move name <span class="token number">1</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>将name数据移动到数据库1</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>EXPIRE name <span class="token number">10</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>10秒后删除</p>
<h1 id="五大数据类型" tabindex="-1"><a class="header-anchor" href="#五大数据类型" aria-hidden="true">#</a> 五大数据类型</h1>
<blockquote>
<p>Redis is an open source (BSD licensed), in-memory data structure store,  used as a database, cache and message broker. It supports data  structures such as                  strings, hashes, lists, sets, sorted sets with range  queries, bitmaps,  hyperloglogs, geospatial indexes with radius queries  and streams. Redis has built-in replication, Lua scripting, LRU  eviction, transactions and different levels of on-disk persistence, and  provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.</p>
</blockquote>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token builtin class-name">type</span> name
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>查看当前key的类型</p>
<h2 id="string" tabindex="-1"><a class="header-anchor" href="#string" aria-hidden="true">#</a> String</h2>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>APPEND name <span class="token string">"haha"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>If <code v-pre>key</code> already exists and is a string, this command appends the <code v-pre>value</code> at the              end of the string. If <code v-pre>key</code> does not exist it is created and set as an empty string</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926155338096.png" alt="image-20200926155338096"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926160052155.png" alt="image-20200926160052155"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926160311378.png" alt="image-20200926160311378"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926160444817.png" alt="image-20200926160444817"></p>
<hr>
<p>更多命令见https://redis.io/commands#</p>
<h2 id="list" tabindex="-1"><a class="header-anchor" href="#list" aria-hidden="true">#</a> List</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926162005556.png" alt="image-20200926162005556"></p>
<hr>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> LPOP list
<span class="token string">"three"</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> RPOP list
<span class="token string">"right"</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> LRANGE list <span class="token number">0</span> <span class="token parameter variable">-1</span>
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"two"</span>
<span class="token number">2</span><span class="token punctuation">)</span> <span class="token string">"one"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> LINDEX list <span class="token number">0</span>   <span class="token comment"># 通过下标获得 list 中的元素</span>
<span class="token string">"two"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<p>更多命令见https://redis.io/commands#</p>
<h2 id="set" tabindex="-1"><a class="header-anchor" href="#set" aria-hidden="true">#</a> Set</h2>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926174757035.png" alt="image-20200926174757035"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926174841526.png" alt="image-20200926174841526"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926175220066.png" alt="image-20200926175220066"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926175308080.png" alt="image-20200926175308080"></p>
<hr>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20200926180030963.png" alt="image-20200926180030963"></p>
<hr>
<p>更多命令见https://redis.io/commands#</p>
<h2 id="hash" tabindex="-1"><a class="header-anchor" href="#hash" aria-hidden="true">#</a> Hash</h2>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HSET myhash field1 <span class="token string">"hello"</span>
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HGET myhash field1
<span class="token string">"hello"</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HMSET myhash field1 <span class="token string">"eumenides"</span> field2 <span class="token string">"helloWorld"</span>
OK
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HMGET myhash field1 field2
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"eumenides"</span>
<span class="token number">2</span><span class="token punctuation">)</span> <span class="token string">"helloWorld"</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HGETALL myhash <span class="token comment"># Get all the fields and values in a hash</span>
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"field1"</span>
<span class="token number">2</span><span class="token punctuation">)</span> <span class="token string">"eumenides"</span>
<span class="token number">3</span><span class="token punctuation">)</span> <span class="token string">"field2"</span>
<span class="token number">4</span><span class="token punctuation">)</span> <span class="token string">"helloWorld"</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HDEL myhash field2
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> HVALS myhash
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"eumenides"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="zset" tabindex="-1"><a class="header-anchor" href="#zset" aria-hidden="true">#</a> Zset</h2>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZADD myset <span class="token number">1</span> one
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZADD myset <span class="token number">2</span> two <span class="token number">3</span> three
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">2</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZRANGE myset <span class="token number">0</span> <span class="token parameter variable">-1</span>
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"one"</span>
<span class="token number">2</span><span class="token punctuation">)</span> <span class="token string">"two"</span>
<span class="token number">3</span><span class="token punctuation">)</span> <span class="token string">"three"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZADD salary <span class="token number">2500</span> xiaohong
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZADD salary <span class="token number">5000</span> zhangsan
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZADD salary <span class="token number">500</span> eumenides
<span class="token punctuation">(</span>integer<span class="token punctuation">)</span> <span class="token number">1</span>
<span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> ZRANGEBYSCORE salary <span class="token parameter variable">-inf</span> +inf  <span class="token comment">#排序</span>
<span class="token number">1</span><span class="token punctuation">)</span> <span class="token string">"eumenides"</span>
<span class="token number">2</span><span class="token punctuation">)</span> <span class="token string">"xiaohong"</span>
<span class="token number">3</span><span class="token punctuation">)</span> <span class="token string">"zhangsan"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="设置密码" tabindex="-1"><a class="header-anchor" href="#设置密码" aria-hidden="true">#</a> 设置密码</h1>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>config get requirepass <span class="token comment"># 获得当前密码</span>
config <span class="token builtin class-name">set</span> requirepass <span class="token number">123456</span> <span class="token comment">#设置密码为123456</span>
auth <span class="token number">123456</span>  <span class="token comment">#登录</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="持久化" tabindex="-1"><a class="header-anchor" href="#持久化" aria-hidden="true">#</a> 持久化</h1>
<h2 id="rdb-redis-database" tabindex="-1"><a class="header-anchor" href="#rdb-redis-database" aria-hidden="true">#</a> rdb(redis database)</h2>
<p>Redis会单独创建（fork）一个子进程来进行持久化，会先将数据写入到一个临时文件中，待持久化过程都结束了，再用这个临时文件代替上次持久化好的文件。整个过程中，主进程是不进行任何IO操作的。这就确保了极高的性能。如果需要进行大规模数据的恢复，且对于数据恢复的完整性不是非常敏感，那RDB方式要比AOF方式更加高效。RDB的缺点是最后一次持久化后的数据可能丢失。我们默认的就是RDB，一般情况下不需要修改这个配置！</p>
<p>rdb保存的文件是dump.rdb 这都是我们的配置文件中快照中进行配置的！</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201028201503193.png" alt="image-20201028201503193"></p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201028201700357.png" alt="image-20201028201700357"></p>
<p>在真实生产环境中我们经常会手动备份rdb文件</p>
<blockquote>
<p>触发机制</p>
</blockquote>
<ol>
<li>save的规则满足的情况下，会自动触发rdb规则</li>
<li>执行flushall命令</li>
<li>退出redis</li>
<li>使用<code v-pre>save</code>命令</li>
</ol>
<h2 id="aof-append-only-file" tabindex="-1"><a class="header-anchor" href="#aof-append-only-file" aria-hidden="true">#</a> AOF(Append Only FIle)</h2>
<p>将我们的所有命令都记录下来，history，恢复的时候就把这个文件全部再执行一遍。</p>
<p>以日志的形式来记录每个写操作，将Redis执行过的所有指令记录下来（读操作不记录），只许追加文件但不可以改写文件，redis启动之初会读取该文件(appendonly.aof)重新构建数据，换言之，redis重启的话就根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/image-20201029091521969.png" alt="image-20201029091521969"></p>
<p>使用时仅需把<code v-pre>no</code>改为<code v-pre>yes</code></p>
<p>如果<code v-pre>appendonly.aof</code>出现问题，可以用<code v-pre>redis-check-aof</code>来修复文件</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>redis-check-aof <span class="token parameter variable">--fix</span> appendonly.aof
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>优点：</p>
<ol>
<li>每一次修改都同步，文件的完整性会更好！</li>
<li>每秒同步一次，可能会丢失一秒的数据</li>
</ol>
<p>缺点：</p>
<ol>
<li>相对于数据文件来说，aof远远大于rdb，修复的速度也比rdb慢！</li>
<li>Aof运行效率也要比rdb慢，所以我们redis默认的配置就是rdb持久化！</li>
</ol>
<h2 id="扩展" tabindex="-1"><a class="header-anchor" href="#扩展" aria-hidden="true">#</a> 扩展：</h2>
<ol>
<li>RDB持久化方式能够在指定的时间间隔内对你的数据进行快照存储</li>
<li>AOF持久化方式记录每次对服务器写的操作，当服务器重启的时候会重新执行这些命令来恢复原始的数据，AOF命令以Redis协议追加保存每次写的操作到文件末尾，Redis还能对AOF文件进行后台重写，使得AOF文件的体积不至于过大。</li>
<li>只做缓存，如果你只希望你的数据在服务器运行的时候存在，你也可以不使用任何持久化</li>
<li>同时开启两种持久化方式
<ul>
<li>在这种情况下，当Redis重启的时候会优先载入AOF文件来恢复原始的数据，因为在通常情况下AOF文件保存的数据集要比RDB文件保存的数据集要完整。</li>
<li>RDB的数据不实时，同时使用两者时服务器重启也只会找AOF文件，那要不要只是使用AOF呢？作者建议不要，因为RDB更适合用于备份数据库（AOF在不断变化不好备份），快速重启，而且不会有AOF可能潜在的Bug，留着作为一个万一的手段</li>
</ul>
</li>
<li>性能建议
<ul>
<li>因为RDB文件只用作后备用途，建议只在Slave上持久化RDB文件，而且只要15分钟备份一次就够了，只保留save 900 1 这条规则</li>
<li>如果Enable AOF，好处是在最恶劣的情况下也只会丢失不超过两秒数据，启动脚本较简单只load自己的AOF文件就可以了，代价一是带来了持续的IO，二是AOF rewrite的最后将rewrite过程中产生的新数据写到新文件造成的阻塞几乎是不可避免的。只要硬盘许可，应该尽量减少AOF rewrite的平吕，AOF重写的基础大小默认值64M太小了，可以设到5G以上。</li>
<li>如果不Enable AOF，仅靠Master-Slave Replication 实现高可用性也可以，能省掉一大笔IO，也减少了rewrite时带来的系统波动。代价是如果Master/Slave同时倒掉，会丢失十几分钟的数据，启动脚本也要比较两个Master/Slave中的RDB文件，载入较新的那个，微博就是这种架构。</li>
</ul>
</li>
</ol>
<h1 id="redis发布订阅" tabindex="-1"><a class="header-anchor" href="#redis发布订阅" aria-hidden="true">#</a> Redis发布订阅</h1>
<p>Redis发布订阅（pub/sub）是一种消息通信模式：发送者（pub）发送消息，订阅者（sub）接收消息。微信、微博、关注系统！</p>
<p>Redis客户端可以订阅任意数量的频道。</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/timg.jpg" alt="img"></p>
<p>下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/pubsub1.png" alt="img"></p>
<p>当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：</p>
<p><img src="https://raw.githubusercontent.com/0Eumenides/upic/main/2023/04/18/pubsub2.png" alt="img"></p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>SUBSCRIBE mychannle  <span class="token comment">#订阅频道mychannle</span>
PUBLISH mychannle “hello,dth” <span class="token comment"># 往频道mychannle发送消息"hello,dth"</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="redis主从复制" tabindex="-1"><a class="header-anchor" href="#redis主从复制" aria-hidden="true">#</a> Redis主从复制</h1>
<h2 id="概念" tabindex="-1"><a class="header-anchor" href="#概念" aria-hidden="true">#</a> 概念</h2>
<p>主从复制，是指将一台Redis服务器的数据，复制到其他的Redis服务器。前者称为主节点（master/leader），后者称为从节点（slave/follower）；数据的复制是单向的，只能由主节点到从节点。Master以写为主，Slave以读为主。</p>
<p>默认情况下，每台Redis服务器都是主节点；</p>
<p>且一个主节点可以有多个从节点（或没有从节点），但一个从节点只能有一个主节点。</p>
<p><strong>主从复制的作用主要包括：</strong></p>
<ol>
<li>数据冗余：主从复制实现了数据的热备份，是持久化之外的一种数据冗余方法。</li>
<li>故障恢复：当主节点出现问题时，可以由从节点提供服务，实现快速的故障恢复；实际上是一种服务的冗余。</li>
<li>负载均衡：在主从复制的基础上，配合读写分离，可以由主节点提供写服务，由从节点提供读服务（即写Redis数据时应用连接主节点，读Redis数据时应用连接从节点），分担服务器负载；尤其是在写少读多的场景下，通过多个从节点分担读负载，可以大大提高Redis服务器的并发量。</li>
<li>高可用（集群）基石：除了上述作用以外，主从复制还是哨兵和集群能够实施的基础，因此说主从复制是Redis高可用的基础。</li>
</ol>
<h2 id="环境配置" tabindex="-1"><a class="header-anchor" href="#环境配置" aria-hidden="true">#</a> 环境配置</h2>
<p>只配置从库，不用配置主库！</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token number">127.0</span>.0.1:637<span class="token operator"><span class="token file-descriptor important">9</span>></span> info replication	<span class="token comment"># 查看当前库的信息</span>
<span class="token comment"># Replication</span>
role:master		<span class="token comment"># 角色</span>
connected_slaves:0	<span class="token comment"># 从机数量</span>
master_replid:ae4d03b77278caa1c48262f216e1b516a7eff296
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>SLAVEOF <span class="token number">127.0</span>.0.1 <span class="token number">6379</span> <span class="token comment"># SLAVEOF host 6379 做该主机的从机</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>真实的从主配置应该在配置文件中配置，这样的话是永久的，这里使用命令，只是暂时的！</p>
<p>主机可以写，从机不能写只能读！主机中的所有信息和数据，都会自动被从机保存！</p>
<blockquote>
<p>复制原理</p>
</blockquote>
<p>Slave 启动成功连接到master后会发送一个sync同步命令</p>
<p>Master接到命令，启动后台的存盘进程，同时收集所有接收的用于修改数据集命令，在后台进程执行完毕之后，master将传送整个数据文件到slave，并完成一次完全同步。</p>
<p>==全量复制==：而slave服务在接收到数据库文件数据后，将其存盘并加载到内存中。</p>
<p>==增量复制==：Master继续将新的所有收集到的修改命令依次传给slave，完成同步。</p>
<p>但是只要重新连接master，一次完全同步（全量复制）将被自动执行！我们的数据一定可以在从机中看到！</p>
<hr>
<p>如果主机断开了连接，我们可以使用<code v-pre>SLAVEOF no one</code> 让自己变成主机！其他的节点就可以手动连接到最新的这个主节点（手动）！</p>
<h2 id="哨兵模式" tabindex="-1"><a class="header-anchor" href="#哨兵模式" aria-hidden="true">#</a> 哨兵模式</h2>
<p>主从切换技术的方法是：当主服务器宕机后，需要手动把一台从服务器切换为主服务器，这就需要人工干预，费时费力，还会造成一段时间内服务不可用，更多时候，我们优先考虑哨兵模式。Redis从2.8开始正式提供了Sentinel（哨兵）架构来解决这个问题。</p>
<p>哨兵模式是一种特殊的模式，首先Redis提供了哨兵的命令，哨兵是一个独立的进程，作为进程，它会独立运行。其原理是<strong>哨兵通过发送命令，等待Redis服务器响应，从而监控运行多个Redis实例</strong></p>
<p>假设主服务器宕机，哨兵1先检测到这个结果，系统并不会马上进行failover过程，仅仅是哨兵1主观的认为主服务器不可用，这个现象称为<strong>主观下线</strong>。当后面的哨兵也检测到主服务器不可用，并且数量达到一定值时，那么哨兵之间就会进行一次投票，投票的结果由一个哨兵发起，进行failover[故障转移]操作。切换成功后，就会通过发布订阅模式，让各个哨兵把自己监控的从服务器实现切换主机，这个过程称为<strong>客观下线</strong></p>
<blockquote>
<p>测试！</p>
</blockquote>
<ol>
<li>
<p>新建哨兵配置文件sentinel.conf，写入配置</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment"># sentinel monitor 被监控的名称 host port 数字</span>
sentinel monitor myredis <span class="token number">127.0</span>.0.1 <span class="token number">6379</span> <span class="token number">2</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>数字</strong>表示多少个哨兵认为该主机宕机时代表该主机真的宕机了。</p>
</li>
<li>
<p>启动哨兵</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>redis-sentinel econfig/sentinel.conf
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
<p>当主机宕机后，哨兵会选出新的主机。如果旧主机回来了，只能归并到新的主机下，当作从机，这就是哨兵模式的规则！</p>
<p><strong>优点：</strong></p>
<ol>
<li>哨兵集群，基于主从复制模式，所有主从配置优点，它全有</li>
<li>主从可以切换，故障可以转移，系统的可用性就会更好</li>
<li>哨兵模式就是主从模式的升级，手动到自动，更加健壮！</li>
</ol>
<p><strong>缺点：</strong></p>
<ol>
<li>Redis不好在线扩容，集群容量一旦到达上限，在线扩容就十分麻烦！</li>
<li>实现哨兵模式的配置其实是很麻烦的，里面有很多选择！</li>
</ol>
<h1 id="redis缓存穿透和雪崩" tabindex="-1"><a class="header-anchor" href="#redis缓存穿透和雪崩" aria-hidden="true">#</a> Redis缓存穿透和雪崩</h1>
<p>Redis缓存的使用，极大的提升了应用程序的性能和效率，特别使数据查询方面。但同时，它也带来了一些问题。其中，最要害的问题，就是数据的一致性问题，从严格意义上讲，这个问题无解。如果对数据的一致性要求很高，那么就不能使用缓存。</p>
<p>另外的一些典型问题就是，缓存穿透、缓存雪崩和缓存击穿。目前，业界也都有比较流行的解决方案。</p>
<h2 id="缓存穿透-查不到" tabindex="-1"><a class="header-anchor" href="#缓存穿透-查不到" aria-hidden="true">#</a> 缓存穿透（查不到）</h2>
<blockquote>
<p>概念</p>
</blockquote>
<p>缓存穿透的概念很简单，用户想要查询一个数据，发现redis内存数据库没有，也就是缓存没有命中，于是向持久层数据库查询。发现也没有，于是本次查询失败。当用户很多的时候，缓存都没有命中，于是都去请求了持久层数据库，这会给持久层数据库造成很大的压力，这时候就相当于出现了缓存穿透。</p>
<blockquote>
<p>解决方案</p>
</blockquote>
<h3 id="布隆过滤器" tabindex="-1"><a class="header-anchor" href="#布隆过滤器" aria-hidden="true">#</a> 布隆过滤器</h3>
<p>布隆过滤器是一种数据结构，对所有可能查询的参数以hash形式存储，在控制层先进行校验，不符合则丢弃，从而避免了对底层存储系统的查询压力。</p>
<h3 id="缓存空对象" tabindex="-1"><a class="header-anchor" href="#缓存空对象" aria-hidden="true">#</a> 缓存空对象</h3>
<p>当存储层不命中后，即使返回的空对象也将其缓存起来，同时会设置一个过期时间，之后再访问这个数据将会从缓存中获取，保护了后端数据源。</p>
<p>但是这种方法会存在两个问题：</p>
<ol>
<li>如果空值能够被缓存起来，这就意味着缓存需要更多的空间存储更多的键，因为这当中可能会有很多的空值的键；</li>
<li>即使对空值设置了过期时间，还是会存在缓存层和存储层的数据会有一段时间窗口的不一致，这对于需要保持一致性的业务会有影响。</li>
</ol>
<h2 id="缓存击穿-量太大-缓存过期" tabindex="-1"><a class="header-anchor" href="#缓存击穿-量太大-缓存过期" aria-hidden="true">#</a> 缓存击穿（量太大，缓存过期！）</h2>
<blockquote>
<p>概述</p>
</blockquote>
<p>这里需要注意和缓存击穿的区别，缓存击穿，是指一个key非常热点，在不停的扛着大并发，大并发集中对这一个点进行访问，当这个key在失效的瞬间，持续的大并发就穿破缓存，直接请求数据库，就像在一个屏障上凿开了一个洞。</p>
<p>当某个key在过期的瞬间，有大量的请求并发访问，这类数据一般是热点数据，由于缓存过期，会同时访问数据库来查询最新数据，并且回写缓存，会导致数据库瞬间压力过大。</p>
<blockquote>
<p>解决方案</p>
</blockquote>
<p><strong>设置热点数据永不过期</strong></p>
<p>从缓存层面来看，没有设置过期时间，所以不会出现热点key过期后产生的问题。</p>
<p><strong>加互斥锁</strong></p>
<p>分布式锁：使用分布式锁，保证对于每个key同时只有一个线程去查询后端服务，其他线程没有获取分布式锁的权限，因此只需要等待即可。这个方式将高并发的压力转移到了分布式锁，因此对分布式锁的考验很大。</p>
<h2 id="缓存雪崩" tabindex="-1"><a class="header-anchor" href="#缓存雪崩" aria-hidden="true">#</a> 缓存雪崩</h2>
<blockquote>
<p>概念</p>
</blockquote>
<p>缓存雪崩，是指在某一个时间段，缓存集中过期失效。Redis宕机！于是所有的请求都会达到存储层，存储层的调用量会暴增，造成存储层挂掉的情况。</p>
<blockquote>
<p>解决方案</p>
</blockquote>
<p><strong>redis高可用</strong></p>
<p>这个思想的含义是，既然redis有可能挂掉，那我多增设几台redis，这样一台挂掉之后其他的还可以继续工作，其实就是搭建集群。</p>
<p><strong>限流降级</strong></p>
<p>这个解决方案的思想是，在缓存失效后，通过加锁或者队列来控制读数据库写缓存的线程数量。比如对某个key只允许一个线程查询数据和写缓存，其他线程等待。</p>
<p><strong>数据预热</strong></p>
<p>数据加热的含义就是在正式部署之前，先把可能的数据先预先访问一遍，这样部分可能大量访问的数据就会加载到缓存中。在即将发生大并发访问前手动触发加载缓存不同的key，设置不同的过期时间，让缓存失效的时间尽量均匀。</p>
</div></template>


