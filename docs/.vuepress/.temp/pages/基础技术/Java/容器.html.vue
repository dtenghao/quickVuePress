<template><div><h1 id="iterable-接口" tabindex="-1"><a class="header-anchor" href="#iterable-接口" aria-hidden="true">#</a> Iterable 接口</h1>
<p>Iterable是一个超级接口，被Collection所继承。它只有一个方法：  <code v-pre>Iterator&lt;T&gt; iterator()</code> 即返回一个迭代器。</p>
<p>迭代器是一种设计模式，它是一个对象，它可以遍历并选择序列中的对象，而开发人员不需要了解该序列的底层结构。迭代器通常被称为**“轻量级”**对象，因为创建它的代价小。</p>
<p>iterator为Java中的迭代器对象，iterable接口里定义了返回iterator的方法，相当于对iterator的封装，同时实现了iterable接口的类（list、vector）可以支持for each循环。可使用<code v-pre>list.iterator()</code> 得到迭代器对象。</p>
<p>iterator功能比较简单，并且只能单向移动，使用next()获得序列中的下一个元素。 使用hasNext()检查序列中是否还有元素。使用remove()将迭代器新返回的元素删除。</p>
<hr>
<h1 id="collection-实现类" tabindex="-1"><a class="header-anchor" href="#collection-实现类" aria-hidden="true">#</a> Collection 实现类</h1>
<p>List 是Collection的子接口，最流行的实现类有Vector、ArrayList、LinkedList。</p>
<ol>
<li>
<h5 id="arraylist" tabindex="-1"><a class="header-anchor" href="#arraylist" aria-hidden="true">#</a> ArrayList</h5>
<p>ArrayLis是基于数组实现的List类，它封装了一个<em>动态的、增长的、允许再分配的</em>Object[ ]数组.它允许对元素进行快速随机访问</p>
<p>当从ArrayList的中间位置插入或者删除元素时，需要对数组进行复制、移动、代价比较高。因此，它<strong>适合随机查找和遍历</strong>，不适合插入和删除。</p>
<p>扩容方式（默认）增长50%，线程不安全</p>
</li>
<li>
<h5 id="vector" tabindex="-1"><a class="header-anchor" href="#vector" aria-hidden="true">#</a> Vector</h5>
<p>Vector与ArrayList一样，也是通过数组实现的，不同的是它<strong>支持线程的同步</strong>，即某一时刻只有一个线程能够写Vector，避免多线程同时写而引起的不一致性，但实现同步需要很高的花费，因此，访问它比访问ArrayList慢。所以现在已经不太常用了</p>
<p>扩容方式（默认）增长一倍，线程安全</p>
<p><strong>Stack</strong> 是Vector提供的一个子类，用于模拟栈这种数据结构(LIFO后进先出)</p>
</li>
<li>
<h5 id="linkedlist" tabindex="-1"><a class="header-anchor" href="#linkedlist" aria-hidden="true">#</a> LinkedList</h5>
<p>LinkedList是用<strong>链表结构</strong>存储数据的，很适合数据的<strong>动态插入和删除</strong>，随机访问和遍历速度比较慢。</p>
<p>另外，它还实现了Deque接口，专门用于操作表头和表尾元素，可以当作堆栈、队列和<strong>双向队列</strong>使用。</p>
</li>
</ol>
<hr>
<p>Set判断两个对象相同不是使用&quot;==&quot;运算符，而是<strong>根据equals方法</strong>。也就是说，我们在加入一个新元素的时候，如果这个新元素对象和Set中已有对象进行注意equals比较都返回false，则Set就会接受这个新元素对象，否则拒绝。</p>
<p>Set最流行的实现类有HashSet、TreeSet、LinkedHashSet（从HashSet继承而来）。</p>
<ol>
<li>
<h5 id="hashset" tabindex="-1"><a class="header-anchor" href="#hashset" aria-hidden="true">#</a> HashSet</h5>
<p>HashSet是Set接口的典型实现，HashSet使用HASH算法来存储集合中的元素，因此具有良好的存取和查找性能。当向HashSet集合中存入一个元素时，HashSet会调用该对象的 hashCode()方法来得到该对象的hashCode值，然后根据该HashCode值决定该对象在HashSet中的存储位置，如果hashCode()的返回值相等，则会调用equals()方法比较相等。</p>
</li>
<li>
<h5 id="treeset" tabindex="-1"><a class="header-anchor" href="#treeset" aria-hidden="true">#</a> TreeSet</h5>
<p>TreeSet是SortedSet接口的实现类，TreeSet可以确保集合元素处于排序状态.</p>
</li>
</ol>
<hr>
<p>Map不是collection的子接口或者实现类。Map是一个接口。</p>
<ol>
<li>
<h5 id="hashmap" tabindex="-1"><a class="header-anchor" href="#hashmap" aria-hidden="true">#</a> HashMap</h5>
<p>和HashSet集合不能保证元素的顺序一样，HashMap也不能保证key-value对的顺序。并且类似于HashSet判断两个key是否相等的标准一样。</p>
</li>
<li>
<p><strong>TreeMap</strong></p>
<p>TreeMap是一个红黑树结构，每个键值对都作为红黑树的一个节点。TreeMap存储键值对时，需要根据key对节点进行排序，TreeMap可以保证所有的key-value对处于有序状态。 同时，TreeMap也有两种排序方式：自然排序、定制排序。</p>
</li>
</ol>
</div></template>


