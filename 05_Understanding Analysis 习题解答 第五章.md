@import "style.less"

[16.导函数极限定理](#16)(5.3.8-5.3.9)

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

![alt text](https://img-cdn.lusyoe.com/images/HuangTianye/2026/01/18/tpso00u6so.png)

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
