
[1.绝对值不等式的本质](#1)(1.2.5)
[2.德·摩根律在无穷情况下的推广](#2)(1.2.12)
[3.施罗德-伯恩斯坦双射定理](#10)(1.4.13)
[4.二维可数集的构造](#3)(1.4.8)

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
