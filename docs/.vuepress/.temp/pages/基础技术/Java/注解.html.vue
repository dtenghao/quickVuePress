<template><div><h1 id="元注解" tabindex="-1"><a class="header-anchor" href="#元注解" aria-hidden="true">#</a> 元注解</h1>
<p>元注解顾名思义我们可以理解为注解的注解，它是作用在注解中，方便我们使用注解实现想要的功能。</p>
<h2 id="retention" tabindex="-1"><a class="header-anchor" href="#retention" aria-hidden="true">#</a> @Retention</h2>
<p>@Retention(RetentionPolicy.SOURCE)，注解仅存在于源码中，在class字节码文件中不包含</p>
<p>@Retention(RetentionPolicy.CLASS)， 默认的保留策略，注解会在class字节码文件中存在，但运行时无法获得</p>
<p>@Retention(RetentionPolicy.RUNTIME)， 注解会在class字节码文件中存在，在运行时可以通过反射获取到</p>
<hr>
<h2 id="target" tabindex="-1"><a class="header-anchor" href="#target" aria-hidden="true">#</a> @Target</h2>
<p>==@Target(ElementType.TYPE) 作用接口、类、枚举、注解==</p>
<p>@Target(ElementType.FIELD) 作用属性字段、枚举的常量</p>
<p>@Target(ElementType.METHOD) 作用方法</p>
<p>@Target(ElementType.PARAMETER) 作用方法参数</p>
<p>@Target(ElementType.CONSTRUCTOR) 作用构造函数</p>
<p>@Target(ElementType.LOCAL_VARIABLE)作用局部变量</p>
<p>@Target(ElementType.ANNOTATION_TYPE)作用于注解（@Retention注解中就使用该属性）</p>
<p>@Target(ElementType.PACKAGE) 作用于包</p>
<p>@Target(ElementType.TYPE_PARAMETER) 作用于类型泛型，即泛型方法、泛型类、泛型接口 （jdk1.8加入）</p>
<p>@Target(ElementType.TYPE_USE) 类型使用.可以用于标注任意类型除了 class （jdk1.8加入）</p>
<p>一般比较常用的是ElementType.TYPE类型</p>
<hr>
<h2 id="documented" tabindex="-1"><a class="header-anchor" href="#documented" aria-hidden="true">#</a> @Documented</h2>
<p>Document的英文意思是文档。它的作用是能够将注解中的元素包含到 Javadoc 中去。</p>
<hr>
<h2 id="inherited" tabindex="-1"><a class="header-anchor" href="#inherited" aria-hidden="true">#</a> @Inherited</h2>
<p>@Inherited注解了的注解修饰了一个父类，如果他的子类没有被其他注解修饰，则它的子类也继承了父类的注解。</p>
<hr>
<h2 id="repeatable" tabindex="-1"><a class="header-anchor" href="#repeatable" aria-hidden="true">#</a> @Repeatable</h2>
<p>Repeatable的英文意思是可重复的。顾名思义说明被这个元注解修饰的注解可以同时作用一个对象多次，但是每次作用注解又可以代表不同的含义。</p>
<hr>
<h1 id="注解的属性" tabindex="-1"><a class="header-anchor" href="#注解的属性" aria-hidden="true">#</a> 注解的属性</h1>
<p>注解的属性类似与类中定义的属性，定义方法如下：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Repeatable</span><span class="token punctuation">(</span><span class="token class-name">People</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span>
<span class="token annotation punctuation">@Retention</span><span class="token punctuation">(</span><span class="token class-name">RetentionPolicy</span><span class="token punctuation">.</span><span class="token constant">RUNTIME</span><span class="token punctuation">)</span>
<span class="token annotation punctuation">@Target</span><span class="token punctuation">(</span><span class="token class-name">ElementType</span><span class="token punctuation">.</span><span class="token constant">TYPE</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token annotation punctuation">@interface</span> <span class="token class-name">Game</span> <span class="token punctuation">{</span>
    <span class="token class-name">String</span> <span class="token function">value</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">default</span> <span class="token string">""</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>String 是返回类型，value是属性名，<code v-pre>default &quot;&quot;</code>表示默认为空字符串</p>
<hr>
<h1 id="注解的本质" tabindex="-1"><a class="header-anchor" href="#注解的本质" aria-hidden="true">#</a> 注解的本质</h1>
<p>注解的本质就是一个Annotation接口</p>
<p>注解本身就是Annotation接口的子接口，<strong>也就是说注解中其实是可以有属性和方法，但是接口中的属性都是static final的，对于注解来说没什么意义，而我们定义接口的方法就相当于注解的属性，也就对应了前面说的为什么注解只有属性成员变量，其实他就是接口的方法，这就是为什么成员变量会有括号</strong>，不同于接口我们可以在注解的括号中给成员变量赋值。</p>
<hr>
<h1 id="注解成员变量赋值" tabindex="-1"><a class="header-anchor" href="#注解成员变量赋值" aria-hidden="true">#</a> 注解成员变量赋值</h1>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token annotation punctuation">@Documented</span>
<span class="token annotation punctuation">@Inherited</span>
<span class="token annotation punctuation">@Retention</span><span class="token punctuation">(</span><span class="token class-name">RetentionPolicy</span><span class="token punctuation">.</span><span class="token constant">RUNTIME</span><span class="token punctuation">)</span>
<span class="token annotation punctuation">@Target</span><span class="token punctuation">(</span><span class="token class-name">ElementType</span><span class="token punctuation">.</span><span class="token constant">TYPE</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token annotation punctuation">@interface</span> <span class="token class-name">MyTestAnnotation</span> <span class="token punctuation">{</span>
    <span class="token class-name">String</span> <span class="token function">name</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">default</span> <span class="token string">"mao"</span><span class="token punctuation">;</span>
    <span class="token keyword">int</span> <span class="token function">age</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">default</span> <span class="token number">18</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token annotation punctuation">@MyTestAnnotation</span><span class="token punctuation">(</span>name <span class="token operator">=</span> <span class="token string">"father"</span><span class="token punctuation">,</span>age <span class="token operator">=</span> <span class="token number">50</span><span class="token punctuation">)</span>
<span class="token keyword">public</span> <span class="token keyword">class</span> <span class="token class-name">Father</span> <span class="token punctuation">{</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><hr>
<h1 id="获取注解属性" tabindex="-1"><a class="header-anchor" href="#获取注解属性" aria-hidden="true">#</a> 获取注解属性</h1>
<p>依靠反射获取注解的属性，主要有三个基本的方法。</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code> <span class="token doc-comment comment">/**是否存在对应 Annotation 对象*/</span>
<span class="token keyword">public</span> <span class="token keyword">boolean</span> <span class="token function">isAnnotationPresent</span><span class="token punctuation">(</span><span class="token class-name">Class</span><span class="token generics"><span class="token punctuation">&lt;</span><span class="token operator">?</span> <span class="token keyword">extends</span> <span class="token class-name">Annotation</span><span class="token punctuation">></span></span> annotationClass<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token class-name">GenericDeclaration</span><span class="token punctuation">.</span><span class="token keyword">super</span><span class="token punctuation">.</span><span class="token function">isAnnotationPresent</span><span class="token punctuation">(</span>annotationClass<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

 <span class="token doc-comment comment">/**获取 Annotation 对象*/</span>
<span class="token keyword">public</span> <span class="token generics"><span class="token punctuation">&lt;</span><span class="token class-name">A</span> <span class="token keyword">extends</span> <span class="token class-name">Annotation</span><span class="token punctuation">></span></span> <span class="token class-name">A</span> <span class="token function">getAnnotation</span><span class="token punctuation">(</span><span class="token class-name">Class</span><span class="token generics"><span class="token punctuation">&lt;</span><span class="token class-name">A</span><span class="token punctuation">></span></span> annotationClass<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token class-name">Objects</span><span class="token punctuation">.</span><span class="token function">requireNonNull</span><span class="token punctuation">(</span>annotationClass<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token punctuation">(</span><span class="token class-name">A</span><span class="token punctuation">)</span> <span class="token function">annotationData</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>annotations<span class="token punctuation">.</span><span class="token function">get</span><span class="token punctuation">(</span>annotationClass<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
 <span class="token doc-comment comment">/**获取所有 Annotation 对象数组*/</span>   
<span class="token keyword">public</span> <span class="token class-name">Annotation</span><span class="token punctuation">[</span><span class="token punctuation">]</span> <span class="token function">getAnnotations</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token class-name">AnnotationParser</span><span class="token punctuation">.</span><span class="token function">toArray</span><span class="token punctuation">(</span><span class="token function">annotationData</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>annotations<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>    
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>应用示例：</p>
<div class="language-java line-numbers-mode" data-ext="java"><pre v-pre class="language-java"><code><span class="token keyword">public</span> <span class="token keyword">class</span> test <span class="token punctuation">{</span>
   <span class="token keyword">public</span> <span class="token keyword">static</span> <span class="token keyword">void</span> <span class="token function">main</span><span class="token punctuation">(</span><span class="token class-name">String</span><span class="token punctuation">[</span><span class="token punctuation">]</span> args<span class="token punctuation">)</span> <span class="token keyword">throws</span> <span class="token class-name">NoSuchMethodException</span> <span class="token punctuation">{</span>

        <span class="token doc-comment comment">/**
         * 获取类注解属性
         */</span>
        <span class="token class-name">Class</span><span class="token generics"><span class="token punctuation">&lt;</span><span class="token class-name">Father</span><span class="token punctuation">></span></span> fatherClass <span class="token operator">=</span> <span class="token class-name">Father</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">;</span>
        <span class="token keyword">boolean</span> annotationPresent <span class="token operator">=</span> fatherClass<span class="token punctuation">.</span><span class="token function">isAnnotationPresent</span><span class="token punctuation">(</span><span class="token class-name">MyTestAnnotation</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">if</span><span class="token punctuation">(</span>annotationPresent<span class="token punctuation">)</span><span class="token punctuation">{</span>
            <span class="token class-name">MyTestAnnotation</span> annotation <span class="token operator">=</span> fatherClass<span class="token punctuation">.</span><span class="token function">getAnnotation</span><span class="token punctuation">(</span><span class="token class-name">MyTestAnnotation</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span>annotation<span class="token punctuation">.</span><span class="token function">name</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span>annotation<span class="token punctuation">.</span><span class="token function">age</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>

        <span class="token doc-comment comment">/**
         * 获取方法注解属性
         */</span>
        <span class="token keyword">try</span> <span class="token punctuation">{</span>
            <span class="token class-name">Field</span> age <span class="token operator">=</span> fatherClass<span class="token punctuation">.</span><span class="token function">getDeclaredField</span><span class="token punctuation">(</span><span class="token string">"age"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">boolean</span> annotationPresent1 <span class="token operator">=</span> age<span class="token punctuation">.</span><span class="token function">isAnnotationPresent</span><span class="token punctuation">(</span><span class="token class-name">Age</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">if</span><span class="token punctuation">(</span>annotationPresent1<span class="token punctuation">)</span><span class="token punctuation">{</span>
                <span class="token class-name">Age</span> annotation <span class="token operator">=</span> age<span class="token punctuation">.</span><span class="token function">getAnnotation</span><span class="token punctuation">(</span><span class="token class-name">Age</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
                <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span>annotation<span class="token punctuation">.</span><span class="token function">value</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>

            <span class="token class-name">Method</span> play <span class="token operator">=</span> <span class="token class-name">PlayGame</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">.</span><span class="token function">getDeclaredMethod</span><span class="token punctuation">(</span><span class="token string">"play"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">if</span> <span class="token punctuation">(</span>play<span class="token operator">!=</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
                <span class="token class-name">People</span> annotation2 <span class="token operator">=</span> play<span class="token punctuation">.</span><span class="token function">getAnnotation</span><span class="token punctuation">(</span><span class="token class-name">People</span><span class="token punctuation">.</span><span class="token keyword">class</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
                <span class="token class-name">Game</span><span class="token punctuation">[</span><span class="token punctuation">]</span> value <span class="token operator">=</span> annotation2<span class="token punctuation">.</span><span class="token function">value</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
                <span class="token keyword">for</span> <span class="token punctuation">(</span><span class="token class-name">Game</span> game <span class="token operator">:</span> value<span class="token punctuation">)</span> <span class="token punctuation">{</span>
                    <span class="token class-name">System</span><span class="token punctuation">.</span>out<span class="token punctuation">.</span><span class="token function">println</span><span class="token punctuation">(</span>game<span class="token punctuation">.</span><span class="token function">value</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
                <span class="token punctuation">}</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">}</span> <span class="token keyword">catch</span> <span class="token punctuation">(</span><span class="token class-name">NoSuchFieldException</span> e<span class="token punctuation">)</span> <span class="token punctuation">{</span>
            e<span class="token punctuation">.</span><span class="token function">printStackTrace</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


