@import "style.less"

[17.一致连续和一致收敛的等价命题](#17)(6.2.10)
[18.Bolzano-Weierstrass 定理的函数序列版本](#18)(6.2.14-6.2.16)

# 函数序列与函数级数

## 习题 6.2 函数序列的一致收敛

!!! question "练习 6.2.1"
    设
    $$ f_n(x) = \frac{nx}{1 + nx^2} $$
    
    (a) 找出 $(f_n)$ 对所有 $x \in (0, \infty)$ 的点态极限。
    
    (b) 在 $(0, \infty)$ 上收敛是否一致？
    
    (c) 在 $(0, 1)$ 上收敛是否一致？
    
    (d) 在 $(1, \infty)$ 上收敛是否一致？

(a) $\displaystyle\lim_{n\to \infty}f_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x}{\displaystyle\frac{1}{n}+x^2}=\displaystyle\frac{1}{x}$。

(b) 记 $f(x)=\displaystyle\frac{1}{x}$。

因为 $\left|f_n(x)-f(x)\right|=\left|\displaystyle\frac{1}{x(1+nx^2)}\right|<\varepsilon$ 会得到 $n>\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}$。

对 $\forall\ N\in \mathbb{N^+}$，让 $x$ 足够逼近 $0$ 即可使得 $\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}$ 分母足够大分子又大于某正值，最后大于 $N$。具体来说，令 $x<\min\left\{\displaystyle\frac{1}{2\varepsilon},\sqrt[3]{\displaystyle\frac{1}{2\varepsilon N}}\right\}$，则 $\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}> \displaystyle\frac{\frac{1}{2\varepsilon}}{x^3}>N$。

(c) 由 (b) 问，不一致收敛。

(d) 当 $x>1$ 时，$\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}=\displaystyle\frac{1}{\varepsilon x^3}-\displaystyle\frac{1}{x^2}<\displaystyle\frac{1}{\varepsilon}$，所以令 $N>\displaystyle\frac{1}{\varepsilon}$，即可保证不等式恒成立，因此一致收敛。

<br/>

!!! question "练习 6.2.2"
    设
    $$ g_n(x) = \frac{nx + \sin(nx)}{2n} $$
    找出 $(g_n)$ 在 $\mathbb{R}$ 上的点态极限。在 $[-10, 10]$ 上收敛是否一致？在整个 $\mathbb{R}$ 上收敛是否一致？
    
$\displaystyle\lim_{n\to \infty}g_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x+\displaystyle\frac{\sin(nx)}{n}}{2}=\displaystyle\frac{x}{2}$。

$\left|g_n(x)-\displaystyle\frac{x}{2}\right|=\left|\displaystyle\frac{\sin(nx)}{2n}\right|\leq \displaystyle\frac{1}{2n}$。

所以，对 $\forall\ \varepsilon>0$，令 $N>\displaystyle\frac{1}{2\varepsilon}$，则对 $\forall\ n\geq N$ 和 $\forall\ x\in \mathbb{R}$，都有 $\left|g_n(x)-\displaystyle\frac{x}{2}\right|<\varepsilon$。

所以 $g_n$ 在 $[-10,10]$ 和 $\mathbb{R}$ 上都一致收敛。

<br/>

!!! question "练习 6.2.3"
    考虑函数序列
    $$ h_n(x) = \frac{x}{1 + x^n} $$
    在域 $[0, \infty)$ 上。
    (a) 找出 $(h_n)$ 在 $[0, \infty)$ 上的逐点极限。

    (b) 解释为什么我们知道收敛在 $[0, \infty)$ 上不可能一致。

    (c) 选择一个较小的集合，使得收敛在其上一致，并提供论证证明情况确实如此。
    
(a) 因为

$$
\displaystyle\lim_{n\to \infty}x^n=\begin{cases}
    0,\quad &\text{if } 0\leq x<1\\
    1,\quad &\text{if } x=1\\
    +\infty,\quad &\text{if } x>1
\end{cases}
$$

所以

$$
h(x)=\displaystyle\lim_{n\to \infty}h_n(x)=\begin{cases}
    x, \quad &\text{if }0\leq x<1\\
    \displaystyle\frac{1}{2}, \quad &\text{if } x=1\\
    0, \quad &\text{if } x>1
\end{cases}
$$

(b) 因为 $h_n(x)$ 是连续的，而一致收敛的函数列的极限函数也是连续的，但 $h(x)$ 不连续，所以不可能一致收敛。

(c) 我们证明 $\left\{h_n(x)\right\}$ 在 $[2,+\infty)$ 上一致收敛。

因为 $x\geq 2$，取 $n>2$，所以 $h_n(x)=\displaystyle\frac{x}{1+x^n}=\displaystyle\frac{1}{\displaystyle\frac{1}{x}+x^{n-1}}<\displaystyle\frac{1}{x^{n-1}}\leq\displaystyle\frac{1}{2^{n-1}}$。

所以令 $N=\max\left\{3,\log_{2}{\displaystyle\frac{1}{\varepsilon}+1}\right\}$，则对 $\forall\ n>N$，$\left|h_n(x)-0 \right|<\varepsilon$。所以 $\left\{h_n(x)\right\}$ 在 $[2,+\infty)$ 上一致收敛。

<br/>

!!! question "练习 6.2.4"
    对于每个 $n \in \mathbb{N}$，找出 $\mathbb{R}$ 上函数 $f_n(x) = x/ (1 + nx^2)$ 达到其最大值和最小值的点。用此证明 $(f_n)$ 在 $\mathbb{R}$ 上一致收敛。极限函数是什么？
    
$f_n(x)$ 是连续可微的。求导可得 $f_n'(x) = \displaystyle\frac{1 - n x^2}{(1 + n x^2)^2}$。

利用中值定理我们可以知道，$f'_n(x)$ 大于 $0$ 则原函数单调递增，小于 $0$ 则单调递减。

因此，$f_n(x)$ 在 $(-\infty,\displaystyle-\frac{1}{\sqrt[]{n}})$ 递减，$(-\displaystyle\frac{1}{\sqrt[]{n}},\displaystyle\frac{1}{\sqrt[]{n}})$ 递增，$(\displaystyle\frac{1}{\sqrt[]{n}}, +\infty)$ 递减。

最大值为 $f_n\left(\displaystyle\frac{1}{\sqrt{n}}\right)=\displaystyle\frac{1}{2\sqrt{n}}$，最小值为 $f_n\left(-\displaystyle\frac{1}{\sqrt[]{n}}\right)=-\displaystyle\frac{1}{2\sqrt{n}}$。

首先，$f(x)=\displaystyle\lim_{n\to \infty}f_n(x)=0$。

因为 $\left|f(x)-f_n(x)\right|\leq \displaystyle\frac{1}{2\sqrt{n}}$，所以 $N$ 的选取是与 $x$ 无关的，所以 $\left\{f_n(x)\right\}$ 在 $\mathbb{R}$ 上一致收敛，极限函数为 $f(x)=0$。

<br/>

!!! question "练习 6.2.5"
    对于每个 $n \in \mathbb{N}$，在 $\mathbb{R}$ 上定义 $f_n$
    $$ f_n(x) = \begin{cases} 1 & \text{if } |x| \ge 1/n \\ n|x| & \text{if } |x| < 1/n \end{cases} $$
    (a) 找出 $(f_n)$ 在 $\mathbb{R}$ 上的逐点极限，并判断收敛是否一致。
    
    (b) 构造一个连续函数的逐点极限的例子，该极限在紧集 $[-5, 5]$ 上处处收敛到一个在该集上无界的极限函数。
    
(a) 对 $\forall\ x_0\in \mathbb{R}\setminus\left\{0\right\}$，取 $N>\displaystyle\frac{1}{|x_0|}$，则对 $\forall\ n>N$，$|x_0|\geq \displaystyle\frac{1}{n}$，所以 $f_n(x_0)=1$。

当 $x_0=0$ 时，$f_n(0)=0$。

所以 $f(x)=\begin{cases}    0,\quad \text{if } x=0\\    1,\quad \text{if } x\neq 0\end{cases}$

而一致收敛的连续函数序列总能收敛到连续函数，所以 $\left\{f_n\right\}$ 不一致收敛。

(b) 分段函数能够生成带可去间断点的极限函数。 <a id="6.2.5"></a>

$$
f_n(x)=\begin{cases}
    \displaystyle\frac{1}{|x|},\quad &\text{if }|x|\geq \displaystyle\frac{1}{n}\\
    n^2|x|,\quad &\text{if }|x|<\displaystyle\frac{1}{n}
\end{cases}
$$

则极限函数为

$$
f(x)=\begin{cases}
    \displaystyle\frac{1}{|x|},\quad &\text{if }x\neq 0\\
    0,\quad &\text{if }x=0
\end{cases}
$$

<br/>

!!! question "练习 6.2.6"
    利用实数收敛序列的 Cauchy 准则 (定理 2.6.4)，为定理 6.2.5 (一致收敛的 Cauchy 准则) 提供一个证明。(首先，定义一个 $f(x)$ 的候选者，然后论证 $f_n \to f$ 一致收敛。)
    
$\Rightarrow$ 若 $f_n\to f$ 一致收敛（设定义域为 $A$），则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$\forall\ x\in A$，$\left|f_n(x)-f(x)\right|<\displaystyle\frac{\varepsilon}{2}$。

则对 $\forall\ m,n>N$，有 $\left|f_m(x)-f(x)\right|<\displaystyle\frac{\varepsilon}{2}$。

所以 $\left|f_m(x)-f_n(x)\right|\leq \left|f_m(x)-f(x)\right|+\left|f_n(x)-f(x)\right|<\varepsilon$。

$\Leftarrow$ 若对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n>N$，$\forall\ x\in A$，$\left|f_m(x)-f_n(x)\right|<\varepsilon$。

则对任意的 $x_0\in A$，$\left\{f_n(x_0)\right\}$ 是 Cauchy 列，所以收敛。设 $\displaystyle f(x_0)=\lim_{n\to \infty}f_n(x_0)$，则有 $f_n(x)$ 逐点收敛于 $f(x)$。

下证其一致收敛。

假设它不一致收敛，则存在 $\varepsilon_0>0$，对 $\forall\ N\in \mathbb{N^+}$，$\exists\ n>N$，$\exists\ x_n\in A$，使得 $\left|f_n(x_n)-f(x_n)\right|\geq \varepsilon_0$。

我的想法如下：利用某个 $f_n(x_0)$ 与 $f(x_0)$ 足够远的情况，再利用 Cauchy 列的性质使得 $\left\{f_n(x_0)\right\}$ 无法收敛到 $f(x_0)$，进而得出矛盾。

取 $N_1$，使得对 $\forall\ m,n>N_1$，$\forall\ x\in A$，都有 $\left|f_m(x)-f_n(x)\right|<\displaystyle\frac{\varepsilon_0}{2}$。

因为不一致收敛，所以 $\exists\ n>N_1$，$\exists\ x_0\in A$，使得 $\left|f_n(x_0)-f(x_0)\right|\geq \varepsilon_0$。

所以对 $\forall\ m>N_1$，都有 $\left|f_m(x_0)-f_n(x_0)\right|<\displaystyle\frac{\varepsilon_0}{2}$。

所以 $\left|f_m(x_0)-f(x_0)\right|\geq \left|f_n(x_0)-f(x_0)\right|-\left|f_m(x_0)-f_n(x_0)\right|\geq \varepsilon_0-\displaystyle\frac{\varepsilon_0}{2}=\displaystyle\frac{\varepsilon_0}{2}$。

这说明 $\left\{f_m(x_0)\right\}$ 不收敛于 $f(x_0)$，与假设矛盾。

所以 $\left\{f_n(x)\right\}$ 一致收敛于 $f(x)$。

<br/>

!!! question "练习 6.2.7"
    假设 $(f_n)$ 在 $A$ 上一致收敛于 $f$，且每个 $f_n$ 在 $A$ 上一致连续。证明 $f$ 在 $A$ 上一致连续。
    
使用绝对值不等式：

$$
\left|f(x)-f(y)\right|\leq \left|f(x)-f_n(x)\right|+\left|f_n(x)-f_n(y)\right|+\left|f_n(y)-f(y)\right|。
$$

因为 $\left\{f_n\right\}$ 一致收敛，所以对 $\exists\ \varepsilon>0$，$\exists\ n\in \mathbb{N^+}$ 使得对 $\forall\ x\in A$，$\left|f(x)-f_n(x)\right|<\displaystyle\frac{\varepsilon}{3}$。同理 $\left|f_n(y)-f(y)\right|<\displaystyle\frac{\varepsilon}{3}$。

又因为 $f_n$ 在 $A$ 上一致连续，所以对上述 $\varepsilon>0$，$\exists\ \delta>0$，使得对 $\forall\ x,y\in A$，当 $|x-y|<\delta$ 时，$\left|f_n(x)-f_n(y)\right|<\displaystyle\frac{\varepsilon}{3}$。

综上所述，由绝对值不等式，对 $\forall\ x,y\in A$，$\left|x-y\right|<\delta$，有 $\left|f(x)-f(y)\right|<\varepsilon$。

所以 $f$ 在 $A$ 上一致连续。

<br/>

!!! question "练习 6.2.8"
    判断以下猜想哪些为真，哪些为假。为有效的猜想提供证明，为每个无效的猜想提供反例。
    
    (a) 如果 $f_n \to f$ 在紧集 $K$ 上逐点收敛，则 $f_n \to f$ 在 $K$ 上一致收敛。
    
    (b) 如果 $f_n \to f$ 在 $A$ 上一致收敛且 $g$ 是 $A$ 上的有界函数，则 $f_n g \to fg$ 在 $A$ 上一致收敛。
    
    (c) 如果 $f_n \to f$ 在 $A$ 上一致收敛，且每个 $f_n$ 在 $A$ 上有界，则 $f$ 也必须有界。
    
    (d) 如果 $f_n \to f$ 在集合 $A$ 上一致收敛，且 $f_n \to f$ 在集合 $B$ 上一致收敛，则 $f_n \to f$ 在 $A \cup B$ 上一致收敛。
    
    (e) 如果 $f_n \to f$ 在区间上一致收敛，且每个 $f_n$ 是递增的，则 $f$ 也是递增的。
    
    (f) 重复猜想 (e)，假设仅有点态收敛。
    
(a) 错误的。反例在 [习题 6.2.5 (b)](#6.2.5) 中给出，利用分段函数在紧集上产生无界不连续的极限函数。

(b) 正确的。若 $f_n \to f$ 在 $A$ 上一致收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$ 和 $\forall\ x\in A$，$\left|f_n(x)-f(x)\right|<\varepsilon$。

又因为 $g$ 在 $A$ 上有界，所以 $\exists\ M>0$，使得对 $\forall\ x\in A$，$\left|g(x)\right|\leq M$。

所以对 $\forall\ n>N$ 和 $\forall\ x\in A$，有
$$
\left|f_n(x)g(x)-f(x)g(x)\right|=\left|g(x)\right|\left|f_n(x)-f(x)\right|<M\varepsilon。
$$

因此 $f_n g \to fg$ 在 $A$ 上一致收敛。

(c) 正确的。若 $f_n \to f$ 在 $A$ 上一致收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$ 和 $\forall\ x\in A$，$\left|f_n(x)-f(x)\right|<\varepsilon$。

又因为每个 $f_n$ 在 $A$ 上有界，所以 $\exists\ M>0$，使得对 $\forall\ x\in A$，$|f_{N+1}(x)|<M$。

所以有 $\left|f(x)\right|\leq \left|f_{N+1}(x)\right|+\varepsilon<M+\varepsilon$。

综上，$f$ 在 $A$ 上有界。

(d) 正确的。若 $f_n \to f$ 在 $A,B$ 上分别一致收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$ 和 $\forall\ x\in A$，$\left|f_n(x)-f(x)\right|<\varepsilon$；$\exists\ N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_2$ 和 $\forall\ x\in B$，$\left|f_n(x)-f(x)\right|<\varepsilon$。

令 $N = \max\{N_1, N_2\}$，则对 $\forall\ n>N$ 和 $\forall\ x\in A \cup B$，都有 $\left|f_n(x)-f(x)\right|<\varepsilon$。

所以 $f_n \to f$ 在 $A \cup B$ 上一致收敛。

(e) 正确的。我们要证明对 $\forall\ x<y$，$f(x)\leq f(y)$。

对 $\forall\ x<y$，令 $g(n)=f_n(y)-f_n(x)$。因为对 $\forall\ n\in \mathbb{N^+}$，$g(n)\geq 0$，所以 $\displaystyle\lim_{n\to \infty}g(n)=\displaystyle\lim_{n\to \infty}f_n(y)-\displaystyle\lim_{n\to \infty}f_n(x)=f(y)-f(x)\geq 0$ $\Rightarrow$ $f(x)\leq f(y)$。

(f) 正确的，原因同上。

<br/>

!!! question "练习 6.2.9"
    假设 $(f_n)$ 在紧集 $K$ 上一致收敛于 $f$，且 $g$ 是 $K$ 上的连续函数，满足 $g(x) \neq 0$。证明 $(f_n/g)$ 在 $K$ 上一致收敛于 $f/g$。
    
因为 $g$ 是紧集 $K$ 上的连续函数，所以 $|g(x)|$ 在 $K$ 上有最小值，记为 $m$。又因为 $g(x)\neq 0$，所以 $m>0$。

因为 $f_n\to f$ 在 $K$ 上一致收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$ 和 $\forall\ x\in K$，$\left|f_n(x)-f(x)\right|<\varepsilon$。所以 $\left|\displaystyle\frac{f_n(x)}{g(x)}-\displaystyle\frac{f(x)}{g(x)}\right|=\displaystyle\frac{1}{\left|g(x)\right|}\left|f_n(x)-f(x)\right|< \displaystyle\frac{1}{m}\varepsilon$。

所以 $\displaystyle\frac{f_n}{g}$ 在 $K$ 上一致收敛于 $\displaystyle\frac{f}{g}$。

<br/>

!!! question "练习 6.2.10"
    设 $f$ 在整个 $\mathbb{R}$ 上一致连续，并通过 $f_n(x) = f(x + 1/n)$ 定义一个函数序列。证明 $f_n \to f$ 一致收敛。给出一个例子说明如果 $f$ 仅在 $\mathbb{R}$ 上连续而不一致连续，该命题不成立。
    
若 $f$ 在 $\mathbb{R}$ 上一致连续，则对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，使得对 $\forall\ x,y\in \mathbb{R}$，当 $|x-y|<\delta$ 时，$\left|f(x)-f(y)\right|<\varepsilon$。

所以对上述 $\delta>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>N$，$\displaystyle\frac{1}{n}<\delta$，所以有 $\left|f\left(x+\displaystyle\frac{1}{n}\right)-f(x)\right|<\varepsilon$。

所以 $f_n \to f$ 在 $\mathbb{R}$ 上一致收敛。

不一致连续的情况下，即使两个自变量靠得很近，函数值也不一定接近。

例如 $f(x)=x^2$ 时，$f\left(x+\displaystyle\frac{1}{n}\right)-f(x)=\displaystyle\frac{2x}{n}+\displaystyle\frac{1}{n^2}$，其中的 $\displaystyle\frac{2x}{n}$ 项就不单单是 $n$ 能控制的了。

<a id="17">一致连续与一致收敛的等价命题</a>

其实这个命题反过来也是成立的。叙述如下：

$f$ 在 $\mathbb{R}$ 上一致连续 $\Leftrightarrow$ 对任意 $a_n\to 0$，$f(x+a_n)\to f(x)$ 在 $\mathbb{R}$ 上一致收敛。

$\Rightarrow$ 同上，利用 $a_n\to 0$，找出 $a_n<\delta$ 的 $N$。

$\Leftarrow$ 假设 $f$ 在 $\mathbb{R}$ 上不一致连续，则 $\exists\ \varepsilon_0>0$，对 $\forall\ n\in \mathbb{N^+}$，都会存在 $x_n, y_n \in \mathbb{R}$ 满足 $|x_n-y_n|<\displaystyle\frac{1}{n}$，但 $\left|f(x_n)-f(y_n)\right|\geq \varepsilon_0$。

令 $a_n = y_n - x_n$，则 $|a_n| < \displaystyle\frac{1}{n}$，显然当 $n\to\infty$ 时，$\left\{a_n\right\}\to 0$。

所以对 $\forall\ n\in \mathbb{N^+}$，都存在 $x_n\in \mathbb{R}$，使得 $\left|f\left(x_n+a_n\right)-f(x_n)\right|\geq \varepsilon_0$。所以 $\left\{f(x+a_n)\right\}$ 不一致收敛，矛盾。

 综上，$f$ 在 $\mathbb{R}$ 上一致连续。

<br/>

!!! question "练习 6.2.11"
    假设 $(f_n)$ 和 $(g_n)$ 是一致收敛的函数序列。
    (a) 证明 $(f_n + g_n)$ 是一致收敛的函数序列。
    (b) 给出一个例子说明乘积 $(f_n g_n)$ 可能不一致收敛。
    (c) 证明如果存在一个 $M > 0$ 使得对于所有 $n \in \mathbb{N}$，$|f_n| \le M$ 和 $|g_n| \le M$ 成立，则 $(f_n g_n)$ 确实一致收敛。
    
(a) 因为 $\left\{f_n\right\}$，$\left\{g_n\right\}$ 均是一致收敛函数序列，所以对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，$\left|f_n(x)-f(x)\right|<\displaystyle\frac{\varepsilon}{2}$；对 $\forall\ n>N_2$ 和 $\forall\ x$，$\left|g_n(x)-g(x)\right|<\displaystyle\frac{\varepsilon}{2}$。

记 $N=\max\left\{N_1,N_2\right\}$，则对 $\forall\ n>N$，

$$
\begin{align*}
    \left|\left(f_n(x)+g_n(x\right))-\left(f(x)+g(x)\right)\right|&=\left|\left(f_n(x)-f(x)\right)+\left(g_n(x)-g(x)\right)\right|\\&\leq \left|f_n(x)-f(x)\right|+\left|g_n(x)-g(x)\right|<\varepsilon
\end{align*}
$$

所以 $\left\{f_n+g_n\right\}$ 是一致收敛的函数序列。

(b) 令 $f_n(x)=g_n(x)=x+\displaystyle\frac{1}{n}$，则它们各自收敛到 $x$，但无法收敛至 $x^2$。

(c) 因为对 $\forall\ n\in \mathbb{N^+}$，$\left|f_n\right|\leq M$，$\left|g_n\right|\leq M$，所以 $\left|f(x)\right|=\displaystyle\lim_{n\to \infty}\left|f_n(x)\right|\leq M$，同理 $\left|g(x)\right|\leq M$。

确立了 $f,g$ 的有界性后，就可以用数列极限类似的证明方式：

$$
\begin{align*}
    \left|f_n(x)g_n(x)-f(x)g(x)\right|&=\left|\left(f_n(x)-f(x)\right)g_n(x)+\left(g_n(x)-g(x)\right)f(x)\right|\\ &\leq \left|f_n(x)-f(x)\right|\left|g_n(x)\right|+\left|g_n(x)-g(x)\right|\left|f(x)\right|
\end{align*}
$$

又因为 $\left\{f_n\right\}$，$\left\{g_n\right\}$ 的一致收敛性，所以对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，$\left|f_n(x)-f(x)\right|<\displaystyle\frac{\varepsilon}{2M}$；对 $\forall\ n>N_2$，$\left|g_n(x)-g(x)\right|<\displaystyle\frac{\varepsilon}{2M}$。

取 $N=\max\left\{N_1,N_2\right\}$，则对 $\forall\ n>N$，由上式可以得到

$$
\left|f_n(x)g_n(x)-f(x)g(x)\right|<\varepsilon
$$

这就证明了 $\left\{f_ng_n\right\}$ 是一致收敛序列。

<br/>

!!! question "练习 6.2.12"
    定理 6.2.6 有一个部分逆命题。假设 $f_n \to f$ 在紧集 $K$ 上逐点收敛，并且假设对于每个 $x \in K$，序列 $f_n(x)$ 是递增的。按照以下步骤证明，如果 $f_n$ 和 $f$ 在 $K$ 上连续，则收敛是一致的。
    
    (a) 设 $g_n = f - f_n$ 并将前面的假设转化为关于序列 $(g_n)$ 的陈述。
    (b) 设 $\epsilon > 0$ 为任意值，并定义 $K_n = \{x \in K : g_n(x) \ge \epsilon\}$。论证 $K_1 \supseteq K_2 \supseteq K_3 \supseteq \cdots$ 是一个紧集的嵌套序列，并利用这一观察来完成论证。
    
(a) 设 $g_n(x)=f(x)-f_n(x)$，因为 $f_n(x)$ 是递增的，所以 $g_n(x)$ 是递减的。

可知对 $\forall\ x\in K$，$\displaystyle\lim_{n\to \infty}g_n(x)=0$。记 $g(x)=\displaystyle\lim_{n\to \infty}g_n(x)=0$。

(b) 因为对 $\forall\ x\in K$，$\forall\ p,q \in \mathbb{N^+}$ 且 $p<q$ 有 $f_p(x)\leq f_q(x)$，所以 $g_p(x)\geq g_q(x)$。若 $g_q(x)\geq \varepsilon$，则 $g_p(x)\geq \varepsilon$，所以 $K_p \supseteq K_q$。

**这里我漏掉了一个关键的步骤，它利用了 $f_n，f$ 的连续性**，那就是证明 $K_n$ 是紧集。

因为 $f_n$ 和 $f$ 在 $K$ 上连续，所以 $g_n$ 在 $K$ 上连续。设 $\left\{x_m\right\}\subseteq K_n$，则 $\left\{x_m\right\}\subseteq K$。因为 $K$ 是紧集，所以 $\left\{x_m\right\}$ 有一个收敛子列 $\left\{x_{m_k}\right\}\to x_0$，其中 $x_0\in K$。

因为对 $\forall\ k\in \mathbb{N^+}$，$g_n(x_{m_k})\geq \varepsilon$，由 $g_n$ 的连续性，$g_n(x_0)\geq \varepsilon$。所以 $x_0\in K_n$，这就证明了 $K_n$ 是紧集。

紧集嵌套序列给我们的灵感是一个定理：若对 $\forall\ n\in \mathbb{N^+}$，$K_n$ 均不为空，则 $\displaystyle\bigcap_{n=1}^{\infty} K_n$ 同样不空。也就是说，$\exists\ x_0\in \displaystyle\bigcap_{n=1}^{\infty} K_n$。由 $K_n$ 的定义，对 $\forall\ n\in \mathbb{N^+}$，$g_n(x_0)\geq \varepsilon$，这与 $\displaystyle\lim_{n\to \infty}g(x_0)=0$ 是矛盾的。

所以 $\exists\ N\in \mathbb{N^+}$，使得 $K_N$ 为空集。也就是说，对 $\forall\ n>N$ 和 $\forall\ x\in K$，$g_n(x)=f(x)-f_n(x)<\varepsilon$。这就证明了 $\left\{f_n(x)\right\}\to f(x)$ 是一致收敛的。

<br/>

!!! question "练习 6.2.13 (Cantor 函数)"
    回顾第 3.1 节中 Cantor 集 $C \subseteq [0,1]$ 的构造。本练习利用了该讨论中的结果和符号。
    
    (a) 为所有 $x \in [0,1]$ 定义 $f_0(x) = x$。现在，设
    $$ f_1(x) = \begin{cases} (3/2)x & \text{for } 0 \le x \le 1/3 \\ 1/2 & \text{for } 1/3 < x < 2/3 \\ (3/2)x - 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
    绘制 $f_0$ 和 $f_1$ 在 $[0,1]$ 上，并观察到 $f_1$ 是连续的、递增的，并且在中间三分之一 $(1/3, 2/3) = [0,1] \setminus C_1$ 上是恒定的。
    
    (b) 通过模仿这一过程，将 $f_1$ 的每个非恒定段的中间三分之一压平来构造 $f_2$。具体来说，令
    $$ f_2(x) = \begin{cases} (1/2)f_1(3x) & \text{for } 0 \le x \le 1/3 \\ f_1(x) & \text{for } 1/3 < x < 2/3 \\ (1/2)f_1(3x - 2) + 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
    如果我们继续这个过程，证明生成的序列 $(f_n)$ 在 $[0,1]$ 上一致收敛。
    
    (c) 设 $f = \lim f_n$。证明 $f$ 是 $[0,1]$ 上的一个连续、递增函数，且满足 $f(0) = 0$ 和 $f(1) = 1$，对于开集 $[0,1] \setminus C$ 中的所有 $x$，满足 $f'(x) = 0$。回想一下，Cantor 集 $C$ 的“长度”为 0。然而，$f$ 在“长度为 1”的集合上保持不变的同时，设法从 0 增加到 1。
    
(a) ![](https://calculus1437.github.io/MathBlog/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20203712.png){width=45%} ![](https://calculus1437.github.io/MathBlog/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20204217.png){width=45%}

(b) 直接求解出最后 $f(x)$ 的形态是困难的。所以在这里我们考虑用 Cauchy 准则，即分析 $\left|f_m(x)-f_n(x)\right|$ 的大小来进行证明。

![](https://calculus1437.github.io/MathBlog/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20213311.png)
这是 $f_2(x)$ 的图像。

观察可得，这个迭代函数是以 $f_1$ 的形状为基本模块，在每个非定值的区间里用缩放过的该模块来进行替换。所以有几个基本猜测：

(1) 如果 $f_m(x)$ 在某个区间上是定值，则对任意 $n>m$，$f_n(x)$ 在那个区间上也是定值。

(2) 模块在每次迭代中都会被横向压缩成原来的 $1/3$，纵向压缩成原来的 $1/2$。

这些猜测有什么用呢？一方面，在定值的区间上，$\left|f_m(x)-f_n(x)\right|$ 可以保持始终为 $0$；另一方面，在非定值的区间上，由于模块被放缩得越来越小，$f_m$ 和 $f_n$ 的取值也就可能越来越接近。

例如，$f_0(x)$ 和$f_1(x)$ 的差值在这个模块的“尖角”处（定值与非定值区间交点处）取得最大值，则 $f_1(x)$ 与 $f_2(x)$ 也会在放缩后的“尖角”处取得最大值，但因此时模块被放缩成原来的 $\displaystyle\frac{1}{2}$，所以差值也就会变成迭代前的 $\displaystyle\frac{1}{2}$ 了。

这些猜测直接对任意 $m,n$ 进行证明还不知如何下手，就先从相邻迭代处开始分析。

$$
f_n(x)=\begin{cases}
    \displaystyle\frac{1}{2}f_{n-1}(3x),\quad &\text{if }0\leq x\leq \displaystyle\frac{1}{3}\\\\
    f_{n-1}(x),\quad &\text{if }\displaystyle\frac{1}{3}<x<\displaystyle\frac{2}{3}\\\\
    \displaystyle\frac{1}{2}f_{n-1}(3x-2)+\displaystyle\frac{1}{2},\quad &\text{if }\displaystyle\frac{2}{3}\leq x\leq 1
\end{cases}
$$

所以

$$
\begin{align*}
    f_{n+1}(x)-f_n(x)
    &=\begin{cases}
    \displaystyle\frac{1}{2}f_n(3x)-f_n(x),\quad &\text{if }0\leq x\leq \displaystyle\frac{1}{3}\\\\
    0,\quad &\text{if }\displaystyle\frac{1}{3}<x<\displaystyle\frac{2}{3}\\\\
    \displaystyle\frac{1}{2}f_n(3x-2)+\displaystyle\frac{1}{2}-f_n(x),\quad &\text{if }\displaystyle\frac{2}{3}\leq x\leq 1
\end{cases}\\\\
&=\begin{cases}
    \displaystyle\frac{1}{2}(f_n(3x)-f_{n-1}(3x)),\quad &\text{if } 0\leq x\leq \displaystyle\frac{1}{3}\\\\
    0,\quad &\text{if } \displaystyle\frac{1}{3}<x<\displaystyle\frac{2}{3}\\\\
    \displaystyle\frac{1}{2}(f_n(3x-2)-f_{n-1}(3x-2)),\quad &\text{if } \displaystyle\frac{2}{3}\leq x\leq 1
\end{cases}
\end{align*}
$$

又因为 $\displaystyle\frac{1}{2}(f_n(3x)-f_{n-1}(3x))$ 在 $[0,\displaystyle\frac{1}{3}]$ 上实际上与 $\displaystyle\frac{1}{2}(f_n(x)-f_{n-1}(x))$ 在 $[0,1]$ 上的值域相同，所以不妨设 $g_n(x)=\max|f_{n+1}(x)-f_n(x)|$，则有 $g_n(x)=\displaystyle\frac{1}{2}g_{n-1}(x)=\cdots=\displaystyle\frac{1}{2^n}g_0(x)=\displaystyle\frac{1}{2^n}\max\left|f_1(x)-f_0(x)\right|=\displaystyle\frac{1}{2^n6}$。

借助绝对值不等式，我们就能估计 $\left|f_m(x)-f_n(x)\right|$ 的值了。

对 $\forall\ \varepsilon>0$，取 $N>\displaystyle\frac{1}{3\varepsilon}+1$，则对 $\forall\ m,n>N$，有

$$
\begin{align*}
    \left|f_m(x)-f_n(x)\right|&\leq \displaystyle\sum_{i=m}^{n-1}\left|f_i(x)-f_{i+1}(x)\right|\leq \displaystyle\sum_{i=m}^{n-1}g_i(x)\\
    &=\displaystyle\sum_{i=m}^{n-1}\displaystyle\frac{1}{2^i6}=\displaystyle\frac{1}{2^m6}\displaystyle\sum_{i=1}^{n-m}\displaystyle\frac{1}{2^i}\\
    &<\displaystyle\frac{1}{2^m6}\displaystyle\sum_{i=1}^{\infty}\displaystyle\frac{1}{2^i}\\
    &=\displaystyle\frac{1}{2^m3}<\displaystyle\frac{1}{3m}<\varepsilon
\end{align*}
$$

综上，$\left\{f_n\right\}$ 是 $[0,1]$ 上的一致收敛函数序列。

(c) 由前面习题所述结论，因为对 $\forall\ n\in \mathbb{N^+}$，$f_n$ 都是连续递增的，所以 $f$ 也是连续递增的。又因为 $f_n(0)=0$，$f_n(1)=1$，所以 $f(0)=0$，$f(1)=1$。

现在解决定值区间的问题。因为

$$
    f_{n+1}(x)-f_n(x)
=\begin{cases}
    \displaystyle\frac{1}{2}(f_n(3x)-f_{n-1}(3x)),\quad &\text{if } 0\leq x\leq \displaystyle\frac{1}{3}\\\\
    0,\quad &\text{if } \displaystyle\frac{1}{3}<x<\displaystyle\frac{2}{3}\\\\
    \displaystyle\frac{1}{2}(f_n(3x-2)-f_{n-1}(3x-2)),\quad &\text{if } \displaystyle\frac{2}{3}\leq x\leq 1
\end{cases}
$$

即 $f_{n+1}(x)-f_n(x)=0$，在 $\left(\displaystyle\frac{1}{3},\displaystyle\frac{2}{3}\right)$ 和 次一级迭代上是成立的，所以由迭代规律，$f_n(3x)-f_{n-1}(3x)=0$ 在 $\left(\displaystyle\frac{1}{9},\displaystyle\frac{2}{9}\right)$ 和它的次一级迭代成立，而 $f_n(3x-2)-f_{n-1}(3x-2)=0$ 的解则向右平移 $\displaystyle\frac{2}{3}$。

第一层的定值区间，$\left(\displaystyle\frac{1}{3},\displaystyle\frac{2}{3}\right)$ 在 $[0,1]$ 上的补集是 $C_1$；第二层的定值区间在第一层的基础上切下了 $C_1$ 两个闭区间各自中间的 $\displaystyle\frac{1}{3}$，得到了 $C_2$；此后的操作与构造 $C$ 的操作完全一致。所以 $f(x)$ 的定值区间至少会包含 $[0,1]\setminus C$ 这一个开集。利用开集内任意一点始终被开区间包含的性质，依据导数的定义，就可以得到对 $\forall\ x\in [0,1]\setminus C$，$f'(x)=0$。

<br/>

<a id="18">Bolzano-Weierstrass 定理的函数序列版本</a>

!!! question "练习 6.2.14"
    回想一下，Bolzano-Weierstrass 定理 (定理 2.5.5) 指出，每个有界的实数序列都有一个收敛的子序列。对于有界函数序列的类似陈述在一般情况下并不成立，但在更强的假设下，可以得出几种不同的结论。一种方法是假设序列中所有函数的共同定义域是可数的。(另一种方法将在接下来的两个练习中探讨。)
    
    设 $A = \{x_1, x_2, x_3, \dots\}$ 为可数集。对于每个 $n \in \mathbb{N}$，令 $f_n$ 定义在 $A$ 上，并假设存在一个 $M > 0$，使得对于所有 $n \in \mathbb{N}$ 和 $x \in A$，$|f_n(x)| \le M$ 成立。按照以下步骤证明存在 $(f_n)$ 的一个子序列在 $A$ 上逐点收敛。
    
    (a) 为什么实数序列 $f_n(x_1)$ 必然包含一个收敛子序列 $(f_{n_k})$？为了表示函数子序列 $(f_{n_k})$ 是通过考虑函数在 $x_1$ 处的值生成的，我们将使用符号 $f_{n_k} = f_{1,k}$。
    (b) 现在，解释为什么序列 $f_{1,k}(x_2)$ 包含一个有界子序列。
    (c) 仔细构造一个嵌套的子序列族 $(f_{m,k})$，并使用 Cantor 对角线化技术 (来自定理 1.5.1) 生成一个在 $A$ 的每一点都收敛的 $(f_n)$ 的单一子序列。
    
(a) 由 Bolzano-Weierstrass 定理，因为 $\left\{f_n(x_1)\right\}$ 是有界的，所以有收敛子列。

(b) 同上，因为它是有界的，所以有收敛子列。

(c) 我们同上，把 $f_{1,k}$ 在 $x_2$ 处收敛的函数子序列记作 $\left\{f_{2,k}\right\}$。

因为 $\{f_{1,k}\}$ 在 $x_1$ 处收敛，所以 $\{f_{2,k}\}$ 在 $x_1,x_2$ 处均收敛。

而 $\{f_{2,k}(x_3)\}$ 也是有界的，所以它也包含一个收敛子列 $\{f_{3,k}(x_3)\}$。

继续这个过程，我们可以得到一个嵌套的子序列族 $\left\{f_{m,k}\right\}$，其中 $\left\{f_{m,k}\right\}$ 在 $x_1,x_2,\dots,x_m$ 处均收敛。

现在的难点是，我们不知道 $f_{m,k}$ 在 $m\to +\infty$ 时是否存在一个收敛的函数子序列。不过根据对角化的灵感，我们可以从已有的这些函数中进行选择来生成一个满足条件的序列。

令 $g_n(x)=f_{n,n}(x)$ （如果把所有 $f_{m,k}$ 排成矩阵，这正好是对角线上的函数！）。对 $x_p\in A$，$n>p$ 时 $g_n(x)$ 均是 $f_{p,k}(x)$ 子列中的元素（而且能保证 $k\to +\infty$），所以 $g_n(x_p)$ 是收敛的。所以 $g_n$ 在 $A$ 上逐点收敛。

<br/>

!!! question "练习 6.2.15"
    定义在集合 $E \subseteq \mathbb{R}$ 上的一列函数 $(f_n)$ 被称为**等度连续的**，如果对于每一个 $\epsilon > 0$，存在一个 $\delta > 0$，使得对于 $E$ 中的所有 $n \in \mathbb{N}$ 和 $|x - y| < \delta$，都有 $|f_n(x) - f_n(y)| < \epsilon$。
    (a) 说一列函数 $(f_n)$ 是等度连续的，与仅仅断言序列中的每一个 $f_n$ 都是单独一致连续的，有什么区别？
    (b) 给出一个定性解释，说明为什么序列 $g_n(x) = x^n$ 在 $[0, 1]$ 上不是等度连续的。每个 $g_n$ 在 $[0, 1]$ 上是否一致连续？
    
(a) 每个函数单独一致连续时，它们的 $\delta$ 可能各不相同；而等度连续要求这些函数的 $\delta$ 是同一个。

其实这跟 $f$ 连续和一致连续的区别很类似：连续函数只是在每一点都有一个适配 $\varepsilon$ 的 $\delta$，而一致连续则要求这些 $\delta$ 是相同的。

(b) 闭区间上的连续函数是一致连续的，所以 $g_n$ 的一致连续性毋庸置疑。

但我们知道 $g_n$ 不是一致收敛的。这说明为了满足 $\varepsilon-\delta$ 条件，$\delta$ 的取值必须依赖于 $n$（尤其在 $g_n(1)=1$ 附近），据此给出定性解释：

 取 $x=1$，$y=1-t\delta$（$0<t<1$），则 $\left|x-y\right|<\delta$。

 但是 $\left|1-\left(1-t\delta\right)^n\right|$ 并不能不受 $n$ 的影响而任意小。

 取 $\varepsilon_0=\displaystyle\frac{1}{2}$，

当 $\delta\geq 1$ 时，$\left|g_n(1)-g_n(0)\right|=1>\displaystyle\frac{1}{2}$。

当 $\delta<1$ 时，令 $\left(1-t\delta\right)^n<\displaystyle\frac{1}{2}$，得 $n>\displaystyle\frac{\ln \displaystyle\frac{1}{2}}{\ln \left(1-t\delta\right)}$，所以当 $n$ 大于此值时，便有 $\left|g_n(1)-g_n(1-t\delta)\right|>\displaystyle\frac{1}{2}$。

综上所述， $g_n$ 在 $[0,1]$ 上不是等度连续的。

<br/>

!!! question "练习 6.2.16 (阿尔泽拉-阿斯科利定理, Arzela-Ascoli Theorem)"
    对于每个 $n \in \mathbb{N}$，设 $f_n$ 是定义在 $[0, 1]$ 上的函数。如果 $(f_n)$ 在 $[0, 1]$ 上**有界**——即存在一个 $M > 0$，使得对于所有 $n \in \mathbb{N}$ 和 $x \in [0, 1]$，$|f_n(x)| \le M$ 成立——并且如果函数集合 $(f_n)$ 是**等度连续的** (习题 6.2.15)，按照以下步骤证明 $(f_n)$ 包含一个一致收敛的子序列。
    
    (a) 使用练习 6.2.14 生成一个子序列 $(f_{n_k})$，该序列在 $[0, 1]$ 中的每个**有理点**处收敛。为简化符号，设 $g_k = f_{n_k}$。仍需证明 $(g_k)$ 在 $[0, 1]$ 上一致收敛。
    (b) 设 $\epsilon > 0$。根据等连续性，存在一个 $\delta > 0$ 使得 $|g_k(x) - g_k(y)| < \epsilon/3$ 对于所有 $|x - y| < \delta$ 和 $k \in \mathbb{N}$。利用这个 $\delta$，设 $r_1, r_2, \dots, r_m$ 是一个有理点的有限集合，其性质是邻域 $V_\delta(r_i)$ 的并集包含 $[0, 1]$。
    解释为什么必须存在一个 $N \in \mathbb{N}$ 使得 $|g_s(r_i) - g_t(r_i)| < \epsilon/3$ 对于所有 $s, t \ge N$ 和 $r_i$ 在刚刚描述的 $[0, 1]$ 的有限子集中。为什么集合 $\{r_1, r_2, \dots, r_m\}$ 是有限的这一点很重要？
    (c) 通过证明对于任意的 $x \in [0, 1]$， $|g_s(x) - g_t(x)| < \epsilon$ 对于所有的 $s, t \ge N$ 完成论证。
    
(a) 由练习 6.2.14，可以生成这样的一个子序列 $\left\{g_k\right\}$。

(b) 因为 $g_k(x)$ 在 $[0,1]$ 上所有的有理点处收敛，所以也在 $r_i$ 处收敛。由 Cauchy 收敛准则，$\exists\ N_i\in \mathbb{N^+}$，对 $\forall\ s,t\geq N_i$，$\left|g_s(r_i)-g_t(r_i)\right|<\displaystyle\frac{\varepsilon}{3}$。

因为 $\left\{r_1,r_2,\ldots,r_m\right\}$ 是有限集，所以可以取 $N=\max\left\{N_1,N_2,\ldots,N_m\right\}$，这样对 $\forall\ s,t\geq N$ 和 $\forall\ i\in \left\{1,2,\ldots,m\right\}$，都有 $\left|g_s(r_i)-g_t(r_i)\right|<\displaystyle\frac{\varepsilon}{3}$。

(c) 对 $\forall\ x\in [0,1]$，$\exists\ i\in \left\{1,2,\ldots,m\right\}$ 使得 $x\in V_\delta(r_i)$。所以对 $\forall\ s,t\geq N$，有

$$
\begin{align*}
    \left|g_s(x)-g_t(x)\right|&\leq \left|g_s(x)-g_s(r_i)\right|+\left|g_s(r_i)-g_t(r_i)\right|+\left|g_t(r_i)-g_t(x)\right|\\
    &<\displaystyle\frac{\varepsilon}{3}+\displaystyle\frac{\varepsilon}{3}+\displaystyle\frac{\varepsilon}{3}=\varepsilon
\end{align*}
$$

所以 $g_k(x)$ 在 $[0,1]$ 上一致收敛。

<br/>

---

## 习题 6.3 一致收敛与微分

!!! question "练习 6.3.1"
    (a) 设

    \[
    {h}_{n}\left( x\right)  = \frac{\sin \left( {nx}\right) }{n}.
    \]

    证明 \({h}_{n} \rightarrow  0\) 在 \(\mathbb{R}\) 上一致收敛。导数序列 \({h}_{n}^{\prime }\) 在哪些点收敛？

    (b) 修改此示例以证明序列 \(\left( {f}_{n}\right)\) 可能一致收敛，但 \(\left( {f}_{n}^{\prime }\right)\) 无界。

(a) 因为 $\left|\sin(nx)\right|\leq 1$，所以 $\left|h_n(x)\right|\leq \displaystyle\frac{1}{n}$。对 $\forall\ \varepsilon>0$，取 $N>\displaystyle\frac{1}{\varepsilon}$，则对 $\forall\ n>N$ 和 $\forall\ x\in \mathbb{R}$，$\left|h_n(x)-0\right|=\left|h_n(x)\right|\leq \displaystyle\frac{1}{n}<\varepsilon$，所以 $h_n$ 在 $\mathbb{R}$ 上一致收敛。

$h_n'(x)=\cos(nx)$，现在要考虑 $\cos(nx)$ 的范围。具体分析见 (b) 问，结论是 $h_n'$ 在 $x=2k\pi$，$k\in \mathbb{Z}$ 上收敛。

(b) (你之前关于 $\sin(nx)/\sqrt{n}$ 的片段解答了本题 (b) 问中“修改此示例”的一部分：)

**注意：这是被删除的一道题的一部分解答，所以过程可能有些突兀**

令 $h_n(x)=\displaystyle\frac{\sin(nx)}{\sqrt{n}}$。

利用 $\sin(nx)$ 的有界性，同前几题的解法可得 $h_n \to 0$ 在 $\mathbb{R}$ 上是一致的。

$h_n'(x)=\sqrt[]{n}\cos(nx)$。前面 $\sqrt[]{n}$ 可得无界性，现在要考虑 $\cos(nx)$ 的范围。

若 $x=\displaystyle\frac{p\pi}{q}$，其中 $p,q\in \mathbb{Z}$ 且 $q>0$，令 $n=2kq$，$k\in \mathbb{N^+}$，则 $h'_{2kq}(x)=\sqrt[]{2kq}\cos(2kp\pi)=\sqrt[]{2kq}$ 发散，即证原序列也发散。

若 $x\neq \displaystyle\frac{p\pi}{q}$，此时 $\cos(nx)$ 的值难以估计，我并没有想到。询问了 Gemini 3.1 Pro 后，它提供给我了关于序列本身的思路：

假设对 $x_0\in \mathbb{R}$，$h_n'(x_0)=\sqrt[]{n}\cos(nx_0)$ 收敛，设 $\displaystyle\lim_{n\to \infty}\sqrt[]{n}\cos(nx_0)=L$，则由极限的四则运算性质可得 $\displaystyle\lim_{n\to \infty}\cos(nx_0)=\displaystyle\frac{\displaystyle\lim_{n\to \infty}\sqrt[]{n}\cos(nx_0)}{\displaystyle\lim_{n\to \infty}\sqrt[]{n}}=\displaystyle\frac{L}{\displaystyle\lim_{n\to \infty}\sqrt[]{n}}=0$。所以只需要证明 $\cos(nx_0)$ 不收敛到 $0$ 即可。

由二倍角公式，$\cos(2nx_0)=2\cos^2(nx_0)-1$。如果极限为 $0$，两边取极限得到 $0=-1$，这显然是不可能的！所以 $\cos(nx_0)$ 不收敛到 $0$，从而 $h_n'(x_0)$ 发散。

综上，$\left\{h_n'\right\}$ 对每个 $x \in \mathbb{R}$ 都是发散的。

<br/>

!!! question "练习 6.3.2"
    考虑由以下定义的函数序列

    \[
    {g}_{n}\left( x\right)  = \frac{{x}^{n}}{n}.
    \]

    (a) 证明 \(\left( {g}_{n}\right)\) 在 \(\left\lbrack  {0,1}\right\rbrack\) 上一致收敛，并求出 \(g = \lim {g}_{n}\) 。证明 \(g\) 可微，并计算所有 \(x \in  \left\lbrack  {0,1}\right\rbrack\) 的 \({g}^{\prime }\left( x\right)\) 。

    (b) 现在，证明 \(\left( {g}_{n}^{\prime }\right)\) 在 \(\left\lbrack  {0,1}\right\rbrack\) 上收敛。收敛是否一致？设 \(h = \lim {g}_{n}^{\prime }\) 并比较 \(h\) 和 \({g}^{\prime }\) 。它们是否相同？

(a)  令 $N>\displaystyle\frac{2}{\varepsilon}$，则对 $\forall\ m,n>N$，$\forall\ x\in [0,1]$，有 $\left|g_m(x)-g_n(x)\right|=\left|\displaystyle\frac{x^m}{m}-\displaystyle\frac{x^n}{n}\right|\leq \left|\displaystyle\frac{x^m}{m}\right|+\left|\displaystyle\frac{x^n}{n}\right|\leq \displaystyle\frac{1}{m}+\displaystyle\frac{1}{n}<\displaystyle\frac{2}{N}<\varepsilon$，所以 $\left\{g_n\right\}$ 在 $[0,1]$ 上一致收敛。

$g(x)=\displaystyle\lim_{n\to \infty}g_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x^n}{n}=0$。

$g'(x)=0$。

(b) 对 $\forall\ n\in \mathbb{N^+}$，由定义可求得 $g_n'(x)=x^{n-1}$。它不是一致收敛的， 得到的 $h(x)=\displaystyle\lim_{n\to \infty}g_n'(x)=\begin{cases}    0, \quad \text{if }x\in [0,1)\\    1, \quad \text{if }x=1\end{cases}$

可得出 $h(x)$ 与 $g'(x)$ 并不相同的结论。

<br/>

!!! question "练习 6.3.3"
    考虑函数序列

    \[
    {f}_{n}\left( x\right)  = \frac{x}{1 + n{x}^{2}}.
    \]

    练习6.2.4包含了一些关于如何证明 \(\left( {f}_{n}\right)\) 在 \(\mathbb{R}\) 上一致收敛的建议。复习或完成这个练习。

    现在，设 \(f = \lim {f}_{n}\) 。计算 \({f}_{n}^{\prime }\left( x\right)\) 并找出所有满足 \({f}^{\prime }\left( x\right)  = \lim {f}_{n}^{\prime }\left( x\right)\) 的 \(x\) 的值。

(a) $f_n'(x)=\displaystyle\frac{1-nx^2}{\left(1+nx^2\right)^2}$，对 $\forall\ n\in \mathbb{N^+}$，$f_n(x)$ 在 $\left(-\infty,-\displaystyle\frac{1}{\sqrt[]{n}}\right),\left(\displaystyle\frac{1}{\sqrt[]{n}},+\infty\right)$ 递减，在 $\left(-\displaystyle\frac{1}{\sqrt[]{n}},\displaystyle\frac{1}{\sqrt[]{n}}\right)$ 递增，所以最小值为 $f_n\left(-\displaystyle\frac{1}{\sqrt[]{n}}\right)=-\displaystyle\frac{1}{2\sqrt{n}}$，最大值为 $f_n\left(\displaystyle\frac{1}{\sqrt[]{n}}\right)=\displaystyle\frac{1}{2\sqrt{n}}$。

所以，令 $N>\displaystyle\frac{1}{\varepsilon^2}$，则对 $\forall\ m,n>N$，$\forall\ x\in \mathbb{R}$，$\left|f_m(x)-f_n(x)\right|\leq \displaystyle\frac{1}{2\sqrt{m}}+\displaystyle\frac{1}{2\sqrt{n}}<\varepsilon$。

所以 $\left\{f_n\right\}$ 在 $\mathbb{R}$ 上一致收敛。

计算得 $\displaystyle\lim_{n\to \infty}f_n(x)=0$。

(b) 当 $x\neq 0$ 时，$\displaystyle\lim_{n\to \infty}f_n'(x)=0$；当 $x=0$ 时，$\displaystyle\lim_{n\to \infty}f_n'(0)=1$。

所以 $f'(x)=\displaystyle\lim_{n\to \infty}f_n'(x)$ 的解集为 $\mathbb{R}\setminus\left\{0\right\}$。

<br/>

!!! question "练习 6.3.4"
    设

    \[
    {g}_{n}\left( x\right)  = \frac{{nx} + {x}^{2}}{2n},
    \]

    并设 \(g\left( x\right)  = \lim {g}_{n}\left( x\right)\) 。证明 \(g\) 在两种方式下可微:

    (a) 通过代数方法计算 \(g\left( x\right)\) ，取 \(n \rightarrow  \infty\) 的极限，然后求 \({g}^{\prime }\left( x\right)\) 。

    (b) 对每个 \(n \in  \mathbb{N}\) 计算 \({g}_{n}^{\prime }\left( x\right)\) ，并证明导数序列 \(\left( {g}_{n}^{\prime }\right)\) 在每个区间 \(\left\lbrack  {-M,M}\right\rbrack\) 上一致收敛。使用定理 6.3.3 得出结论 \({g}^{\prime }\left( x\right)  = \lim {g}_{n}^{\prime }\left( x\right)\) 。

    (c) 对序列 \({f}_{n}\left( x\right)  = \left( {n{x}^{2} + 1}\right) /\left( {{2n} + x}\right)\) 重复部分 (a) 和 (b)。

(a) $g(x)=\displaystyle\lim_{n\to \infty}g_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x+\displaystyle\frac{x^2}{n}}{2}=\displaystyle\frac{x}{2}$。

$g'(x)=\displaystyle\frac{1}{2}$。

(b) $g_n'(x)=\displaystyle\frac{n+2x}{2n}=\displaystyle\frac{1}{2}+\displaystyle\frac{x}{n}$。

令 $N>\displaystyle\frac{2M}{\varepsilon}$，则对 $\forall\ m,n>N$，$\forall\ x\in [-M,M]$，有 $\left|g_m'(x)-g_n'(x)\right|\leq \left|x\right|\left(\displaystyle\frac{1}{m}+\displaystyle\frac{1}{n}\right)<M\cdot\displaystyle\frac{2}{N}<\varepsilon$。

所以 $\left\{g_n'\right\}$ 在 $[-M,M]$ 上一致收敛。

又因为 $\displaystyle\lim_{n\to \infty}g_n(0)=0=g(0)$，所以由定理 6.3.3（原函数序列可微且单点收敛，导数序列一致收敛），$g'(x)=\displaystyle\lim_{n\to \infty}g_n'(x)=\displaystyle\frac{1}{2}$。

(c) $f(x)=\displaystyle\lim_{n\to \infty}f_n(x)=\displaystyle\frac{x^2}{2}$，$f'(x)=x$。

$f_n'(x)=\displaystyle\frac{nx^2+\left(2n\right)^2x-1}{\left(2n+x\right)^2}=\displaystyle\frac{4x+\displaystyle\frac{x^2}{n}-\displaystyle\frac{1}{n^2}}{\left(2+\displaystyle\frac{x}{n}\right)^2}$。

可以求得 $\displaystyle\lim_{n\to \infty}f_n'(x)=x$，且 $\left|f_n'(x)-x\right|=\left|\displaystyle\frac{\displaystyle\frac{3x^2}{n}+\displaystyle\frac{x^3+1}{n^2}}{\left(2+\displaystyle\frac{x}{n}\right)^2}\right|$。对任意 $\varepsilon>0$，令 $N>\max\left\{\displaystyle\frac{6M^2}{\varepsilon},\sqrt[]{\displaystyle\frac{2(M^3+1)}{\varepsilon}},M\right\}$，则对 $\forall\ n>N$，$x\in [-M,M]$，$\left|f_n'(x)-x\right|<\displaystyle\frac{3M^2}{n}+\displaystyle\frac{M^3+1}{n^2}<\varepsilon$。

所以 $\left\{f_n'\right\}$ 在 $[-M,M]$ 上一致收敛，得到 $f'(x)=\displaystyle\lim_{n\to \infty}f_n'(x)=x$。

<br/>

!!! question "练习 6.3.5"
    使用以下建议为定理 6.3.2 提供证明。首先，观察三角不等式意味着，对于任何 \(x \in\)  \(\left\lbrack  {a,b}\right\rbrack\) ，

    \[
    \left| {{f}_{n}\left( x\right)  - {f}_{m}\left( x\right) }\right|  \leq  \left| {\left( {{f}_{n}\left( x\right)  - {f}_{m}\left( x\right) }\right)  - \left( {{f}_{n}\left( {x}_{0}\right)  - {f}_{m}\left( {x}_{0}\right) }\right) }\right|  + \left| {{f}_{n}\left( {x}_{0}\right)  - {f}_{m}\left( {x}_{0}\right) }\right| .
    \]

    现在，将中值定理应用于 \({f}_{n} - {f}_{m}\) 。

由中值定理，$\exists\ \alpha\in (x_0,x)$ 或 $(x,x_0)$ 使得

$\left|f_n(x)-f_m(x)-\left(f_n(x_0)-f_m(x_0)\right)\right|=\left|x-x_0\right|\left|f_n'(\alpha)-f_m'(\alpha)\right|$。

由 $\left\{f_n'(x)\right\}$ 一致收敛，对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，对 $\forall\ m,n>N_1$，$\forall\ x\in [a,b]$，$\left|f_m'(x)-f_n'(x)\right|<\displaystyle\frac{\varepsilon}{2(b-a)}$。

又因为 $\left\{f_n(x)\right\}$ 在 $x_0$ 处收敛，所以对上述 $\varepsilon$，$\exists\ N_2\in \mathbb{N^+}$，对 $\forall\ m,n>N_2$，$\left|f_m(x_0)-f_n(x_0)\right|<\displaystyle\frac{\varepsilon}{2}$。

取 $N=\max\left\{N_1,N_2\right\}$，则对 $\forall\ m,n>N$，$\forall\ x\in [a,b]$，有

$$
\begin{align*}
    \left|f_m(x)-f_n(x)\right|&\leq \left|f_m(x)-f_n(x)-\left(f_m(x_0)-f_n(x_0)\right)\right|+\left|f_m(x_0)-f_n(x_0)\right|\\&=\left|x-x_0\right|\left|f_m'(\alpha)-f_n'(\alpha)\right|+\left|f_m(x_0)-f_n(x_0)\right|\\&<\left|x-x_0\right|\displaystyle\frac{\varepsilon}{2(b-a)}+\displaystyle\frac{\varepsilon}{2}\leq \varepsilon
\end{align*}
$$

所以 $\left\{f_n\right\}$ 在 $[a,b]$ 上一致收敛。

设 $f(x)=\displaystyle\lim_{n\to \infty}f_n(x)$，由定理 $6.3.1$ 可知 $f'(x)=\displaystyle\lim_{n\to \infty}f_n'(x)=g(x)$。

<br>

---

## 习题 6.4 函数级数

!!! question "练习 6.4.1"
    证明如果 $\sum_{n=1}^\infty g_n$ 一致收敛，则 $(g_n)$ 一致收敛于零。

应用函数一致收敛的 Cauchy 准则，得到对 $\forall\ \varepsilon$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>N$，$\left|\displaystyle\sum_{k=1}^{n}g_k(x)-\displaystyle\sum_{k=1}^{n-1}g_k(x)\right|=\left|g_n(x)\right|<\varepsilon$。所以 $\left\{g_n\right\}$ 一致收敛于 $0$。

<br/>

!!! question "练习 6.4.2"
    提供 Weierstrass M-判别法 (推论 6.4.5) 证明的细节。

若 $\displaystyle\sum_{n=1}^{\infty}M_n$ 收敛，由级数的 Cauchy 准则，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>m>N$，有 $\left|M_{m+1} + M_{m+2} + \cdots + M_n\right| < \varepsilon$。

因为 $\left|f_n(x)\right|\leq M_n$，所以 

$$\begin{align*}
    \left|f_{m+1}(x) + f_{m+2}(x) + \cdots + f_n(x)\right| &\leq \left|f_{m+1}(x)\right|+\left|f_{m+2}(x)\right|+\cdots+\left|f_n(x)\right|\\&\leq \left|M_{m+1} + M_{m+2} + \cdots + M_n\right| \\&< \varepsilon
\end{align*}$$

所以 $\displaystyle\sum_{n=1}^{\infty} f_n(x)$ 在 $A$ 上一致收敛。

<br/>

!!! question "练习 6.4.3"
    (a) 证明 $g(x) = \sum_{n=1}^\infty \frac{\cos(2^n x)}{2^n}$ 在整个 $\mathbb{R}$ 上连续。
    (b) 证明 $h(x) = \sum_{n=1}^\infty \frac{x^n}{n^2}$ 在 $[-1, 1]$ 上连续。

(a) 因为 $\left|\frac{\cos(2^n x)}{2^n}\right| \leq \frac{1}{2^n}$，所以使用 Weierstrass M-判别法。

对 $\forall\ \varepsilon>0$，取 $N>\log_2{\displaystyle\frac{1}{\varepsilon}+1}$，则对 $\forall\ n>N$，$\displaystyle\frac{1}{2^{n}}<\varepsilon$。

所以对 $\forall\ x\in \mathbb{R}$，$\forall\ n>m>N$，有

$$
\left|\displaystyle\sum_{i=m+1}^{n}\frac{\cos(2^i x)}{2^i}\right| \leq \sum_{i=m+1}^{n} \frac{1}{2^i} < \displaystyle\frac{1}{2^m}<\varepsilon
$$

所以 $\left\{\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{\cos(2^nx)}{2^n}\right\}$ 在 $\mathbb{R}$ 上一致收敛。又因为 $\displaystyle\sum_{n=1}^{m}\displaystyle\frac{\cos(2^nx)}{2^n}$ 对 $\forall\ m\in \mathbb{N^+}$ 都连续，所以 $g$ 在 $\mathbb{R}$ 上连续。

(b) 因为 $x\in [-1,1]$ 时，$\left|x^n\right|\leq 1$，所以 $\left|\displaystyle\frac{x^n}{n^2}\right|\leq \displaystyle\frac{1}{n^2}$。

因为 $\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{1}{n^2}$ 收敛，所以同上题，使用 Weierstrass M-判别法，$h$ 在 $[-1,1]$ 上连续。

<br/>

!!! question "练习 6.4.4"
    在第 5.4 节中，我们推迟了关于无处可微函数
    $$g(x) = \sum_{n=0}^\infty \frac{1}{2^n} h(2^n x)$$
    在 $\mathbb{R}$ 上连续的论证。使用 Weierstrass M-判别法来补充缺失的证明。

由 $\left|\displaystyle\frac{1}{2^n}h(2^nx)\right|\leq \displaystyle\frac{1}{2^n}$ 同上题证明。

<br/>

!!! question "练习 6.4.5"
    设
    $$f(x) = \sum_{k=1}^\infty \frac{\sin(kx)}{k^3}$$
    (a) 证明 $f(x)$ 是可微的，并且导数 $f'(x)$ 是连续的。
    (b) 我们能否确定 $f$ 是否二次可微？

(a) 令 $g_k(x)=\displaystyle\frac{\sin(kx)}{k^3}$，则 $f(x)=\displaystyle\sum_{k=1}^{\infty}g_k(x)$。

由 Weierstrass M-判别法，同前几题可得 $\left\{\displaystyle\sum_{k=1}^{\infty} g_k\right\}$ 在 $\mathbb{R}$ 上一致收敛，所以 $f$ 在 $\mathbb{R}$ 上连续。

而 $\left|g_k'(x)\right|=\left|\displaystyle\frac{\cos(kx)}{k^2}\right|\leq \displaystyle\frac{1}{k^2}$，同理也可得 $\left\{\displaystyle\sum_{k=1}^{\infty}g_k'(x)\right\}$ 在 $\mathbb{R}$ 上一致收敛，所以 $f$ 可微且 $f'(x)=\displaystyle\sum_{k=1}^{\infty}g_k'(x)$。又因为 $g_k'(x)$ 连续，所以 $f'(x)$ 连续。

(b) 因为 $\left|g_k''(x)\right|=\left|-\displaystyle\frac{\sin(kx)}{k}\right|\leq \displaystyle\frac{1}{k}$，而 $\displaystyle\sum_{k=1}^{\infty}\displaystyle\frac{1}{k}$ 发散，所以无法使用 Weierstrass M-判别法来证明 $f$ 二次可微。

<br/>

!!! question "练习 6.4.6"
    观察级数
    $$f(x) = \sum_{n=1}^\infty \frac{x^n}{n} = x + \frac{x^2}{2} + \frac{x^3}{3} + \frac{x^4}{4} + \cdots$$
    对于半开区间 $[0, 1)$ 中的每一个 $x$ 都收敛，但在 $x = 1$ 时不收敛。对于固定的 $x_0 \in (0, 1)$，解释我们如何仍然可以使用 Weierstrass M-判别法 (Weierstrass M-Test) 来证明 $f$ 在 $x_0$ 处连续。

**注：解答较为繁琐，用 $\displaystyle\frac{x^n}{n}\leq x^n$ 放缩成几何级数可大幅简化证明**

如果直接将分子化为 $1$，则 $f(x)\leq \displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{1}{n}$，但调和级数并不收敛，不能直接使用 Weierstrass M-判别法。

所以分子必须做其他处理。如果小于某个常数，常数乘上调和级数还是不会收敛。因为 $\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{1}{n^p}$ 在 $p>1$ 时收敛，所以可以令 $x_0^n<\displaystyle\frac{1}{n^k}(k>0)$，使得 $\displaystyle\frac{x_0^n}{n}<\displaystyle\frac{1}{n^{1+k}}$，这样就化成了一个收敛的级数。

令 $x_0^n<\displaystyle\frac{1}{n}$，得到 $\left(\displaystyle\frac{1}{n}\right)^{\frac{1}{n}}>x_0$，我们讨论是否能找到这样的 $n$。

令 $g(x)=\left(\displaystyle\frac{1}{x}\right)^{\frac{1}{x}}=\mathrm{e}^{\frac{1}{x}\ln\left(\frac{1}{x}\right)}$，则 $\displaystyle\lim_{x\to +\infty} \displaystyle\frac{\ln\left(\frac{1}{x}\right)}{x}=\displaystyle\lim_{x\to +\infty}\displaystyle\frac{-\frac{1}{x^2}}{\frac{1}{x}}=\displaystyle\lim_{x\to +\infty}-\displaystyle\frac{1}{x}=0$。所以得到 $\displaystyle\lim_{x\to +\infty}g(x)=1$。

所以 $\displaystyle\lim_{n\to \infty}g(n)=1$，即对 $\forall\ \varepsilon=1-x_0>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>N$，$\left|g(n)-1\right|<\varepsilon$ $\Rightarrow$ $g(n)>1-\varepsilon=x_0$。

所以对 $\forall\ n>N$，$\displaystyle\frac{x^n}{n}<\displaystyle\frac{1}{n^2}$，$f(x_0)<\displaystyle\sum_{n=1}^{N}\displaystyle\frac{x_0^n}{n}+\displaystyle\sum_{n=N+1}^{\infty}\displaystyle\frac{1}{n^2}$。因为右侧级数收敛，所以由 Weierstrass M-判别法，$f$ 在 $x_0$ 处收敛。又因为 $\displaystyle\frac{x^n}{n}$ 在 $x_0$ 处连续，所以 $f$ 在 $x_0$ 处连续。

<br/>

!!! question "练习 6.4.7"
    设
    $$h(x) = \sum_{n=1}^\infty \frac{1}{x^2+n^2}$$
    (a) 证明 $h$ 是定义在 $\mathbb{R}$ 上的连续函数。
    (b) $h$ 是否可微？如果是，导数函数 $h'$ 是否连续？

令 $g_n(x)=\displaystyle\frac{1}{x^2+n^2}$,则 $h(x)=\displaystyle\sum_{n=1}^{\infty}g_n(x)$。

(a) 因为 $\left|\displaystyle\frac{1}{x^2+n^2}\right|\leq \displaystyle\frac{1}{n^2}$，所以使用 Weierstrass M-判别法，$h$ 在 $\mathbb{R}$ 上连续。

(b) 因为 $g_n'(x)=-\displaystyle\frac{2x}{\left(x^2+n^2\right)^2}$，考虑把分子上的 $x$ 消掉。

考察 $(x^2+n^2)(x^2+n^2)\geq x^2n^2$，故有 $\left|g_n'(x)\right|\leq \displaystyle\frac{2}{\left|x\right| n^2}$，但在 $\left|x\right|<1$ 时右侧难以控制，所以分开讨论：

$\left|x\right|<1$ 时，$\left|g_n'(x)\right|\leq \displaystyle\frac{2}{\left(x^2+n^2\right)^2}\leq \displaystyle\frac{2}{n^2}$；$\left|x\right|\geq 1$ 时，$\left|g_n'(x)\right|\leq \displaystyle\frac{2}{\left|x\right|n^2}\leq \displaystyle\frac{2}{n^2}$。

所以 $\left|g_n'(x)\right|\leq \displaystyle\frac{2}{n^2}$，由 Weierstrass M-判别法，$\left\{\displaystyle\sum_{n=1}^{\infty}g_n'\right\}$ 一致收敛。又 $\left\{\displaystyle\sum_{n=1}^{\infty}g_n\right\}$ 一致收敛，所以 $h$ 可微且 $h'(x)=\displaystyle\sum_{n=1}^{\infty}g_n'(x)$。又因为 $g_n'(x)$ 连续，所以 $h'(x)$ 连续。

<br/>

!!! question "练习 6.4.8"
    令 $\{r_1, r_2, r_3, \dots\}$ 是有理数集的一个枚举。对于每个 $r_n \in \mathbb{Q}$，定义
    $$u_n(x) = \begin{cases} 1/2^n & \text{若 } x > r_n \\ 0 & \text{若 } x \le r_n \end{cases}$$
    现在，令 $h(x) = \sum_{n=1}^\infty u_n(x)$。证明 $h$ 是定义在整个 $\mathbb{R}$ 上的单调函数，并且在每个有理点都不连续。

首先说明 $h(x)$ 一致收敛。因为 $\left|u_n(x)\right|\leq \displaystyle\frac{1}{2^n}$，所以使用 Weierstrass M-判别法，$\displaystyle\sum_{n=1}^{\infty}u_n(x)$ 一致收敛。

对 $\forall\ x_1<x_2$，若 $r_n< x_1<x_2$，则 $u_n(x_1)=\displaystyle\frac{1}{2^n}=u_n(x_2)$；若 $x_1\leq r_n<x_2$，则 $u_n(x_1)=0<u_n(x_2)=\displaystyle\frac{1}{2^n}$；若 $x_1<x_2\leq r_n$，则 $u_n(x_1)=0=u_n(x_2)$。

所以对 $\forall\ n\in \mathbb{N^+}$，$u_n(x_1)\leq u_n(x_2)$。所以 $h(x_1)=\displaystyle\sum_{n=1}^{\infty}u_n(x_1)\leq \displaystyle\sum_{n=1}^{\infty}u_n(x_2)=h(x_2)$，所以 $h$ 单调递增。

对 $\forall\ n\in \mathbb{N^+}$，$h(r_n)=\displaystyle\sum_{r_i<r_n}u_i(r_n)+\displaystyle\sum_{r_i\geq r_n}u_i(r_n)=\displaystyle\sum_{r_i<r_n}\displaystyle\frac{1}{2^i}$，而对 $\forall\ x>r_n$，$h(x)=\displaystyle\sum_{r_i<x}\displaystyle\frac{1}{2^i}\geq \displaystyle\sum_{r_i<r_n}\displaystyle\frac{1}{2^i}+u_n(x)=h(r_n)+\displaystyle\frac{1}{2^n}$。即 $\exists\ \varepsilon=\displaystyle\frac{1}{2^n}>0$，对 $\forall\ \delta>0$，$\exists\ x\in V_\delta(r_n)$，使得 $\left|h(x)-h(r_n)\right|\geq \varepsilon$，所以 $h$ 在 $r_n$ 处不连续。

综上，$h(x)$ 在每个有理点都不连续。

<br/>

---

## 习题 6.5 幂级数

!!! question "练习 6.5.1"
    考虑由幂级数定义的函数 $g$
    
    $$
    g\left( x\right)  = x - \frac{{x}^{2}}{2} + \frac{{x}^{3}}{3} - \frac{{x}^{4}}{4} + \frac{{x}^{5}}{5} - \cdots .
    $$
    
    (a) $g$ 在 $(-1,1)$ 上定义吗？它在这个集合上连续吗？ $g$ 在 $( - 1,1]$ 上定义吗？它在这个集合上连续吗？在 $\left\lbrack  {-1,1}\right\rbrack$ 上会发生什么？ $g\left( x\right)$ 的幂级数是否可能在其他点 $\left| x\right|  > 1$ 上收敛？请解释。
    
    (b) 对于哪些 $x$ 的值， ${g}^{\prime }\left( x\right)$ 有定义？求 ${g}^{\prime }$ 的公式。

(a) 因为 $g(1)=\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{(-1)^{n+1}}{n}$ 是收敛的，所以 $g$ 在 $(-1,1)$ 上绝对收敛，进而在该区间的任意紧子集上一致收敛。所以 $g$ 在 $(-1,1)$ 上定义且连续。

由 Abel 定理， $g$ 在 $(-1,1]$ 上定义且连续。

因为 $g(-1)=\displaystyle\sum_{n=1}^{\infty}-\displaystyle\frac{1}{n}$ 是发散的，所以在 $[-1,1]$ 并不完全定义与连续。

因为若 $g(x)=\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{(-1)^{n+1}}{n}x^n$ 收敛，则必然有 $\displaystyle\frac{(-1)^{n+1}}{n}x^n\to 0$，所以 $g(x)$ 的幂级数并不可能在 $\left|x\right|>1$ 处收敛。

(b) $g'(x)=\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}x^{n-1}$，它在 $x=1$ 处是发散的，所以只在 $(-1,1)$ 上有定义。

<br/>

!!! question "练习 6.5.2"
    找到合适的系数 $\left( {a}_{n}\right)$ ，使得生成幂级数 $\sum {a}_{n}{x}^{n}$
    
    (a) 对所有 $x \in  \left\lbrack  {-1,1}\right\rbrack$ 绝对收敛，并在此集合外发散；
    
    (b) 在 $x =  - 1$ 处条件收敛，在 $x = 1$ 处发散；
    
    (c) 在 $x =  - 1$ 和 $x = 1$ 处都条件收敛。
    
    (d) 是否有可能找到一个幂级数的例子，它在 $x =  - 1$ 处条件收敛，在 $x = 1$ 处绝对收敛？

(a) $a_n=\displaystyle\frac{1}{2(n+1)^2}$，$\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{x^n}{2(n+1)^2}$ 在 $[-1,1]$ 上绝对收敛，而在 $\left|x\right|>1$ 上由于指数函数大于多项式的增长率从而发散。

(b) $a_n=\displaystyle\frac{1}{n+1}$，这样 $x=-1$ 时级数为 $\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{(-1)^n}{n+1}$ 是收敛的，而 $x=1$ 是 $\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{1}{n+1}$ 调和级数，从而发散。

(c) 我们需要找到原级数 $\sum a_n$ 和交错级数 $\sum (-1)^{n}a_n$ 都条件收敛的 $a_n$。条件收敛的级数很多情况下都是交错级数，但是交错级数再交错一次就会失效，所以我们要想一种办法，使 $(-1)^n$ 不影响原有级数的交错性。

一种可能的思路是，考虑在 $n=2k$ 上交错，$n=2k+1$ 上完全取 $0$ 的级数，这样就能避免 $(-1)^n$ 带来的影响：

$$
a_n=\begin{cases}
    \displaystyle\frac{(-1)^k}{n+1} \quad &\text{if }n=2k, k\in \mathbb{N}\\
    0 \quad &\text{if }n=2k+1, k\in \mathbb{N}
\end{cases}
$$

(d) 这是不可能的。事实上，在 $x=R$ 上绝对收敛的幂级数在 $[-R,R]$ 上均绝对收敛。这是因为对 $\forall\ x\in [-R,R]$，有 $\left|a_nx^n\right|\leq \left|a_nR^n\right|$，而 $\displaystyle\sum_{n=0}^{\infty}\left|a_nR^n\right|$ 收敛，由 Weierstrass M-判别法，得到 $\displaystyle\sum_{n=0}^{\infty}\left|a_nx^n\right|$ 也收敛。

<br/>

!!! question "练习 6.5.3"
    解释为什么幂级数最多只能在两个点上条件收敛。

若幂级数 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $x=R$ 处条件收敛，则它必然在 $(-\left|R\right|,\left|R\right|)$ 上绝对收敛。考虑条件收敛的第二点 $C$：若 $\left|C\right|>\left|R\right|$，则幂级数在 $R\in \left(-\left|C\right|,\left|C\right|\right)$ 上绝对收敛，矛盾；若 $\left|C\right|<\left|R\right|$，则幂级数在 $C\in \left(-\left|R\right|,\left|R\right|\right)$ 上也绝对收敛，矛盾。所以只有可能是 $\left|C\right|=\left|R\right|$ 即 $C=-R$。

所以幂级数最多只能在两个点上条件收敛，即收敛半径的两个端点。

<br/>

!!! question "练习 6.5.4"
    (a) 通过引用适当的定理，详细论证在区间(-R, R)上收敛的幂级数必然在每个点 $x \in  \left( {-R,R}\right)$ 上表示一个连续函数。
    
    (b) 如果级数在端点 $x = R$ 上收敛，指出我们如何知道连续性扩展到集合 $(-R,R]$ 。

对 $\forall\ x\in (-R,R)$，$\exists\ t\in (-R,R)$ 使得 $\left|x\right|<\left|t\right|$。因为幂级数在 $t$ 处收敛，所以必在 $(-\left|t\right|,\left|t\right|)$ 上绝对收敛，从而在 $x$ 处绝对收敛。<mark>（$R$ 处收敛 $\Rightarrow$ $(-R,R)$ 绝对收敛）</mark>

又存在 $\left|x\right|<\left|u\right|<\left|t\right|$，幂级数在 $u$ 处绝对收敛，所以幂级数在 $[-\left|u\right|,\left|u\right|]$ 上一致收敛。<mark>（$R$ 处绝对收敛 $\Rightarrow$ $[-R,R]$ 上一致收敛）</mark>

又因为 $\displaystyle\sum_{n=0}^{m}a_nx^n$ 是连续函数，所以 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $[-\left|u\right|,\left|u\right|]$ 上连续，即在 $x\in [-\left|u\right|,\left|u\right|]$ 处连续。<mark>（$[-R,R]$ 上一致收敛且函数序列连续 $\Rightarrow$ $[-R,R]$ 上连续）</mark>

(b) 因为一致收敛与连续性往往挂钩，我们考虑证明幂级数在 $[0,R]$（下界不是 $0$ 也可以）上一致收敛来证明在 $R$ 处连续。

对 $\forall\ x\in [0,R]$，$\left|\displaystyle\sum_{i=m+1}^{n}a_ix^i\right|=\left|\displaystyle\sum_{i=m+1}^{n}(a_iR^i)\left(\displaystyle\frac{x}{R}\right)^{i}\right|$，将其转化成 $R$ 处收敛的序列来估计大小。

因为幂级数在 $R$ 处收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>m>N$，$\left|\displaystyle\sum_{i=m+1}^{n}a_iR^i\right|<\varepsilon$。

所以有

$$
\begin{align*}
    \left|\displaystyle\sum_{i=m+1}^{n}a_ix^i\right|&=\left|\displaystyle\sum_{i=m+1}^{n}\left(a_iR^i\right)\left(\displaystyle\frac{x}{R}\right)^i\right|\\
    &\leq2\varepsilon\left(\displaystyle\frac{x}{R}\right)^{m+1}<2\varepsilon
\end{align*}
$$
<mark>（Abel 判别法）</mark>

所以 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $[0,R]$ 上一致收敛，从而在 $R$ 处连续。

<mark> Abel 判别法是比一般绝对值不等式更精确的估计方法。</mark>

<br/>

!!! question "练习 6.5.5"
    使用Weierstrass M-判别法证明定理 6.5.2：
    
    如果幂级数 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $x_0$ 处绝对收敛，则其在闭区间 $[-\left|x_0\right|,\left|x_0\right|]$ 上一致收敛。

若幂级数在 $x_0$ 处绝对收敛，则对 $\forall\ x\in [-\left|x_0\right|,\left|x_0\right|]$，$\left|a_nx^n\right|\leq \left|a_nx_0^n\right|$。因为 $\displaystyle\sum_{n=0}^{\infty}\left|a_nx_0^n\right|$ 收敛，由 Weierstrass M-判别法，$\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 一致收敛。

<mark> 事实上得出的是 $\sum\left|a_nx^n\right|$ 一致收敛的结论，所以幂级数在这个区间上也是绝对收敛的。</mark>

<br/>

!!! question "练习 6.5.6"
    展示定理 6.5.1、定理 6.5.2 和 Abel 定理如何共同暗示，如果幂级数在紧集上逐点收敛，那么收敛实际上在该集上是一致的。

设幂级数在紧集 $K$ 上逐点收敛。

因紧集有界，设其上下确界分别为 $m,n$，则 $m,n\in K$。所以幂级数在 $m,n$ 处收敛。

如果 $m=n$，则 $K$ 为单点紧集，幂级数在 $K$ 上一致收敛。

若 $m>n$，不妨假设 $m>0>n$（其他的情况可用类似的方法证明），由 Abel 定理，幂级数在 $[0,m]$，$[n,0]$ 上均一致收敛。下面证明它们的并集一致收敛即可。

因为幂级数在 $[0,m]$ 上一致收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，对 $\forall\ m,n>N_1$，$\forall\ x\in [0,m]$，有 $\left|\displaystyle\sum_{i=m+1}^{n}a_nx^n\right|<\varepsilon$。同理在 $[n,0]$ 上也存在相应的 $N_2\in \mathbb{N^+}$。

现在取 $N=\max\left\{N_1,N_2\right\}$，则对 $\forall\ m,n>N$，$\forall\ x\in [n,m]$，都有 $\left|\displaystyle\sum_{i=m+1}^{n}a_nx^n\right|<\varepsilon$。所以幂级数在 $[n,m]$ 上一致收敛。

又因为 $K\subseteq [n,m]$，所以幂级数在 $K$ 上一致收敛。

<br/>

!!! question "练习 6.5.7"
    (a) 比值判别法(来自练习 2.7.9)指出，如果 $\left( {b}_{n}\right)$ 是一个满足 $\lim \left| {{b}_{n + 1}/{b}_{n}}\right|  = r < 1$ 的非零项序列，那么级数 $\sum {b}_{n}$ 收敛。利用这一点来论证，如果 $s$ 满足 $0 < s < 1$ ，那么 $n{s}^{n - 1}$ 对所有 $n \geq  1$ 都是有界的。
    
    (b) 给定任意 $x \in  \left( {-R,R}\right)$ ，选择 $t$ 以满足 $\left| x\right|  < t < R$ 。利用观察
    
    $$
    \left| {n{a}_{n}{x}^{n - 1}}\right|  = \frac{1}{t}\left( {n\left| \frac{{x}^{n - 1}}{{t}^{n - 1}}\right| }\right) \left| {{a}_{n}{t}^{n}}\right|
    $$
    
    为定理6.5.6构建一个证明。

(a) 考虑式子 $\displaystyle\frac{(n+1)s^n}{ns^{n-1}}=\displaystyle\frac{n+1}{n}s$，当 $n\to \infty$ 时，$\displaystyle\frac{n+1}{n}s\to s<1$，所以 $\displaystyle\sum_{n=1}^{\infty}ns^{n-1}$ 收敛，从而 $ns^{n-1}\to 0$，所以 $ns^{n-1}$ 是有界的。

(b) 分析式子 $\left|na_nx^{t-1}\right|=\displaystyle\frac{1}{t}\left|a_nt^n\right|\left(n\left|\displaystyle\frac{x}{t}\right|^{n-1}\right)$。一方面，因为 $\left|x\right|<t$，所以 $\displaystyle\sum_{n=1}^{\infty}n\left|\displaystyle\frac{x}{t}\right|^{n-1}$ 是收敛的；另一方面，$\displaystyle\sum_{n=1}^{\infty}\left|a_nt^n\right|$ 本身也是收敛的，所以 $\displaystyle\sum_{n=1}^{\infty}\left|na_nx^{t-1}\right|$ 收敛。从而证明了微分级数的收敛性。

<br/>

!!! question "练习 6.5.8"
    设 $\sum {a}_{n}{x}^{n}$ 为一个幂级数，且 ${a}_{n} \neq  0$ ，并假设
    
    $$
    L = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left| \frac{{a}_{n + 1}}{{a}_{n}}\right|
    $$
    
    存在。
    
    (a) 证明如果 $L \neq  0$ ，则该级数对所有 $x$ 在 $\left( {-1/L,1/L}\right)$ 中收敛。(练习2.7.9中的建议可能有所帮助。)
    
    (b) 证明如果 $L = 0$ ，则该级数对所有 $x \in  \mathbb{R}$ 收敛。
    
    (c) 证明如果 $L$ 被极限替换，(a)和(b)仍然成立。
    
    $$
    {L}^{\prime } = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{n}\;\text{ where }\;{s}_{n} = \sup \left\{  {\left| \frac{{a}_{k + 1}}{{a}_{k}}\right|  : k \geq  n}\right\}  .
    $$
    
    值 ${L}^{\prime }$ 被称为序列 $\left| {{a}_{n + 1}/{a}_{n}}\right|$ 的“上极限”或“lim sup”。当且仅当序列有界时，它存在(练习 2.4.6)。
    
    (d) 证明如果 $\left| {{a}_{n + 1}/{a}_{n}}\right|$ 无界，则原级数 $\sum {a}_{n}{x}^{n}$ 仅在 $x = 0$ 时收敛。

(a) 这里仍然需要利用 $x$ 的范围来抵消 $a_n$ 带来的影响。考虑如下的式子：

$\left|\displaystyle\frac{a_{n+1}x^{n+1}}{a_nx^n}\right|=\left|\displaystyle\frac{a_{n+1}}{a_n}\right|\left|x\right|$。当 $\left|x\right|<\displaystyle\frac{1}{L}$ 时（由绝对值极限的性质可知 $L>0$），得 $\displaystyle\lim_{n\to \infty}\left|\displaystyle\frac{a_{n+1}x^{n+1}}{a_nx^n}\right|<1$，所以 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 收敛。

(b) 这里的步骤是同上的，只不过因为 $\displaystyle\lim_{n\to \infty}\left|\displaystyle\frac{a_{n+1}}{a_n}\right|=0$ 而使得 $x$ 任意取值都不会改变极限的结果，所以 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 对 $\forall\ x\in \mathbb{R}$ 收敛。

(c) 对固定的 $x$，有 $\sup (b_n\cdot x)=x\sup b_n$（使用上确界的性质证明）。我们用这个式子把 $x$ 嵌进上确界的代数式中。

$\left|x\right|s_n=\sup \left\{\left|\displaystyle\frac{a_{k+1}x^{k+1}}{a_{k}x^k}\right|:k\geq n\right\}\geq \left|\displaystyle\frac{a_{n+1}x^{n+1}}{a_{n}x^n}\right|$。

所以 $\left|x\right|L'=\displaystyle\lim_{n\to \infty}\left|x\right|s_n\geq \displaystyle\lim_{n\to \infty}\left|\displaystyle\frac{a_{n+1}x^{n+1}}{a_{n}x^n}\right|$，这样就把这个式子化成了 (a)、(b) 问完全一样的形式。

所以得证。

(d) <mark style="background-color: red; color: white;"> 事实上这道题的结论是错误的。 </mark> 
直接推导的话，我们只能得出 $x\neq 0$ 时 $\sum \displaystyle\frac{a_{n+1}x^{n+1}}{a_nx^n}$ 是发散的，但这并不意味着 $\sum a_nx^n$ 本身就是发散的。

事实上，如果限定了 $\left|a_n\right|$ 的上界，即使 $\left|\displaystyle\frac{a_{n+1}}{a_n}\right|$ 是无界的，同样可以构造出在 $x\neq 0$ 时收敛的幂级数：（$k\in \mathbb{N^+}$）

$$
a_n=\begin{cases}
    1, \quad \text{if }n=2k-1\\
    \displaystyle\frac{1}{10^k}, \quad \text{if }n=2k\\
\end{cases}
$$

<br/>

!!! question "练习 6.5.9"
    使用定理 6.5.7 论证幂级数是唯一的。如果我们有
    
    $$
    \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n} = \mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n}
    $$
    
    对于所有在区间 $(-R, R)$ 内的 $x$ ，证明对于所有 $n = 0,1,2,\ldots$ ， ${a}_{n} = {b}_{n}$ 成立。(首先证明 ${a}_{0} = {b}_{0}$ 。)

令 $g_1(x)=\displaystyle\sum_{n=0}^{\infty}a_nx^n$，$g_2(x)=\displaystyle\sum_{n=0}^{\infty}b_nx^n$，则 $g_1(x)=g_2(x)$ 对 $\forall\ x\in (-R,R)$ 成立。

因为 $g_1(0)=a_0$，$g_2(0)=b_0$，所以 $a_0=b_0$。

因为原函数相等，所以 $g_1'(x)=g_2'(x)$ 对 $\forall\ x\in (-R,R)$ 成立，即 $\displaystyle\sum_{n=1}^{\infty}na_nx^{n-1}=\displaystyle\sum_{n=1}^{\infty}nb_nx^{n-1}$。

所以 $g_1'(0)=g_2'(0)$，即 $a_1=b_1$。

同理，因为幂级数是任意阶可导的，所以重复上述步骤，对 $\forall\ n\in \mathbb{N}$，都有 $a_n=b_n$。

<br/>

!!! question "练习 6.5.10"
    回顾第2.8节中关于级数乘积和Cauchy乘积的定义和结果。在第2.9节的末尾，我们提到了以下结果:如果 $\sum {a}_{n}$ 和 $\sum {b}_{n}$ 分别条件收敛于 $A$ 和 $B$ ，那么Cauchy乘积有可能发散。
    
    $$
    \sum {d}_{n}\;\text{ where }\;{d}_{n} = {a}_{0}{b}_{n} + {a}_{1}{b}_{n - 1} + \cdots  + {a}_{n}{b}_{0},
    $$
    
    然而，如果 $\sum {d}_{n}$ 确实收敛，那么它必须收敛于 ${AB}$ 。为了证明这一点，设
    
    $$
    f\left( x\right)  = \sum {a}_{n}{x}^{n},\;g\left( x\right)  = \sum {b}_{n}{x}^{n},\;\text{ and }\;h\left( x\right)  = \sum {d}_{n}{x}^{n}.
    $$
    
    使用 Abel定理 和练习2.8.8中的结果来建立这一结论。

标红的地方为错解，实际上右边还有许多余项。

<mark style="background-color: red;">考察有限项下的情形：$\left(\displaystyle\sum_{i=0}^{n}a_ix^i\right)\left(\displaystyle\sum_{i=0}^{n}b_ix^i\right)=\left(\displaystyle\sum_{i=0}^{2n}d_ix^i\right)$。 </mark>

由幂级数的性质，因为 $f(1),g(1),h(1)$ 都收敛，所以由 Abel 定理，$f(x),g(x),h(x)$ 在 $[0,1]$ 上一致收敛，同时在 $(-1,1)$ 上绝对收敛。<mark>（这保证了级数的项可以重排）</mark>

因此在 $x\in (-1,1)$ 时，
$$
\begin{align*}
    f(x)g(x)&=(a_0+a_1x+a_2x^2+\cdots)(b_0+b_1x+b_2x^2+\cdots)\\
    &=(a_0b_0)+(a_0b_1+a_1b_0)x+(a_0b_2+a_1b_1+a_2b_0)x^2+\cdots\\
    &=d_0+d_1x+d_2x^2+\cdots\\
    &=h(x)
\end{align*}
$$

又因为 $f(x),g(x),h(x)$ 在 $[0,1]$ 上一致收敛，所以均在 $[0,1]$ 上连续。所以有 $h(1)=\displaystyle\lim_{x\to 1^-}h(x)=\displaystyle\lim_{x\to 1^-}f(x)g(x)=f(1)g(1)=AB$。

<br/>

!!! question "练习 6.5.11"
    如果幂级数
    
    $$
    f\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}
    $$
    
    对所有 $x \in  [ 0,1)$ 和 $L = \mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}f\left( x\right)$ 收敛，则级数 $\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}$ 被称为 Abel-可求和 于 $L$。（即不需要本身收敛）
    
    (a) 证明任何收敛到极限 $L$ 的级数也是 Abel-可求和 到 $L$ 。
    
    (b) 证明 $\mathop{\sum }\limits_{{n = 0}}^{\infty }{\left( -1\right) }^{n}$ 是 Abel-可求和 的，并求出其和。

(a) 若级数收敛于 $L$，则 $f(1)=L$，由 Abel 定理可得其在 $[0,1]$ 上一致收敛，所以 $f(x)$ 在 $[0,1]$ 上连续，有 $\displaystyle\lim_{x\to 1^-}f(x)=f(1)=L$，这就证明了级数 Abel-可求和 于 $L$。

(b) 令 $f(x)=\displaystyle\sum_{n=0}^{\infty}(-1)^nx^n$，则 $x\in [0,1)$ 时，$(-1)^nx^n\leq x^n$，由 Weierstrass M-判别法可知 $f(x)$ 收敛，同时也能得出 $f(x)$ 在 $[0,1)$ 上绝对收敛，任意紧子集上一致收敛，所以 $f(x)$ 在 $[0,1)$ 上连续。

这里的求和我没注意到！事实上 $f(x)=\displaystyle\sum_{n=0}^{\infty}(-x)^n=\displaystyle\lim_{n\to \infty}\displaystyle\frac{1-(-x)^{n+1}}{1-(-x)}=\displaystyle\frac{1}{1+x}$ 在 $[0,1)$ 上连续！所以

Abel-可求和 的和为 $\displaystyle\lim_{x\to 1^-}f(x)=\displaystyle\lim_{x\to 1^-}\displaystyle\frac{1}{1+x}=\displaystyle\frac{1}{2}$。

<br/>

!!! question "练习 6.5.12"
    考虑分支过程开篇讨论中的函数 $G$ ，并回想概率的递增单调序列 $\left( {d}_{r}\right)$ 有一个满足 $G\left( d\right)  = d$ 的极限 $d = \lim {d}_{r}$ 。假设我们处于有两个固定点的情况: $G\left( 1\right)  = 1$ 和另一个满足 $G\left( {d}_{0}\right)  = {d}_{0}$ 的值 $0 < {d}_{0} < 1$ 。阐述为什么序列 $\left( {d}_{r}\right)$ 必然收敛到值 $d = {d}_{0}$ 而不是 $d = 1$ 的理由。

利用 Abel 定理，我们可以得出 $G(x)$ 在 $[0,1]$ 上连续的结论。同时因为 $G(1)$ 实际上是绝对收敛的，所以 $G(x)$ 在 $[0,1]$ 上一致收敛。

所以可以得出 $\displaystyle\lim_{r\to \infty}G(d_r)=G(d)=\displaystyle\lim_{r\to \infty}d_{r+1}=d$ 的结论。

不仅如此，$G(x)$ 的任意阶导数都是恒大于 $0$ 的，这为我们分析函数的性质起到了很大帮助。事实上，我们想知道有两个不动点对 $G$ 来说究竟意味着什么。

考察函数 $f(x)=G(x)-x$，则 $f(d_0)=f(1)=0$。由 $f'(x)=G'(x)-1$ 可知导函数的值是递增的。又由罗尔中值定理，$\exists\ c\in (d_0,1)$ 使得 $f'(c)=0$，所以我们得到结论：$f(x)$ 在 $(0,c)$ 上递减，而在 $(c,1)$ 上递增。

这能说明什么呢？一方面，由于 $d_0<c<1$，$f(x)$ 在 $(0,d_0)$ 上递减，在 $(d_0,1)$ 上先减后增；另一方面，由于 $f(d_0)=f(1)=0$，我们可以知道 $(0,d_0)$ 上 $f(x)>0\Rightarrow G(x)>x$，而 $(d_0,1)$ 上 $f(x)<0\Rightarrow G(x)<x$，示意图大致如下：

![](https://calculus1437.github.io/MathBlog/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-04-02%20185743.png)

这给我们一个猜想：因为 $d_{r+1}=G(d_r)$，所以 $\left\{d_r\right\}$ 会在这逐步迭代中逐渐落向 $d_0$。但并不是所有在 $y=x$ 两侧的函数都满足这个性质，比如 $h(x)=\displaystyle\frac{1}{x}$。但由于这里 $\left\{d_r\right\}$ 本身是递增的，于是我们有一种很简单的办法可以得到这个结论：

因为 $d_1=p_0<1$，由于 $G(x)$ 递增，对 $\forall\ x<1$ 有 $G(x)<1$，所以 $d_2=G(d_1)<1$。

若 $d_2>d_0$，则 $d_3=G(d_2)<d_2$，与 $\left\{d_n\right\}$ 递增的性质矛盾。所以 $d_2\leq d_0$。

同理，可以得到 $d_3\leq d_0$。以此类推，可得到对 $\forall\ r\in \mathbb{N^+}$，$d_r\leq d_0$ 的结论。

又因为 $\displaystyle\lim_{r\to \infty}d_r=d=G(d)\leq d_0$，所以 $d=d_0$。

<br/>

---

## 习题 6.6 泰勒级数

!!! question "练习 6.6.1"
    第七章即将得出的结果将证明这个方程对所有 \(x \in  \left( {-1,1}\right)\) 都成立，但请注意，当 \(x = 1\) 时，这个级数实际上收敛。假设 \(\arctan \left( x\right)\) 是连续的，解释为什么在 \(x = 1\) 处级数的值必然是 \(\arctan \left( 1\right)\) 。在这种情况下，我们得到了什么有趣的身份？

<br/>

!!! question "练习 6.6.2"
    从本节方程 \eqref{eq:6.6.1} 中的恒等式出发，找到 \(\ln \left( {1 + x}\right)\) 的幂级数表示。对于哪些 \(x\) 值，这个表达式是有效的？

<br/>

!!! question "练习 6.6.3"
    (a) 对方程\eqref{eq:6.6.2}的每一边求导，并推导出 \({f}^{\prime }\left( 0\right)  = {a}_{1}\) 。一般来说，证明如果 \(f\) 具有幂级数展开，则系数必须由公式给出

    \[
    {a}_{n} = \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}.
    \]

    提供证明对公式\eqref{eq:6.6.2}中级数进行操作的定理的参考文献。

<br/>

!!! question "练习 6.6.4"
    使用前一个练习中 \({a}_{n}\) 的Taylor公式来生成/验证所谓的 \(\sin \left( x\right)\) 的Taylor级数，其形式为

    \[
    \sin \left( x\right)  \sim  x - \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} - \frac{{x}^{7}}{7!} + \cdots .
    \]

<br/>

!!! question "练习 6.6.5"
    证明 \({S}_{N}\left( x\right)\) 在 \(\left\lbrack  {-2,2}\right\rbrack\) 上一致收敛于 \(\sin \left( x\right)\) 。将此证明推广到证明在形如 \(\left\lbrack  {-R,R}\right\rbrack\) 的任何区间上收敛是一致的。

<br/>

!!! question "练习 6.6.6"
    (a) 生成指数函数 \(f\left( x\right)  = {e}^{x}\) 的Taylor系数，然后证明相应的Taylor级数在形如 \(\left\lbrack  {-R,R}\right\rbrack\) 的任何区间上一致收敛于 \({e}^{x}\) 。

    (b) 验证公式 \({f}^{\prime }\left( x\right)  = {e}^{x}\) 。

    使用代换生成 \({e}^{-x}\) 的级数，然后通过将两个级数相乘并收集 \(x\) 的相同幂次来计算 \({e}^{x} \cdot  {e}^{-x}\) 。

<br/>

!!! question "练习 6.6.7"
    解释为什么误差函数 \({E}_{N}\left( x\right)  = {f}_{N}\left( x\right)  - {S}_{N}\left( x\right)\) 满足

    \[
    {E}_{N}^{\left( n\right) }\left( 0\right)  = 0\;\text{ for all }n = 0,1,2,\ldots ,N.
    \]

    为了简化符号，假设 \(x > 0\) 并将广义中值定理应用于函数 \({E}_{N}\left( x\right)\) 和 \({x}^{N + 1}\) 在区间 \(\left\lbrack  {0,x}\right\rbrack\) 上。因此，存在一个点 \({x}_{1} \in  \left( {0,x}\right)\) 使得

    \[
    \frac{{E}_{N}\left( x\right) }{{x}^{N + 1}} = \frac{{E}_{N}^{\prime }\left( {x}_{1}\right) }{\left( {N + 1}\right) {x}_{1}^{N}}.
    \]

<br/>

!!! question "练习 6.6.8"
    完成Lagrange余项定理的证明。

<br/>

!!! question "练习 6.6.9"
    使用 \(\infty /\infty\) 版本的 L'Hospital 法则(定理\ref{thm:5.3.8})证明 \({g}^{\prime }\left( 0\right)  = 0\) 。

<br/>

!!! question "练习 6.6.10"
    计算 \({g}^{\prime }\left( x\right)\) 对于 \(x \neq  0\) 。计算 \({g}^{\prime \prime }\left( x\right)\) 和 \({g}^{\prime \prime \prime }\left( x\right)\) 对于 \(x \neq  0\) 。利用这些观察结果，并发明所需的符号，给出 \(n\) 阶导数 \({g}^{\left( n\right) }\left( x\right)\) 在非零点的一般描述。

<br/>

!!! question "练习 6.6.11"
    计算 \({g}^{\prime \prime }\left( 0\right)\) 。从这个例子中，提出一个关于如何计算 \({g}^{\left( n\right) }\left( 0\right)\) 的一般论证。

    讨论此示例的后果。 \(g\) 是否无限可微？它的Taylor级数是什么样子的？这个级数在哪些点收敛？收敛到什么？这个示例对每个无限可微函数都可以由其Taylor级数展开表示的猜想有何影响？

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
