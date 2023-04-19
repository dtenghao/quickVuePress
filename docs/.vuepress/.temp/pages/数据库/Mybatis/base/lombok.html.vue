<template><div><p>使用步骤：</p>
<ol>
<li>在IDEA中安装Lombok插件</li>
<li>在项目中导入lombok的jar包</li>
</ol>
<div class="language-xml line-numbers-mode" data-ext="xml"><pre v-pre class="language-xml"><code><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dependency</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>groupId</span><span class="token punctuation">></span></span>org.projectlombok<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>groupId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>artifactId</span><span class="token punctuation">></span></span>lombok<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>artifactId</span><span class="token punctuation">></span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>version</span><span class="token punctuation">></span></span>1.16.20<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>version</span><span class="token punctuation">></span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dependency</span><span class="token punctuation">></span></span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="3">
<li>在实体类上加注解即可！</li>
</ol>
<hr>
<p>lombok提供许多注解</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Getter</span> and <span class="token annotation punctuation">@Setter</span>
<span class="token annotation punctuation">@FieldNameConstants</span>
<span class="token annotation punctuation">@ToString</span>
<span class="token annotation punctuation">@EqualsAndHashCode</span>
<span class="token annotation punctuation">@AllArgsConstructor</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@RequiredArgsConstructor</span> and <span class="token annotation punctuation">@NoArgsConstructor</span>
<span class="token annotation punctuation">@Log</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@Log4j</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@Log4j2</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@Slf4j</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@XSlf4j</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@CommonsLog</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@JBossLog</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@Flogger</span><span class="token punctuation">,</span> <span class="token annotation punctuation">@CustomLog</span>
<span class="token annotation punctuation">@Data</span>
<span class="token annotation punctuation">@Builder</span>
<span class="token annotation punctuation">@SuperBuilder</span>
<span class="token annotation punctuation">@Singular</span>
<span class="token annotation punctuation">@Delegate</span>
<span class="token annotation punctuation">@Value</span>
<span class="token annotation punctuation">@Accessors</span>
<span class="token annotation punctuation">@Wither</span>
<span class="token annotation punctuation">@With</span>
<span class="token annotation punctuation">@SneakyThrows</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-text line-numbers-mode" data-ext="text"><pre v-pre class="language-text"><code>@Data:自动生成getter、setter、tostring、hashcode、equals
@AllArgsConstructor：自动生成有参构造器
@NoArgsConstructor:生成无参构造器
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


