@import "style.less"

## 习题 6.2 函数序列的一致收敛

> [!question] 习题 6.2.1
> 设
> $$ f_n(x) = \frac{nx}{1 + nx^2} $$
>
> (a) 找出 $(f_n)$ 对所有 $x \in (0, \infty)$ 的点态极限。
> (b) 在 $(0, \infty)$ 上收敛是否一致？
> (c) 在 $(0, 1)$ 上收敛是否一致？
> (d) 在 $(1, \infty)$ 上收敛是否一致？

(a) $\displaystyle\lim_{n\to \infty}f_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x}{\displaystyle\frac{1}{n}+x^2}=\displaystyle\frac{1}{x}$。

(b) 记 $f(x)=\displaystyle\frac{1}{x}$。

因为 $\left|f_n(x)-f(x)\right|=\left|\displaystyle\frac{1}{x(1+nx^2)}\right|<\varepsilon$ 会得到 $n>\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}$。

对 $\forall\ N\in \mathbb{N^+}$，让 $x$ 足够逼近 $0$ 即可使得 $\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}$ 分母足够大分子又大于某正值，最后大于 $N$。具体来说，令 $x<\min\left\{\displaystyle\frac{1}{2\varepsilon},\sqrt[3]{\displaystyle\frac{1}{2\varepsilon N}}\right\}$，则 $\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}> \displaystyle\frac{\frac{1}{2\varepsilon}}{x^3}>N$。

(c) 由 (b) 问，不一致收敛。

(d) 当 $x>1$ 时，$\displaystyle\frac{\displaystyle\frac{1}{\varepsilon}-x}{x^3}=\displaystyle\frac{1}{\varepsilon x^3}-\displaystyle\frac{1}{x^2}<\displaystyle\frac{1}{\varepsilon}$，所以令 $N>\displaystyle\frac{1}{\varepsilon}$，即可保证不等式恒成立，因此一致收敛。

<br/>

> [!question] 习题 6.2.2
> 设
> $$ g_n(x) = \frac{nx + \sin(nx)}{2n} $$
> 找出 $(g_n)$ 在 $\mathbb{R}$ 上的点态极限。在 $[-10, 10]$ 上收敛是否一致？在整个 $\mathbb{R}$ 上收敛是否一致？

$\displaystyle\lim_{n\to \infty}g_n(x)=\displaystyle\lim_{n\to \infty}\displaystyle\frac{x+\displaystyle\frac{\sin(nx)}{n}}{2}=\displaystyle\frac{x}{2}$。

$\left|g_n(x)-\displaystyle\frac{x}{2}\right|=\left|\displaystyle\frac{\sin(nx)}{2n}\right|\leq \displaystyle\frac{1}{2n}$。

所以，对 $\forall\ \varepsilon>0$，令 $N>\displaystyle\frac{1}{2\varepsilon}$，则对 $\forall\ n\geq N$ 和 $\forall\ x\in \mathbb{R}$，都有 $\left|g_n(x)-\displaystyle\frac{x}{2}\right|<\varepsilon$。

所以 $g_n$ 在 $[-10,10]$ 和 $\mathbb{R}$ 上都一致收敛。

<br/>

> [!question] 习题 6.2.3
> 考虑函数序列
> $$ h_n(x) = \frac{x}{1 + x^n} $$
> 在域 $[0, \infty)$ 上。
> (a) 找出 $(h_n)$ 在 $[0, \infty)$ 上的逐点极限。
> (b) 解释为什么我们知道收敛在 $[0, \infty)$ 上不可能一致。
> (c) 选择一个较小的集合，使得收敛在其上一致，并提供论证证明情况确实如此。

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

> [!question] 习题 6.2.4
> 对于每个 $n \in \mathbb{N}$，找出 $\mathbb{R}$ 上函数 $f_n(x) = x/ (1 + nx^2)$ 达到其最大值和最小值的点。用此证明 $(f_n)$ 在 $\mathbb{R}$ 上一致收敛。极限函数是什么？

$f_n(x)$ 是连续可微的。求导可得 $f_n'(x) = \displaystyle\frac{1 - n x^2}{(1 + n x^2)^2}$。

利用中值定理我们可以知道，$f'_n(x)$ 大于 $0$ 则原函数单调递增，小于 $0$ 则单调递减。

因此，$f_n(x)$ 在 $(-\infty,\displaystyle-\frac{1}{\sqrt[]{n}})$ 递减，$(-\displaystyle\frac{1}{\sqrt[]{n}},\displaystyle\frac{1}{\sqrt[]{n}})$ 递增，$(\displaystyle\frac{1}{\sqrt[]{n}}, +\infty)$ 递减。

最大值为 $f_n\left(\displaystyle\frac{1}{\sqrt[]{n}}\right)=\displaystyle\frac{1}{2\sqrt[]{n}}$，最小值为 $f_n\left(-\displaystyle\frac{1}{\sqrt[]{n}}\right)=-\displaystyle\frac{1}{2\sqrt[]{n}}$。

首先，$f(x)=\displaystyle\lim_{n\to \infty}f_n(x)=0$。

因为 $\left|f(x)-f_n(x)\right|\leq \displaystyle\frac{1}{2\sqrt[]{n}}$，所以 $N$ 的选取是与 $x$ 无关的，所以 $\left\{f_n(x)\right\}$ 在 $\mathbb{R}$ 上一致收敛，极限函数为 $f(x)=0$。

<br/>

> [!question] 习题 6.2.5
> 对于每个 $n \in \mathbb{N}$，在 $\mathbb{R}$ 上定义 $f_n$
> $$ f_n(x) = \begin{cases} 1 & \text{if } |x| \ge 1/n \\ n|x| & \text{if } |x| < 1/n \end{cases} $$
> (a) 找出 $(f_n)$ 在 $\mathbb{R}$ 上的逐点极限，并判断收敛是否一致。
> (b) 构造一个连续函数的逐点极限的例子，该极限在紧集 $[-5, 5]$ 上处处收敛到一个在该集上无界的极限函数。

(a) 对 $\forall\ x_0\in \mathbb{R}\setminus\left\{0\right\}$，取 $N>\displaystyle\frac{1}{|x_0|}$，则对 $\forall\ n>N$，$|x_0|\geq \displaystyle\frac{1}{n}$，所以 $f_n(x_0)=1$。

当 $x_0=0$ 时，$f_n(0)=0$。

所以 $f(x)=\begin{cases}    0,\quad \text{if } x=0\\    1,\quad \text{if } x\neq 0\end{cases}$

而一致收敛的连续函数序列总能收敛到连续函数，所以 $\left\{f_n\right\}$ 不一致收敛。

(b) 分段函数能够生成带可去间断点的极限函数。

$$
f_n(x)=\begin{cases}
    \displaystyle\frac{1}{|x|},\quad &\text{if }|x|\geq \displaystyle\frac{1}{n}\\
    n^2x,\quad &\text{if }|x|<\displaystyle\frac{1}{n}
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

> [!question] 习题 6.2.6
> 利用实数收敛序列的 Cauchy 准则 (定理 2.6.4)，为定理 6.2.5 (一致收敛的 Cauchy 准则) 提供一个证明。(首先，定义一个 $f(x)$ 的候选者，然后论证 $f_n \to f$ 一致收敛。)

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

> [!question] 习题 6.2.7
> 假设 $(f_n)$ 在 $A$ 上一致收敛于 $f$，且每个 $f_n$ 在 $A$ 上一致连续。证明 $f$ 在 $A$ 上一致连续。
>

<br/>

> [!question] 习题 6.2.8
> 判断以下猜想哪些为真，哪些为假。为有效的猜想提供证明，为每个无效的猜想提供反例。
> (a) 如果 $f_n \to f$ 在紧集 $K$ 上逐点收敛，则 $f_n \to f$ 在 $K$ 上一致收敛。
> (b) 如果 $f_n \to f$ 在 $A$ 上一致收敛且 $g$ 是 $A$ 上的有界函数，则 $f_n g \to fg$ 在 $A$ 上一致收敛。
> (c) 如果 $f_n \to f$ 在 $A$ 上一致收敛，且每个 $f_n$ 在 $A$ 上有界，则 $f$ 也必须有界。
> (d) 如果 $f_n \to f$ 在集合 $A$ 上一致收敛，且 $f_n \to f$ 在集合 $B$ 上一致收敛，则 $f_n \to f$ 在 $A \cup B$ 上一致收敛。
> (e) 如果 $f_n \to f$ 在区间上一致收敛，且每个 $f_n$ 是递增的，则 $f$ 也是递增的。
> (f) 重复猜想 (e)，假设仅有点态收敛。
>

<br/>

> [!question] 习题 6.2.9
> 假设 $(f_n)$ 在紧集 $K$ 上一致收敛于 $f$，且 $g$ 是 $K$ 上的连续函数，满足 $g(x) \neq 0$。证明 $(f_n/g)$ 在 $K$ 上一致收敛于 $f/g$。
>

<br/>

> [!question] 习题 6.2.10
> 设 $f$ 在整个 $\mathbb{R}$ 上一致连续，并通过 $f_n(x) = f(x + 1/n)$ 定义一个函数序列。证明 $f_n \to f$ 一致收敛。给出一个例子说明如果 $f$ 仅在 $\mathbb{R}$ 上连续而不一致连续，该命题不成立。
>

<br/>

> [!question] 习题 6.2.11
> 假设 $(f_n)$ 和 $(g_n)$ 是一致收敛的函数序列。
> (a) 证明 $(f_n + g_n)$ 是一致收敛的函数序列。
> (b) 给出一个例子说明乘积 $(f_n g_n)$ 可能不一致收敛。
> (c) 证明如果存在一个 $M > 0$ 使得对于所有 $n \in \mathbb{N}$，$|f_n| \le M$ 和 $|g_n| \le M$ 成立，则 $(f_n g_n)$ 确实一致收敛。
>

<br/>

> [!question] 习题 6.2.12
> 定理 6.2.6 有一个部分逆命题。假设 $f_n \to f$ 在紧集 $K$ 上逐点收敛，并且假设对于每个 $x \in K$，序列 $f_n(x)$ 是递增的。按照以下步骤证明，如果 $f_n$ 和 $f$ 在 $K$ 上连续，则收敛是一致的。
>
> (a) 设 $g_n = f - f_n$ 并将前面的假设转化为关于序列 $(g_n)$ 的陈述。
> (b) 设 $\epsilon > 0$ 为任意值，并定义 $K_n = \{x \in K : g_n(x) \ge \epsilon\}$。论证 $K_1 \supseteq K_2 \supseteq K_3 \supseteq \cdots$ 是一个紧集的嵌套序列，并利用这一观察来完成论证。
>

<br/>

> [!question] 习题 6.2.13 (Cantor 函数)
> 回顾第 3.1 节中 Cantor 集 $C \subseteq [0,1]$ 的构造。本练习利用了该讨论中的结果和符号。
>
> (a) 为所有 $x \in [0,1]$ 定义 $f_0(x) = x$。现在，设
> $$ f_1(x) = \begin{cases} (3/2)x & \text{for } 0 \le x \le 1/3 \\ 1/2 & \text{for } 1/3 < x < 2/3 \\ (3/2)x - 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
> 绘制 $f_0$ 和 $f_1$ 在 $[0,1]$ 上，并观察到 $f_1$ 是连续的、递增的，并且在中间三分之一 $(1/3, 2/3) = [0,1] \setminus C_1$ 上是恒定的。
>
> (b) 通过模仿这一过程，将 $f_1$ 的每个非恒定段的中间三分之一压平来构造 $f_2$。具体来说，令
> $$ f_2(x) = \begin{cases} (1/2)f_1(3x) & \text{for } 0 \le x \le 1/3 \\ f_1(x) & \text{for } 1/3 < x < 2/3 \\ (1/2)f_1(3x - 2) + 1/2 & \text{for } 2/3 \le x \le 1 \end{cases} $$
> 如果我们继续这个过程，证明生成的序列 $(f_n)$ 在 $[0,1]$ 上一致收敛。
>
> (c) 设 $f = \lim f_n$。证明 $f$ 是 $[0,1]$ 上的一个连续、递增函数，且满足 $f(0) = 0$ 和 $f(1) = 1$，对于开集 $[0,1] \setminus C$ 中的所有 $x$，满足 $f'(x) = 0$。回想一下，Cantor 集 $C$ 的“长度”为 0。然而，$f$ 在“长度为 1”的集合上保持不变的同时，设法从 0 增加到 1。
>

<br/>

> [!question] 习题 6.2.14
> 回想一下，Bolzano-Weierstrass 定理 (定理 2.5.5) 指出，每个有界的实数序列都有一个收敛的子序列。对于有界函数序列的类似陈述在一般情况下并不成立，但在更强的假设下，可以得出几种不同的结论。一种方法是假设序列中所有函数的共同定义域是可数的。(另一种方法将在接下来的两个练习中探讨。)
>
> 设 $A = \{x_1, x_2, x_3, \dots\}$ 为可数集。对于每个 $n \in \mathbb{N}$，令 $f_n$ 定义在 $A$ 上，并假设存在一个 $M > 0$，使得对于所有 $n \in \mathbb{N}$ 和 $x \in A$，$|f_n(x)| \le M$ 成立。按照以下步骤证明存在 $(f_n)$ 的一个子序列在 $A$ 上逐点收敛。
>
> (a) 为什么实数序列 $f_n(x_1)$ 必然包含一个收敛子序列 $(f_{n_k})$？为了表示函数子序列 $(f_{n_k})$ 是通过考虑函数在 $x_1$ 处的值生成的，我们将使用符号 $f_{n_k} = f_{1,k}$。
> (b) 现在，解释为什么序列 $f_{1,k}(x_2)$ 包含一个有界子序列。
> (c) 仔细构造一个嵌套的子序列族 $(f_{m,k})$，并使用 Cantor 对角线化技术 (来自定理 1.5.1) 生成一个在 $A$ 的每一点都收敛的 $(f_n)$ 的单一子序列。
>

<br/>

> [!question] 习题 6.2.15
> 定义在集合 $E \subseteq \mathbb{R}$ 上的一列函数 $(f_n)$ 被称为**等度连续的**，如果对于每一个 $\epsilon > 0$，存在一个 $\delta > 0$，使得对于 $E$ 中的所有 $n \in \mathbb{N}$ 和 $|x - y| < \delta$，都有 $|f_n(x) - f_n(y)| < \epsilon$。
> (a) 说一列函数 $(f_n)$ 是等度连续的，与仅仅断言序列中的每一个 $f_n$ 都是单独一致连续的，有什么区别？
> (b) 给出一个定性解释，说明为什么序列 $g_n(x) = x^n$ 在 $[0, 1]$ 上不是等度连续的。每个 $g_n$ 在 $[0, 1]$ 上是否一致连续？
>

<br/>

> [!question] 习题 6.2.16 (阿尔泽拉-阿斯科利定理, Arzela-Ascoli Theorem)
> 对于每个 $n \in \mathbb{N}$，设 $f_n$ 是定义在 $[0, 1]$ 上的函数。如果 $(f_n)$ 在 $[0, 1]$ 上**有界**——即存在一个 $M > 0$，使得对于所有 $n \in \mathbb{N}$ 和 $x \in [0, 1]$，$|f_n(x)| \le M$ 成立——并且如果函数集合 $(f_n)$ 是**等度连续的** (习题 6.2.15)，按照以下步骤证明 $(f_n)$ 包含一个一致收敛的子序列。
>
> (a) 使用练习 6.2.14 生成一个子序列 $(f_{n_k})$，该序列在 $[0, 1]$ 中的每个**有理点**处收敛。为简化符号，设 $g_k = f_{n_k}$。仍需证明 $(g_k)$ 在 $[0, 1]$ 上一致收敛。
> (b) 设 $\epsilon > 0$。根据等连续性，存在一个 $\delta > 0$ 使得 $|g_k(x) - g_k(y)| < \epsilon/3$ 对于所有 $|x - y| < \delta$ 和 $k \in \mathbb{N}$。利用这个 $\delta$，设 $r_1, r_2, \dots, r_m$ 是一个有理点的有限集合，其性质是邻域 $V_\delta(r_i)$ 的并集包含 $[0, 1]$。
> 解释为什么必须存在一个 $N \in \mathbb{N}$ 使得 $|g_s(r_i) - g_t(r_i)| < \epsilon/3$ 对于所有 $s, t \ge N$ 和 $r_i$ 在刚刚描述的 $[0, 1]$ 的有限子集中。为什么集合 $\{r_1, r_2, \dots, r_m\}$ 是有限的这一点很重要？
> (c) 通过证明对于任意的 $x \in [0, 1]$， $|g_s(x) - g_t(x)| < \epsilon$ 对于所有的 $s, t \ge N$ 完成论证。
>

<br/>

---
