<template><div><h1 id="starters命名规范" tabindex="-1"><a class="header-anchor" href="#starters命名规范" aria-hidden="true">#</a> starters命名规范</h1>
<p>所有的官方starters命名方式都是<code v-pre>spring-boot-starter-*</code>，*是具体的技术。</p>
<p>自定义的starter，应<code v-pre>*-spring-boot-starter</code></p>
<h1 id="默认扫描器basepackage" tabindex="-1"><a class="header-anchor" href="#默认扫描器basepackage" aria-hidden="true">#</a> 默认扫描器basepackage</h1>
<p>springboot的主启动类所在的package就是扫描器的basepackage。</p>
<h1 id="热部署" tabindex="-1"><a class="header-anchor" href="#热部署" aria-hidden="true">#</a> 热部署</h1>
<ol>
<li>在项目的配置文件<code v-pre>pom.xml</code>中引入依赖</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependencies</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
        <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.springframework.boot<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
        <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>spring-boot-devtools<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
        <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>optional</span><span class="token punctuation">></span></span>true<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>optional</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependencies</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="2">
<li>
<p>在设置中<code v-pre>build,Execution,deployment-&gt;Compiler</code>中勾选<code v-pre>Build project automatically</code></p>
</li>
<li>
<p>按<code v-pre>ctrl+shift+alt+/</code>，回车，勾选<code v-pre>compiler.automake.allow.when.app.running</code></p>
</li>
<li>
<p>重启项目</p>
</li>
</ol>
<h1 id="配置文件" tabindex="-1"><a class="header-anchor" href="#配置文件" aria-hidden="true">#</a> 配置文件</h1>
<p>springboot 启动会扫描以下位置的application.properties或者application.yml文件作为Springboot的默认配置文件</p>
<p>-file:./config/</p>
<p>-file:./  	项目的根路径，如果当前的项目有父工程，配置文件要放在父工程的根路径</p>
<p>-classpath:/config/</p>
<p>-classpath:/</p>
<p><strong>优先级由高到低</strong></p>
<hr>
<p>如果需要修改配置文件名称，可以通过以下参数来指定配置文件的名称，myproject是配置文件名</p>
<div class="language-linux line-numbers-mode" data-ext="linux"><pre v-pre class="language-linux"><code>$java -jar myproject.jar --spring.config.name=myproject
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>如果需要修改位置：</p>
<div class="language-linux line-numbers-mode" data-ext="linux"><pre v-pre class="language-linux"><code>$java -jar myporject.jar
--spring.config.location=path
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="yaml语法" tabindex="-1"><a class="header-anchor" href="#yaml语法" aria-hidden="true">#</a> YAML语法</h1>
<p>yml是YAML（YAML Ain't Markup Language）语言的文件，以数据为中心，比properties、xml等更适合做配置文件</p>
<ul>
<li>yml和xml相比，少了一些结构化的代码，使数据更直接，一目了然</li>
<li>相比properties文件更简洁</li>
</ul>
<div class="language-yaml line-numbers-mode" data-ext="yml"><pre v-pre class="language-yaml"><code><span class="token key atrule">yaml</span><span class="token punctuation">:</span>
  <span class="token key atrule">str</span><span class="token punctuation">:</span> 字符串不需要加双引号
  <span class="token key atrule">num</span><span class="token punctuation">:</span> <span class="token number">666</span>
  <span class="token key atrule">Dnum</span><span class="token punctuation">:</span> <span class="token number">666.88</span>
  <span class="token key atrule">birth</span><span class="token punctuation">:</span> 2000/08/05 12<span class="token punctuation">:</span><span class="token datetime number">23:34</span>
<span class="token comment">#  list:</span>
<span class="token comment">#    - one</span>
<span class="token comment">#    - two</span>
  <span class="token key atrule">list</span><span class="token punctuation">:</span> <span class="token punctuation">[</span>one<span class="token punctuation">,</span>two<span class="token punctuation">]</span>   <span class="token comment">#数组的两种形式</span>
  <span class="token key atrule">map</span><span class="token punctuation">:</span> <span class="token punctuation">{</span><span class="token key atrule">key1</span><span class="token punctuation">:</span> value1<span class="token punctuation">,</span> <span class="token key atrule">key2</span><span class="token punctuation">:</span> value2<span class="token punctuation">}</span> <span class="token comment">#键值对</span>
  <span class="token key atrule">users</span><span class="token punctuation">:</span>             <span class="token comment">#对象</span>
    <span class="token punctuation">-</span> <span class="token key atrule">name</span><span class="token punctuation">:</span> zhangsan
      <span class="token key atrule">salary</span><span class="token punctuation">:</span> <span class="token number">123.8</span>
    <span class="token punctuation">-</span> <span class="token key atrule">name</span><span class="token punctuation">:</span> lisi
      <span class="token key atrule">salary</span><span class="token punctuation">:</span> <span class="token number">123</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>以空格的缩进程度来控制层级关系。空格的个数并不重要，大小写敏感。</p>
<p>在属性类中，前缀不可以驼峰模式，只能用羊肉串模式，但是在yml中是可以用驼峰模式来配置的。</p>
<hr>
<p>先编写配置bean，再写yml配置文件</p>
<p>引入插件</p>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.springframework.boot<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>spring-boot-configuration-processor<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>optional</span><span class="token punctuation">></span></span>true<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>optional</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>可以在编写yml时获得代码提示。</p>
<h1 id="data注解" tabindex="-1"><a class="header-anchor" href="#data注解" aria-hidden="true">#</a> @Data注解</h1>
<p>过多的getter和setter会增大代码量。</p>
<p>可以引入依赖</p>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
   <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.projectlombok<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
   <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>lombok<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
   <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>1.16.20<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>再在类上添加@Data注解，他会帮我们加入setter、getter、tostring等方法</p>
<h1 id="属性绑定" tabindex="-1"><a class="header-anchor" href="#属性绑定" aria-hidden="true">#</a> 属性绑定</h1>
<p>编写yml文件</p>
<div class="language-yaml line-numbers-mode" data-ext="yml"><pre v-pre class="language-yaml"><code><span class="token key atrule">person</span><span class="token punctuation">:</span>
  <span class="token key atrule">name</span><span class="token punctuation">:</span> 邓腾浩
  <span class="token key atrule">age</span><span class="token punctuation">:</span> <span class="token number">20</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>再在需要绑定的类上加上<code v-pre>@ConfigurationProperties(prefix = &quot;person&quot;)</code>，注意字段名与属性名要一一对应</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Component</span>
<span class="token annotation punctuation">@ConfigurationProperties</span><span class="token punctuation">(</span>prefix <span class="token operator">=</span> <span class="token string">"person"</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">Person</span> <span class="token punctuation">{</span>
    <span class="token keyword">private</span> <span class="token class-name">String</span> name<span class="token punctuation">;</span>
    <span class="token keyword">private</span> <span class="token keyword">int</span> age<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<p>当然在寻找<code v-pre>person</code>前缀时默认从<code v-pre>application.yml</code>中查找，我们也可以指定去其他的配置文件中查找：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@PropertySource</span><span class="token punctuation">(</span>value <span class="token operator">=</span> <span class="token string">"classpath:person.properties"</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><p>这样我们就会去resources目录下的<strong>person.properties</strong>配置文件查找person前缀</p>
<h1 id="属性绑定的校验" tabindex="-1"><a class="header-anchor" href="#属性绑定的校验" aria-hidden="true">#</a> 属性绑定的校验</h1>
<p>引入依赖</p>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.hibernate<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>hibernate-validator<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>5.2.0.Final<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>在属性类上加上注解<code v-pre>@Validated</code>，然后在需要校验的属性上加注解如<code v-pre>@NotNull</code>、<code v-pre>@Max(20)</code>、<code v-pre>@Email</code></p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@NotNull</span><span class="token punctuation">(</span>message<span class="token operator">=</span><span class="token string">"名字不能为空"</span><span class="token punctuation">)</span>
<span class="token keyword">private</span> <span class="token class-name">String</span> userName<span class="token punctuation">;</span>
<span class="token annotation punctuation">@Max</span><span class="token punctuation">(</span>value<span class="token operator">=</span><span class="token number">120</span><span class="token punctuation">,</span>message<span class="token operator">=</span><span class="token string">"年龄最大不能c过120"</span><span class="token punctuation">)</span>
<span class="token keyword">private</span> <span class="token keyword">int</span> age<span class="token punctuation">;</span>
<span class="token annotation punctuation">@Email</span><span class="token punctuation">(</span>message<span class="token operator">=</span><span class="token string">"邮箱格式错误"</span><span class="token punctuation">)</span>
<span class="token keyword">private</span> <span class="token class-name">String</span> email<span class="token punctuation">;</span>


空检查
<span class="token annotation punctuation">@Null</span>       验证对象是否为<span class="token keyword">null</span>
<span class="token annotation punctuation">@NotNull</span>    验证对象是否不为<span class="token keyword">null</span><span class="token punctuation">,</span> 无法查检长度为<span class="token number">0</span>的字符串
<span class="token annotation punctuation">@NotBlank</span>   检查约束字符串是不是<span class="token class-name">Null</span>还有被<span class="token class-name">Trim</span>的长度是否大于<span class="token number">0</span><span class="token punctuation">,</span>只对字符串<span class="token punctuation">,</span>且会去掉前后空格<span class="token punctuation">.</span>
<span class="token annotation punctuation">@NotEmpty</span>   检查约束元素是否为<span class="token constant">NULL</span>或者是<span class="token class-name">EMPTY<span class="token punctuation">.</span>
    
Booelan</span>检查
<span class="token annotation punctuation">@AssertTrue</span>     验证 <span class="token class-name">Boolean</span> 对象是否为 <span class="token boolean">true</span>  
<span class="token annotation punctuation">@AssertFalse</span>    验证 <span class="token class-name">Boolean</span> 对象是否为 <span class="token boolean">false</span>  
    
长度检查
<span class="token annotation punctuation">@Size</span><span class="token punctuation">(</span>min<span class="token operator">=</span><span class="token punctuation">,</span> max<span class="token operator">=</span><span class="token punctuation">)</span> 验证对象（<span class="token class-name">Array</span><span class="token punctuation">,</span><span class="token class-name">Collection</span><span class="token punctuation">,</span><span class="token class-name">Map</span><span class="token punctuation">,</span><span class="token class-name">String</span>）长度是否在给定的范围之内  
<span class="token annotation punctuation">@Length</span><span class="token punctuation">(</span>min<span class="token operator">=</span><span class="token punctuation">,</span> max<span class="token operator">=</span><span class="token punctuation">)</span> string is between min and max included<span class="token punctuation">.</span>
 
 
日期检查
<span class="token annotation punctuation">@Past</span>       验证 <span class="token class-name">Date</span> 和 <span class="token class-name">Calendar</span> 对象是否在当前时间之前  
<span class="token annotation punctuation">@Future</span>     验证 <span class="token class-name">Date</span> 和 <span class="token class-name">Calendar</span> 对象是否在当前时间之后  
<span class="token annotation punctuation">@Pattern</span>    验证 <span class="token class-name">String</span> 对象是否符合正则表达式的规则
 
 
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>等等
除此以外，我们还可以自定义一些数据校验规则
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>当需要校验内部类时，如名为Security的内部类，则需要添加注解</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Valid</span>
<span class="token keyword">private</span> <span class="token keyword">final</span> <span class="token class-name">Security</span> security <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">Security</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="value" tabindex="-1"><a class="header-anchor" href="#value" aria-hidden="true">#</a> @Value</h1>
<table>
<thead>
<tr>
<th style="text-align:center">Feature</th>
<th style="text-align:center">@ConfigurationProperties</th>
<th style="text-align:center">@Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">松散绑定</td>
<td style="text-align:center">Yes</td>
<td style="text-align:center">Limit</td>
</tr>
<tr>
<td style="text-align:center">元数据支持</td>
<td style="text-align:center">Yes</td>
<td style="text-align:center">No</td>
</tr>
<tr>
<td style="text-align:center">SpEL表达式</td>
<td style="text-align:center">No</td>
<td style="text-align:center">Yes</td>
</tr>
<tr>
<td style="text-align:center">复杂类型绑定</td>
<td style="text-align:center">Yes</td>
<td style="text-align:center">No</td>
</tr>
<tr>
<td style="text-align:center">校验</td>
<td style="text-align:center">Yes</td>
<td style="text-align:center">No</td>
</tr>
<tr>
<td style="text-align:center">应用场景</td>
<td style="text-align:center">Boot里面属性多个绑定</td>
<td style="text-align:center">单个属性的绑定</td>
</tr>
</tbody>
</table>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Value</span><span class="token punctuation">(</span><span class="token string">"${acme.first-name}"</span><span class="token punctuation">)</span>
<span class="token keyword">private</span> <span class="token class-name">String</span> firstName<span class="token punctuation">;</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div></div></div><p>注解中必须羊肉串模式，配置文件中可以驼峰或羊肉串。</p>
<p>不支持绑定数组等复杂类型</p>
<p>不支持校验</p>
<h1 id="yaml文件的profile用法" tabindex="-1"><a class="header-anchor" href="#yaml文件的profile用法" aria-hidden="true">#</a> Yaml文件的profile用法</h1>
<p>根据环境不同创建不同的配置文件，命名方式如下：</p>
<p>运行项目前需要指定使用哪个配置，在Configuration-&gt;Environment-&gt;VM options中写入<code v-pre>-Dspring.profiles.active=配置名</code></p>
</div></template>


