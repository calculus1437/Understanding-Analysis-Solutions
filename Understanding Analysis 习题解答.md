
<style>
.markdown-preview.markdown-preview .admonition.question {
    background-color: #e3f2fd; /* 浅天蓝背景 */
    border-left-color: #2196f3; /* 深天蓝左边框 */
    color: #000000; /* 深蓝色文字 */
}
.markdown-preview.markdown-preview .admonition.question .admonition-title {
    background-color: #bbdefb; /* 标题栏稍微深一点的天蓝 */
    color: #0d47a1;
    border-bottom: 1px solid #90caf9;
}
</style>

[1.绝对值不等式的本质](#1)
[2.德·摩根律在无穷情况下的推广](#2)
[3.施罗德-伯恩斯坦双射定理](#10)
[4.二维可数集的构造](#3)
[5.极限平均值定理与反向情况下的反例](#4)
[6.实数几大基本定理的互证](#5)
[7.几何级数与 $\mathrm{p}$ 级数间的转换](#6)
[8.绝对收敛重排定理的证明](#7)
[9.压缩映射定理与不动点收敛问题](#8)
[10.线性柯西方程](#9)
[11.拓宽定义域来证明一致连续性](#11)
[12.区间分割的一致连续性](#12)
[13.利普希茨条件下的一致连续性](#13)
[14.连续性的拓扑特征](#14)
[15.连续延拓定理](#15)
[16.导函数极限定理](#16)

# 实数

## 习题 1.2 预备知识

!!! question "练习 1.2.1"
    (a) 证明 $\sqrt{3}$ 是无理数。类似的论证是否适用于证明 $\sqrt{6}$ 是无理数？

    (b) 如果我们尝试用定理1.1.1的证明来证明 $\sqrt{4}$ 是无理数，证明在何处会失效？

(a) 使用反证的方式。假设存在互素整数 $p,q$ 满足 $p/q=\sqrt{3}$，那么 $p^2=3q^2$，$p$ 是 $3$ 的倍数，因此 $q$ 也是 $3$ 的倍数，这与 $p,q$ 互素的假设矛盾。所以 $\sqrt{3}$ 是无理数。

$\sqrt{6}$ 可以用同样的方式证明。

(b) 使用同样的方式，得到 $p^2=4q^2$，但此时只能得到 $p$ 是 $2$ 的倍数，于是可得到 $q=1$，这样不会产生矛盾。

<br/>

!!! question "练习 1.2.2"
    判断以下哪些陈述正确地描述了集合的性质。对于任何错误的陈述，提供一个具体的例子说明该陈述不成立。

    (a) 如果 ${A}_{1} \supseteq  {A}_{2} \supseteq  {A}_{3} \supseteq  {A}_{4}\cdots$ 都是包含无限多个元素的集合，那么它们的交集 ${ \cap  }_{n = 1}^{\infty }{A}_{n}$ 也是无限的。

    (b) 如果 ${A}_{1} \supseteq  {A}_{2} \supseteq  {A}_{3} \supseteq  {A}_{4}\cdots$ 都是有限的、非空的实数集，那么它们的交集 ${ \cap  }_{n = 1}^{\infty }{A}_{n}$ 是有限且非空的。

    (c) $A \cap  \left( {B \cup  C}\right)  = \left( {A \cap  B}\right)  \cup  C$ .

    (d) $A \cap  \left( {B \cap  C}\right)  = \left( {A \cap  B}\right)  \cap  C$ .

    (e) $A \cap  \left( {B \cup  C}\right)  = \left( {A \cap  B}\right)  \cup  \left( {A \cap  C}\right)$ .

(a) 这是可能不正确的。例如定义

$$
A_n=\left\{x\in \mathbb{N}:x\geq n\right\}
$$

则有

$$
\displaystyle\bigcap_{n=1}^{\infty}{A_n}=\varnothing
$$

(b) 这是正确的。证明它的关键是找到一个元素 $x$ 使 $x\in \displaystyle\bigcap_{n=1}^{\infty}{A_n}$。

尝试从有限非空的定义入手。与 (a) 问的区别在于，本题中 $A_{n+1}$ 的元素个数总是不大于 $A_n$ 的元素个数的。所以，从限制元素个数的角度入手，对某一 $k\in \mathbb{Z^+}$，

$$
A_k=\left\{x_1,x_2,...,x_p\right\}
$$

不妨设 $\exists \ n\in \mathbb{Z^+}$ 使 $\forall\ i\in \left\{1,2,...,p\right\}$ 都有 $x_i\notin A_n$，此时 $A_n\subseteq A_k$， 所以 $A_n=\varnothing$，这与其非空的事实矛盾。所以对 $\forall\ n\in \mathbb{Z^+}$ 都 $\exists \ i\in \left\{1,2,...,p\right\}$ 使得 $x_i\in A_n$，这就证明了 $\displaystyle\bigcap_{n=1}^{\infty}{A_n}$ 的非空性，又有限集合的交集是有限的，故它是有限非空的。

(c) 错误的。事实上左侧表达的是 $x\in A\cap B$ 或 $x\in A\cap C$，右侧表达的是 $x\in A\cap B$ 或 $x\in C$, 左侧是右侧的子集。

(d) 正确的。两者的元素都是同时属于三集合的元素。

(e) 正确的。

<br/>

!!! question "练习 1.2.3 (德摩根定律)"
    设 $A$ 和 $B$ 是 $\mathbb{R}$ 的子集。

    (a) 如果 $x \in  {\left( A \cap  B\right) }^{c}$ ，解释为什么 $x \in  {A}^{c} \cup  {B}^{c}$ 。这表明 ${\left( A \cap  B\right) }^{c} \subseteq$  ${A}^{c} \cup  {B}^{c}$ 。

    (b) 证明反向包含 ${\left( A \cap  B\right) }^{c} \supseteq  {A}^{c} \cup  {B}^{c}$ ，并得出结论 ${\left( A \cap  B\right) }^{c} = {A}^{c} \cup  {B}^{c}$ 。

    (c) 通过双向包含证明 ${\left( A \cup  B\right) }^{c} = {A}^{c} \cap  {B}^{c}$ 。

(a) 若 $x\in \left(A\cap B\right)^c$，则 $x\notin A$ 或 $x\notin B$，在 $x\in \mathbb{R}$ 的情况下，$x\in A^c$ 或 $x\in B^c$，即 $x\in A^c\cup B^c$，这说明 $\left(A\cap B\right)^c\subseteq A^c\cup B^c$。

(b) 同上反推，这样就能得到 $\left(A\cap B\right)^c= A^c\cup B^c$。

(c) 同理。

<br/>

!!! question "练习 1.2.4"
    验证在以下特殊情况下的三角不等式:
    
    (a) $a$ 和 $b$ 具有相同的符号；

    (b) $a \geq  0,b < 0$ ，以及 $a + b \geq  0$ 。

(a) 当 $a,b\geq 0$ 时，$|a|=a$，$|b|=b$，因此 $|a+b|\leq|a|+|b|$ 显然成立。

当 $a,b<0$ 时，$|a|=-a$，$|b|=-b$，所以原式可化作 $-(a+b)\leq-(a+b)$，仍然成立。

(b) $a\geq 0$，$b<0$，$a+b\geq 0$ 时，$|a|=a$，$|b|=-b$，$|a+b|=a+b<a-b=|a|+|b|$。

<br/>

!!! question "练习 1.2.5"
    使用三角不等式来建立不等式 
    
    (a) $\left| {a - b}\right|  \leq  \left| a\right|  + \left| b\right|$ ；

    (b) $\left| \right| a\left| -\right| b\left| \right|  \leq  \left| {a - b}\right|$ .

(a) 将 $b$ 替换成 $-b$，因为 $|-b|=|b|$，所以 $|a-b|\leq |a|+|-b|=|a|+|b|$。

(b) <a id="1">绝对值不等式的本质</a>

这里证明不等式的关键是，$|a+b|\leq|a|+|b|$ 这个不等式左右绝对值内的数字之和是一致的，要证不等式只要满足这个形式，通过赋值就能证明。

要证 $\left||a|-|b|\right|\leq|a-b|$, 其实是证明 $|a|-|b|\leq|a-b|$ 和 $|b|-|a|\leq|a-b|$，它们变形后为 $|a|\leq|a-b|+|b|$ 和 $|b|\leq |b-a|+|a|$，都满足前述绝对值不等式的形式。将绝对值不等式里的 $a$ 替换成 $a-b$ 或者是将 $b$ 替换成 $b-a$，就能证明。

<br/>

!!! question "练习 1.2.6"
    给定一个函数 $f$ 及其定义域的一个子集 $A$ ，让 $f\left( A\right)$ 表示 $f$ 在集合 $A$ 上的范围；即 $f\left( A\right)  = \{ f\left( x\right)  : x \in  A\}$ 。

    (a) 设 $f\left( x\right)  = {x}^{2}$ 。若 $A = \left\lbrack  {0,2}\right\rbrack$ (闭区间 $\{ x \in  \mathbb{R} : 0 \leq  x \leq  2\}$ )且 $B = \left\lbrack  {1,4}\right\rbrack$ ，求 $f\left( A\right)$ 和 $f\left( B\right)$ 。在这种情况下 $f\left( {A \cap  B}\right)  = f\left( A\right)  \cap  f\left( B\right)$ 是否成立？ $f\left( {A \cup  B}\right)  = f\left( A\right)  \cup  f\left( B\right)$ 是否成立？

    (b) 找到两个集合 $A$ 和 $B$ ，使得 $f\left( {A \cap  B}\right)  \neq  f\left( A\right)  \cap  f\left( B\right)$ 。

    (c) 证明对于任意函数 $g : \mathbb{R} \rightarrow  \mathbb{R}$ ，对于所有集合 $A,B \subseteq  \mathbb{R}$ ， $g\left( {A \cap  B}\right)  \subseteq  g\left( A\right)  \cap  g\left( B\right)$ 总是成立。

    (d) 形成并证明一个关于任意函数 $g$ 下 $g\left( {A \cup  B}\right)$ 和 $g\left( A\right)  \cup  g\left( B\right)$ 之间关系的猜想。

<a id="1.2.6."></a>

(a) $f(A)=[0,4]$，$f(B)=[1,16]$，$A\cap B=[1,2]$，$A\cup B=[0,4]$，$f(A\cap B)=[1,4]$，$f(A)\cap f(B)=[1,4]$，$f(A\cup B)=[0,16]=f(A)\cup f(B)$。

(b) 由于 $f(x)=x^2$ 在不同的自变量取值下能得到相同的函数值，所以没有交集的集合它们的函数值是可能有交集的。例如取 $A=[-2,-1]$，$B=[1,2]$，$A\cap B=\varnothing$，$f(A\cap B)=\varnothing$，$f(A)\cap f(B)=[1,4]$，$f(A\cap B)\neq f(A)\cap f(B)$。

(c) 由这一映射的定义，对 $x\notin A$，$g(x)\in g(A)$ 的情形， $\exists\ x_1\in A$，$g(x_1)=g(x)$。所以对于这个问题，只需讨论 $A\cup B$ 中的 $x$ 即可。

由定义，$A\cap B$ 中的全体 $x$ 所对应的 $g(x)$ 组成 $g(A\cap B)$，$A$ 中的全体 $x$ 所对应的 $g(x)$ 组成 $g(A)$，$B$ 中的全体 $x$ 所对应的 $g(x)$ 组成 $g(B)$。所以 $g(A\cap B)\subseteq g(A)$ 且 $g(A\cap B)\subseteq g(B)$，从而 $g(A\cap B)\subseteq g(A)\cap g(B)$。

顺带附加说明这个式子在相反方向是不成立的。由 (b) 问的灵感，令 $x_1\in A\setminus B$，$x_2\in B$，若 $g(x_1)=g(x_2)$，由于 $g(x_1)\in g(A)$，$g(x_2)\in g(B)$，此时可得 $g(x_1)\notin g(A\cap B)$ 但是 $g(x_1)\in g(A)\cap g(B)$，所以 $g(A\cap B)\not\subseteq g(A)\cap g(B)$。

(d) $g(A\cup B)=g(A)\cup g(B)$。

同 (c) 问，只需考虑 $A\cup B$ 中的元素即可。令 $x\in A\cup B$，若 $x\in A$，则 $g(x)\in g(A)$，所以 $g(x)\in g(A)\cup g(B)$；若 $x\in B$，同理可得 $g(x)\in g(A)\cup g(B)$。所以 $g(A\cup B)\subseteq g(A)\cup g(B)$。

对于相反方向的情况，若 $g(x)\in g(A)\cup g(B)$，则 $g(x)$ 必定来自于 $g(A)$ 或 $g(B)$，所以 $x$ 必定来自于 $A\cup B$，这就证明了 $g(A)\cup g(B)\subseteq g(A\cup B)$。

所以 $g(A\cup B)=g(A)\cup g(B)$。

<br/>

!!! question "练习 1.2.7"
    给定一个函数 $f : D \rightarrow  \mathbb{R}$ 和一个子集 $B \subseteq  \mathbb{R}$ ，令 ${f}^{-1}\left( B\right)$ 为定义域 $D$ 中所有被映射到 $B$ 的点的集合；即 ${f}^{-1}\left( B\right)  = \{ x \in  D : f\left( x\right)  \in  B\}$ 。这个集合被称为 $B$ 的原像。

    (a) 设 $f\left( x\right)  = {x}^{2}$ 。如果 $A$ 是闭区间 $\left\lbrack  {0,4}\right\rbrack$ 且 $B$ 是闭区间 $\left\lbrack  {-1,1}\right\rbrack$ ，求 ${f}^{-1}\left( A\right)$ 和 ${f}^{-1}\left( B\right)$ 。在这种情况下， ${f}^{-1}\left( {A \cap  B}\right)  = {f}^{-1}\left( A\right)  \cap  {f}^{-1}\left( B\right)$ 成立吗？ ${f}^{-1}\left( {A \cup  B}\right)  = {f}^{-1}\left( A\right)  \cup  {f}^{-1}\left( B\right)$ 成立吗？

    (b) 在(a)中展示的原像的良好行为是完全普遍的。证明对于任意函数 $g : \mathbb{R} \rightarrow  \mathbb{R}$ ，对于所有集合 $A,B \subseteq  \mathbb{R}$ ， ${g}^{-1}\left( {A \cap  B}\right)  = {g}^{-1}\left( A\right)  \cap  {g}^{-1}\left( B\right)$ 和 ${g}^{-1}\left( {A \cup  B}\right)  = {g}^{-1}\left( A\right)  \cup  {g}^{-1}\left( B\right)$ 总是成立。

(a) $A\cap B=[0,1]$，$A\cup B=[-1,4]$。$f^{-1}(A)=[-2,2]$，$f^{-1}(B)=[-1,1]$，$f^{-1}(A\cap B)=[-1,1]$，$f^{-1}(A\cup B)=[-2,2]$。

所以 $f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B)$，$(1)$

$f^{-1}(A\cup B)=f^{-1}(A)\cup f^{-1}(B)$。$(2)$

(b) 我们要证明对任意的 $g:\mathbb{R}\to \mathbb{R}$, 公式 $(1)$ 和 $(2)$ 仍然成立。

对于 $(1)$,我们有:

$x\in g^{-1}(A\cap B) \iff g(x)\in A\cap B \iff g(x)\in A \text{ 且 } g(x)\in B \iff x\in g^{-1}(A) \text{ 且 } x\in g^{-1}(B) \iff x\in g^{-1}(A)\cap g^{-1}(B)$

所以 $g^{-1}(A\cap B)=g^{-1}(A)\cap g^{-1}(B)$。

同理可得 $g^{-1}(A\cup B)=g^{-1}(A)\cup g^{-1}(B)$。

顺带说明此题和 [$1.2.6.$](#1.2.6.) 结论的区别。事实上这关乎映射的单射性质。$x\mapsto f(x)$ 不一定是一个单射，而 $f(x)\mapsto x$ 一定是一个单射。 事实上，如果是一个单射，那么上述的两个公式将会成立。证明如下：

如果 $f$ 是一个单射，那么对于 $\forall\ x\notin A$，$f(x)\notin f(A)$。 从而 $f(x)\in f(A)\iff x\in A$。所以 $f(x)\in f(A\cap B)\iff x\in A\cap B\iff f(x)\in f(A)\cap f(B)$。$f(x)\in f(A\cup B)\iff x\in A\cup B\iff f(x)\in f(A)\cup f(B)$。

所以有 $f(A\cap B)=f(A)\cap f(B)$，$f(A\cup B)=f(A)\cup f(B)$。

<br/>

!!! question "练习 1.2.8"
    形成每个命题的逻辑否定。一种方法是在每个断言前简单地加上“情况并非如此……”，但对于每个陈述，尝试将“不”这个词尽可能深入地嵌入到结果句子中(或完全避免使用它)。

    (a) 对于所有满足 $a < b$ 的实数，存在一个 $n \in  \mathbb{N}$ 使得 $a + 1/n < b$ 。

    (b) 在每两个不同的实数之间，存在一个有理数。

    (c) 对于所有自然数 $n \in  \mathbb{N},\sqrt{n}$ ，它要么是自然数，要么是无理数。

    (d) 给定任何实数 $x \in  \mathbb{R}$ ，存在 $n \in  \mathbb{N}$ 满足 $n > x$ 。

(a) 存在两个实数 $a<b$，对任意 $n\in \mathbb{N}$，$a+1/n\geq b$。

(b) 存在两个实数，它们中间没有有理数。

(c) 存在 $n\in \mathbb{N}$，$\sqrt{n}$ 既不是自然数，也不是无理数。

(d) 存在 $x\in \mathbb{R}$，对 $\forall\ n\in \mathbb{N}$，$n\leq x$。

<br/>

!!! question "练习 1.2.9"
    证明在例1.2.7中定义的序列 $\left( {{x}_{1},{x}_{2},{x}_{3},\ldots }\right)$ 以2为上界；即，证明对于每个 $n \in  \mathbb{N}$ ， ${x}_{n} \leq  2$ 成立。

使用数学归纳法进行证明。假设 $x_n\leq 2$，则 $x_{n+1}=(1/2)x_n+1\leq 2$。

又因为 $x_1=1\leq 2$，所以对任意 $n\in \mathbb{N}$，都有 $x_n\leq 2$。

<br/>

!!! question "练习 1.2.10"
    设 ${y}_{1} = 1$ ，并且对于每个 $n \in  \mathbb{N}$ 定义 ${y}_{n + 1} = \left( {3{y}_{n} + 4}\right) /4$ 。

    (a) 使用归纳法证明该序列对所有 $n \in  \mathbb{N}$ 满足 ${y}_{n} < 4$ 。

    (b) 使用另一个归纳论证来证明序列 $\left( {{y}_{1},{y}_{2},{y}_{3},\ldots }\right)$ 是递增的。

(a) 同上，假设 $y_n<4$，则 $y_{n+1}=(3y_n+4)/4<4$。又 $y_1=1$，故成立。

(b) 假设 $y_{n+1}>y_n$，则 $y_{n+2}-y_{n+1}=(3y_{n+1}+4)/4-(3y_n+4)/4=3(y_{n+1}-y_n)/4>0$，所以 $y_{n+2}>y_{n+1}$。

又因为 $y_2=7/4>y_1$，所以 $y_n$ 是递增的。

<br/>

!!! question "练习 1.2.11"
    如果一个集合 $A$ 包含 $n$ 个元素，证明 $A$ 的不同子集的数量等于 ${2}^{n}$ 。(请记住，空集 $\varnothing$ 被认为是每个集合的子集。)

任何一个元素在子集中都有存在/不存在的两种可能性，所以有 $2^n$ 个子集。

<br/>

!!! question "练习 1.2.12"
    对于本练习，假设练习 1.2.3 已成功完成。

    (a) 展示如何使用归纳法得出结论
    $$
    {\left( {A}_{1} \cup  {A}_{2} \cup  \cdots  \cup  {A}_{n}\right) }^{c} = {A}_{1}^{c} \cap  {A}_{2}^{c} \cap  \cdots  \cap  {A}_{n}^{c}
    $$
    对于任何有限的 $n \in  \mathbb{N}$ 。

    (b) 解释为什么不能使用归纳法得出结论
    $$
    {\left( \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{A}_{n}\right) }^{c} = \mathop{\bigcap }\limits_{{n = 1}}^{\infty }{A}_{n}^{c}
    $$
    考虑练习1.2.2的(a)部分可能有所帮助。

    (c) 部分(b)中的陈述是否有效？如果有效，请写出一个不使用归纳法的证明。

(a) 若 $\left(A_1\cup A_2\cup \cdots \cup A_n\right)^c=A_1^c\cap A_2^c\cap \cdots \cap A_n^c$，则有 $\left(A_1\cup A_2\cup \cdots \cup A_n\cup A_{n+1}\right)^c=\left(A_1\cup A_2\cup \cdots \cup A_n\right)^c\cap A_{n+1}^c=A_1^c\cap A_2^c\cap \cdots \cap A_n^c\cap A_{n+1}^c$。又由于 $n=2$ 时是成立的，所以对任意 $n\in \mathbb{Z^+}$ 都成立。

(b) 因为有限是不能直接推广到无限的。<a id="无限"></a>

(c) <a id="2">德·摩根律在无穷情况下的推广</a>

$$
\left(\displaystyle\bigcup_{n=1}^{\infty}A_n\right)^c=\displaystyle\bigcap_{n=1}^{\infty}A_n^c
$$

是成立的。

设 $x\in (\displaystyle\bigcup_{n=1}^{\infty}A_n)^c$，则对 $\forall\ n\in \mathbb{N}$，$x\notin A_n$，即 $x\in A_n^c$，所以 $x\in \displaystyle\bigcap_{n=1}^{\infty}A_n^c$。这说明 $(\displaystyle\bigcup_{n=1}^{\infty}A_n)^c\subseteq \displaystyle\bigcap_{n=1}^{\infty}A_n^c$。

反之，设 $x\in \displaystyle\bigcap_{n=1}^{\infty}A_n^c$，则对 $\forall\ n\in \mathbb{N}$，$x\in A_n^c$，即 $x\notin A_n$，所以 $x\notin \displaystyle\bigcup_{n=1}^{\infty}A_n$，$x\in (\displaystyle\bigcup_{n=1}^{\infty}A_n)^c$ 。这说明 $\displaystyle\bigcap_{n=1}^{\infty}A_n^c\subseteq \left(\displaystyle\bigcup_{n=1}^{\infty}A_n\right)^c$。

综上所述，$\left(\displaystyle\bigcup_{n=1}^{\infty}A_n\right)^c=\displaystyle\bigcap_{n=1}^{\infty}A_n^c$。

参考资料：[MSE上的证明](https://math.stackexchange.com/questions/1542248/generalized-demorgans-law-proof?noredirect=1)

---

## 习题 1.3 完备性公理

!!! question "练习 1.3.1"
    设 ${\mathbb{Z}}_{5} = \{ 0,1,2,3,4\}$ 并定义加法和乘法模5。换句话说，计算 $a + b$ 和 ${ab}$ 除以5时的整数余数，并分别将其作为和与积的值。

    (a) 证明，给定任何元素 $z \in  {\mathbb{Z}}_{5}$ ，存在一个元素 $y$ ，使得 $z + y = 0$ 。元素 $y$ 称为 $z$ 的加法逆元。

    (b) 证明，给定任意 $z \neq  0$ 在 ${\mathbb{Z}}_{5}$ 中，存在一个元素 $x$ 使得 ${zx} = 1$ 。该元素 $x$ 被称为 $z$ 的乘法逆元。

    (c) 加法和乘法逆元的存在性是域定义的一部分。研究集合 ${\mathbb{Z}}_{4} = \{ 0,1,2,3\}$ (其中加法和乘法定义为模4)中加法和乘法逆元的存在性。对 $n$ 的值在 ${\mathbb{Z}}_{n}$ 中存在加法逆元的情况提出一个猜想，然后对乘法逆元的存在性提出另一个猜想。

(a)(b) 显然。

(c) 加法逆元均存在，乘法逆元里 $1,3$为其本身，$2$ 不存在。

$n\in \mathbb{Z^+}$ 时 $\mathbb{Z_n}$ 均存在加法逆元；$n$ 为质数时 $\mathbb{Z_n}$ 均存在乘法逆元。

<br/>

!!! question "练习 1.3.2"
    (a) 以定义 1.3.2 的风格为集合的下确界或最大下界写一个正式定义。

    (b) 现在，陈述并证明一个关于最大下界的引理 1.3.7 的版本。

(a) 称实数 $s$ 是集合 $A\subseteq \mathbb{R}$ 的最大下界， 若满足以下条件：

(i) $s$ 是 $A$ 的下界；

(ii) 若 $b$ 是 $A$ 的任一下界，则 $b\leq s$。

(b) 设 $s$ 是 $A\subseteq \mathbb{R}$ 的一个下界，则 $s=\inf A$ 当且仅当对 $\forall\ \varepsilon>0$，$\exists\ a\in A$，$s+\varepsilon>a$。

<br/>

!!! question "练习 1.3.3"
    (a) 设 $A$ 有下界，并定义 $B = \{ b \in  \mathbb{R}$ : $b$ 是 $A\}$ 的下界。证明 $\sup B = \inf A$ 。

    (b) 使用(a)解释为什么在完备性公理中不需要断言最大上界的存在。

    (c) 提出另一种利用完备性公理证明有下界的集合存在最大下界的方法。

(a) 首先，对 $\forall\ a\in A$，$\forall\ b\in B$，有 $b\leq a$，所以集合 $B$ 存在上界，由完备性公理，其存在上确界 $\sup B$。下证 $\sup B=\inf A$。

(i) 若 $a<\sup B$，则 $\exists\ b \in B$，$a<b$，即 $a\notin A$。所以若 $a\in A$，$\sup B\leq a$，这说明 $\sup B$ 是 $A$ 的下界。

(ii) 又对 $\forall\ b\in B$，$b\leq \sup B$，所以 $\sup B$ 是$A$ 的最大下界，由定义，$\sup B=\inf A$。

(b) 完备性公理不需定义最大下界，直接定义下界的上确界即可。

(c) 设集合 $A$ 有下界，即存在 $Q\in \mathbb{R}$ 使得对 $\forall\ a\in A$，$Q\leq a$。要证明它有最大下界，我们从上界入手，试着把它的下界转换成上界。

设 $B=\left\{x\in \mathbb{R}:-x\in A\right\}$，那么对 $\forall\ x\in B$，有 $-x\in A$，所以 $-x\geq Q$，即 $x\leq -Q$，这说明 $B$ 有上界 $-Q$。由完备性公理，$B$ 有上确界 $\sup B$。

(i) 对 $\forall\ x\in B$，$x\leq \sup B$，即 $-x\geq -\sup B$；

(ii) 对 $\forall\ \varepsilon>0$，$\exists\ x\in B$ 使得 $\sup B-\varepsilon<x$，即 $-x<-\sup B+\varepsilon$。

因为 $\forall\ -x\in A$，$\exists\ x\in B$，所以上述两条性质对全体 $a\in A$ 都成立，所以 $A$ 的下确界存在，且 $\inf A=-\sup B$。

<br/>

!!! question "练习 1.3.4"
    假设 $A$ 和 $B$ 非空、有上界，并满足 $B \subseteq  A$ 。证明 $\sup B \leq  \sup A$ 。

由题意，$\sup A$，$\sup B$ 均存在。

因为 $B\subseteq A$，所以对 $\forall\ b\in B$，$b\in A$，即 $b\leq \sup A$，这说明 $\sup A$ 是 $B$ 的一个上界，由 $\sup B$ 的定义，$\sup B\leq \sup A$。

<br/>

!!! question "练习 1.3.5"
    设 $A \subseteq  \mathbb{R}$ 有上界，且设 $c \in  \mathbb{R}$ 。定义集合 $c + A$ 和 ${cA}$ 为 $c + A = \{ c + a : a \in  A\}$ 和 ${cA} = \{ {ca} : a \in  A\}$ 。

    (a) 证明 $\sup \left( {c + A}\right)  = c + \sup A$ 。

    (b) 如果 $c \geq  0$ ，证明 $\sup \left( {cA}\right)  = c\sup A$ 。

    (c) 对于 $c < 0$ 的情况，假设一个类似 $\sup \left( {cA}\right)$ 的陈述。

由题意，$\sup A$ 存在。

(a) (i) 对 $\forall\ a\in A$，$a\leq \sup A$。所以对 $\forall\ x\in c+A$，$\exists\ a\in A$，使得 $x=c+a\leq c+\sup A$，所以 $c+\sup A$ 是 $c+A$ 的一个上界。

(ii) 对 $\forall\ \varepsilon>0$，$\exists\ a\in A$ 使得 $\sup A-\varepsilon<a$，所以 $\exists\ x\in c+A$ 使得 $x=c+a>c+\sup A-\varepsilon$。

所以 $\sup (c+A)=c+\sup A$。

(b) $c=0$ 时，$\sup (cA)=0=c\sup A$，显然成立。

$c>0$ 时，(i) 对 $\forall\ x\in cA$，$\exists\ a\in A$，使得 $x=ca\leq c\sup A$，所以 $c\sup A$ 是 $cA$ 的一个上界。

(ii) 对 $\forall\ \varepsilon>0$，$\exists\ a\in A$ 使得 $\sup A-\varepsilon<a$，所以 $\exists\ x\in cA$ 使得 $x=ca>c\sup A-c\varepsilon$,由 $\varepsilon$ 的任意性，得证。

所以 $\sup (cA)=c\sup A$。

(c) $c<0$ 时，$\sup (cA)=c\inf A$。通过改变不等号方向即可证明。

<br/>

!!! question "练习 1.3.6"
    在不证明的情况下，计算以下集合的上确界和下确界:

    (a) $\left\{  {n \in  \mathbb{N} : {n}^{2} < {10}}\right\}$ .

    (b) $\{ n/\left( {m + n}\right)  : m,n \in  \mathbb{N}\}$ .

    (c) $\{ n/\left( {{2n} + 1}\right)  : n \in  \mathbb{N}\}$ .

    (d) $\{ n/m : m,n \in  \mathbb{N}$ 与 $m + n \leq  {10}\}$ 。

(a) 上确界 $3$，下确界 $1$。

(b) $1$，$0$。

(c) $1/2$，$1/3$。

(d) $9$，$1/9$。

<br/>

!!! question "练习 1.3.7"
    证明如果 $a$ 是 $A$ 的上界，并且 $a$ 也是 $A$ 的元素，那么必有 $a = \sup A$ 。

对任何一个上界 $b$，因为 $a\in A$，所以 $a\leq b$，这说明 $a=\sup A$。

<br/>

!!! question "练习 1.3.8"
    如果 $\sup A < \sup B$ ，则证明存在一个元素 $b \in  B$ ，它是 $A$ 的上界。

取 $\varepsilon=(\sup B-\sup A)/2$，则 $\exists\ b\in B$，$b>\sup B-\varepsilon=(\sup B+\sup A)/2>\sup A$，所以 $b$ 是 $A$ 的一个上界。

<br/>

!!! question "练习 1.3.9"
    暂时不考虑形式证明，判断以下关于上确界和下确界的陈述是真还是假。对于任何错误的陈述，提供一个例子说明该主张似乎不成立。

    (a) 一个有限的非空集总是包含它的上确界。

    (b) 如果对于集合 $A$ 中的每个元素 $a$ ，都有 $a < L$ ，那么 $\sup A < L$ 。

    (c) 如果 $A$ 和 $B$ 是具有以下性质的集合:对于每个 $a \in  A$ 和每个 $b \in  B$ ，都有 $a < b$ ，那么可以得出 $\sup A < \inf B$ 。

    (d) 如果 $\sup A = s$ 且 $\sup B = t$ ，则 $\sup \left( {A + B}\right)  = s + t$ 。集合 $A + B$ 定义为 $A + B = \{ a + b : a \in  A$ 和 $b \in  B\}$ 。

    (e) 如果 $\sup A \leq  \sup B$ ，则存在一个元素 $b \in  B$ ，它是 $A$ 的上界。

(a) 真。

(b) 假。考虑 $A=\left\{x\in \mathbb{Q}: x^2<2\right\}$，其内的任意元素都小于 $\sqrt{2}$，但是 $\sup A=\sqrt{2}$。

(c) 假。 考虑 (b) 中的 $A$ 和 $B=\left\{x\in \mathbb{Q}: x^2>2,x>0\right\}$，则对 $\forall\ a\in A,b\in B$ 有 $a<b$，但是 $\sup A=\inf B=\sqrt{2}$。

(d) 真。

(e) 假。考虑 (b) 中的 $A$，令 $B=A$，则 $\sup B=\sup A$，此时不存在 $b\in B$，使得 $b\geq \sup A$。

---

## 习题 1.4 完备性的推论

!!! question "练习 1.4.1"
    在不做太多工作的情况下，展示如何通过将此情况转换为已证明的情况来证明定理1.4.3。

$a<0<b$ 时，$0$ 即为答案。

$a<b\leq 0$ 时，化成 $0\leq -b<-a$ 即可转化为前述情况证明。

<br/>

!!! question "练习 1.4.2"
    回想一下， $\mathbb{R}\setminus\mathbb{Q}$ 代表无理数集。

    (a) 证明如果 $a,b \in  \mathbb{Q}$ ，那么 ${ab}$ 和 $a + b$ 也是 $\mathbb{Q}$ 的元素。

    (b) 证明如果 $a \in  \mathbb{Q}$ 和 $t \in  \mathbb{R}\setminus\mathbb{Q}$ ，那么只要 $a \neq  0$ ， $a + t \in  \mathbb{R}\setminus\mathbb{Q}$ 和 ${at} \in  \mathbb{R}\setminus\mathbb{Q}$ 也成立。

    (c) 部分 (a) 可以总结为 $\mathbb{Q}$ 在加法和乘法下是封闭的。 $\mathbb{R}\setminus\mathbb{Q}$ 在加法和乘法下是否封闭？给定两个无理数 $s$ 和 $t$ ，我们可以对 $s + t$ 和 ${st}$ 说些什么？

<a id="1.4.2."></a>

(a) 由于 $a,b\in \mathbb{Q}$，那么可令 $a=p_1/q_1$，$b=p_2/q_2$，那么 $a+b=(p_1q_2+p_2q_1)/q_1q_2\in \mathbb{Q}$，同理 $ab\in \mathbb{Q}$。

(b) 由 $(a)$，若 $a+t\in \mathbb{Q}$，则 $t=(a+t)-a\in \mathbb{Q}$，所以 $a+t\in \mathbb{R}\backslash\mathbb{Q}$，同理 $at\in \mathbb{R}\backslash\mathbb{Q}$。

(c) $\mathbb{R}\backslash \mathbb{Q}$ 在加法和乘法下不封闭，更精确地说，无理数的运算结果可能是有理数。

<br/>

!!! question "练习 1.4.3"
    使用练习 1.4.2，通过将定理 1.4.3 应用于实数 $a - \sqrt{2}$ 和 $b - \sqrt{2}$ ，为推论 1.4.4 提供一个证明。

任意两个实数 $a,b$ 之中必有一个有理数 $q$，使得 $a<q<b$。

所以 $a-\sqrt{2}<q-\sqrt{2}<b-\sqrt{2}$，由 [$1.4.2.$](#1.4.2.) 可知 $q-\sqrt{2}$ 是无理数。

<br/>

!!! question "练习 1.4.4"
    使用 $\mathbb{R}$ 的阿基米德性质来严格证明 $\inf \{ 1/n : n \in  \mathbb{N}\}  = 0$ 。

首先，对于 $\forall\ n\in \mathbb{Z^+}$，有 $0<1/n$，所以 $0$ 是 $\{1/n:n\in \mathbb{Z^+}\}$ 的一个下界。

下面证明 $0$ 是下确界。事实上由实数的阿基米德性，对 $\forall\ y>0$，$\exists\ n\in \mathbb{Z^+}$，$1/n<y$，所以任何比 $0$ 大的数都不是下界，即 $0$ 是下确界。

<br/>

!!! question "练习 1.4.5"
    证明 $\mathop{\bigcap }\limits_{{n = 1}}^{\infty }\left( {0,1/n}\right)  = \varnothing$ 。注意，这表明闭区间套定理中的区间必须是闭的，以便定理的结论成立。

由阿基米德性的结论即可知对 $\forall\ y>0$，$y\notin \displaystyle\bigcap_{n=1}^{\infty} (0,1/n)$。所以 $\displaystyle\bigcap_{n=1}^{\infty} (0,1/n)=\varnothing$。

<br/>

!!! question "练习 1.4.6"
    (a) 通过展示假设 ${\alpha }^{2} > 2$ 导致与事实 $\alpha  = \sup T$ 矛盾的结论，完成定理1.4.5的证明。

    (b) 修改此论证以证明对于任何实数 $b \geq  0$ ， $\sqrt{b}$ 的存在性。

(a) 若 $\alpha^2>2$，对 $n\in \mathbb{N}^+$，取 $(\alpha-1/n)^2=\alpha^2-2\alpha/n+1/n^2>\alpha^2-2\alpha/n>2$，得 $n>2\alpha/(\alpha^2-2)$，所以 $\alpha-1/n$ 也是 $T$ 的上界，矛盾。

这里默认了 $\alpha>0$。

(b) $b=0$ 时是显然成立的。

$b>0$ 时，考虑集合 $T=\{t>0:t^2<b\}$。$b<1$ 时，$b\in T$ 且 $1$ 是 $T$ 的上界，所以 $\sup T$ 存在。$b\geq 1$ 同理可得其存在性。

令 $x=\sup T$，下面证明 $x^2=b$。

(i) 若 $x^2<b$，对 $n\in \mathbb{N}^+$，取 $(x+1/n)^2=x^2+2x/n+1/n^2<x^2+(2x+1)/n<b$，得 $n>(2x+1)/(b-x^2)$，即 $x+1/n$ 可能属于 $T$，矛盾。

(ii) 若 $x^2>b$，对 $n\in \mathbb{N}^+$，取 $(x-1/n)^2=x^2-2x/n+1/n^2>x^2-2x/n>b$，得 $n>2x/(x^2-b)$，即 $x-1/n$ 是 $T$ 的上界，矛盾。

所以 $x^2=b$。即 $x=\sqrt{b}$。

<br/>

!!! question "练习 1.4.7"
    完成定理1.4.12的以下证明。

    假设 $B$ 是一个可数集。因此，存在 $f : \mathbb{N} \rightarrow  B$ ，它是 $1 - 1$ 且满射。设 $A \subseteq  B$ 是 $B$ 的一个无限子集。我们必须证明 $A$ 是可数的。

    设 ${n}_{1} = \min \{ n \in  \mathbb{N} : f\left( n\right)  \in  A\}$ 。作为 $g : \mathbb{N} \rightarrow  A$ 定义的开端，设 $g\left( 1\right)  = f\left( {n}_{1}\right)$ 。展示如何归纳地继续这个过程，以生成一个从 $\mathbb{N}$ 到 $A$ 的一对一函数 $g$ 。

<a id="1.4.7."></a>

设 $n_2=\min \{n\in \mathbb{N}^+:f(n)\in A,n>n_1\}$，令 $g(2)=f(n_2)$。

以此类推，对于 $g(k)=f(n_k)$，由于 $A$ 是无限集，所以总存在 $n_{k+1}=\min \{n\in \mathbb{N}^+:f(n)\in A,n>n_k\}$，令 $g(k+1)=f(n_{k+1})$。

这样就得到了 $g:\mathbb{N}^+\to A$ 的映射。

<br/>

!!! question "练习 1.4.8"
    使用以下大纲为定理1.4.13中的陈述提供证明。

    (a) 首先，证明两个可数集合 ${A}_{1}$ 和 ${A}_{2}$ 的陈述(i)。例1.4.8(ii)可能是一个有用的参考。通过首先将 ${A}_{2}$ 替换为集合 ${B}_{2} = {A}_{2} \smallsetminus  {A}_{1} = \left\{  {x \in  {A}_{2} : x \notin  {A}_{1}}\right\}$ ，可以避免一些技术性问题。这样做的目的是使并集 ${A}_{1} \cup  {B}_{2}$ 等于 ${A}_{1} \cup  {A}_{2}$ ，并且集合 ${A}_{1}$ 和 ${B}_{2}$ 是不相交的。(如果 ${B}_{2}$ 是有限的，会发生什么？)

    (b) 现在，解释(i)中更一般的陈述是如何得出的。

    解释为什么不能使用归纳法从(i)部分证明定理1.4.13的(ii)部分。

    (c) 展示如何将 $\mathbb{N}$ 排列成二维数组
    $$
    \begin{array}{llllll} 1 & 3 & 6 & {10} & {15} & \cdots  \end{array}
    $$
    $$
    \begin{array}{lllll} 2 & 5 & 9 & {14} & \cdots  \end{array}
    $$
    $$
    \begin{array}{llll} 4 & 8 & {13} & \cdots  \end{array}
    $$
    $$
    \begin{array}{lll} 7 & {12} & \cdots  \end{array}
    $$
    $$
    11 \ldots
    $$
    $$
    \vdots
    $$
    从而证明定理1.4.13 (ii)。

<a id="1.4.8."></a>

(a) 如果 $B_2$ 是无限集，那么由 [$1.4.7.$](#1.4.7.) 可知，$B_2$ 是可数集，那么存在两个双射 $f,g$，有 $f:\mathbb{N}^+\to A_1$，$g:\mathbb{N}^+\to B_2$。现在定义映射 $h:\mathbb{N}^+\to A_1\cup B_2$ 为

$$
h(n)=\begin{cases}
 f\left(\frac{n+1}{2}\right), & n \text{ 为奇数}\\
    g\left(\frac{n}{2}\right), & n \text{ 为偶数且不为0}\\
\end{cases}
$$

由 $A_1\cap B_2=\varnothing$，可知 $h$ 是单射。由 $f,g$ 的双射性知 $h$ 是满射，于是 $h$ 是双射。这说明 $A_1\cup B_2$ 即 $A_1\cup A_2$ 是可数集。

如果 $B_2$ 是有限集，设它其中的元素个数为 $m$，则 $B_2=\{b_1,b_2,\ldots,b_m\}$。存在双射 $f:\mathbb{N}^+\to A_1$。现在定义映射 $h:\mathbb{N}^+\to A_1\cup B_2$ 为

$$
h(n)=\begin{cases}
    b_n, & n\leq m\\
    f(n-m), & n>m\\
\end{cases}
$$

同上可得 $h$ 是双射。所以 $A_1\cup B_2$ 即 $A_1\cup A_2$ 是可数集。

(b) 使用数学归纳法。假设 $A_1,A_2,\ldots,A_n$ 是可数集时 $A_1\cup A_2\cup\ldots\cup A_n$ 是可数集，令 $B=A_1\cup A_2\cup\ldots\cup A_n$，则 $A_{n+1}$ 是可数集时 $B\cup A_{n+1}$ 即 $A_1\cup A_2\cup\ldots\cup A_n\cup A_{n+1}$ 也是可数集。又 $n=2$ 时结论成立，由数学归纳法可知结论对 $\forall\ n\in \mathbb{N}^+$ 成立。

由 [$1.2.12.(b)$](#无限) 可知，有限归纳法不能直接推广到无限的情况。

(c) <a id="3">二维正整数集为可数集的对角线构造证明法</a>

由图所示，我们可以构造映射 $f:\mathbb{(N^+)^2}\to \mathbb{N^{+}}$，

$$
f(m,n)=\begin{cases}
   1, &\text{if } m=n=1;\\
   f(m+1,n-1)+1, &\text{if } n>1;\\
   f(1,m-1)+1, &\text{if } m>1,n=1;
\end{cases}
$$

$(m,n)$ 是下面这个数表下面第 $m$，右边第 $n$ 个元素：

$$
\begin{array}{ccccc}
& 1 & 3 & 6 & 10  &\cdots\\
& 2 & 5 & 9 & 14  &\cdots\\
& 4 & 8 & 13 & 19  &\cdots\\
& 7 & 12 & 18 & 25  &\cdots\\
& \vdots & \vdots & \vdots & \vdots
\end{array}
$$

可以看出，全体正整数都出现在这个表中，且每个正整数只出现一次。所以 $f$ 是一个双射。下面我们严格地证明这一点。

首先，我们证明 $f$ 是单射。 当横纵坐标之和固定时，这些点都在同一对角线上，我们利用这个性质给出下面的证明：

设 $f(m_1,n_1)=f(m_2,n_2)$， 不失一般性，令 $m_1+n_1\leq m_2+n_2$，此时 $(m_1,n_1)$ 所在的对角线在 $(m_2,n_2)$ 所在的对角线的上方（也是左侧）或与之重合。

若不重合即 $m_1+n_1<m_2+n_2$，则 $f(m_1,n_1)\leq f(1,m_1+n_1-1)<f(m_1+n_1,1)$，移动到下一条对角线上，直到 $(m_2,n_2)$ 所在的对角线，即移到 $f(m_1+n_1+k,1)$，其中 $m_1+n_1+k+1=m_2+n_2$。由一条对角线上的单调性，由 $n_2\geq 1$，有 $f(m_2,n_2)\geq f(m_1+n_1+k,1)>f(m_1,n_1)$。这就矛盾。

所以 $m_1+n_1=m_2+n_2$，即 $(m_1,n_1)$ 和 $(m_2,n_2)$ 在同一条对角线上。由对角线上的单调性，$m_1\geq m_2$ 可推出 $f(m_1,n_1)\leq f(m_2,n_2)$，所以 $m_1=m_2$，进而 $n_1=n_2$。综上所述，$f$ 是单射。

接着证明 $f$ 是满射，使用数学归纳法。假设对某个 $k\in \mathbb{N^+}$，$\exists\ m,n\in \mathbb{N^+}$，使得 $f(m,n)=k$，则对 $k+1$，有

$$
\begin{matrix}
   f(m-1,n+1)=f(m,n)+1=k+1, &\text{if } m>1;\\
   f(n+1,m)=f(m,n)+1=k+1, &\text{if } m=1;
\end{matrix}
$$

而 $f(1,1)=1$，所以 $f$ 是满射。

综上所述，$f$ 是双射。

对无穷多个可数集 $A_1,A_2,\ldots$，令 $B_1=A_1$，$B_2=A_2\backslash A_1$，$B_3=A_3\backslash (A_1\cup A_2)$，依此类推，$B_n=A_n\backslash (A_1\cup A_2\cup\ldots\cup A_{n-1})$，则 $A_1,A_2,\ldots$ 的并集可表示为 $B_1\cup B_2\cup B_3\cup\ldots$，且 $B_i\cap B_j=\varnothing$（$i\neq j$）。

若对 $\forall\ i\in \mathbb{N}^+$，$B_i$ 是可数集，设 $B_i=\{b_{i1},b_{i2},\ldots\}$，则定义映射 $g:\mathbb{N}^+\to B_1\cup B_2\cup B_3\cup\ldots$ 为 $f(m,n)\mapsto b_{mn}$，由定义可知 $g$ 是双射，所以 $A_1\cup A_2\cup A_3\cup\ldots$ 是可数集。

若 $\exists\ i\in \mathbb{N}^+$，$B_i$ 是有限集，令 $C$ 为这些有限集的并集，仿照 [$1.4.8.(a)$](#1.4.8.) 中的构造方法，可知 $C$ 是可数集，于是也能得证。

综上， $A_1\cup A_2\cup A_3\cup\ldots$ 是可数集。

<br/>

!!! question "练习 1.4.9"
    (a) 给定集合 $A$ 和 $B$ ，解释为什么 $A \sim  B$ 等价于断言 $B \sim  A$ 。

    (b) 对于三个集合 $A,B$ 、 $C$ ，证明 $A \sim  B$ 和 $B \sim  C$ 蕴含 $A \sim  C$ 。这两个性质意味着 $\sim$ 是一个等价关系。

(a) 由题意，存在双射 $f:A \to B$。则构造 $g:B \to A$ 使得 $g(f(x)) = x$ 对任意 $x \in A$ 成立。由于 $f$ 是双射，$g$ 也是双射。所以 $B \sim A$。

(b) 由题意，存在双射 $f:A \to B$ 和双射 $g:B \to C$。则构造 $h:A \to C$ 使得 $h(x) = g(f(x))$ 对任意 $x \in A$ 成立。由于 $f,g$ 是双射，$h$ 也是双射。所以 $A \sim C$。

<br/>

!!! question "练习 1.4.10"
    证明 $\mathbb{N}$ 的所有有限子集的集合是一个可数集。(事实上， $\mathbb{N}$ 的所有子集的集合不是一个可数集。这是1.5节的主题。)

将子集按元素和从小到大，元素个数从少到多排列：$\{1\},\{2\},\{3\},\{1,2\},\ldots$，则每个子集都能对应一个唯一的自然数。故所有有限子集的集合可数。

<br/>

!!! question "练习 1.4.11"
    考虑开区间(0,1)，并设 $S$ 为开单位正方形中的点集；即 $S = \{ \left( {x,y}\right)  : 0 < x,y < 1\}$ 。

    (a) 找到一个将(0,1)映射到 $S$ 的一对一函数，但不一定满射。(这很容易。)

    (b) 利用每个实数都有小数展开的事实，构造一个将 $S$ 映射到(0,1)的一对一函数。讨论所构造的函数是否为满射。(请记住，任何终止小数展开，如.235，与.234999...表示相同的实数。)

    接下来在练习1.4.13中讨论的施罗德-伯恩斯坦定理现在可以应用于得出结论 $\left( {0,1}\right)  \sim  S$ 。

(a) $f:x\mapsto (x,1/2)$。

(b) 构造如下的映射 $g:S\to (0,1)$：令 $x=0.a_1a_2\ldots$，$y=0.b_1b_2\ldots$，则 $g(x,y)=k$，其中 $k=0.a_1b_1a_2b_2\ldots$。

由于每个实数都有唯一的无限小数表示，由此知 $g$ 为满射。

<br/>

!!! question "练习 1.4.12"
    一个实数 $x \in  \mathbb{R}$ 被称为代数数，如果存在不全为零的整数 ${a}_{0},{a}_{1},{a}_{2},\ldots ,{a}_{n} \in  \mathbb{Z}$ ，使得
    $$
    {a}_{n}{x}^{n} + {a}_{{n}_{1}}{x}^{n - 1} + \cdots  + {a}_{1}x + {a}_{0} = 0.
    $$
    换句话说，如果一个实数是具有整数系数的多项式的根，那么它就是代数数。不是代数数的实数被称为超越数。重读第1.1节的最后一段。这里提出的最后一个问题与超越数是否存在密切相关。

    (a) 证明 $\sqrt{2},\sqrt[3]{2}$ 和 $\sqrt{3} + \sqrt{2}$ 是代数数。

    (b) 固定 $n \in  \mathbb{N}$ ，并令 ${A}_{n}$ 为作为具有整数系数的多项式根所得到的代数数，这些多项式的次数为 $n$ 。利用每个多项式都有有限个根的事实，证明 ${A}_{n}$ 是可数的。(对于每个 $m \in  \mathbb{N}$ ，考虑满足 $\left. {\left| {a}_{n}\right|  + \left| {a}_{n - 1}\right|  + \cdots  + \left| {a}_{1}\right|  + \left| {a}_{0}\right|  \leq  m.}\right)$ 的多项式 ${a}_{n}{x}^{n} + {a}_{{n}_{1}}{x}^{n - 1} + \cdots  + {a}_{1}x + {a}_{0}$ )

    (c) 现在，论证所有代数数的集合是可数的。关于超越数集合，我们可以得出什么结论？

(a) $(\sqrt{2})^2-2=0$，$(\sqrt[3]{2})^3-2=0$。

令 $t=\sqrt{2}+\sqrt{3}$，考虑 $t^2=5+2\sqrt{6}$，则 $(t^2-5)^2-24=0$，展开来得 $t^4-10t^2+1=0$。

所以它们都是代数数。

(b) 令 $B_m$ 为系数满足 $m-1<\displaystyle \sum_{i=0}^{n}|a_i|\leq m$ 的多项式的根的集合。显然满足 $B_m$ 条件的多项式个数有限，每个多项式的根的个数也有限，所以 $B_m$ 是有限集。

所以 $A_n=\displaystyle\bigcup_{m=1}^\infty B_m$ 由 [$1.4.8.$](#1.4.8.) 知是可数集。

(c) 所有代数数的集合为 $\displaystyle\bigcup_{n=1}^\infty A_n$，由 [$1.4.8.$](#1.4.8.) 知是可数集。

超越数集合是不可数的，换句话说，超越数的个数比代数数要多得多。

<br/>

<a id="10"></a>

!!! question "练习 1.4.13 (施罗德-伯恩斯坦定理)"
    假设存在一个一对一函数 $f : X \rightarrow  Y$ 和另一个 $1 - 1$ 函数 $g : Y \rightarrow  X$ 。按照步骤证明存在一个 $1 - 1$ 且满射的函数 $h : X \rightarrow  Y$ ，因此 $X \sim  Y$ 。

    (a) $f$ 的范围由 $f\left( X\right)  = \{ y \in  Y : y = f\left( x\right)$ 定义，其中 $x \in  X\}$ 。设 $y \in  f\left( X\right)$ 。(因为 $f$ 不一定是满射，范围 $f\left( X\right)$ 可能不是 $Y$ 的全部。)解释为什么存在唯一的 $x \in  X$ 使得 $f\left( x\right)  = y$ 。现在定义 ${f}^{-1}\left( y\right)  = x$ ，并证明 ${f}^{-1}$ 是从 $f\left( X\right)$ 到 $X$ 的一对一函数。

    以类似的方式，我们也可以定义 $1 - 1$ 函数 ${g}^{-1} : g\left( X\right)  \rightarrow  Y$ 。

    (b) 设 $x \in  X$ 为任意元素。令链 ${C}_{x}$ 为由所有形如以下元素的集合组成

    (1)
    $$
    \ldots ,{f}^{-1}\left( {{g}^{-1}\left( x\right) }\right) ,{g}^{-1}\left( x\right) ,x,f\left( x\right) ,g\left( {f\left( x\right) }\right) ,f\left( {g\left( {f\left( x\right) }\right) }\right) ,\ldots .
    $$
    解释为什么在上述链中， $x$ 左侧的元素数量可能为零、有限或无限。

    (c) 证明任意两条链要么完全相同，要么完全不相交。

    (d) 注意在 (1) 中的链的项在 $X$ 的元素和 $Y$ 的元素之间交替。给定一条链 ${C}_{x}$ ，我们希望关注 ${C}_{x} \cap  Y$ ，它只是链中位于 $Y$ 的部分。

    定义集合 $A$ 为所有满足 ${C}_{x} \cap  Y \subseteq  f\left( X\right)$ 的链 ${C}_{x}$ 的并集。令 $B$ 由不在 $A$ 中的剩余链的并集组成。证明任何包含在 $B$ 中的链必须具有以下形式
    $$
    y,g\left( y\right) ,f\left( {g\left( y\right) }\right) ,g\left( {f\left( {g\left( y\right) }\right) }\right) ,\ldots ,
    $$
    其中 $y$ 是 $Y$ 的一个元素，且不在 $f\left( X\right)$ 中。

    (e) 设 ${X}_{1} = A \cap  X,{X}_{2} = B \cap  X,{Y}_{1} = A \cap  Y$ ，且 ${Y}_{2} = B \cap  Y$ 。证明 $f$ 将 ${X}_{1}$ 映射到 ${Y}_{1}$ ，且 $g$ 将 ${Y}_{2}$ 映射到 ${X}_{2}$ 。利用此信息证明 $X \sim  Y$ 。

(a) 因为 $f$ 是单射，所以若 $f(x_1) = f(x_2)=y$，则有 $x_1 = x_2$，这就说明 $f(x)=y$ 的唯一性，因此 $f^{-1}$ 是良定义且单射的。

(b) 如果不存在 $y\in Y$ 使得 $g(y)=x$，那么 $g^{-1}(x)$ 不存在，因此左侧元素数量为 $0$。

同理，如果左侧延伸到某个元素满足上述情况，那么链在该元素截断，左侧元素数量有限。

若对左侧任何一个元素 $x$，$x\in Y$ 时 $f^{-1}(x)$ 存在， $x\in X$ 时 $g^{-1}(x)$ 存在，那么链可以无限延伸下去，左侧元素数量无限。

(c) 如果两条链所有元素都不相同就不相交。

如果两条链有一个元素相同，由 $f,g$ 的单射性可知，该元素左侧和右侧的所有元素都相同，因此两条链完全相同。

(d) 考虑链 $C_x$ 中的一个元素 $y\in Y$。

若 $y\in f(X)$，则链延伸到 $f^{-1}(y)$，否则链在 $y$ 截断，$C_x\subseteq B$。

若链在 $f^{-1}(y)$ 截断，那么对链中任意的 $x\in Y$ 都有 $x\in f(X)$，$C_x\subseteq A$。

如果继续往左延伸到某个元素 $x$ 使得 $f^{-1}(x)$ 不存在，那么 $C_x\subseteq B$。

如果一直无限延伸，$C_x\subseteq A$。

所以所有 $C_x\subseteq B$ 都以 $y\notin f(X)$ 为头开始。

(e) 根据 (c) 可知，所有链 $C_x$ 互不相交，于是 $f$ 将 $X_1$ 映到 $Y_1$，$g$ 将 $Y_2$ 映到 $X_2$。

又由题意，$X_1\cup X_2=X$，$Y_1\cup Y_2=Y$，根据 $f:X_1\to Y_1$ 和 $g:Y_2\to X_2$ 的双射性，构造如下的映射 $h:X\to Y$：

$$
h=\begin{cases}
    f(x), & x\in X_1,\\
    g^{-1}(x), & x\in X_2.
\end{cases}
$$

显然 $h$ 是双射。所以 $X\sim Y$。

---

## 习题 1.5 Cantor 定理

!!! question "练习 1.5.1"
    证明$(0,1)$不可数当且仅当 $\mathbb{R}$ 不可数。这表明定理1.5.1与定理1.4.11是等价的。

$\Rightarrow)$ 若 $(0,1)$ 不可数，由于可数集的子集可数，所以 $\mathbb{R}$ 也不可数。

$\Leftarrow)$ 若 $\mathbb{R}$ 不可数，假设 $(0,1)$ 可数，则 $[0,1)$ 同样可数，由于 $f:[0,1)\to [1,2)$，$f(x)=x+1$ 是一个双射，所以 $[1,2)$ 可数，同样对 $\forall\ x\in \mathbb{Z}$，$[x,x+1)$ 可数，所以 $\mathbb{R}=\displaystyle \bigcup_{x\in \mathbb{Z}}[x,x+1)$ 可数，矛盾。 

故 $(0,1)$ 不可数。

<br/>

!!! question "练习 1.5.2"
    (a) 解释为什么实数 $x = {.b}_{1}{b}_{2}{b}_{3}{b}_{4}\ldots$ 不能是 $f\left( 1\right)$ 。

    (b) 现在，解释为什么 $x \neq  f\left( 2\right)$ ，以及一般来说为什么对于任何 $n \in  \mathbb{N}$ ， $x \neq  f\left( n\right)$ 成立。

    (c) 指出这些观察中产生的矛盾，并得出结论:$(0,1)$是不可数的。

(b) 对 $\forall\ x\in \mathbb{N}$，$b_n\neq a_{nn}$，所以 $x\neq f(n)$。

(c) 由 (b) 可知这样的列表无法覆盖整个 $(0,1)$，所以 $(0,1)$ 不可数。

<br/>

!!! question "练习 1.5.3"
    对以下关于定理 1.5.1 证明的质疑提供反驳。

    (a) 每个有理数都有一个小数展开，因此我们可以应用相同的论点来证明0到1之间的有理数集是不可数的。然而，因为我们知道 $\mathbb{Q}$ 的任何子集都必须是可数的，所以定理1.5.1的证明一定有缺陷。

    (b) 一些数字有两种不同的小数表示。具体来说，任何终止的小数展开也可以用重复的9表示。例如， $1/2$ 可以写成.5或.4999.... 这不会导致一些问题吗？

(a) 表中的小数都是实数，各位数都可以随意列出。如果换成有理数：(1) 表中的小数无法任意排布；(2) 得到的表格外面的数不一定是有理数。因此无法用对角线法证明有理数不可数。

(b) 将所有有限小数都写成它的无限小数形式即可规避该问题。

<br/>

!!! question "练习 1.5.4"
    设 $S$ 为由所有0和1的序列组成的集合。注意， $S$ 不是一个特定的序列，而是一个包含序列作为元素的大集合；即，
    $$
    S = \left\{  {\left( {{a}_{1},{a}_{2},{a}_{3},\ldots }\right)  : {a}_{n} = 0\text{ or }1}\right\}  .
    $$
    例如，序列 $\left( {1,0,1,0,1,0,1,0,\ldots }\right)$ 是 $S$ 的一个元素，序列 $\left( {1,1,1,1,1,1,\ldots }\right)$ 也是。

    给出一个严格的论证，证明 $S$ 是不可数的。

<a id="1.5.4."></a>

假设 $S$ 可数，则可以使用对角线法构造一个如下的表格：

$$
\begin{matrix}
    &1\longleftrightarrow (a_{11},a_{12},a_{13},\ldots)\\
    &2\longleftrightarrow (a_{21},a_{22},a_{23},\ldots)\\
    &3\longleftrightarrow (a_{31},a_{32},a_{33},\ldots)\\
    &\vdots\\
    &d\longleftrightarrow (a_{d1},a_{d2},a_{d3},\ldots)\\
    &\vdots
\end{matrix}
$$

然后构造一个新的序列 $(b_1,b_2,b_3,\ldots)$，其中 $b_i\neq a_{ii}$，则该序列不在表格中，矛盾。

故 $S$ 不可数。

<br/>

!!! question "练习 1.5.5"
    (a) 设 $A = \{ a,b,c\}$ 。列出 $P\left( A\right)$ 的八个元素。(不要忘记 $\varnothing$ 被视为每个集合的子集。)

    (b) 如果 $A$ 是有限的，且有 $n$ 个元素，证明 $P\left( A\right)$ 有 ${2}^{n}$ 个元素。(构造 $A$ 的一个特定子集可以解释为关于是否包含 $A$ 的每个元素的一系列决策。)

(a) $\varnothing,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}$。

(b) 对于 $A$ 的任意子集，都可以用一个 $0-1$ 序列来表示，$1$ 表示该位置的元素在子集中，$0$ 表示不在。因此列出后可得到 $2^n$ 个子集。

<br/>

!!! question "练习 1.5.6"
    (a) 使用特定集合 $A = \{ a,b,c\}$ ，展示从 $A$ 到 $P\left( A\right)$ 的两个不同的1-1映射。

    (b) 设 $B = \{ 1,2,3,4\}$ ，生成一个 $1 - 1$ 映射 $g : B \rightarrow  P\left( B\right)$ 的例子。

    解释为什么在(a)和(b)部分中，不可能构造出满射映射。

(a) $A\to P(A)$：(1) $a\mapsto \{a\}$，(2) $a\mapsto \varnothing$。

(b) $B\to P(B)$：$b\mapsto \{b\}$。

因为 P(A) 中的元素个数远大于 A 中的元素个数，所以不可能有一个满射。

<br/>

!!! question "练习 1.5.7"
    回到练习1.5.6中构造的特定函数，并使用前面的规则构造得到的子集 $B$ 。在每种情况下，注意 $B$ 不在所用函数的值域内。

采用 $A\to P(A)$：(1) $a\mapsto \{a\}$ 的规则，得到 $B=\varnothing$。

<br/>

!!! question "练习 1.5.8"
    (a) 首先，证明情况 ${a}^{\prime } \in  B$ 会导致矛盾。

    (b) 现在，通过证明情况 ${a}^{\prime } \notin  B$ 同样不可接受来完成论证。

(a) 若 $a'\in B$，则 $a'\notin f(a')$，但 $B=f(a')$，矛盾。

(b) 若 $a'\notin B$，则 $a'\in f(a')$，但 $B=f(a')$，矛盾。

所以从 $A$ 到 $P(A)$ 不存在一个满射函数。

<br/>

!!! question "练习 1.5.9"
    作为最后一个练习，通过建立与已知基数集合的一一对应关系来回答以下每个问题。

    (a) 从 $\{ 0,1\}$ 到 $\mathbb{N}$ 的所有函数集合是可数的还是不可数的？

    (b) 从 $\mathbb{N}$ 到 $\{ 0,1\}$ 的所有函数的集合是可数的还是不可数的？

    (c) 给定一个集合 $B$ ， $P\left( B\right)$ 的一个子集 $\mathcal{A}$ 被称为一个反链，如果 $\mathcal{A}$ 的任何元素都不是 $\mathcal{A}$ 中任何其他元素的子集。 $P\left( \mathbb{N}\right)$ 是否包含一个不可数的反链？

(a) 建立 $f:\{0,1\}\to \mathbb{N^+}$: $f(0)=a,f(1)=b$，把所有这样的函数组成集合 $A$ 。我们再建立 $g:A\to  \mathbb{(N^+)^2}$: $g(f)=(a,b)$。显然，$g$ 是一个双射。由前述构造，$\mathbb{N}\sim \mathbb{(N^+)^2}$，所以集合 $A$ 可数。

(b) 同上，建立 $f:\mathbb{N^+}\to \{0,1\}$，这个 $f$ 把正整数序列转换成了无穷的 $0-1$ 序列，由 [$1.5.4.$](#1.5.4.) 可知这样的序列不可数，所以全体 $f$ 组成的集合不可数。

(c) 这里借鉴了别人的解答。

设 $p_m$ 是第 $m$ 个素数。我们利用素数的唯一分解性来构造一个映射：

$$
\Phi:P(\mathbb{N^+})\setminus\left\{\varnothing,\mathbb{N^+}\right\} \to P(\mathbb{N^+}):\\
\Phi\left(X\right)=\left\{p_m^n: m\in X,n\notin X\right\}
$$

记 $\mathcal{A}=\left\{\Phi(X): X\in P(\mathbb{N}^+)\setminus\left\{\varnothing,\mathbb{N^+}\right\}\right\}$，下面我们要证明 $\mathcal{A}$ 是一个不可数的反链，即对任意 $X\neq Y$，都有 $\Phi(X)\not\subseteq \Phi(Y)$ 且 $\Phi(Y)\not\subseteq \Phi(X)$。

首先，由素数的唯一分解性，$\Phi$ 是一个单射。

不妨设 $\exists\ m\in X$，$m\notin Y$（即 $X \not\subseteq Y$），则对某个 $n\notin X$，$p_m^n\in \Phi(X)$，但 $p_m^n\notin \Phi(Y)$（因为底数 $m \notin Y$），所以 $\Phi(X)\not\subseteq \Phi(Y)$。

对于反方向 $\Phi(Y) \not\subseteq \Phi(X)$：
如果 $\exists\ l\in Y$，$l\notin X$（即 $Y \not\subseteq X$），则同理可证 $\Phi(Y)\not\subseteq \Phi(X)$。
如果对 $\forall\ l\in Y$，$l\in X$（即 $Y \subsetneq X$），则对上述 $m$（满足 $m \in X \setminus Y$），任取 $l \in Y$，考察元素 $z = p_l^m$。
$z \in \Phi(Y)$（因底数 $l \in Y$，指数 $m \notin Y$）。
但 $z \notin \Phi(X)$（因指数 $m \in X$，不满足 $\Phi(X)$ 的定义要求）。
所以 $\Phi(Y)\not\subseteq \Phi(X)$。

综上，$\mathcal{A}$ 中任何元素都不是其他元素的子集。又因为 $P(\mathbb{N^+})\setminus\left\{\varnothing,\mathbb{N^+}\right\}$ 是不可数的，所以 $\mathcal{A}$ 也是不可数的。

所以，$\mathcal{A}$ 就是一个不可数的反链。

---

# 数列与级数

## 习题 2.2 序列的极限

!!! question "练习 2.2.1"
    使用序列收敛的定义，验证以下序列收敛于所提出的极限。
    
    (a) \(\lim \frac{1}{\left( 6{n}^{2} + 1\right) } = 0\) .
    
    (b) \(\lim \frac{{3n} + 1)}{\left( 2n + 5\right) } = \frac{3}{2}\) .
    
    (c) \(\lim \frac{2}{\sqrt{n + 3}} = 0\) .

(a) 选取一个 $\varepsilon>0$，我们寻找 $N\in \mathbb{N^+}$ 使得 $\displaystyle\frac{1}{6N^2+1}<\varepsilon$。事实上，因为 $\displaystyle\frac{1}{6N^2+1}<\frac{1}{N}$，令 $\displaystyle \frac{1}{N}<\varepsilon$，得出 $\displaystyle N>\frac{1}{\varepsilon}$ 即可，于是对 $\forall\ n>N$，都有 $\displaystyle\frac{1}{6n^2+1}-0<\varepsilon$。

(b) 相似地，令 $\displaystyle \left|\frac{3N+1}{2N+5}-\frac{3}{2}\right|=\frac{13}{4N+10}<\frac{13}{4N}<\varepsilon$，得出 $\displaystyle N>\frac{13}{4\varepsilon}$。

(c) 同理。

<br/>


!!! question "练习 2.2.2"
    如果我们在定义2.2.3中颠倒量词的顺序，会发生什么？
    
    定义:一个序列 \(\left( {x}_{n}\right)\) verconges到 \(x\) ，如果存在一个 \(\varepsilon  > 0\) ，使得对于所有 \(N \in  \mathbb{N}\) ， \(n \geq  N\) 蕴含 \(\left| {{x}_{n} - x}\right|  < \varepsilon\) 成立。
    
    给出一个vercongent序列的例子。你能给出一个发散但vergonent序列的例子吗？这个奇怪的定义到底在描述什么？

$\exists\ \varepsilon>0$，对 $\forall\ N\in \mathbb{N^+}$，只要 $n\geq N$ 就有 $|a_n-a|<\varepsilon$。

其实这就是说 $a_n$ 是有界的。

例如：$\displaystyle a_n=(-1)^n$，取 $\varepsilon=1.1$，$a=0$。

<br/>


!!! question "练习 2.2.3"
    描述为了反驳以下每个陈述，我们需要证明什么。
    
    (a) 在美国的每一所大学里，都有一个至少七英尺高的学生。
    
    (b) 对于美国的所有大学，都存在一位教授给每个学生A或B的成绩。
    
    在美国有一所大学，那里的每个学生都至少有六英尺高。

(a) 在美国某一所大学里，有一个没有七英尺高的学生。

(b) 在美国某一所大学里，没有一位给学生 $A$ 或 $B$ 成绩的教授。

(c) 在美国所有大学里，都有一位没有六英尺高的学生。

<br/>


!!! question "练习 2.2.4"
    论证该序列
    
    $$
    1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,\left( {5\text{ zeros }}\right) ,1,\ldots
    $$
    
    不收敛于零。对于哪些 \(\varepsilon  > 0\) 值存在响应 \(N\) 。对于哪些 \(\varepsilon  > 0\) 值没有合适的响应？

我们假设它以 $0$ 为极限，那么对于 $\varepsilon\geq 1$ 有效，对于 $\varepsilon<1$ 无效。事实上，由于这个数列永远都会在 $0,1$ 之间跳动，所以不可能以 $0$ 为极限。

<br/>


!!! question "练习 2.2.5"
    设 \(\left\lbrack  \left\lbrack  x\right\rbrack  \right\rbrack\) 为小于或等于 \(x\) 的最大整数。例如， \(\left\lbrack  \left\lbrack  \pi \right\rbrack  \right\rbrack   = 3\) 和 \(\left\lbrack  \left\lbrack  3\right\rbrack  \right\rbrack   = 3\) 。求 \(\lim {a}_{n}\) 并为每个结论提供证明，如果
    
    (a) \({a}_{n} = \left\lbrack  \left\lbrack  {1/n}\right\rbrack  \right\rbrack\) ,
    
    (b) \({a}_{n} = \left\lbrack  \left\lbrack  {\left( {{10} + n}\right) /{2n}}\right\rbrack  \right\rbrack\) .
    
    反思这些例子，评论定义 2.2.3 之后的陈述:“ \(\varepsilon\) -邻域越小， \(N\) 可能需要越大。”

(a) 对于 $\displaystyle a_n=[[\frac{1}{n}]]$，除了 $a_1=1$，其余项均为 $0$，所以它以 $0$ 为极限。

(b) 对于 $\displaystyle a_n=[[\frac{10+n}{2n}]]$， 当 $n>10$ 时均为 $0$，所以它以 $0$ 为极限。

“$\varepsilon$-邻域越小，$N$ 可能需要越大”是对所有收敛数列的普遍刻画，但并不是说 $N$ 一定会随着 $\varepsilon$ 的减小而增大。

<br/>


!!! question "练习 2.2.6"
    假设对于特定的 \(\varepsilon  > 0\) ，我们已经找到了一个合适的 \(N\) 值，该值在定义2.2.3的意义上对给定序列“有效”。
    
    (a) 那么，任何更大/更小(选择一个)的 \(N\) 也将对相同的 \(\varepsilon  > 0\) 有效。
    
    (b) 那么，相同的 \(N\) 也将对任何更大/更小的 \(\varepsilon\) 值有效。

(a) (b) 均为更大，用不等式的传递性得出结论。

<br/>


!!! question "练习 2.2.7"
    非正式地说，序列 \(\sqrt{n}\) “收敛到无穷大”。
    
    (a) 模仿定义2.2.3的逻辑结构，为数学陈述 \(\lim {x}_{n} = \infty\) 创建一个严格的定义。使用这个定义来证明 \(\lim \sqrt{n} = \infty\) 。
    
    (b) 你在(a)中的定义对特定序列 \(\left( {1,0,2,0,3,0,4,0,5,0,\ldots }\right)\) 说了什么？

(a) 对 $\forall\ G>0$，$\exists\ N\in \mathbb{N^+}$ 使得 $\forall\ n\geq N$，都有 $a_n>G$。

对于 $a_n=\sqrt{n}$，取 $N>G^2$ 即可。

(b) 因为总 $\exists\ k\in \mathbb{N^+}$ 使得 $a_k=0$，所以它不满足 (a) 中定义，不收敛到无穷大。

<br/>


!!! question "练习 2.2.8"
    这里有两个有用的定义:
    
    (i) 一个序列 \(\left( {a}_{n}\right)\) 最终在一个集合 \(A \subseteq  \mathbb{R}\) 中，如果存在一个 \(N \in  \mathbb{N}\) 使得对于所有 \(n \geq  N\) ， \({a}_{n} \in  A\) 。
    
    (ii) 一个序列 \(\left( {a}_{n}\right)\) 频繁在一个集合 \(A \subseteq  \mathbb{R}\) 中，如果对于每一个 \(N \in  \mathbb{N}\) ，存在一个 \(n \geq  N\) 使得 \({a}_{n} \in  A\) 。
    
    (a) 序列 \({\left( -1\right) }^{n}\) 是最终还是频繁在集合 \(\{ 1\}\) 中？
    
    (b) 哪个定义更强？频繁是否意味着最终，还是最终意味着频繁？
    
    (c) 使用频繁或最终重新表述定义 2.2.3B。我们想要的是哪个术语？
    
    (d) 假设一个序列 \(\left( {x}_{n}\right)\) 的无限多项等于2。 \(\left( {x}_{n}\right)\) 是否必然最终在区间(1.9,2.1)内？它是否频繁出现在(1.9,2.1)内？

(a) 频繁。

(b) (i) 定义更强，最终也意味着频繁。

(c)  使用“最终”术语：$(a_n)$ 收敛于 $a$，若对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$ 使得 $\forall\ n\geq N$，都有 $a_n\in (a-\varepsilon,a+\varepsilon)$。

(d) 如果它还在其它数上跳跃，那么可能不最终，但因为总有 $a_k=2\in (1.9,2.1)$，所以频繁。

---

## 习题 2.3 代数极限定理与序极限定理

!!! question "练习 2.3.1"
    证明常数序列 \(\left( {a,a,a,a,\ldots }\right)\) 收敛到 \(a\) 。

 严谨地写一遍，对 $\forall\ \varepsilon>0$，$|a_n-a|=0<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty} a_n=a$。

<br/>


!!! question "练习 2.3.2"
    设 \({x}_{n} \geq  0\) 对于所有 \(n \in  \mathbb{N}\) 。
    
    (a) 如果 \(\left( {x}_{n}\right)  \rightarrow  0\) ，证明 \(\left( \sqrt{{x}_{n}}\right)  \rightarrow  0\) 。
    
    (b) 如果 \(\left( {x}_{n}\right)  \rightarrow  x\) ，证明 \(\left( \sqrt{{x}_{n}}\right)  \rightarrow  \sqrt{x}\) 。

(a) 由题意，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$， 使得对 $\forall\ n>N$，有 $|x_n-0|<\varepsilon^2$。即 $|\sqrt{x_n}-0|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty} \sqrt{x_n}=0$。

(b) 由 (a) 同样的操作，可得对某个 $n>N_1$，$|x_n-x|<C\varepsilon$，其中 $C$ 可以是大于 $0$ 的任意常数。由 $\displaystyle|\sqrt{x_n}-\sqrt{x}|=\frac{|x_n-x|}{\sqrt{x_n}+\sqrt{x}}$，考虑 $\sqrt{x_n}+\sqrt{x}$ 的下界即可。

由于 $\displaystyle\lim_{n\to \infty}x_n=x$，那么 $\exists\ N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_2$，有 $\displaystyle x_n>\frac{x}{2}$。所以取 $C=\displaystyle\frac{1}{\sqrt{\displaystyle\frac{x}{2}}+\sqrt{x}}$，并让 $N>\max\{N_1,N_2\}$，则有 $\displaystyle|\sqrt{x_n}-\sqrt{x}|=\frac{|x_n-x|}{\sqrt{x_n}+\sqrt{x}}<\varepsilon$。这样就得到 $\displaystyle\lim_{n\to\infty}\sqrt{x_n}= \sqrt{x}$。

<br/>


!!! question "练习 2.3.3"
    (夹逼定理)。证明如果对于所有 \(n \in\)  \(\mathbb{N}\) 有 \({x}_{n} \leq  {y}_{n} \leq  {z}_{n}\) ，且如果 \(\lim {x}_{n} = \lim {z}_{n} = l\) ，则 \(\lim {y}_{n} = l\) 也成立。

使用两次序极限定理，得到 $\displaystyle\lim_{n\to\infty}x_n\leq\lim_{n\to\infty}y_n\leq\lim_{n\to\infty}z_n$。由此可得 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=\lim_{n\to\infty}z_n=l$。

<br/>


!!! question "练习 2.3.4"
    证明极限如果存在，则必须是唯一的。换句话说，假设 \(\lim {a}_{n} = {l}_{1}\) 和 \(\lim {a}_{n} = {l}_{2}\) ，并证明 \({l}_{1} = {l}_{2}\) 。

不失一般性，不妨设 $l_1>l_2$，利用 $l_1,l_2$ 的间距，以及数列与极限间距离随项数增大会小于任何间距得出矛盾。

由定义，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，有 $\displaystyle|a_n-l_1|<\frac{l_1-l_2}{2}$，因此 $\displaystyle a_n>\frac{l_1+l_2}{2}$，所以 $\displaystyle\lim_{n\to\infty} a_n\geq \frac{l_1+l_2}{2}>l_2$，这与 $\displaystyle\lim_{n\to\infty} a_n=l_2$ 矛盾。

所以 $l_1=l_2$，极限有唯一性。

<br/>

$2.3.5.$<a id="2.3.5."></a>

$\Rightarrow$) 若 $\{z_n\}$ 收敛，则 $\exists\ z\in \mathbb{R}$，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，有 $|z_n-z|<\varepsilon$。即 $|x_n-z|<\varepsilon$ 和 $|y_n-z|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=z$。

$\Leftarrow)$ 若 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=z$，则对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，有 $|x_n-z|<\varepsilon$，对 $\forall\ n>N_2$，有 $|y_n-z|<\varepsilon$。取 $N=\max\{N_1,N_2\}$，则对 $\forall\ n>N$，有 $|x_{2n}-z|<\varepsilon$ 和 $|y_{2n}-z|<\varepsilon$，即 $|z_n-z|<\varepsilon$，所以 $\{z_n\}$ 收敛。

<br/>


!!! question "练习 2.3.6"
    (a) 证明如果 \(\left( {b}_{n}\right)  \rightarrow  b\) ，则绝对值序列 \(\left| {b}_{n}\right|\) 收敛到 \(\left| b\right|\) 。
    
    (b) 部分(a)的逆命题是否成立？如果我们知道 \(\left| {b}_{n}\right|  \rightarrow  \left| b\right|\) ，能否推断出 \(\left( {b}_{n}\right)  \rightarrow  b\) ？

(a)  对于单独的绝对值，尝试使用绝对值不等式 $||b_n|-|b||\leq |b_n-b|<\varepsilon$，所以 $\displaystyle \lim_{n\to\infty}|b_n|=|b|$。

(b) 不等式的反向是不成立的。考虑 $b_n=(-1)^n$，则 $\displaystyle\lim_{n\to\infty}|b_n|=1$，但 $\{b_n\}$ 发散。

<br/>


!!! question "练习 2.3.7"
    (a) 设 \(\left( {a}_{n}\right)\) 为有界(不一定收敛)序列，并假设 \(\lim {b}_{n} = 0\) 。证明 \(\lim \left( {{a}_{n}{b}_{n}}\right)  = 0\) 。为什么我们不能使用代数极限定理来证明这一点？
    
    (b) 如果我们假设 \(\left( {b}_{n}\right)\) 收敛到某个非零极限 \(b\) ，能否得出关于 \(\left( {{a}_{n}{b}_{n}}\right)\) 收敛性的任何结论？
    
    (c) 使用(a)来证明定理2.3.3的第(iii)部分，当 \(a = 0\) 时的情况。

(a) $\{a_n\}$ 发散的情况下并不能使用代数极限定理。这里利用有界性进行证明。

$\{a_n\}$ 有界即 $\exists\ M>0$，对 $\forall\ n\in \mathbb{N^+}$，有 $|a_n|<M$。所以 $|a_nb_n|=|a_n||b_n|<M|b_n|$，再令 $\displaystyle|b_n-b|<\frac{\varepsilon}{M}$ 即得 $\displaystyle\lim_{n\to\infty}a_nb_n=0$。

(b) 不能，$\{a_n\}$ 任意跳动的情况下，$\{a_nb_n\}$ 也会任意跳动。

(c) $\{b_n\}$ 收敛即有界，使用 (a) 的结论即可。

<br/>


!!! question "练习 2.3.8"
    给出以下每种情况的例子，或通过引用适当的定理说明这样的请求是不可能的:
    
    (a) 序列 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) ，两者都发散，但它们的和 \(\left( {{x}_{n} + {y}_{n}}\right)\) 收敛；
    
    (b) 序列 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) ，其中 \(\left( {x}_{n}\right)\) 收敛， \(\left( {y}_{n}\right)\) 发散，且 \(\left( {{x}_{n} + }\right.\)  \(\left. {y}_{n}\right)\) 收敛；
    
    (c) 一个收敛的序列 \(\left( {b}_{n}\right)\) ，对于所有 \(n\) 满足 \({b}_{n} \neq  0\) ，使得 \(\left( {1/{b}_{n}}\right)\) 发散；
    
    (d) 一个无界序列 \(\left( {a}_{n}\right)\) 和一个收敛序列 \(\left( {b}_{n}\right)\) ，其中 \(\left( {{a}_{n} - }\right.\)  \(\left. {b}_{n}\right)\) 有界；
    
    (e) 两个序列 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) ，其中 \(\left( {{a}_{n}{b}_{n}}\right)\) 和 \(\left( {a}_{n}\right)\) 收敛但 \(\left( {b}_{n}\right)\) 不收敛。

(a) $x_n=n$，$y_n=-n$ 是可能的。

(b) 由代数极限定理，两个收敛数列的和或差一定收敛，所以不可能。

(c) $b_n=\displaystyle\frac{1}{n}$ 是可能的。

(d) 用绝对值不等式 $|a_n|=|(a_n-b_n)+b_n|\leq |a_n-b_n|+|b_n|$，如果 $\{a_n-b_n\}$ 和 $\{b_n\}$ 都有界，则 $\{a_n\}$ 必有界，所以不可能。

(e) $a_n=0$ 是可能的。

<br/>


!!! question "练习 2.3.9"
    如果所有不等式都假设为严格不等式，定理 2.3.4 是否仍然成立？例如，如果我们假设一个收敛序列 \(\left( {x}_{n}\right)\) 对所有 \(n \in  \mathbb{N}\) 满足 \({x}_{n} > 0\) ，我们可以得出关于极限的什么结论？

不成立。

如果 $x_n>0$，沿用定理的证明，则极限 $x=0$ 的时候也能成立。所以 $x\geq 0$。

<br/>


!!! question "练习 2.3.10"
    如果 \(\left( {a}_{n}\right)  \rightarrow  0\) 且 \(\left| {{b}_{n} - b}\right|  \leq  {a}_{n}\) ，则证明 \(\left( {b}_{n}\right)  \rightarrow  b\) 。

由题，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|a_n|<\varepsilon$，所以 $|b_n-b|\leq |a_n|<\varepsilon$。所以 $\displaystyle\lim_{n\to\infty}b_n=b$。

<br/>


!!! question "练习 2.3.11"
    (切萨罗均值)。证明如果 \(\left( {x}_{n}\right)\) 是一个收敛序列，则由平均值给出的序列
    
    $$
    {y}_{n} = \frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n}
    $$
    
    也收敛到相同的极限。
    
    举一个例子说明，即使 \(\left( {x}_{n}\right)\) 不收敛，平均值序列 \(\left( {y}_{n}\right)\) 也可能收敛。

<a id="4">极限平均值定理与反向情况下的反例</a>

假设 $\displaystyle\lim_{n\to\infty}x_n=x$，考虑将平均值转化为极限的形式：

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|
$$

我们以 $N$ 为界限进行拆分：假设 $N$ 是满足对 $\forall\ n>N$，有 $|x_n-x|<\varepsilon$ 的正整数，则有

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|<\frac{1}{n}(\sum_{k=1}^N|x_k-x|+(n-N)\varepsilon)
$$

再利用有界性，$\exists\ M>0$，使得对 $\forall\ k\in \mathbb{N^+}$，有 $|x_k|<M$，则有 $|x_k-x|\leq |x_k|+|x|<M+|x|$。所以

$$\begin{align*}
    |\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|&<\frac{1}{n}(N(M+|x|)+(n-N)\varepsilon)\\
    &<\frac{1}{n}(N(M+|x|))+\varepsilon
\end{align*}
$$

当然，$\exists\ N_1\in \mathbb{N^+}$，$N_1>N$，使得对 $\forall\ n>N_1$，有 $\displaystyle\frac{1}{n}(N(M+|x|))<\varepsilon$，所以

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|<2\varepsilon
$$

所以 $\displaystyle\lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=x=\displaystyle\lim_{n\to\infty}x_n$。

对于下一个问题，我先考虑了 $\{x_n\}$ 的增长度小于 $n$ 的情况，比如 $x_n=\sqrt{n}$，但这并不能说明问题。后来我尝试反向证明，得到了这样一串式子：

$$
\begin{align*}
     |\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|&=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|\\
     &\leq \frac{1}{n}\displaystyle\sum_{k=1}^n|x_k-x|\\
     &\leq \frac{1}{n}|x_n-x|\\
     &<\frac{1}{n}n\varepsilon=\varepsilon
\end{align*}
$$

这个式子是不成立的，但它的确给了我启发：对于 $\{x_n\}$ 单调递增（趋近于 $x$）的情况， 貌似可以符合上面的条件。我没有直接证明这一点，但我想到了另外一种思路来构造反例 $\{x_n\}$：让它左右跳动，连上面的式子都不成立。比如 $\displaystyle x_n=(-1)^n$。不难得出 $\displaystyle\lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=0$，但是 $\{x_n\}$ 发散。

<br/>


!!! question "练习 2.3.12"
    考虑双索引数组 \({a}_{m,n} = m/\left( {m + n}\right)\) 。
    
    (a) 直观地说， \(\mathop{\lim }\limits_{{m,n \rightarrow  \infty }}{a}_{m,n}\) 应该代表什么？计算“迭代”极限
    
    $$
    \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\lim }\limits_{{m \rightarrow  \infty }}{a}_{m,n}\;\text{ and }\;\mathop{\lim }\limits_{{m \rightarrow  \infty }}\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{m,n}.
    $$
    
    (b) 以定义2.2.3的风格为以下陈述制定一个严格的定义
    
    $$
    \mathop{\lim }\limits_{{m,n \rightarrow  \infty }}{a}_{m,n} = l
    $$

(a) 直观来讲，$\displaystyle\lim_{m,n\to\infty}a_{m,n}$ 应当表示 $m,n$ 同时趋于无穷时 $\{a_n\}$ 的极限。

$\displaystyle\lim_{n\to\infty}\displaystyle\lim_{m\to\infty}a_{m,n}=\displaystyle\lim_{n\to\infty}1=1$，$\displaystyle\lim_{m\to\infty}\displaystyle\lim_{n\to\infty}a_{m,n}=\displaystyle\lim_{m\to\infty}0=0$。

所以上面的直观难以给我们一个准确的答案，我们需要更清晰的定义，例如规定 $m,n$ 的取极限顺序。

(b) 若对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，对 $\forall\ n>N_1$，$m>N_2$，$|a_{m,n}-b_m|<\varepsilon$，$|b_m-l|<\varepsilon$，则有 $\displaystyle\lim_{m,n\to\infty}a_{m,n}=l$。

---

## 习题 2.4 单调收敛定理与无穷级数初探

!!! question "练习 2.4.1"
    通过证明如果级数 \(\mathop{\sum }\limits_{{n = 0}}^{\infty }{2}^{n}{b}_{{2}^{n}}\) 发散，那么 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\) 也发散，来完成定理2.4.6的证明。示例2.4.5可能是一个有用的参考。

若级数 $\displaystyle\sum_{n=0}^{\infty}2^nb_{2^n}$ 发散，则考虑在 $\displaystyle\sum_{n=1}^{\infty}b_n$ 中构造该级数以证明其发散。

固定 $m\in \mathbb{N^+}$，则总存在 $t\in \mathbb{N}$ 使 $2^t\leq m$，因此

$$
\begin{align*}
    \displaystyle\sum_{n=1}^{m}b_n&=b_1+b_2+\cdots+b_m\\
    &\geq b_1+b_2+\cdots+b_{2^t}\\
    &=b_1+b_2+(b_3+b_4)+\cdots+(b_{2^{t-1}+1}+b_{2^{t-1}+2}+\cdots+b_{2^t})\\
    &\geq b_1+b_2+2b_4+4b_8+\cdots+2^{t-1}b_{2^t}\\
    &=\displaystyle\frac{1}{2}b_1+\displaystyle\frac{1}{2}\displaystyle\sum_{n=0}^{t}2^nb_{2^n}\\
    &\geq \displaystyle\frac{1}{2}\displaystyle\sum_{n=0}^{t}2^nb_{2^n}.
\end{align*}
$$

对 $\forall\ G>0$，$\exists\ t\in \mathbb{N}$ 使 $\displaystyle\sum_{n=0}^{t}2^nb_{2^n}>2G$，即 $\exists\ m\in \mathbb{N^+}$ 使 $\displaystyle\sum_{n=1}^{m}b_n>G$。

所以 $\displaystyle\sum_{n=1}^{\infty}b_n$ 发散。

<br/>

$2.4.2.$<a id="2.4.2"></a>

(a) 计算可得 $x_2=1<x_1$，$x_3=\displaystyle\frac{1}{3}<x_2$，$\cdots$ 大胆猜想 $\{x_n\}$ 是单调递减的，配合单调有界定理证明其收敛。

假设 $x_{n+1}<x_n$，即 $\displaystyle\frac{1}{4-x_n}<x_n$，整理得 $\displaystyle\frac{x_n^2-4x_n+1}{4-x_n}<0$，考虑到原题中 $x_1=3<4$，可得 $x_n^2-4x_n+1<0$。设 $x^2-4x+1=0$ 两根分别为 $t_1<t_2$，那么 $x_n\in (t_1,t_2)$。

下面证明 $x_{n+2}<x_{n+1}$，利用同样的方法化简得到 $\displaystyle\frac{x_{n+1}^2-4x_{n+1}+1}{4-x_{n+1}}<0$。下面判断这个不等式的正负。

要判断它的正负，关键是求解 $x_{n+1}$ 的范围，而 $x_{n+1}$ 的范围又由 $x_{n}$ 所控制，所以我们考虑 $x_n\in (t_1,t_2)$ 时对 $x_{n+1}$ 的影响。

分析 $x^2-4x+1=0$ 解的范围，可知 $0<t_1<t_2<4$。由于 $x_{n+1}=\displaystyle\frac{1}{4-x_n}$，所以 $x_{n+1}\in (\displaystyle\frac{1}{4-t_1},\displaystyle\frac{1}{4-t_2})$。此时直接化简有些困难，于是我思考了这一方程的来历，发现这一方程就是 $x=\displaystyle\frac{1}{4-x}$ 的变形，于是 $x_{n+1}\in (t_1,t_2)$。

上面由 $x_{n+2}<x_{n+1}$ 得到的那个不等式因为形式完全一致，所以成立。

所以 $x_{n+2}<x_{n+1}$。

由数学归纳法可得 $\{x_n\}$ 单调递减。又因为 $x_n\in (t_1,t_2)$ 对 $\forall\ n\in \mathbb{N^+}$ 成立，所以 $\{x_n\}$ 有界，由单调有界定理可知其收敛。

(b) $\displaystyle\lim_{n\to\infty}x_n$ 与 $\displaystyle\lim_{n\to\infty}x_{n+1}$ 的意义是相同的。下面我们用极限定义严格地说明一下这一点。

设 $\displaystyle\lim_{n\to\infty}x_n=A$，即对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$, $|x_n-A|<\varepsilon$。取 $N_2=N_1-1$，则对 $\forall\ n>N_2$，$|x_{n+1}-A|<\varepsilon$。所以 $\displaystyle\lim_{n\to\infty}x_{n+1}=A$。

反向的证明可以使用同样的操作。

对 (a) 中递推公式左右取极限，可得 $A=\displaystyle\frac{1}{4-A}$，解得 $A=2-\sqrt{3}$ 或 $A=2+\sqrt{3}$，考虑原式里 $x_n$ 始终小于 $3$ 的事实，由序极限定理可知 $A\leq 3<2+\sqrt{3}$，所以 $\displaystyle\lim_{n\to\infty}x_n=A=2-\sqrt{3}$。

<br/>


!!! question "练习 2.4.3"
    按照练习2.4.2的模型，证明由 \({y}_{1} = 1\) 和 \({y}_{n + 1} = 4 - 1/{y}_{n}\) 定义的序列收敛并求出极限。

使用 [$2.4.2$](#2.4.2) 中完全一致的方法就可以得出结论。

其一：$y_n$ 是单调递增的，且 $y_n<4$，所以 $y_n$ 收敛。

其二：两边同时取极限得到 $A=4-\displaystyle\frac{1}{A}$，其实这个方程的两解跟上一题完全一样，不过这次因为 $y_n>1$ 是恒成立的，所以 $\displaystyle\lim_{n\to\infty}y_n=A=2+\sqrt{3}$。

<br/>


!!! question "练习 2.4.4"
    证明
    
    $$
    \sqrt{2},\sqrt{2\sqrt{2}},\sqrt{2\sqrt{2\sqrt{2}}},\ldots
    $$
    
    收敛并求出极限。

把它写成数列形式如下：

$$
    x_{n+1}=\sqrt{2x_n},\quad x_1=\sqrt{2}\,.
$$

先试探数列单调性，假设 $x_{n+1}>x_n$，化简得到 $x_n<2$，从而 $x_{n+1}=\sqrt{2x_n}<2$，所以 $x_{n+2}=\sqrt{2x_{n+1}}<x_{n+1}$。又因为 $x_1=\sqrt{2}<2$，假设成立，数列单调递增。

又因为对 $\forall\ n\in \mathbb{N^+}$，$\sqrt{2}\leq x_n<2$，由单调有界定理知其收敛。

两边同时取极限得到 $A=\sqrt{2A}$，解得 $A=2$ 或 $A=0$，又因为 $\sqrt{2}\leq x_n$，由序极限定理 $\displaystyle\lim_{n\to\infty}x_n=A=2$。

<br/>


!!! question "练习 2.4.5"
    (计算平方根)。设 \({x}_{1} = 2\) ，并定义
    
    $$
    {x}_{n + 1} = \frac{1}{2}\left( {{x}_{n} + \frac{2}{{x}_{n}}}\right) .
    $$
    
    (a) 证明 \({x}_{n}^{2}\) 总是大于2，然后利用这一点证明 \({x}_{n} - {x}_{n + 1} \geq  0\) 。由此得出结论 \(\lim {x}_{n} = \sqrt{2}\) 。
    
    (b) 修改序列 \(\left( {x}_{n}\right)\) 使其收敛到 \(\sqrt{c}\) 。

(a) 若 $x_n>0$，则 $x_{n+1}=\displaystyle\frac{1}{2}(x_n+\frac{2}{x_n})>0$。考虑均值不等式 

$$
    \displaystyle\frac{1}{2}(x_n+\frac{2}{x_n})\geq \sqrt{x_n\cdot\frac{2}{x_n}}=\sqrt{2}
$$

所以 $x_{n+1}\geq \sqrt{2}$。又因为 $x_1=2$，$x_n\neq \sqrt{2}$ 时 $x_{n+1}\neq \sqrt{2}$，所以无法取等， $x_n^2>2$。

下面借助这一点证明其单调性。令 $x_{n+1}-x_n$ 得到

$$
    x_{n+1}-x_n=\displaystyle\frac{1}{2}(x_n+\displaystyle\frac{2}{x_n})-x_n=\displaystyle\frac{2-x_n^2}{2x_n}<0
$$

所以 $\{x_n\}$ 单调递减。由之前不等式知其有界，由单调有界定理可知其收敛。

两边同时取极限，利用 $x_n>0$ 舍去一根解出 $\displaystyle\lim_{n\to\infty}x_n=\sqrt{2}$。

(b) $x_{n+1}=\displaystyle\frac{1}{2}(x_n+\displaystyle\frac{c}{x_n})$ 其中 $c>0$。再规定 $x_1>0$。

<br/>


!!! question "练习 2.4.6"
    (上极限)。设 \(\left( {a}_{n}\right)\) 是一个有界序列。
    
    (a) 证明由 \({y}_{n} = \sup \left\{  {{a}_{k} : k \geq  n}\right\}\) 定义的序列收敛。
    
    (b) \(\left( {a}_{n}\right)\) 的上极限，或 \(\limsup {a}_{n}\) ，定义为
    
    $$
    \lim \sup {a}_{n} = \lim {y}_{n},
    $$
    
    其中 \({y}_{n}\) 是本练习部分 (a) 中的序列。为 \(\liminf {a}_{n}\) 提供一个合理的定义，并简要解释为什么它对任何有界序列总是存在。
    
    (c) 证明对于每个有界序列 \(\liminf {a}_{n} \leq  \limsup {a}_{n}\) ，并给出一个不等式严格成立的序列示例。
    
    证明 \(\liminf {a}_{n} = \limsup {a}_{n}\) 当且仅当 \(\lim {a}_{n}\) 存在。在这种情况下，三者共享相同的值。

(a) 用单调有界定理证明。

如果对 $\forall\ n\in \mathbb{N^+}$，$\exists\ G>0$ 使得 $|x_n|<G$，则 $|y_n|<G$ 同样成立，故 $\{y_n\}$ 有界。

若 $\exists\ k>n$ 使 $x_k\geq x_n$ 则有 $y_n=y_{n+1}$，否则 $y_n=x_n>y_{n+1}$，所以 $\{y_n\}$ 单调递减。

由单调有界定理可知 $\{y_n\}$ 收敛。

(b) 令 $z_n=\inf \{a_k:k\geq n\}$，$\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}z_n$。

同 (a)，它是单调的，又因为它有界，所以它收敛。

(c) $z_n\leq a_n\leq y_n$，得出 $z_n\leq y_n$，利用序极限定理即可证明。

例如 $a_n=(-1)^n$ 时不等式会严格成立。

$\Rightarrow$) 若 $\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}\sup a_n$，则由夹逼定理可知 $\{a_n\}$ 收敛。

$\Leftarrow$) 若 $\{a_n\}$ 收敛，设 $\displaystyle\lim_{n\to\infty}a_n=A$。

首先，$\{a_n\}$ 有界，$\displaystyle\lim_{n\to\infty}z_n$ 与 $\displaystyle\lim_{n\to\infty}y_n$ 均存在。

然后，对 $\forall\ \varepsilon>0$，$\exists\ N>0$ 使得对 $\forall\ n>N$，$|a_n-A|<\displaystyle\frac{\varepsilon}{2}$，即 $A-\displaystyle\frac{\varepsilon}{2}<a_n<A+\displaystyle\frac{\varepsilon}{2}$。

若 $\exists\ k>N$ 使得 $z_k<A-\displaystyle\frac{\varepsilon}{2}$，则由下确界的性质可知 $\exists\ m\geq k$ 使得 $a_m\leq A-\displaystyle\frac{\varepsilon}{2}$，矛盾，所以：

$$
    A-\varepsilon<A-\displaystyle\frac{\varepsilon}{2}\leq z_n\leq a_n<A+\varepsilon\\
    |z_n-A|<\varepsilon
$$

所以 $\displaystyle\lim_{n\to\infty}z_n=A$。同理反向可证 $\displaystyle\lim_{n\to\infty}y_n=A$。

综上，$\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}\sup a_n$ 当且仅当 $\displaystyle\lim_{n\to\infty}a_n$ 存在。

---

## 习题 2.5 子列与 Bolzano-Weierstrass 定理

!!! question "练习 2.5.1"
    证明定理2.5.2。

设 $\displaystyle\lim_{n\to\infty}a_n=L$，则对 $\forall\ \varepsilon>0$，$\exists\ N>0$，使得 当 $n>N$ 时，$|a_n-L|<\varepsilon$。考虑子列 $a_{n_k}$，由于 $n_k\geq k$，所以对 $\forall\ k>N$，有 $n_k>N$，从而 $|a_{n_k}-L|<\varepsilon$。因此 $\displaystyle\lim_{k\to\infty}a_{n_k}=L$。

<br/>


!!! question "练习 2.5.2"
    (a) 证明如果一个无穷级数收敛，则结合律成立。假设 \({a}_{1} + {a}_{2} + {a}_{3} + {a}_{4} + {a}_{5} + \cdots\) 收敛到极限 \(L\) (即，部分和序列 \(\left( {s}_{n}\right)  \rightarrow  L\) )。证明任何对项的重组
    
    $$
    \left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{{n}_{1}}}\right)  + \left( {{a}_{{n}_{1} + 1} + \cdots  + {a}_{{n}_{2}}}\right)  + \left( {{a}_{{n}_{2} + 1} + \cdots  + {a}_{{n}_{3}}}\right)  + \cdots
    $$
    
    都会导致一个同样收敛到 \(L\) 的级数。
    
    (b) 将此结果与第2.1节末尾讨论的例子进行比较，其中无穷加法被证明不满足结合律。为什么我们在(a)中的证明不适用于这个例子？

(a) 定义 $s_{n_k}=\displaystyle\sum_{i=1}^{n_k}a_i$，$k\in \mathbb{N^+}$，则 $\{s_{n_k}\}$ 是 $\{s_n\}$ 的子列。所以 $\displaystyle\lim_{k\to\infty}s_{n_k}=\displaystyle\lim_{n\to\infty}s_n=L$。

别看错了，这不是黎曼重排定理，事实上，级数的结合律只是把相邻的数加在一起而已，甚至没有改变顺序，所以敛散性和原级数应该一致。

举个例子，$\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2}+\displaystyle\frac{1}{4}+\displaystyle\frac{1}{4}+\cdots=\left(\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2}\right)+\left(\displaystyle\frac{1}{4}+\displaystyle\frac{1}{4}\right)+\cdots=1+\displaystyle\frac{1}{2}+\cdots$。

(b) 因为那个级数是不收敛的。

<br/>


!!! question "练习 2.5.3"
    给出以下每种情况的例子，或论证这样的请求是不可能的。
    
    (a) 一个不包含0或1作为项的序列，但包含收敛到这些值的子列。
    
    (b) 一个单调但发散的序列，且具有收敛的子列。
    
    (c) 一个包含收敛到无限集 \(\{ 1,1/2,1/3,1/4,1/5,\ldots \}\) 中每个点的子列的序列。
    
    一个具有收敛子列的无界序列。
    
    一个具有有界子列但不包含任何收敛子列的序列。

(a) 构造交替子列，极限分别为 $0,1$ 即可。例如 $\{\displaystyle\frac{1}{2n}\}$ 和 $\{1-\displaystyle\frac{1}{2n}\}$。放 $2n$ 的目的是防止 $0,1$ 出现在其中。

(b) 这是不可能的。不妨设它单调递增，因为原数列的任意序列到最后都会变得很大，因此发散，下面我们来证明这一点。

其实要证的就是对 $\forall\ G>0$，存在 $N>0$，使得当 $n\geq N$ 时，$a_n>G$。首先，$\exists\ N>0$ 使得 $a_N>G$，是无误的，然后由原数列单调递增，$\forall\ n\geq N$，都有 $a_n\geq a_N>G$，从而对任何一个 $\{a_{n_k}\}$ 子列都有 $k>N$ 时，$a_{n_k}>G$，因此发散。

(c) 可能。考虑一种分别构造的方式，使得数列里面 $1,1/2,1/3,\ldots$ 都出现无穷多次。

直接按顺序排会让它们无法出现第二次，因此尝试交替排列，例如 $\{1,1/2,1,1/2,1/3,1,1/2,1/3,1/4,\ldots\}$，符合要求。

可能。构造两个子列交替排列，一个收敛，一个发散。

不可能，因为由 Bolzano-Weierstrass 定理，这个有界子列里存在一个更小的收敛子列。

<br/>

$2.5.4.$<a id="2.5.4."></a>

由 Bolzano-Weierstrass 定理，有界数列一定有收敛子列，但是这并不意味着所有所有子列都是收敛的，所以想通过数列每项都属于某个收敛子列来证明数列收敛是行不通的。

那我们来考察一下，假如 $\{a_n\}$ 有界，且要么子列不收敛，要么子列都收敛到同一个极限 $a$ 呢?

比如说 $(-1)^n$，如果它是 $\{a_n\}$ 的子列，那么它确实不收敛。但是它也有自己的两个子列，并且这两个子列收敛到的极限不相同，那么就矛盾了。

所以，如果子列都收敛到同一个极限 $a$，那么 $\{a_n\}$ 就不能有不收敛的子列。事实上，因为 $\{a_n\}$ 有界，那么子列也有界，符合 Bolzano-Weierstrass 定理的要求，所以可以利用这个定理在发散子列里面创造两个更小的收敛子列，从而导致矛盾。这就是我们的证明逻辑。

我们用反证法。假设 $\{a_n\}$ 发散，因为 $\{a_n\}$ 有界，故由 Bolzano-Weierstrass 定理知，$\{a_n\}$ 有收敛子列，设该子列为 $\{a_{n_k}\}$，且 $\displaystyle\lim_{k\to\infty}a_{n_k}=a$。

下面我们创造第二个收敛子列，并且让它的极限不等于 $a$。因为 $\{a_n\}$ 发散，所以肯定有无穷多项不在 $\{a_n\}$ 的邻域里面，不然 $\{a_n\}$ 就收敛了。又因为这无穷多项是有界的，所以它肯定有一个不收敛到 $a$ 的子列，这样就得出了矛盾。用数学语言来说就是：

 $\exists\ \varepsilon>0$，使得对 $\forall\ N>0$，$\exists\ n>N$，使得 $|a_n-a|\geq \varepsilon$。也就是 $a_n\notin (a-\varepsilon,a+\varepsilon)$。

取 $n_1>N$ 满足上述条件，由 $N$ 的任意性，可以取到 $n_2>n_1$ 满足上述条件。以此类推，对 $\forall\ k\in \mathbb{N^+}$，都可以取到 $n_{k+1}>n_{k}$ 满足上述条件。所以我们得到了 $\{a_n\}$ 的一个子列 $\{a_{n_k}\}$。由于 $\{a_n\}$ 有界，所以 $\{a_{n_k}\}$ 也有界，由 Bolzano-Weierstrass 定理知，$\{a_{n_k}\}$ 有收敛子列，设该子列为 $\{a_{n_{k_j}}\}$，且 $\displaystyle\lim_{j\to\infty}a_{n_{k_j}}=b$。由于 $\forall\ k\in \mathbb{N^+}$，都有 $a_{n_k}\notin (a-\varepsilon,a+\varepsilon)$，所以由序极限定理 $b\notin (a-\varepsilon,a+\varepsilon)$，从而 $b\neq a$，这就得到了矛盾。

综上所述，$\{a_n\}$ 必须收敛。由收敛数列子列的极限和原数列极限相同可知 $\displaystyle\lim_{n\to\infty}a_n=a$。

<br/>


!!! question "练习 2.5.5"
    将例 2.5.3 中证明的结果推广到 \(\left| b\right|  < 1\) 的情况。证明当 \(- 1 < b < 1\) 时， \(\lim \left( {b}^{n}\right)  = 0\) 成立。

可以看出，$-1<b<0$ 时，$\{b^n\}$ 正负交错并不单调。但是我们可以把它的正负项分别提取成两个子列，并且这两个子列都收敛到 $0$。再利用 [$2.3.5.$](#2.3.5.) 的结论，我们就可以进行证明。

正数项子列的收敛性书上已证，现在证明负数项子列的收敛性。令 $c_n=b^{2n-1}$，则 $\{c_n\}$ 为 全体负数项组成的子列。因为 $-1<b<0$，所以 $b<b^3<b^5<\cdots<0$，由单调有界定理 $\{c_n\}$ 收敛。记 $\displaystyle\lim_{n\to\infty}c_n=c$，则 $\{c_n\}$ 的子列 $\{c_{2n}\}$ 也应当收敛到 $c$，而 $c_{2n}=b^{4n-1}=b(c_n)^2$，所以 $c=bc^2$，从而 $c=0$ 或 $\displaystyle\frac{1}{b}$，但是 $\displaystyle\frac{1}{b}<-1<c_n$，所以 $c=0$。

所以这两个子列的极限都为 $0$。由于这两个子列交替构成了 $\{b^n\}$，由 [$2.3.5.$](#2.3.5.) 的结论可知，$\{b^n\}$ 也收敛到 $0$。


<br/>


!!! question "练习 2.5.6"
    设 \(\left( {a}_{n}\right)\) 是一个有界序列，并定义集合
    
    $$
    S = \left\{  {x \in  \mathbb{R} : x < {a}_{n}\text{ for infinitely many terms }{a}_{n}}\right\}  .
    $$
    
    证明存在一个子列 \(\left( {a}_{{n}_{k}}\right)\) 收敛于 \(s = \sup S\) 。(这是利用完备性公理对Bolzano-Weierstrass定理的直接证明。)

只需要证明 $s$ 的任意邻域都存在 $\{a_n\}$ 中的项，便能构造出收敛到 $s$ 的子列。

假设存在 $\varepsilon>0$，使得 $\forall\ n\in \mathbb{N^+}$，$a_n\notin (s-\varepsilon,s+\varepsilon)$。那么 $\{a_n\}$ 中就有无限多项大于 $s+\varepsilon$，或小于 $s-\varepsilon$。

若有无限多项大于 $s+\varepsilon$，则 $x=s+\displaystyle\frac{\varepsilon}{2}\in S$，与 $s=\sup S$ 矛盾。

若只有无限多项小于 $s-\varepsilon$，则不存在 $x>s-\varepsilon$，使得 $x\in S$，与 $s=\sup S$ 矛盾。

所以 $\forall\ \varepsilon>0$，$\exists\ n\in \mathbb{N^+}$，使得 $a_n\in (s-\varepsilon,s+\varepsilon)$。由此便能构造出收敛到 $s$ 的子列。

首先，$\exists\ n_1\in \mathbb{N^+}$，使得 $a_{n_1}\in (s-1,s+1)$；

然后，$\exists\ n_2\in \mathbb{N^+}$，$n_2>n_1$，使得 $a_{n_2}\in (s-\displaystyle\frac{1}{2},s+\displaystyle\frac{1}{2})$；

依此类推，对 $\forall\ k\in \mathbb{N^+}$，$\exists\ n_k\in \mathbb{N^+}$，$n_k>n_{k-1}$，使得 $a_{n_k}\in (s-\displaystyle\frac{1}{k},s+\displaystyle\frac{1}{k})$。

这样便构造出了 $\{a_{n_k}\}$。

对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，$N>\displaystyle\frac{1}{\varepsilon}$，对 $\forall\ k>N$，有 $|a_{n_k}-s|<\displaystyle\frac{1}{k}<\varepsilon$。

所以 $\displaystyle\lim_{k\to\infty}a_{n_k}=s$。

---

## 习题 2.6 Cauchy 准则

!!! question "练习 2.6.1"
    给出以下每种情况的例子，或者论证这样的请求是不可能的。
    
    (a) 一个不是单调的Cauchy列(Cauchy sequence)。
    
    (b) 一个不是Cauchy的单调序列。
    
    (c) 一个具有发散子列的Cauchy列。
    
    (d) 一个包含Cauchy子列的无界序列。

(a) $a_n=(-1)^n\displaystyle\frac{1}{n}$。

(b) $a_n=n$。

(c) 不存在，因为柯西列一定收敛，所有子列都必须收敛。

(d) 让 $\{1\}$ 和 $\{n\}$ 交替组成  $\{a_n\}$ 即可。

<br/>


!!! question "练习 2.6.2"
    为定理2.6.2提供证明。

定理 $2.6.2$ 的证明利用了原数列的极限作为中间量，关键如下：在 $n$ 足够大时，每个 $a_n$ 都靠近极限 $a$ $\Rightarrow$ $a_n$ 之间都相互靠近。接下来定量证明即可 $\forall\ \varepsilon>0$，$\exists\ N>0$，$\forall\ m,n>N$，$|a_m-a|<\varepsilon$，$|a_n-a|<\varepsilon$，也就是说，$a_m,a_n$ 最多都只离 $a$ 有 $\varepsilon$ 的距离，因此它们两之间最多也只有 $2\varepsilon$ 的距离，用三角不等式得出 $   |a_m-a_n|\leq|a_m-a|+|a_n-a|<2\varepsilon$。这就证明了收敛数列都是柯西列。

<br/>


!!! question "练习 2.6.3"
    (a) 解释以下伪Cauchy性质与Cauchy列的正确定义有何不同:一个序列 \(\left( {s}_{n}\right)\) 是伪Cauchy的，如果对于所有 \(\varepsilon  > 0\) ，存在一个 \(N\) ，使得如果 \(n \geq  N\) ，则 \(\left| {{s}_{n + 1} - {s}_{n}}\right|  < \varepsilon\) 。
    
    (b) 如果可能，给出一个发散序列 \(\left( {s}_{n}\right)\) 的例子，该序列是伪Cauchy的。

(a) 伪柯西列的定义仅要求相邻项的距离足够小，而柯西列的定义要求任意两项的距离都足够小。

(b) 一个发散序列是有可能是伪柯西列的，对它的一个直观想法是：它是单调递增的，在增长量越来越小（趋于 $0$）的情况下无限增大。由于 $\{n\}$ 是一个典型的增长量不变的数列，所以我们可以考虑那些增长小于 $\{n\}$ 的数列，比如 $\{\sqrt{n}\}$。因为 $\displaystyle\lim_{n\to\infty}(\sqrt{n+1}-\sqrt{n})=\lim_{n\to\infty}\frac{1}{\sqrt{n+1}+\sqrt{n}}=0$，所以 $\{\sqrt{n}\}$ 是一个伪柯西列。

<br/>


!!! question "练习 2.6.4"
    假设 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) 是Cauchy列。使用三角不等式论证证明 \({c}_{n} = \left| {{a}_{n} - {b}_{n}}\right|\) 是Cauchy的。

$|c_m-c_n|=\big||a_m-b_m|-||a_n-b_n|\big|\leq |(a_m-a_n)-(b_m-b_n)|\leq |a_m-a_n|+|b_m-b_n|$，依此即可证明。

<br/>


!!! question "练习 2.6.5"
    如果 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 是Cauchy列，那么证明 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是Cauchy列的一个简单方法是使用Cauchy准则。根据定理 2.6.4， \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 必须是收敛的，而代数极限定理则意味着 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是收敛的，因此是Cauchy列。
    
    (a) 给出一个直接论证，证明 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是Cauchy列，而不使用Cauchy准则或代数极限定理。
    
    (b) 对乘积 \(\left( {{x}_{n}{y}_{n}}\right)\) 做同样的论证。

(a) 与 $2.6.4.$ 类似，令 $z_n=x_n+y_n$，则有 $|z_m-z_n|=|(x_m+y_m)-(x_n+y_n)|\leq |x_m-x_n|+|y_m-y_n|$，依此即可证明。

(b) 令 $w_n=x_ny_n$，则有 $|w_m-w_n|=|x_my_m-x_ny_n|=|x_my_m-x_ny_m+x_ny_m-x_ny_n|=|(x_m-x_n)y_m+(y_m-y_n)x_n|\leq |y_m||x_m-x_n|+|x_n||y_m-y_n|$。

对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，对 $\forall\ m,n\geq N_1$，$|x_m-x_n|<\varepsilon$；对 $\forall\ m,n\geq N_2$，$|y_m-y_n|<\varepsilon$。取 $N\in \mathbb{N^+}$，$N>\max\{N_1,N_2\}$，则对 $\forall\ m,n\geq N$，上述两式均成立。

又因为柯西列是有界的，所以 $\exists\ M_1,M_2>0$，对 $\forall\ n\in \mathbb{N^+}$，$|x_n|\leq M_1$，$|y_n|\leq M_2$。因此对 $\forall\ m,n\geq N$，有 $|w_m-w_n|<M_2\varepsilon+M_1\varepsilon=(M_1+M_2)\varepsilon$。这就证明了 $\{w_n\}$ 是柯西列。

<br/>

$2.6.6.$<a id="5">实数几大基本定理的互证</a>

(a) 闭区间套定理 $\Rightarrow$ 完备性公理

闭区间套定理其实揭示了实数的连续性，也就是说，实数轴上不存在空隙。使用无限的闭区间嵌套，在闭区间长度减小（趋于 $0$）的情况下，一定会正好落在某个实数上，这就像拿越来越细的刀去切实数轴，当它的厚度趋于 $0$ 时，一定会切到某个实数上。

从刀的比喻拓展来看，闭区间套定理最终能够把实数轴切成两个部分，而完备性公理正好就描述了这一性质：通过上确界的存在唯一性，将实数轴上所有点都划分成要么属于集合，要么属于上界的两部分（当然这里不严谨，我们只考虑切右边即上确界，下确界在这里忽略了）。

所以它们两个说明的是同一个性质，下面考虑用数学语言严谨地证明。

考虑有上界的非空集合 $A$。如果 $a\in A$ 为它的上界，那么 $a=\sup A$。具体来讲，任何一个元素都小于等于 $a$，而且 $a-\varepsilon<a$，满足上确界两条性质。实际上这个在第一章证明过了。

如果任何一个元素都不是 $A$ 的上界，那么这时我们就要用闭区间套定理把 $\sup A$ “切”出来了。我们可以仿照书上 Bolzano-Weierstrass 定理的证明思路，这样构造：

(i) 闭区间的左端点属于 $A$，右端点是 $A$ 的上界。

(ii) 下一个闭区间的长度是上一个的 $\displaystyle\frac{1}{2}$，以达到长度趋于 $0$ 的效果。

如此一来，闭区间“切出来”的实数应该就是“属于”和“上界”的分界点，即 $\sup A$。

理论存在，操作开始：

设 $A$ 的一个上界是 $M$，且有 $a\in A$。因为任何元素都不是 $A$ 的上界，所以 $a<M$。令 $a_1=a$，$b_1=M$，构造第一个闭区间 $[a_1,b_1]$。

现在，考虑 $[a_1,b_1]$ 的中点 $c_1=\displaystyle\frac{a_1+b_1}{2}$。按照这个形式操作:

(i) 若 $c_1$ 不是 $A$ 的上界，则令 $a_2=c_1$，$b_2=b_1$，构造下一个闭区间 $[a_2,b_2]$。

(ii) 若 $c_1$ 是 $A$ 的上界，则令 $a_2=a_1$，$b_2=c_1$，构造下一个闭区间 $[a_2,b_2]$。

$c_1$ 能且仅能满足其一，由此可得到下一个闭区间 $[a_2,b_2]$。

接下来，考虑 $[a_2,b_2]$ 的中点 $c_2=\displaystyle\frac{a_2+b_2}{2}$。按照完全相同的形式操作...

也就是说，对 $\forall\ n\in \mathbb{N^+}$，我们对 $[a_n,b_n]$ 的中点 $c_n=\displaystyle\frac{a_n+b_n}{2}$ 进行相同的操作；

(i) 若 $c_n$ 不是 $A$ 的上界，则令 $a_{n+1}=c_n$，$b_{n+1}=b_n$，构造下一个闭区间 $[a_{n+1},b_{n+1}]$。

(ii) 若 $c_n$ 是 $A$ 的上界，则令 $a_{n+1}=a_n$，$b_{n+1}=c_n$，构造下一个闭区间 $[a_{n+1},b_{n+1}]$。

得到下一个闭区间 $[a_{n+1},b_{n+1}]$。

如此一来，我们便得到一个闭区间套。由闭区间套定理，一定存在一个实数 $c$，使得 $c\in\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]$。

下面我们证明 $c=\sup A$。

$c$ 的特殊之处在哪呢？它的左边 $a_n$ 不是 $A$ 的上界，而右边 $b_n$ 都是 $A$ 的上界，而且 $a_n,b_n$ 之间会随 $n$ 增大任意接近，这说明 $a_n,c,b_n$ 三者也能在后面任意接近。把这个“任意接近”和上确界定义里面的“任意接近”联系起来，就能得到证明。

(i) 先证明 $c$ 是 $A$ 的上界，也就是说任何一个大于 $c$ 的数字都是 $A$ 的上界，这一点利用右边。如果 $c$ 不是一个上界，则 $\exists\ x\in A$，$c<x$。因为 $c,b_n$ 之间的距离能任意小，所以它们肯定能小于 $c,x$ 之间的距离，也就是说 $x$ 会大于某个 $b_n$，这样就矛盾了。数学语言说法如下：

取 $\varepsilon=x-c$，因为 $b_n-c\leq b_n-a_n=\displaystyle\frac{b_1-a_1}{2^{n-1}}$，而令 $n>\log_2(\displaystyle\frac{b_1-a_1}{\varepsilon})+1$ 时，$b_n-c<\varepsilon$，即 $x>b_n>x$，矛盾。（一个元素不能大于上界，不然就大于自身）

所以 $c$ 是 $A$ 的上界。

(ii) 再证明 $c$ 是 $A$ 的最小上界，也就是说任何一个小于 $c$ 的数字都不是 $A$ 的上界，这一点利用左边。如果 $c$ 不是最小上界，则 $\exists\ y<c$，使得 $y$ 是 $A$ 的上界。同上分析，取 $\varepsilon=c-y$，因为 $c-a_n\leq b_n-a_n=\displaystyle\frac{b_1-a_1}{2^{n-1}}$，而令 $n>\log_2\left(\displaystyle\frac{b_1-a_1}{\varepsilon}\right)+1$ 时，$c-a_n<\varepsilon$，即 $a_n<y<a_n$，矛盾。（其实跟上面一样）

综上所述 ，$c=\sup A$。

这就证明了完备性公理。

(b) 单调有界定理 $\Rightarrow$ 闭区间套定理

单调有界定理说明，一列一直增加的数列，如果有上界，那么它一定会收敛到某个实数。如果不收敛到某个上界，肯定也会收敛到更小的一个上界。这就像打到了一堵墙上，数列会越来越靠近墙，但不会穿过墙。

“墙”与“切”的关系其实很紧密，事实上，闭区间套定理用刀切出来的实数正好就可以看作分开左右端点的一堵墙。所以左/右端点的极限就是切出来的实数。

下面用数学语言证明。

设 $\{[a_n,b_n]\}$ 是闭区间套，则对 $\forall\ n\in \mathbb{N^+}$，$a_n\leq a_{n+1}\leq b_1$，这说明 $\{a_n\}$ 单调递增有上界，由单调有界定理，$\{a_n\}$ 有极限，设 $\displaystyle\lim_{n\to\infty}a_n=a$。

下面证明 $a\in [a_n,b_n]$ 对 $\forall\ n\in \mathbb{N^+}$ 成立。由于右边端点全是上界，即对 $\forall\ m,n\in \mathbb{N^+}$，$a_m\leq b_n$，由序极限定理 $a\leq b_n$。

对于左边，我们固定一个 $n$，因为 $\{a_n\}$ 单调递增，所以对 $\forall\ m\geq n$，$a_n\leq a_m$，由序极限定理 $a_n\leq a$。

所以对 $\forall\ n\in \mathbb{N^+}$，$a\in [a_n,b_n]$。即 $\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]=\{a\}\neq \varnothing$。

这就证明了闭区间套定理。

(c) Bolzano-Weierstrass 定理 $\Rightarrow$ 闭区间套定理

Bolzano-Weierstrass 定理可以在任何一个有界序列里面找到一个极限，而闭区间套的左右端点都是有界的，所以我们可以用前者来生成一个极限，由 (b) 问的证明可知，这个极限就是闭区间套切出来的实数。

总之，由 (b) 问的概述，$\{a_n\}$ 是有界的，所以由 Bolzano-Weierstrass 定理，$\{a_n\}$ 有一个收敛子列 $\{a_{n_k}\}$，设 $\displaystyle\lim_{k\to\infty}a_{n_k}=a$。

其实对这个子列的分析与 (b) 问的分析是一样的，同样由序极限定理得出 $a\leq b_n$。

左边同样固定 $n$，并使 $m>n$，则 $n_m\geq m>n$，所以 $a_n\leq a_{n_m}$，由序极限定理 $a_n\leq a$。

所以对 $\forall\ n\in \mathbb{N^+}$，$a\in [a_n,b_n]$。即 $\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]=\{a\}\neq \varnothing$。

这就证明了闭区间套定理。

(d) Cauchy 准则 $\Rightarrow$ Bolzano-Weierstrass 定理

Cauchy 准则在不知道极限，只需要知道数列的项彼此之间足够接近的情况下，就能判断数列收敛。所以我们需要用它来构造一个收敛子列。而 Bolzano-Weierstrass 定理的条件是有界。有界和足够接近...要怎么结合到一起呢？我们可以仿照书上的证明思路，因为它有界，所以我们可以不断的选取更小区间范围里的项，从而使它们彼此足够接近。

设 $\{a_n\}$ 有界，$\exists\ M>0$，对 $\forall\ n\in \mathbb{N^+}$，$a_n\in [-M,M]$。

选取第一个 $a_{n_1}\in [-M,M]$，记 $b_1=-M,c_1=M$，则 $a_{n_1}\in [b_1,c_1]$。

选取第二个 $a_{n_2}$，$n_2>n_1$：

若 $[b_1,\displaystyle\frac{b_1+c_1}{2}]$ 有 $\{a_n\}$ 的无限项，则 $a_{n_2}\in [b_1,\displaystyle\frac{b_1+c_1}{2}]$，否则 $a_{n_2}\in [\displaystyle\frac{b_1+c_1}{2},c_1]$，记 $a_{n_2}$ 属于的新闭区间为 $[b_2,c_2]$。

选取第三个 $a_{n_3}$，$n_3>n_2$：

若 $[b_2,\displaystyle\frac{b_2+c_2}{2}]$ 有 $\{a_n\}$ 的无限项，则 $a_{n_3}\in [b_2,\displaystyle\frac{b_2+c_2}{2}]$，否则 $a_{n_3}\in [\displaystyle\frac{b_2+c_2}{2},c_2]$，记 $a_{n_3}$ 属于的新闭区间为 $[b_3,c_3]$。

$\cdots$

依此类推，对 $\forall\ k\in \mathbb{N^+}$，都可以选取出一个闭区间，$a_{n_k}\in [b_k,c_k]$。

这样就构造出了一个子列 $\{a_{n_k}\}$。

依据选取方式，$c_k-b_k=\displaystyle\frac{M}{2^{k-2}}$，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，$N>\log_2\left(\displaystyle\frac{M}{\varepsilon}\right)+2$，对 $\forall\ p,q>N$，都有 $b_N\leq a_{n_p}\leq c_N$，$b_N\leq a_{n_q}\leq c_N$，所以 $|a_{n_p}-a_{n_q}|\leq c_N-b_N=\displaystyle\frac{M}{2^{N-2}}<\varepsilon$，$\{a_{n_k}\}$ 收敛。

这就证明了 Bolzano-Weierstrass 定理。

---

## 习题 2.7 无穷级数的性质

!!! question "练习 2.7.1"
    证明交错级数判别法(定理2.7.7)相当于证明部分和序列
    
    $$
    {s}_{n} = {a}_{1} - {a}_{2} + {a}_{3} - \cdots  \pm  {a}_{n}
    $$
    
    收敛。(第2.1节中的开篇例子包括 \(\left( {s}_{n}\right)\) 的典型说明。)完备性的不同特征导致不同的证明。
    
    (a) 通过证明 \(\left( {s}_{n}\right)\) 是Cauchy列来证明交错级数判别法。
    
    (b) 使用嵌套区间性质(定理1.4.1)为该结果提供另一种证明。
    
    (c) 考虑子列 \(\left( {s}_{2n}\right)\) 和 \(\left( {s}_{{2n} + 1}\right)\) ，并展示单调收敛定理如何为交错级数检验提供第三种证明。

因为 $s_n=\displaystyle\sum_{k=1}^{n}(-1)^{k+1}a_k$，所以证明 $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}a_n$ 收敛相当于证明 $\{s_n\}$ 收敛。

我们以 $a_k=\displaystyle\frac{1}{k}$ 为例，生成 $s_n$ 的一份点列图：

![](https://img-cdn.lusyoe.cn/images/HuangTianye/2025/10/12/kvjr23rpdi.png)

可以看到，奇数项和偶数项各自单调，且摆动区间越来越小，这将为我们接下来的证明提供参考。

(a) 由于 $\displaystyle\lim_{n\to\infty}a_n=0$，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|a_n|<\varepsilon$。

所以对 $\forall\ n>m>N$，$|s_m-s_n|=\left|\displaystyle\sum_{k=m+1}^n a_k\right| \leq \sum_{k=m+1}^n |a_k| < (n-m)\varepsilon$。

这样子不足以控制它的大小。

再考虑没有用上的 $\{a_n\}$ 单调递减，则有 $a_{k}-a_{k+1}\geq 0$，这个不等式正反用可得 $0\leq a_k-(a_{k+1}-a_{k+2})\leq a_{k}$。事实上，$a_k$ 后面所有摆动项加起来的威力，都无法让它脱离这个区间。因此，我们最终的目的是证明 $0\leq \displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}$。

若 $a_n$ 前为正号，则 $\displaystyle\sum_{k=m+1}^{n}a_k=a_{m+1}-(a_{m+2}-a_{m+3})-(a_{m+4}-a_{m+5})-\cdots-(a_{n-1}-a_{n})\leq a_{m+1}$，

$\displaystyle\sum_{k=m+1}^{n}a_k=(a_{m+1}-a_{m+2})+(a_{m+3}-a_{m+4})+\cdots+(a_{n-2}+a_{n-1})+a_n\geq 0$，

所以 $0\leq \displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}$。

若 $a_n$ 前为负号，用同样的方法两次组合分别证明。

所以 $|s_m-s_n|=\displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}<\varepsilon$，由 Cauchy 准则可知 $\{s_n\}$ 收敛。

(b) 考虑到 $\{s_n\}$ 是在越来越小的区间里面摆动的，所以利用闭区间套定理可以追踪到它的极限，再进行证明。

若 $s_k\leq s_{k+1}$ 即 $a_{k+1}$ 前面为正号，则 $s_{k+2}=s_{k+1}-a_{k+2}\leq s_{k+1}$，$s_{k+2}=s_k+(a_{k+1}-a_{k+2})\geq s_k$，得到 $s_k\leq s_{k+2}\leq s_{k+1}$。

若 $s_k\geq s_{k+1}$ 即 $a_{k+1}$ 前面为负号，用同样的方法可得 $s_k \leq s_{k+2}\leq s_{k+1}$。

这说明 $\{s_n\}$ 在越来越小的区间内摆动，下面构造闭区间套。

设 $I_k=[s_k,s_{k+1}]$，则由上述分析可知 $I_{k+1}\subset I_k$。

所以 $\{I_k\}$ 是一个闭区间套，由闭区间套定理，$\exists\ s\in \displaystyle\bigcap_{k=1}^{\infty}I_k$。

下面证明 $\displaystyle\lim_{n\to\infty}s_n=s$。

因为 $\displaystyle\lim_{n\to\infty}|s_{n+1}-s_{n}|=\displaystyle\lim_{n\to\infty}|a_{n+1}|=0$，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|s_{n+1}-s_n|<\varepsilon$。

又因为 $s\in I_n$，所以 $|s_n-s|\leq |s_{n+1}-s_n|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}s_n=s$。

所以 $\{s_n\}$ 收敛。

(c) 我们这里让 $n$ 从 $1$ 开始计数，这样 $\{s_{2n-1}\}$ 作为子列比 $\{s_{2n+1}\}$ 更为合适。

$s_{2n+1}=s_{2n-1}-(a_{2n}-a_{2n+1})\leq s_{2n-1}$，所以 $\{s_{2n-1}\}$ 单调递减。

$s_{2n+2}=s_{2n}+a_{2n+1}-a_{2n+2}\geq s_{2n}$，所以 $\{s_{2n}\}$ 单调递增。

又因为 $s_{2n-1}-s_{2n}=a_{2n}\geq 0$，所以 $s_1\geq s_{2n-1}\geq s_{2n}\geq s_2$，这说明 $\{s_{2n-1}\}$ 和 $\{s_{2n}\}$ 都是有界的。

由单调有界定理可知 $\{s_{2n-1}\}$ 和 $\{s_{2n}\}$ 都收敛。

设 $\displaystyle\lim_{n\to\infty}s_{2n-1}=s$，则对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，$|s_{2n-1}-s|<\displaystyle\frac{\varepsilon}{2}$。

又 $\displaystyle\lim_{n\to\infty}a_{2n}=\displaystyle\lim_{n\to\infty}|s_{2n-1}-s_{2n}|=0$，所以对 $\forall\ \varepsilon>0$，$\exists\ N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_2$，$|s_{2n-1}-s_{2n}|<\displaystyle\frac{\varepsilon}{2}$。

取 $N=\max\{N_1,N_2\}$，则对 $\forall\ n>N$，$|s_{2n}-s|=|s_{2n}-s_{2n-1}+s_{2n-1}-s|\leq |s_{2n}-s_{2n-1}|+|s_{2n-1}-s|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}s_{2n}=s$。

由 [$2.3.5.$](#2.3.5.)，$\displaystyle\lim_{n\to\infty}s_n=s$。

<br/>


!!! question "练习 2.7.2"
    (a) 使用级数的Cauchy准则为比较检验(定理2.7.4)的证明提供详细步骤。
    
    (b) 使用单调收敛定理为比较判别法提供另一种证明。

令 $s_n=\displaystyle\sum_{k=1}^{n}a_k$，$t_n=\displaystyle\sum_{k=1}^{n}b_k$，那么判断它们的敛散性就相当于判断原级数的敛散性了。

由于对 $\forall\ k\in \mathbb{N^+}$，$0\leq a_k\leq b_k$，所以 $s_n\leq t_n$，且它们都是单调递增的。

(a) (i) 若 $\{t_n\}$ 收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n>N$，$|t_m-t_n|<\varepsilon$，即 $\displaystyle\sum_{k=m+1}^{n}b_k<\varepsilon$。

所以 $|s_m-s_n|=\displaystyle\sum_{k=m+1}^{n}a_k\leq \displaystyle\sum_{k=m+1}^{n}b_k<\varepsilon$，由 Cauchy 准则可知 $\{s_n\}$ 收敛。

(ii) 若 $\{s_n\}$ 发散，则 $\exists\ \varepsilon>0$，对 $\forall\ N\in \mathbb{N^+}$，$\exists\ m,n>N$，使得 $|s_m-s_n|\geq \varepsilon$，即 $\displaystyle\sum_{k=m+1}^{n}a_k\geq \varepsilon$。

所以 $|t_m-t_n|=\displaystyle\sum_{k=m+1}^{n}b_k\geq \displaystyle\sum_{k=m+1}^{n}a_k\geq \varepsilon$，由 Cauchy 准则可知 $\{t_n\}$ 发散。

(b) (i) 若 $\{t_n\}$ 收敛，则 $\{t_n\}$ 有界，$\exists\ M>0$，使得对 $\forall\ n\in \mathbb{N^+}$，$|t_n|\leq M$。

又因为 $s_n\leq t_n\leq M$，所以 $\{s_n\}$ 也有界，又因为 $\{s_n\}$ 单调递增，所以由单调有界定理可知 $\{s_n\}$ 收敛。

(ii) 若 $\{s_n\}$ 发散，则对 $\forall\ M>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$s_n>M$。

所以 $t_n\geq s_n>M$，$\{t_n\}$ 发散。

<br/>


!!! question "练习 2.7.3"
    设 \(\sum {a}_{n}\) 给定。对于每个 \(n \in  \mathbb{N}\) ，如果 \({a}_{n}\) 为正，则赋值 \({p}_{n} = 0\) ；如果 \({a}_{n}\) 为负，则赋值 \({q}_{n} = {a}_{n}\) 。类似地，如果 \({a}_{n}\) 为负，则赋值 \({q}_{n} = 0\) ；如果 \({a}_{n}\) 为正，则赋值 [latex7]。
    
    (a) 论证如果 \(\sum {a}_{n}\) 发散，则 \(\sum {p}_{n}\) 或 \(\sum {q}_{n}\) 中至少有一个发散。
    
    (b) 证明如果 \(\sum {a}_{n}\) 条件收敛，则 \(\sum {p}_{n}\) 和 \(\sum {q}_{n}\) 都发散。

译本的题目有点问题，这里我按照自己的想法修正一下：

对于每个 $n\in \mathbb{N^+}$，

$$
    p_n=\begin{cases}
        0,\quad &a_n\geq 0\\
        a_n,\quad &a_n<0
    \end{cases}
$$

$$
    q_n=\begin{cases}
        a_n,\quad &a_n\geq 0\\
        0,\quad &a_n<0
    \end{cases}
$$

由此定义，$\sum a_n=\sum p_n+\sum q_n$。

(a) 若 $\{\sum a_n\}$ 发散，由 $\sum a_n=\sum p_n+\sum q_n$ 可知 $\sum p_k,\sum q_k$ 必有其一发散。

(b) 若 $\sum a_n$ 条件收敛，则 $\sum |a_n|$ 发散。

由 $\sum a_n=\sum p_n+\sum q_n$ 收敛，$\sum p_n,\sum q_n$ 要么都收敛，要么都发散；

由 $\sum |a_n|=-\sum p_n+\sum q_n$ 发散，$\sum p_n,\sum q_n$ 必有其一发散。

综合两条，即得 $\sum p_n$ 和 $\sum q_n$ 均发散。

<br/>


!!! question "练习 2.7.4"
    给出一个例子，说明 \(\sum {x}_{n}\) 和 \(\sum {y}_{n}\) 都发散，但 \(\sum {x}_{n}{y}_{n}\) 收敛的情况是可能的。

考虑构造交错级数，用它乘上另一个级数就可能让它项与项之间相互抵消，进而收敛。

$x_n=1$，$y_n=(-1)^n$ 可以吗？$\sum x_ny_n$ 永远在 $0,1$ 上摆动，不收敛。

所以另一个级数还得单调递减，让抵消后的值越来越小。

比如说，$x_n=\displaystyle\frac{1}{n}$，$y_n=(-1)^n$，那么 $x_ny_n=(-1)^n\displaystyle\frac{1}{n}$ 就是一个交错级数，由判别法可知它收敛。

<br/>


!!! question "练习 2.7.5"
    (a) 证明如果 \(\sum {a}_{n}\) 绝对收敛，则 \(\sum {a}_{n}^{2}\) 也绝对收敛。这个命题在没有绝对收敛的情况下是否成立？(b) 如果 \(\sum {a}_{n}\) 收敛且 \({a}_{n} \geq  0\) ，我们能否得出关于 \(\sum \sqrt{{a}_{n}}\) 的任何结论？

(a) 若 $\sum a_n$ 绝对收敛，要证 $\sum a_n^2$ 收敛，一个可能的想法是 $a_n^2\leq |a_n|$ 即 $|a_n|<1$，而这在绝对收敛的条件下是做得到的（事实上 $a_n$ 可以任意小）。

由 Cauchy 准则，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n\geq N$，$\displaystyle\sum_{k=m+1}^{n}|a_k|<\varepsilon$。我们取 $\varepsilon<1$，$m=n-1$，就有 $\forall\ n>N$， $|a_n|<\varepsilon<1$，所以 $a_n^2\leq |a_n|$。

所以 $\displaystyle\sum_{k=n+1}^{n}a_k^2\leq \displaystyle\sum_{k=m+1}^{n}|a_k|<\varepsilon$，由 Cauchy 准则可知 $\sum a_n^2$ 收敛。由非负性可得 $\sum a_n^2$ 绝对收敛。

(b) 不能。由 (a) 的分析，$0\leq a_n<1$ 时 $a_n\leq \sqrt{a_n}$，所以 $\sqrt{a_n}$ 的值增大了，那它的和就不一定收敛。

比如令 $a_n=\displaystyle\frac{1}{n^2}$，则 $\sum a_n$ 收敛，但 $\sum \sqrt{a_n}=\sum \displaystyle\frac{1}{n}$ 发散。

<br/>


!!! question "练习 2.7.6"
    (a) 证明如果 \(\sum {x}_{n}\) 绝对收敛，且序列 \(\left( {y}_{n}\right)\) 有界，则和 \(\sum {x}_{n}{y}_{n}\) 收敛。
    
    (b) 找出一个反例，证明如果 \(\sum {x}_{n}\) 的条件收敛，则(a)部分并不总是成立。

(a) 用绝对值不等式将 $|\sum x_ny_n|$ 拆开，再用 $\{y_n\}$ 有界进行估计，最后用绝对收敛的条件得出结论。

由 $\{y_n\}$ 有界，$\exists\ M>0$，使得对 $\forall\ n\in \mathbb{N^+}$，$|y_n|\leq M$。

又因为 $\sum x_n$ 绝对收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n>N$，$\displaystyle\sum_{k=m+1}^{n}|x_k|<\displaystyle\frac{\varepsilon}{M}$。

所以对 $\forall\ m,n>N$，$|\displaystyle\sum_{k=m+1}^{n}x_ky_k|\leq \displaystyle\sum_{k=m+1}^{n}|x_k||y_k|\leq M\displaystyle\sum_{k=m+1}^{n}|x_k|<M\displaystyle\frac{\varepsilon}{M}=\varepsilon$，由 Cauchy 准则可知 $\sum x_ny_n$ 收敛。

(b) 考虑 $\sum x_n,\sum y_n$ 都是交错级数的情况，那么它们相乘后可能抵消符号，变成正项级数，从而发散。

比如说，$x_n=(-1)^{n+1}\displaystyle\frac{1}{n}$，$y_n=(-1)^{n+1}$，则满足题意，但 $x_ny_n=\displaystyle\frac{1}{n}$，$\sum x_ny_n$ 发散。

<br/>

$2.7.7.$<a id="6">几何级数与 $\mathrm{p}$ 级数间的转换</a>

题目让我们用几何级数的敛散性证明 $\mathrm{p}$ 级数的敛散性。也就是

$$
    \sum ar^n \Rightarrow \sum \frac{1}{n^p}
$$

这两个级数的变化量一个在指数上，一个在底数上，所以需要想一个转换的方法。

有什么办法能将变化量这样转换，而不改变原级数的敛散性呢？我没有想到，问了 deepseek 后，它为我提供了 Cauchy 判敛法，在 $2.4$ 节提过：

$$
    a_n\ \text{单调递减且非负}\Rightarrow \sum a_n\ \text{收敛}\Leftrightarrow \sum 2^na_{2^n}\ \text{收敛}
$$

由此可见，$\sum \displaystyle\frac{1}{n^p}$ 是否收敛等价于 $\sum 2^n\displaystyle\frac{1}{(2^n)^p}=\sum (2^{(1-p)})^n$ 是否收敛，这就把变量转移到指数上来了。

由几何级数的敛散性可知，当且仅当 $|2^{1-p}|<1$ 即 $p>1$ 时 $\sum (2^{(1-p)})^n$ 收敛。

所以 $\sum \displaystyle\frac{1}{n^p}$ 当且仅当 $p>1$ 时收敛。

<br/>


!!! question "练习 2.7.8"
    证明定理2.7.1的第(ii)部分。

我们要论证部分和序列

$$
    \begin{align*}
        s_n&=(a_1+b_1)+(a_2+b_2)+\cdots (a_n+b_n)\\
        &=(a_1+a_2+\cdots +a_n)+(b_1+b_2+\cdots +b_n)\\
    \end{align*}
$$

收敛，则令 $p_n=a_1+a_2+\cdots +a_n$，$q_n=b_1+b_2+\cdots +b_n$，则 $s_n=p_n+q_n$。

由 $p_n,q_n$ 收敛可知 $s_n$ 收敛。

<br/>


!!! question "练习 2.7.9"
    (比值判别法). 给定一个级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) ，其中 \({a}_{n} \neq  0\) ，比值判别法指出，如果 \(\left( {a}_{n}\right)\) 满足
    
    $$
    \lim \left| \frac{{a}_{n + 1}}{{a}_{n}}\right|  = r < 1
    $$
    
    则该级数绝对收敛。
    
    (a) 设 \({r}^{\prime }\) 满足 \(r < {r}^{\prime } < 1\) 。(为什么这样的 \({r}^{\prime }\) 必须存在？)解释为什么存在一个 \(N\) ，使得 \(n \geq  N\) 蕴含 \(\left| {a}_{n + 1}\right|  \leq  \left| {a}_{n}\right| {r}^{\prime }\) 。
    
    (b) 为什么 \(\left| {a}_{N}\right| \sum {\left( {r}^{\prime }\right) }^{n}\) 必然收敛？
    
    (c) 现在，证明 \(\sum \left| {a}_{n}\right|\) 收敛。

(a) 由实数稠密性可知 $r'$ 必须存在。

由 $\displaystyle\lim_{n\to\infty}|\displaystyle\frac{a_{n+1}}{a_n}|=r<r'$，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n\geq N$，$|\displaystyle\frac{a_{n+1}}{a_n}-r|\leq \varepsilon$。

取 $\varepsilon=r'-r$，则对 $\forall\ n>N$，$|\displaystyle\frac{a_{n+1}}{a_n}|\leq r+\varepsilon=r'$。所以 对 $\forall\ n\geq N$，$|a_{n+1}|\leq |a_n|r'$。

(b) 因为 $|\displaystyle\frac{a_{n+1}}{a_n}|\geq 0$，由序极限定理可知 $\displaystyle\lim_{n\to\infty}|\displaystyle\frac{a_{n+1}}{a_n}|=r\geq 0$。所以 $0<r'<1$，由几何级数的敛散性可知 $|a_N|\sum (r')^n$ 收敛。

(c) 结合前两问我们可以把 $\{a_n\}$ 放缩成一个收敛的几何级数，从而证明 $\sum a_n$ 收敛。

对 $\forall\ n\in \mathbb{N}$，由上面递推式得出 $|a_{n+N}|\leq |a_N|(r')^{n}$。所以 $\displaystyle\sum_{n=N}^{\infty}|a_n|\leq \displaystyle\sum_{n=0}^{\infty}|a_N|(r')^{n}=|a_N|\sum_{n=0}^{\infty}(r')^{n}=\frac{|a_N|}{1-r'}$。由此可知 $\displaystyle \sum_{n=N}^{\infty}|a_n|$ 收敛。

由于收敛级数的前有限项和不影响其敛散性（Cauchy 收敛准则），所以 $\sum |a_n|$ 收敛。

<br/>


!!! question "练习 2.7.10"
    (a) 证明如果 \({a}_{n} > 0\) 和 \(\lim \left( {n{a}_{n}}\right)  = l\) 且 \(l \neq  0\) ，则级数 \(\sum {a}_{n}\) 发散。
    
    (b) 假设 \({a}_{n} > 0\) 和 \(\lim \left( {{n}^{2}{a}_{n}}\right)\) 存在。证明 \(\sum {a}_{n}\) 收敛。

(a) 通过 $\displaystyle\lim_{n\to\infty}(na_n)=l$ 估计 $a_n$ 的下界即可。这里我们用 $2.7.9.$ 的类似操作。

首先，由 $a_n>0$，$l>0$（题目中给出了 $l\neq 0$），所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n\geq N$，$|na_n-l|<\varepsilon$。

取 $\varepsilon=\displaystyle\frac{l}{2}$，则对 $\forall\ n\geq N$，$|na_n-l|<\displaystyle\frac{l}{2}$，即 $-\displaystyle\frac{l}{2}<na_n-l<\displaystyle\frac{l}{2}$，所以 $na_n>\displaystyle\frac{l}{2}$，即 $a_n>\displaystyle\frac{l}{2n}$。

所以 $\displaystyle\sum_{n=N}^{\infty} a_n>\displaystyle\frac{l}{2}\sum_{n=N}^{\infty} \displaystyle\frac{1}{n}$，由 $\mathrm{p}$ 级数的敛散性和比较判别法可知 $\sum a_n$ 发散。

(b) 同样的方法，这次估计上界。

记 $\displaystyle\lim_{n\to\infty}(n^2a_n)=l$，由 (a) 问同样的操作最终可得出 $\exists\ N\in \mathbb{N^+}$，对 $\forall\ n\geq N$，$a_n<\displaystyle\frac{3l}{2n^2}$

还是对 $n\geq N$ 的项进行求和放缩，同样的操作即可知 $\sum a_n$ 收敛。

<br/>


!!! question "练习 2.7.11"
    找出两个级数 \(\sum {a}_{n}\) 和 \(\sum {b}_{n}\) 的例子，它们都发散，但 \(\sum \min \left\{  {{a}_{n},{b}_{n}}\right\}\) 收敛。为了使问题更具挑战性，请给出 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) 为正且递减的例子。

一般的例子可以这么构造：$0,n$ 奇偶交替，另外一个级数 $n,0$ 奇偶交替，这样它们的最小值永远是 $0$ 即可收敛。

全都为正项递减的例子太难了，问了 deepseek 也构造不出来。

问了 Gemini 2.5 pro 后，它给了我一个思路：

$a_n,b_n$ 都要一段递减，一段常数，交替进行，使得 $\min(a_n,b_n)$ 永远在递减。

首先我们选取递减部分，它肯定要收敛，所以我们选取 $\displaystyle\frac{1}{n^2}$，并先让 $a_n=\displaystyle\frac{1}{n^2}$ 一段距离。

$a_1=1$，$a_2=\displaystyle\frac{1}{4}$ 时，让 $b_1=b_2=1$，接下来让 $a_3$ 到 $a_6$ 都等于 $\displaystyle\frac{1}{4}$，而 $b_3$ 到 $b_6$ 按接下来的 $\displaystyle\frac{1}{n^2}$ 序列递减，一直递减到 $\displaystyle\frac{1}{36}$，

然后让 $a_7$ 到 $a_{42}$ 的值都等于 $\displaystyle\frac{1}{36}$，而 $b_7$ 到 $b_{42}$ 按接下来的 $\displaystyle\frac{1}{n^2}$ 序列递减，一直递减到 $\displaystyle\frac{1}{42^2}$。

接下来就让从 $a_{43}$ 开始的 $42^2$ 项按 $\displaystyle\frac{1}{n^2}$ 通项递减，而从 $b_{43}$ 开始的 $42^2$ 项值都等于 $\displaystyle\frac{1}{42^2}$。

所以，我们的操作流程如下：每次常数段的前一项记作 $a_k$，那么下一段常数段每一项的值就为 $a_k$，而长度为 $\displaystyle\frac{1}{a_k}$，这样这一段所有常数的和就为 $1$。常数段结束之后，紧接着按 $\displaystyle\frac{1}{n^2}$ 的通项递减，而常数段的最后一项 $a_s$ 的下标作为另一个数列常数段的前一项下标，即 $b_s$ 为 $\{b_n\}$ 常数段的前一项。而 $a_2$ 作为 $\{a_n\}$ 的第一个常数段的前一项，$b_1$ 到 $b_2$ 作为 $\{b_n\}$ 的第一个常数段。再规定 $b_1=b_2=a_1=1$。

这样子就能保证 $\{a_n\}$ 和 $\{b_n\}$ 永远在递减，而且都有无穷多个常数段，这样级数和里面就有无穷多个 $1$ 的和，这就保证了级数发散。

而交替递减的形式保证了 $\{\min(a_n,b_n)\}=\{\displaystyle\frac{1}{n^2}\}$，所以 $\sum \min(a_n,b_n)$ 收敛。

下为 $\{a_n\},\{b_n\}$ 的示意图，使用对数坐标轴让交替单调递减的性质更清晰可见：

![](https://img-cdn.lusyoe.cn/images/HuangTianye/2025/10/13/pgkfkj1l92.png)

<br/>


!!! question "练习 2.7.12"
    (分部求和法)。设 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 为序列，且令 \({s}_{n} = {x}_{1} + {x}_{2} + \cdots  + {x}_{n}\) 。利用 \({x}_{j} = {s}_{j} - {s}_{j - 1}\) 的观察来验证公式
    
    $$
    \mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j} = {s}_{n}{y}_{n + 1} - {s}_{m}{y}_{m + 1} + \mathop{\sum }\limits_{{j = m + 1}}^{n}{s}_{j}\left( {{y}_{j} - {y}_{j + 1}}\right) .
    $$

我们主要分析这个式子：

$$
    \displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})
$$

由题目给出的提示，我们考虑产生 $\{s_j\}$ 的相邻项再作差。因为上面这个求和每一项里都有 $\{y_j\}$ 相邻项的差，所以求和的项与项之间是有公因式 $y_j$ 的，将不同的 $s_j$ 都提取成它的系数即可构造：

$$
    \begin{align*}
    &s_j(y_j-y_{j+1})+s_{j+1}(y_{j+1}-y_{j+2})+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+(s_{j+1}-s_j)y_{j+1}-s_{j+1}y_{j+2}+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}-s_{j+1}y_{j+2}+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+(s_{j+2}-s_{j+1})y_{j+2}-s_{j+2}y_{j+3}+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+x_{j+2}y_{j+2}-s_{j+2}y_{j+3}+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+x_{j+2}y_{j+2}+\cdots+x_ny_n-s_ny_{n+1}\\
    \end{align*}
$$

所以

$$
    \begin{align*}
        &s_ny_{n+1}-s_my_{m+1}+\displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})\\
        =\ &s_ny_{n+1}-s_my_{m+1}+s_{m+1}y_{m+1}-s_ny_{n+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &(s_{m+1}-s_m)y_{m+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &x_{m+1}y_{m+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &\displaystyle\sum_{j=m+1}^{n}x_jy_j\\
    \end{align*}
$$

<br/>


!!! question "练习 2.7.13"
    (Dirichlet判别法)。Dirichlet判别法用于判断级数收敛性，它指出如果 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 的部分和有界(但不一定收敛)，且如果 \(\left( {y}_{n}\right)\) 是一个满足 \({y}_{1} \geq  {y}_{2} \geq  {y}_{3} \geq  \cdots  \geq  0\) 且 \(\lim {y}_{n} = 0\) 的序列，那么级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}{y}_{n}\) 收敛。
    
    (a) 设 \(M > 0\) 为 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 的部分和的上界。利用习题 2.7.12 证明
    
    $$
    \left| {\mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j}}\right|  \leq  {2M}\left| {y}_{m + 1}\right| .
    $$
    
    (b) 证明上述Dirichlet判别法。
    
    展示如何将交替级数判别法(定理2.7.7)作为Dirichlet判别法的特例推导出来。

记 $\displaystyle\sum_{j=1}^{n}x_j=s_n$。

(a) 由题意 $s_n\leq M$ 总是成立。

由 $\{y_n\}$ 正项递减，$y_j-y_{j+1}\geq 0$ 总是成立。

由 $2.7.12.$ 可得

$$
    \begin{align*}
        \displaystyle\sum_{j=m+1}^{n}x_jy_j
        &=s_ny_{n+1}-s_my_{m+1}+\displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})\\
        &\leq |s_n||y_{n+1}|+|s_m||y_{m+1}|+\displaystyle\sum_{j=m+1}^{n}|s_j||y_j-y_{j+1}|\\
        &\leq M|y_{n+1}|+M|y_{m+1}|+M\displaystyle\sum_{j=m+1}^{n}|y_j-y_{j+1}|\\
        &=M(y_{n+1}+y_{m+1}+\displaystyle\sum_{j=m+1}^{n}(y_j-y_{j+1}))\\
        &=2My_{m+1}=2M|y_{m+1}|\\
    \end{align*}
$$

(b) 由 $\displaystyle\lim_{n\to\infty}y_n=0$ 可知对 $\forall \ \varepsilon>0$，$\exists\ N\in\mathbb{N^+}$，当 $n>N$ 时，有 $|y_n|<\displaystyle\frac{\varepsilon}{2M}$。

即对 $\forall\ m,n>\mathbb{N^+}$，有 $\displaystyle\sum_{j=m+1}^{n}x_jy_j\leq 2M|y_{m+1}|<2M\cdot \frac{\varepsilon}{2M}=\varepsilon$。

所以 $\displaystyle\sum_{n=1}^{\infty}x_ny_n$ 收敛。

取 $x_n=(-1)^{n+1}$，$y_n$ 正项递减且趋于 $0$，则 $\sum x_n y_n$ 符合交错级数判别法的条件，由 Dirichlet 判别法知其收敛。

<br/>


!!! question "练习 2.7.14"
    (Abel判别法)。Abel判别法用于判断级数收敛性，其指出如果级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 收敛，且 \(\left( {y}_{n}\right)\) 是一个满足以下条件的序列:
    
    $$
    {y}_{1} \geq  {y}_{2} \geq  {y}_{3} \geq  \cdots  \geq  0
    $$
    
    那么级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}{y}_{n}\) 收敛。
    
    (a)仔细指出Abel判别法的假设与练习2.7.13中Dirichlet判别法的假设有何不同。
    
    (b) 假设 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) 的部分和有界于常数 \(A > 0\) ，并假设 \({b}_{1} \geq  {b}_{2} \geq  {b}_{3} \geq  \cdots  \geq  0\) 。使用练习 2.7.12 来证明
    
    $$
    \left| {\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{j}{b}_{j}}\right|  \leq  {2A}{b}_{1}
    $$
    
    (c) 通过以下策略证明Abel判别法(Abel’s Test)。对于固定的 \(m \in  N\) ，将部分 (b) 应用于 \(\mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j}\) ，通过设置 \({a}_{n} = {x}_{m + n}\) 和 \({b}_{n} = {y}_{m + n}\) 。(论证 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) 的部分和的上界可以通过取 \(m\) 为任意大而变得任意小。)

(a) Abel 判别法将收敛的条件从 $\{y_n\}$ 转移到了 $\{x_n\}$ 上，并且对收敛的要求变弱了，不需要指出收敛于某个具体值。

(b) 用 $2.7.13.$ 完全一样的证明方法。

(c) 由题意可知 $\sum x_n$ 收敛，所以由 Cauchy 收敛准则，对任意 $\varepsilon>0$，存在 $N\in \mathbb{N^+}$，对任意 $n>m>N$，$\left|\displaystyle\sum_{j=m+1}^{n}x_n\right|=\left|\displaystyle\sum_{j=1}^{n-m}a_n\right|<\displaystyle\frac{\varepsilon}{2b_1}$。

所以有 $\left|\displaystyle\sum_{j=m+1}^{n}x_ny_n\right|=\left|\displaystyle\sum_{j=1}^{n-m}a_nb_n\right|\leq 2b_1\cdot \displaystyle\frac{\varepsilon}{2b_1}=\varepsilon$，由 Cauchy 收敛准则可知 $\sum x_ny_n$ 收敛。

<br/>

附录：<a id="7">绝对收敛重排定理的证明</a>

定理复述：若 $\displaystyle\sum_{n=1}^{\infty}a_n$ 绝对收敛，则它的任意重排都收敛到相同的极限。

注：证明有点画蛇添足，想看收敛同极限的证明直接跳到“接下来证明极限是同一个”这一段。

证明：这里用一种跟书上不同的证明。

我的考虑是这样的：如果原数列的项是有正有负的，那么重排可以把正项和负项打乱，假设前面全排正项（或负项）部分和就会变得很大（小），难以估计重排后的部分和的范围，于是难以用 $\varepsilon-\delta$ 语言说明（这也许就是条件收敛级数重排不一定收敛的原因）。但是我们可以利用绝对收敛的性质进行估计，因为它的项全都是非负的，重排之后部分和的性质仍然好掌握，再由绝对收敛得出原重排级数收敛即可。

设 $\displaystyle\sum_{n=1}^{\infty}b_n$ 为 $\displaystyle\sum_{n=1}^{\infty}a_n$ 的一个重排。由绝对收敛的性质，$\displaystyle\sum_{n=1}^{\infty}|a_n|$ 收敛，因为它的部分和单调递增，所以它一定有界，不妨设 $\displaystyle\sum_{n=1}^{\infty}|a_n|<M$。因为 $\{b_n\}$ 中的项均为 $\{a_n\}$ 中的项，所以 $\displaystyle\sum_{n=1}^{\infty}|b_n|<M$，由其单调的性质得到 $\displaystyle\sum_{n=1}^{\infty}|b_n|$ 收敛。也就是说 $\displaystyle\sum_{n=1}^{\infty}b_n$ 绝对收敛，所以它本身也必定收敛。

接下来证明极限为同一个，利用 Cauchy 收敛准则和绝对收敛的性质打出组合拳。

我想利用的性质是，通过两级数之差为 $0$ 证明它们收敛到同一个极限。因为 $\{a_n\}$ 中的项在 $\{b_n\}$ 中均出现，所以肯定 $\exists\ N,T\in \mathbb{N^+}$，$\{a_1,\ldots,a_N\}\subseteq \{b_1,\ldots,b_T\}$。这样 $|a_T-b_T|$ 留下来的项其下标均大于 $N$，再利用绝对收敛性质得以证明。

对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>m>N$，都有 $\displaystyle\sum_{k=m}^{n}|a_k|<\varepsilon$。同时又 $\exists\ T>N$，使得 ，$\{a_1,\ldots,a_N\}\subseteq \{b_1,\ldots,b_T\}$。所以对 $\forall\ n>T$，

$$
    \begin{align*}
        |\displaystyle\sum_{k=1}^{n}a_k-\displaystyle\sum_{k=1}^{n}b_k|&\leq|a_{r_1}|+|a_{r_2}|+\cdots+|a_{r_m}| \qquad r_1<r_2<\cdots<r_m，r_i>N\\
        &\leq \displaystyle\sum_{k=r_1}^{r_m}|a_k|<\varepsilon
    \end{align*}
$$

所以 $\displaystyle\sum_{n=1}^{\infty}a_n-\displaystyle\sum_{n=1}^{\infty}b_n=0$。又因为它们均收敛，所以它们的极限相同。

---

## 习题 2.8 双重求和与无穷级数的乘积

$2.8$ 节的习题旨在探索级数乘积的求和条件，我会在对应习题的后面简要说明它对应的探索步骤。

!!! question "练习 2.8.1"
    使用第2.1节中的特定数组 \(\left( {a}_{ij}\right)\) ，计算 \(\mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn}\) 。这个值与已经计算的两个迭代和值相比如何？
    
    如何定义双重求和的问题与第2.7节末尾讨论的重排主题之间存在深刻的相似性。两者都涉及到无限设置中加法的交换性。对于重排，解决方案是增加了绝对收敛的假设，同样的方法适用于双重求和也就不足为奇了。在绝对收敛的假设下，讨论的每种计算双重和值的方法都会得到相同的结果。

$s_{nn}=-1\left(1+\displaystyle\frac{1}{2}+\displaystyle\frac{1}{4}+\cdots+\displaystyle\frac{1}{2^{n-1}}\right)=-2+\displaystyle\frac{1}{2^{n-1}}$

所以 $\displaystyle\lim_{n\to\infty}s_n=-2=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_{ij}$。

<br/>

!!! question "练习 2.8.2"
    （双重级数绝对收敛 $\Rightarrow$ 本身收敛）
    
    证明如果迭代级数
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {a}_{ij}\right|
    $$
    
    收敛(意味着对于每个固定的 $i \in  \mathbb{N}$ ，级数 $\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {a}_{ij}\right|$ 收敛到某个实数 ${b}_{i}$ ，并且级数 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{b}_{i}$ 也收敛)，则迭代级数
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{ij}
    $$
    
    收敛。


下为二维数列 $\{a_{ij}\}$ 的无限方形数表，其中把每一行的和记为 $c_{i}$：

| $a_{11}$ | $a_{12}$ | $a_{13}$ | $a_{14}$ | $a_{15}$ | $\cdots$ | $c_{1}$  |

| -------- | -------- | -------- | -------- | -------- | -------- | -------- |

| $a_{21}$ | $a_{22}$ | $a_{23}$ | $a_{24}$ | $a_{25}$ | $\cdots$ | $c_{2}$  |

| $a_{31}$ | $a_{32}$ | $a_{33}$ | $a_{34}$ | $a_{35}$ | $\cdots$ | $c_{3}$  |

| $a_{41}$ | $a_{42}$ | $a_{43}$ | $a_{44}$ | $a_{45}$ | $\cdots$ | $c_{4}$  |

| $a_{51}$ | $a_{52}$ | $a_{53}$ | $a_{54}$ | $a_{55}$ | $\cdots$ | $c_{5}$  |

| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

首先，由定义可得 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}=\displaystyle\sum_{i=1}^{\infty}c_i$，所以我们要证明：

1. $c_i$ 的存在性，即 $\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 对任意 $i\in \mathbb{N^+}$ 收敛。

2. $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

因为 $\displaystyle\sum_{j=1}^{\infty}|a_{ij}|$ 收敛到 $b_i$，由绝对收敛的性质可知 $\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 也收敛，所以 $c_i$ 存在。

又因为 $\displaystyle\sum_{i=1}^{\infty}b_i$ 收敛，且 $|c_i|=\left|\displaystyle\sum_{j=1}^{\infty}a_{ij}\right| \leq \displaystyle\sum_{j=1}^{\infty}|a_{ij}|=b_i$，所以 $0\leq \displaystyle\sum_{i=1}^{\infty}|c_i|\leq \displaystyle\sum_{i=1}^{\infty}b_i$，$\displaystyle\sum_{i=1}^{\infty}|c_i|$ 收敛，所以 $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

综上所述，$\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 收敛。

<br/>

!!! question "练习 2.8.3"
    （考察 $n\times n$  区域求和的收敛性）
    
    (a) 证明集合 $\left\{  {{t}_{mn} : m,n \in  \mathbb{N}}\right\}$ 有上界，并利用这一事实得出结论:序列 $\left( {t}_{nn}\right)$ 收敛。
    
    (b) 现在，利用 $\left( {t}_{nn}\right)$ 是Cauchy列这一事实，论证 $\left( {s}_{nn}\right)$ 也是Cauchy列，因此收敛。


(a) 使用 $2.8.2.$ 中一样的条件，则 $\displaystyle\sum_{i=1}^{\infty}b_i$ 是有界的，即存在 $M>0$，使得对任意的 $m\in \mathbb{N^+}$，都有 $\displaystyle\sum_{i=1}^{m}b_i \leq M$。

所以 $t_{mn}=\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_{ij}| \leq \displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{\infty}|a_{ij}| \leq \displaystyle\sum_{i=1}^{m}b_i \leq M$。

这就得到 $\{t_{mn}\}$ 有界。

又因为对 $\forall\ n\in \mathbb{N^+}$，$t_{n+1,n+1}=\displaystyle\sum_{i=1}^{n+1}\displaystyle\sum_{j=1}^{n+1}|a_{ij}|=\displaystyle\sum_{i=1}^{n}\displaystyle\sum_{j=1}^{n}|a_{ij}|+\displaystyle\sum_{j=1}^{n+1}|a_{n+1,j}|+\displaystyle\sum_{i=1}^{n}|a_{i,n+1}|\geq t_{nn}$，所以 $\{t_{nn}\}$ 单调递增。由单调有界定理可知 $\{t_{nn}\}$ 收敛。

(b) 对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\  n>m>N$，有 $|t_{mm}-t_{nn}|<\varepsilon$。

由绝对值不等式，$|s_{mm}-s_{nn}|=\left|\displaystyle\sum_{i=m+1}^{n}\displaystyle\sum_{j=1}^{n}a_{ij}+\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=m+1}^{n}a_{ij}\right|\leq \displaystyle\sum_{i=m+1}^{n}\displaystyle\sum_{j=1}^{n}|a_{ij}|+\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=m+1}^{n}|a_{ij}|=|t_{mm}-t_{nn}|<\varepsilon$。

所以 $\{s_{nn}\}$ 也是 Cauchy 列，故收敛。

<br/>

!!! question "练习 2.8.4"
    （说明 $m\times n$ 区域求和的有界性）
    
    (a) 论证存在一个 ${N}_{1} \in  \mathbb{N}$ ，使得 $m,n \geq  {N}_{1}$ 蕴含 $B - \frac{\varepsilon }{2} < {t}_{mn} \leq  B$ 。
    
    (b) 现在，证明存在一个 $N$ ，使得
    
    $$
    \left| {{s}_{mn} - S}\right|  < \varepsilon
    $$
    
    对于所有 $m,n \geq  N$ 。


(a) 取 $N_1>\max\{m_0,n_0\}$，由 $|a_{ij}|$ 的非负性可得 $\forall\ m,n>N_1$，$B-\displaystyle\frac{\varepsilon}{2}<t_{m_0n_0}\leq t_{mn}\leq B$。

(b) 一个想法是 $|s_{mn}-S|\leq |s_{mn}-s_{nn}|+|s_{nn}-S|$，并估计 $|s_{mn}-s_{nn}|$ 的大小。

绝对值不等式可得 $|s_{mn}-s_{nn}|\leq |t_{mn}-t_{nn}|$，再利用 (a) 中的结论限制 $t_{mn}$ 的范围完成证明。

首先，对 $\forall\ \varepsilon>0$，$\exists\ N_2\in \mathbb{N^+}$，对 $\forall\ n>N_2$，都有 $|s_{nn}-S|<\displaystyle\frac{\varepsilon}{2}$。

由 (a)，对 $\forall\ m,n>N_1$，$B-\displaystyle\frac{\varepsilon}{2}<t_{mn}\leq B$，$B-\displaystyle\frac{\varepsilon}{2}<t_{nn}\leq B$，所以 $|t_{mn}-t_{nn}|<\displaystyle\frac{\varepsilon}{2}$。

取 $N=\max\{N_1,N_2\}$，则对 $\forall\ m,n>N$，都有

$$
    \begin{align*}
        |s_{mn}-S| &\leq |s_{mn}-s_{nn}|+|s_{nn}-S| \\
                   &\leq |t_{mn}-t_{nn}|+|s_{nn}-S| \\
                   &< \displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon
    \end{align*}
$$

<br/>

!!! question "练习 2.8.5"
    （利用上题估计出的界限，横纵求两次极限得出结论）
    
    (a) 使用代数极限定理(定理 2.3.3)和序极限定理(定理 2.3.4)来证明对于所有 $m \geq  N$
    
    $$
    \left| {\left( {{r}_{1} + {r}_{2} + \cdots  + {r}_{m}}\right)  - S}\right|  \leq  \varepsilon .
    $$
    
    得出结论，迭代和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{ij}$ 收敛于 $S$ 。


因为 $|s_{mn}-S|<\varepsilon$，所以由序极限定理，对 $\forall\ m>N$，

$\displaystyle\lim_{n\to\infty}|s_{mn}-S|\leq \varepsilon$，即 $-\varepsilon\leq \displaystyle\lim_{n\to\infty}(s_{mn}-S)\leq \varepsilon$。

而

$$
    \begin{align*}
        \displaystyle\lim_{n\to\infty}(s_{mn}-S)&=\displaystyle\lim_{n\to\infty}s_{mn}-S\\
        &=\displaystyle\lim_{n\to\infty}(\displaystyle\sum_{j=1}^{n}a_{1j}+\displaystyle\sum_{j=1}^{n}a_{2j}+\cdots+\displaystyle\sum_{j=1}^{n}a_{mj})-S\\
        &=(\displaystyle\sum_{j=1}^{\infty}a_{1j}+\displaystyle\sum_{j=1}^{\infty}a_{2j}+\cdots+\displaystyle\sum_{j=1}^{\infty}a_{mj})-S\\
        &=(r_1+r_2+\cdots+r_m)-S
    \end{align*}
$$

所以 $|(r_1+r_2+\cdots+r_m)-S|\leq \varepsilon$，由此可得 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}=\displaystyle\sum_{i=1}^{\infty}r_i=S$。

<br/>

!!! question "练习 2.8.6"
    （运用前面所有的结论，纵横求两次极限，得到横纵求和与纵横求和结果相同的结论）
    
    通过证明另一个迭代和 $\mathop{\sum }\limits_{{j = 1}}^{\infty }\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{ij}$ 也收敛于 $S$ 来完成证明。
    注意，一旦确定对于每个固定列 $j$ ，和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{ij}$ 收敛于某个实数 ${c}_{i}$ ，就可以使用相同的论证。


仿照上题，首先对 $\forall\ n>N$，$\displaystyle\lim_{m\to\infty}|s_{mn}-S|\leq \varepsilon$；

然后把 $s_{mn}$ 逐列拆解，$s_{mn}=\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{m}a_{ij}=(\displaystyle\sum_{i=1}^{m}a_{i1}+\displaystyle\sum_{i=1}^{m}a_{i2}+\cdots+\displaystyle\sum_{i=1}^{m}a_{in})$；

根据 $t_{mn}$ 的有界性，得到 $\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}|a_{ij}|$ 有界收敛，所以对 $\forall\ k\in \mathbb{N^+}$，$\displaystyle\sum_{i=1}^{\infty}|a_{ik}|$ 收敛 $\Rightarrow$ $\displaystyle\sum_{i=1}^{\infty}a_{ik}$ 收敛。

所以 $|\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{\infty}a_{ij}-S|\leq \varepsilon$，$\displaystyle\lim_{n\to\infty}\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{\infty}a_{ij}=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_{ij}=S$。

<br/>

!!! question "练习 2.8.7"
    （这一题为下面叙述级数之积求和做铺垫）
    
    (a) 假设定理 2.8.1 的假设——以及结论——成立，证明 $\mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k}$ 绝对收敛。
    
    (b) 模仿定理 2.8.1 证明中的策略，证明 $\mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k}$ 收敛于 $S = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn}$ 。


(a) 由绝对值不等式，$0\leq \displaystyle\sum_{k=2}^{n+1}|d_k|\leq t_{nn}$。

因为 $\{t_{nn}\}$ 收敛，所以 $\displaystyle\sum_{k=2}^{\infty}d_k$ 绝对收敛。

(b) 由 (a)，$\displaystyle\sum_{k=2}^{\infty}d_k$ 收敛。

我们要得出 $\displaystyle\lim_{n\to\infty}\displaystyle\sum_{k=2}^{n}d_k=S=\displaystyle\lim_{n\to\infty}s_{nn}$，仿照前面的做法，我们可以估计 $\left|\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right|$ 的范围。

绘制一个简单的图来说明这个范围包括的区域：

![](https://img-cdn.lusyoe.com/images/HuangTianye/2025/10/21/bj2bcdcuyp.png)

（这里假设 $n=4$）

- 红色：$s_{nn}-\displaystyle\sum_{k=2}^{n}d_k$ 剩余的元素求和；

- 红色+蓝色：$\displaystyle\sum_{k=2}^{2n}d_k-\displaystyle\sum_{k=2}^{n}d_k$ 剩余的元素求和；

因为 $\displaystyle\sum_{k=2}^{\infty}|d_k|$ 收敛，所以由 Cauchy 收敛准则，红色+蓝色区域的各元素绝对值的和可以被限制，于是可以进一步限制红色，进而得到证明。

由 $\displaystyle\sum_{k=2}^{\infty}|d_k|$ 收敛，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ m,n>N$，$\left|\displaystyle\sum_{k=2}^{m}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$。

取 $m=2n$ 有 $\left|\displaystyle\sum_{k=2}^{2n}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$。

又 $\left|\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right|\leq \left|\displaystyle\sum_{k=2}^{2n}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}\left(\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right)=0$。

所以 $\displaystyle\lim_{n\to\infty}\displaystyle\sum_{k=2}^{\infty}d_k=\displaystyle\lim_{n\to\infty}s_{nn}=S$。

<br/>

!!! question "练习 2.8.8"
    假设 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{i}$ 绝对收敛于 $A$ ，且 $\mathop{\sum }\limits_{{j = 1}}^{\infty }{b}_{j}$ 绝对收敛于 $B$ 。
    
    (a) 证明该集合
    
    $$
    \left\{  {\mathop{\sum }\limits_{{i = 1}}^{m}\mathop{\sum }\limits_{{j = 1}}^{n}\left| {{a}_{i}{b}_{j}}\right|  : m,n \in  \mathbb{N}}\right\}
    $$
    
    是有界的。利用这一点来证明迭代和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {{a}_{i}{b}_{j}}\right|$ 收敛，从而我们可以应用定理2.8.1。
    
    (b) 设 ${s}_{nn} = \mathop{\sum }\limits_{{i = 1}}^{n}\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i}{b}_{j}$ ，并利用代数极限定理证明 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn} = {AB}$ 。由此得出结论
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{i}{b}_{j} = \mathop{\sum }\limits_{{j = 1}}^{\infty }\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{i}{b}_{j} = \mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k} = {AB},
    $$
    
    其中，如前所述， ${d}_{k} = {a}_{1}{b}_{k - 1} + {a}_{2}{b}_{k - 2} + \cdots  + {a}_{k - 1}{b}_{1}$ 。


（这一题其实可以把 $a_ib_j$ 看作 $c_{ij}$，这样所有的结论可以通过双重求和的性质给出）

(a) 由题知 $\displaystyle\sum_{i=1}^{\infty}a_i=A$，$\displaystyle\sum_{j=1}^{\infty}b_j=B$。（绝对收敛于 $A$ 指的是它本身收敛于 $A$，且是绝对收敛的）

由绝对收敛级数的单调性，可得 $\exists\ M,N>0$, 对 $\forall\ m,n\in \mathbb{N^+}$，$\displaystyle\sum_{i=1}^{m}|a_i|\leq M$，$\displaystyle\sum_{j=1}^{n}|b_j|\leq N$。

再利用绝对值的性质，可得

$$
    \begin{align*}
        \displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_ib_j|&=\displaystyle\sum_{i=1}^{m}(|a_ib_1|+|a_ib_2|+\cdots+|a_ib_n|)\\
        &=\displaystyle\sum_{i=1}^{m}(|a_i|(|b_1|+|b_2|+\cdots+|b_n|))\\
        &=\displaystyle\sum_{i=1}^{m}|a_i|\displaystyle\sum_{j=1}^{n}|b_j|\\
        &\leq MN
    \end{align*}
$$

所以 $\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_ib_j|$ 是有界的。

由单调有界定理，对 $\forall\ i\in \mathbb{N^+}$，$|a_i|\displaystyle\sum_{j=1}^{n}|b_j|$ 收敛于 $c_i\geq 0$，所以 $\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{\infty}|a_ib_j|=\displaystyle\sum_{i=1}^{m}c_i$，又由单调有界定理知 $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

所以 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}|a_ib_j|$ 收敛。

(b) 根据 (a) 中一样的方法可以将双重求和拆开，所以

$\displaystyle\lim_{n\to\infty}s_{nn}=\displaystyle\lim_{n\to\infty}\left(\displaystyle\sum_{i=1}^{n}a_i\displaystyle\sum_{j=1}^{n}b_j\right)=\displaystyle\sum_{i=1}^{\infty}a_i\displaystyle\sum_{j=1}^{\infty}b_j=AB$。

再运用书上定理 $2.8.1.$ 即可得到结论

$$
    \displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_ib_j=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_ib_j=\displaystyle\sum_{k=2}^{\infty}d_k=AB
$$

---

# $\mathbb{R}$ 的基本拓扑结构

## 习题 3.2 开集与闭集

!!! question "练习 3.2.1"
    (a) 在定理3.2.3第(ii)部分的证明中，假设开集集合是有限的这一条件在何处被使用？
    
    (b) 给出一个无限嵌套开集集合的例子
    
    $$
    {O}_{1} \supseteq  {O}_{2} \supseteq  {O}_{3} \supseteq  {O}_{4} \supseteq  \cdots
    $$
    
    其交集 \(\mathop{\bigcap }\limits_{{n = 1}}^{\infty }{O}_{n}\) 是闭集且非空。

(a) 在 $\varepsilon=\min\{\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_N\}$ 这一步被用到，因为无限交集的情况下，不一定有最小的 $\varepsilon_k$。

(b) 构造一个最简单的：取 $O_k=(-\displaystyle\frac{1}{k},\displaystyle\frac{1}{k})$，则 $O_k$ 是开集，但 $\displaystyle\bigcap_{k=1}^\infty O_k=\{0\}$，它是一个闭集。

<br/>


!!! question "练习 3.2.2"
    设
    
    $$
    B = \left\{  {\frac{{\left( -1\right) }^{n}n}{n + 1} : n = 1,2,3,\ldots }\right\}  .
    $$
    
    (a) 找出 \(B\) 的极限点。
    
    (b) \(B\) 是一个闭集吗？
    
    (c) \(B\) 是一个开集吗？
    
    (d) \(B\) 是否包含任何孤立点？
    
    (e) 求 \(\bar{B}\) 。

(a) 震荡数列 $(-1)^n\displaystyle\frac{n}{n+1}$ 在 $-1,1$ 之间震荡，所以 $B$ 的极限点为 $1,-1$。

(b) 因为极限点不属于 $B$，所以 $B$ 不是闭集。

(c) 因为 $B$ 中任何一个点的邻域都不包含于 $B$，所以 $B$ 不是开集。

(d) $B$ 中所有的点都不是极限点，可以说明所有的点都是孤立点。

(e) $\overline B=\{-1,1\}\cup B$。

<br/>


!!! question "练习 3.2.3"
    判断以下集合是开集、闭集还是两者都不是。如果集合不是开集，找出集合中的一个点，使得该点没有包含在集合中的 \(\varepsilon\) -邻域。如果集合不是闭集，找出一个不在集合中的极限点。
    
    (a) \(\mathbb{Q}\) .
    
    (b) \(\mathbb{N}\) .
    
    (c) \(\{ x \in  \mathbb{R} : x > 0\}\) .
    
    (d) \((0,1\rbrack  = \{ x \in  \mathbb{R} : 0 < x \leq  1\}\) .
    
    (e) \(\left\{  {1 + 1/4 + 1/9 + \cdots  + 1/{n}^{2} : n \in  \mathbb{N}}\right\}\) .

(a) $\mathbb{Q}$ 不是开集也不是闭集。

对 $\forall\ p\in \mathbb{Q}$，$\forall\ \varepsilon>0$，$(p-\varepsilon,p+\varepsilon)$ 中总有无理数，所以 $\mathbb{Q}$ 不是开集。

又因为 $\mathbb{Q}$ 的任意一个极限点都是实数，而 $\mathbb{Q}$ 中没有所有的实数，所以 $\mathbb{Q}$ 不是闭集。

(b) $\mathbb{N}$ 不是开集但它是闭集。

不是开集的理由同上。

是闭集的理由为：它里面没有极限点，满足闭集定义；或者说，它的补集是开集。

(c) $(0,+\infty)$ 是开集但不是闭集。

对 $\forall\ p\in (0,+\infty)$，取 $\varepsilon=\displaystyle\frac{p}{2}$，则 $V_\varepsilon(p)\subseteq (0,+\infty)$，所以它是开集。

又因为 $0$ 是 $(0,+\infty)$ 的极限点，所以它不是闭集。

(d) $(0,1]$ 既不是开集也不是闭集。$1$ 不满足开集定义，$0$ 不满足闭集定义。

(e) $\{\displaystyle\sum_{i=1}^{n}\displaystyle\frac{1}{i^2}:n\in \mathbb{N^+}\}$ 既不是开集也不是闭集。单点不满足开集定义，这个序列的极限不满足闭集定义。

<br/>


!!! question "练习 3.2.4"
    通过证明如果 \(x =\)  \(\lim {a}_{n}\) 对于包含在 \(A\) 中的某个序列 \(\left( {a}_{n}\right)\) 满足 \({a}_{n} \neq  x\) ，则 \(x\) 是 \(A\) 的极限点，来证明定理 3.2.5 的逆命题。

由极限定义，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，当 $n>N$ 时，有 $a_n\in V_\varepsilon(x)$，所以 $x$ 是 $A$ 的极限点。

<br/>


!!! question "练习 3.2.5"
    设 \(a \in  A\) 。证明 \(a\) 是 \(A\) 的孤立点，当且仅当存在一个 \(\varepsilon\) 邻域 \({V}_{\varepsilon }\left( a\right)\) ，使得 \({V}_{\varepsilon }\left( x\right)  \cap  A = \{ a\}\) 。

$\Rightarrow)$ 若 $a$ 是 $A$ 的孤立点，则它不是 $A$ 的极限点，即 $\exists\ \varepsilon>0$，使得 $V_\varepsilon(a)\cap A=\{a\}$。

$\Leftarrow)$ 若 $\exists\ \varepsilon>0$，使得 $V_\varepsilon(a)\cap A=\{a\}$，则 $a$ 不是 $A$ 的极限点，所以它是 $A$ 的孤立点。

<br/>


!!! question "练习 3.2.6"
    证明定理 3.2.8。

$\Rightarrow)$ 若 $F$ 是闭集，则它包含它的所有极限点。对于里面任何一个 Cauchy 列，它的极限就是 $F$ 的极限点，所以要属于 $F$。

$\Leftarrow)$ 若 $F$ 包含它的所有 Cauchy 列的极限，而任何一个极限点都是某个 Cauchy 列的极限，所以它包含它的所有极限点，所以它是闭集。

<br/>


!!! question "练习 3.2.7"
    设 \(x \in  O\) ，其中 \(O\) 是一个开集。如果 \(\left( {x}_{n}\right)\) 是一个收敛到 \(x\) 的序列，证明 \(\left( {x}_{n}\right)\) 中除有限项外的所有项都包含在 \(O\) 中。

因为 $O$ 是开集，所以 $\exists\ \varepsilon>0$，使得 $V_\varepsilon(x)\subseteq O$。

而对这样的 $\varepsilon$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>N$，$x_n\in V_\varepsilon(x)$，所以 $x_n\in O$。

所以 $\{x_n\}$ 中至多除有限项（$N$ 项）外都在 $O$ 中。

<br/>


!!! question "练习 3.2.8"
    给定 \(A \subseteq  \mathbb{R}\) ，设 \(L\) 为 \(A\) 的所有极限点的集合。
    
    (a) 证明集合 \(L\) 是闭集。
    
    (b) 论证如果 \(x\) 是 \(A \cup  L\) 的极限点，则 \(x\) 也是 \(A\) 的极限点。利用这一观察为定理3.2.12提供证明。

(a) 若 $x\in L$ 是 $L$ 的一个极限点，则存在序列 $\{y_n\}\subseteq L$，使得 $\displaystyle\lim_{n\to\infty}y_n=x$。

又 $y_n\in L$ 对 $\forall\ n\in \mathbb{N^+}$ 成立，所以对任意的 $n$ 存在 $\{z_{n_k}\}\subseteq A$ 使得 $\displaystyle\lim_{k\to\infty}z_{n_k}=y_n$。

也就是说全体 $\{z_{n_k}\}$ 组成的序列以 $x$ 为极限点，所以 $x\in L$。

一个更严谨的写法是，因为 $y_n$ 总是 $A$ 中某个序列的极限，所以肯定存在 $z_n\in A$，使 $|y_n-z_n|<\displaystyle\frac{\varepsilon}{2}$，再通过极限表达式得出结论。

(b) 由 (a) 可知无论 $a$ 是 $A$ 的极限点还是 $L$ 的极限点，都必定属于 $L$，所以 $a$ 一定是 $A$ 的极限点。所以 $\overline A$ 是一个闭集。而任何一个包含 $A$ 的闭集都必须包含 $A$ 的所有极限点也就是 $L$，所以 $\overline A$ 是包含 $A$ 的最小闭集。

<br/>


!!! question "练习 3.2.9"
    (a) 如果 \(y\) 是 \(A \cup  B\) 的极限点，证明 \(y\) 要么是 \(A\) 的极限点，要么是 \(B\) 的极限点(或两者都是)。
    
    (b) 证明 \(\overline{A \cup  B} = \bar{A} \cup  \bar{B}\) 。
    
    (c) (b)中关于闭包的结果是否适用于集合的无限并集？

(a) 因为 $y$ 是 $A\cup B$ 的极限点，所以对 $\forall\ \varepsilon>0$，$\exists\ x\in A\cup B$ 使得 $x\in V_\varepsilon(y)$。

如果 $y$ 不是 $A$ 的极限点，则 $\exists\ \varepsilon_1>0$，使得对 $\forall\ x_1\in A$，$x_1\notin V_{\varepsilon_1}(y)$。但是又有 $A\cup B$ 中的元素属于这个邻域，所以上面定义中的 $x$ 在 $\varepsilon<\varepsilon_1$ 时必定属于 $B$，所以 $y$ 是 $B$ 的极限点。

所以 $y$ 必定是 $A$ 或 $B$ 的极限点。

(b) 因为 $\overline{A\cup B}$ 包含了所有 $A$ 或 $B$ 的极限点，所以 $\overline{A}\subseteq \overline{A\cup B}$，$\overline{B}\subseteq\overline{A\cup B}$，所以 $\overline{A}\cup \overline{B}\subseteq \overline{A\cup B}$。

又因为 $A\subseteq \overline{A}$，$B\subseteq \overline{B}$，所以 $A\cup B\subseteq \overline{A}\cup \overline{B}$。又因为 $\overline{A\cup B}$ 是包含 $A\cup B$ 的最小闭集，而 $\overline{A}\cup \overline{B}$ 是闭集，所以 $\overline{A\cup B}\subseteq \overline{A}\cup \overline{B}$。

综上所述，$\overline{A\cup B}=\overline{A}\cup \overline{B}$。

(c) 因为无限个闭集的并集不一定是闭集，所以不适用于无限的情况。 ^2

<br/>


!!! question "练习 3.2.10"
    (德摩根定律)。在练习1.2.3中概述了德摩根定律在两组情况下的证明。一般情况的论证类似。
    
    (a) 给定一组集合 \(\left\{  {{E}_{\lambda } : \lambda  \in  \Lambda }\right\}\) ，证明
    
    $$
    {\left( \mathop{\bigcup }\limits_{{\lambda  \in  \Lambda }}{E}_{\lambda }\right) }^{c} = \mathop{\bigcap }\limits_{{\lambda  \in  \Lambda }}{E}_{\lambda }^{c}\;\text{ and }\;{\left( \mathop{\bigcap }\limits_{{\lambda  \in  \Lambda }}{E}_{\lambda }\right) }^{c} = \mathop{\bigcup }\limits_{{\lambda  \in  \Lambda }}{E}_{\lambda }^{c}.
    $$
    
    (b) 现在，提供定理3.2.14的证明细节。

(a) 这一点在 [$1.2.12.$](#2) 已经给出。

(b) 1. 若 $E_1,E_2,\ldots,E_n$ 均为闭集，则 $\left(\displaystyle\bigcup_{i=1}^nE_i\right)^c=\displaystyle\bigcap_{i=1}^nE_i^c$，因为等式右边是有限个开集的交，所以 $\left(\displaystyle\bigcup_{i=1}^nE_i\right)^c$ 是个开集，即 $\displaystyle\bigcup_{i=1}^nE_i$ 是闭集。

2. 若 $\{E_\lambda:\lambda\in\Lambda\}$ 是任意个闭集的族，则 $\left(\displaystyle\bigcap_{\lambda\in\Lambda}E_\lambda\right)^c=\displaystyle\bigcup_{\lambda\in\Lambda}E_\lambda^c$，因为任意个开集的并是开集，所以 $\displaystyle\bigcap_{\lambda\in\Lambda}E_\lambda$ 是闭集。

<br/>


!!! question "练习 3.2.11"
    设 \(A\) 有上界，使得 \(s = \sup A\) 存在。证明 \(s \in  \bar{A}\) 。

由上确界的定义，对 $\forall\ \varepsilon>0$，$\exists\ x\in A$，使得 $s-\varepsilon<x\leq s\Rightarrow x\in V_\varepsilon(A)$。

如果 $x=s$，则 $s\in A$，即 $s\in \overline A$。

如果总有 $x\neq s$ 满足上式，则 $s$ 是 $A$ 的极限点，所以 $s\in \overline A$。

综上所述，$s\in \overline A$。

<br/>


!!! question "练习 3.2.12"
    判断以下陈述是真还是假。为假的陈述提供反例，为真的陈述提供证明。
    
    (a) 对于任何集合 \(A \subseteq  \mathbb{R},{\bar{A}}^{c}\) ，它是开集。
    
    (b) 如果一个集合 \(A\) 有一个孤立点，它不能是开集。
    
    (c) 一个集合 \(A\) 是闭集当且仅当 \(\bar{A} = A\) 。
    
    如果 \(A\) 是一个有界集，那么 \(s = \sup A\) 是 \(A\) 的一个极限点。
    
    每个有限集都是闭集。
    
    一个包含所有有理数的开集必定是整个 \(\mathbb{R}\) 。

(a) 正确的。因为 $\overline{A}$ 是闭集，所以 $\overline{A}^c$ 是开集。

(b) 正确的。因为开集的定义强调了任何元素的邻域都包含在该集合内，而孤立点的邻域不满足这点。

(c) 正确的。因为 $\overline{A}$ 包含 $A$ 及其所有极限点，而若 $A$ 本身为闭集，它也包含自身所有极限点，所以 $A=\overline{A}$（更数学一点的证明可以参考 $\overline{A}$ 是包含 $A$ 的最小闭集这一性质）。

(d) 错误的。若 $s\in A$，它完全可以作为孤立点而存在。

(e) 正确的。因为有限集合没有极限点，相当于它包含了全体极限点（空集）。

从补集角度上来讲，有限集的补集是任意开集的并，仍然是开集，故它本身是并集。

(f) 错误的。虽然每个实数都必定处在某个有理数的某个邻域内，但完全可以控制这些邻域的大小，使得它们的并不覆盖整个实数集。

，比如说 $R \setminus \sqrt{2}$。

<br/>


!!! question "练习 3.2.13"
    证明既是开集又是闭集的唯一集合是 \(\mathbb{R}\) 和空集 \(\varnothing\) 。

对于 $\mathbb{R}$，因为它中任意元素的邻域都包含于自身，而且任意极限点也属于自身，所以它既是开集又是闭集。

对于 $\varnothing$，因为它没有任何元素，所以任意元素的邻域（空集）包含于它，因此它是开集。同时，$\varnothing$ 也不包含任何极限点，所以全体极限点的集合（空集）包含于它，因此它是闭集。

（从补集上考虑，它的补集 $\mathbb{R}$ 既是开集又是闭集，所以它自身既是闭集又是开集。）

接下来说明除这两个集合之外，不可能有其他既是开集又是闭集的集合。

考虑一个不等于 $\mathbb{R}$ 的非空集合 $A$，也就是说存在 $x_0,y_0$，$x_0\in A$，$y_0\notin A$。

因为有开区间的端点是开区间的极限点但不属于开区间这一特殊例子，所以我们的证明同样从端点入手。若 $x_0<y_0$，则令 $B=\{x<y_0:x\in A\}$，否则令 $B=\{x>y_0:x\in A\}$，这样保证了 $B$ 非空。

又因为 $B$ 总有界，所以存在上确界或下确界 $b$，这样 $b$ 就是 $B$ 的一个极限点。又因为 $B\subseteq A$，所以它也是 $A$ 的极限点。

如果 $A$ 是既是开集又是闭集，则 $b\in A$，且存在 $\varepsilon$ 使得 $V_\varepsilon(b)\subseteq A$。由 $A$ 的定义知 $y_0\notin V_\varepsilon(b)$。

我们考虑 $B=\{x<y_0:x\in A\}$ 的情况，由确界定义和邻域范围可得 $V_\varepsilon(b)$ 所有元素都小于 $y_0$，由 $B$ 的定义可得 $V_\varepsilon(b)\subseteq B$，但这与 $b$ 的确界性质矛盾。

同理，$B$ 集合的另一种情况也能推出矛盾。所以 $A$ 不可能既是开集又是闭集。

(当然也可以从开集中没有孤立点入手，这样更加简单。)

<br/>

!!! question "练习 3.2.14"
    一个集合 $A$ 被称为 $F_{\sigma }$ 集，如果它可以写成闭集的可数并集。一个集合 $B$ 被称为 $G_{\delta }$ 集，如果它可以写成开集的可数交集。
    
    (a) 证明闭区间 $[a,b]$ 是一个 $G_{\delta }$ 集。
    
    (b) 证明半开区间 $(a,b]$ 既是 $G_{\delta }$ 集又是 $F_{\sigma }$ 集。
    
    (c) 证明 $\mathbb{Q}$ 是一个 $F_{\sigma }$ 集，且无理数集 $\mathbb{R}\setminus\mathbb{Q}$ 构成一个 $G_{\delta }$ 集。(我们将在3.5节中看到， $\mathbb{Q}$ 不是一个 $G_{\delta }$ 集， $\mathbb{R}\setminus\mathbb{Q}$ 也不是一个 $F_{\sigma }$ 集。)

(a) $[a,b]=\displaystyle\bigcap_{n=1}^\infty(a-\frac{1}{n},b+\frac{1}{n})$，右边是可数个开集的交。

(b) $(a,b]=\displaystyle\bigcap_{n=1}^\infty(a,b+\displaystyle\frac{1}{n})=\displaystyle\bigcup_{n=1}^\infty[a+\frac{1}{n},b]$，分别是可数开集的交和可数闭集的并。

(c) $\mathbb{Q}$ 可以直接写成全体有理数的并集，每个有理数自身构成闭集，而且有理数的个数可数。

所以 $\mathbb{Q}=\displaystyle\bigcup_{q\in\mathbb{Q}}\{q\}$，$\mathbb{R}\setminus\mathbb{Q}=\mathbb{Q}^c=\left(\displaystyle\bigcup_{q\in\mathbb{Q}}\{q\}\right)^c=\displaystyle\bigcap_{q\in\mathbb{Q}}(\{q\})^c=\displaystyle\bigcap_{q\in\mathbb{Q}}(\mathbb{R}\setminus \{q\})$，右边是可数个开集的交。

所以 $\mathbb{Q}$ 是 $G_\delta$ 集，$\mathbb{R}\setminus\mathbb{Q}$ 是 $F_\sigma$ 集。

### 附加题目

!!! info "附加题目 3.2.F1"
    把闭区间套定理里的闭区间换成闭集，结论是否成立？

不成立。因为闭区间套定理依赖于闭区间的有界性，而闭集不一定有界。

试想一下，因为 $a_n<b_1$，单调有界才保证了 $\displaystyle\lim_{n\to\infty}a_n$ 的存在，可是如果 $\{a_n\}$ 无界呢？

这样就可以构造出反例了：$\displaystyle\bigcap_{n=1}^\infty[n,+\infty)=\varnothing$。

<br/>

!!! info "附加题目 3.2.F2"
    一个集合有可能包含不可数个孤立点吗？

因为每个孤立点都存在一个只包含它本身的开区间，所以这等于在问：是否可以在实数轴上放置不可数多个互不相交的开区间？

答案是否定的。因为每个开区间内都包含有理数，于是在可以每个开区间里面选一个有理数出来与之对应。因为有理数集是可数集，所以这些开区间的个数也只能是可数的。

<br/>

!!! info "附加题目 3.2.F3"
    对任意集合 $A$，证明 $\left(\overline{A}\right)^c\cap \overline{A^c}$ 是开集但不一定是闭集。

以 $A=(a,b)$ 为例子，$\left(\overline{A}\right)^c$ 不包括 $a,b$，但 $\overline{A^c}$ 包括 $a,b$，所以可以猜测，$\left(\overline{A}\right)^c\subseteq \overline{A^c}$。这样就得到本题结论。

设 $A$ 的极限点集为 $L$，$A^c$ 的极限点集为 $M$，则 $\overline{A}=A\cup L$，$\overline{A^c}=A^c\cup M$。

所以 $\left(\overline{A}\right)^c=A^c\cap L^c$，也就是说 $\left(\overline{A}\right)^c\subseteq A^c\subseteq\overline{A^c}$，所以 $\left(\overline{A}\right)^c\cap \overline{A^c}=\left(\overline{A}\right)^c$，它是闭集的补集，所以是开集。

<br/>

!!! info "附加题目 3.2.F4"
    设 $A$ 是一个不可数集，集合 $B$ 将 $A$ 从中间拆开成两个不可数子集，即 $B$ 的元素 $s$ 满足 $A_{ls}=\{x:x\in A,x<s\}$ 和 $A_{rs}=\{x:x\in A,x>s\}$ 都是不可数集。证明 $B$ 非空且是开集。

这里想通过闭区间套定理类似的方法，通过不断缩减范围得到证明。

首先证明存在 $M>0$，使得 $C_M=\{x:x\in A,|x|<M\}$ 是不可数集。事实上，如果对任意的 $M$ 它都是可数集，那么 $A=\displaystyle\bigcup_{n=1}^\infty C_n$，等于可数个可数集的并集，则它是可数集，得到矛盾。所以这样的 $M$ 存在。

接下来说明 $B$ 非空，关键就是找到一个点 $s$，能把 $C_M$ 分割成两个不可数集。如果存在 $a,b\in C_M$，使得 $a<b$，$a$ 点左侧的部分和 $b$ 点右侧的部分都是不可数集，那么我们就可以取 $s=a$ 或 $b$。如果对任意的 $s\in C_M$，分割的结果都是左侧为可数集，因为 $\sup C_M$ 存在，所以对任意 $n\in \mathbb{N^+}$，$D_n=\{x:x\in C_M,x<\sup C_M-\displaystyle\frac{1}{n}\}$ 总是可数集，而 $C_M=\displaystyle\bigcup_{n=1}^\infty D_n$ 同上得到是可数集，就又矛盾了，所以肯定存在上述 $s$，即 $s\in B$，得到 $B$ 非空。

同样的方法可以用来证明 $B$ 是开集。对 $s\in B$，若对 $\forall\ \varepsilon>0$，$V_\varepsilon(s)\cap B=\{s\}$，则对 $\forall\ n\in \mathbb{N^+}$，$A_{l(s-\frac{1}{n})}$ 和 $A_{r(s+\frac{1}{n})}$ 都是可数集。而 $\displaystyle\bigcup_{n=1}^\infty A_{l(s-\frac{1}{n})}=\{x:x\in A,x<s\}$ 是不可数集，得出矛盾，所以 $\exists\ \varepsilon>0$，使得 $V_\varepsilon(s)\subseteq B$，所以 $B$ 是开集。

---

## 习题 3.3 紧集

!!! question "练习 3.3.1"
    证明如果 \(K\) 是紧的，那么 \(\sup K\) 和 \(\inf K\) 都存在并且是 \(K\) 的元素。

如果 $K$ 是紧的，则它是闭的且是有界的，由完备性公理可得 $\sup K$ 和 $\inf K$ 都存在，由闭集定义可得它们均属于 $K$。

<br/>


!!! question "练习 3.3.2"
    通过证明如果一个集合 \(K \subseteq  \mathbb{R}\) 是闭且有界的，那么它是紧的，来证明定理3.3.4的逆命题。

对这个集合的任意序列 $\{a_n\}$，因为该集合有界，所以由 Bolzano-weierstrass 定理，它存在收敛子列 $\{a_{n_k}\}$。又因为集合是闭集，所以收敛子列的极限属于该集合。所以它是紧集。

<br/>


!!! question "练习 3.3.3"
    证明第 3.1 节中定义的Cantor集(Cantor set)是一个紧集(compact set)。

由 Cantor 集是一个有界闭集得出它是一个紧集。（闭集性源于它由任意个闭集的交构造而成。）

<br/>


!!! question "练习 3.3.4"
    证明如果 \(K\) 是紧集(compact)且 \(F\) 是闭集(closed)，那么 \(K \cap  F\) 是紧集(compact)。

因为 $K$ 有界，所以 $K\cap F$ 有界。

又因为 $K$ 是紧集，所以对任意序列 $\{x_n\}\subseteq K\cap F$，它存在收敛子列 $\{x_{n_k}\}$，且极限属于 $K$，但又因为 $F$ 是闭集，所以极限也属于 $F$，得出极限属于 $K\cap F$。

所以 $K\cap F$ 是闭集，综上得出 $K\cap F$ 是紧集。

<br/>


!!! question "练习 3.3.5"
    判断以下哪些集合是紧集(compact)。对于那些不是紧集的集合，说明定义 3.3.1 为何不成立。换句话说，给出一个包含在给定集合中的序列，该序列不具有收敛到集合中某个极限的子序列。
    
    (a) \(\mathbb{Q}\) .
    
    (b) \(\mathbb{Q} \cap  \left\lbrack  {0,1}\right\rbrack\) .
    
    (c) \(\mathbb{R}\) .
    
    (d) \(\mathbb{R} \cap  \left\lbrack  {0,1}\right\rbrack\) .
    
    (e) \(\{ 1,1/2,1/3,1/4,1/5,\ldots \}\) .
    
    (f) \(\{ 1,1/2,2/3,3/4,4/5,\ldots \}\) .

(a) $\mathbb{Q}$ 不是紧集，因为它不是闭集。

比如说 $\{x:x\in \mathbb{Q}，|x-\sqrt{2}|<\displaystyle\frac{1}{n},n\in\mathbb{N^+}\}$，这个集合的极限不在 $\mathbb{Q}$ 中。

(b) $\mathbb{Q}\cap [0,1]$ 同样不是闭集，因此同样也不是紧集。构造收敛于 $[0,1]$ 中无理数的有理数序列即可得到反例。

(c) $\mathbb{R}$ 不是紧集，因为它无界。

比如说 $\{x:x\in \mathbb{N^+}\}$ 没有一个收敛子列。

(d) $\mathbb{R}\cap [0,1]$ 是紧集，因为它是闭集且有界。

(e) $\{\displaystyle\frac{1}{n}:n\in \mathbb{N^+}\}$ 不是紧集，因为它的极限 $0$ 不属于该集合，所以它不是闭集。

(f) $\{1,\displaystyle\frac{1}{2},\displaystyle\frac{2}{3},\displaystyle\frac{3}{4},\ldots\}$ 是紧集，因为它有界，而且任意子列的极限均为 $1$，属于该集合，所以它还是闭集。

<br/>


!!! question "练习 3.3.6"
    作为Cantor集(Cantor set)令人惊讶性质的更多证据，按照以下步骤证明和 \(C + C = \{ x + y : x,y \in  C\}\) 等于闭区间 \(\left\lbrack  {0,2}\right\rbrack\) 。(请记住， \(C\) 的长度为零且不包含任何区间。)
    
    观察到 \(\{ x + y : x,y \in  C\}  \subseteq  \left\lbrack  {0,2}\right\rbrack\) 被认为是显而易见的，因此我们只需证明反向包含 \(\left\lbrack  {0,2}\right\rbrack   \subseteq  \{ x + y : x,y \in  C\}\) 。因此，给定 \(s \in  \left\lbrack  {0,2}\right\rbrack\) ，我们必须找到两个元素 \(x,y \in  C\) 满足 \(x + y = s\) 。
    
    (a) 证明存在 \({x}_{1},{y}_{1} \in  {C}_{1}\) 使得 \({x}_{1} + {y}_{1} = s\) 。一般情况下，对于任意 \(n \in  \mathbb{N}\) ，我们总能找到 \({x}_{n},{y}_{n} \in  {C}_{n}\) 使得 \({x}_{n} + {y}_{n} = s\) 。
    
    (b) 考虑到序列 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 不一定收敛，展示如何利用它们生成所需的 \(x\) 和 \(y\) 以满足 \(C\) 中的 \(x + y = s\) 。

(a) 若 $x_1,y_1\in [0,\displaystyle\frac{1}{3}]\cup [\displaystyle\frac{2}{3},1]$，用不等式的性质即可得出 $x_1+y_1\in [0,2]$。（两组四个闭区间可以两两相加得出）

若 $s\in [0,\displaystyle\frac{2}{3}]$，可通过 $x_1,y_1\in [0,\displaystyle\frac{1}{3}]$ 得出。

若 $s\in [\displaystyle\frac{2}{3},\displaystyle\frac{4}{3}]$，可通过 $x_1\in [0,\displaystyle\frac{1}{3}]$，$y_1\in [\displaystyle\frac{2}{3},1]$ 得出。

若 $s\in [\displaystyle\frac{4}{3},2]$，可通过 $x_1,y_1\in [\displaystyle\frac{2}{3},1]$ 得出。

(b) 因为 $C$ 是紧集，所以 $\{x_n\}$ 存在收敛子列 $\{x_{n_k}\}$，其极限 $x\in C$。同理得出 $y\in C$，所以就存在 $x,y\in C$ 使 $x+y=s$。

<br/>


!!! question "练习 3.3.7"
    判断以下命题是真还是假。如果命题成立，提供一个简短的证明；如果命题不成立，提供一个反例。
    
    (a) 任意紧集的交集是紧集。
    
    (b) 设 \(A \subseteq  \mathbb{R}\) 为任意集合，且 \(K \subseteq  \mathbb{R}\) 为紧集。那么，交集 \(A \cap  K\) 是紧集。
    
    (c) 如果 \({F}_{1} \supseteq  {F}_{2} \supseteq  {F}_{3} \supseteq  {F}_{4} \supseteq  \cdots\) 是一个非空闭集的嵌套序列，那么交集 \(\mathop{\bigcap }\limits_{{n = 1}}^{\infty }{F}_{n} \neq  \varnothing\) 。
    
    (d) 有限集总是紧的。
    
    (e) 可数集总是紧的。

(a) 正确。设 $\{K_n:n\in \Lambda\}$ 是紧集的一个族，取 $K=\displaystyle\bigcap_{n\in \Lambda} K_n$。因为任意一个 $K_n$ 有界，所以 $K$ 有界。又因为任意一个 $K_n$ 是闭集，所以 $K$ 是闭集，所以 $K$ 是紧集。

(b) 错误。例如 $A=(0,1)$，$K=[0,2]$。

(c) 错误，与紧集交集不为空不同的是，闭集不一定有界。

例如 $\displaystyle\bigcup_{n=1}^\infty [n,+\infty)=\varnothing$。

(d) 正确。因为有限集是有界闭集。

(e) 错误。例如 $\mathbb{Z},\mathbb{Q},\mathbb{N^+}$ 等都不是紧集。

<br/>


!!! question "练习 3.3.8"
    按照以下步骤证明定理 3.3.8 中的最后一个蕴涵。
    
    假设 \(K\) 满足条件(i)和(ii)，并令 \(\left\{  {{O}_{\lambda } : \lambda  \in  \Lambda }\right\}\) 为 \(K\) 的一个开覆盖。为了引出矛盾，我们假设不存在有限的子覆盖。令 \({I}_{0}\) 为一个包含 \(K\) 的闭区间，并将 \({I}_{0}\) 二等分为两个闭区间 \({A}_{1}\) 和 \({B}_{1}\) 。
    
    (a) 为什么 \({A}_{1} \cap  K\) 或 \({B}_{1} \cap  K\) (或两者)必须没有由 \(\left\{  {{O}_{\lambda } : \lambda  \in  \Lambda }\right\}\) 中的集合组成的有限子覆盖？
    
    (b) 证明存在一个闭区间嵌套序列 \({I}_{0} \supseteq  {I}_{1} \supseteq\)  \({I}_{2} \supseteq  \cdots\) ，其性质为，对于每个 \(n,{I}_{n} \cap  K\) 无法被有限覆盖且 \(\lim \left| {I}_{n}\right|  = 0\) 。
    
    (c) 证明存在一个 \(x \in  K\) ，使得对于所有 \(n\) ， \(x \in  {I}_{n}\) 成立。
    
    (d) 由于 \(x \in  K\) ，原始集合中必须存在一个包含 \(x\) 作为元素的开集 \({O}_{{\lambda }_{0}}\) 。论证必须存在一个足够大的 \({n}_{0}\) ，以保证 \({I}_{{n}_{0}} \subseteq  {O}_{{\lambda }_{0}}\) 。解释为什么这为我们提供了所需的矛盾。

(a) 如果两者都有由 $\{O_\lambda:\lambda\in\Lambda\}$ 中的集合生成的有限子覆盖，则它们的并集 $K$ 就存在有限子覆盖，这样矛盾。

(b) 我们设 $A_1,B_1$ 中与 $K$ 交集无法被有限覆盖的那个闭区间为 $I_1$。并选择 $x_1\in I_1\cap K$。

接下来将 $I_1$ 二等分为 $A_2,B_2$，因为两者无法都被有限覆盖（不然就同 (a) 问出现矛盾），所以选择其中与 $K$ 交集无法被有限覆盖的那个闭区间为 $I_2$，并选择 $x_2\in I_2\cap K$。

$\cdots$

依此类推，我们得到闭区间套 $\{I_n\}$ 和序列 $\{x_n\}$，且 $x_n\in I_n\cap K$。

$\displaystyle\lim_{n\to\infty}|I_n|=\displaystyle\lim_{n\to\infty}\displaystyle\frac{|I_0|}{2^n}=0$。

(c) 因为 $\{x_n\}$ 是有界的，所以它存在收敛子列 $\{x_{n_k}\}$，设其极限为 $x$，因为 $x_n\in K$，所以 $x\in K$。

因为 $I_0\supseteq I_1\supseteq I_2\supseteq\cdots$，所以对 $\forall\ n\in \mathbb{N^+}$，对 $\forall\ k>n$，都有 $x_{n_k}\in I_n$。所以 $x\in I_n$。

(d) 因为 $x\in K$，所以肯定存在一个开集 $O_{\lambda_0}$，使得 $x\in O_{\lambda_0}$。

也就是说，$\exists\ \varepsilon>0$，使得 $V_\varepsilon(x)\subseteq O_{\lambda_0}$。

又因为对 $\forall\ n\in \mathbb{N^+}$，$x\in I_n$，所以 $\exists\ n_0\in \mathbb{N^+}$，使得 $|I_{n_0}|<\varepsilon$。

所以 $I_{n_0}\subseteq V_\varepsilon(x)\subseteq O_{\lambda_0}$，这就说明 $I_{n_0}\cap K$ 可以被有限覆盖，矛盾。

综上所述，$K$ 必定可以被 $\{O_\lambda:\lambda\in\Lambda\}$ 中的有限个集合覆盖。

<br/>


!!! question "练习 3.3.9"
    考虑练习3.3.5中列出的每个集合。对于每个非紧的集合，找到一个没有有限子覆盖的开覆盖。

(a) $\mathbb{Q}$：$\{O_n=(n-1,n+1):n\in \mathbb{Z}\}$。

(b) $\mathbb{Q}\cap [0,1]$：$\left\{O_q=(q-\left|\displaystyle\frac{q-\displaystyle\frac{\sqrt{2}}{2}}{2}\right|,q+\left|\displaystyle\frac{q-\displaystyle\frac{\sqrt{2}}{2}}{2}\right|):q\in \mathbb{Q}\cap [0,1]\right\}$。

(c) $\mathbb{R}$：$\{O_n=(n-1,n+1):n\in \mathbb{Z}\}$。

(e) $\{\displaystyle\frac{1}{n}:n\in \mathbb{N^+}\}$：$\{O_n=\left(\displaystyle\frac{1}{n},2\right):n\in \mathbb{N^+}\}$。

<br/>


!!! question "练习 3.3.10"
    我们称一个集合为“闭紧”的，如果它具有以下性质:每个闭覆盖(即由闭集组成的覆盖)都允许一个有限子覆盖。描述 \(\mathbb{R}\) 的所有闭紧子集。

$\mathbb{R}$ 的所有闭紧子集是有限集和空集。因为任何集合都能以点本身作闭集，进行闭覆盖，这样只有元素有限才能进行有限闭覆盖。

---

## 习题 3.4 完备集与连通集

!!! question "练习 3.4.1"
    如果 \(P\) 是一个完备集且 \(K\) 是紧的，那么交集 \(P \cap  K\) 是否总是紧的？是否总是完备的？

因为完备集也是闭集，所以 $P\cap K$ 是闭集。又因为紧集有界，所以 $P\cap K$ 有界。所以 $P\cap K$ 是紧集。

它们的交可能不是完备集，例如 $K=\{1\}$，其本身就是孤立点。

<br/>


!!! question "练习 3.4.2"
    是否存在一个仅由有理数组成的完备集？

没有，因为完备集是不可数的。

<br/>


!!! question "练习 3.4.3"
    回顾定理3.4.2给出的证明部分，并按照这些步骤完成论证。
    
    (a) 因为 \(x \in  {C}_{1}\) ，论证存在一个 \({x}_{1} \in  C \cap  {C}_{1}\) 满足 \({x}_{1} \neq  x\) 且满足 \(\left| {x - {x}_{1}}\right|  \leq  1/3\) 。
    
    (b) 通过证明对于每个 \(n \in  \mathbb{N}\) ，存在一个不同于 \(x\) 的 \({x}_{n} \in  C \cap  {C}_{n}\) 满足 \(\left| {x - {x}_{n}}\right|  \leq  1/{3}^{n}\) ，来完成证明。

(a) 因为 $x\in [0,\displaystyle\frac{1}{3}]\cup [\displaystyle\frac{2}{3},1]$，且各区间的长度均为 $\displaystyle\frac{1}{3}$，所以设 $x$ 属于某个区间 $P_1$，则取 $x_1$ 等于该区间的两个端点中的一个，满足 $x_1\neq x$，则 $|x_1-x|\leq \displaystyle\frac{1}{3}$。

(b) 同上，因为 $x\in C_n$，所以 $x$ 肯定属于其中某个区间 $P_n$，长度为 $\displaystyle\frac{1}{3^n}$。取 $x_n$ 为该区间的两个端点中的一个，满足 $x_n\neq x$，则 $|x_n-x|\leq \displaystyle\frac{1}{3^n}$。

<br/>


!!! question "练习 3.4.4"
    重复第 3.1 节中的Cantor(Cantor)构造，这次从开区间 \(\left\lbrack  {0,1}\right\rbrack\) 开始。然而，这次从每个组成部分中移除开中间四分之一。
    
    (a) 结果集是紧的吗？是完备的吗？
    
    使用第3.1节中的算法，计算这个类Cantor集(Cantor-like set)的长度和维度。

(a) 这个类 Cantor 集是有界闭集（由任意闭集构造），所以它是紧集。

因为之后每个闭区间的长度都是前一个的 $\displaystyle\frac{3}{8}$，所以任意一个闭区间套的长度趋于 $0$，也就是说对任意元素仍然可以构造收敛序列，所以它是完备集。

(b) 因为 $|C_{n+1}|=\displaystyle\frac{3}{4}|C_n|$，所以

$$ 
    |C|=\displaystyle\lim_{n\to\infty}|C_n|=\displaystyle\lim_{n\to\infty}\left(\displaystyle\frac{3}{4}\right)^n=0。
$$

因为把 $[0,1]$ 变为 $\displaystyle\frac{8}{3}$ 倍后，会得到两个副本，所以维度 $x$ 满足 $\left(\displaystyle\frac{8}{3}\right)^x=2$，得 $x=\displaystyle\frac{\ln2}{3\ln2-\ln3}\approx 0.71$。

<br/>


!!! question "练习 3.4.5"
    设 \(A\) 和 \(B\) 是 \(\mathbb{R}\) 的子集。证明如果存在不相交的开集 \(U\) 和 \(V\) ，使得 \(A \subseteq  U\) 和 \(B \subseteq  V\) ，则 \(A\) 和 \(B\) 是分离的。

证明 $U$ 和 $V$ 是分离的即可。

首先证明 $\overline{U}\cap V=\varnothing$，即 $U$ 的极限点不可能在 $V$ 中。假设 $U$ 的极限点 $x$ 在 $V$ 中，因为 $V$ 是开集，所以 $\exists\ \varepsilon>0$，使得 $V_\varepsilon(x)\subseteq V$。又因为 $x$ 是 $U$ 的极限点，所以 $\exists\ y\in U$，使得 $y\in V_\varepsilon(x)$，这就说明 $U$ 和 $V$ 交集不为空，矛盾。

同理可证 $\overline{V}\cap U=\varnothing$，所以 $U$ 和 $V$ 是分离的。

因为 $A\subseteq U$，$B\subseteq V$，所以 $A$ 的极限点不可能在 $B$ 中，反之同理。所以 $A$ 和 $B$ 是分离的。

<br/>


!!! question "练习 3.4.6"
    证明定理3.4.6。

$\Rightarrow)$ 若 $E$ 是连通集，则 $E$ 的任意分割 $A$ 和 $B$ 都不分离，即 $\overline{A}\cap B$ 和 $\overline{B}\cap A$ 必有其一不为空。假设 $\overline{A}\cap B\neq \varnothing$，则 存在 $x\in \overline{A}\cap B$，所以 $x$ 是 $A$ 的极限点。所以 $\exists\ \{x_n\}\subseteq A$，使得 $x_n\to x$。也就是 存在 $A$ 中的序列收敛到 $B$ 中的点 $x$。另一种情况也同理。

$\Leftarrow)$ 若 $E$ 的任意分割 $A$ 和 $B$ 都存在上述的收敛序列，设 $A$ 中的序列收敛到 $B$ 中的点 $x$，则 $x$ 是 $A$ 的极限点，所以 $x\in \overline{A}\cap B$，所以 $\overline{A}\cap B\neq \varnothing$。另一种情况也同理。所以 $E$ 是连通集。

<br/>


!!! question "练习 3.4.7"
    (a) 找出一个闭包连通但非连通的集合的例子。
    
    (b) 如果 \(A\) 是连通的， \(\bar{A}\) 是否必然连通？如果 \(A\) 是完备的， \(\bar{A}\) 是否必然完备？

(a) 构造两个相邻开集的并，例如 $(0,1)\cup(1,2)$。

(b) 如果 $A$ 是连通的，则 $A$ 是一个区间。因为 $\overline{A}$ 也是一个区间，所以它也是连通的。

如果 $A$ 是完备的，则它是闭集，所以 $\overline{A}=A$，它也是完备的。

<br/>


!!! question "练习 3.4.8"
    一个集合 \(E\) 是完全非连通的，如果给定任意两点 \(x,y \in\)  \(E\) ，存在分离的集合 \(A\) 和 \(B\) ，使得 \(x \in  A,y \in  B\) ，且 \(E = A \cup  B\) 。
    
    (a) 证明 \(\mathbb{Q}\) 是完全非连通的。
    
    (b) 无理数集是完全非连通的吗？

(a) 给定任意 $p,q\in \mathbb{Q}$，则 $\exists\ x\in \mathbb{R}\setminus \mathbb{Q}$，使得 $p<x<q$。令 $A=(-\infty,x)\cap \mathbb{Q}$，$B=(x,+\infty)\cap \mathbb{Q}$，则 $A$ 和 $B$ 是分离的，且 $\mathbb{Q}=A\cup B$，所以 $\mathbb{Q}$ 是完全非连通的。

(b) 同理，因为任何两个无理数间都能找到一个有理数，所以无理数集也是完全非连通的。

<br/>

$3.4.9.$<a id="3.4.9."></a>

(a) $C_n$ 的单个闭区间长度为 $\displaystyle\frac{1}{3^n}$，所以取 $N>\log_3{\displaystyle\frac{1}{\varepsilon}}$，就有 $\displaystyle\frac{1}{3^N}<\varepsilon$，这样 $x,y$ 就不能属于同一个闭区间了。

(b) 因为 $x,y$ 不在同一个闭区间内，而 $C_N$ 任意两个闭区间内都存在不属于 $C$ 的点 $z$，这样就得到答案。所以 $(x,y)$ 内总有不属于 $C$ 的点 $z$。

(c) 所以上述的 $(x,z)$，$(z,y)$ 是分离的。令 $A=[0,z)\cap C$，$B=(z,1]\cap C$，则 $x\in A$，$y\in B$，$C=A\cup B$，且 $A,B$ 是分离的。

所以 $C$ 是完全非连通的。

<br/>


!!! question "练习 3.4.10"
    设 \(\left\{  {{r}_{1},{r}_{2},{r}_{3},\ldots }\right\}\) 为有理数的一个枚举，对于每个 \(n \in  \mathbb{N}\) 设 \({\varepsilon }_{n} = 1/{2}^{n}\) 。定义 \(O = \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{V}_{{\varepsilon }_{n}}\left( {r}_{n}\right)\) ，并设 \(F = {O}^{c}.\)
    
    (a) 论证 \(F\) 是一个闭的、非空的集合，且仅由无理数组成。
    
    (b) \(F\) 是否包含任何非空开区间？ \(F\) 是否是完全非连通的？(定义见练习 3.4.8。)
    
    (c) 是否有可能知道 \(F\) 是否是完全的？如果不能，我们能否修改此构造以生成一个非空的完全无理数集？

(a) 因为 $O$ 是任意个开集的交，所以它是开集，$F=O^c$ 就是闭集。

又因为 $|O|=\displaystyle\sum_{n=1}^{\infty}2\cdot \displaystyle\frac{1}{2^n}=2$ 有限，所以 $F$ 是非空的。

又因为 $O$ 包含所有有理数，所以 $F$ 只包含无理数。

(b) 因为任何非空开区间都包含有理数，所以 $F$ 不包含任何开区间。

又因为任何两个无理数间都存在有理数，所以 $F$ 是完全非连通的。

(c) 参考资料：[MSE上的讨论：F有可能完备吗？](https://math.stackexchange.com/questions/2854900/constructing-perfect-set-without-rationals-by-removing-open-neighborhood-around/2857460#2857460)

---

## 习题 3.5 Baire 定理

!!! question "练习 3.5.1"
    论证一个集合 \(A\) 是 \({G}_{\delta }\) 集合当且仅当它的补集是 \({F}_{\sigma }\) 集合。

设 $B$ 是 $G_\delta$ 集合，则 $B=\displaystyle\bigcap_{n=1}^\infty O_n$，其中 $O_n$ 是开集。

由德·摩根律可得 $B^c=\left(\displaystyle\bigcap_{n=1}^\infty O_n\right)^c=\displaystyle\bigcup_{n=1}^\infty O_n^c$，其中 $O_n^c$ 是闭集，所以 $B^c$ 是 $F_\sigma$ 集。

由 $(B^c)^c=B$，同理可得 $F_\sigma$ 集的补集是 $G_\delta$ 集。

<br/>


!!! question "练习 3.5.2"
    根据哪个更合适，将每个\_\_\_\_\_替换为单词“有限”或“可数”。
    
    (a) \({F}_{\sigma }\) 集合的\_\_\_\_\_并集是一个 \({F}_{\sigma }\) 集合。
    
    (b) \({F}_{\sigma }\) 集合的\_\_\_\_\_交集是一个 \({F}_{\sigma }\) 集合。
    
    (c) \({G}_{\delta }\) 集合的\_\_\_\_\_并集是一个 \({G}_{\delta }\) 集合。
    
    (d)\_\_\_\_\_ 集合的交集是一个 \({G}_{\delta }\) 集合。

(a) 可数

(b) 有限

(c) 有限

(d) 可数

<br/>

$3.5.3.$ 在 [$3.2.14.$](#3.2.14.) 中已经证明。

<br/>


!!! question "练习 3.5.4"
    (a) 从 \(n = 1\) 开始，归纳地构造一个满足 \({I}_{n} \subseteq  {G}_{n}\) 的闭区间嵌套序列 \({I}_{1} \supseteq  {I}_{2} \supseteq  {I}_{3} \supseteq  \cdots\) 。特别注意每个 \({I}_{n}\) 的端点问题。
    
    (b) 现在，使用定理 3.3.5 或闭区间套性质来完成证明。

(a) 首先寻找包含于开集 $G_1$ 的一个开区间，并在其中构造闭区间 $I_1$。因为 $G_1$ 是稠密的，所以 $\exists\ x_1\in G_1$，并 $\exists\ \varepsilon_1>0$ 使 $V_{\varepsilon_1}(x_1)\subseteq G_1$，取 $I_1=[x_1-\displaystyle\frac{\varepsilon_1}{2},x_1+\displaystyle\frac{\varepsilon_1}{2}]$。

现在构造 $I_2$。因为 $G_2$ 是稠密的，所以 $\exists\ x_2\in I_1$，$x_2\in G_2$，并 $\exists\ \varepsilon_2>0$ 使 $V_{\varepsilon_2}(x_2)\subseteq G_2$，$V_{\varepsilon_2}(x_2)\subseteq I_1$，取 $I_2=[x_2-\displaystyle\frac{\varepsilon_2}{2},x_2+\displaystyle\frac{\varepsilon_2}{2}]$。

同理，对 $\forall\ n\in \mathbb{N^+}$，可得 $I_n$，由此得到闭区间列 ${I_n}$。

(b) 由闭区间套定理，$\exists\ x\in \displaystyle\bigcap_{n=1}^\infty I_n$。

因为 $x\in I_n\Rightarrow x\in G_n$，所以 $x\in \displaystyle\bigcap_{n=1}^\infty G_n$。

<br/>

$3.5.5.$<a id="3.5.5."></a>

$\left(\displaystyle\bigcup_{n=1}^\infty F_n\right)^c=\displaystyle\bigcap_{n=1}^\infty F_n^c$，得到可数开集的交，利用 $3.5.4.$ 指出它非空即可。

由 $F_n$ 不包含任何非空开区间，所以对 $\forall\ x<y\in R$，$\exists\ i\in (x,y)$，$i\notin F_n \Rightarrow i\in F_n^c$，这说明 $F_n^c$ 是稠密的。

所以 $\displaystyle\bigcap_{n=1}^\infty F_n^c\neq \varnothing \Rightarrow \displaystyle\bigcup_{n=1}^\infty F_n\neq \mathbb{R}$。

<br/>


!!! question "练习 3.5.6"
    展示前一个练习如何暗示无理数集 \(\mathbb{R}\setminus\mathbb{Q}\) 不能是一个 \({F}_{\sigma }\) 集，且 \(\mathbb{Q}\) 不能是一个 \({G}_{\delta }\) 集。

如果 $\mathbb{R}\setminus \mathbb{Q}$ 可以写成可数闭集的并，由有理数集稠密性可知这些闭集都不包括非空开区间。因为 $\mathbb{Q}$ 可以写成可数上述性质闭集的并，所以 $\mathbb{R}$ 也可以写成可数上述性质闭集的并，这与 $3.5.5.$ 矛盾。

所以 $\mathbb{R}\setminus \mathbb{Q}$ 不是 $F_\sigma$ 集，$\mathbb{Q}$ 也不是 $G_\delta$ 集。

<br/>


!!! question "练习 3.5.7"
    使用练习 3.5.6 和练习 3.5.2 中的陈述版本，构造一个既不在 \({F}_{\sigma }\) 也不在 \({G}_{\delta }\) 中的集合。

(a) 设 $A=\mathbb{R}\setminus\mathbb{Q}\cap (-\infty,0]$，$B=\mathbb{Q}\cap (0,+\infty)$，我们证明 $A\cup B$ 满足题意。

首先，$A$ 不是 $F_\sigma$ 集。

若 $A$ 是 $F_\sigma$ 集，则 $A=\displaystyle\bigcup_{n=1}^\infty F_n$，其中 $F_n$ 是闭集。

现在令 $-F_n=\{-x,x\in F_n\}$，则 $-F_n$ 是闭集，且 $\mathbb{R}\setminus\mathbb{Q}\cap [0,+\infty)=\displaystyle\bigcup_{n=1}^\infty (-F_n)$，所以 $\mathbb{R}\setminus\mathbb{Q}=A\cup \left(\displaystyle\bigcup_{n=1}^\infty (-F_n)\right)$，是 $F_\sigma$ 集，矛盾。

同理可得 $B$ 不是 $G_\delta$ 集。

现在，若 $A\cup B$ 是 $F_\sigma$ 集，则 $(A\cup B) \cap (-\infty,0]=A$ 是 $F_\sigma$ 集，矛盾。

所以 $A\cup B$ 不是 $F_\sigma$ 集。同理可得 $A\cup B$ 不是 $G_\delta$ 集。

<br/>


!!! question "练习 3.5.8"
    证明集合 \(E\) 在 \(\mathbb{R}\) 中是无处稠密的，当且仅当 \(\bar{E}\) 的补集在 \(\mathbb{R}\) 中是稠密的。

$\Rightarrow)$ 由定义，对 $\forall\ x<y\in \mathbb{R}$，$\exists\ z\in (x,y)$，$z\notin \overline{E}\Rightarrow z\in (\overline{E})^c$。

所以 $(\overline{E})^c$ 是稠密的。

$\Leftarrow)$ 如果 $(\overline{E})^c$ 是稠密的，则对 $\forall\ x<y\in \mathbb{R}$，$\exists\ z\in (x,y)$，$z\in (\overline{E})^c\Rightarrow z\notin \overline{E}$。

所以 $\overline{E}$ 不包含任何非空开区间。

<br/>


!!! question "练习 3.5.9"
    判断以下集合在 \(\mathbb{R}\) 中是稠密的、无处稠密的，还是介于两者之间。
    
    (a) \(A = \mathbb{Q} \cap  \left\lbrack  {0,5}\right\rbrack\) .
    
    (b) \(B = \{ 1/n : n \in  \mathbb{N}\}\) .
    
    (c) 无理数集。
    
    (d) Cantor集。

(a) 两者之间

(b) 无处稠密的

(c) 稠密的

(d) 无处稠密的。[$3.4.9.$](#3.4.9.) 告诉我们 $C$ 是完全非连通的，而且 $C$ 是闭集。

<br/>


!!! question "练习 3.5.10"
    通过找到与本节结果相矛盾的结论来完成证明。

[$3.5.5.$](#3.5.5.) 指出，$\mathbb{R}$ 不能写成如下集合的可数并集：不包含任何非空开区间的闭集。

因为 $E_n$ 是无处稠密的，所以 $\overline{E_n}$ 就是不包含任何非空开区间的闭集。

所以 $\mathbb{R}\neq \displaystyle\bigcup_{n=1}^\infty \overline{E_n}$，即 $\displaystyle\bigcup_{n=1}^\infty \overline{E_n}\subsetneqq\mathbb{R}$。

这就是说，$\exists\ x\in \mathbb{R}$，$x\notin \displaystyle\bigcup_{n=1}^\infty \overline{E_n}$。

因为 $E_n\subseteq \overline{E_n}$，所以 $\displaystyle\bigcup_{n=1}^\infty E_n\subseteq \displaystyle\bigcup_{n=1}^\infty \overline{E_n}\Rightarrow x\notin \displaystyle\bigcup_{n=1}^\infty E_n$。

所以 $\mathbb{R}\neq \displaystyle\bigcup_{n=1}^\infty E_n$，矛盾。

综上所述，$\mathbb{R}$ 不能表示成无处稠密集的可数并集。

---

# 函数极限与连续性

## 习题 4.2 函数极限

!!! question "练习 4.2.1"
    使用定义 $4.2.1$ 为以下极限语句提供证明。

    (a) $\displaystyle\lim_{x \to 2}(2x + 4) = 8$．

    (b) $\displaystyle\lim_{x \to 0}x^3 = 0$．

    (c) $\displaystyle\lim_{x \to 2}x^3 = 8$．

    (d) $\displaystyle\lim_{x \to \pi}[[x]] = 3$，其中 $[[x]]$ 表示小于或等于 $x$ 的最大整数．

(a) 对 $\forall\ \varepsilon>0$，$\exists\ \delta=\displaystyle\frac{\varepsilon}{2}$，对 $\forall\ 0<|x-2|<\delta$，有 $|(2x+4)-8|<2\delta=\varepsilon$，所以 $\displaystyle\lim_{x\to 2}(2x+4)=8$．

(b) 对 $\forall\ \varepsilon>0$，$\exists\ \delta=\sqrt[3]{\varepsilon}$，对 $\forall\ 0<|x|<\delta$，有 $|x^3-0|<\delta^3=\varepsilon$，所以 $\displaystyle\lim_{x\to 0}x^3=0$．

(c) 此题需要估计 $x^3-8=(x-2)(x^2+2x+4)$ 的范围．当 $1<x<3$ 时，$x^2+2x+4<19$，再配合 $|x-2|$ 大小的任意性给出证明．

对 $\forall\ \varepsilon>0$，$\exists\ \delta=\min\{\displaystyle\frac{\varepsilon}{19},1\}$，对 $\forall\ 0<|x-2|<\delta$，有 $|x^3-8|=|x-2||x^2+2x+4|<\displaystyle\frac{\varepsilon}{19}\cdot 19=\varepsilon$，所以 $\displaystyle\lim_{x\to 2}x^3=8$．

(d) 对 $\forall\ \varepsilon>0$，取 $\delta=0.1$，对 $\forall\ 0<|x-\pi|<\delta$，$x\in (3,3.3)$，所以 $\left|[[x]]-3\right|=0<\varepsilon$，所以 $\displaystyle\lim_{x\to \pi}[[x]]=3$．

<br/>
 
!!! question "练习 4.2.2"
    假设某个 $\delta > 0$ 已被构造为对特定 $\varepsilon$ 挑战的适当响应。那么，任何更大/更小(选择一个)的 $\delta$ 也将足够．

任何更小的 $\delta$ 是足够的．

考虑一个 $\delta$ 满足对 $\forall\ x\in V_\delta(c)$，$f(x)\in V_\varepsilon(L)$ 均成立，则由于对任意 $\delta_1<\delta$，$V_{\delta_1}(c)\subseteq V_\delta(c)$，所以对 $\forall\ x\in V_{\delta_1}(c)$ 也同样成立，所以任何更小的 $\delta$ 也将足够。

<br/>

!!! question "练习 4.2.3"
    使用推论 4.2.5 证明以下每个极限不存在。 

    (a) $\displaystyle\lim_{x \to 0}|x|/x$

    (b) $\displaystyle\lim_{x \to 1}g(x)$，其中 $g$ 是来自第4.1节的Dirichlet函数。

(a) 设 $f(x)=\displaystyle\frac{|x|}{x}$，考虑如下序列 $x_n=\displaystyle\frac{1}{n}$ 和 $y_n=-\displaystyle\frac{1}{n}$，则 $\displaystyle\lim_{n\to \infty}x_n=\displaystyle\lim_{n\to \infty}y_n=0$，但 $\displaystyle\lim_{n\to \infty}f(x_n)=1$，$\displaystyle\lim_{n\to \infty}f(y_n)=-1$，所以原极限不存在。

(b) 同理，令 $x_n=1+\displaystyle\frac{1}{n}$ 为有理数序列，$y_n=1+\displaystyle\frac{\sqrt{2}}{n}$ 为无理数序列，则 $\displaystyle\lim_{n\to \infty}g(x_n)=1$，$\displaystyle\lim_{n\to \infty}g(y_n)=0$，所以原极限不存在。

<br/>

!!! question "练习 4.2.4"
    回顾第4.1节中Thomae函数(Thomae’s function) $t(x)$ 的定义。

    (a) 构造三个不同的序列 $(x_n)$，$(y_n)$，$(z_n)$，每个序列都收敛到 $1$，但不使用数字 $1$ 作为序列中的项。

    (b) 现在，计算 $\lim t(x_n)$，$\lim t(y_n)$ 和 $\lim t(z_n)$。

    (c) 对 $\displaystyle\lim_{x \to 1}t(x)$ 做出一个有根据的猜想，并使用定义 $4.2.1B$ 来验证该主张。(给定 $\varepsilon > 0$，考虑点集 $\{ x \in \mathbb{R} : t(x) \geq \varepsilon \}$。论证该集合中的所有点都是孤立的。)

(a) $x_n=1+\displaystyle\frac{1}{n}$，$y_n=1-\displaystyle\frac{1}{n}$，$z_n=1+\displaystyle\frac{\sqrt{2}}{n}$。

(b) $\displaystyle\lim_{n\to \infty}t(x_n)=\displaystyle\lim_{n\to \infty}t(y_n)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{1}{n}=0$，$\displaystyle\lim_{n\to \infty}t(z_n)=\displaystyle\lim_{n\to \infty}0=0$。

(c) $\displaystyle\lim_{x\to 1}t(x)=0$。

<a id="4.2.4"></a> 

对 $\forall\ \varepsilon>0$，$\exists\ n\in \mathbb{N^+}$，使得 $\displaystyle\frac{1}{n}>\varepsilon$ 而 $\displaystyle\frac{1}{n+1}<\varepsilon$。所以，点集 $S=\{ x\in \mathbb{R}:t(x)\geq \varepsilon \}=\{x=\displaystyle\frac{p}{q}:p,q\in \mathbb{N^+},q \leq n,\gcd{(p,q)}=1\}$。因为该集合中任意两个点的距离至少为 $\displaystyle\frac{1}{n^2}$，所以该集合中的所有点都是孤立的。

又因为 $1\in S$，所以 $1$ 也是孤立的，因此一定存在 $\delta>0$，使得对于 $\forall\ x\in V_\delta(1)\setminus\{1\}$，都有 $t(x)<\varepsilon$，所以 $\displaystyle\lim_{x\to 1}t(x)=0$。

<br/>

!!! question "练习 4.2.5"
    (a) 详细说明推论 4.2.4 第 (ii) 部分如何从定理 4.2.3 中函数极限的序列准则和第 2 章中证明的序列代数极限定理得出。

    (b) 现在，直接从定义 4.2.1 出发，不使用定理 4.2.3 中的序列准则，写出推论 4.2.4 第 (ii) 部分的另一个证明。

    (c) 对推论 4.2.4 第 (iii) 部分重复 (a) 和 (b)。

(a) 由海涅定理可知，对 $\forall\ x_n \neq c$，$\{x_n\}\rightarrow c$，都有 $f(x_n)\rightarrow L$，$g(x_n)\rightarrow M$，即 $(f(x_n)+g(x_n))\rightarrow L+M$，所以 $\displaystyle\lim_{x\to c}(f(x)+g(x))=L+M$。

(b) 对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，使得对 $\forall\ 0<|x-c|<\delta_1$，有 $|f(x)-L|<\displaystyle\frac{\varepsilon}{2}$，对 $\forall\ 0<|x-c|<\delta_2$，有 $|g(x)-M|<\displaystyle\frac{\varepsilon}{2}$。取 $\delta=\min\{\delta_1,\delta_2\}$，则对 $\forall\ 0<|x-c|<\delta$，有 $|f(x)+g(x)-(L+M)|\leq |f(x)-L| + |g(x)-M| <\displaystyle\frac{\varepsilon}{2}+\frac{\varepsilon}{2} = \varepsilon$。

所以 $\displaystyle\lim_{x\to c}(f(x)+g(x))=L+M$。

(c) (i) 由海涅定理可知，对 $\forall\ x_n \neq c$，$\{x_n\}\rightarrow c$，都有 $f(x_n)\rightarrow L$，$g(x_n)\rightarrow M$，即 $(f(x_n)g(x_n))\rightarrow LM$，所以 $\displaystyle\lim_{x\to c}(f(x)g(x))=LM$。

(ii) 对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，使得对 $\forall\ 0<|x-c|<\delta_1$，有 $|f(x)-L|<\displaystyle\frac{\varepsilon}{2|M|}<|L|$，对 $\forall\ 0<|x-c|<\delta_2$，有 $|g(x)-M|<\displaystyle\frac{\varepsilon}{4|L|}$。取 $\delta=\min\{\delta_1,\delta_2\}$，则对 $\forall\ 0<|x-c|<\delta$，有 $|f(x)g(x)-LM|\leq |f(x)||g(x)-M|+|f(x)-L||M|<2|L|\cdot \displaystyle\frac{\varepsilon}{4|L|}+\displaystyle\frac{\varepsilon}{2|M|}\cdot |M|=\varepsilon$。

所以 $\displaystyle\lim_{x\to c}(f(x)g(x))=LM$。

<br/>

!!! question "练习 4.2.6"
    设 $g : A \to \mathbb{R}$ 并假设 $f$ 是 $A \subseteq \mathbb{R}$ 上的有界函数(即存在 $M > 0$ 满足对于所有 $x \in A$ 有 $|f(x)| \leq M$)。证明如果 $\displaystyle\lim_{x \to c}g(x) = 0$，则 $\displaystyle\lim_{x \to c}g(x)f(x) = 0$ 也成立。

由 $\displaystyle\lim_{x\to c}g(x)=0$，对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ 0<|x-c|<\delta$，有 $|g(x)-0|<\displaystyle\frac{\varepsilon}{M}$，即 $|g(x)f(x)|<\displaystyle\frac{\varepsilon}{M}\cdot M=\varepsilon$，所以 $\displaystyle\lim_{x\to c}g(x)f(x)=0$。

<br/>

!!! question "练习 4.2.7"
    (a) 陈述 $\displaystyle\lim_{x \to 0}1/x^2 = \infty$ 在直觉上显然是有意义的。为形式为 $\displaystyle\lim_{x \to c}f(x) = \infty$ 的极限陈述构建一个类似于定义 4.2.1 的“挑战-回应”风格的严格定义，并用它来证明之前的陈述。

    (b) 现在，为陈述 $\displaystyle\lim_{x \to \infty}f(x) = L$ 构建一个定义。展示 $\displaystyle\lim_{x \to \infty}1/x = 0$。

    (c) $\lim_{x \to \infty}f(x) = \infty$ 的严格定义会是什么样？给出一个这样的极限的例子。

(a) 对 $\forall\ M>0$，$\exists\ \delta>0$，使得对 $\forall\ 0<|x-c|<\delta$，都有 $f(x)>M$。

(b) 对 $\forall\ \varepsilon>0$，$\exists\ G>0$，使得对 $\forall\ |x|>G$，都有 $|f(x)-L|<\varepsilon$。

例如，取 $G=\displaystyle\frac{1}{\varepsilon}$，则对 $\forall\ |x|>G$，有 $\left|\displaystyle\frac{1}{x}-0\right|<\varepsilon$，所以 $\displaystyle\lim_{x\to \infty}\displaystyle\frac{1}{x}=0$。

(c) 对 $\forall\ M>0$，$\exists\ G>0$，对 $\forall\ |x|>G$，有 $f(x)>M$。
例如：$f(x)=x$。

<br/>

!!! question "练习 4.2.8"
    假设对于某个集合 $A$ 中的所有 $x$， $f(x) \geq g(x)$ 成立，其中 $f$ 和 $g$ 在该集合上定义。证明对于 $A$ 的任何极限点 $c$，我们必须有

    $$
    \lim_{x \to c}f(x) \geq \lim_{x \to c}g(x).
    $$

对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，对 $\forall\ 0<|x-c|<\delta_1$，有 $|f(x)-\displaystyle\lim_{x\to c}f(x)|<\varepsilon\Rightarrow f(x)<\displaystyle\lim_{x\to c}f(x)+\varepsilon$，对 $\forall\ 0<|x-c|<\delta_2$，有 $|g(x)-\displaystyle\lim_{x\to c}g(x)|<\varepsilon\Rightarrow g(x)>\displaystyle\lim_{x\to c}g(x)-\varepsilon$。由 $f(x)\geq g(x)$ 可得

$$
\displaystyle\lim_{x\to c}f(x)>\displaystyle\lim_{x\to c}g(x)-2\varepsilon.
$$

这里由 $\varepsilon$ 的任意性就可知道 $\displaystyle\lim_{x\to c}f(x)$ 不能比 $\displaystyle\lim_{x\to c}g(x)$ 小，否则总会有一段空隙让 $\varepsilon$ 插入。

假设 $\displaystyle\lim_{x\to c}f(x)<\displaystyle\lim_{x\to c}g(x)$，则令 $\varepsilon=\displaystyle\frac{\displaystyle\lim_{x\to c}g(x)-\displaystyle\lim_{x\to c}f(x)}{2}>0$，代入上式可得 $\displaystyle\lim_{x\to c}f(x)>\displaystyle\lim_{x\to c}f(x)$，矛盾。

所以 $\displaystyle\lim_{x\to c}f(x)\geq \displaystyle\lim_{x\to c}g(x)$。

<br/>

!!! question "练习 4.2.9(夹逼定理)"
    设 $f$，$g$，$h$ 满足 $f(x) \leq g(x) \leq h(x)$ 对于所有在某个共同定义域 $A$ 中的 $x$ 。如果 $\displaystyle\lim_{x \to c}f(x) = L$ 且 $\displaystyle\lim_{x \to c}h(x) = L$ 在 $A$ 的某个极限点 $c$ 处，证明 $\displaystyle\lim_{x \to c}g(x) = L$ 也成立。

对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，使得对 $\forall\ 0<|x-c|<\delta_1$，有 $|f(x)-L|<\varepsilon$，对 $\forall\ 0<|x-c|<\delta_2$，有 $|h(x)-L|<\varepsilon$。取 $\delta=\min\{\delta_1,\delta_2\}$，则对 $\forall\ 0<|x-c|<\delta$，有 $L-\varepsilon<f(x)<L+\varepsilon$，$L-\varepsilon<h(x)<L+\varepsilon$。因为 $f(x)\leq g(x)\leq h(x)$，所以 $L-\varepsilon<g(x)<L+\varepsilon\Rightarrow |g(x)-L|<\varepsilon$，所以 $\displaystyle\lim_{x\to c}g(x)=L$。

---

## 习题 4.3 连续函数的运算

!!! question "练习 4.3.1"
    设 $g\left( x\right)  = \sqrt[3]{x}$ 。

    (a) 证明 $g$ 在 $c = 0$ 处连续。

    (b) 证明 $g$ 在点 $c \neq  0$ 处连续。(恒等式 ${a}^{3} - {b}^{3} =$  $\left( {a - b}\right) \left( {{a}^{2} + {ab} + {b}^{2}}\right)$ 将有所帮助。)

(a) 对 $\forall\ \varepsilon>0$，$\exists\ \delta=\varepsilon^3$，对 $\forall\ |x|<\delta$，$|\sqrt[3]{x}-\sqrt[3]{0}|<\varepsilon$，所以 $g$ 在 $0$ 处连续。

(b) 由恒等式，我们可得
$$
|\sqrt[3]{x}-\sqrt[3]{c}|=\frac{|x-c|}{|\sqrt[3]{x^2}+\sqrt[3]{xc}+\sqrt[3]{c^2}|}
$$
我们通过控制 $|x-c|$ 的大小来控制 $|\sqrt[3]{x}-\sqrt[3]{c}|$ 的大小，所以对 $\forall\ \varepsilon>0$，$\exists\ \delta=\min\{\sqrt[3]{c^2}\varepsilon,\left|\displaystyle\frac{c}{2}\right|\}$，使得对 $\forall\ |x-c|<\delta$，有 $xc>0$，所以这样就能将分母放缩，得到
$$
|\sqrt[3]{x}-\sqrt[3]{c}|=\frac{|x-c|}{|\sqrt[3]{x^2}+\sqrt[3]{xc}+\sqrt[3]{c^2}|}<\displaystyle\frac{|x-c|}{\sqrt[3]{c^2}}<\displaystyle\frac{\sqrt[3]{c^2}\varepsilon}{\sqrt[3]{c^2}}<\varepsilon
$$
所以 $g$ 在点 $c\neq 0$ 处连续。

<br/>

!!! question "练习 4.3.2"
    (a) 使用连续性的 $\varepsilon  - \delta$ 特征为定理 4.3.9 提供证明。

    (b) 使用连续性的序列特征(来自定理 4.3.2 (iv))给出该定理的另一个证明。

(a) 若 $g$ 在 $f(c)$ 上连续，则对 $\forall\ \varepsilon>0$，$\exists\ \delta_1>0$，对 $\forall\ |y-f(c)|<\delta_1$，$|g(y)-g(f(c))|<\varepsilon$。

而对上述 $\delta_1>0$，$\exists\ \delta_2>0$，对 $\forall\ |x-c|<\delta_2$，$|f(x)-f(c)|<\delta_1$，此时 $|g(f(x))-g(f(c))|<\varepsilon$，所以 $g(f(x))$ 在 $c$ 处连续。

(b) 由题，对 $\forall\ \{x_n\}\rightarrow c$，$f(x_n)\rightarrow f(c)$。

又因为对 $\forall\ \{y_n\}\rightarrow f(c)$，$g(y_n)\rightarrow g(f(c))$，所以用 $f(x_n)$ 代替 $y_n$ 可得 $g(f(x_n))\rightarrow g(f(c))$。
所以 $g(f(x))$ 在 $c$ 处连续。

<br/>

!!! question "练习 4.3.3"
    使用连续性的 $\varepsilon  - \delta$ 特征(因此不使用关于序列的先前结果)，证明线性函数 $f\left( x\right)  = {ax} + b$ 在 $\mathbb{R}$ 的每一点都连续。

 
对 $\forall\ x_0\in \mathbb{R}$，我们有

对 $\forall\ \varepsilon>0$，$\exists\ \delta=\displaystyle\frac{\varepsilon}{a}$，对 $\forall\ |x-x_0|<\delta$，$|f(x)-f(x_0)|\leq|a||x-x_0|<\varepsilon$，所以 $f$ 对 $\forall\ x_0\in \mathbb{R}$ 都连续。

<br/>

!!! question "练习 4.3.4"
    (a) 使用定义 4.3.1 证明，任何定义域为 $\mathbb{Z}$ 的函数 $f$ 在其定义域的每一点都必然连续。

    (b) 证明一般情况下，如果 $c$ 是 $A \subseteq  \mathbb{R}$ 的孤立点，那么 $f : A \rightarrow  \mathbb{R}$ 在 $c$ 处连续。

(a) 对 $\forall\ x_0\in \mathbb{Z}$，我们有
对 $\forall\ \varepsilon>0$，$\exists\ \delta=\displaystyle\frac{1}{2}$，对 $\forall\ |x-x_0|<\delta$，$x=x_0$，所以 $|f(x)-f(x_0)|=0<\varepsilon$，所以 $f$ 对 $\forall\ x_0\in \mathbb{Z}$ 都连续。

(b) 如果 $c$ 是 $A\subseteq \mathbb{R}$ 的孤立点，则总存在 $\delta>0$ 使得对任意 $\left|x-c\right|<\delta$，$x\in A$，$x=c$，则对 $\forall\ \varepsilon>0$，$\left|f(x)-f(c)\right|=0<\varepsilon$。

所以 $f:A\rightarrow \mathbb{R}$ 在 $c$ 处连续。

<br/>

!!! question "练习 4.3.5"
    在定理 4.3.4 中，陈述 (iv) 指出，如果 $f$ 和 $g$ 都连续，且商有定义，则 $f\left( x\right) /g\left( x\right)$ 在 $c$ 处连续。证明如果 $g$ 在 $c$ 和 $g\left( c\right)  \neq  0$ 处连续，则存在一个包含 $c$ 的开区间，在该区间上 $f\left( x\right) /g\left( x\right)$ 始终有定义。

若 $g$ 在 $c$ 处连续，则取 $\varepsilon=\left|\displaystyle\frac{g(c)}{2}\right|$，$\exists\ \delta>0$，对 $\forall\ \left|x-c\right|<\delta$，$\left|g(x)-g(c)\right|<\varepsilon=\left|\displaystyle\frac{g(c)}{2}\right|\Rightarrow \left|g(x)\right|>\left|\displaystyle\frac{g(c)}{2}\right|>0$，所以在 $V_\delta(c)$ 区间上 $\displaystyle\frac{f(x)}{g(x)}$ 始终有定义。

<br/>

!!! question "练习 4.3.6"
    (a) 参考相关定理，给出一个正式论证，证明第4.1节中的Dirichlet函数(Dirichlet’s function)在 $\mathbb{R}$ 上处处不连续。

    (b) 回顾第4.1节中Thomae函数(Thomae's function)的定义，并证明其在每个有理点处都不连续。

    (c) 使用定理4.3.2 (iii)中的连续性特征，证明Thomae函数在 $\mathbb{R}$ 中的每个无理点处连续。(给定 $\varepsilon  > 0$ ，考虑点集 $\{ x \in  \mathbb{R} : t\left( x\right)  \geq  \varepsilon \}$ 。论证该集合中的所有点都是孤立的。)

(a) 对任意的 $c\in \mathbb{R}$，构造两个序列 $\left\{x_n\right\}\rightarrow c$，$\left\{y_n\right\}\rightarrow c$，其中 $x_n\in \mathbb{Q}$，$y_n\in \mathbb{R}\setminus\mathbb{Q}$。这样总有 $\displaystyle\lim_{n\to \infty}D(x_n)=0$，$\displaystyle\lim_{n\to \infty}D(y_n)=1$，由此可得其在 $\mathbb{R}$ 上处处不连续。

(b) 对任意的 $c\in \mathbb{Q}$，构造 $\left\{x_n\right\}\rightarrow c$，其中 $x_n\in \mathbb{R}\setminus\mathbb{Q}$，则 $\displaystyle\lim_{n\to \infty}t(x_n)=0\neq t(c)$，所以其在有理点上均不连续。

(c) 点集的性质在 [练习 4.2.4](#4.2.4) 中已经证明过了。

设 $q\in \mathbb{N^+}$ 满足 $\displaystyle\frac{1}{q}\geq \varepsilon$，$\displaystyle\frac{1}{q+1}<\varepsilon$，则该点集中的点的分母都不会大于 $q$。考虑任意无理数 $x_0$ 的某一邻域 $V_\delta(x_0)$，可知对任意 $n\in \mathbb{N^+}$，$n\leq q$，使得 $\displaystyle\frac{p}{n}\in V_\delta(x_0)$，$\gcd(p,n)=1$ 的有理数是有限的，即在该邻域内点集的点是有限的。

于是取邻域内 $x_0$ 与点集所有点的距离的最小值 $\delta_1$，则对任意 $x\in V_{\delta_1}(x_0)$，$t(x)<\varepsilon$。因此 $\displaystyle\lim_{x\to x_0}t(x)=0=t(x_0)$，所以 $t(x)$ 在无理点上均连续。

<br/>

!!! question "练习 4.3.7"
    假设 $h : \mathbb{R} \rightarrow  \mathbb{R}$ 在 $\mathbb{R}$ 上连续，且令 $K = \{ x$ : $h\left( x\right)  = 0\}$ 。证明 $K$ 是一个闭集。

如果 $K$ 中没有极限点则其为闭集。

如果 $K$ 中存在极限点 $x_0$，则对 $\forall\ \delta>0$，存在 $x\in K$ 且 $|x-x_0|<\delta$，$h(x)=0$。

因为 $h$ 在 $\mathbb{R}$ 上连续，所以对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$ 使得对 $\forall\ |x-x_0|<\delta$，有 $|h(x)-h(x_0)|<\varepsilon$。而对这个 $\delta$，又 $\exists\ x_1\in K$ 且 $|x_1-x_0|<\delta$，$h(x_1)=0$，$\left|h(x_1)-h(x_0)\right|=\left|h(x_0)\right|<\varepsilon$，由 $\varepsilon$ 的任意性可得 $h(x_0)=0$，$x_0\in K$。

所以 $K$ 是闭集。

<br/>

!!! question "练习 4.3.8"
    (a) 证明如果一个函数在整个 $\mathbb{R}$ 上连续，并且在每个有理点上都等于 0，那么它必须在整个 $\mathbb{R}$ 上恒等于 0。

    (b) 如果 $f$ 和 $g$ 在整个 $\mathbb{R}$ 上定义，并且在每个有理点上都满足 $f\left( r\right)  = g\left( r\right)$ ，那么 $f$ 和 $g$ 必须是同一个函数吗？

(a) 因为任何一个无理数都可以被有理数序列逼近，由连续性可得函数在无理数点上也为 0，所以其在 $\mathbb{R}$ 上恒等于 0。

(b) 不是，如果不连续，它们在无理点上可以随意定义。

连续的情况下则是的。令 $h(x)=f(x)-g(x)$，由 (a) 问可知 $h(x)\equiv 0$，因此 $f(x)\equiv g(x)$，它们是同一个函数。

<br/>

<a id="8"></a>

!!! question "练习 4.3.9 (压缩映射定理)"
    (压缩映射定理)。设 $f$ 是定义在 $\mathbb{R}$ 上的函数，并假设存在常数 $c$ 使得 $0 < c < 1$ 且

    $$
    \left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  c\left| {x - y}\right|
    $$

    对于所有 $x,y \in  \mathbb{R}$ 。

    (a) 证明 $f$ 在 $\mathbb{R}$ 上是连续的。

    (b) 选取某点 ${y}_{1} \in  \mathbb{R}$ 并构造序列

    $$
    \left( {{y}_{1},f\left( {y}_{1}\right) ,f\left( {f\left( {y}_{1}\right) }\right) ,\ldots }\right) \text{ . }
    $$

    一般情况下，如果 ${y}_{n + 1} = f\left( {y}_{n}\right)$ ，证明生成的序列 $\left( {y}_{n}\right)$ 是Cauchy序列。因此我们可以令 $y = \lim {y}_{n}$ 。

    (c) 证明 $y$ 是 $f$ 的不动点(即 $f\left( y\right)  = y$ )，并且在此方面是唯一的。

    最后，证明如果 $x$ 是 $\mathbb{R}$ 中的任意一点，则序列 $\left( {x,f\left( x\right) ,f\left( {f\left( x\right) }\right) ,\ldots }\right)$ 收敛到(b)中定义的 $y$ 。

(a) 对任意的 $x_0\in \mathbb{R}$，对 $\forall\ \varepsilon>0$，令 $\delta=\displaystyle\frac{\varepsilon}{c}$，则对任意 $|x-x_0|<\delta$，$\left|f(x)-f(x_0)\right|\leq c\left|x-x_0\right|<\varepsilon$，所以 $f$ 在 $\mathbb{R}$ 上连续。

(b) 对任意的 $n\in \mathbb{N^+}$，$\left|y_{n+1}-y_{n+2}\right|=|f(y_n)-f(y_{n+1})|\leq c|y_n-y_{n+1}|\leq c^n\left|y_1-y_2\right|$，

因为相邻两项之差之间也有比例关系，所以这里考虑用绝对值不等式拆开来放缩：

$$
\begin{align*}
    |y_m-y_n|&\leq\displaystyle\sum_{j=m}^{n-1}|y_j-y_{j+1}| \\
    &\leq \displaystyle\sum_{j=m}^{n-1}\left(c^{j-1}|y_1-y_2|\right) \\
    &\leq |y_1-y_2|\displaystyle\sum_{j=m}^{n-1}c^{j-1} \\
    &=\displaystyle\frac{|y_1-y_2|c^{m-1}(1-c^{n-m})}{1-c} \\
    &\leq \frac{|y_1-y_2|c^{m-1}}{1-c}\\
\end{align*}
$$

所以对 $\forall\ \varepsilon>0$，$\exists\ N>\displaystyle\frac{\ln\frac{(1-c)\varepsilon}{|y_1-y_2|}}{\ln c}+1$，对 $\forall\ n,m>N$，有 $|y_n-y_m|<\varepsilon$，所以 $\{y_n\}$ 是Cauchy序列。

(c) 由题意，对 $f$ 的不动点 $y$ 有 $\left|y_{n+1}-y\right|\leq c^n|y_1-y_2|$，所以对 $\forall\ \varepsilon>0$，$\exists\ N>\displaystyle\frac{\ln\frac{\varepsilon}{\left|y_1-y_2\right|}}{\ln c}+1$，对 $\forall\ n>N$ 有 $|y_n-y|<\varepsilon$，所以 $\displaystyle\lim_{n\to \infty}y_n=y$。

由极限的唯一性可知 $y$ 是唯一的。

由 (b) 中 $y_1$ 选取的任意性可知对任意 $x\in \mathbb{R}$，序列 $\{x,f(x),f(f(x)),\ldots\}$ 收敛到 $y$。

<br/>

<a id="9"></a>

!!! question "练习 4.3.10"
    设 $f$ 是定义在 $\mathbb{R}$ 上的函数，满足对所有 $x,y \in  \mathbb{R}$ 的加性条件 $f\left( {x + y}\right)  = f\left( x\right)  + f\left( y\right)$ 。

    (a) 证明 $f\left( 0\right)  = 0$ 且对所有 $x \in  \mathbb{R}$ 有 $f\left( {-x}\right)  =  - f\left( x\right)$ 。

    (b) 证明如果 $f$ 在 $x = 0$ 处连续，则 $f$ 在 $\mathbb{R}$ 中的每一点都连续。

    (c) 设 $k = f\left( 1\right)$ 。证明对于所有 $n \in  \mathbb{N}$ ， $f\left( n\right)  = {kn}$ 成立，然后证明对于所有 $z \in  \mathbb{Z}$ ， $f\left( z\right)  = {kz}$ 成立。现在，证明对于任何有理数 $r$ ， $f\left( r\right)  = {kr}$ 成立。

    (d) 使用 (b) 和 (c) 得出结论，对于所有 $x \in  \mathbb{R}$ ， $f\left( x\right)  = {kx}$ 成立。因此，任何在 $x = 0$ 处连续的加性函数必然是通过原点的线性函数。

(a) 令 $x=y=0$ 可得 $f(0)=f(0)+f(0)$，所以 $f(0)=0$。

对 $\forall\ x\in \mathbb{R}$，有 $f(0)=f(x)+f(-x)$，所以 $f(x)=-f(-x)$。

(b) 对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ |x|<\delta$，$|f(x)|<\varepsilon$。
所以对 $\forall\ x_0\in \mathbb{R}$，对上述的 $\varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ |x-x_0|<\delta$，有 $\left|f(x)-f(x_0)\right|=|f(x-x_0)|<\varepsilon$。

所以 $f$ 在 $\mathbb{R}$ 上任一点都连续。

(c) 对 $\forall\ n\in \mathbb{N^+}$，$f(n)=f(n-1)+f(1)=f(n-2)+2f(1)=\cdots=nf(1)=kn$。

对 $\forall\ z\in \mathbb{Z}$，若 $z>0$，$f(z)=kz$；若 $z=0$，$f(z)=0=k0$；若 $z<0$，$f(z)=-f(-z)=-k(-z)=kz$，所以 $f(z)=kz$ 总是成立。

同理可推，对 $\forall\ n\in \mathbb{Z}\setminus \left\{0\right\}$，$f(1)=nf\left(\displaystyle\frac{1}{n}\right)$，$f\left(\displaystyle\frac{1}{n}\right)=\displaystyle\frac{k}{n}$。

所以对任意有理数 $r=\displaystyle\frac{p}{q}$，$f(r)=f\left(\displaystyle\frac{p}{q}\right)=pf\left(\displaystyle\frac{1}{q}\right)=\displaystyle\frac{kp}{q}=kr$。

(d) 对 $\forall\ x_0\in \mathbb{R}$，由有理数的稠密性，总存在有理数序列 $\left\{q_n\right\}\rightarrow x_0$。

因为 $f$ 在 $x_0$ 连续，所以 $f(x_0)=\displaystyle\lim_{n\to \infty}f(q_n)=\displaystyle\lim_{n\to \infty}kq_n=kx_0$。

所以 $f(x)=kx$。

<br/>

!!! question "练习 4.3.11"
    对于以下每个 $A$ 的选择，构造一个函数 $f : \mathbb{R} \rightarrow  \mathbb{R}$ ，该函数在 $A$ 中的每个点 $x$ 处具有不连续性，并且在 ${A}^{c}$ 上连续。

    (a) $A = \mathbb{Z}$ .

    (b) $A = \{ x : 0 < x < 1\}$ .

    (c) $A = \{ x : 0 \leq  x \leq  1\}$ .

    (d) $A = \left\{  {\frac{1}{n} : n \in  \mathbb{N}}\right\}$ .

(a) $f(x)=\begin{cases}1 & \text{if } x\in \mathbb{Z}\\ 0 & \text{if }x\notin \mathbb{Z}\end{cases}$ 。

(b)
$$
f(x)=\begin{cases}
    \displaystyle\frac{1}{2}-\left|x-\displaystyle\frac{1}{2}\right|&\text{if }x\in \mathbb{Q}\cap A\\
    0&\text{if }x\notin \mathbb{Q}\cap A
\end{cases}$$

(c)
$$
f(x)=\begin{cases}
    0&\text{if }x\in A\cap \mathbb{Q}\\
    1&\text{if }x\in A\cap (\mathbb{R}\setminus \mathbb{Q})\\
    0&\text{if }x\notin A
\end{cases}
$$

(d) 
$$
f(x)=\begin{cases}
    x & \text{if }x\in A\\
    0 & \text{if }x\notin A
\end{cases}
$$

<br/>

!!! question "练习 4.3.12"
    设 $C$ 为第 3.1 节中构造的Cantor集(Cantor set)。定义 $g : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}$ 为

    $$
    g\left( x\right)  = \left\{  \begin{array}{ll} 1 & \text{ if }x \in  C \\  0 & \text{ if }x \notin  C. \end{array}\right.
    $$

    (a) 证明 $g$ 在任何点 $c \in  C$ 处都不连续。

    (b) 证明 $g$ 在每个点 $c \notin  C$ 处都连续。

(a) 因为 $C$ 是完全非连通的，所以取 $\varepsilon=1$，对任意 $c\in C$，$\forall\ \delta>0$，$V_\delta(c)$ 中总存在 $x\notin C$，使得 $|g(x)-g(c)|=|0-1|=1\geq \varepsilon$，所以 $g$ 在 $c\in C$ 处不连续。

(b) 假设存在 $c_0 \notin C$ 使得 $g$ 在 $c_0$ 处不连续，则对任意 $\delta_n=\displaystyle\frac{1}{n}$，总存在 $x_n\in C$，$x_n\in V_{\delta_{n}}(c_0)$。这样就得到了一个序列 $\left\{x_n\right\}\rightarrow c_0$。因为 $C$ 是闭集，所以 $c_0\in C$，与假设矛盾。所以 $g$ 在每个 $c\notin C$ 处均连续。

---

## 习题 4.4 紧集上的连续函数

!!! question 练习 4.4.1
    (a) 证明 $f(x) = x^3$ 在整个 $\mathbb{R}$ 上连续。
    (b) 利用定理 4.4.5 论证 $f$ 在 $\mathbb{R}$ 上不是一致连续的。
    (c) 证明 $f$ 在 $\mathbb{R}$ 的任何有界子集上是一致连续的。

(a) 对 $\forall\ x_0\in \mathbb{R}$，$\forall\ \varepsilon>0$：

i. 若 $x_0=0$，则取 $\delta=\sqrt[3]{\varepsilon}$，当 $|x-0|<\delta$ 时，有 $|f(x)-f(0)|=|x^3-0|=|x|^3<\delta^3=\varepsilon$。

ii. 若 $x_0 \neq 0$，则令 $\delta<|x_0|$，那么 $\left|x-x_0\right|<\delta$ 可得 $x\cdot x_0>0$ 且 $|x|<2|x_0|$，再令 $\delta=\min\left\{\displaystyle\frac{\left|x_0\right|}{2}, \displaystyle\frac{\varepsilon}{7|x_0|^2}\right\}$ 可得

$$
\left|f(x)-f(x_0)\right|=\left|(x-x_0)(x^2+xx_0+x_0^2)\right|<\displaystyle\frac{\varepsilon}{7|x_0|^2}\cdot 7|x_0|^2=\varepsilon.
$$

所以 $f(x)=x^3$ 在整个 $\mathbb{R}$ 上连续。

(b) 令 $x_n=n+\displaystyle\frac{1}{n}$，$y_n=n-\displaystyle\frac{1}{n}$，则 $\displaystyle\lim_{n\to \infty}\left|x_n-y_n\right|=0$，但 $\left|f(x_n)-f(y_n)\right|=6n+\displaystyle\frac{2}{n^3}>1$，所以 $f$ 在 $\mathbb{R}$ 上不是一致连续的。

(c) 设 $A\subseteq \mathbb{R}$ 是有界集，则存在 $M>0$ 使得 $\forall\ x\in A$，$|x|<M$。对于 $\forall\ \varepsilon>0$，令 $\delta=\displaystyle\frac{\varepsilon}{3M^2}$，则对任意 $\left|x-y\right|<\delta$，
$$
\left|f(x)-f(y)\right|\leq \left|x-y\right|\left|x^2+xy+y^2\right|<\displaystyle\frac{\varepsilon}{3M^2}\cdot 3M^2=\varepsilon.
$$

所以 $f$ 在 $\mathbb{R}$ 的任何有界子集上是一致连续的。

<br/>

!!! question 练习 4.4.2
    (a) $f(x) = 1/x$ 在 $(0, 1)$ 上是一致连续的吗？
    (b) $g(x) = \sqrt{x^2 + 1}$ 在 $(0, 1)$ 上是一致连续的吗？
    (c) $h(x) = x \sin(1/x)$ 在 $(0, 1)$ 上是一致连续的吗？

(a) 不是。令 $x_n=\displaystyle\frac{1}{n}$，$y_n=\displaystyle\frac{1}{n+1}$，则 $\left|x_n-y_n\right|\rightarrow 0$，但 $\left|f(x_n)-f(y_n)\right|=1$。

(b) 是的。令 $\delta=\varepsilon$，则对 $\forall\ x,y\in (0,1)$ 且 $|x-y|<\delta$ 有

$$
\begin{align*}
    \left|g(x)-g(y)\right|&=\left|\sqrt{x^2+1}-\sqrt[]{y^2+1}\right|=\displaystyle\frac{\left|x^2-y^2\right|}{\sqrt[]{x^2+1}+\sqrt[]{y^2+1}}<\displaystyle\frac{\left|x-y\right|\left|x+y\right|}{2}\\
    &<\displaystyle\frac{\left|x-y\right|\cdot 2}{2}=\left|x-y\right|<\varepsilon.
\end{align*}
$$

(c) <a id="11">拓宽定义域来证明一致连续性</a>

令 $h_1(x)=\begin{cases} x\sin(1/x), & x\in (0,1]\\0, & x=0\end{cases}$

因为 $|x\sin(1/x)|\leq |x|$，由夹逼准则知 $\displaystyle\lim_{x\to \infty}h_1(x)=0$，所以 $h_1(x)$ 在 $[0,1]$ 上连续，由紧集上连续函数的性质可知 $h_1(x)$ 在 $[0,1]$ 上一致连续 $\Rightarrow$ $h_1(x)$ 在 $(0,1)$ 上一致连续。

又因为在 $(0,1)$ 上，$h(x)=h_1(x)$，所以 $h(x)$ 在 $(0,1)$ 上一致连续。

<br/>

!!! question 练习 4.4.3
    证明 $f(x) = 1/x^2$ 在集合 $[1, \infty)$ 上是一致连续的，但在集合 $(0, 1]$ 上不是。

$x\in [1,+\infty)$ 时，$f(x)\leq 1$，所以对 $\forall\ \varepsilon>0$，令 $\delta=\displaystyle\frac{\varepsilon}{2}$，则对任意的 $x,y\in [1,+\infty)$，$|x-y|<\delta$，

$$
\left|f(x)-f(y)\right|=\displaystyle\frac{|x-y||x+y|}{x^2y^2}\leq |x-y|\cdot |\displaystyle\frac{1}{xy^2}+\displaystyle\frac{1}{x^2y}|<\displaystyle\frac{\varepsilon}{2}\cdot 2=\varepsilon.
$$

所以 $f(x)=1/x^2$ 在 $[1, \infty)$ 上是一致连续的。

当 $x_n=\displaystyle\frac{1}{n}$，$y_n=\displaystyle\frac{1}{n+1}$ 时，$\left|x_n-y_n\right|\rightarrow 0$，但 $\left|f(x_n)-f(y_n)\right|=2n+1>1$，所以 $f(x)=1/x^2$ 在 $(0, 1]$ 上不是一致连续的。

<br/>

!!! question 练习 4.4.4
    判断下列每个陈述是真还是假，并证明你的结论。
    (a) 如果 $f$ 在 $[a, b]$ 上连续，且对于所有 $a \le x \le b$ 都有 $f(x) > 0$，则 $1/f$ 在 $[a, b]$ 上有界（意味着 $1/f$ 的值域有界）。
    (b) 如果 $f$ 在有界集 $A$ 上是一致连续的，则 $f(A)$ 是有界的。
    (c) 如果 $f$ 定义在 $\mathbb{R}$ 上，且只要 $K$ 是紧集 $f(K)$ 就是紧集，则 $f$ 在 $\mathbb{R}$ 上连续。

(a) 正确。由极值定理，$x_0\in [a,b]$ 使得对任意 $x\in [a,b]$ 有 $f(x_0)\leq f(x)$，且 $f(x_0)>0$，所以对任意 $x\in [a,b]$，$0<\displaystyle\frac{1}{f(x)}\leq \displaystyle\frac{1}{f(x_0)}$，即 $1/f$ 在 $[a,b]$ 上有界。

(b) 正确。$A$ 为有限集的情况下 $f(x)$ 显然是有界的。
对 $A$ 为无限集的情况使用反证法。假设 $f(A)$ 是无界的，则一定存在序列 $\left\{x_n\right\}\subseteq A$ 满足对 $\forall\ n\in \mathbb{N^+}$，$n<f(x_n)<f(x_{n+1})$。因为 $A$ 有界，所以 $\left\{x_n\right\}$ 也有界。由 Bolzano-Weierstrass 定理可知其有收敛子列 $\left\{x_{k_n}\right\}$。设 $\displaystyle\lim_{n\to \infty}x_{k_n}=x_0$, 则 $x_0$ 为 $A$ 的极限点。若 $x_0\in A$，则 $f(x_0)=\displaystyle\lim_{n\to \infty}f(x_{k_n})$，但 $f(x_{k_n})$ 是发散的，所以矛盾。

若 $x_0\notin A$，由一致连续性可知对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，当 $\left|x-y\right|<\delta$ 时，有 $\left|f(x)-f(y)\right|<\varepsilon$。对上述的 $\delta>0$，因为 $\displaystyle\lim_{n\to \infty}x_{k_n}=x_0$，所以存在 $N\in \mathbb{N^+}$，对任意的 $n>N$，有 $\left|x_{k_n}-x_0\right|<\displaystyle\frac{\delta}{2}$。因此对任意的 $m,n>N$，有 $\left|x_{k_n}-x_{k_m}\right|\leq |x_{k_n}-x_0|+|x_{k_m}-x_0|<\delta$，从而 $\left|f(x_{k_n})-f(x_{k_m})\right|<\varepsilon$，由 Cauchy 收敛准则可知 $\left\{f(x_{k_n})\right\}$ 是收敛的，这与 $f(x_{k_n})$ 发散矛盾。

综上，$f(A)$ 是有界的。

(c) 错误。考虑 Dirichlet 函数 $D(x)$，对任意集合 $A$，$D(A)$ 只可能是 $\varnothing,\left\{0\right\},\left\{1\right\},\left\{0,1\right\}$，均是紧集，但 $D(x)$ 在 $\mathbb{R}$ 上不连续。

<br/>

<a id="12"></a>

!!! question 练习 4.4.5
    假设 $g$ 定义在开区间 $(a, c)$ 上，并且已知它在 $(a, b]$ 和 $[b, c)$ 上是一致连续的，其中 $a < b < c$。证明 $g$ 在 $(a, c)$ 上是一致连续的。

因为 $g$ 在 $\left(a,b\right]$，$[b,c)$ 上都一致连续，所以对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，对 $\forall\ x,y\in (a,b]$，$|x-y|<\delta_1$ 有 $\left|g(x)-g(y)\right|<\varepsilon$，对 $\forall\ x,y\in [b,c)$，$|x-y|<\delta_2$ 有 $\left|g(x)-g(y)\right|<\varepsilon$。

令 $\delta=\min\left\{\delta_1,\delta_2\right\}$，则对 $\forall\ x,y\in (a,c)$，$|x-y|<\delta$，当 $x,y\in (a,b]$ 或 $x,y\in [b,c)$ 时，都有 $\left|g(x)-g(y)\right|<\varepsilon$；当 $x\in (a,b]$，$y\in [b,c)$ 时，$\left|g(x)-g(y)\right|\leq \left|g(x)-g(b)\right|+\left|g(y)-g(b)\right|<2\varepsilon$。

所以 $g$ 在 $(a,c)$ 上一致连续。

<br/>

!!! question 练习 4.4.6
    给出下列每种情况的例子，或者说明这种要求是不可能的。对于任何不可能的情况，提供一个简短的解释说明原因。
    (a) 一个连续函数 $f : (0, 1) \to \mathbb{R}$ 和一个柯西序列 $(x_n)$，使得 $f(x_n)$ 不是柯西序列；
    (b) 一个一致连续函数 $f : (0, 1) \to \mathbb{R}$ 和一个柯西序列 $(x_n)$，使得 $f(x_n)$ 不是柯西序列；
    (c) 一个连续函数 $f : [0, \infty) \to \mathbb{R}$ 和一个柯西序列 $(x_n)$，使得 $f(x_n)$ 不是柯西序列。

(a) 令 $f(x)=1/x$，$x_n=1/n$，则 $f(x_n)=n$ 不是柯西序列。

(b) 这是不可能的。若 $f$ 在 $(0,1)$ 上一致连续，则对 $\forall\ \varepsilon>0$，$\forall\ \delta>0$，对 $\forall\ \left|x-y\right|<\delta$，$\left|f(x)-f(y)\right|<\varepsilon$。现在，若 $\left\{x_n\right\}$ 是柯西序列，则对上述的 $\delta>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ m,n>N$，$\left|x_m-x_n\right|<\delta\Rightarrow \left|f(x_m)-f(x_n)\right|<\varepsilon$，这说明 $f(x_n)$ 也是柯西序列。

(c) 这是不可能的。因为 $[0,+\infty)$ 是闭集，所以 $\left\{x_n\right\}$ 的极限 $x_0\in [0,+\infty)$，由连续函数的性质可得 $\displaystyle\lim_{n\to \infty}f(x_n)=f(x_0)$，所以 $f(x_n)$ 是柯西序列。

<br/>

!!! question 练习 4.4.7
    证明 $f(x) = \sqrt{x}$ 在 $[0, \infty)$ 上是一致连续的。

$\left|\sqrt[]{x}-\sqrt[]{y}\right|=\displaystyle\frac{|x-y|}{\sqrt[]{x}+\sqrt[]{y}}$ 的分母在 $x,y$ 靠近 $0$ 时难以估计，但考虑到它们靠近 $0$ 时本身已足够小，故采用绝对值不等式对原式直接进行放缩。

对 $\forall\ \varepsilon>0$，$\exists\ \delta<\varepsilon^2$。则对 $\forall\ x,y\in \left[0,\displaystyle\frac{\varepsilon^2}{4}\right]$，$\left|\sqrt[]{x}-\sqrt[]{y}\right|\leq \sqrt[]{x}+\sqrt[]{y}\leq \varepsilon$。所以 $f$ 在 $\left[0,\displaystyle\frac{\varepsilon^2}{4}\right]$ 上一致连续。

同理，对 $\forall\ x,y\in \left[\displaystyle\frac{\varepsilon^2}{4},+\infty\right)$，$\left|\sqrt[]{x}-\sqrt[]{y}\right|=\displaystyle\frac{\left|x-y\right|}{\sqrt[]{x}+\sqrt[]{y}}\leq \displaystyle\frac{\left|x-y\right|}{\varepsilon}<\varepsilon$，所以 $f$ 在 $\left[\displaystyle\frac{\varepsilon^2}{4},+\infty\right)$ 上一致连续。

由 [4.4.5](#12)，$f$ 在 $[0,+\infty)$ 上一致连续。

<br/>

!!! question 练习 4.4.8
    给出下列每种情况的例子，或者提供一个简短的论证说明为什么该要求是不可能的。
    (a) 定义在 $[0, 1]$ 上的连续函数，其值域为 $(0, 1)$。
    (b) 定义在 $(0, 1)$ 上的连续函数，其值域为 $[0, 1]$。
    (c) 定义在 $(0, 1]$ 上的连续函数，其值域为 $(0, 1)$。

(a) 不可能。若其值域为 $(0,1)$，则必存在序列 $\left\{x_n\right\}\rightarrow x_0\in [0,1]$ 使得 $\left\{f(x_n)\right\}\rightarrow 1=f(x_0)$，$0$ 同理。即 $0,1$ 在 $f(x)$ 值域中。

(b) 可能。例如 $f(x)=|\sin\left(2\pi x\right)|$。

(c) 可能。关键是存在两个序列 $\left\{x_n\right\},\left\{y_n\right\}$ 均趋于 $0$，使得 $f(x_n)\rightarrow 0$，$f(y_n)\rightarrow 1$，这说明 $\displaystyle\lim_{x\to 0}f(x)$ 是不存在的。

令 $f(x)=\displaystyle\frac{1}{2}\left((1-x)\sin\displaystyle\frac{1}{x}+1\right)$。对于 $(1-x)\sin\displaystyle\frac{1}{x}$ 这部分，其在 $x\in (0,1]$ 的时候始终在 $(-1,1)$ 之间，于是 $f(x)$ 的值域一定在 $(0,1)$ 内部。其次，令 $x_n=\displaystyle\frac{1}{2\pi n-\displaystyle\frac{\pi}{2}}$，$y_n=\displaystyle\frac{1}{2\pi n+\displaystyle\frac{\pi}{2}}$ 可以满足我们之前提出的要求。由 $(0,1]$ 上的连续性，$f(x)$ 可以取遍 $0,1$ 间的所有数，所以 $f$ 的值域为 $(0,1)$。

<br/>

<a id="13"></a>

!!! question 练习 4.4.9 (利普希茨函数)
    一个函数 $f : A \to \mathbb{R}$ 被称为利普希茨（Lipschitz）函数，如果存在一个界 $M > 0$ 使得
    $$ \left| \frac{f(x) - f(y)}{x - y} \right| \le M $$
    对于所有 $x \ne y \in A$ 成立。从几何上讲，如果函数 $f$ 图像上任意两点连线的斜率大小有一个一致的界，则称该函数为利普希茨函数。
    (a) 证明如果 $f : A \to \mathbb{R}$ 是利普希茨函数，那么它在 $A$ 上是一致连续的。
    (b) 逆命题成立吗？所有一致连续函数都必然是利普希茨函数吗？

(a) 对 $\forall\ \varepsilon>0$，令 $\delta=\displaystyle\frac{\varepsilon}{M}$，则对 $\forall\ x,y\in A$，$|x-y|<\delta$ 有 $\left|f(x)-f(y)\right|\leq M\left|x-y\right|<\varepsilon$，所以 $f$ 是一致连续的。

(b) 逆命题不成立。考虑构造一个斜率无界的一致连续函数，例如 $h(x)=x\sin \displaystyle\frac{1}{x}$，其在 $(0,1)$ 上一致连续，但考虑 $x_n=\displaystyle\frac{1}{2\pi n+\displaystyle\frac{\pi}{2}}$，$y_n=\displaystyle\frac{1}{2\pi n-\displaystyle\frac{\pi}{2}}$，则 $\left|\displaystyle\frac{f(x_n)-f(y_n)}{x_n-y_n}\right|=4n$，当 $n$ 增大时可以任意大，所以 $h(x)$ 不是利普希茨函数。

<br/>

!!! question 练习 4.4.10
    假设 $f$ 和 $g$ 是定义在公共定义域 $A$ 上的一致连续函数。下列哪些组合在 $A$ 上必然是一致连续的：
    $$ f(x) + g(x), \quad \frac{f(x)}{g(x)}, \quad f(x)g(x), \quad f(g(x))? $$
    （假设商和复合是定义良好的，因此至少是连续的。）

我们知道这些函数都是连续的，而证明它们一致连续的过程和证明它们连续的过程类似，下面进行讨论。

对于加法，对 $\forall\ \varepsilon>0$，$\exists\ \delta_1,\delta_2>0$，当 $\left|x-y\right|<\delta_1$ 时，有 $\left|f(x)-f(y)\right|<\displaystyle\frac{\varepsilon}{2}$，当 $\left|x-y\right|<\delta_2$ 时，有 $\left|g(x)-g(y)\right|<\displaystyle\frac{\varepsilon}{2}$。令 $\delta=\min\left\{\delta_1,\delta_2\right\}$，则当 $\left|x-y\right|<\delta$ 时，有

$$
\left|(f(x)+g(x))-(f(y)+g(y))\right|\leq \left|f(x)-f(y)\right|+\left|g(x)-g(y)\right|<\varepsilon.
$$

所以 $f(x)+g(x)$ 在 $A$ 上一致连续。

但在乘法上的情况则有区别。用与连续性证明同样的化简方式，可以得到 $\left|f(x)g(x)-f(y)g(y)\right|\leq\left|f(x)\right|\left|g(x)-g(y)\right|+\left|g(y)\right|\left|f(x)-f(y)\right|<\left(\left|f(x)\right|+\left|g(y)\right|\right)\varepsilon$。但与连续性证明不同的是，连续性证明中的 $f(x),f(y),g(x),g(y)$ 都是有界的（一个是常数，另一个被 $\delta$ 锁在了常数附近），而这里则不一定。事实上，若它们会任意大，则乘积很可能是不一致连续的。

例如 $f(x)=g(x)=x$，则 $f(x)g(x)=x^2$ 在 $\mathbb{R}$ 上不一致连续。

除法上的情况同理，令 $f(x)=\sqrt[]{x}$，$g(x)=x$，则 $f(x)/g(x)=\displaystyle\frac{1}{\sqrt[]{x}}$ 在 $(0,1)$ 上不一致连续。

最后考虑复合函数。对 $\forall\ \varepsilon>0$，$\exists\ \delta_1>0$，当 $\left|u-v\right|<\delta_1$ 时，有 $\left|f(u)-f(v)\right|<\varepsilon$。对上述 $\delta_1>0$，$\exists\ \delta_2>0$，当 $\left|x-y\right|<\delta_2$ 时，有 $\left|g(x)-g(y)\right|<\delta_1$，所以有 $\left|f(g(x))-f(g(y))\right|<\varepsilon$，所以 $f(g(x))$ 在 $A$ 上一致连续。

<br/>

<a id="14"></a>

!!! question 练习 4.4.11 (连续性的拓扑特征)
    设 $g$ 定义在整个 $\mathbb{R}$ 上。如果 $B$ 是 $\mathbb{R}$ 的子集，定义集合 $g^{-1}(B)$ 为
    $$ g^{-1}(B) = \{x \in \mathbb{R} : g(x) \in B\}. $$
    证明 $g$ 是连续的当且仅当对于任何开集 $O \subseteq \mathbb{R}$，$g^{-1}(O)$ 也是开集。

$\Rightarrow$ 设 $g(x)$ 在 $\mathbb{R}$ 上连续，对于任意开集 $O\subseteq\mathbb{R}$，若 $g(x_0)\in O$，则 $x_0\in g^{-1}(O)$，$\exists\ \varepsilon>0$ 使得 $V_\varepsilon(g(x_0))\subseteq O$．由 $g(x)$ 的连续性，$\exists\ \delta>0$，当 $\left|x-x_0\right|<\delta$ 时，有 $\left|g(x)-g(x_0)\right|<\varepsilon$，即 $g(x)\in V_\varepsilon(g(x_0))\subseteq O$，所以 $x\in g^{-1}(O)$。因此，$V_\delta(x_0)\subseteq g^{-1}(O)$。所以 $g^{-1}(O)$ 也是开集。

$\Leftarrow$ 若对任意开集 $O\subseteq \mathbb{R}$，$g^{-1}(O)$ 也是开集，则对 $\forall\ x_0\in g^{-1}(O)$，$\exists\ \delta>0$，$V_\delta(x_0) \subseteq g^{-1}(O)$。不妨令 $O=V_\varepsilon(g(x_0))$，则 $g(x_0)\in O$，所以对 $\forall\ x\in V_\delta(x_0)$，$g(x)\in O=V_\varepsilon(g(x_0))$。所以 $g$ 在 $\mathbb{R}$ 上连续。

<br/>

!!! question 练习 4.4.12
    回顾练习 4.4.11，然后确定关于定义在 $\mathbb{R}$ 上的连续函数的下列陈述中哪些是正确的：
    (a) 只要 $B$ 是有限集，$f^{-1}(B)$ 就是有限集。
    (b) 只要 $K$ 是紧集，$f^{-1}(K)$ 就是紧集。
    (c) 只要 $A$ 是有界集，$f^{-1}(A)$ 就是有界集。
    (d) 只要 $F$ 是闭集，$f^{-1}(F)$ 就是闭集。

(a) 错误。函数可能有多值对应单值，例如 $f(x)=c$，则 $\left\{c\right\}$ 是有限集，但 $f^{-1}(\left\{c\right\})=\mathbb{R}$。

(b) 错误，原因同上。

(c) 错误，原因同上。

(d) 正确。因为闭集的补集是开集，设 $F$ 是闭集，则 $F^c$ 是开集，由 4.4.11 可知 $f^{-1}(F^c)$ 是开集，所以 $\left(f^{-1}(F^c)\right)^c$ 是闭集。而 $x\notin f^{-1}(F^c)\Rightarrow f(x)\notin F^c\Rightarrow f(x)\in F \Rightarrow x\in f^{-1}(F)$，所以 $\left(f^{-1}(F^c)\right)^c=f^{-1}(F)$ 是闭集。
 
<br/>

<a id="15"></a>

!!! question 练习 4.4.13 (连续延拓定理)
    (a) 证明一致连续函数保持柯西序列；即，如果 $f : A \to \mathbb{R}$ 是一致连续的且 $(x_n) \subseteq A$ 是柯西序列，则证明 $f(x_n)$ 是柯西序列。
    (b) 设 $g$ 是开区间 $(a, b)$ 上的连续函数。证明 $g$ 在 $(a, b)$ 上一致连续当且仅当可以在端点处定义值 $g(a)$ 和 $g(b)$，使得延拓后的函数 $g$ 在 $[a, b]$ 上连续。

(a) 若 $f$ 一致连续，则对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ \left|x-y\right|<\delta$，$\left|f(x)-f(y)\right|<\varepsilon$。现在对上述 $\delta>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ m,n>N$，$\left|x_m-x_n\right|<\delta \rightarrow \left|f(x_m)-f(x_n)\right|<\varepsilon$。所以 $f(x_n)$ 是柯西序列。

(b) 这题的核心是：一致连续使得开区间端点的极限存在。

$\Rightarrow$ 若 $g$ 在 $(a,b)$ 上一致连续，则对任意序列 $\left\{x_n\right\}\rightarrow a$，$g(x_n)$ 是柯西序列，即 $\displaystyle\lim_{n\to \infty}g(x_n)$ 存在。所以 $\displaystyle\lim_{x\to a}g(x)$ 存在。同理 $\displaystyle\lim_{x\to b}g(x)$ 存在。定义 $g(a)=\displaystyle\lim_{x\to a}g(x)$，$g(b)=\displaystyle\lim_{x\to b}g(x)$，则 $g$ 在 $[a,b]$ 上连续。

$\Leftarrow$ 若可定义 $g(a),g(b)$ 使得 $g$ 在 $[a,b]$ 上连续，则由紧集上连续函数的性质可知 $g$ 在 $[a,b]$ 上一致连续，所以 $g$ 在 $(a,b)$ 上一致连续。

<br/>

!!! question 练习 4.4.14
    利用海涅-博雷尔定理（定理 3.3.8 (iii)）中紧性的开覆盖特征，构造定理 4.4.7 的另一种证明。

设 $f$ 是定义在紧集 $K$ 上的连续函数。则对 $\forall\ x\in K$，$\forall\ \varepsilon>0$，$\exists\ \delta_x>0$，对 $\forall\ \left|y-x\right|<\delta_x$，$\left|f(y)-f(x)\right|<\varepsilon$。

现在的想法是，从这些 $\delta_x$ 中找到一个最小的 $\delta_x$，使之满足所有选取的 $x\in K$，用有限覆盖定理来实现这一点。

考虑 $K$ 的开覆盖 $\left\{V_{\delta_x}(x) : x\in K\right\}$，由有限覆盖定理，存在 $x_1,x_2,\cdots,x_n\in K$，使得 $K\subseteq \displaystyle\bigcup_{i=1}^n V_{\delta_{x_i}}(x_i)$。令 $\delta=\min\left\{\delta_{x_1},\delta_{x_2},\ldots,\delta_{x_n}\right\}$。

从而对 $\forall\ \left|x-y\right|<\delta$，若 $x,y\in V_{\delta_{x_i}}(x_i)$，则 $\left|f(x)-f(x_i)\right|<\varepsilon$，$\left|f(y)-f(x_i)\right|<\varepsilon$，$\left|f(x)-f(y)\right|\leq \left|f(x)-f(x_i)\right|+\left|f(y)-f(x_i)\right|<2\varepsilon$。所以 $f$ 在任意的 $V_{\delta_{x_i}}(x_i)$ 上均一致连续。

现在考虑两个相邻区间 $V_{\delta_{x_i}}(x_i),V_{\delta_{x_j}}(x_j)$，因为全体开区间的并覆盖了 $K$，所以 $V_{\delta_{x_i}}(x_i)\cap V_{\delta_{x_j}}(x_j)\neq \varnothing$，设 $z\in V_{\delta_{x_i}}(x_i)\cap V_{\delta_{x_j}}(x_j)$，则可以把 $V_{\delta_{x_i}}(x_i)\cup V_{\delta_{x_j}}(x_j)$ 重新划分为 $(a,z]\cup [z,b)$，其中 $a,b$ 为左右端。因为中间的 $z$ 同属于两个区间，而 $a,b$ 都属于某个开区间，所以 $(a,z]$ 肯定包含于某个 $V_{\delta_{x_m}}(x_m)$，所以 $f$ 在 $(a,z]$ 上一致连续。同理 $f$ 在 $[z,b)$ 上一致连续。由 [4.4.5](#12) 可知 $f$ 在 $(a,b)$ 即 $V_{\delta_{x_i}}(x_i)\cup V_{\delta_{x_j}}(x_j)$ 上一致连续。对所有开区间依次使用这个步骤，就能得到 $f$ 在 $K$ 上一致连续。

综上，在紧集 $K$ 上的连续函数 $f$ 在 $K$ 上一致连续。

【注】其实不需要考虑相邻区间的情况，因为开覆盖区间长度的选取是任意的，所以可以选取足够小的区间长度，让 $x,y$ 与区间端点差值的和小于 $\delta$，从而直接使用一致连续的定义即可。

例如，考虑 $K$ 的开覆盖 $\left\{V_{\frac{\delta_x}{2}}(x) : x\in K\right\}$，之后同理。则对任意的 $\left|x-y\right|<\delta$，若 $x\in V_{\frac{\delta_{x_0}}{2}}(x_0)$，则 $\left|x-x_0\right|<\displaystyle\frac{\delta_{x_0}}{2}$，$\left|y-x_0\right|\leq\left|y-x\right|+\left|x-x_0\right|<\delta_{x_0}$，所以 $\left|f(x)-f(y)\right|\leq \left|f(x)-f(x_0)\right|+\left|f(y)-f(x_0)\right|<2\varepsilon$，由此证得一致连续性。

---

## 习题 4.5 介值定理

!!! question "练习 4.5.1"
    说明介值定理如何作为定理 4.5.2 的推论得出。

因为 $[a,b]$ 是连通的，所以 $f([a,b])$ 也是连通的。所以对任意 $f(a)<L<f(b)$，$\exists\ c\in [a,b]$ 使得 $f(c)=L$。

<br/>

!!! question "练习 4.5.2"
    提供以下每一项的例子，或者解释为什么该要求是不可能的：
    
    (a) 定义在开区间上的连续函数，其值域等于闭区间。
    (b) 定义在闭区间上的连续函数，其值域等于开区间。
    (c) 定义在开区间上的连续函数，其值域等于不同于 $\mathbb{R}$ 的无界闭集。
    (d) 定义在整个 $\mathbb{R}$ 上的连续函数，其值域等于 $\mathbb{Q}$。

(a) 可以的。考虑一个最值都不在端点上的连续函数即可，比如说定义在 $(0,1)$ 上的 $f(x)=\displaystyle\frac{1}{2}\left(\sin\displaystyle\frac{1}{x}+1\right)$，值域为 $[0,1]$。
(b) 不可能。闭区间是紧集，连续函数将紧集映射为紧集，而开区间不是紧集。
(c) 可以的。例如：$f(x)=\begin{cases}    \displaystyle\frac{1}{x},\quad 0<x\leq 1\\    x,\quad x>1\end{cases}$，其值域为 $[1,+\infty)$。    
(d) 不可能。$\mathbb{R}$ 是连通集，而 $\mathbb{Q}$ 不是连通集。

<br/>

!!! question "练习 4.5.3"
    如果对于 $A$ 中的所有 $x < y$ 都有 $f(x) \le f(y)$，则称函数 $f$ 在 $A$ 上是递增的。证明如果 $f$ 在 $[a, b]$ 上是递增的并且满足介值性质 (定义 4.5.3)，那么 $f$ 在 $[a, b]$ 上是连续的。

对 $\forall\ x_0\in [a,b]$：

若 $x_0\in (a,b)$，则 $f(a)\leq f(x_0)\leq f(b)$，对 $\forall\ \varepsilon>0$，由介值性，$\exists\ \delta>0$，使得 $V_\delta(x_0)\subseteq [a,b]$ 且 $f(x_0-\delta)>f(x_0)-\varepsilon$， $f(x_0+\delta)<f(x_0)+\varepsilon$。又由单调性，对 $\forall\ x\in V_\delta(x_0)$，$|f(x)-f(x_0)|<\varepsilon$，所以 $f$ 在 $x_0$ 处连续。

若 $x_0=a$，则同上，由介值性可得 $f(x_0+\delta)<f(x_0)+\varepsilon$，接下来同理证明。$x_0=b$ 的情况同理。

综上，$f$ 在 $[a,b]$ 上连续。

<br/>

!!! question "练习 4.5.4"
    设 $f$ 是区间 $A$ 上的连续函数，并设 $F$ 是 $f$ 并非一对一的点集；即
    $$ F = \{x \in A : f(x) = f(y) \text{ 对于某个 } y \ne x \text{ 且 } y \in A\}. $$
    证明 $F$ 要么是空的，要么是不可数的。

基本思路是：先找到一组 $f(a)=f(b)$，在 $[a,b]$ 间继续找其他的点。找一个与 $f(a)$ 不同的 $f(x_0)$，这样 $[a,x_0)$ 和 $(x_0,b]$ 中就能分别找到从 $f(x_0)$ 到 $f(a)$ 所有取值的点，而这些点是不可数的。

假设 $F$ 是非空的，则 $\exists\ a,b\in A$，$a<b$ 使得 $f(a)=f(b)$。我们首先有 $[a,b]\subseteq A$。

若对 $\forall\ x\in [a,b]$，$f(x)=f(a)$，则 $[a,b]\subseteq F$，$F$ 不可数。

若 $\exists\ c\in (a,b)$ 使得 $f(c)\neq f(a)$，不妨设 $f(c)<f(a)$。则由介值定理，对 $\forall\ x_1\in [a,c)$，$f(c)<f(x_1)\leq f(a)=f(b)$，总 $\exists\ x_2\in (c,b]$ 使得 $f(x_2)=f(x_1)$。所以 $x_1,x_2\in F$。

同理，对 $\forall\ x\in [a,b]$，$f(c)<f(x)\leq f(a)$ 都有 $x\in F$，而这样的 $x$ 是不可数的（考虑 $f(c)$ 与 $f(a)$ 间的取值有不可数个），所以 $F$ 不可数。

综上，$F$ 要么是空的，要么是不可数的。

<br/>

!!! question "练习 4.5.5"
    (a) 完成前面开始的使用完备性公理的介值定理的证明。
    (b) 完成前面开始的使用嵌套区间性质的介值定理的证明。

我们考虑 $f(a)<f(b)$ 的情形。$f(a)>f(b)$ 的情况可以用类似的方法证明。

要证明的内容是：对 $\forall\ f(a)<L<f(b)$，$\exists\ c\in (a,b)$ 使得 $f(c)=L$。

(a) 令 $A=\left\{x\in [a,b]:f(x)<L\right\}$，则 $a\in A$ 且 $A$ 有上界 $b$，由完备性公理可得 $c=\sup A$ 存在。下证 $f(c)=L$。

由函数连续性，对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对任意 $\left|x-c\right|<\delta$，$\left|f(x)-f(c)\right|<\varepsilon$。

若 $f(c)>L$，取 $\varepsilon=f(c)-L>0$，则对任意的 $\left|x-c\right|<\delta$，$f(x)>L$。因为 $c= \sup A$，所以 $\exists\ x_0>c-\delta$ 使得 $f(x_0)<L$，矛盾。

若 $f(c)<L$，取 $\varepsilon=L-f(c)>0$，则对任意的 $\left|x-c\right|<\delta$，$f(x)<L$。所以 $\exists\ x_0=c+\displaystyle\frac{\delta}{2}>c$，$f(x_0)<L$，这与 $c=\sup A$ 矛盾。

综上，$f(c)=L$。

(b) 令 $a_1=a$，$b_1=b$。

取 $\displaystyle\frac{a+b}{2}$。若 $f\left(\displaystyle\frac{a+b}{2}\right)<L$，则令 $a_2=\displaystyle\frac{a+b}{2}$，$b_2=b$；否则令 $a_2=a$，$b_2=\displaystyle\frac{a+b}{2}$。

取 $\displaystyle\frac{a_2+b_2}{2}$。若 $f\left(\displaystyle\frac{a_2+b_2}{2}\right)<L$，则令 $a_3=\displaystyle\frac{a_2+b_2}{2}$，$b_3=b_2$；否则令 $a_3=a_2$，$b_3=\displaystyle\frac{a_2+b_2}{2}$。

一直操作，我们可以得到闭区间套 $\left\{I_n\right\}=\left\{[a_n,b_n]\right\}$。由闭区间套定理，存在唯一的 $c\in [a_n,b_n]$ 对任意 $n\in \mathbb{N^+}$ 成立。此时 $c=\displaystyle\lim_{n\to \infty}a_n=\displaystyle\lim_{n\to \infty}b_n$。

因为 $f(a_n)<L$，$f(b_n)\geq L$，所以 $\displaystyle\lim_{n\to \infty}(a_n)\leq L$， $\displaystyle\lim_{n\to \infty}(b_n)\geq L$。

由连续函数的性质，$f(c)=\displaystyle\lim_{n\to \infty}f(a_n)=\displaystyle\lim_{n\to \infty}f(b_n)=L$。

<br/>

!!! question "练习 4.5.6"
    设 $f : [0, 1] \to \mathbb{R}$ 是连续的，且 $f(0) = f(1)$。
    
    (a) 证明必然存在 $x, y \in [0, 1]$ 满足 $|x - y| = 1/2$ 且 $f(x) = f(y)$。
    (b) 证明对于每个 $n \in \mathbb{N^+}$，存在 $x_n, y_n \in [0, 1]$ 满足 $|x_n - y_n| = 1/n$ 且 $f(x_n) = f(y_n)$。
    (c) 如果 $h \in (0, 1/2)$ 不是 $1/n$ 的形式，则不一定存在满足 $f(x) = f(y)$ 的 $|x - y| = h$。使用 $h = 2/5$ 提供一个说明这一点的例子。

(a) 令 $g(x)=f(x)-f\left(x+\displaystyle\frac{1}{2}\right)$，则 $g$ 在 $\left[0,\displaystyle\frac{1}{2}\right]$ 上连续，且 $g(0)=f(0)-f\left(\displaystyle\frac{1}{2}\right)$，$g\left(\displaystyle\frac{1}{2}\right)=f\left(\displaystyle\frac{1}{2}\right)-f(1)=-g(0)$。

若 $g(0)=0$，则 $f(0)=f\left(\displaystyle\frac{1}{2}\right)$。

若 $g(0)\neq 0$，则 $g(0)$ 和 $g\left(\displaystyle\frac{1}{2}\right)$ 必然异号，由介值定理，$\exists\ x_0\in \left(0,\displaystyle\frac{1}{2}\right)$ 使得 $g(x_0)=f(x_0)-f\left(x_0+\displaystyle\frac{1}{2}\right)=0$，即 $f(x_0)=f\left(x_0+\displaystyle\frac{1}{2}\right)$。

综上，总能找到 $x,y\in [0,1]$ 使得 $|x-y|=\displaystyle\frac{1}{2}$ 且 $f(x)=f(y)$。

(b) 同上，构造 $g_1(x)=f(x)-f\left(x+\displaystyle\frac{1}{n}\right)$，则同理可得

$$
\begin{align*}
    \displaystyle\sum_{i=0}^{n-1}g_1\left(\displaystyle\frac{i}{n}\right)&=f(0)-f\left(\displaystyle\frac{1}{n}\right)+ f\left(\displaystyle\frac{1}{n}\right)-f\left(\displaystyle\frac{2}{n}\right)+\cdots+f\left(\displaystyle\frac{n-1}{n}\right)-f(1)\\
    &=f(0)-f(1)\\
    &=0
\end{align*}
$$

若存在一个 $i$ 使得 $g_1\left(\displaystyle\frac{i}{n}\right)=f\left(\displaystyle\frac{i}{n}\right)-f\left(\displaystyle\frac{i+1}{n}\right)$=0，则成立。

若不存在上面的 $i$，则必存在 $i_1,i_2\in [0,n-1]$ 使得 $g_1\left(\displaystyle\frac{i_1}{n}\right)g_1\left(\displaystyle\frac{i_2}{n}\right)<0$，由介值定理，$\exists\ x_0\in \left(\displaystyle\frac{i_1}{n},\displaystyle\frac{i_2}{n}\right)$，使得 $g_1(x_0)=0$ 即 $f(x_0)=f\left(x_0+\displaystyle\frac{1}{n}\right)$，从而得证。

综上，对 $\forall\ n\in \mathbb{N^+}$，都能找到 $x_n,y_n\in [0,1]$ 使得 $|x_n-y_n|=\displaystyle\frac{1}{n}$ 且 $f(x_n)=f(y_n)$。

(c) 对这一论断的初步理解是，不形如 $\displaystyle\frac{1}{n}$ 的长度可能无法完全分割原区间，从而产生遗漏情况。这个时候 $g_2(x)=f(x)-f\left(x+\displaystyle\frac{2}{5}\right)$ 就不是先前那样用上一段的结束点和下一段的开始点作比较了，这样就无法用 $f(0)=f(1)$ 来控制大小，从而 $g_2(x)=0$ 的解可能不存在。

我们不妨看看能不能构造 $g_2(x)$ 恒大于 $0$ 的情况。

如果 $g_2(x)>0$，则 $f(0)>f\left(\displaystyle\frac{2}{5}\right)$，$f\left(\displaystyle\frac{3}{5}\right)>f(1)=f(0)$，函数不能是单调的。如果 $f$ 的趋势是 $0$ 减到 $\displaystyle\frac{2}{5}$ 增到 $\displaystyle\frac{3}{5}$ 减到 $1$，那可能有矛盾，因为 $f\left(\displaystyle\frac{1}{5}\right)>f\left(\displaystyle\frac{3}{5}\right)$，当然还有 $f\left(\displaystyle\frac{2}{5}\right)>f\left(\displaystyle\frac{4}{5}\right)$。所以这个连续函数的图像大致如下：

![alt text](https://img-cdn.lusyoe.com/images/HuangTianye/2026/01/11/21b9uzbow8.png)

可以看到，因为 $\displaystyle\frac{2}{5}$ 长度的区间分割无法完全无重复覆盖整个定义域，所以这为中间锯齿状的波动提供了可能。

（一个小细节是我把每两个对应段的斜率都设置成相同的了，这样就能保证前面始终大于后面，甚至 $g_2(x)$ 还是一个定值。）

<br/>

!!! question "练习 4.5.7"
    设 $f$ 是闭区间 $[0, 1]$ 上的连续函数，其值域也包含在 $[0, 1]$ 中。证明 $f$ 必须有一个不动点；即，证明对于至少一个 $x \in [0, 1]$ 值，有 $f(x) = x$。

令 $g(x)=f(x)-x$，则 $g$ 在 $[0,1]$ 上连续，且 $g(0)=f(0)-0\geq 0$，$g(1)=f(1)-1\leq 0$。

若 $g(0)=0$ 或 $g(1)=0$，则成立。

若 $g(0)>0$ 且 $g(1)<0$，则由介值定理，$\exists\ c\in (0,1)$ 使得 $g(c)=0$，即 $f(c)=c$。

综上，至少有一个 $x\in [0,1]$ 使得 $f(x)=x$。

<br/>

!!! question "练习 4.5.8" <a id="4.5.8"></a>
    **[反函数]** 如果函数 $f : A \to \mathbb{R}$ 是一对一的，那么我们可以以自然的方式在 $f$ 的值域上定义反函数 $f^{-1}$：$f^{-1}(y) = x$ 其中 $y = f(x)$。
    
    证明如果 $f$ 在区间 $[a, b]$ 上是连续且一对一的，那么 $f^{-1}$ 也是连续的。

我的第一想法是这样的：因为 $[a,b]$ 是紧集，所以 $f$ 在 $[a,b]$ 上是一致连续的。那么对 $\forall\ |x-y|<\delta$ 就能有 $\left|f(x)-f(y)\right|<\varepsilon$。现在考虑一个问题，这两个式子的顺序能不能反过来？

如果只有连续是不行的，有可能两个相距很远的自变量得到的函数值会相近，但一对一的情况则可以限制（实际上也只有一对一才能产生反函数）。

根据这一点我们来写出证明。假设 $\exists\ \delta>0$，对 $\forall\ \varepsilon>0$，总存在 $x,y$，使得 $\left|f(x)-f(y)\right|<\varepsilon$ 但是 $|x-y|\geq \delta$。

对 $\forall\ n\in \mathbb{N^+}$，分别令 $\varepsilon_n=\displaystyle\frac{1}{n}$，则存在对应的 $x_n,y_n$，满足上述情况。

之后的证明和前面一致连续性定理的证明类似。由 Bolzano-Weierstrass 定理，$\left\{x_n\right\},\left\{y_n\right\}$ 分别有收敛子列 $\left\{x_{n_k}\right\},\left\{y_{n_k}\right\}$，设其极限分别为 $x_0,y_0$。那么我们可以得出 $f(x_0)=f(y_0)$ 但是 $x_0\neq y_0$，这与 $f$ 一对一矛盾。

所以 上述的假设不成立。即对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，当 $\left|f(x)-f(y)\right|<\delta$ 时，$|x-y|<\varepsilon$。

这样就证明了 $f^{-1}$ 是一致连续的，自然就是连续的了。

---

## 习题 4.6 不连续点集

这一节习题在探讨一个函数的不连续点集满足什么样的性质。我们的结论是：单调函数的不连续点集必须由有限或可数个跳跃间断点组成；任意函数的不连续点集都可以表示成闭集的可数并集。

!!! question "练习 4.6.1"
    使用这些函数的修改，构造一个函数 $f : \mathbb{R} \rightarrow  \mathbb{R}$ ，使得

    (a) ${D}_{f} = \mathbb{Z}$ .

    (b) ${D}_{f} = \{ x : 0 < x \leq  1\}$ .

(a) 在整数上构造间断点。

$$
f(x)=\begin{cases}
    0,\quad \text{if }x\notin \mathbb{Z}\\
    1,\quad \text{if }x\in \mathbb{Z}
\end{cases}
$$

(b) 在 $(0,1]$ 上使用 Dirichlet 函数的变体。

$$
f(x)=\begin{cases}
    0,\quad \text{if }x\notin (0,1]\\
    x,\quad \text{if }x\in (0,1]\cap \mathbb{Q}\\
    0,\quad \text{if }x\in (0,1]\setminus \mathbb{Q}
\end{cases}
$$

<br/>

!!! question "练习 4.6.4"
    设 $f : \mathbb{R} \rightarrow  \mathbb{R}$ 为递增函数。证明 $\mathop{\lim }\limits_{{x \rightarrow  {c}^{ + }}}f\left( x\right)$ 和 $\mathop{\lim }\limits_{{x \rightarrow  {c}^{ - }}}f\left( x\right)$ 必须在每个点 $c \in  \mathbb{R}$ 处存在。论证单调函数唯一可能具有的不连续性类型是跳跃不连续性。

对任意的 $c\in \mathbb{R}$，令 $E=\left\{f(x):x>c\right\}$，则由 $f$ 单调递增，对 $\forall\ f(x)\in E$，$f(x)\geq f(c)$。这说明 $E$ 非空有下界。由完备性公理，$\inf E$ 存在，记为 $L$，下证 $L=\displaystyle\lim_{x\to c^+}f(x)$。

因为 $L=\inf E$，所以对 $\forall\ \varepsilon>0$，存在 $f(x_0)\in E$，使得 $L\leq f(x_0)<L+\varepsilon$。由 $f$ 单调递增，令 $\delta=x_0-c>0$，则对 $\forall\ 0<x-c<\delta$，$0\leq f(x)-L<\varepsilon$，所以 $\displaystyle\lim_{x\to c^+}f(x)=L$，即 $\displaystyle\lim_{x\to c^+}f(x)$ 存在。

同理可得 $\displaystyle\lim_{x\to c^-}f(x)$ 存在。所以单调函数唯一可能具有的不连续类型是跳跃不连续性。

<br/>

!!! question "练习 4.6.5"
    构造一个单调函数 $f$ 的跳跃间断点集与 $\mathbb{Q}$ 的一个子集之间的双射。得出结论:单调函数 $f$ 的 ${D}_{f}$ 必须是有限的或可数的，但不能是不可数的。

由 $f$ 的单调性，对任意一个间断点 $c$，都有 $\displaystyle\lim_{x\to c^-}f(x)<\displaystyle\lim_{x\to c^+}f(x)$，所以可以找到一个有理数 $c_1\in (\displaystyle\lim_{x\to c^-}f(x),\displaystyle\lim_{x\to c^+}f(x))$。 又因为单调性，所以对 $\forall\ x< c$，$f(x)\leq \displaystyle\lim_{x\to c^-}f(x)<c_1$，$x>c$ 的情况同理。所以这样就可以构建从 $c$ 到 $c_1$ 一一对应的映射即双射。因为有理数集是可数的，所以 $D_f$ 必然是有限的或可数的。

<br/>

!!! question "练习 4.6.6"
    证明在每种情况下，我们得到一个 ${F}_{\sigma }$ 集作为每个函数的不连续点集。

$\mathbb{R}$ 本身是一个闭集，所以它是一个 ${F}_{\sigma }$ 集。

$\mathbb{R}\setminus\left\{0\right\}=\displaystyle\bigcup_{n=1}^{\infty}\left((-\infty,\displaystyle-\frac{1}{n}]\cup[\displaystyle\frac{1}{n},+\infty)\right)$，所以它是一个 ${F}_{\sigma }$ 集。

$\mathbb{Q}=\displaystyle\bigcup_{n=1}^\infty\left\{q_n\right\}$，其中 $\left\{q_n\right\}$ 是有理数的某个排列，所以它是一个 ${F}_{\sigma }$ 集。

$\mathbb{Z}$ 是全体整数的并集，自然也是 $F_\sigma$ 集。

最后，$(0,1]=\displaystyle\bigcup_{n=1}^\infty \left[\frac{1}{n},1\right]$，所以它是一个 ${F}_{\sigma }$ 集。

<br/>

!!! question "练习 4.6.7"
    证明对于固定的 $\alpha  > 0$ ，集合 ${D}_{\alpha }$ 是闭集。

我们需要证明 $D_\alpha$ 的任何极限点 $x_0$ 都在该集合内。

若 $D_\alpha$ 没有极限点，则其只有孤立点，故为闭集。

若 $x_0\in D_\alpha$ 是其极限点，则存在序列 $\left\{x_n\right\}\subseteq D_\alpha$ 满足 $\left\{x_n\right\}\rightarrow x_0$。

则对 $\forall\ \delta>0$，$\exists\ n\in \mathbb{N^+}$ 使得 $x_n\in V_\delta(x_0)$。

因为 $f$ 在 $x_n$ 处不 $\alpha$ - 连续，所以对任意的 $\varepsilon>0$， $\exists\ y,z\in V_\varepsilon(x_n)$ 满足 $\left|f(y)-f(z)\right|\geq \alpha$。

现在令 $\varepsilon<\delta-\left|x_0-x_n\right|$ 以满足 $V_\varepsilon(x_n)\subseteq V_\varepsilon(x_0)$，则 $\exists\ y,z\in V_\varepsilon(x_0)$，$\left|f(y)-f(z)\right|\geq \alpha$。

所以 $f$ 在 $x_0$ 处不 $\alpha$ - 连续，即 $x_0\in D_\alpha$。

综上，$D_\alpha$ 是闭集。

<br/>

!!! question "练习 4.6.8" <a id="4.6.8"></a>
    如果 ${\alpha }_{1} < {\alpha }_{2}$ ，证明 ${D}_{{\alpha }_{2}} \subseteq  {D}_{{\alpha }_{1}}$ 。

对 $\forall\ x\in D_{\alpha_2}$，对任意 $\delta>0$，$\exists\ y,z\in V_\delta(x)$ 使得 $\left|f(y)-f(z)\right|\geq \alpha_2>\alpha_1$，所以 $x\in D_{\alpha_1}$。所以${D}_{{\alpha }_{2}} \subseteq  {D}_{{\alpha }_{1}}$ 。

<br/>

!!! question "练习 4.6.9"
    设 $\alpha  > 0$ 给定。证明如果 $f$ 在 $x$ 处连续，则它在 $x$ 处也是 $\alpha$ -连续的。解释由此如何得出 ${D}_{\alpha } \subseteq  {D}_{f}$ 。

若 $f$ 在 $x$ 处连续，则对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，使得对 $\forall\ y\in V_\delta(x)$，$\left|f(y)-f(x)\right|<\varepsilon$。现在取 $\varepsilon=\displaystyle\frac{\alpha}{2}$，则对 $\forall\ y,z\in V_\delta(x)$，都有

$$
\left|f(y)-f(z)\right|\leq\left|f(y)-f(x)\right|+\left|f(z)-f(x)\right|\leq2\varepsilon=\alpha
$$

所以 $f$ 在 $x$ 处 $\alpha$ - 连续。

这个命题的逆否命题是若 $f$ 在 $x$ 处不 $\alpha$ - 连续，则 $f$ 在 $x$ 处不连续。所以 ${D}_{\alpha } \subseteq  {D}_{f}$ 。

<br/>

!!! question "练习 4.6.10"
    证明如果 $f$ 在 $x$ 处不连续，则 $f$ 对于某个 $\alpha  > 0$ 不是 $\alpha$ -连续的。现在解释为什么这保证了

    $$
    {D}_{f} = \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{D}_{\frac{1}{n}}
    $$

    因为每个 ${D}_{\frac{1}{n}}$ 都是闭集，证明完成。

若 $f$ 在 $x$ 处不连续，则 $\exists\ \varepsilon_0>0$，对 $\forall\ \delta>0$ 都 $\exists\ y\in V_\delta(x)$ 使得 $\left|f(y)-f(x)\right|\geq \varepsilon_0$。

因为 $x\in V_\delta(x)$，所以取 $\alpha=\varepsilon_0$ 就得到 $f$ 在 $x$ 处不 $\alpha$ - 连续。

现在对 $\forall\ x\in D_f$，$f$ 在 $x$ 处不连续，所以 $\exists\ \alpha>0$ 使得 $f$ 在 $x$ 处不 $\alpha$ - 连续。又存在 $n\in \mathbb{N^+}$，使得 $\displaystyle\frac{1}{n}<\alpha$，则由练习 [4.6.8](#4.6.8) 可知 $x\in D_{\frac{1}{n}}$。所以 $x\in \displaystyle\bigcup_{n=1}^\infty D_{\frac{1}{n}}$。

又因为每个不 $\alpha$ - 连续点都是不连续点，所以对 $\forall\ x\in \displaystyle\bigcup_{n=1}^\infty D_{\frac{1}{n}}$，也有 $x\in D_f$。

所以 $D_f=\displaystyle\bigcup_{n=1}^\infty D_{\frac{1}{n}}$。因为 $D_{\frac{1}{n}}$ 都是闭集，所以 $D_f$ 是一个 ${F}_{\sigma }$ 集。

---


# 导数

## 习题 5.2 导数和介值性质

!!! question "练习 5.2.1"
    提供定理 5.2.4 的 (i) 和 (ii) 部分的证明。

$(f+g)'(c)=\displaystyle\lim_{x\to c}\displaystyle\frac{(f(x)+g(x))-(f(c)+g(c))}{x-c}\\ =\displaystyle\lim_{x\to c}\displaystyle\frac{f(x)-f(c)}{x-c}+\displaystyle\lim_{x\to c}\displaystyle\frac{g(x)-g(c)}{x-c}\\=f'(c)+g'(c)$。

$(kf)'(c)=\displaystyle\lim_{x\to c}\displaystyle\frac{kf(x)-kf(c)}{x-c}\\=k\displaystyle\lim_{x\to c}\displaystyle\frac{f(x)-f(c)}{x-c}\\=kf'(c)$。

<br/>

!!! question "练习 5.2.2"
    恰好有一项请求是不可能的。确定是哪一项，并为其他三项提供例子。在每种情况下，让我们假设函数定义在整个 $\mathbb{R}$ 上。
    
    (a) 函数 $f$ 和 $g$ 在零点不可微，但 $fg$ 在零点可微。
    
    (b) 函数 $f$ 在零点不可微，函数 $g$ 在零点可微，且 $fg$ 在零点可微。

    (c) 函数 $f$ 在零点不可微，函数 $g$ 在零点可微，且 $f + g$ 在零点可微。

    (d) 函数 $f$ 在零点可微，但在其他点均不可微。

(a) $f(x)=g(x)=\begin{cases}
    -1,\quad &\text{if } x<0\\
    1,\quad &\text{if } x\geq 0
\end{cases}$，此时 $f(x)g(x) = 1$ 在零点可微。

(b) 也许 $f=\displaystyle\frac{fg}{g}$ 会错误得出 $f$ 也可微的结论，但 $g(x)=0$ 会使这个式子无意义，从而会使 $f$ 不可微成为可能。

(c) 与上一题不同，$f=f+g-g$ 这个式子在任何情况下都是有意义的，所以 $f,g$ 的可微性必须相同，所以这种情况是不可能的。

(d) 一种想法是构造单点连续函数，例如考虑 Dirichlet 函数的变式：

$f(x)=\begin{cases}
    0,\quad &\text{if } x\in \mathbb{Q}\\
    x,\quad &\text{if } x \notin \mathbb{Q}
\end{cases}$

计算 $f'(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{f(x)-f(0)}{x}=0$，所以 $f$ 在 $0$ 处可微，而在其他任意点都不连续，所以就不可微了。

<br/>

!!! question "练习 5.2.3"
    (a) 使用定义 5.2.1 得出 $h(x)=1/x$ 的导数的正确公式。

    (b) 结合 (a) 的结果与链式法则 (定理 5.2.5) 来证明定理 5.2.4 的 (iv) 部分。

    (c) 通过类似于定理 5.2.4 (iii) 证明风格的代数变换差商，直接证明定理 5.2.4 (iv)。

(a) $h'(c)=\displaystyle\lim_{x\to c}\displaystyle\frac{\frac{1}{x}-\frac{1}{c}}{x-c}=\displaystyle\lim_{x\to c}-\displaystyle\frac{1}{xc}=-\displaystyle\frac{1}{c^2}$。

(b) $\left(\displaystyle\frac{f}{g}\right)'(c)=\left(f'\displaystyle\frac{1}{g}\right)(c)+\left(\left(\displaystyle\frac{1}{g}\right)'f\right)(c)\\=\displaystyle\frac{f'(c)}{g(c)}+f(c)\left(-\displaystyle\frac{1}{g^2(c)}\right)g'(c)\\\ \\=\displaystyle\frac{f'(c)g(c)-g'(c)f(c)}{g^2(c)}$。

(c) $\left(\displaystyle\frac{f}{g}\right)'(c)=\displaystyle\lim_{x\to c}\displaystyle\frac{\frac{f(x)}{g(x)}-\frac{f(c)}{g(c)}}{x-c}\\=\displaystyle\lim_{x\to c}\left(\displaystyle\frac{1}{g(x)g(c)}\right)\left(\displaystyle\frac{f(x)g(c)-g(x)f(c)}{x-c}\right)\\\ \\=\displaystyle\lim_{x\to c}\left(\displaystyle\frac{1}{g(x)g(c)}\right)\left(g(x)\displaystyle\frac{f(x)-f(c)}{x-c}-f(x)\displaystyle\frac{g(x)-g(c)}{x-c}\right)\\\ \\=\displaystyle\frac{f'(c)g(c)-g'(c)f(c)}{g^2(c)}$。

<br/>

!!! question "练习 5.2.4"
    按照以下步骤提供链式法则的一个稍微修改的证明。

    (a) 证明函数 $h: A \to \mathbb{R}$ 在 $a \in A$ 处可微，当且仅当存在一个在 $a$ 处连续的函数 $l: A \to \mathbb{R}$ 满足 $h(x) - h(a) = l(x)(x - a)$ 对所有 $x \in A$ 成立。

    (b) 使用这个可微性判据 (两个方向) 来证明定理 5.2.5。

(a) $\Leftarrow$ 若 $l$ 在 $a$ 处连续，则有

$$\begin{align*}
    \displaystyle\lim_{x\to a}l(x)&=\displaystyle\lim_{x\to a}\displaystyle\frac{h(x)-h(a)}{x-a}\\&=h'(a)=l(a)
\end{align*}
$$

所以 $h$ 在 $a$ 处可微。

$\Rightarrow$ 若 $h$ 在 $a$ 处可微，则定义如下函数

$$
l(x)=\begin{cases}
    \displaystyle\frac{h(x)-h(a)}{x-a},\quad &\text{if }x\in A\setminus\left\{a\right\}\\
    h'(a),\quad &\text{if }x=a
\end{cases}
$$

则　$\displaystyle\lim_{x\to a}l(x)=\displaystyle\lim_{x\to a}\displaystyle\frac{h(x)-h(a)}{x-a}=h'(a)=l(a)$，所以 $l$ 在 $a$ 处连续。

(b) 定义这样的函数 $l$:

$$
l(x)=\begin{cases}
    \displaystyle\frac{g(x)-g(f(c))}{x-f(c)},\quad &\text{if }x\in f(A)\setminus\left\{f(c)\right\}\\
    g'(f(c)),\quad &\text{if }x=f(c)
\end{cases}
$$

由 $(a)$，有 $g(y)-g(f(c))=l(y)(y-f(c))$。

用 $y=f(x)$ 代换上式，得到

$g(f(x))-g(f(c))=l(f(x))(f(x)-f(c))$。

因为连续函数的复合还是连续函数，所以 $\displaystyle\lim_{x\to c}l(f(x))=l(f(c))=g'(f(c))$。

所以对 $\displaystyle\frac{g(f(x))-g(f(c))}{x-c}=l(f(x))\displaystyle\frac{f(x)-f(c)}{x-c}$ 左右两式取极限即得结果

$(g\circ f)'(c)=g'(f(c))f'(c)$。

<br/>

!!! question "练习 5.2.5" <a id="5.2.5"></a>
    设 $f_a(x) = \begin{cases} x^a & \text{if } x > 0 \\ 0 & \text{if } x \le 0 \end{cases}$。

    (a) 对于哪些 $a$ 值，$f$ 在零点处连续？

    (b) 对于哪些 $a$ 值，$f$ 在零点处可微？在这种情况下，导函数是连续的吗？

    (c) 对于哪些 $a$ 值，$f$ 是二次可微的？

(a) $a<0$ 时，$f_a(x)$ 在 $x>0$ 时会随着 $x$ 减小而增大，不连续；

$a=0$ 时，$f_a(x)=1$ 在 $x>0$ 时成立，所以不连续；

$a>0$ 时，取 $\delta=\varepsilon^{\frac{1}{a}}$ 可以满足 $\varepsilon-\delta$ 条件，所以连续。

综上，$a>0$ 时，$f$ 在零点处连续。

(b) 也就是说，要判断 $\displaystyle\lim_{x\to 0^+}\displaystyle\frac{x^a}{x}=\displaystyle\lim_{x\to 0^+}x^{a-1}$ 是否存在和是否等于 $0$。

当 $a<1$ 时，极限不存在即不可微；

当 $a=1$ 时，极限为 $1$，但 $\displaystyle\lim_{x\to 0^-}\displaystyle\frac{f_a(x)}{x}=0$，所以仍然不可微；

当 $a>1$ 时，极限为 $0$，所以可微。

此时导函数的式子如下：

$$
f_a'(x)=\begin{cases}
    ax^{a-1},\quad &\text{if } x>0\\
    0,\quad &\text{if } x\leq 0
\end{cases}
$$

因为 $a>1$ 时 $\displaystyle\lim_{x\to 0}ax^{a-1}=0$，所以导函数在零点处连续。导函数是连续的。

(c) 首先，单次不可微点处二次不可微，所以 $a\leq 1$ 时不二次可微。

然后同上，研究 $\displaystyle\lim_{x\to 0^+}\displaystyle\frac{ax^{a-1}}{x}=\displaystyle\lim_{x\to 0^+}ax^{a-2}$ 是否存在和是否等于 $0$。

结论：$a>2$ 时二次可微。

<br/>

!!! question "练习 5.2.6"
    设 $g$ 定义在区间 $A$ 上，且 $c \in A$。

    (a) 解释为什么定义 5.2.1 中的 $g'(c)$ 可以由下式给出
    $$ g'(c) = \lim_{h \to 0} \frac{g(c+h) - g(c)}{h} $$

    (b) 假设 $A$ 是开区间。如果 $g$ 在 $c \in A$ 处可微，证明
    $$ g'(c) = \lim_{h \to 0} \frac{g(c+h) - g(c-h)}{2h} $$

(a) 令 $x-c=h$，则 $x\to c$ 时 $h\to 0$。所以

$$
\displaystyle\lim_{x\to c}\displaystyle\frac{f(x)-f(c)}{x-c}=\displaystyle\lim_{h\to 0}\displaystyle\frac{g(c+h)-g(c)}{h}
$$

即为上式。

(b) 令 $h=-t$，则 $h\to 0$ 时 $t\to 0$。所以

$$
g'(c)=\displaystyle\lim_{t\to 0}\displaystyle\frac{g(c-t)-g(c)}{-t}=\displaystyle\lim_{h\to 0}\displaystyle\frac{g(c)-g(c-h)}{h}
$$

$$\begin{align*}
    g'(c)&=\displaystyle\frac{1}{2}\left(\displaystyle\lim_{h\to 0}\displaystyle\frac{g(c+h)-g(c)}{h}+\displaystyle\lim_{h\to 0}\displaystyle\frac{g(c)-g(c-h)}{h}\right)\\&=\lim_{h \to 0} \frac{g(c+h) - g(c-h)}{2h}
\end{align*}
$$

<br/>

!!! question "练习 5.2.7"
    设
    $$g_a(x) = \begin{cases} x^a \sin(1/x) & \text{if } x \ne 0 \\ 0 & \text{if } x = 0 \end{cases}$$
    找到一个特定的 (可能非整数) $a$ 值，使得

    (a) $g_a$ 在 $\mathbb{R}$ 上可微，但 $g'_a$ 在 $[0, 1]$ 上无界。

    (b) $g_a$ 在 $\mathbb{R}$ 上可微且 $g'_a$ 连续，但在零点不可微。（注：原文可能指 $g'_a$ 本身在零点不可微，或者 $g_a$ 满足特定条件，需结合上下文理解，原文为 "ga is differentiable on R with g'a continuous but not differentiable at zero." 这里指的是 $g'_a$ 在 0 点不可微）

    (c) $g_a$ 在 $\mathbb{R}$ 上可微且 $g'_a$ 在 $\mathbb{R}$ 上可微，但 $g''_a$ 在零点不连续。

 (a) 使 $g_a'$ 不连续可以做到这一点。

 首先我们要 $g_a'(0)=0$，由夹逼准则，$\displaystyle\lim_{x\to 0}\displaystyle\frac{x^a\sin \displaystyle\frac{1}{x}}{x}$ 的极限被 $x^{a-1}$ 控制。由 [练习 5.2.5](#5.2.5) 可知 $a>1$ 时，$g_a$ 在 $0$ 处可微且 $g_a'(0)=0$。

下面考虑函数 $g_a'(x)$：

$$
g_a'(x)=\begin{cases}
    ax^{a-1}\sin\displaystyle\frac{1}{x}-x^{a-2}\cos\displaystyle\frac{1}{x},\quad &\text{if } x\neq 0\\
    0,\quad &\text{if } x=0
\end{cases}
$$

当 $1<a<2$ 时，$x^{a-2}$ 在 $0$ 附近无界，所以 $g_a'$ 在 $[0,1]$ 上无界。比如说 $a=\displaystyle\frac{3}{2}$ 时（$n\in \mathbb{N^+}$）：

$$
g_{\frac{3}{2}}'\left(\displaystyle\frac{1}{2\pi n}\right)=-\sqrt{2\pi n}
$$

而它是无界的。

(b) 同上分析，可得 $a>2$ 时 $g_a'$ 是连续的，而 $2<a\leq 3$ 时 $g_a'$ 在 $0$ 处不可微。

(c) 由于每次求导会使得 $x$ 的指数降一次，而导函数里的最低指数会降两次（三角函数内 $\displaystyle\frac{1}{x}$ 带来的影响），所以我们可以推断，$3<a\leq 4$ 时，$g_a'$ 在 $\mathbb{R}$ 上可微，但 $g_a''$ 在 $0$ 处不连续。

<br/>

!!! question "练习 5.2.8"
    回顾一致连续性的定义 (定义 4.4.4)。给定一个可微函数 $f : A \to \mathbb{R}$，我们说 $f$ 在 $A$ 上一致可微，如果任给 $\varepsilon > 0$，存在 $\delta > 0$ 使得
    $$ \left| \frac{f(x) - f(y)}{x - y} - f'(y) \right| < \epsilon \quad \text{whenever } 0 < |x - y| < \delta $$
    
    (a) $f(x) = x^2$ 在 $\mathbb{R}$ 上是一致可微的吗？$g(x) = x^3$ 呢？

    (b) 证明如果一个函数在区间 $A$ 上是一致可微的，那么导数必须在 $A$ 上连续。

    (c) 是否存在类似于定理 4.4.7 的关于微分的定理？在闭区间 $[a, b]$ 上可微的函数一定是一致可微的吗？

(a) 对 $f(x)=x^2$ 求导可得 $f'(x)=2x$。由于

$$
\left|\displaystyle\frac{x^2-y^2}{x-y}-2y\right|=\left|x-y\right|
$$

所以令 $\delta=\varepsilon$ 即可满足。故 $f(x)=x^2$ 在 $\mathbb{R}$ 上一致可微。

对 $g(x)=x^3$ 求导可得 $g'(x)=3x^2$。由于

$$
\left|\displaystyle\frac{x^3-y^3}{x-y}-3y^2\right|=\left|x^2-2y^2+xy\right|=\left|(x-y)(x+2y)\right|
$$

当 $x,y$ 足够大时（比如 $x+2y>\displaystyle\frac{\varepsilon}{\delta}$ 时）将不会成立，所以 $g(x)=x^3$ 在 $\mathbb{R}$ 上不一致可微。

(b) 我们要证明 $\displaystyle\lim_{x\to x_0}f'(x)=f'(x_0)$ 对 $\forall\ x_0\in A$ 均成立。

若 $f$ 在 $A$ 上一致可微，则对 $\forall\ x_0\in A$，$\forall\ \varepsilon>0$，存在 $\delta>0$ 使得当 $0<|x-x_0|<\delta$ 时，有

$$
\left|\displaystyle\frac{f(x_0)-f(x)}{x_0-x}-f'(x)\right|<\varepsilon
$$

所以 $\displaystyle\lim_{x\to x_0}\left(\displaystyle\frac{f(x_0)-f(x)}{x_0-x}-f'(x)\right)=0$，展开即得 $\displaystyle\lim_{x\to x_0}f'(x)=f'(x_0)$。

所以一致可微函数其导数必连续。

(c) 我们找一个反例，如果有一个函数在闭区间上可微但导函数不连续，那么它就不是一致可微的。

考虑函数 

$$
g(x)=\begin{cases}
    x^2\sin\displaystyle\frac{1}{x},\quad &\text{if } x\neq 0\\
    0,\quad &\text{if } x=0\\
\end{cases}
$$

在闭区间 $[-1,1]$ 上可微，但其导函数 $g'(x)$ 在 $0$ 处不连续，所以 $g(x)$ 在 $[-1,1]$ 上不一致可微。

<br/>

!!! question "练习 5.2.9"
    判定每个猜想是真还是假。为真的提供论证，为假的提供反例。

    (a) 如果 $f'$ 在区间上存在且非常数，那么 $f'$ 必须取某个无理数值。

    (b) 如果 $f'$ 在开区间上存在，且存在某点 $c$ 使得 $f'(c) > 0$，那么存在 $c$ 的一个 $\delta$-邻域 $V_\delta(c)$，其中对于所有 $x \in V_\delta(c)$ 都有 $f'(x) > 0$。

    (c) 如果 $f$ 在包含零的区间上可微，且如果 $\displaystyle\lim_{x \to 0} f'(x) = L$，那么必须有 $L = f'(0)$。

(a) 正确的。由达布定理，如果存在两个值 $f'(a),f'(b)$（假设 $a<b$），对它们之间任意的无理数 $r$，总存在 $c\in (a,b)$ 使得 $f'(c)=r$。

(b) 错误的。这只在导函数连续时成立，但处处可导且不连续的函数是可以存在的。例如下题的 $g(x)=\displaystyle\frac{1}{2}x+ x^2 \sin\displaystyle\frac{1}{x}$，能够算出 $g'(0)=\displaystyle\frac{1}{2}>0$，但对 $n\in \mathbb{N^+}$ 总有 $g'\left(\displaystyle\frac{1}{2\pi n}\right)<0$。

(c) 正确的。由定义，对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ x\in V_\delta(0)\setminus\left\{0\right\}$，有 $f'(x)\in V_\varepsilon(L)$。

假设 $f'(0)\neq L$（不妨设其大于 $L$），则总存在一个 $\varepsilon>0$ 使得 $f'(0)>L+\varepsilon$。因为 $\forall\  c\in [-\displaystyle\frac{\delta}{2},\displaystyle\frac{\delta}{2}]\setminus\left\{0\right\}$，都有 $f'(c)\in V_\varepsilon(L)$，由达布定理，总要存在 $d\in [-\displaystyle\frac{\delta}{2},\displaystyle\frac{\delta}{2}]$ 使得 $f'(d)=L+\displaystyle\frac{\varepsilon}{2}$，而 $f'(d)\neq f'(0)$ 又说明 $d\in [-\displaystyle\frac{\delta}{2},\displaystyle\frac{\delta}{2}]\setminus\left\{0\right\}$，这就矛盾了。

综上所述，导函数若在某点可导，且该点的极限存在，则该极限值等于该点的导数值（即导函数在该点连续）。

<br/>

!!! question "练习 5.2.10"
    回顾：函数 $f : (a, b) \to \mathbb{R}$ 在 $(a, b)$ 上递增，如果当 $x < y$ 时 $f(x) \le f(y)$。微积分中一个熟悉的口诀是：如果导数为正，则可微函数是递增的。但为了完全准确，这个陈述需要一些改进。
    
    证明函数
    $$g(x) = \begin{cases} x/2 + x^2 \sin(1/x) & x \ne 0 \\ 0 & x = 0 \end{cases}$$
    在 $\mathbb{R}$ 上可微且满足 $g'(0) > 0$。现在，证明 $g$ 在任何包含 0 的开区间上都不是递增的。
    在下一节我们将看到 $f$ 在 $(a, b)$ 上确实是递增的当且仅当对于所有 $x \in (a, b)$ 都有 $f'(x) \ge 0$。

我们指出 $g'(0)=\displaystyle\frac{1}{2}>0$ 的事实，并在任何其他地方都可以用导数的运算规则来计算出导数的值。

然而，$g$ 在任何包含 $0$ 的开区间上都不是递增的，因为对于 $n\in \mathbb{N^+}$，考察这两个序列 $x_n=\displaystyle\frac{1}{2\pi n-\frac{\pi }{2}}$ 和 $y_n=\displaystyle\frac{1}{2\pi n+\frac{\pi}{2}}$，因为它们均趋于 $0$ 且总有 $x_n>y_n$ 和 $g(x_n)<g(y_n)$，所以 $g$ 在任何包含 $0$ 的开区间上都不是递增的。


<br/>

!!! question "练习 5.2.11"
    假设 $g$ 在 $[a, b]$ 上可微且满足 $g'(a) < 0 < g'(b)$。

    (a) 证明存在点 $x \in (a, b)$ 使得 $g(a) > g(x)$，以及点 $y \in (a, b)$ 使得 $g(y) < g(b)$。

    (b) 现在完成前面开始的达布定理的证明。

(a) 由导数定义，$g'(a)=\displaystyle\lim_{x\to a^+}\displaystyle\frac{g(x)-g(a)}{x-a}<0$，则由极限保号性，$\exists\ \delta>0$，$x\in (a,a+\delta)$ 使得 $\displaystyle\frac{g(x)-g(a)}{x-a}<0$，则 $g(a)<g(x)$。

同理也可得出 $\exists\ \delta>0$，$y\in (b-\delta,b)$ 使得 $g(y)<g(b)$。

(b) 因为 $g$ 可微，所以 $g$ 连续。由极值定理，$g$ 在 $[a,b]$ 上有最大最小值。又因为存在 $x,y\in (a,b)$ 使得 $g(a)>g(x)$ 且 $g(y)<g(b)$，所以 $g(a),g(b)$ 均不是最小值，所以 $\exists\ x_0\in (a,b)$ 使得 $g(x_0)$ 是最小值。由费马原理可得 $g'(x_0)=0$。

现在完成达布定理的证明。若 $f$ 在 $[a,b]$ 上可微，且存在 $\exists\ \alpha$ 满足 $f'(a)<\alpha<f'(b)$，则令 $g(x)=f(x)-\alpha x$ 使得 $g'(x)=f'(x)-\alpha$ 也在 $[a,b]$ 上可微。因为此时 $g'(a)<0$，$g'(b)>0$，所以 $\exists\ x_0\in (a,b)$ 满足 $g'(x_0)=f'(x_0)-\alpha=0$，由此可得 $f'(x_0)=\alpha$。

<br/>

!!! question "练习 5.2.12 (反函数)"
    如果 $f : [a, b] \to \mathbb{R}$ 是一对一的，那么存在定义在 $f$ 值域上的反函数 $f^{-1}$，由 $f^{-1}(y) = x$ 其中 $y = f(x)$ 给出。在练习 4.5.8 中我们看到如果 $f$ 在 $[a, b]$ 上连续，那么 $f^{-1}$ 在其定义域上连续。让我们增加假设：$f$ 在 $[a, b]$ 上可微且对于所有 $x \in [a, b]$ 都有 $f'(x) \ne 0$。证明 $f^{-1}$ 是可微的，且
    $$ (f^{-1})'(y) = \frac{1}{f'(x)} $$
    其中 $y = f(x)$。

根据 [练习 4.5.8](#4.5.8) 的结论，一对一的函数对 $\forall\ x_0\in [a,b]$ 一定有 $x\to x_0\Leftrightarrow f(x)\to f(x_0)$（这也是反函数存在的依据），令 $y=f(x)$，$y_0=f(x_0)$，所以

$$\begin{align*}
    (f^{-1})'(y_0)&=\displaystyle\lim_{y\to y_0}\displaystyle\frac{f^{-1}(y)-f^{-1}(y_0)}{y-y_0}\\&=\displaystyle\lim_{f(x)\to f(x_0)}\displaystyle\frac{x-x_0}{f(x)-f(x_0)}\\&=\displaystyle\lim_{x\to x_0}\displaystyle\frac{1}{\displaystyle\frac{f(x)-f(x_0)}{x-x_0}}\\&=\displaystyle\frac{1}{f'(x_0)}
\end{align*}
$$

<br/>

---

## 习题 5.3 中值定理

!!! question "练习 5.3.1"
    回顾练习 4.4.9，函数 $f : A \to \mathbb{R}$ 在 $A$ 上是利普希茨的 (Lipschitz)，如果存在 $M > 0$ 使得
    $$ \left| \frac{f(x) - f(y)}{x - y} \right| \le M $$
    对于 $A$ 中所有 $x \ne y$ 成立。
    
    (a) 证明如果 $f$ 在闭区间 $[a, b]$ 上可微，且如果 $f'$ 在 $[a, b]$ 上连续，那么 $f$ 在 $[a, b]$ 上是利普希茨的。
    
    (b) 回顾练习 4.3.11 中压缩函数的定义。如果我们增加假设：在 $[a, b]$ 上 $|f'(x)| < 1$，是否由此可得 $f$ 在该集合上是压缩的？

(a) 因为 $f$ 在 $[a,b]$ 上可微，所以由拉格朗日中值定理，对 $\forall\ x,y\in [a,b]$，$\exists\ \xi\in (a,b)$ 使得 $\displaystyle\frac{f(x)-f(y)}{x-y}=f'(\xi)$，即 $\left|\displaystyle\frac{f(x)-f(y)}{x-y}\right|=\left|f'(\xi)\right|$。

又因为 $f'$ 在 $[a,b]$ 上连续，所以由极值定理，$f'$ 在 $[a,b]$ 上有最大值和最小值，即 $f'$ 是有界的。所以对于 $\forall\ \xi \in [a,b]$，$\exists\ M>0$ 使得 $\left|f'(\xi)\right|\leq M$。所以，$\left|\displaystyle\frac{f(x)-f(y)}{x-y}\right|=\left|f'(\xi)\right|\leq M$。所以 $f$ 在 $[a,b]$ 上是利普希茨的。

(b) 因为 $|f'(x)|<1$，所以 $\max\left|f'(x)\right|=M< 1$，所以 $\left|f(x)-f(y)\right|\leq M\left|x-y\right|$。所以 $f$ 在 $[a,b]$ 上是压缩的。

<br/>

!!! question "练习 5.3.2"
    设 $f$ 在区间 $A$ 上可微。如果 $A$ 上 $f'(x) \ne 0$，证明 $f$ 在 $A$ 上是一对一的。提供一个例子说明逆命题不一定为真。

对 $\forall\ x,y\in A$，不妨设 $x<y$，则 $[x,y]\subseteq A$。由拉格朗日中值定理，$\exists\ \xi \in (x,y)$ 使得 $\displaystyle\frac{f(y) - f(x)}{y - x} = f'(\xi)$。因为 $f'(\xi)\neq 0$，所以 $f(y)-f(x)\neq 0$，即 $f(x)\neq f(y)$。所以 $f$ 在 $A$ 上是一对一的。

单调函数可说明逆命题错误。例如 $f(x)=x$ 是一对一的，但 $f'(x)=1>0$。


<br/>

!!! question "练习 5.3.3"
    设 $h$ 是定义在区间 $[0, 3]$ 上的可微函数，并假设 $h(0) = 1, h(1) = 2$，且 $h(3) = 2$。
    
    (a) 论证存在一个点 $d \in [0, 3]$ 使得 $h(d) = d$。
    
    (b) 论证在某点 $c$ 我们有 $h'(c) = 1/3$。
    
    (c) 论证在定义域内的某点 $h'(x) = 1/4$。

(a) 令 $f(x)=h(x)-x$，则 $f$ 在 $[0,3]$ 上连续，且 $f(0)=f(3)=1>0$，$f(1)=-1<0$。由介值定理可得 $\exists\ d\in (0,1)$ 使得 $f(d)=h(d)-d=0$ $\Rightarrow$ $h(d)=d$。

(b) 由拉格朗日中值定理，$\exists\ c\in (0,3)$ 使得 $h'(c)=\displaystyle\frac{h(3)-h(0)}{3-0}=\displaystyle\frac{1}{3}$。

(c) 由拉格朗日中值定理，$\exists\ c_1\in (0,3)$ 使得 $h'(c_1)=\displaystyle\frac{h(3)-h(1)}{3-1}=0$。

因为 $h'(c_1)<\displaystyle\frac{1}{4}<h'(c)$，所以由达布定理，$\exists\ x\in (c_1,c)$ 使得 $h'(x)=\displaystyle\frac{1}{4}$。

<br/>

!!! question "练习 5.3.4"
    设 $f$ 在包含零的区间 $A$ 上可微，并假设 $(x_n)$ 是 $A$ 中的序列，满足 $(x_n) \to 0$ 且 $x_n \ne 0$。
    
    (a) 如果对于所有 $n \in \mathbb{N}$ 都有 $f(x_n) = 0$，证明 $f(0) = 0$ 且 $f'(0) = 0$。
    
    (b) 增加假设：$f$ 在零点二次可微，并证明 $f''(0) = 0$ 也成立。

(a) 因为 $f$ 在 $A$ 上可微且连续，所以 $f(0)=\displaystyle\lim_{n\to \infty}f(x_n)=0$。

若 $f'(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{f(x)}{x}\neq 0$，则由极限保号性，$\exists\ \delta>0$，对 $\forall\ x\in (-\delta,\delta)\setminus\left\{0\right\}$，$\left|\displaystyle\frac{f(x)}{x}\right|>0$，这与 $f(x_n)=0$ 矛盾。所以 $f'(0)=0$。

(b) 若 $f''(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{f'(x)}{x}\neq 0$，则同上分析，可得 $\exists\ \delta>0$，$\forall\ x\in (-\delta,\delta)\setminus\left\{0\right\}$ 均有 $\left|\displaystyle\frac{f'(x)}{x}\right|>0$。不妨设 $f'(x)>0$（反向同理），则由拉格朗日中值定理，对 $x_{n_1},x_{n_2}\in (0,\delta)$，$\exists\ \xi\in (x_{n_1},x_{n_2})$ 使得 $f'(\xi)=\displaystyle\frac{f(x_{n_1})-f(x_{n_2})}{x_{n_1}-x_{n_2}}=0$，但前述又表明 $f'(\xi)>0$，这就矛盾了。

综上，$f''(0)=0$。

<br/>

!!! question "练习 5.3.5"
    (a) 提供柯西广义中值定理 (定理 5.3.5) 证明的细节。
    
    (b) 给出广义中值定理的图形解释，类似于 5.3 节开头给出的中值定理的解释。(将 $f$ 和 $g$ 视为曲线的参数方程。)

(a) 我们仿照拉格朗日中值定理的证明，采用参数方程下的直线构造。假设 $f,g$ 是某条曲线参数方程下的两个分量函数，如果 $g'(x)$ 恒不为 $0$，那么构造类似直线方程如下：

$$
L(x)=f(x)-\left(\displaystyle\frac{f(b)-f(a)}{g(b)-g(a)}(g(x)-g(a))+f(a)\right)
$$

则 $L(a)=L(b)=0$，由罗尔中值定理，$\exists\ c\in (a,b)$ 使得 $L'(c)=0$，即

$$
\displaystyle\frac{f'(c)}{g'(c)}=\displaystyle\frac{f(b)-f(a)}{g(b)-g(a)}
$$

对于 $g'(x)=0$ 的情形，我们也可以对“直线”方程通分得到更一般的形式：

$$
L(x)=(f(x)-f(a))(g(b)-g(a))-(g(x)-g(a))(f(b)-f(a))
$$

结论同上，这样就证明了柯西中值定理。

(b) 如图。（华东师范大学, 数学分析 第五版（上册）, 第六章 §2, 图 6-5）

![[alt text](image-1.png)](https://img-cdn.lusyoe.com/images/HuangTianye/2026/01/18/tpso00u6so.png)

<br/>

!!! question "练习 5.3.6"
    (a) 设 $g : [0, a] \to \mathbb{R}$ 可微，$g(0) = 0$，且对于所有 $x \in [0, a]$ 都有 $|g'(x)| \le M$。证明对于所有 $x \in [0, a]$ 都有 $|g(x)| \le Mx$。
    
    (b) 设 $h : [0, a] \to \mathbb{R}$ 二次可微，$h'(0) = h(0) = 0$ 且对于所有 $x \in [0, a]$ 都有 $|h''(x)| \le M$。证明对于所有 $x \in [0, a]$ 都有 $|h(x)| \le Mx^2/2$。
    
    (c) 对于在 $[0, a]$ 上三次可微的函数，猜想并证明一个类似的结果。

(a) $x=0$ 时成立。

由拉格朗日中值定理，对 $\forall\ x\in (0,a]$，$\exists\ \xi\in (0,x)$，$|g'(\xi)|=\left|\displaystyle\frac{g(x)-g(0)}{x-0}\right|\leq M$，所以 $|g(x)|\leq Mx$。

(b) 同样 $x=0$ 时成立。

因为 $h$ 二次可微，所以 $h'$ 在 $[0,a]$ 上连续且可微。同样使用拉格朗日中值定理，得到 $\left|h''(\xi)\right|=\left|\displaystyle\frac{h'(x)-h'(0)}{x-0}\right|\leq M$ $\Rightarrow$ $\left|h'(x)\right|\leq Mx$。

因为 $\left(\displaystyle\frac{x^2}{2}\right)'=x$，所以这里我们考虑使用柯西中值定理。对 $\forall\ x\in (0,a]$，$\exists\ \xi\in (0,x)$ 使得

$$
\left|\displaystyle\frac{h(x)-h(0)}{\displaystyle\frac{x^2}{2}-0}\right|=\left|\displaystyle\frac{h'(\xi)}{\xi}\right|\leq M
\Rightarrow |h(x)|\leq M\displaystyle\frac{x^2}{2}
$$

综上有 $|h(x)| \le M\displaystyle\frac{x^2}{2}$。

(c) 对于在 $[0, a]$ 上三次可微的函数 $k$，若 $k(0)=k'(0)=k''(0)=0$ 且对于所有 $x \in [0, a]$ 都有 $|k'''(x)| \le M$，则对于所有 $x \in [0, a]$ 都有 $|k(x)| \le M\displaystyle\frac{x^3}{6}$。

$x=0$ 时还是成立的。剩下的情况用柯西中值定理递推过去：

$$
\begin{align*}
    \left|k'''(x)\right|\leq M &\Rightarrow \left|\displaystyle\frac{k''(x)}{x}\right|\leq M \\
    &\Rightarrow \left|\displaystyle\frac{k'(x)}{\displaystyle\frac{x^2}{2}}\right|\leq M \\
    &\Rightarrow \left|\displaystyle\frac{k(x)}{\displaystyle\frac{x^3}{6}}\right|\leq M \\
    &\Rightarrow |k(x)| \le M\displaystyle\frac{x^3}{6}
\end{align*}
$$

<br/>

!!! question "练习 5.3.7"
    函数 $f$ 的不动点是一个值 $x$ 使得 $f(x) = x$。证明如果 $f$ 在区间上可微且 $f'(x) \ne 1$，那么 $f$ 最多只能有一个不动点。

构造函数 $g(x)=f(x)-x$，等价于说 $g(x)$ 在区间上不能有两个零点。

设 $f$ 定义在区间 $A$ 上。若 $\exists\ x_1,x_2\in A$ 使得 $g(x_1)=g(x_2)=0$，则由罗尔中值定理 $\exists\ c\in (x_1,x_2)$ 使得 $g'(c)=0$ $\Rightarrow$ $f'(c)=1$，得到矛盾。

所以 $f$ 最多只能有一个不动点。

<br/>

!!! question "练习 5.3.8 （<a id="16">导函数极限定理</a>）"
    假设 $f$ 在包含零的区间上连续，且对于所有 $x \ne 0$ 可微。如果 $\displaystyle\lim_{x \to 0} f'(x) = L$，证明 $f'(0)$ 存在且等于 $L$。


由极限定义，对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ x\in V_\delta(0)\setminus\left\{0\right\}$，有 $f'(x)\in V_\varepsilon(L)$。

对于 $\forall\ x\in V_\delta(0)\setminus\left\{0\right\}$，由拉格朗日中值定理，总存在 $\xi \in (0,x)$（$x>0$）或 $\xi \in (x,0)$（$x<0$）使得

$$
\left|\displaystyle\frac{f(x)-f(0)}{x-0}\right|=\left|f'(\xi)\right|\in V_\varepsilon(L)
$$

所以 $f'(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{f(x)-f(0)}{x-0}=L$。

这个定理给出了只用连续和极限存在就能得到导函数也连续的结论。

<br/>

!!! question "练习 5.3.9"
    假设 $f$ 和 $g$ 如定理 5.3.6 中所述，但现在增加假设：$f$ 和 $g$ 在 $a$ 处可微，且 $f'$ 和 $g'$ 在 $a$ 处连续，其中 $g'(a) \ne 0$。在这个更强的假设下，为洛必达法则的 $0/0$ 情况找到一个简短的证明。

直接求导：（其实我没想到，脑子瓦特了）

$$
\begin{align*}
    \displaystyle\lim_{x\to a}\displaystyle\frac{f(x)}{g(x)}&=\displaystyle\lim_{x\to a}\displaystyle\frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}=\displaystyle\frac{f'(a)}{g'(a)}=\displaystyle\lim_{x\to a}\displaystyle\frac{f'(x)}{g'(x)}
\end{align*}
$$

<br/>

!!! question "练习 5.3.10"
    设 $f(x) = x \sin(1/x^4)e^{-1/x^2}$ 和 $g(x) = e^{-1/x^2}$。利用这些函数的熟悉性质，计算当 $x$ 趋于零时 $f(x), g(x), f(x)/g(x)$ 和 $f'(x)/g'(x)$ 的极限。解释为什么结果令人惊讶但不与定理 5.3.6 (洛必达法则) 的内容冲突。

综合运用之前的极限计算法则可以得到：

$\displaystyle\lim_{x\to 0}f(x)=0$，$\displaystyle\lim_{x\to 0}g(x)=0$，是 $\displaystyle\frac{0}{0}$ 型。

$\displaystyle\lim_{x\to 0}\displaystyle\frac{f(x)}{g(x)}=0$；

$\displaystyle\lim_{x\to 0}\displaystyle\frac{f'(x)}{g'(x)}=\displaystyle\lim_{x\to 0}\left(\left(\displaystyle\frac{x^3}{2}+x\right)\sin\displaystyle\frac{1}{x^4}-\displaystyle\frac{2}{x}\cos\displaystyle\frac{1}{x^4}\right)$，这个极限是不存在的。

洛必达法则要求导函数之比极限存在才能成立，如果不存在则不成立，所以不冲突。

<br/>

!!! question "练习 5.3.11"
    (a) 使用广义中值定理提供洛必达法则 $0/0$ 情况 (定理 5.3.6) 的证明。
    
    (b) 如果我们保持定理 5.3.6 假设的第一部分不变，但假设
    $$ \lim_{x \to a} \frac{f'(x)}{g'(x)} = \infty $$
    是否必然得出
    $$ \lim_{x \to a} \frac{f(x)}{g(x)} = \infty $$

(a) 若 $\displaystyle\lim_{x\to a}\displaystyle\frac{f'(x)}{g'(x)}=L$，则对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ x\in V_\delta(a)\setminus\left\{a\right\}$， 有 $\displaystyle\left|\displaystyle\frac{f'(x)}{g'(x)}\right|\in V_\varepsilon(L)$。

现在，对 $\forall\ x\in V_\delta(a)\setminus\left\{a\right\}$，由柯西中值定理，$\exists\ \xi\in (x,a)$（$x<a$）或 $\xi\in (a,x)$（$x>a$）使得

$$
\left|\displaystyle\frac{f(x)-f(a)}{g(x)-g(a)}\right|=\left|\displaystyle\frac{f(x)}{g(x)}\right|=\left|\displaystyle\frac{f'(\xi)}{g'(\xi)}\right|\in V_\varepsilon(L)
$$

所以 $\displaystyle\lim_{x\to a}\displaystyle\frac{f(x)}{g(x)}=L=\displaystyle\lim_{x\to a}\displaystyle\frac{f'(x)}{g'(x)}$。

(b) 用同样的极限思路进行估计。

对 $\forall\ M>0$，$\exists\ \delta>0$，对 $\forall\ x\in V_\delta(a)\setminus\left\{a\right\}$， 有 $\displaystyle\displaystyle\frac{f'(x)}{g'(x)}>M$。

对这一部分 $x$，使用柯西中值定理得到 $\displaystyle\frac{f(x)}{g(x)}=\displaystyle\frac{f'(\xi)}{g'(\xi)}>M$，
于是 $\displaystyle\lim_{x\to a}\displaystyle\frac{f(x)}{g(x)}=\infty$。

这里我犯了一点糊涂，以为要 $\displaystyle\frac{f(x)}{g(x)}$ 在 $a$ 处连续才行，实际上柯西中值定理只需要 $f,g$ 本身满足就可以了。

<br/>

!!! question "练习 5.3.12"
    如果 $f$ 在包含 $a$ 的开区间上二次可微，且 $f''$ 在 $a$ 处连续，证明
    $$ \lim_{h \to 0} \frac{f(a + h) - 2f(a) + f(a - h)}{h^2} = f''(a) $$
    (比较练习 5.2.6(b))

使用洛必达法则：

原式 $=\displaystyle\lim_{h\to 0}\displaystyle\frac{f'(a+h)-f'(a-h)}{2h}=f''(a)$。

解释一下题目里二阶导连续的问题：其实只要二阶导存在，就可以用上述方法求解，而连续（其实也不用连续，附近二阶可微就行了）的条件下 $a$ 附近的二阶导是存在的，所以可以直接连用两次洛必达法则，更快得到结果：

原式 $=\displaystyle\lim_{h \to 0}\displaystyle\frac{f'(a+h)-f'(a-h)}{2h}=\displaystyle\lim_{h\to 0}\displaystyle\frac{f''(a+h)+f''(a-h)}{2}=f''(a)$。

<br/>

---

## 习题 5.4 一个处处不可导的连续函数

!!! question "练习 5.4.1"
    在 $[-2, 3]$ 上绘制 $(1/2)h(2x)$ 的图形，并随着 $n$ 增大对这些函数进行定性描述。
    $$ h_n(x) = \frac{1}{2^n} h(2^n x) $$

![](https://img-cdn.lusyoe.com/images/HuangTianye/2026/01/20/nj28ru24up.png)

如图所示。

当 $n$ 变大时，$h_n(x)$ 值域将会越来越小，但周期也会越来越小，使得其震荡越来越频繁。

<br/>

!!! question "练习 5.4.2"
    固定 $x \in \mathbb{R}$。论证该级数
    $$ \sum_{n=0}^\infty \frac{1}{2^n} h(2^n x) $$
    绝对收敛，因此 $g(x)$ 是良定的。

$$
\begin{align*}
    \displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)&\leq\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}=2
\end{align*}
$$

由单调有界定理知其收敛。

<br/>

!!! question "练习 5.4.3"
    假设 $h(x)$ 的连续性已知，参考第四章中适当的定理，这些定理暗示了有限和
    $$ g_m(x) = \sum_{n=0}^m \frac{1}{2^n} h(2^n x) $$
    在 $\mathbb{R}$ 上是连续的。

有限个连续函数的和是有限的。

<br/>

!!! question "练习 5.4.4"
    证明
    $$ \frac{g(x_m) - g(0)}{x_m - 0} = m + 1 $$
    并利用这一点证明 $g'(0)$ 不存在。

首先，$g(0)=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}h(0)=0$。

因为 $g(x_m)=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}h(2^{n-m})$，我们需要分析 $h(2^{n-m})$ 的值。

因为 $2^{n-m}$ 要么是小于 $1$ 的正数要么是 $2$ 的倍数，而 $h(2n)=h(0+2+2+\cdots+2)=h(0)=0$，所以我们有

$$
h(2^{n-m})=\begin{cases}
    2^{n-m},\quad &\text{if } n\leq m\\
    0,\quad &\text{if } n>m
\end{cases}
$$

所以 $g(x_m)=(m+1)\cdot \displaystyle\frac{1}{2^n}\cdot 2^{n-m}=(m+1)2^{-m}$。

所以 $\displaystyle\frac{g(x_m)-g(0)}{x_m-0}=m+1$。这说明 $\displaystyle\lim_{m\to 0}\displaystyle\frac{g(x_m)-g(0)}{x_m-0}$ 不存在，所以 $g'(0)$ 不存在。

<br/>

!!! question "练习 5.4.5"
    (a) 修改前面的论证以证明 $g'(1)$ 不存在。证明 $g'(1/2)$ 不存在。
    
    (b) 证明对于任何形式为 $x = p/2^k$ 的有理数，$g'(x)$ 不存在，其中 $p \in \mathbb{Z}$ 和 $k \in \mathbb{N} \cup \{0\}$。

(a) 同上一题，求解得 $g(1)=1$。

考虑这样的序列 $x_m = 1 + \displaystyle\frac{1}{2^m}$，则 $\left\{x_m\right\}\to 1$。$g(x_m)=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}h(2^n+2^{n-m})$。

由于 $2^n+2^{n-m}$ 仍然有和上题类似的二倍性质（不过考虑 $2^0=1$ 这一特殊情况，此时 $1+2^{-m}>1$，要用周期性和绝对值再处理），所以

$$
h(2^n+2^{n-m})=\begin{cases}
    1-2^{-m},\quad &\text{if } n=0\\
    2^{n-m},\quad &\text{if } 0<n\leq m\\
    0,\quad &\text{if } n>m
\end{cases}
$$

求解得 $g(x_m)=1+(m-1)2^{-m}$，得到 $\displaystyle\frac{g(x_m)-g(1)}{x_m-1}=m-1$，同上可得 $g'(1)$ 不存在。

对 $g'\left(\displaystyle\frac{1}{2}\right)$ 的情形使用序列 $x_m=\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2^m}$ 即可用完全类似的方法得到结论。

(b) 对任意 $x=\displaystyle\frac{p}{2^k}$，为了简化问题，当 $p\geq 0$ 时，使用序列 $x_m=\displaystyle\frac{p}{2^k}+\displaystyle\frac{1}{2^m}$（小于 $0$ 时则减去 $\displaystyle\frac{1}{2^m}$，利用 $h$ 的绝对值性质结果相同）：

$g(x_m)=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{2^n}h(p\cdot 2^{n-k}+2^{n-m})$。

随着 $p$ 取值的不同内部取值会有非常多的情况（大于 $1$ 则要用绝对值取反，大于 $2$ 则要用周期性处理），这需要我们思考更多的方法来简化问题。

考虑 $h(2n)=0$ 的这一特性。在之前的习题中我们利用的主要是指数的特性，即 $h(2^n)$ 当 $n>0$ 时为 $0$ 的特性，所以纯粹的 $2^n$ 形式是利于其运算的。所以，我们可以将 $p$ 写成若干个 $2^n$ 求和的形式，更准确地来说，写出它的唯一二进制表示形式：

$$
\begin{align*}
    p=2^{p_1}+2^{p_2}+\cdots+2^{p_j},\quad p_1>p_2>\cdots>p_j\geq 0
\end{align*}
$$

（这里对表示的唯一性不作证明，具体可以使用数学归纳法或带余除法来进行证明）

这样就能改写 $h(p\cdot 2^{n-k})=h\left(\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}\right)$。

接下来用 $\displaystyle\frac{1}{2^n}$ 的等比数列性质对求和式的大小进行分析。我们可以得出以下几个结论：

1. 若 $\exists\ a\in [1,j]$ 使得 $n+p_a-k=0$，则它前面的项都是 $2$ 的倍数，所以 $h\left(\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}\right)=h\left(\displaystyle\sum_{i=a}^{j}2^{n+p_i-k}\right)$。

2.  因为 $\displaystyle\sum_{i=1}^{n}\displaystyle\frac{1}{2^n}$ 在有限求和下总是小于 $1$ 的，所以上面的 $\displaystyle\sum_{i=a}^{j}2^{n+p_i-k}\in [1,2)$（因为第一项是 $1$，后面一定小于完全等比数列的求和），这就得出了结果：

$$
h\left(\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}\right)=2-\displaystyle\sum_{i=a}^{j}2^{n+p_i-k}
$$

3. 若 $\forall\ a\in [1,j],\ n+p_a-k<0$，则 $h\left(\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}\right)=\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}$。

4. 若 $\forall\ a\in [1,j],\ n+p_a-k>0$，则 $h\left(\displaystyle\sum_{i=1}^{j}2^{n+p_i-k}\right)=0$。

上述一共三种情况，其中只有第一种情况会使得绝对值符号改变。

因为等比数列的有限求和总会和 $2$ 有一段距离，考虑导数是求极限的式子，所以我们令 $m$ 足够大，使得 $p\cdot 2^{n-k}+2^{n-m}$ 总不会因为 $2^{n-m}$ 的影响而超过 $1$ 或 $2$，从而能轻松求解 $h(p\cdot 2^{n-k}+2^{n-m})$。

在得出以上结论之后，我们就可以试着求解：

因为 $m$ 足够大时，$2^{n-m}$ 项不会对 $p\cdot 2^{n-k}+2^{n-m}$ 和 $1,2$ 的大小关系产生影响，所以 $h(p\cdot 2^{n-k}+2^{n-m})$ 和 $h(p\cdot 2^{n-k})$ 在 $n$ 相同时受绝对值和周期性的影响是相同的，也就是说所有的 $p\cdot 2^{n-k}$ 都会在导数的差商式子中被抵消掉，只会剩下 $2^{-m}$ 的倍数。由于使得绝对值取反的 $n+p_a-k=0$ 的 $a$ 最多有 $j$ 个，所以当 $m$ 足够大的时候：

$$
\begin{align*}
    &g(x_m)-g(p\cdot 2^{-k})\geq (m+1-2j)2^{-m}\\
    &\displaystyle\frac{g(x_m)-g(p\cdot 2^{-k})}{x_m - p\cdot 2^{-k}}\geq m+1-2j
\end{align*}
$$

而这个下界的值可以任意大，所以 $\displaystyle\lim_{m\to\infty}\displaystyle\frac{g(x_m)-g(p\cdot 2^{-k})}{x_m - p\cdot 2^{-k}}$ 不存在，从而 $g'\left(p\cdot 2^{-k}\right)$ 不存在。

<br/>

!!! question "练习 5.4.6"
    (a) 无需过多计算，解释为什么部分和 $g_m = h_0 + h_1 + \cdots + h_m$ 在 $x$ 处可微。现在，证明对于每一个 $m$ 的值，我们有
    $$ |g'_{m+1}(x) - g'_m(x)| = 1 $$
    
       (b) 证明这两个不等式
       $$ \frac{g(y_m) - g(x)}{y_m - x} < g'_m(x) < \frac{g(x_m) - g(x)}{x_m - x} $$
    
       (c) 使用 (a) 和 (b) 部分来证明 $g'(x)$ 不存在。

(a) 首先，$h_n(x)$ 在非 $0,2^{-n},-2^{-n}$ 处可微；然后，$x$ 不是二进点，所以 $x$ 在 $h_n(x)$ 上可微；最后，有限个可微函数的和是可微的。

由于 $|h'(2^nx)|=2^n$，所以

$$
\begin{align*}
    \left|g'_{m+1}(x) - g'_m(x)\right|&=\left|\left(\displaystyle\frac{1}{2^{m+1}}h(2^{m+1}x)\right)'+\left(\displaystyle\sum_{n=0}^{m}\displaystyle\frac{1}{2^n}h(2^nx)\right)'-\left(\displaystyle\sum_{n=0}^{m}\displaystyle\frac{1}{2^n}h(2^nx)\right)'\right|\\&=1
\end{align*}
$$

(b) 下面的论证基于 Gemini 给的这些提示：

(1) $g_m(x)$ 在二进点区间 $[\displaystyle\frac{p}{2^m},\displaystyle\frac{p+1}{2^m}]$ 上是线性的。因为区间端点正好是 $h_m(x)$ 的两端点，所以对 $h_m(x)$ 及更小的下标来说都是线性的。

(2) $g(x_m)=g_m(x_m)$，因为对更大的下标 $n>m$ 来说，$2^n\cdot\displaystyle\frac{p}{2^m}$ 是 $2$ 的倍数，从而 $h_n(x_m)=0$。同理 $g(y_m)=g_m(y_m)$。

所以式子可以重写成

$$ \frac{g(y_m) - g(x)}{y_m - x} < \displaystyle\frac{g(y_m)-g(x_m)}{y_m-x_m} < \frac{g(x_m) - g(x)}{x_m - x} $$

这说明它们之间一定是有联系的。为了更加明确这个联系，我们试着用定量分析的方法进行求解。

先分析 $h'(2^nx)$ 的大小，由于它本质上是 $|2^nx|$，所以：

$$
h'(2^nx)=\begin{cases}
    2^n,\quad &\text{if } 2k<2^nx<2k+1\\
    -2^n,\quad &\text{if } 2k+1<2^nx<2k+2
\end{cases}
$$

其中 $k\in\mathbb{Z}$。因为 $x$ 不是二进点，所以 $2^nx$ 不会是一个整数。

所以 $g_m'(x)=\displaystyle\sum_{n=0}^{m}\displaystyle\frac{1}{2^n}h'(2^nx)=\displaystyle\sum_{i=0}^{m}(-1)^{x_i}$，其中 $x_i\in\{0,1\}$ 代表 $h'(2^nx)$ 的符号。

接下来计算 $g(y_m),g(x_m)$。首先，因为 $x_m,y_m$ 都是二进点，所以 $g(y_m)=g_m(y_m)$，$g(x_m)=g_m(x_m)$。

难点同样在判定它们的符号上，幸运的是，它们的符号总会是相同的。要证明这一点，我们需要得出 $2^n y_m$ 和 $2^n x_m$（$n<m$）与 $x$ 都落在同样的两个整数之间。通过证明它们之间没有整数可以做到这一点：

假设存在整数 $k$ 满足 $2^n x_m < k < 2^n y_m$，则 $p<2^{m-n}k<p+1$，矛盾。所以 $(2^nx_m,2^ny_m)$ 上不存在整数。这样我们就有：

$$
\begin{align*}
    &2k\leq 2^nx_m<2^nx<2^ny_m\leq 2k+1\\
    \text{或者 }&2k+1\leq 2^nx_m<2^nx<2^ny_m\leq 2k+2
\end{align*}
$$

所以 $2^nx_m$，$2^nx$，$2^ny_m$ 都落在同样的两个整数之间，这就保证了它们被周期性和绝对值处理的方式是相同的。所以有：

$$
\begin{align*}
    \displaystyle\frac{g(x_m)-g(x)}{x_m-x}&=\displaystyle\frac{g_m(x_m)-g_m(x)-\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{x_m-x}\\&=\displaystyle\frac{\displaystyle\sum_{n=1}^{m}\displaystyle\frac{1}{2^n}\displaystyle\sum_{i=0}^{m}(-1)^{x_i}2^n(x_m-x)-\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{x_m-x}\\&=\frac{\displaystyle\sum_{i=0}^{m}(-1)^{x_i}(x_m-x)-\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{x_m-x}\\&=\displaystyle\sum_{i=0}^{m}(-1)^{x_i}+\displaystyle\frac{\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{x-x_m}\\&=g_m'(x)+\displaystyle\frac{\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{x-x_m}>g_m'(x)
\end{align*}
$$

求和式里绝对值和 $x$ 非二进点的性质保证了大于号成立。

同理可计算 $\displaystyle\frac{g(y_m) - g(x)}{y_m - x}=g_m'(x)-\displaystyle\frac{\displaystyle\sum_{n=m+1}^{\infty}\displaystyle\frac{1}{2^n}h(2^nx)}{y_m - x}<g_m'(x)$。

(c) 如果 $g'(x)$ 存在，则 $g'(x)=\displaystyle\lim_{m\to \infty}\displaystyle\frac{g(y_m)-g(x)}{y_m-x}=\displaystyle\lim_{m\to \infty}\displaystyle\frac{g(x_m)-g(x)}{x_m-x}=\displaystyle\lim_{m\to \infty} g_m'(x)$。

但是由 (a) 部分可知，$|g'_{m+1}(x)-g'_m(x)|=1$，所以 $\left\{g_m'(x)\right\}$ 不是柯西收敛的，从而 $\displaystyle\lim_{m\to \infty} g_m'(x)$ 不存在，矛盾。所以 $g'(x)$ 不存在。

<br/>

!!! question "练习 5.4.7"
    回顾 $g(x)$ 在非二进点处不可微的论证。如果我们用求和 $\sum_{n=0}^\infty (1/2^n)h(3^n x)$ 替换 $g(x)$，这个论证是否仍然成立？这个论证对于函数 $\sum_{n=0}^\infty (1/3^n)h(2^n x)$ 是否有效？

这一论断的关键变化是对柯西收敛数列的描述。如果我们令 $g(x)=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{p^n}h(q^nx)$ ：

$$
\begin{align*}
    \left|g'_{m+1}(x) - g'_m(x)\right|&=\left|\left(\displaystyle\frac{1}{p^{m+1}}h(q^{m+1}x)\right)'+\left(\displaystyle\sum_{n=0}^{m}\displaystyle\frac{1}{p^n}h(q^nx)\right)'-\left(\displaystyle\sum_{n=0}^{m}\displaystyle\frac{1}{p^n}h(q^nx)\right)'\right|\\&=\left(\displaystyle\frac{q}{p}\right)^{m+1}
\end{align*}
$$

对于 $p=2$，$q=3$ 的情况，仍然发散的结果表明论证仍然成立。但 $p=3$，$q=2$ 时，$\left(\displaystyle\frac{2}{3}\right)^{m+1}$ 是收敛的，所以此方法在这时失效。

<br/>

---

# 函数序列与函数级数

## 习题 6.2 函数序列的一致收敛

!!! question "练习 6.2.1"
    令 $f_n(x) = \dfrac{nx}{1+nx^2}$。
    
    (a) 求 $(f_n)$ 在 $x \in (0, \infty)$ 上的逐点极限；
    (b) 收敛在 $(0, \infty)$ 上是一致的吗？
    (c) 收敛在 $(0, 1)$ 上是一致的吗？
    (d) 收敛在 $(1, \infty)$ 上是一致的吗？

<br/>

!!! question "练习 6.2.2"
    (a) 定义 $\mathbb{R}$ 上的函数序列：
    $$
    f_n(x) = \begin{cases} 1 & \text{若 } x = 1, 1/2, 1/3, \dots, 1/n \\ 0 & \text{其他情况} \end{cases}
    $$
    令 $f$ 为 $f_n$ 的逐点极限。每个 $f_n$ 在零点处连续吗？$f_n \to f$ 在 $\mathbb{R}$ 上是一致的吗？$f$ 在零点处连续吗？
    
    (b) 对函数序列 $g_n$ 重复此练习：
    $$
    g_n(x) = \begin{cases} x & \text{若 } x = 1, 1/2, 1/3, \dots, 1/n \\ 0 & \text{其他情况} \end{cases}
    $$
    
    (c) 对序列 $h_n$ 重复此练习：
    $$
    h_n(x) = \begin{cases} 1 & \text{若 } x = 1/n \\ x & \text{若 } x = 1, 1/2, \dots, 1/(n-1) \\ 0 & \text{其他情况} \end{cases}
    $$
    
    在每种情况下，解释结果如何与连续极限定理 (定理 6.2.6) 的内容相一致。

<br/>

!!! question "练习 6.2.3"
    对于每个 $n \in \mathbb{N}$ 和 $x \in [0, \infty)$，令
    $$
    g_n(x) = \frac{x}{1+x^n} \quad \text{和} \quad h_n(x) = \begin{cases} 1 & \text{若 } x \ge 1/n \\ nx & \text{若 } 0 \le x < 1/n \end{cases}
    $$
    回答关于序列 $(g_n)$ 和 $(h_n)$ 的以下问题：
    
    (a) 求 $[0, \infty)$ 上的逐点极限。
    (b) 解释我们如何知道收敛在 $[0, \infty)$ 上不可能是完全一致的。
    (c) 选择一个收敛是一致的较小集合，并提供论证说明确实如此。

<br/>

---


<br/>

!!! question "练习 6.2.4"
    回顾练习 5.2.8，其中包括一致可微函数的定义。使用 6.2 节中讨论的结果证明，如果 $f$ 是一致可微的，则 $f'$ 是连续的。

<br/>

!!! question "练习 6.2.5"
    使用实数收敛数列的柯西判别法 (定理 2.6.4)，提供定理 6.2.5 的证明。（首先，定义 $f(x)$ 的候选者，然后论证 $f_n \to f$ 是一致的。）

<br/>

!!! question "练习 6.2.6"
    假设 $f_n \to f$ 在集合 $A$ 上。定理 6.2.6 是提出一种典型问题的例子，即询问确每个 $f_n$ 拥有的特性是否会被极限函数继承。如果假设收敛仅是逐点的，提供一个反例说明以下所有命题都是错误的。然后回头确定在一致收敛的更强假设下哪些是正确的。
    
    (a) 如果每个 $f_n$ 是一致连续的，则 $f$ 是一致连续的。
    (b) 如果每个 $f_n$ 是有界的，则 $f$ 是有界的。
    (c) 如果每个 $f_n$ 有有限个不连续点，则 $f$ 有有限个不连续点。
    (d) 如果每个 $f_n$ 的不连续点少于 $M$ 个（其中 $M \in \mathbb{N}$ 是固定的），则 $f$ 的不连续点少于 $M$ 个。
    (e) 如果每个 $f_n$ 至多有可数个不连续点，则 $f$ 至多有可数个不连续点。

<br/>

!!! question "练习 6.2.7"
    设 $f$ 在整个 $\mathbb{R}$ 上一致连续，并定义函数序列 $f_n(x) = f(x + 1/n)$。证明 $f_n \to f$ 是一致的。举一个反例说明如果只假设 $f$ 是连续的而不是一致连续的，则该命题不成立。

<br/>

!!! question "练习 6.2.8"
    设 $(g_n)$ 是连续函数序列，在紧集 $K$ 上一致收敛于 $g$。如果 $g(x) \ne 0$ 在 $K$ 上，证明 $(1/g_n)$ 在 $K$ 上一致收敛于 $1/g$。

<br/>

!!! question "练习 6.2.9"
    假设 $(f_n)$ 和 $(g_n)$ 是一致收敛的函数序列。
    
    (a) 证明 $(f_n + g_n)$ 是一致收敛的函数序列。
    (b) 提供一个例子说明乘积 $(f_n g_n)$ 可能不一致收敛。
    (c) 证明如果存在 $M > 0$ 使得对所有 $n \in \mathbb{N}$ 有 $|f_n| \le M$ 和 $|g_n| \le M$，则 $(f_n g_n)$ 确实一致收敛。

<br/>

!!! question "练习 6.2.10"
    本练习和下一个练习探索连续极限定理 (定理 6.2.6) 的部分逆命题。假设 $f_n \to f$ 在 $[a, b]$ 上是逐点收敛，并且极限函数 $f$ 在 $[a, b]$ 上是连续的。如果每个 $f_n$ 是递增的（但不一定连续），证明 $f_n \to f$ 是一致的。

<br/>

!!! question "练习 6.2.11 (Dini 定理)"
    假设 $f_n \to f$ 在紧集 $K$ 上逐点收敛，并假设对于每个 $x \in K$，序列 $f_n(x)$ 是递增的。按照以下步骤证明如果 $f_n$ 和 $f$ 在 $K$ 上是连续的，则收敛是一致的。
    
    (a) 设 $g_n = f - f_n$，并将前面的假设转化为关于序列 $(g_n)$ 的陈述。
    (b) 令 $\epsilon > 0$ 任意，定义 $K_n = \{x \in K : g_n(x) \ge \epsilon\}$。论证 $K_1 \supseteq K_2 \supseteq K_3 \supseteq \dots$，并使用此观察完成论证。

<br/>

!!! question "练习 6.2.12 (康托函数)"
    回顾 3.1 节中康托集 $C \subseteq [0, 1]$ 的构造。本练习使用该讨论中的结果和符号。
    
    (a) 定义 $f_0(x) = x$ 对于所有 $x \in [0, 1]$。现在，令
    $$
    f_1(x) = \begin{cases} (3/2)x & \text{若 } 0 \le x < 1/3 \\ 1/2 & \text{若 } 1/3 \le x < 2/3 \\ (3/2)x - 1/2 & \text{若 } 2/3 \le x \le 1 \end{cases}
    $$
    在 $[0, 1]$ 上绘制 $f_0$ 和 $f_1$，并观察 $f_1$ 是连续的、递增的，并且在中间三分之一 $(1/3, 2/3) = [0, 1] \setminus C_1$ 上是常数。
    
    (b) 通过模仿这个过程构造 $f_2$，即把 $f_1$ 的每个非常数线段的中间三分之一变平。具体来说，令
    $$
    f_2(x) = \begin{cases} (1/2)f_1(3x) & \text{若 } 0 \le x < 1/3 \\ f_1(x) & \text{若 } 1/3 \le x < 2/3 \\ (1/2)f_1(3x-2) + 1/2 & \text{若 } 2/3 \le x \le 1 \end{cases}
    $$
    如果我们继续这个过程，证明结果序列 $(f_n)$ 在 $[0, 1]$ 上一致收敛。
    
    (c) 令 $f = \lim f_n$。证明 $f$ 是 $[0, 1]$ 上的连续递增函数，且 $f(0)=0$ 和 $f(1)=1$，并且满足对于所有开集 $[0, 1] \setminus C$ 中的 $x$，有 $f'(x) = 0$。
    
    回顾一下，康托集 $C$ 的“长度”为 0。不知何故，$f$ 设法从 0 增加到 1，同时在“长度为 1”的集合上保持常数。

<br/>

!!! question "练习 6.2.13"
    回顾 Bolzano-Weierstrass 定理 (定理 2.5.5) 指出，每个有界实数序列都有一个收敛子序列。对于有界函数序列的类似陈述通常不成立，但在更强的假设下，有几个不同的结论是可能的。一种途径是假设序列中所有函数的公共定义域是可数的。（另一种途径在接下来的两个练习中探讨。）
    
    令 $A = \{x_1, x_2, x_3, \dots\}$ 是一个可数集。对于每个 $n \in \mathbb{N}$，令 $f_n$ 定义在 $A$ 上，并假设存在 $M > 0$ 使得对于所有 $n \in \mathbb{N}$ 和 $x \in A$ 有 $|f_n(x)| \le M$。按照以下步骤证明存在 $(f_n)$ 的一个子序列在 $A$ 上逐点收敛。
    
    (a) 为什么实数序列 $f_n(x_1)$ 文然包含一个收敛子序列 $(f_{n_k})$？为了表明函数子序列 $(f_{n_k})$ 是通过考虑函数在 $x_1$ 处的值生成的，我们将使用符号 $f_{n_k} = f_{1,k}$。
    (b) 现在，解释为什么序列 $f_{1,k}(x_2)$ 包含一个收敛子序列。
    (c) 仔细构造一个嵌套的子序列族 $(f_{m,k})$，并展示如何使用它来产生 $(f_n)$ 的单个子序列，该子序列在 $A$ 的每一点都收敛。

<br/>

!!! question "练习 6.2.14"
    如果在集合 $E \subseteq \mathbb{R}$ 上定义的函数序列 $(f_n)$ 对于每个 $\epsilon > 0$ 存在 $\delta > 0$，使得对于所有 $n \in \mathbb{N}$ 和 $E$ 中的 $|x - y| < \delta$ 都有 $|f_n(x) - f_n(y)| < \epsilon$，则称该序列为**同程度连续** (equicontinuous)。
    
    (a) 说函数序列 $(f_n)$ 是同程度连续的，和仅仅断言序列中的每个 $f_n$ 单个地一致连续之间有什么区别？
    (b) 对序列 $g_n(x) = x^n$ 在 $[0, 1]$ 上不是同程度连续的原因给出一个定性解释。每个 $g_n$ 在 $[0, 1]$ 上是一致连续的吗？

<br/>

!!! question "练习 6.2.15 (Arzela-Ascoli 定理)"
    对于每个 $n \in \mathbb{N}$，令 $f_n$ 是定义在 $[0, 1]$ 上的函数。如果 $(f_n)$ 在 $[0, 1]$ 上是有界的——即存在 $M > 0$ 使得对于所有 $n \in \mathbb{N}$ 和 $x \in [0, 1]$ 都有 $|f_n(x)| \le M$——并且如果函数集合 $(f_n)$ 是同程度连续的 (练习 6.2.14)，按照以下步骤证明 $(f_n)$ 包含一个一致收敛子序列。
    
    (a) 使用练习 6.2.13 产生一个子序列 $(f_{n_k})$，该子序列在 $[0, 1]$ 中的每个有理点都收敛。为了简化符号，设 $g_k = f_{n_k}$。剩下的就是证明 $(g_k)$ 在整个 $[0, 1]$ 上一致收敛。
    (b) 令 $\epsilon > 0$。根据同程度连续性，存在 $\delta > 0$ 使得 $|g_k(x) - g_k(y)| < \epsilon/3$ 对于所有 $|x - y| < \delta$ 和 $k \in \mathbb{N}$ 都成立。使用这个 $\delta$，令 $r_1, r_2, \dots, r_m$ 是有限个有理点的集合，具有邻域 $V_\delta(r_i)$ 的并集包含 $[0, 1]$ 的性质。
    (c) 解释为什么必须存在 $N \in \mathbb{N}$ 使得 $|g_s(r_i) - g_t(r_i)| < \epsilon/3$ 对于所有 $s, t \ge N$ 和刚才描述的 $[0, 1]$ 的有限子集中的 $r_i$ 都成立。为什么集合 $\{r_1, r_2, \dots, r_m\}$ 是有限的很关键？
    (d) 通过证明对于任意 $x \in [0, 1]$，对于所有 $s, t \ge N$ 都有 $|g_s(x) - g_t(x)| < \epsilon$ 来完成论证。

<br/>

---

## 习题 6.3 一致收敛与微分

!!! question "练习 6.3.1"
    考虑由 $g_n(x) = \dfrac{x^n}{n}$ 定义的函数序列。
    
    (a) 证明 $(g_n)$ 在 $[0, 1]$ 上一致收敛，并求 $g = \lim g_n$。证明 $g$ 是可微的，并计算所有 $x \in [0, 1]$ 的 $g'(x)$。
    (b) 现在，证明 $(g'_n)$ 在 $[0, 1]$ 上收敛。收敛是一致的吗？设 $h = \lim g'_n$ 并比较 $h$ 和 $g'$。它们是相同的吗？

<br/>

!!! question "练习 6.3.2"
    考虑函数序列 $h_n(x) = \sqrt{x^2 + \dfrac{1}{n}}$。
    
    (a) 计算 $(h_n)$ 的逐点极限，然后证明在 $\mathbb{R}$ 上的收敛是一致的。
    (b) 注意每个 $h_n$ 都是可微的。证明 $g(x) = \lim h'_n(x)$ 对所有 $x$ 都存在，并解释我们如何确定在零的任何邻域上的收敛**不**是一致的。

<br/>

!!! question "练习 6.3.3"
    考虑函数序列 $f_n(x) = \dfrac{x}{1+nx^2}$。
    
    (a) 找出在 $\mathbb{R}$ 上每个 $f_n(x)$ 达到其最大值和最小值的点。利用这一点证明 $(f_n)$ 在 $\mathbb{R}$ 上一致收敛。极限函数是什么？
    (b) 令 $f = \lim f_n$。计算 $f'_n(x)$ 并找出使得 $f'(x) = \lim f'_n(x)$ 的所有 $x$ 值。

<br/>

!!! question "练习 6.3.4"
    令 $h_n(x) = \dfrac{\sin(nx)}{\sqrt{n}}$。证明 $h_n \to 0$ 在 $\mathbb{R}$ 上是一致的，但导数序列 $(h'_n)$ 对每个 $x \in \mathbb{R}$ 都是发散的。

<br/>

!!! question "练习 6.3.5"
    令 $g_n(x) = \dfrac{nx+x^2}{2n}$，并设 $g(x) = \lim g_n(x)$。用两种方法证明 $g$ 是可微的：
    
    (a) 通过代数方法取 $n \to \infty$ 的极限来计算 $g(x)$，然后求 $g'(x)$。
    (b) 计算每个 $n \in \mathbb{N}$ 的 $g'_n(x)$，并证明导数序列 $(g'_n)$ 在每个区间 $[-M, M]$ 上一致收敛。使用定理 6.3.3 得出 $g'(x) = \lim g'_n(x)$。
    (c) 对序列 $f_n(x) = \dfrac{nx^2+1}{2n+x}$ 重复 (a) 和 (b) 部分。

<br/>

---
<br/>

## 习题 6.4 函数级数

!!! question "练习 6.4.1"
    补全魏尔斯特拉斯 M-判别法 (推论 6.4.5) 的证明细节。

<br/>

!!! question "练习 6.4.2"
    判断每个命题是真还是假，并提供简短的理由或反例。

    (a) 如果 $\sum_{n=1}^\infty g_n$ 一致收敛，则 $(g_n)$ 一致收敛于零。
    (b) 如果 $0 \le f_n(x) \le g_n(x)$ 且 $\sum_{n=1}^\infty g_n$ 一致收敛，则 $\sum_{n=1}^\infty f_n$ 一致收敛。
    (c) 如果 $\sum_{n=1}^\infty f_n$ 在 $A$ 上一致收敛，则存在 $M$ 使得对于所有 $x \in A$ 都有 $|\sum_{n=1}^\infty f_n(x)| \le M$。

<br/>

!!! question "练习 6.4.3"
    (a) 证明
    $$
    g(x) = \sum_{n=0}^\infty \frac{\cos(2^n x)}{2^n}
    $$
    在整个 $\mathbb{R}$ 上是连续的。
    (b) 这里的收敛是一致的吗？证明你的断言。

<br/>

!!! question "练习 6.4.4"
    定义
    $$
    g(x) = \sum_{n=0}^\infty \frac{x^{2n}}{1+x^{2n}}
    $$
    找出级数收敛的所有 $x$ 值，并证明我们在这个集上得到了一个连续函数。

<br/>

!!! question "练习 6.4.5"
    (a) 证明
    $$
    h(x) = \sum_{n=1}^\infty \frac{x^n}{n^2} = x + \frac{x^2}{4} + \frac{x^3}{9} + \cdots
    $$
    定义了一个在 $[-1, 1]$ 上的连续函数。
    (b) 这个级数在 $[-1, 1]$ 上是可微的吗？如果是，其导数是连续的吗？证明它。

<br/>

!!! question "练习 6.4.6"
    令
    $$
    f(x) = \sum_{n=0}^\infty \frac{(-1)^n}{x+n} = \frac{1}{x} - \frac{1}{x+1} + \frac{1}{x+2} - \frac{1}{x+3} + \cdots
    $$
    证明 $f$ 对所有 $x > 0$ 都有定义。$f$ 在 $(0, \infty)$ 上连续吗？可微吗？由逐项微分得到的级数是否一致收敛？

<br/>

!!! question "练习 6.4.7"
    令
    $$
    f(x) = \sum_{k=1}^\infty \frac{\sin(kx)}{k^3}
    $$
    (a) 证明 $f(x)$ 是可微的，并且导数 $f'(x)$ 是连续的。
    (b) 我们能否确定 $f$ 是二次可微的？

<br/>

!!! question "练习 6.4.8"
    考虑函数
    $$
    f(x) = \sum_{k=1}^\infty \frac{\sin(x/k)}{k}
    $$
    $f$ 在哪里有定义？连续？可微？二次可微？

<br/>

!!! question "练习 6.4.9"
    令
    $$
    h(x) = \sum_{n=1}^\infty \frac{1}{x^2+n^2}
    $$
    (a) 证明 $h$ 是定义在整个 $\mathbb{R}$ 上的连续函数。
    (b) $h$ 是可微的吗？如果是，导函数 $h'$ 是连续的吗？

<br/>

!!! question "练习 6.4.10"
    令 $\{r_1, r_2, r_3, \dots\}$ 是有理数集的一个枚举。对于每个 $r_n \in \mathbb{Q}$，定义
    $$
    u_n(x) = \begin{cases} 1/2^n & \text{若 } x > r_n \\ 0 & \text{若 } x \le r_n \end{cases}
    $$
    现在，令 $h(x) = \sum_{n=1}^\infty u_n(x)$。证明 $h$ 是定义在整个 $\mathbb{R}$ 上的单调函数，并且在每个有理点都不连续。

<br/>

---

## 习题 6.5 幂级数

!!! question "练习 6.5.1"
    考虑由幂级数
    $$
    g(x) = \sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots
    $$
    定义的函数 $g$。
    
    (a) $g$ 在 $(-1, 1)$ 上有定义吗？在这个集合上连续吗？$g$ 在 $(-1, 1]$ 上有定义吗？在这个集合上连续吗？在 $[-1, 1]$ 上会发生什么？幂级数 $g(x)$ 对于任何 $|x| > 1$ 的点可能收敛吗？解释。
    (b) $g'(x)$ 对哪些 $x$ 值有定义？找出 $g'$ 的公式。

<br/>

!!! question "练习 6.5.2"
    寻找合适的系数 $(a_n)$ 使得结果幂级数 $\sum a_n x^n$ 具有给定的性质，或者解释为什么这样的要求是不可能的。
    
    (a) 对每个 $x \in \mathbb{R}$ 都收敛。
    (b) 对每个 $x \in \mathbb{R}$ 都发散。
    (c) 对所有 $x \in [-1, 1]$ 绝对收敛，并在这个集合之外发散。
    (d) 在 $x = -1$ 处条件收敛，在 $x = 1$ 处绝对收敛。
    (e) 在 $x = -1$ 和 $x = 1$ 处都条件收敛。

<br/>

!!! question "练习 6.5.3"
    (a) 如果 $\sum a_n x^n$ 在 $x=1$ 处绝对收敛，则该级数必须在 $x=-1$ 处收敛吗？
    (b) 如果 $\sum a_n x^n$ 在 $x=1$ 处收敛，则该级数必须在 $x=-1$ 处收敛吗？
    (c) 如果 $\sum a_n x^n$ 在 $x=1$ 处条件收敛，则该级数必须在 $x=-1$ 处收敛吗？
    (d) 如果 $\sum a_n x^n$ 在 $x=1$ 处发散，则该级数必须在 $x=-1$ 处发散吗？

<br/>

!!! question "练习 6.5.4"
    证明如果 $\sum a_n x^n$ 在 $A$ 上一致收敛，而 $\sum b_n x^n$ 在 $B$ 上一致收敛，则 $\sum (a_n + b_n) x^n$ 在 $A \cap B$ 上一致收敛。

<br/>

!!! question "练习 6.5.5"
    (a) 如果 $\sum a_n x^n$ 的收敛半径为 $R$，证明 $\sum a_n (x-k)^n$ 的收敛半径也为 $R$。
    (b) 假如 $\sum a_n x^n$ 和 $\sum b_n x^n$ 的收敛半径分别为 $R_a$ 和 $R_b$。证明 $\sum a_n b_n x^n$ 的收敛半径至少是 $R_a R_b$。

<br/>

!!! question "练习 6.5.6"
    如果幂级数 $\sum a_n x^n$ 在 $x=R$ 处收敛，证明它在 $(-R, R]$ 上是一致收敛的吗？

<br/>

!!! question "练习 6.5.7"
     阿贝尔定理 (Abel's Theorem, 定理 6.5.4) 说明如果在端点处收敛，则在该端点处连续。
     (a) 构造一个在 $(-1, 1)$ 上收敛但在 $x=1$ 处发散的幂级数。该幂级数必须在 $x=1$ 处趋于无穷大吗？
     (b) 如果幂级数在 $x=R$ 处收敛，证明它在 $[-R, R]$ 上不一定一致收敛。（提示：考虑 Abel 定理的逆命题）

<br/>

## 习题 6.6 泰勒级数

!!! question "练习 6.6.1"
    例 6.6.1 中的推导表明 $\arctan(x)$ 的泰勒级数对所有 $x \in (-1, 1)$ 有效。然而，注意该级数在 $x=1$ 时也收敛。假设 $\arctan(x)$ 是连续的，解释为什么级数在 $x=1$ 处的值必然是 $\arctan(1)$。这种情况下我们得到了什么有趣的恒等式？

<br/>

!!! question "练习 6.6.2"
    从本节之前生成的级数之一开始，使用类似于例 6.6.1 的操作，找出以下每个函数的泰勒级数表示。每个级数表示对于哪些确切的 $x$ 值是有效的？
    
    (a) $x \cos(x^2)$
    (b) $x / (1 + 4x^2)^2$
    (c) $\log(1 + x^2)$

<br/>

!!! question "练习 6.6.3"
    导出定理 6.6.2 中给出的泰勒系数公式 $a_n = \frac{f^{(n)}(0)}{n!}$。

<br/>

!!! question "练习 6.6.4"
    给出一个函数例子，它在 $x=0$ 处所有阶导数都存在且为零，但在零的任何邻域内都不恒为零。这说明了泰勒级数不一定收敛于生成它的函数。

<br/>

!!! question "练习 6.6.5"
    (a) 生成 $f(x) = |x|$ 在 $x=0$ 处的泰勒级数（如果存在）。
    (b) 解释为什么 $f(x) = \sqrt{x}$ 在 $x=0$ 处没有泰勒级数展开。

<br/>

!!! question "练习 6.6.6"
    求 $f(x) = \sin(x^2) + e^{x^3}$ 在 $x=0$ 处的泰勒级数前几项。

<br/>

!!! question "练习 6.6.7"
    假设 $f(x) = \sum a_n x^n$ 在 $(-R, R)$ 上收敛。证明如果是偶函数（即 $f(-x) = f(x)$），则所有奇数项系数 $a_{2k+1}$ 为零。如果是奇函数（即 $f(-x) = -f(x)$），则所有偶数项系数 $a_{2k}$ 为零。

<br/>

!!! question "练习 6.6.8"
    拉格朗日余项 (Lagrange Remainder) 形式。假设 $f$ 在包含 $0$ 的区间上是 $N+1$ 次可微的。设 $S_N(x)$ 为 $N$ 次泰勒多项式。证明存在 $c$ 在 $0$ 和 $x$ 之间使得 $f(x) = S_N(x) + \frac{f^{(N+1)}(c)}{(N+1)!} x^{N+1}$。

<br/>

!!! question "练习 6.6.9"
    柯西余项 (Cauchy Remainder) 形式。证明 $R_N(x) = \frac{f^{(N+1)}(c)}{N!} (x-c)^N x$ 对于某个 $c$ 成立。

<br/>

---

## 习题 6.7 魏尔斯特拉斯逼近定理

!!! question "练习 6.7.1"
    假设 WAT (魏尔斯特拉斯逼近定理) 成立，证明如果 $f$ 在 $[a, b]$ 上连续，则存在多项式序列 $(p_n)$ 使得 $p_n \to f$ 在 $[a, b]$ 上一致收敛。

<br/>

!!! question "练习 6.7.2"
    证明定理 6.7.3：如果 $f$ 在 $[a, b]$ 上连续，则对任意 $\epsilon > 0$ 存在多边形函数 (polygonal function) $\phi$ 使得 $|f(x) - \phi(x)| < \epsilon$。

<br/>

!!! question "练习 6.7.3"
    (a) 找出插值 $g(x) = |x|$ 在点 $(-1, 1), (0, 0), (1, 1)$ 上的二次多项式 $p(x)$。在同一坐标轴上绘制 $[-1, 1]$ 上的 $g(x)$ 和 $p(x)$。
    (b) 找出插值 $g(x) = |x|$ 在点 $x = -1, -1/2, 0, 1/2, 1$ 上的四次多项式。

<br/>

!!! question "练习 6.7.4"
    使用伯恩斯坦多项式 (Bernstein Polynomials) $B_n(f; x) = \sum_{k=0}^n f(k/n) \binom{n}{k} x^k (1-x)^{n-k}$ 来逼近 $f(x)=x^2$。证明 $B_n(x^2; x) = x^2 + \frac{x(1-x)}{n}$ 并由此验证一致收敛。

<br/>

!!! question "练习 6.7.5"
    证明如果 $f \in C[a, b]$ 且 $\int_a^b f(x) x^n dx = 0$ 对所有 $n=0, 1, 2, \dots$ 成立，则 $f(x) = 0$。

<br/>

!!! question "练习 6.7.6"
    Stone-Weierstrass 定理的推广。

<br/>

!!! question "练习 6.7.7"
    关于代数封闭子集的问题。

<br/>

---
