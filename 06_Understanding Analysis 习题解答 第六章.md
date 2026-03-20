@import "style.less"

[17.一致连续和一致收敛的等价命题](#17)(6.2.10)
[18.Bolzano-Weierstrass 定理的函数序列版本](#18)(6.2.14-6.2.16)

# 函数序列与函数级数

## 习题 6.2 函数序列的一致收敛

!!! question 习题 6.2.1
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

!!! question 习题 6.2.2
    设
    $$ g_n(x) = \frac{nx + \sin(nx)}{2n} $$
    找出 $(g_n)$ 在 $\mathbb{R}$ 上的点态极限。在 $[-10, 10]$ 上收敛是否一致？在整个 $\mathbb{R}$ 上收敛是否一致？
    
$\displaystyle\lim_{n\to \infty}g_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x+\displaystyle\frac{\sin(nx)}{n}}{2}=\displaystyle\frac{x}{2}$。

$\left|g_n(x)-\displaystyle\frac{x}{2}\right|=\left|\displaystyle\frac{\sin(nx)}{2n}\right|\leq \displaystyle\frac{1}{2n}$。

所以，对 $\forall\ \varepsilon>0$，令 $N>\displaystyle\frac{1}{2\varepsilon}$，则对 $\forall\ n\geq N$ 和 $\forall\ x\in \mathbb{R}$，都有 $\left|g_n(x)-\displaystyle\frac{x}{2}\right|<\varepsilon$。

所以 $g_n$ 在 $[-10,10]$ 和 $\mathbb{R}$ 上都一致收敛。

<br/>

!!! question 习题 6.2.3
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

!!! question 习题 6.2.4
    对于每个 $n \in \mathbb{N}$，找出 $\mathbb{R}$ 上函数 $f_n(x) = x/ (1 + nx^2)$ 达到其最大值和最小值的点。用此证明 $(f_n)$ 在 $\mathbb{R}$ 上一致收敛。极限函数是什么？
    
$f_n(x)$ 是连续可微的。求导可得 $f_n'(x) = \displaystyle\frac{1 - n x^2}{(1 + n x^2)^2}$。

利用中值定理我们可以知道，$f'_n(x)$ 大于 $0$ 则原函数单调递增，小于 $0$ 则单调递减。

因此，$f_n(x)$ 在 $(-\infty,\displaystyle-\frac{1}{\sqrt[]{n}})$ 递减，$(-\displaystyle\frac{1}{\sqrt[]{n}},\displaystyle\frac{1}{\sqrt[]{n}})$ 递增，$(\displaystyle\frac{1}{\sqrt[]{n}}, +\infty)$ 递减。

最大值为 $f_n\left(\displaystyle\frac{1}{\sqrt{n}}\right)=\displaystyle\frac{1}{2\sqrt{n}}$，最小值为 $f_n\left(-\displaystyle\frac{1}{\sqrt[]{n}}\right)=-\displaystyle\frac{1}{2\sqrt{n}}$。

首先，$f(x)=\displaystyle\lim_{n\to \infty}f_n(x)=0$。

因为 $\left|f(x)-f_n(x)\right|\leq \displaystyle\frac{1}{2\sqrt{n}}$，所以 $N$ 的选取是与 $x$ 无关的，所以 $\left\{f_n(x)\right\}$ 在 $\mathbb{R}$ 上一致收敛，极限函数为 $f(x)=0$。

<br/>

!!! question 习题 6.2.5
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

!!! question 习题 6.2.6
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

!!! question 习题 6.2.7
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

!!! question 习题 6.2.8
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

!!! question 习题 6.2.9
    假设 $(f_n)$ 在紧集 $K$ 上一致收敛于 $f$，且 $g$ 是 $K$ 上的连续函数，满足 $g(x) \neq 0$。证明 $(f_n/g)$ 在 $K$ 上一致收敛于 $f/g$。
    
因为 $g$ 是紧集 $K$ 上的连续函数，所以 $|g(x)|$ 在 $K$ 上有最小值，记为 $m$。又因为 $g(x)\neq 0$，所以 $m>0$。

因为 $f_n\to f$ 在 $K$ 上一致收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$ 和 $\forall\ x\in K$，$\left|f_n(x)-f(x)\right|<\varepsilon$。所以 $\left|\displaystyle\frac{f_n(x)}{g(x)}-\displaystyle\frac{f(x)}{g(x)}\right|=\displaystyle\frac{1}{\left|g(x)\right|}\left|f_n(x)-f(x)\right|< \displaystyle\frac{1}{m}\varepsilon$。

所以 $\displaystyle\frac{f_n}{g}$ 在 $K$ 上一致收敛于 $\displaystyle\frac{f}{g}$。

<br/>

!!! question 习题 6.2.10
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

!!! question 习题 6.2.11
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

!!! question 习题 6.2.12
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

!!! question 习题 6.2.13 (Cantor 函数)
    回顾第 3.1 节中 Cantor 集 $C \subseteq [0,1]$ 的构造。本练习利用了该讨论中的结果和符号。
    
    (a) 为所有 $x \in [0,1]$ 定义 $f_0(x) = x$。现在，设
    $$ f_1(x) = \begin{cases} (3/2)x & \text{for } 0 \le x \le 1/3 \\ 1/2 & \text{for } 1/3 < x < 2/3 \\ (3/2)x - 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
    绘制 $f_0$ 和 $f_1$ 在 $[0,1]$ 上，并观察到 $f_1$ 是连续的、递增的，并且在中间三分之一 $(1/3, 2/3) = [0,1] \setminus C_1$ 上是恒定的。
    
    (b) 通过模仿这一过程，将 $f_1$ 的每个非恒定段的中间三分之一压平来构造 $f_2$。具体来说，令
    $$ f_2(x) = \begin{cases} (1/2)f_1(3x) & \text{for } 0 \le x \le 1/3 \\ f_1(x) & \text{for } 1/3 < x < 2/3 \\ (1/2)f_1(3x - 2) + 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
    如果我们继续这个过程，证明生成的序列 $(f_n)$ 在 $[0,1]$ 上一致收敛。
    
    (c) 设 $f = \lim f_n$。证明 $f$ 是 $[0,1]$ 上的一个连续、递增函数，且满足 $f(0) = 0$ 和 $f(1) = 1$，对于开集 $[0,1] \setminus C$ 中的所有 $x$，满足 $f'(x) = 0$。回想一下，Cantor 集 $C$ 的“长度”为 0。然而，$f$ 在“长度为 1”的集合上保持不变的同时，设法从 0 增加到 1。
    
(a) ![f_0](https://calculus1437.github.io/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20203712.png){width=45%} ![f_1](https://calculus1437.github.io/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20204217.png){width=45%}

(b) 直接求解出最后 $f(x)$ 的形态是困难的。所以在这里我们考虑用 Cauchy 准则，即分析 $\left|f_m(x)-f_n(x)\right|$ 的大小来进行证明。

![](https://calculus1437.github.io/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20213311.png)

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

!!! question 习题 6.2.14
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

!!! question 习题 6.2.15
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

!!! question 习题 6.2.16 (阿尔泽拉-阿斯科利定理, Arzela-Ascoli Theorem)
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
