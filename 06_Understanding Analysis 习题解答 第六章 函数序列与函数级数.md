
[17.一致连续和一致收敛的等价命题](#17)(6.2.10)
[18.Bolzano-Weierstrass 定理的函数序列版本](#18)(6.2.14-6.2.16)
[19.柯西余项定理](#19)(6.6.9-6.6.10)

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
    
(a) ![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20203712.png){width=45%} ![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20204217.png){width=45%}

(b) 直接求解出最后 $f(x)$ 的形态是困难的。所以在这里我们考虑用 Cauchy 准则，即分析 $\left|f_m(x)-f_n(x)\right|$ 的大小来进行证明。

![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-15%20213311.png)
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
    (a) 通过引用适当的定理，详细论证在区间 $(-R, R)$ 上收敛的幂级数必然在每个点 $x \in  \left( {-R,R}\right)$ 上表示一个连续函数。
    
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

(b) 分析式子 $\left|na_nx^{n-1}\right|=\displaystyle\frac{1}{t}\left|a_nt^n\right|\left(n\left|\displaystyle\frac{x}{t}\right|^{n-1}\right)$。一方面，因为 $\left|x\right|<t$，所以 $\displaystyle\sum_{n=1}^{\infty}n\left|\displaystyle\frac{x}{t}\right|^{n-1}$ 是收敛的；另一方面，$\displaystyle\sum_{n=1}^{\infty}\left|a_nt^n\right|$ 本身也是收敛的，所以 $\displaystyle\sum_{n=1}^{\infty}\left|na_nx^{n-1}\right|$ 收敛。从而证明了微分级数的收敛性。

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
    1, \quad &\text{if }n=2k-1\\
    \displaystyle\frac{1}{10^k}, \quad &\text{if }n=2k\\
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

![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-04-02%20185743.png)

这给我们一个猜想：因为 $d_{r+1}=G(d_r)$，所以 $\left\{d_r\right\}$ 会在这逐步迭代中逐渐落向 $d_0$。但并不是所有在 $y=x$ 两侧的函数都满足这个性质，比如 $h(x)=\displaystyle\frac{1}{x}$。但由于这里 $\left\{d_r\right\}$ 本身是递增的，于是我们有一种很简单的办法可以得到这个结论：

因为 $d_1=p_0<1$，由于 $G(x)$ 递增，对 $\forall\ x<1$ 有 $G(x)<1$，所以 $d_2=G(d_1)<1$。

若 $d_2>d_0$，则 $d_3=G(d_2)<d_2$，与 $\left\{d_n\right\}$ 递增的性质矛盾。所以 $d_2\leq d_0$。

同理，可以得到 $d_3\leq d_0$。以此类推，可得到对 $\forall\ r\in \mathbb{N^+}$，$d_r\leq d_0$ 的结论。

又因为 $\displaystyle\lim_{r\to \infty}d_r=d=G(d)\leq d_0$，所以 $d=d_0$。

<br/>

---

## 习题 6.6 泰勒级数

!!! question "练习 6.6.1"
    
    例 6.6.1 中的推导表明，$\arctan(x)$ 的泰勒级数对所有 $x \in (-1,1)$ 都成立。然而请注意，当 $x = 1$ 时，该级数也收敛。假设 $\arctan(x)$ 是连续的，解释为什么该级数在 $x = 1$ 处的值必然是 $\arctan(1)$。在这种情况下我们能得到什么有趣的恒等式？

令 $f(x)=x-\displaystyle\frac{1}{3}x^3+\displaystyle\frac{1}{5}x^5-\cdots$ 并令 $g(x)=f(x)-\arctan(x)$。 依题意可知 $g(x)$ 在 $(-1,1]$ 上是连续的，并且在 $(-1,1)$ 上都有 $g(x)=0$。

所以 $g(1)=\displaystyle\lim_{x\to 1^-}g(x)=0$。由此得到恒等式：

$$
\displaystyle\frac{\pi}{4}=\arctan(1)=1-\displaystyle\frac{1}{3}+\displaystyle\frac{1}{5}-\cdots
$$

<br/>

!!! question "练习 6.6.2"
    
    从本节之前生成的某个级数出发，使用类似于例 6.6.1 中的代数变换，找到以下各个函数的泰勒级数表示。每个级数表示恰好在哪些 $x$ 的值上有效？
    
    (a) $x\cos(x^2)$
    
    (b) $x/(1+4x^2)^2$
    
    (c) $\ln(1+x^2)$

(a) 我们使用 $\sin(x)=x-\displaystyle\frac{x^3}{3!}+\displaystyle\frac{x^5}{5!}-\cdots$ 来完成这一题。将 $x$ 替换为 $x^2$，并进行求导：

$\left(\sin(x^2)\right)'=2x\cos(x^2)$，所以：

$$
x\cos(x^2)=x-\displaystyle\frac{x^5}{2!}+\displaystyle\frac{x^9}{4!}-\cdots
$$

(b) 同上，$\displaystyle\frac{x}{\left(1+4x^2\right)^2}=-\displaystyle\frac{1}{8}\left(\displaystyle\frac{1}{1+4x^2}\right)'$，先利用 $\displaystyle\frac{1}{1-x}=1+x+x^2+\cdots$ 来得到 $\displaystyle\frac{1}{1+4x^2}=1-4x^2+16x^4-\cdots$，再求导：

$$
\left(\left(-4x^2\right)^n\right)'=(-1)^n8nx(4x^2)^{n-1}
$$

$$
\displaystyle\frac{x}{\left(1+4x^2\right)^2}=x-8x^3+48x^5-\cdots
$$

(c) $\left(\ln(1+x^2)\right)'=\displaystyle\frac{2x}{1+x^2}$，先利用 $\displaystyle\frac{1}{1-x}=1+x+x^2+\cdots$ 来得到 $\displaystyle\frac{2x}{1+x^2}=2x-2x^3+2x^5-\cdots$，再求积分：

$$
\ln(1+x^2)=x^2-\frac{x^4}{2}+\frac{x^6}{3}-\cdots
$$

<mark>这里感觉很奇怪，难道泰勒级数可以任意做变量替换，求导积分和其他项的乘除吗？</mark>

<br/>

!!! question "练习 6.6.3"
    
    推导定理 6.6.2 中给出的泰勒系数公式。

若 $f$ 可以被表示成幂级数的形式：

$$
f(x)=a_0+a_1x+a_2x^2+\cdots
$$

则 $f(0)=a_0$。

对 $f$ 求导，有：

$$
f'(x)=a_1+2a_2x+3a_3x^2+\cdots
$$

所以 $f'(0)=a_1$。

同理，进行 $n$ 次求导后可得结果为：

$$
f^{(n)}(x)=n!a_n+{\left(n+1\right)}!a_{n+1}x+\cdots
$$

所以 $f^{(n)}(0)=n!a_n$，即 $a_n=\displaystyle\frac{f^{(n)}(0)}{n!}$，命题得证。

<br/>

!!! question "练习 6.6.4"
    
    解释如何修改拉格朗日余项定理以证明：
    
    $$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \cdots = \ln(2)$$

定义 $f(x)=\ln(1+x)$ 并定义其泰勒级数的部分多项式 $S_n(x)$：

$$
\begin{align*}
  S_n(x)&=f(0)+\displaystyle\sum_{i=1}^{n} \displaystyle\frac{f^{(i)}(0)}{i!} x^i=\displaystyle\sum_{i=1}^{n}(-1)^{i+1}\displaystyle\frac{x^i}{i}\\&=x-\displaystyle\frac{x^2}{2}+\displaystyle\frac{x^3}{3}-\cdots+(-1)^{n+1}\displaystyle\frac{x^n}{n}
\end{align*}
$$

由拉格朗日余项定理，存在 $\left|c\right|<\left|x\right|$，$E_n(x)=f(x)-S_n(x)=\displaystyle\frac{f^{(n+1)}(c)}{\left(n+1\right)!}x^{n+1}=\displaystyle\frac{\left(-1\right)^{n}}{n+1}\cdot\left(\displaystyle\frac{x}{1+c}\right)^{n+1}$。

因为 $x=1$ 时，$0<c<1$，所以 $1+c>x$，$\displaystyle\lim_{n\to \infty}E_n(1)=f(1)-\displaystyle\lim_{n\to \infty}S_n(1)=0$。所以泰勒级数收敛，有

$$
1-\displaystyle\frac{1}{2}+\displaystyle\frac{1}{3}-\displaystyle\frac{1}{4}+\displaystyle\frac{1}{5}-\displaystyle\frac{1}{6}+\cdots=\ln(2)
$$

<br/>

!!! question "练习 6.6.5"
    
    (a) 生成指数函数 $f(x) = \mathrm{e}^x$ 的泰勒系数，并证明相应的泰勒级数在任何形如 $[-R, R]$ 的区间上一致收敛到 $\mathrm{e}^x$。
    
    (b) 验证公式 $f'(x) = \mathrm{e}^x$。
    
    (c) 使用代换法生成 $\mathrm{e}^{-x}$ 的级数，然后通过将两个级数相乘并合并 $x$ 的同次幂，非正式地计算 $\mathrm{e}^x \cdot \mathrm{e}^{-x}$。

(a) 因为 $f^{(n)}(x)=\mathrm{e}^x$，所以泰勒系数为 $\displaystyle\frac{f^{(n)}(0)}{n!}=\frac{\mathrm{e}^0}{n!}=\frac{1}{n!}$。相应的级数 $S_n(x)$ 有：

$$
S_n(x)=\displaystyle\sum_{k=0}^{n}\displaystyle\frac{1}{k!}x^k
$$

下面估计 $E_n(x)=f(x)-S_n(x)=\displaystyle\frac{\mathrm{e}^c}{\left(n+1\right)!}x^{n+1}$，$\left|c\right|<\left|x\right|$。由于指数函数的增长程度远小于阶乘（稍后证明），所以 $\displaystyle\lim_{n\to \infty}E_n(x)=0$。所以对 $\forall\ x\in \mathbb{R}$，$S_n(x)$ 都是收敛的，故在任何区间 $[-R,R]$ 上一致收敛于 $\mathrm{e}^x$。

(b) 求导！

$$
\mathrm{e}^x=1+x+\displaystyle\frac{x^2}{2!}+\displaystyle\frac{x^3}{3!}+\cdots
$$

$$
\left(\mathrm{e}^x\right)'=0+1+x+\displaystyle\frac{x^2}{2!}+\cdots
$$

相当于每一项后移了一位而已，没有变化，所以 $\left(\mathrm{e}^x\right)'=\mathrm{e}^x$。

(c) $\mathrm{e}^{-x}=1-x+\displaystyle\frac{x^2}{2!}-\displaystyle\frac{x^3}{3!}+\cdots$

$$
\begin{align*}
  \mathrm{e}^x\cdot\mathrm{e}^{-x}&=\left(1+x+\displaystyle\frac{x^2}{2!}+\cdots\right)\left(1-x+\displaystyle\frac{x^2}{2!}-\cdots\right)\\&=1\cdot 1+1\cdot(x+\left(-x\right))+1\cdot\left(\displaystyle\frac{x^2}{2!}+\displaystyle\frac{x^2}{2!}\right)\\&\mathrel{+}x\cdot (-x)+\left(x+\left(-x\right)\right)\cdot\displaystyle\frac{x^2}{2!}+\cdots \text{（最终后面的项都被消掉）}\\&=1
\end{align*}
$$

<mark>指数函数增长速度远小于阶乘的证明</mark>

证明对 $\forall\ x\in \mathbb{R}$（不妨设 $x>0$），$\displaystyle\lim_{n\to \infty}\left(\displaystyle\frac{x^n}{n!}\right)=0$。

设 $N>2x$，则对 $\forall\ k>N$，

$$
\displaystyle\frac{x^k}{k!}\leq\displaystyle\frac{x^{N}}{N!}\cdot\left(\displaystyle\frac{x}{2x}\right)^{k-N}=\displaystyle\frac{x^{N}}{N!}\cdot\left(\displaystyle\frac{1}{2}\right)^{k-N}
$$

而右边在 $k\to \infty$ 时趋于 $0$，所以 $\displaystyle\lim_{n\to \infty}\left(\displaystyle\frac{x^n}{n!}\right)=0$。
<br/>

!!! question "练习 6.6.6"
    
    复习本节末尾引入的函数
    
    $$g(x) = \begin{cases}\mathrm{e}^{-1/x^2} & \text{当 } x \neq 0, \\0 & \text{当 } x = 0.\end{cases}$$
    
    满足 $g'(0) = 0$ 的证明。
    
    (a) 计算当 $x \neq 0$ 时 $g'(x)$ 的值。然后使用导数的定义求 $g''(0)$。
    
    (b) 计算当 $x \neq 0$ 时 $g''(x)$ 和 $g'''(x)$ 的值。利用这些观察并在需要时发明符号，给出在非零点处第 $n$ 阶导数 $g^{(n)}(x)$ 的一般描述。
    
    (c) 构造一般性证明，说明为什么对所有 $n \in \mathbb{N}$ 有 $g^{(n)}(0) = 0$。

(a) $g'(x)=\displaystyle\frac{2}{x^3}\mathrm{e}^{-\frac{1}{x^2}}$。

$$
\begin{align*}
  &\mathrel{\phantom{=}}g''(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{\displaystyle\frac{2}{x^3}\mathrm{e}^{-\frac{1}{x^2}}}{x}=\displaystyle\lim_{x\to 0}\displaystyle\frac{2\mathrm{e}^{-\frac{1}{x^2}}}{x^4}\\&=2\displaystyle\lim_{t\to +\infty}\displaystyle\frac{t^2}{\mathrm{e}^t}\text{（这里作了 }t=\displaystyle\frac{1}{x^2}\text{ 的代换）}\\&=0 \text{（洛必达法则对上下求导）}
\end{align*}
$$

(b) $g''(x)=\left(-\displaystyle\frac{6}{x^4}+\left(\displaystyle\frac{2}{x^3}\right)^2\right)\mathrm{e}^{-\frac{1}{x^2}}$。

$g'''(x)=\left(\displaystyle\frac{24}{x^5}-\displaystyle\frac{24}{x^7}-\displaystyle\frac{12}{x^7}+\left(\displaystyle\frac{2}{x^3}\right)^3\right)\mathrm{e}^{-\frac{1}{x^2}}$。

一般的分式 $\displaystyle\frac{1}{x^p}$ 自身求导时分母次数只会加一，而 $\mathrm{e}^{-\frac{1}{x^2}}$ 每次求导都会给分母次数加三，所以 $g^{(n)}(x)$ 中 $\mathrm{e}^{-\frac{1}{x^2}}$ 的分式系数的分母次数最大值为 $3n$。令 $P_n(x)$ 为 $x$ 最大次数为 $n$ 的多项式，则有

$$
g^{(n)}(x) = P_{3n}\left(\displaystyle\frac{1}{x}\right) \cdot \mathrm{e}^{-\frac{1}{x^2}}
$$

(c) 这里使用数学归纳法。首先，$g'(0)=g''(0)=0$。

然后，若 $\exists\ n\in \mathbb{N^+}$ 使得 $g^{(n)}(0)=0$，则

$$
\begin{align*}
  &\mathrel{\phantom{=}}g^{(n+1)}(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{P_{3n}\left(\displaystyle\frac{1}{x}\right)\cdot \mathrm{e}^{-\frac{1}{x^2}}}{x}=\displaystyle\lim_{t\to +\infty}\displaystyle\frac{\sqrt{t}\cdot P_{3n}\left(\sqrt{t}\right)}{\mathrm{e}^t}\\&=\displaystyle\lim_{t\to +\infty}\displaystyle\frac{P_{\frac{3n+1}{2}}\left(t\right)}{\mathrm{e}^t}
\end{align*}
$$

所以对上式左右两边求 $2n$ 次导，得到

$$
\displaystyle\lim_{t\to +\infty}\displaystyle\frac{P_{\frac{3n+1}{2}}\left(t\right)}{\mathrm{e}^t}=\displaystyle\lim_{t\to +\infty}\displaystyle\frac{0}{\mathrm{e}^t}=0
$$

这说明了 $g^{(n+1)}(0)=0$。

所以由数学归纳法，对 $\forall\ n\in \mathbb{N^+}$，$g^{(n)}(0)=0$。

<br/>

!!! question "练习 6.6.7"
    
    举例说明以下各种情况，或者解释为什么不存在这样的函数：
    
    (a) 在整个 $\mathbb{R}$ 上无限次可微的函数 $g(x)$，其泰勒级数仅当 $x \in (-1,1)$ 时收敛到 $g(x)$。
    
    (b) 具有与 $\sin(x)$ 相同泰勒级数但在所有 $x \neq 0$ 处满足 $h(x) \neq \sin(x)$ 的无限次可微函数 $h(x)$。
    
    (c) 在整个 $\mathbb{R}$ 上无限次可微的函数 $f(x)$，其泰勒级数当且仅当 $x \leq 0$ 时收敛到 $f(x)$。

(a) 这里有两种思路，一种是构造一个在 $(-1,1)$ 上收敛的幂级数，通过 $\displaystyle\frac{g^{(n)}(0)}{n!}x^n$ 的值来反推 $g$ 本身；一种是考察已有的仅在 $(-1,1)$ 收敛的泰勒级数，并试着改进。前者需要积分学的知识，故优先考虑后者。

考察如下的泰勒级数：

$$
\displaystyle\frac{1}{1-x}=1+x+x^2+\cdots
$$

这个级数正好仅当在 $(-1,1)$ 上收敛，剩下要做的就是试着拓展它的定义域。

令 $g(x)=\displaystyle\frac{1}{1+x^2}$，则 $g$ 在 $\mathbb{R}$ 上无限次可微，且有如下的泰勒展开：

$$
g(x)=1-x^2+x^4-\cdots
$$

令 $S_n(x)=\displaystyle\sum_{i=0}^{n} (-1)^i x^{2i}$，利用等比数列的公式可以求得差值 $E_n(x)=g(x)-S_n(x)=(-1)^{n+1}\displaystyle\frac{x^{2(n+1)}}{1+x^2}$。

由 $(-1)^{n+1}x^{2(n+1)}$ 项可得，$\left|x\right|<1$ 时，$\displaystyle\lim_{n\to \infty}E_n(x)=0$，$\left|x\right|\geq 1$ 时，$E_n(x)$ 发散。

所以 $g(x)=\displaystyle\frac{1}{1+x^2}$ 满足要求。

(b) 由于 $0$ 处的泰勒级数仅由 $0$ 处各阶导数的值决定，所以泰勒级数相同但函数不同也许是可能的。

先写出 $\sin x$ 的泰勒级数：

$$
\sin x=x-\displaystyle\frac{x^3}{3!}+\displaystyle\frac{x^5}{5!}-\cdots=\displaystyle\sum_{m=0}^{\infty} (-1)^m \frac{x^{2m+1}}{(2m+1)!}
$$

也就是说，我们要找的 $h(x)$，它的奇数次导数为 $h^{(2m+1)}(0)=(-1)^m$，偶数次导数为 $h^{(2m)}(0)=0$，这个条件太苛刻了。

放宽一点条件，先寻找任意次导数下导数值不变（或跳动）的函数，由此考虑到了 $\mathrm{e}^x$ 的一族函数。例如，$\mathrm{e}^{-x}$ 的泰勒展开为：

$$
\mathrm{e}^{-x}=1-x+\displaystyle\frac{x^2}{2!}-\displaystyle\frac{x^3}{3!}+\cdots=\displaystyle\sum_{m=0}^{\infty} (-1)^m \frac{x^{m}}{m!}
$$

虽然它的偶数次跟 $\sin x$ 特别相近，但是符号都是负号，想要变为正负交替非常困难。

等等！练习 6.6.6 里那个非常特殊的函数可以派上用场：

$$

I(x) = \begin{cases}
\mathrm{e}^{-1/x^2} & \text{当 } x \neq 0 \\
0 & \text{当 } x = 0
\end{cases}

$$

可见 $I^{(n)}(0)=0$。令 $h(x)=I(x)+\sin x$，则 $h$ 的泰勒级数与 $\sin x$ 的泰勒级数相同，且两者在 $x\neq 0$ 处不相等。

(c) 相似的思路在这里是可行的：

$$
f(x)=\begin{cases}
  I(x) + \sin x & \text{当 } x > 0 \\
  \sin x & \text{当 } x \leq 0
\end{cases}
$$



<br/>

!!! question "练习 6.6.8"
    
    这是一个较弱形式的拉格朗日余项定理，它的证明可以说比强结果的证明更具启发性。
    
    (a) 首先建立一个引理：如果 $g$ 和 $h$ 在 $[0,x]$ 上可微，满足 $g(0) = h(0)$，且对所有 $t \in [0,x]$ 有 $g'(t) \leq h'(t)$，那么对所有 $t \in [0,x]$ 有 $g(t) \leq h(t)$。
    
    (b) 设 $f, S_N$ 和 $E_N$ 同定理 6.6.3，并取 $0 < x < R$。如果对于所有 $t \in [0, x]$ 有 $|f^{(N+1)}(t)| \leq M$，证明：
    
    $$|E_N(x)| \leq \frac{Mx^{N+1}}{(N+1)!}$$

(a) 令 $I(t)=g(t)-h(t)$，则 $I'(t)=g'(t)-h'(t)\leq 0$，所以 $I(t)$ 在 $[0,x]$ 上单调递减，因此 $I(t) \leq I(0) = 0$，即 $g(t) \leq h(t)$。

(b) 原不等式化成 $-M\leq f^{(N+1)}(t)\leq M$。

由 (a) 问的灵感，我们可以把 $f^{(N+1)}(t)$ 和 $M$ 看作两个函数的导函数，再利用 (a) 中引理降低阶数。

当然，后续的操作无非就是一直降阶至原函数，所以我们不妨先反复使用 (a) 中的引理，来得到如下结论：、

若 $g(t)$ 和 $h(t)$ 在 $[0,x]$ 上 $n+1$ 阶可微，满足 $g^{k}(t)=h^{k}(t)=0$ 对于所有 $k\in \mathbb{N}$，$k\leq n$，且对所有 $t \in [0,x]$ 有 $g^{(n+1)}(t) \leq h^{(n+1)}(t)$，那么对所有 $t \in [0,x]$ 有 $g(t) \leq h(t)$。

由于 $f(t)$ 本身不一定 $n$ 阶导数零点均为 $0$，所以我们还是仿造泰勒展开的形式来构造 $E_N(x)$：

$$
\begin{align*}
  &E_N(x)=f(x)-S_N(x)\\
  &S_N(x)=f(0)+\displaystyle\frac{f'(0)}{1!}x+\displaystyle\frac{f''(0)}{2!}x^2+\cdots+\displaystyle\frac{f^{(N)}}{N!}x^N
\end{align*}
$$

再令 $h(x)=\displaystyle\frac{Mx^{N+1}}{(N+1)!}$，则 $E_N(x)$ 和 $h(x)$ 满足上述条件。所以

$$
\begin{align*}
  &\mathrel{\phantom{\Rightarrow}}-h(x)\leq E_N(x)\leq h(x)\\
  &\Rightarrow\left|E_N(x)\right|\leq \displaystyle\frac{Mx^{N+1}}{(N+1)!}
\end{align*}
$$

<br/>

<a id=19></a>

!!! question "练习 6.6.9"
    
    （柯西余项定理）。设 $f$ 在 $(-R,R)$ 上有 $N+1$ 阶可微。对每个 $a \in (-R,R)$，令 $S_N(x,a)$ 为 $f$ 在中心点 $a$ 处泰勒级数的部分和；换言之，定义
    
    $$S_N(x,a) = \sum_{n=0}^{N} c_n (x-a)^n \quad \text{其中} \quad c_n = \frac{f^{(n)}(a)}{n!}$$
    
    令 $E_N(x,a) = f(x) - S_N(x,a)$。现在在 $(-R,R)$ 中固定 $x \neq 0$，并将 $E_N(x,a)$ 视为变量 $a$ 的函数。
    
    (a) 计算 $E_N(x,x)$。
    
    (b) 解释为什么 $E_N(x,a)$ 关于 $a$ 可导，并证明：
    
    $$E_N'(x,a) = \frac{-f^{(N+1)}(a)}{N!} (x-a)^N$$
    
    (c) 证明：
    
    $$E_N(x) = E_N(x,0) = \frac{f^{(N+1)}(c)}{N!} (x-c)^N x$$
    
    其中 $c$ 在 $0$ 和 $x$ 之间。这就是在原点展开的泰勒级数的柯西余项形式。

(a) $E_N(x,x)=0$。

(b) $E_N(x,a)$ 是由 $f^{(k)}(a)$ 和 $(x-a)^k$（$k\in \mathbb{N}$，$k\leq n$）四则运算构成的函数，而这两种成分均在 $a$ 处可微，故 $E_N(x,a)$ 在 $a$ 处可微，并有：

$$
\begin{align*}
  \left(c_n(x-a)^n\right)'&=\displaystyle\frac{f^{(n+1)}(a)}{n!}(x-a)^n-\displaystyle\frac{f^{(n)}(a)}{n!}\cdot n(x-a)^{n-1}\\&=(n+1)c_{n+1}(x-a)^n-nc_n(x-a)^{n-1}
\end{align*}
$$

$$
\begin{align*}
  E_N'(x,a)&=-\displaystyle\sum_{n=0}^{N}\left(c_n(x-a)^n\right)'\\&=-\displaystyle\sum_{n=0}^{N}\left((n+1)c_{n+1}(x-a)^n-nc_n(x-a)^{n-1}\right)\\&=-(N+1)c_{N+1}(x-a)^N\\&=\displaystyle\frac{-f^{(N+1)}(a)}{N!}(x-a)^N
\end{align*}
$$

(c) 由拉格朗日中值定理，存在 $c$ 在 $0$ 和 $x$ 之间，使得：

$$
\begin{align*}
  \displaystyle\frac{E_N(x,x)-E_N(x,0)}{x-0}&=E_N'(x,c)\\
  E_N(x,0)&=-E_N'(x,c)x=\displaystyle\frac{f^{(N+1)}(c)}{N!}(x-c)^Nx
\end{align*}
$$

所以 $E_N(x)=E_N(x,0)=\displaystyle\frac{f^{(N+1)}(c)}{N!}(x-c)^Nx$。

<br/>

!!! question "练习 6.6.10"
    
    考虑 $f(x) = 1/\sqrt{1-x}$。
    
    (a) 生成 $f$ 在 $0$ 处的泰勒级数，并使用拉格朗日余项定理证明该级数在 $[0,1/2]$ 上收敛到 $f$。（$x < 1/2$ 的情况较为直接，而 $x = 1/2$ 时需要格外小心。）当我们对 $x > 1/2$ 尝试此方法时会发生什么？
    
    (b) 使用在练习 6.6.9 中证明的柯西余项定理证明 $f$ 的级数表示在 $[0,1)$ 上成立。

(a) $f^{(n)}(x)=\displaystyle\frac{\left(2n-1\right)!!}{2^n}\left(1-x\right)^{-\frac{2n+1}{2}}$，所以 $f$ 在 $0$ 处的泰勒级数为：

$$
\displaystyle\lim_{N\to \infty}S_N=1+\displaystyle\sum_{n=1}^{\infty} \frac{(2n-1)!!}{2^n n!} x^n=1+\displaystyle\sum_{n=1}^{\infty} \frac{(2n-1)!!}{(2n)!!} x^n
$$

由拉格朗日余项定理，存在 $c\in (0,x)$，使得：

$$
\begin{align*}
  E_N(x)&=f(x)-S_N(x)=\displaystyle\frac{f^{(N+1)}(c)}{(N+1)!}x^{N+1}=\displaystyle\frac{\left(2N+1\right)!!}{\left(2N+2\right)!!}\left(1-c\right)^{-\frac{2N+3}{2}}x^{N+1}\\&<\left(1-c\right)^{-\frac{2N+3}{2}}x^{N+1}=\left(\displaystyle\frac{x}{1-c}\right)^{N+1}(1-c)^{-\frac{1}{2}}
\end{align*}
$$

$x\leq \displaystyle\frac{1}{2}$ 时，$c<\displaystyle\frac{1}{2}$，所以 $\left(\displaystyle\frac{x}{1-c}\right)^{N+1} <(2x)^{N+1}$，因此 $x<\displaystyle\frac{1}{2}$ 时，$\displaystyle\lim_{N\to \infty}E_N(x)=0$。

$x=\displaystyle\frac{1}{2}$ 时，

$$
\begin{align*}
  E_N\left(\displaystyle\frac{1}{2}\right)&=\displaystyle\frac{\left(2N+1\right)!!}{\left(2N+2\right)!!}\left(1-c\right)^{-\frac{2N+3}{2}}\left(\displaystyle\frac{1}{2}\right)^{N+1}\\&<\displaystyle\frac{\left(2N+1\right)!!}{\left(2N+2\right)!!}\left(1-\displaystyle\frac{1}{2}\right)^{-\frac{2N+3}{2}}\left(\displaystyle\frac{1}{2}\right)^{N+1}\\&=\sqrt{2}\displaystyle\frac{\left(2N+1\right)!!}{\left(2N+2\right)!!}
\end{align*}
$$

而 $\displaystyle\lim_{n\to \infty}\displaystyle\frac{\left(2N+1\right)!!}{\left(2N+2\right)!!}=0$（证明将稍后给出），所以 $\displaystyle\lim_{n\to \infty}E_N\left(\displaystyle\frac{1}{2}\right)=0$。

$x>\displaystyle\frac{1}{2}$ 时，$1-c<x$，所以不等式的右侧是发散的，不能通过这种形式证明其收敛。

(b) 由柯西余项定理，存在 $c\in (0,x)$，使得：

$$
\begin{align*}
  E_N(x)&=\displaystyle\frac{f^{(N+1)}(x)}{N!}(x-c)^Nx=\displaystyle\frac{\left(2N+1\right)!!}{2\cdot \left(2N\right)!!}\left(1-c\right)^{-\frac{2N+3}{2}}x(x-c)^N\\&=\displaystyle\frac{\left(2N+1\right)!!}{2\cdot \left(2N\right)!!}\left(\displaystyle\frac{x-c}{1-c}\right)^{N}x\left(1-c\right)^{-\frac{3}{2}}\\&=\displaystyle\frac{\left(2N-1\right)!!}{(2N)!!}\left(N+\displaystyle\frac{1}{2}\right)\left(\displaystyle\frac{x-c}{1-c}\right)^Nx\left(1-c\right)^{-\frac{3}{2}}
\end{align*}
$$

现在开始估计。

$\displaystyle\lim_{N\to \infty}\displaystyle\frac{\left(2N-1\right)!!}{\left(2N\right)!!}=0$，$\displaystyle\frac{x-c}{1-c}<1$，但如果它极限是 $1$ 就难办（因为 $c$ 在变）。但考虑到 $x$ 是不变量，故用 $x$ 作出估计：$\displaystyle\frac{x-c}{1-c}=1-\displaystyle\frac{1-x}{1-c}$ 随着 $c$ 增大而递减，故最大值在 $0$ 处取得（当然 $c$ 必须大于 $0$）为 $x$，即 $\displaystyle\frac{1-x}{1-c}<x$。

考虑到 $N+\displaystyle\frac{1}{2}$ 是发散项，但直观上它的增长速度应该小于 $x^N$ 的递减速度。进行分析：上述等同于判断 $Nx^N$ 敛散性。多乘一个 $x$ 肯定比 $N$ 多加一更影响敛散性，所以由比较判别法，$\displaystyle\lim_{N\to \infty}\displaystyle\frac{\left(N+1\right)x^{N+1}}{Nx^N}=\displaystyle\lim_{N\to \infty}\displaystyle\frac{N+1}{N}x=x<1$，$\displaystyle\lim_{N\to \infty}Nx^N=0$。

再加上 $x\left(1-c\right)^{-\frac{3}{2}}$ 是有限项，所以 $\displaystyle\lim_{N\to \infty}E_N(x)=0$。

综上所述，$f$ 的级数表示在 $[0,1)$ 上成立。

<mark>阶乘之商极限为零的证明</mark>

这一证明涉及定积分的知识和一个经典结论，以科普性质放于此进行说明，现在可跳过。

我们要证明 $\displaystyle\lim_{n\to \infty}\displaystyle\frac{\left(2n-1\right)!!}{\left(2n\right)!!}=0$。

一个经典的包含双阶乘的结论是 $\sin^nx$ 的定积分。

$$
\begin{align*}
  &\mathrel{\phantom{=}}\displaystyle\int_{0}^{\frac{\pi}{2}}\sin^n x\, \mathrm{d}{x}=-\sin^{n-1}x\cos x\Big|_0^{\frac{\pi}{2}}+\displaystyle\int_{0}^{\frac{\pi}{2}} (n-1)\sin^{n-2}x\cos^2 x\, \mathrm{d}{x}\text{（分部积分法）}\\&=\displaystyle\int_{0}^{\frac{\pi}{2}} (n-1)\sin^{n-2}x(1-\sin^2 x)\, \mathrm{d}{x}\\&=(n-1)\displaystyle\int_{0}^{\frac{\pi}{2}} \sin^{n-2}x\, \mathrm{d}{x}-(n-1)\displaystyle\int_{0}^{\frac{\pi}{2}} \sin^nx\, \mathrm{d}{x}
\end{align*}
$$

所以求得 $\displaystyle\int_{0}^{\frac{\pi}{2}}{\sin^nx}\, \mathrm{d}{x}=\displaystyle\frac{n-1}{n}\displaystyle\int_{0}^{\frac{\pi}{2}}{\sin^{n-2}x}\, \mathrm{d}{x}$，这是一个递推式，利用这个递推式就可以得出结果：$\displaystyle\int_{0}^{\frac{\pi}{2}}{\sin^{2k}x}\, \mathrm{d}{x}=\displaystyle\frac{\left(2k-1\right)!!}{\left(2k\right)!!}\cdot\displaystyle\frac{\pi}{2}$（当然实际上需要奇偶讨论，这里为了得到所求极限表达式而略去）。

所以证明极限为 $0$ 即证明这个积分极限为 $0$。虽然 $\left(0,\displaystyle\frac{\pi}{2}\right)$ 上 $\displaystyle\lim_{k\to \infty}\sin^{2k}x=0$，但是由于不同 $x$ 的趋近速率不同，估计仍需小心。

当然趋近速率的不同主要是 $x=\displaystyle\frac{\pi}{2}$ 这点导致的，毕竟这里 $\sin^{2k}x$ 为定值。所以我们进行分段讨论。取 $0<\delta<\displaystyle\frac{\pi}{2}$，对 $x\in \left[0,\displaystyle\frac{\pi}{2}-\delta\right]$，$\sin^{2k}x\leq \sin^{2k}\left(\displaystyle\frac{\pi}{2}-\delta\right)$，后者是可以控制的，而 $\left[\displaystyle\frac{\pi}{2}-\delta,\displaystyle\frac{\pi}{2}\right]$ 处的积分可通过区间长度来限制。

因此对 $\forall\ \varepsilon>0$，取 $\delta=\displaystyle\frac{\varepsilon}{2}$。对于 $x\in \left[\displaystyle\frac{\pi}{2}-\delta,\displaystyle\frac{\pi}{2}\right]$，$\displaystyle\int_{\frac{\pi}{2}-\delta}^{\frac{\pi}{2}}\sin^{2k}x\, \mathrm{d}{x}< \displaystyle\int_{\frac{\pi}{2}-\delta}^{\frac{\pi}{2}}{1}\, \mathrm{d}{x}=\delta=\displaystyle\frac{\varepsilon}{2}$；对于 $x\in \left[0,\displaystyle\frac{\pi}{2}-\delta\right]$，$\displaystyle\int_{0}^{\frac{\pi}{2}-\delta}\sin^{2k}x\, \mathrm{d}{x}<\displaystyle\int_{0}^{\frac{\pi}{2}-\delta}\sin^{2k}\left(\displaystyle\frac{\pi}{2}-\delta\right)\, \mathrm{d}{x}=\left(\displaystyle\frac{\pi}{2}-\delta\right)\sin^{2k}\left(\displaystyle\frac{\pi}{2}-\delta\right)<\displaystyle\frac{\pi}{2}\sin^{2k}\left(\displaystyle\frac{\pi}{2}-\delta\right)$。当 $k$ 足够大的时候（$k>\displaystyle\frac{\ln\left(\displaystyle\frac{2\varepsilon}{\pi}\right)}{2\ln\left(\sin\left(\displaystyle\frac{\pi}{2}-\delta\right)\right)}$）就有这一部分小于 $\displaystyle\frac{\varepsilon}{2}$。综上，$k$ 足够大时，$\displaystyle\int_{0}^{\frac{\pi}{2}}{\sin^{2k}x}\, \mathrm{d}{x}<\varepsilon$。

所以 $\displaystyle\lim_{k\to \infty}\displaystyle\int_{0}^{\frac{\pi}{2}}{\sin^{2k}x}\, \mathrm{d}{x}=0$，$\displaystyle\lim_{k\to \infty}\displaystyle\frac{\left(2k-1\right)!!}{\left(2k\right)!!}=0$。

这一积分的更著名结论是沃利斯乘积：

$$
\displaystyle\frac{\pi}{2}=\displaystyle\lim_{k\to \infty}\displaystyle\frac{\left(\left(2k\right)!!\right)^2}{\left(2k-1\right)!!\left(2k+1\right)!!}
$$

但超出这里范围，故不详细说明。

<br/>

---

## 习题 6.7 魏尔斯特拉斯逼近定理

卡尔·魏尔斯特拉斯 (Karl Weierstrass) 的名字与我们已经讨论过的许多重要结果联系在一起。波尔查诺-魏尔斯特拉斯定理对于理解前面章节中得出的收敛性、完备性和紧致性之间的关系至关重要。在本章中，魏尔斯特拉斯 M-判别法作为证明无穷级数一致收敛的主要工具出现。

正如在 5.4 节中所讨论的，魏尔斯特拉斯还在 1872 年给出了最早的连续但处处不可导函数的例子之一。

1885 年，魏尔斯特拉斯证明了一个结果，这与他那个处处不可导的函数形成了一个有趣的对比。这个以他名字命名的定理，后来成为了被称为“逼近论”这一新分析学分支的催化剂。

**定理 6.7.1 (魏尔斯特拉斯逼近定理/Weierstrass Approximation Theorem)**. 设 $f : [a, b] \rightarrow \mathbb{R}$ 是连续的。给定 $\epsilon > 0$，存在一个多项式 $p(x)$ 满足
$$ |f(x) - p(x)| < \epsilon $$
对所有 $x \in [a, b]$ 成立。

不用所有这些符号来重述魏尔斯特拉斯逼近定理 (WAT) 的话，那就是：闭区间上的每一个连续函数都可以被多项式一致逼近。

<br/>

!!! question "练习 6.7.1"
    
    假设 WAT 成立，证明如果 $f$ 在 $[a, b]$ 上连续，那么存在一个多项式序列 $(p_n)$，使得 $p_n \rightarrow f$ 在 $[a, b]$ 上一致收敛。

假设 WAT 成立的情况下，对 $\forall\ n \in \mathbb{N}$，存在多项式 $p_n$，使得 $\left|f(x)-p_n(x)\right|<\displaystyle\frac{1}{n}$。

所以对 $\forall\ \varepsilon>0$，存在 $N>\displaystyle\frac{1}{\varepsilon}$，对 $\forall\ n>N$，$\forall\ x$ 在定义域内均有 $\left|f(x)-p_n(x)\right|<\displaystyle\frac{1}{n}<\varepsilon$。所以 $p_n\to f$ 在 $[a,b]$ 上一致收敛。

<br/>

---

我们在上一节的工作为理解 WAT 在说什么提供了一个很好的起点。给定一个函数，例如 $\sin(x)$，我们在例 6.6.4 中看到，产生的泰勒级数在紧集上一致收敛回 $\sin(x)$。因为泰勒级数的部分和是多项式，这个例子构成了 WAT 在 $f(x) = \sin(x)$ 这一非常特殊情况下的证明。然而，应该清楚的是，泰勒级数在一般情况下是行不通的。为了构造泰勒级数，我们需要 $f$ 是一个无限次可导的函数（即使那样，泰勒级数也可能无法逼近 $f$），而 WAT 仅要求 $f$ 是连续的。

那么，对于这样一个定理的真实性，我们应该感到惊讶吗？这很难说。在纯粹直观的层面上，如果我们考虑 $[-1, 1]$ 上的平滑曲线如 $f(x) = \sqrt{1 - x}$，那么不需要太多想象力就能相信，可能存在一个多项式，随着 $x$ 在定义域上移动，它与 $\sqrt{1 - x}$ 非常贴近。但是 5.4 节的一个教训是：连续函数不一定是平滑的。尽管它不是魏尔斯特拉斯最初的例子，但仔细观察图 5.7 中展示的处处不可导函数也能说明这一点。尽管该图具有难以想象的锯齿状性质，根据 WAT，仍然能够找到一个多项式，在任何指定的精度下一致逼近这个难以控制的函数。

### 插值 (Interpolation)

魏尔斯特拉斯的定理涉及逼近多项式，但是要感受这个结果的内涵，一个好方法是暂时将 WAT 中的多项式替换为所有连续的、分段线性函数的集合。

![Figure 6.6](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/2_423_201_678_614_0.jpg)
*图 6.6: $f(x) = \sqrt{1 - x}$ 的折线逼近。*

**定义 6.7.2**. 我们称一个连续函数 $\phi : [a, b] \rightarrow \mathbb{R}$ 是折线函数（polygonal），如果存在 $[a, b]$ 的一个分割
$$ a = x_0 < x_1 < x_2 < \dots < x_n = b $$
使得 $\phi$ 在每一个子区间 $[x_{i-1}, x_i]$ 上是线性的，其中 $i = 1, \dots, n$。

术语“插值”指的是寻找一个图形经过给定点集的函数的过程。例如，如果我们取这些点
$$ (0, 1), \left(\frac{1}{4}, \frac{\sqrt{3}}{2}\right), \left(\frac{3}{4}, \frac{1}{2}\right), (1, 0) $$
那么存在一个显而易见的折线函数来插值这些点：它就是我们通过用线段连接这些点得到的函数。现在这四个点都位于 $f(x) = \sqrt{1 - x}$ 的图像上，并且注意到由此产生的折线插值相当合理地模仿了 $f$ 的图像 (图 6.6)。这并非巧合。

**定理 6.7.3**. 设 $f : [a, b] \rightarrow \mathbb{R}$ 是连续的。给定 $\varepsilon > 0$，存在一个折线函数 $\phi$ 满足
$$ |f(x) - \phi(x)| < \varepsilon $$
对所有 $x \in [a, b]$ 成立。

<br/>

<a id="6.7.2"></a>

!!! question "练习 6.7.2"
    
    证明定理 6.7.3。
    
    定理 6.7.3 证明的策略是首先在 $f$ 的图像上选择适当数量的点，然后证明对这些点进行折线插值能达到目的。

依题意，$f$ 在 $[a,b]$ 上一致连续。所以对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，使得对 $\forall\ \left|x-y\right|\leq \delta$（这里取等方便后续讨论） 有 $\left|f(x)-f(y)\right|<\varepsilon$。

一致连续给我们的灵感是，只要区间划分得足够小，那么一整个区间的函数值都变化不大，这给我们创造与之相近的折线函数提供了契机。

所以在 $[a,b]$ 上作分割 $a=x_0<x_1<\cdots<x_n=b$ 使得对 $\forall\ i\in \left\{1,2,\ldots,n\right\}$，$x_i-x_{i-1}=\delta$，因此 $\forall\ x,y\in [x_{i-1},x_i]$ 均有 $\left|f(x)-f(y)\right|<\varepsilon$。

现在我们将注意力放在任意的一个区间上，对 $\forall\ i\in \left\{1,2,\ldots,n\right\}$，令 $\phi(x)$ 为连接区间 $[x_{i-1},x_i]$ 两端点的线段即

$$\phi(x)=\displaystyle\frac{f(x_{i})-f(x_{i-1})}{x_i-x_{i-1}}(x-x_{i-1})+f(x_{i-1})$$

我们希望这个线性函数能足够拟合 $f$，所以进行计算：

$$
\begin{align*}
    &\mathrel{\phantom{=}}\left|\phi(x)-f(x)\right|=\left|\displaystyle\frac{f(x_{i})-f(x_{i-1})}{x_i-x_{i-1}}(x-x_{i-1})+f(x_{i-1})-f(x)\right|\\
    &=\displaystyle\frac{1}{x_i-x_{i-1}}\Bigl\lvert \bigl(f(x_i)-f(x_{i-1})\bigr)\left(x-x_{i-1}\right)+\bigl(f(x_{i-1})-f(x)\bigr)\left(x_i-x_{i-1}\right)\Bigr\rvert\\
    &=\displaystyle\frac{1}{x_{i}-x_{i-1}}\Bigl\lvert \bigl(f(x_i)-f(x_{i-1})\bigr)\left(x-x_{i-1}\right)+\bigl(f(x_{i-1})-f(x)\bigr)\left(x_i-x\right)+\bigl(f(x_{i-1})-f(x)\bigr)\left(x-x_{i-1}\right)\Bigr\rvert\\
    &=\displaystyle\frac{1}{x_{i}-x_{i-1}}\Bigl\lvert \bigl(f(x_{i})-f(x)\bigr)(x-x_{i-1})-\bigl(f(x)-f(x_{i-1})\bigr)(x_i-x)\Bigr\rvert\\
    &\leq \displaystyle\frac{1}{x_{i}-x_{i-1}}\Bigl(\bigl|f(x_{i})-f(x)\bigr|\left(x-x_{i-1}\right)+\bigl|f(x)-f(x_{i-1})\bigr|\left(x_i-x\right)\Bigr)\\
    &<\displaystyle\frac{1}{x_{i}-x_{i-1}}\bigl(\varepsilon\left(x-x_{i-1}\right)+\varepsilon\left(x_i-x\right)\bigr)=\varepsilon
\end{align*}
$$

所以在每个区间上都同理取这样的线段，组成 $[a,b]$ 上的函数 $\phi(x)$。对 $\forall\ x\in [a,b]$，$\exists\ i\in \left\{1,2,\cdots,n\right\}$ 使得 $x\in [x_{i-1},x_{i}]$。则对这个区间上的 $\phi(x)$ 有 $\left\lvert f(x)-\phi(x) \right\rvert<\varepsilon$。

综上，对 $\forall\ \varepsilon>0$，存在这样的 $\phi(x)$ 使得 $\left|f(x)-\phi(x)\right|<\varepsilon$ 对所有 $x\in [a,b]$ 成立。

<mark>附录</mark>

上面化简所使用的方法其实是比例分割。函数在 $x$ 处的取值，也可以看作这条线段在 $x$ 处进行的分割，按比例分割成 $x-x_{i-1}$，$x_i-x$ 两部分。因此 $\displaystyle\frac{x-x_{i-1}}{x_i-x_{i-1}}=\lambda$，$\displaystyle\frac{x_i-x}{x_i-x_{i-1}}=1-\lambda$ 就是两部分的比例。所以 $\phi(x)$ 就能转写成 $\phi(x_{i-1})$ 和 $\phi(x_{i})$ 的比例和（转写可以用通过比例进行证明，当然看成共线向量进行论证也是可以的）：

$$
\phi(x)=\lambda\phi(x_{i})+(1-\lambda)\phi(x_{i-1})=\lambda f(x_i)+(1-\lambda)f(x_{i-1})
$$

这样看是不是清晰多了？令 $f(x)=\lambda f(x)+\left(1-\lambda\right)f(x)$，写成同比例的形式，正好能对应起来计算：

$$
\begin{align*}
    \mathrel{\phantom{=}}\left\lvert \phi(x)-f(x) \right\rvert=&\bigl\lvert \lambda f(x_i)+(1-\lambda)f(x_{i-1})-\lambda f(x)-\left(1-\lambda\right)f(x) \bigr\rvert\\
    =&\Bigl\lvert \lambda\bigl(f(x_i)-f(x)\bigr)+(1-\lambda)\bigl(f(x_{i-1})-f(x)\bigr) \Bigr\rvert\\
    \leq&\lambda\bigl|f(x_i)-f(x)\bigr|+(1-\lambda)\bigl|f(x_{i-1})-f(x)\bigr|\\
    <&\lambda\varepsilon+(1-\lambda)\varepsilon=\varepsilon
\end{align*}
$$

<br/>

---

请注意定理 6.7.3 与 WAT 有多么相似，唯一的区别在于我们用折线函数代替了多项式。

怀疑类似的策略可能会引出 WAT 的证明并不是没有道理的。我们能通过构造 $f$ 图像上点的多项式插值来证明 WAT 吗？嗯，事实证明不行，但这并不容易看出来。

<br/>

!!! question "练习 6.7.3"
    
    (a) 找到二次多项式 $p(x) = q_0 + q_1x + q_2x^2$，插值 $g(x) = |x|$ 图像上的三个点 $(-1, 1), (0, 0)$ 和 $(1, 1)$。在同一坐标系上画出 $[-1, 1]$ 上的 $g(x)$ 和 $p(x)$。
    
    (b) 找到插值 $g(x) = |x|$ 在点 $x = -1, -1/2, 0, 1/2$ 和 $1$ 处的四次多项式。将其略图添加到 (a) 中的图上。

(a) $p(x)=x^2$。图像如下所示：

![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-05-25%20221133.png)

(b) 四次多项式为 $q(x)=-\displaystyle\frac{4}{3}x^4+\displaystyle\frac{7}{3}x^2$，图像如下所示：

![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/geogebra-export.png)

<br/>

---

前面这个练习可能仍然给人一种印象：多项式插值方法将导向 WAT 的证明，但情况并非如此。继续使用越来越多的等距点集会产生次数极高、振荡剧烈的多项式，它们实际上在插值点之间对 $g$ 的逼近效果很差。实际上，最终得到的这一多项式序列只会在 $x = -1, 0$ 或 $1$ 时收敛到 $g(x)$。

### 逼近绝对值函数 (Approximating the Absolute Value Function)

在遇到暂时的死胡同后，我们需要后退一步，换一个方向。让我们回到断言每个连续函数都能被折线函数一致逼近的定理 6.7.3。这感觉应该是迈向 WAT 证明的充满希望的第一步，而且确实如此。如果我们能找到一种利用多项式逼近任意折线函数的方法，那么利用三角不等式就能完成此证明。

在我们对这条攻击路线过度兴奋之前，请记住，练习 6.7.3 中的绝对值函数就是折线函数的一个例子，而我们目前还不确定如何构造多项式来逼近它。然而，改变的是我们这样做的动机。稍加思索就会发现处理绝对值函数可能是解决整个问题的关键。这是为什么呢？每个折线函数都是由在拐角处相接的线段组成的。如果我们能找到一致逼近带有直角原点拐角的 $g(x) = |x|$ 的多项式，那么凭点小聪明，我们应该就能处理更一般的折线函数了，并可以利用定理 6.7.3 来证明 WAT。

### 柯西泰勒级数余项公式 (Cauchy's Remainder Formula for Taylor Series)

展示 $g(x) = |x|$ 是多项式的一致极限的一个优雅方法是通过泰勒级数，这多少有些令人惊讶，因为 $|x|$ 不是可导的。正如我们将看到的，这个技巧是——先从计算无限次可导函数 $\sqrt{1 - x}$ 的泰勒级数开始。

<br/>

!!! question "练习 6.7.4"
    
    证明 $f(x) = \sqrt{1 - x}$ 具有泰勒级数系数 $a_n$，其中 $a_0 = 1$ 以及
    
    $$ a_n = \frac{-1 \cdot 3 \cdot 5\cdots (2n - 3)}{2 \cdot 4 \cdot 6\cdots 2n} $$
    
    对于 $n \geq 1$ 成立。

我们在此利用一个常见的泰勒展开式来进行求解：

$$
\left(1+x\right)^\alpha=1+\displaystyle\sum_{n=1}^{\infty} \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!} x^n
$$

令 $\alpha=\displaystyle\frac{1}{2}$，再将 $x$ 替换为 $-x$，就能得到我们满意的结果：

$$
\begin{align*}
    f(x)=\left(1-x\right)^{\frac{1}{2}}=&1+\displaystyle\sum_{n=1}^{\infty} \frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\cdots\left(\frac{1}{2}-n+1\right)}{n!}(-x)^n\\&=1+\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{\left(-1\right)^n1\left(1-2\right)\cdots\bigl(1-2\left(n-1\right)\bigr)}{\left(2n\right)!!}x^n\\&=1+\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{-1\cdot 3\cdot 5\cdots \bigl(2n-3\bigr)}{2\cdot 4\cdot 6\cdots 2n}x^n
\end{align*}
$$

由此得到结果。

<br/>

---

我们的目标是证明
$$ \sqrt{1 - x} = \sum_{n=0}^{\infty} a_n x^n\quad (1)$$
对所有的 $x \in [-1, 1]$ 成立，方法是证明误差函数
$$ E_N(x) = \sqrt{1 - x} - \sum_{n=0}^{N} a_n x^n $$
当 $N \rightarrow \infty$ 时趋向于 0。到目前为止，拉格朗日余项定理一直是处理此类问题的主要工具，但在这种情况下它显得力不从心。为了确切了解为何如此，固定 $x \in (0, 1]$。那么定理 6.6.3 断言存在一个在 $0$ 和 $x$ 之间的 $c$（其依赖于 $N$），使得
$$ E_N(x) = \frac{f^{(N+1)}(c)}{(N+1)!} x^{N+1} $$
$$ = \frac{1}{(N+1)!} \left( \frac{-1 \cdot 3 \cdot 5\cdots (2N - 1)}{2^{N+1}(1 - c)^{N+1/2}} \right) x^{N+1} $$
$$ = \left( \frac{-1 \cdot 3 \cdot 5\cdots (2N - 1)}{2 \cdot 4 \cdot 6\cdots (2N + 2)} \right) \left(\frac{x}{1 - c}\right)^{N+1/2} x^{1/2}. $$
问题在于，当 $c = x$ 时，$x / (1 - c)$ 是最大的，且当 $x$ 大于 $1/2$ 时，$(x/(1-x))^{N+1/2}$ 以指数速度趋于无穷。这并不意味着我们的泰勒级数仅在 $[0, 1/2]$ 上有效；它只是意味着我们找错了余项公式。

<br/>

!!! question "练习 6.7.5"
    
    (a) 听从练习 6.6.9 的建议证明余项的柯西形式：
    
    $$ E_N(x) = \frac{f^{(N+1)}(c)}{N!}(x - c)^N x $$
    
    其中 $c$ 在 $0$ 和 $x$ 之间。
    
    (b) 利用这个结果证明公式 (1) 对所有 $x \in (-1, 1)$ 是成立的。

(a) 

$$
\begin{align*}
    E_N(x)&=\displaystyle\frac{f^{(N+1)}(c)}{N!}(x - c)^N x=\left(\displaystyle\frac{-1\cdot 3\cdot 5\cdots \left(2N-1\right)}{2\cdot 4\cdot 6\cdots 2N \cdot 2}\right)\left(1-c\right)^{-(N+\frac{1}{2})}\left(x-c\right)^Nx\\&=\left(\displaystyle\frac{-1\cdot 3\cdot 5\cdots \left(2N-1\right)}{2\cdot 4\cdot 6\cdots 2N \cdot 2}\right)\left(\displaystyle\frac{x-c}{1-c}\right)^N\left(\displaystyle\frac{x}{\sqrt{1-c}}\right)
\end{align*}
$$

(b) 上述表达式中，$\displaystyle\frac{-1\cdot 3\cdot 5\cdots \left(2N-1\right)}{2\cdot 4\cdot 6\cdots 2N \cdot 2}$ 和 $\displaystyle\frac{x}{\sqrt{1-c}}$ 都是有界量，所以证明收敛的关键在 $\left(\displaystyle\frac{x-c}{1-c}\right)^N$。

$\displaystyle\frac{x-c}{1-c}=1-\displaystyle\frac{1-x}{1-c}$。将 $c$ 看作变量，利用此判断单调性。

$x=0$ 时自然收敛。$0<x<1$ 时，$\displaystyle\frac{x-c}{1-c}>0$ 递减，所以在 $c=0$ 时为最大值 $x$。此时 $\left(\displaystyle\frac{x-c}{1-c}\right)^N<x^N$，故有 $\displaystyle\lim_{N\to \infty}\left(\displaystyle\frac{x-c}{1-c}\right)^N=0\Rightarrow\displaystyle\lim_{N\to \infty}E_N(x)=0$。

$-1<x<0$ 时，$\displaystyle\frac{x-c}{1-c}<0$ 递减，所以在 $c=0$ 时绝对值取最大值 $\left\lvert x \right\rvert$，此时由于 $\left\lvert x \right\rvert<1$，同上也可得 $\displaystyle\lim_{N\to \infty}E_N(x)=0$。

综上，公式 (1) 对所有 $x\in (-1,1)$ 都成立。

---

<br/>

尽管柯西余项定理没有告诉我们，但公式 (1) 在 $x = \pm 1$ 处也是成立的。

!!! question "练习 6.7.6"
    
    (a) 令
    $$ c_n = \frac{1 \cdot 3 \cdot 5\cdots (2n - 1)}{2 \cdot 4 \cdot 6\cdots 2n} $$
    证明 $c_n < \displaystyle\frac{2}{\sqrt{2n + 1}}$。
    
    (b) 利用 (a) 来证明 $\sum_{n=0}^{\infty} a_n$ 收敛 (此处事实上是绝对收敛)，其中 $a_n$ 是练习 6.7.4 中生成的泰勒系数序列。
    
    (c) 仔细解释这如何验证了公式 $(1)$ 对所有的 $x \in [-1, 1]$ 成立。

(a) 这里利用一个不等式：$\sqrt{(n-1)(n+1)}<n$

由此我们有

$$
\begin{align*}
    \displaystyle\prod_{i=1}^{n}2i&>\displaystyle\prod_{i=1}^{n}\sqrt{(2i-1)(2i+1)}\\&=\displaystyle\prod_{i=1}^{n}(2i-1)\sqrt{2n+1}
\end{align*}
$$

所以

$$
\begin{align*}
    c_n=\displaystyle\frac{\displaystyle\prod_{i=1}^{n}\left(2i-1\right)}{\displaystyle\prod_{i=1}^{n}2i}<\displaystyle\frac{\displaystyle\prod_{i=1}^{n}\left(2i-1\right)}{\displaystyle\prod_{i=1}^{n}\left(2i-1\right)\sqrt{2n+1}}=\displaystyle\frac{1}{\sqrt{2n+1}}
\end{align*}
$$

至于题目要求就更不用说了。

(b) $a_n=\displaystyle\frac{-1\cdot 3\cdot 5\cdots (2n-3)}{2\cdot 4\cdot 6 \cdots 2n}=-\displaystyle\frac{c_n}{2n-1}$。$(n\geq 1)$

所以 $\left\lvert a_n \right\rvert<\displaystyle\frac{1}{(2n-1)\sqrt{2n+1}}<\displaystyle\frac{1}{(2n-1)^{3/2}}$。由比较判别法，$\displaystyle\sum_{n=0}^{\infty}\left\lvert a_n \right\rvert< a_0+\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{1}{(2n-1)^{3/2}}$ 收敛，所以 $\displaystyle\sum_{n=0}^{\infty}a_n$ 绝对收敛。

(c) 对于 $x=1$，$\displaystyle\sum_{n=0}^{\infty}a_nx^n=\displaystyle\sum_{n=0}^{\infty}a_n$ 绝对收敛，因此泰勒展开式在 $[-1,1]$ 上一致收敛，即连续。

又 $f(x)=\sqrt{1-x}$ 在 $[-1,1]$ 上连续，且 $f(x)=\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $(-1,1)$ 上成立，所以，$f(x)=\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $[-1,1]$ 上成立。

<br/>

---

回顾一下，我们的目标是找到在包含原点处不可导点的一个区间上一致逼近绝对值函数的多项式。我们对 $\sqrt{1 - x}$ 的泰勒级数为处理这个任务提供了一条巧妙的捷径。

!!! question "练习 6.7.7"
    
    (a) 利用 $|x| = \sqrt{x^2}$ 这一事实证明，给定 $\varepsilon > 0$，存在一个多项式 $q(x)$ 满足
    
    $$ \big| |x| - q(x) \big| < \varepsilon $$
    
    对于所有的 $x \in [-1, 1]$ 成立。
    
    (b) 将此结论推广到任意区间 $[a, b]$。

(a) 将 $1-x$ 中的 $x$ 换成 $1-x^2$，得到相应的泰勒展开式：

$\sqrt{x^2}=\displaystyle\sum_{n=0}^{\infty}a_n\left(1-x^2\right)^n$。

因为 $x\in [-1,1]$ 时，$1-x^2\in [0,1]$，而 $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ 在 $[0,1]$ 上一致收敛，所以这个新级数在 $[-1,1]$ 上同样一致收敛。

这样就说明了上述等号的合理性，且对 $\forall\ \varepsilon>0$，$\exists\ N>0$，对 $\forall\ k>N$，$\forall\ x\in [-1,1]$，有

$$
\left\lvert \displaystyle\sum_{n=0}^{\infty}a_n\left(1-x^2\right)^n-\displaystyle\sum_{n=0}^{k}a_n\left(1-x^2\right)^n \right\rvert<\varepsilon
$$

于是取多项式 $q(x)=\displaystyle\sum_{n=0}^{N+1}a_n\left(1-x^2\right)^n$，再由上述等式，即得

$$
\bigl\lvert \left\lvert x \right\rvert-q(x) \bigr\rvert<\varepsilon
$$

(b) 任意区间上的 $\left\lvert x \right\rvert$ 与 $[-1,1]$ 上的形状其实大差不差。我们只要在包含 $[a,b]$ 的对称区间上逼近就能同时逼近此区间。

令 $c=\max\left\{\left\lvert a \right\rvert,\left\lvert b \right\rvert\right\}$，则 $c>0$，所以 $[a,b]\subseteq [-c,c]$，我们准备在 $[-c,c]$ 上进行逼近。

$x\in [-c,c]$ 时，$\displaystyle\frac{x}{c}\in [-1,1]$，所以 $\displaystyle\sum_{n=0}^{\infty}a_n\left(1-\left(\displaystyle\frac{x}{c}\right)^2\right)^n$ 在 $[-c,c]$ 上一致收敛。又因为 $\left\lvert \displaystyle\frac{x}{c} \right\rvert=\displaystyle\frac{\left\lvert x \right\rvert}{c}=\displaystyle\sum_{n=0}^{\infty}a_n\left(1-\left(\displaystyle\frac{x}{c}\right)^2\right)^n$，所以同 (a)，对 $\forall\ \varepsilon>0$，存在多项式 $q\left(\displaystyle\frac{x}{c}\right)$ 使得

$$
\left\lvert \displaystyle\frac{\left\lvert x \right\rvert}{c}-q\left(\displaystyle\frac{x}{c}\right) \right\rvert<\displaystyle\frac{\varepsilon}{c}
$$

再整理一下就能得到对应多项式 $cq\left(\displaystyle\frac{x}{c}\right)$:

$$
\left\lvert \left\lvert x \right\rvert-cq\left(\displaystyle\frac{x}{c}\right) \right\rvert<\varepsilon
$$

---

<br/>

### 证明 WAT (Proving WAT)

我们前面暗示过，对于绝对值函数这个特例证明是整个 WAT 证明的关键，现在是时候填补细节了。

<br/>

<a id="6.7.8"></a>

!!! question "练习 6.7.8"
    
    (a) 固定 $a \in [-1, 1]$ 并画出
    $$ h_a(x) = \frac{1}{2}(|x - a| + (x - a)) $$
    在 $[-1, 1]$ 上的图像。注意 $h_a$ 是一个折线函数，且对于所有 $x \in [-1, a]$，都有 $h_a(x) = 0$。
    
    (b) 解释为什么我们能确定 $h_a(x)$ 可以在 $[-1, 1]$ 上被一个多项式一致逼近。
    
    (c) 令 $\phi$ 是一个折线函数，它在由下列分割所产生的每一个子区间上为线性：
    
    $$ -1 = a_0 < a_1 < a_2 < \dots < a_n = 1. $$
    
    证明存在常数 $b_0, b_1, \dots, b_{n-1}$ 使得
    
    $$ \phi(x) = \phi(-1) + b_0 h_{a_0}(x) + b_1 h_{a_1}(x) + \dots + b_{n-1} h_{a_{n-1}}(x) $$
    
    对于所有 $x \in [-1, 1]$ 成立。
    
    (d) 完成区间 $[-1, 1]$ 上的 WAT 的证明，并接着将其推广到一般的任意区间 $[a, b]$。

(a) ![](https://cdn.jsdelivr.net/gh/calculus1437/calculus1437.github.io@main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-06-11%20093449.png)

(b) $h_a(x)=\displaystyle\frac{1}{2}\bigl(\left\lvert x-a \right\rvert+\left(x-a\right)\bigr)=\displaystyle\frac{1}{2}\left(x-a\right)+\displaystyle\frac{1}{2}\left\lvert x-a \right\rvert$，其中 $\displaystyle\frac{1}{2}\left(x-a\right)$ 是一个多项式，而 $\displaystyle\frac{1}{2}\left\lvert x-a \right\rvert$ 可以被一个多项式一致逼近，合起来就得到 $h_a(x)$ 也可以被多项式一致逼近。

(c) 在某个区间 $[a_{i-1},a_i]$ 上，根据 $h_{a_k}(x)$ 的定义，可以求得

$$
h_{a_k}(x)=0\quad (k\geq i)
$$

这样，所有的区间都只被该区间与之前下标的 $h_{a_k}(x)$ 所影响，于是我们可以从左往右逐区间构造对应的 $h_{a_k}(x)$ 以满足要求。

首先，对于 $x\in [a_0,a_1]$，$\phi(x)=\displaystyle\frac{\phi(a_1)-\phi(a_0)}{a_1-a_0}(x-a_0)+\phi(a_0)$，而 $h_{a_0}(x)=\displaystyle\frac{1}{2}\left(\left\lvert x-a_0 \right\rvert+\left(x-a_0\right)\right)=x-a_0$，是 $[a_0,a_1]$ 上的线性函数，我们给它调个角度就可以达到 $\phi(x)$ 的要求了。具体来说就是取斜率：令 $b_0=\displaystyle\frac{\phi(a_1)-\phi(a_0)}{a_1-a_0}$，那么就有

$$
\phi(x)=\phi(-1)+b_0h_{a_0}(x)\quad \bigl(x\in [a_0,a_1]\bigr)
$$

接下来，对于 $x\in [a_1,a_2]$，$\phi(x)=\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}(x-a_1)+\phi(a_1)$，而 $h_{a_1}(x)=\displaystyle\frac{1}{2}\left(\left\lvert x-a_1 \right\rvert+\left(x-a_1\right)\right)=x-a_1$，跟上面一样。这时候 $h_{a_1}(x)$ 仍然是作为一个调斜率的工具，用来调整前面区间 $h_{a_0}(x)$ 带来的影响。

$$
\begin{align*}
    \phi(x)&=\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}\left(x-a_1\right)+\phi(a_1)\\
    &=\phi(a_0)+\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}\left(x-a_1\right)+\phi(a_1)-\phi(a_0)\\
    &=\phi(-1)+b_0h_{a_0}(x)-\left(\displaystyle\frac{\phi(a_1)-\phi(a_0)}{a_1-a_0}\left(x-a_0\right)-\bigl(\phi(a_1)-\phi(a_0)\bigr)\right)+\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}\left(x-a_1\right)\\
    &=\phi(-1)+b_0h_{a_0}(x)+\left(\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}-\displaystyle\frac{\phi(a_1)-\phi(a_0)}{a_1-a_0}\right)\left(x-a_1\right)\\
    &=\phi(-1)+b_0h_{a_0}(x)+\left(\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}-b_0\right)\left(x-a_1\right)
\end{align*}
$$

所以 $b_1=\displaystyle\frac{\phi(a_2)-\phi(a_1)}{a_2-a_1}-b_0$。

从几何直观上很好理解，毕竟每个 $h$ 函数的贡献都是一个 $x$，所以 $b_0+b_1$ 就是第二部分区间的斜率。

我们直接证明一般性情形。

对 $k\in \mathbb{N^+}$，$k\in [0,n-2]$，因为 $x\in [a_k,a_{k+1}]$ 时，

$$
\begin{align*}
    \phi(x)&=\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}(x-a_{k+1}+a_{k+1}-a_k)+\phi(a_k)\\
    &=\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}(x-a_{k+1})+\phi(a_{k+1})
\end{align*}
$$

所以对于 $x\in [a_{k+1},a_{k+2}]$，有

$$
\begin{align*}
    \phi(x)&=\displaystyle\frac{\phi(a_{k+2})-\phi(a_{k+1})}{a_{k+2}-a_{k+1}}(x-a_{k+1})+\phi(a_{k+1})\\
    &=\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}(x-a_{k+1})+\phi(a_{k+1})+b_{k+1}(x-a_{k+1})\\
    &=\left(\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}+b_{k+1}\right)(x-a_{k+1})+\phi(a_{k+1})
\end{align*}
$$

所以 $b_{k+1}=\displaystyle\frac{\phi(a_{k+2})-\phi(a_{k+1})}{a_{k+2}-a_{k+1}}-\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}$。特殊地，$b_0=\displaystyle\frac{\phi(a_{1})-\phi(a_0)}{a_{1}-a_0}$。

所以，对 $\forall\ k\in [0,n-1]$，总有

$$
\begin{cases}
    b_0=\displaystyle\frac{\phi(a_{1})-\phi(a_0)}{a_{1}-a_0}\\
    \displaystyle\sum_{i=0}^{k}b_i=\displaystyle\frac{\phi(a_{k+1})-\phi(a_k)}{a_{k+1}-a_k}
\end{cases}
$$

由上述构造，即得 $\phi(x)=\phi(-1)+\displaystyle\sum_{i=0}^{n-1}b_ih_{a_i}(x)$。

(d) 由前面的论述，每个 $h_{a_i}(x)$ 均能被多项式一致逼近，所以它们的线性和再加上个常数，即上面 $\phi(x)$ 的形式，当然能被多项式一致逼近。

所以对任意连续函数 $f:[-1,1]\to \mathbb{R}$，对任意 $\varepsilon>0$，存在一个折线函数 $\phi$ 使得对 $\forall\ x\in [-1,1]$，$\bigl\lvert f(x)-\phi(x) \bigr\rvert<\displaystyle\frac{\varepsilon}{2}$。

而对上述的 $\varepsilon$，又存在一个多项式 $p(x)$，使得对上述 $\phi(x)$，对 $\forall\ x\in [-1,1]$，有 $\bigl\lvert \phi(x)-p(x) \bigr\rvert<\displaystyle\frac{\varepsilon}{2}$。

所以对 $\forall\ x\in [-1,1]$，$\bigl\lvert f(x)-p(x) \bigr\rvert\leq \bigl\lvert f(x)-\phi(x) \bigr\rvert+\bigl\lvert \phi(x)-p(x) \bigr\rvert<\varepsilon$。我们证明了 $[-1,1]$ 上的 WAT。

要将结论推广到 $[a,b]$，我们需要补充 $\phi(x)$ 在此区间上的多项式逼近性。幸运的是，我们已经证明了 $[a,b]$ 上的绝对值函数也能被多项式一致逼近，这样同上，我们就能得到结论了。

<br/>

!!! question "练习 6.7.9"
    
    (a) 找一个反例表明如果我们将闭区间 $[a, b]$ 替换为开区间 $(a, b)$，则 WAT 不再成立。
    
    (b) 如果我们将 $[a, b]$ 替换为闭集 $[a, \infty)$ 会怎样？定理仍然成立吗？$\phantom]$

(a) WAT 的证明依赖闭区间上连续函数的一致连续性，所以构造不一致连续的函数应该能将其破坏。

令 $f(x)=\sin\left(\displaystyle\frac{1}{x}\right)$，$x \in (0,1)$。它在 $0$ 的邻域上震荡极其剧烈，而多项式在此处表现出非常稳定的特性，由此我们给出证明。

假设对某个 $0<\varepsilon<\displaystyle\frac{1}{10^9}$，存在一个多项式 $p(x)$ 使得 $\bigl\lvert f(x)-p(x) \bigr\rvert<\varepsilon$ 对 $\forall\ x\in (0,1)$ 成立，现在考察 $0$ 处邻域：

对上述的 $\varepsilon$，存在 $\delta>0$ 使得对 $\forall\ x\in (0,\delta)$，$\bigl\lvert p(x)-p(0) \bigr\rvert<\varepsilon$，与上式联立即得 $\bigl\lvert f(x)-p(0) \bigr\rvert<2\varepsilon$。

现在，由于 $\exists\ x_1,x_2\in (0,\delta)$，使得 $f(x_1)=1$，$f(x_2)=-1$，那么 $\bigl\lvert f(x_1)-p(0) \bigr\rvert<2\varepsilon$，$\bigl\lvert f(x_2)-p(0) \bigr\rvert<2\varepsilon$，再联立得 $\bigl\lvert f(x_1)-f(x_2) \bigr\rvert<4\varepsilon$，矛盾。

所以 WAT 在开区间上不成立。

<mark>我们还可以从另一个角度考虑。</mark>假设 $f(x)$ 满足 WAT ，则存在一个多项式序列 $\left\{p_n\right\}$ 一致收敛于 $f(x)$。因为任意的多项式在 $[a,b]$ 上均一致连续，所以 $p_n$ 在 $(a,b)$ 上也一致连续。现在的关键就是，如果能证明一致连续的序列一致收敛到的函数一定也是一致连续的，就能直接证明 $(a,b)$ 上连续但不一致连续的函数不满足 WAT 了。

由一致收敛，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得 $\bigl\lvert p_N(x)-f(x) \bigr\rvert<\displaystyle\frac{\varepsilon}{3}$，对 $\forall\ x\in (a,b)$ 成立。

由一致连续，对 $\exists\ \delta>0$，使得对 $\forall\ \left\lvert x-y \right\rvert<\delta$，$\bigl\lvert p_N(x)-p_N(y) \bigr\rvert<\displaystyle\frac{\varepsilon}{3}$。

现在，我们有 $\bigl\lvert p_N(x)-f(x) \bigr\rvert<\displaystyle\frac{\varepsilon}{3}$，$\bigl\lvert p_N(y)-f(y) \bigr\rvert<\displaystyle\frac{\varepsilon}{3}$ 和 $\bigl\lvert p_N(x)-p_N(y) \bigr\rvert<\displaystyle\frac{\varepsilon}{3}$，三者联合便得到 $\bigl\lvert f(x)-f(y) \bigr\rvert<\varepsilon$，所以 $f$ 在 $(a,b)$ 上一致连续。

<mark>当然这里还有一个速证，</mark>若 $\left\{p_n\right\}$ 在 $(a,b)$ 上一致收敛，如果能证得 $\left\{p_n\right\}$ 在 $[a,b]$ 上也一致收敛的话，那么它将收敛到一个闭区间上连续的函数 $F$，而 $F$ 和 $f$ 在 $(a,b)$ 上是相同的，由 $F$ 一致连续就能推及 $f$ 一致连续了。下面给出证明：

若 $\left\{p_n\right\}$ 在 $(a,b)$ 上一致收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ m,n>N$，$\forall\ x\in (a,b)$，均有 $\bigl\lvert p_m(x)-p_n(x) \bigr\rvert<\varepsilon$。由连续性可得在 $x\in \left\{a,b\right\}$ 处也有 $\bigl\lvert p_m(x)-p_n(x) \bigr\rvert\leq \varepsilon$，这就得到 $\left\{p_n\right\}$ 在 $[a,b]$ 上同样一致收敛于 $F$，且 $F=f$（$x\in (a,b)$），然后 $F$ 在 $[a,b]$ 上连续 $\Rightarrow$ $F$ 在 $[a,b]$ 上一致连续 $\Rightarrow$ $F$ 在 $(a,b)$ 上一致连续 $\Rightarrow$ $f$ 在 $(a,b)$ 上一致连续。

(b) 有大量的多项式在 $[a,+\infty)$ 上本来就是不一致连续的，所以从一致连续的角度恐怕无法证明。不过与上述相对的是，多项式在 $x$ 很大的时候表现得非常不稳定，具体来言是值总会趋向正负无穷，而有极大量的函数是有界的。只要证明出前者，就很容易能找到反例了。

当然前提是 $p(x)$ 不能为常数（毕竟常数也无法拟合变量函数），所以令 $p(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0=x^n\left(1+\displaystyle\frac{a_{n-1}}{x}+\cdots+\displaystyle\frac{a_0}{x^n}\right)$（$n\geq 1$）。

因为 $\displaystyle\lim_{x\to +\infty}\left(1+\displaystyle\frac{a_{n-1}}{x}+\cdots+\displaystyle\frac{a_0}{x^n}\right)=1$，所以 $\exists\ M>0$，使得对 $\forall\ x>M$，$\left( 1+\displaystyle\frac{a_{n-1}}{x}+\cdots+\displaystyle\frac{a_0}{x^n} \right)>\displaystyle\frac{1}{2}$。即对 $\forall\ x>M$，$p(x)>\displaystyle\frac{x^n}{2}$。

所以 $p(x)$ 必定无界，无法在 $[a,+\infty)$ 上拟合有界函数（如 $\sin x$），所以 WAT 在 $[a,+\infty)$ 上不成立。

<br/>

!!! question "练习 6.7.10"
    
    是否存在多项式的一个可数子集 $\mathcal{C}$，具有能够让 $[a, b]$ 上的每个连续函数都能被 $\mathcal{C}$ 中的多项式一致逼近的性质？

我们的证明起始于折线函数的构造。一个足够拟合的折线函数，来自于足够精细的区间分割（细细切做臊子）。所以我们的多项式集最好也能逼近足够密集的 $h_i(x)$。因为 $\mathcal{C}$ 的要求是可数，我们就不妨选择稠密的有理数集来完成这一点。

选择折线函数的子集 $\mathcal{D}=\bigl\{h_{p_i}(x):p_i\in\mathbb{Q}\cap[a,b]\cup\{a,b\}\bigr\}$。当然，它是可数的。

我们的目标有二：

(1) 证明 $\mathcal{D}$ 中的函数经过四则运算能拟合 $[a,b]$ 上的任意连续函数（顶多差一常数）；

(2) 构造出能逼近 $\mathcal{D}$ 中任意函数的可数多项式集 $\mathcal{B}$。

(3) 最后再进行拼合，在这些基础上构造一个能满足四则运算组合的可数集 $\mathcal{C}$。

(1) 对 $[a,b]$ 上任意的连续函数 $f$：对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ \left\lvert x-y \right\rvert<\delta$ 有 $\bigl\lvert f(x)-f(y) \bigr\rvert<\varepsilon$。

现在，取 $(a,b)$ 中有限个有理数点与 $a,b$ 两端点 $a=p_0<p_1<p_2<\cdots<p_n=b$ 对 $[a,b]$ 进行区间分割，使得对 $\forall\ i\in [0,n-1]$，有 $p_{i+1}-p_i<\delta$。现在，令 $\phi(x)$ 为每个子区间上 $f$ 两端点连接而成的线段所拼合而成的 $[a,b]$ 上的折线函数，即

$$
\phi(x)=\displaystyle\frac{f(p_{i+1})-f(p_i)}{p_{i+1}-p_i}(x-p_i)+f(p_i)\quad \bigl(x\in [p_i,p_{i+1}]\bigr)
$$

则由题 [$6.7.2$](#6.7.2) 论述，对 $\forall\ x\in [a,b]$，$\bigl\lvert \phi(x)-f(x) \bigr\rvert<\varepsilon$。再由题 [$6.7.8$](#6.7.8)，$\exists\ b_{p_0}, b_{p_1}, \ldots, b_{p_n}\in \mathbb{R}$ 使得

$$
\phi(x)=\phi(p_0)+\displaystyle\sum_{i=0}^{n-1}b_{p_i}h_{p_i}(x)\quad \bigl(x\in [a,b]\bigr)
$$

这样 $\phi(x)$ 就化为了 $\mathcal{D}$ 中函数的线性组合了。（当然，我们多了一个常数，这将在多项式中补齐）

(2) 由 [$6.7.8$](#6.7.8)，对 $\forall\ h_{p_i}(x)\in \mathcal{D}$，均存在一个一致收敛于它的多项式序列 $\left\{p_{i_n}\right\}$。我们的任务是提取出它的一个可数子列，一种方法是提出这样的 $\left\{p_{i_{k}}\right\}$：

$$
\bigl\lvert h_{p_{i}}(x)-p_{i_{k}}(x) \bigr\rvert<\displaystyle\frac{1}{k} \quad \bigl(x\in [a,b]\bigr)
$$

这样每一个 $h_{p_{i}}$ 都对应着一个拟合它的可数多项式序列。$\mathcal{D}$ 本身也是可数的。而我们知道 $\mathbb{N}^2$ 是可数集，于是这些多项式的集合 $\mathcal{B}$ 也是可数集。

接下来我们需要用这些材料拼凑出能还原 $\phi(x)$ 的集合，这需要 $\mathcal{B}$ 中的多项式，系数，和常数。

虽然系数和常数可能是无理数，但都能被有理数逼近，而且极限满足四则运算的规律，所以加上有理数集就能同时满足系数和常数的需求了。

上面的操作均在 $\mathbb{N}^n$ 之内进行，所以最后拼凑出的 $\mathcal{C}$ 还是可数集。

最后，我们的 $\mathcal{C}$ 由下面的几部分组成：

I. 有理数集 $\mathbb{Q}$，它是特殊的多项式；

II. 每一个 $h_{p_i}$ 所对应的多项式逼近子列 $\left\{p_{i_k}\right\}$；

III. 所有 $p_{i_{k}}$ 间的任意有限线性组合，其中系数均为有理数。

<br/>

!!! question "练习 6.7.11"
    
    假设 $f$ 在 $[a, b]$ 上有连续的导数。证明存在一个多项式 $p(x)$ 使得
    
    $$ |f(x) - p(x)| < \varepsilon \quad \text{并且} \quad |f'(x) - p'(x)| < \varepsilon $$
    
    对所有 $x \in [a, b]$ 成立。

这道问题用定积分会比较好做，这里给出一种用中值定理代替，但本质相同的解法。

由 $f'$ 在 $[a,b]$ 上连续，存在多项式 $q(x)$ 使得 $\bigl\lvert f'(x)-q(x) \bigr\rvert<\varepsilon$。

直观上看，两个导数相差很小的函数，它们本身的变化趋势也相差不大，所以现在的目标是，在 $q(x)$ 众多的原函数中，找一个合适一些的。

$q(x)$ 原函数的存在性可以通过逐项导数来证明。所以，设多项式 $Q(x)$ 满足 $Q'(x)=q(x)$，则上式可化为 $\bigl\lvert f'(x)-Q'(x) \bigr\rvert<\varepsilon$。

接下来的思路是使用中值定理将它们与原函数联系起来（当然最关键的还是增量分析）。一种控制中值定理中 $\xi$ 方式是将 $f(x)-Q(x)$ 当作一个整体，这样就有

$$
\bigl(f(x)-Q(x)\bigr)-\bigl(f(a)-Q(a)\bigr)=\left(x-a\right)\bigl(f'(\xi)-Q'(\xi)\bigr)\quad \bigl(\xi\in (a,x)\bigr)
$$

所以

$$
\Bigl\lvert \bigl(f(x)-Q(x)\bigr)-\bigl(f(a)-Q(a)\bigr) \Bigr\rvert<|x-a|\varepsilon\leq (b-a)\varepsilon
$$

令 $p(x)=Q(x)+f(a)-Q(a)$，则 $p(x)$ 也是多项式，且 $p'(x)=Q'(x)=q(x)$，所以就有

$$
\bigl\lvert f(x)-p(x) \bigr\rvert<\left(b-a\right)\varepsilon\quad \text{并且} \quad \bigl\lvert f'(x)-p'(x) \bigr\rvert<\varepsilon \tag{1}
$$

对 $\forall\ \varepsilon>0$，取 $\varepsilon_{1}>0$ 满足 $\max\left\{\left(b-a\right)\varepsilon_{1},\varepsilon_{1}\right\}<\varepsilon$，将 $\varepsilon_{1}$ 用于上述推导得到 $(1)$ 式，即得结论

$$ 
|f(x) - p(x)| < \varepsilon \quad \text{并且} \quad |f'(x) - p'(x)| < \varepsilon 
$$

<br/>

---

## 6.8 结语

这里魏尔斯特拉斯逼近定理给出的论证可归功于亨利·勒贝格 (Henri Lebesgue)，他在 1898 年发表了他的证明。该方法最大的优点在于其相对的简单性。从单一的特例——绝对值函数——出发，我们通过"拔靴带"方式一步步向上，最后抵达了任意的连续函数。但这种方法的一个缺点是：在到达一般连续函数情形时，没有任何实际的方法能显式写出逼近它的那个多项式的公式。

还有很多其他的 WAT 证明没有这个问题。一个非常著名的证明是由谢尔盖·伯恩斯坦 (Sergei Bernstein) 提供的。伯恩斯坦利用了一个非常重要的多项式族——它们现在被称为伯恩斯坦多项式。魏尔斯特拉斯本人的最初做法也非常优美，他的证明与 8.5 节中傅里叶级数的费耶尔 (Fejér) 定理的证明有许多相似之处。这并非巧合，因为 WAT 也可以作为费耶尔定理的一个推论来证明。（见练习 8.5.11）。

魏尔斯特拉斯逼近定理是建立在闭区间 $[a, b]$ 上的。练习 6.7.9 被包含进来以强调定义域为闭集有界性质的重要性。而如果将 $[a, b]$ 替换成任意的紧集，定理依然成立——这应该不那么令人惊讶。那如果替换多项式的集合如何？是否有其他形式相对简单的连续函数簇能够用来逼近任意连续函数？当然有。在定理 6.7.3 我们了解到折线函数就有这个性质，另外还有其他例子。在 20 世纪 30 年代末，马歇尔·斯通 (Marshall Stone) 证明了魏尔斯特拉斯逼近定理的一个意义深远的推广。斯通版的 WAT 从任意的紧集 $K$ 和 $K$ 上一个连续函数族的集合 $\mathcal{C}$ 开始，并且它们具有以下三个性质：

(i) 常数函数 $k(x) = 1$ 在 $\mathcal{C}$ 中，

(ii) 如果 $p, q \in \mathcal{C}$ 并且 $c \in \mathbb{R}$，那么 $p + q, pq$ 和 $cp$ 全都在 $\mathcal{C}$ 中，

(iii) 如果在 $K$ 中 $x \neq y$，那么存在 $p \in \mathcal{C}$ 使得 $p(x) \neq p(y)$。

在这些条件下，斯通证明了 $K$ 上的任何连续函数都可以被 $\mathcal{C}$ 中的函数一致逼近。这个结果，被称为斯通-魏尔斯特拉斯定理 (Stone-Weierstrass Theorem)，它的证明稍微稍微复杂一点，与前一节勾勒的勒贝格关于 WAT 的证明紧密相连。特别是在这两个论证中，极其关键的基础都依赖于能用多项式逼近绝对值函数。

一个符合斯通-魏尔斯特拉斯定理条件 (ii) 的函数簇被称为一个代数系统 (algebra)。符合条件 (iii) 的代数系统被称为能够“分离点”。在代数系统中含有常数函数 $k(x) = 1$ 确保了我们不会出现对于代数系统内所有函数，在某个 $x_0 \in K$ 都有 $p(x_0) = 0$ 的境地（思考一下为什么需要避免这样）。直接验证多项式集以及折线函数集都是能够“分离点”的代数系统是很容易的，因此 WAT 和定理 6.7.3 都成为了斯通一般结果的特例。作为新例子，考虑只含偶数次幂多项式在区间 $[0, 1]$ 的集合。斯通-魏尔斯特拉斯定理告诉我们，这个多项式子集依然一致逼近任意连续函数。不过如果我们把定义域换成 $[-1, 1]$ 该代数系统就无法再分离点了。作为最后一个例子，考虑集合
$$ \mathcal{C} = \{a_0 + a_1\cos(x) + \dots + a_n\cos(nx) : a_0, a_1, \dots, a_n \in \mathbb{R}\} $$
在 8.5 节中，我们将涉及探讨何时可以把某个函数表示成三角函数无穷级数的傅里叶级数理论。作为那场对话的序幕，注意，斯通-魏尔斯特拉斯定理一开始就告诉我们至少每一个在 $[0, \pi]$ 上的连续函数都是 $\mathcal{C}$ 集合内函数的一致极限。

关于第 6.6 节中对于泰勒展开的故事还值得再提一句。凭借欧拉和其它先辈的聪明才智，我们找到了并在微积分中一系列熟悉的函数上挖掘了其幂级数表达，这就能够理解为什么他们会猜测每个函数都能写成这种形式了（此时术语“函数”往往暗指无限次可导函数）。而随着 1821 年柯西发现在 6.6 节末展现的反例，这种观点得以终结。那么泰勒级数在哪些条件下一定会收敛到它的母函数呢？拉格朗日余项定理阐述了泰勒多项式 $S_N(x)$ 与目标函数 $f(x)$ 之间的差项可以这样写：
$$ E_N(x) = \frac{f^{(N+1)}(c)}{(N+1)!}x^{N+1} $$
由于分母中阶乘 $(N+1)!$ 的增长远快于分子项的 $x^{N+1}$。所以，倘若我们知道譬如
$$ |f^{(N+1)}(c)| \leq M $$
对于所有 $c \in (-R, R)$ 且对所有的整数 $N \in \mathbb{N}$ 都成立，我们能肯定 $E_N(x) \rightarrow 0$ 从而 $S_N(x) \rightarrow f(x)$。对于 $\sin(x), \cos(x), e^x$ 正好就是这样，其导数随 $N \rightarrow \infty$ 的演变并不会增大。当然在确保敛散性的情况下，我们也可以给出更弱的关于 $f^{(N+1)}$ 增长率的约束条件。

柯西的反例究竟应不应该让人感到意外，这其实并不完全清楚。既然之前每一次寻找泰勒级数的尝试都以成功告终，这无疑会给人留下一种印象：幂级数表示是无限次可导函数的一种内在属性。但是请注意这背后隐含的意思：函数 $f$ 的泰勒级数是由 $f$ 及其各阶导数仅在原点处的值构造而成的。如果该泰勒级数在某个区间 $(-R, R)$ 上收敛于 $f$，那么 $f$ 在零点附近的行为就完全决定了它在 $(-R, R)$ 内每一点处的行为。它的一个推论是，如果两个具有泰勒级数的函数在某个小邻域 $(-\varepsilon, \varepsilon)$ 上完全一致，那么这两个函数在任何地方都必须完全相同。当我们以这种角度来看待时，我们或许就不应该期望一个泰勒级数总是能收敛回生成它的那个函数了。正如我们所见，对于实值函数来说这确实不一定成立。然而，令人着迷的是，这类结果对于复变量函数却是成立的。当把实数替换为复数时，导数的定义在符号上看起来一模一样，但其深层含义却有着天壤之别。在复分析中，一个在某个开圆盘（open disc）内每一点都可导的函数，必定能在该集合上无限次可导。这就为推导泰勒级数提供了所有必需的条件，并且在任何情况下，（这种复变函数的）泰勒级数都会在紧集上一致收敛到生成它的那个函数。

---