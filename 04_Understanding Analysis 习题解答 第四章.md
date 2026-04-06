
[9.压缩映射定理与不动点收敛问题](#8)(4.3.9)
[10.线性柯西方程](#9)(4.3.10)
[11.拓宽定义域来证明一致连续性](#11)(4.4.2)
[12.区间分割的一致连续性](#12)(4.4.5)
[13.利普希茨条件下的一致连续性](#13)(4.4.9)
[14.连续性的拓扑特征](#14)(4.4.11)
[15.连续延拓定理](#15)(4.4.13)

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

