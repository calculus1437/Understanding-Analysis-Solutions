# Riemann积分

[1.一致收敛函数列的可积性](#7.2.5)(7.2.5)
[2.单调函数的可积性](#7.2.6)(7.2.6)
[3.开集视角下分析不连续点集](#7.3.6)(7.3.6)
[4.$\left\lvert f \right\rvert$ 的可积性](#7.4.1)(7.4.1)
[5.积分值大于零与区间函数值恒大于零的关联](#7.4.4)(7.4.4)
[6.上下和的函数加法不等式](#7.4.5)(7.4.5)
[6.极限与积分换序的初步例子](#7.4.6)(7.4.6)
[7.牛莱公式的弱化版本](#7.5.3)(7.5.3)
[8.自然对数与欧拉常数](#7.5.4)(7.5.4)
[9.积分均值](#7.5.7)(7.5.7)
[10.一个连续单调函数在有理数集上不可微的例子](#7.5.11)(7.5.11)
[11.变量替换定理](#7.5.12)(7.5.12)
[12.二维黎曼重排](#7.6.5)(7.6.5)

## 习题 7.2 Riemann积分的定义

!!! question "练习 7.2.1"

    
    设 $f$ 是定义在 $\left[ {a,b}\right]$ 上的有界函数，且 $P$ 是 $\left[ {a,b}\right]$ 的任意分割。首先，解释为什么 $U\left( f\right)  \geq  L\left( {f,P}\right)$ 。现在，证明引理 7.2.6。

设 $\mathcal{P}$ 为 $\left[ {a,b}\right]$ 上所有分割的集合。已知 $U(f)=\inf\left\{U(f,P):P \in \mathcal{P}\right\}$，$L(f)=\sup\left\{L(f,P):P\in \mathcal{P}\right\}$。

所以使不等式成立的办法是证明 $L(f,P)$ 是全体 $U(f,P')$ 所组成集合的下界。好在对任意的分割 $P'$，的确有 $L(f,P)<U(f,P')$，所以它是下界。由下确界的定义， $U(f)\geq L(f,P)$。

由于上述的 $P$ 分割的任意性，$U(f)$ 同样是全体 $L(f,P)$ 所组成集合的上界。由上确界的定义， $U(f)\geq L(f)$。

综上，$U(f)\geq L(f)$。

<br/>

!!! question "练习 7.2.2"

    
    考虑 $f\left( x\right)  = {2x} + 1$ 在区间 $\left[ {1,3}\right]$ 上的情况。设 $P$ 是由点 $\{ 1,3/2,2,3\}$ 构成的分割。
    
    (a) 计算 $L\left( {f,P}\right) ,U\left( {f,P}\right)$ 和 $U\left( {f,P}\right)  - L\left( {f,P}\right)$ 。
    
    (b) 当我们将点 $5/2$ 添加到分区时， $U\left( {f,P}\right)  - L\left( {f,P}\right)$ 的值会发生什么变化？
    
    (c) 找到一个 $\left[ {1,3}\right]$ 的分区 ${P}^{\prime }$ ，使得 $U\left( {f,{P}^{\prime }}\right)  - L\left( {f,{P}^{\prime }}\right)  < 2$ 。

(a) $L(f,P)=\displaystyle\frac{1}{2}\times 3+\displaystyle\frac{1}{2}\times 4+1\times 5=\displaystyle\frac{17}{2}$。

$U(f,P)=\displaystyle\frac{1}{2}\times 4+\displaystyle\frac{1}{2}\times 5+1\times 7=\displaystyle\frac{23}{2}$。

$U(f,P)-L(f,P)=\displaystyle\frac{23}{2}-\displaystyle\frac{17}{2}=3$。

(b) 分别计算双方在 $\left[2,3 \right]$ 上的值的变化。

$\Delta L(f,P)=\displaystyle\frac{1}{2}\times (6-5)=\displaystyle\frac{1}{2}$。

$\Delta U(f,P)=\displaystyle\frac{1}{2}\times (6-7)=-\displaystyle\frac{1}{2}$。

所以 $\Delta\bigl(U(f,P)-L(f,P)\bigr)=\Delta U(f,P)-\Delta L(f,P)=-1<0$。

即值会变小。

(c) 由于上述分割的值为 $3+(-1)=2$，所以只要在此分割上继续细化，应该就能得到小于 $2$ 的分割。

由于 $f$ 是单调的，不同区间上的确界必定不同。我们就在 $\left(1,\displaystyle\frac{3}{2}\right)$ 上新增一个分点 $p$。

同样计算双方的值变化，得到 $\Delta L(f,P)=\left(\displaystyle\frac{3}{2}-p\right)\bigl(f\left(p\right)-f(1)\bigr)>0$，同理 $\Delta U(f,P)<0$。于是上述式子的值便能减小到小于 $2$ 的值。

<br/>

!!! question "练习 7.2.3"

    
    直接证明(不依赖于定理7.2)常数函数 $f\left( x\right)  = k$ 在任何闭区间 $\left[ {a,b}\right]$ 上可积。 ${\int }_{a}^{b}f$ 是什么？

对任意分割 $P$，有 $L(f,P)=U(f,P)=k(b-a)$。所以 $U(f)=L(f)=k(b-a)$，由此可知 $f$ 在 $\left[ {a,b}\right]$ 上可积，且 ${\int }_{a}^{b}f=k(b-a)$。

<br/>

!!! question "练习 7.2.4"

    
    (a) 证明有界函数 $f$ 在 $\left[ {a,b}\right]$ 上可积的充分必要条件是存在一个分割序列 ${\left( {P}_{n}\right) }_{n = 1}^{\infty }$ 满足
    
    $$
    \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left[ {U\left( {f,{P}_{n}}\right)  - L\left( {f,{P}_{n}}\right) }\right]   = 0.
    $$
    
    (b) 对于每个 $n$ ，令 ${P}_{n}$ 为将 $\left[ {0,1}\right]$ 分割成 $n$ 个相等子区间的分割。如果 $f\left( x\right)  = x$ ，求 $U\left( {f,{P}_{n}}\right)$ 和 $L\left( {f,{P}_{n}}\right)$ 的公式。公式 $1 + 2 + 3 + \cdots  + n =$  $n\left( {n + 1}\right) /2$ 将会有用。
    
    (c) 使用(a)中的可积性顺序准则直接证明 $f\left( x\right)  = x$ 在 $\left[ {0,1}\right]$ 上是可积的。

(a) $\Rightarrow$ 假设 $f$ 可积，则 $U(f)=L(f)$。由确界的定义，对 $\forall\ n\in \mathbb{N^+}$，总存在分割 $P_{n_1},P_{n_2}$ 使得：

$$
\begin{align*}
    L(f,P_{n_1}) &> L(f)-\frac{1}{n} \\
    U(f,P_{n_2}) &< U(f)+\frac{1}{n}=L(f)+\frac{1}{n}
\end{align*}
$$

记 $P_n=P_{n_{1}}\cup P_{n_{2}}$，则由细化的性质有 $L(f,P_{n_1})\leq L(f,P_n)\leq U(f,P_n)\leq U(f,P_{n_2})$，所以 $U\left(f,P_{n}\right)-L\left(f,P_{n}\right)\leq U(f,P_{n_2})-L(f,P_{n_1})<\displaystyle\frac{2}{n}$。

对每个 $n$ 做相同的操作，我们便得到了分割序列 $\left\{P_n\right\}$，且 $\displaystyle\lim_{n\to \infty}\left[ U(f,P_n)-L(f,P_n)\right]=0$。

$\Leftarrow$ 假设存在分割序列 $\left\{P_n\right\}$，使得 $\displaystyle\lim_{n\to \infty}\left[ U(f,P_n)-L(f,P_n)\right]=0$。考虑确界定义下的不等式：

$$
L(f,P_n)\leq L(f)\leq U(f)\leq U(f,P_n)
$$

由此我们有 $0\leq U(f)-L(f)\leq U(f,P_n)-L(f,P_n)$。对两边取极限，得到 $0\leq U(f)-L(f)\leq 0$，所以 $U(f)=L(f)$，即 $f$ 可积。

(b) $L(f,P_n)=\displaystyle\sum_{i=1}^{n}\displaystyle\frac{1}{n}\cdot f\left(\displaystyle\frac{i-1}{n}\right)=\displaystyle\frac{n(n-1)}{2n^2}=\displaystyle\frac{1}{2}-\displaystyle\frac{1}{2n}$。

$U(f,P_n)=\displaystyle\sum_{i=1}^{n}\displaystyle\frac{1}{n}\cdot f\left(\displaystyle\frac{i}{n}\right)=\displaystyle\frac{n(n+1)}{2n^2}=\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2n}$。

(c) 由 (a) 可知 $f$ 是可积的。当然我们还需要证明 $\displaystyle\lim_{n\to \infty}L(f,P_n)=\displaystyle\lim_{n\to \infty}U(f,P_n)=L(f)=U(f)$。

已知 $\displaystyle\lim_{n\to \infty}L(f,P_n)=\displaystyle\lim_{n\to \infty}U(f,P_n)=\displaystyle\frac{1}{2}$，因为 $L(f,P_n)\leq L(f)\leq U(f)\leq U(f,P_n)$ ，由极限保不等式性便可得到四者取极限后依然满足此关系，即 $\displaystyle\frac{1}{2}\leq L(f)\leq U(f)\leq \displaystyle\frac{1}{2}$。

所以 $L(f)=U(f)=\displaystyle\frac{1}{2}$。

<br/>

<a id="7.2.5"></a>

!!! question "练习 7.2.5"

    
    假设对于每个 $n$，${f}_{n}$ 是 $\left[ {a,b}\right]$ 上的可积函数。如果 $\left( {f}_{n}\right)  \rightarrow  f$ 在 $\left[ {a,b}\right]$ 上一致收敛，证明 $f$ 在这个集合上也是可积的。(我们将看到，如果收敛是逐点的，这个结论不一定成立。)

回想一下，一致收敛保证了 $\left\{f_n\right\}$ 和 $f$ 在整体上会足够接近。如果 $\lvert f_n(x)-f(x) \rvert<\varepsilon$，那么它们的上下确界肯定也会十分接近，也就是说上和与下和的值会非常接近。再利用可积的充要条件：

$$
U(f_n,P_\varepsilon)-L(f_n,P_\varepsilon)<\varepsilon
$$

来推出同分割下 $f$ 的上下和之差也会小于任意大的 $\varepsilon$，便能得到证明。

所以我们的目标如下：(1) 找到一个 $f_n$ 使其与 $f$ 充分接近；(2) 在 $f_n$ 上选择一个分割让它的上和与下和充分接近；(3) 证明这个分割使得 $f$ 与 $f_n$ 的上和（下和）充分接近，从而推出 $f$ 的上下和充分接近，由此得到 $f$ 可积的结论。

对 $\forall\ \varepsilon>0$，$\exists\ n\in \mathbb{N^+}$，使得对 $\forall\ x\in \left[ a,b \right]$，有 $\lvert f(x)-f_n(x) \rvert<\varepsilon$。

因为 $f_n$ 在 $\left[ a,b \right]$ 上可积，所以存在 $\left[ a,b \right]$ 上的分割 $P_\varepsilon$，使得 $U(f_n,P_\varepsilon)-L(f_n,P_\varepsilon)<\varepsilon$。

我们用上下和的定义进行推导。对分割 $P_\varepsilon$ 上的任意区间 $I$，均有 $\lvert f(x)-f_n(x) \rvert<\varepsilon$，这个式子即可诱导出上下确界的关系：

$$
\begin{align*}
    f(x)<f_n(x)+\varepsilon \leq \sup_{x\in I}f_n(x)+\varepsilon \\
    f_n(x)<f(x)+\varepsilon \leq \sup_{x\in I}f(x)+\varepsilon
\end{align*}
$$

这说明 $\displaystyle\sup_{x\in I}f_n(x)+\varepsilon$ 是 $\left\{f(x):x\in I\right\}$ 的一个上界，所以 $\displaystyle\sup_{x\in I}f(x)\leq \displaystyle\sup_{x\in I}f_n(x)+\varepsilon$ 。由另一个式子又可以得到 $\displaystyle\sup_{x\in I}f_n(x)\leq \displaystyle\sup_{x\in I}f(x)+\varepsilon$。所以我们有：

$$
\left\lvert \sup_{x\in I}f(x)-\sup_{x\in I}f_n(x) \right\rvert\leq \varepsilon
$$

同理，对下确界的分析也可得到 $\left\lvert \displaystyle\inf_{x\in I}f(x)-\inf_{x\in I}f_n(x) \right\rvert\leq \varepsilon$。

现在计算 $f$ 与 $f_n$ 上和的差值，由定义：

$$
\begin{align*}
    \lvert U(f,P_\varepsilon)-U(f_n,P_\varepsilon) \rvert &= \left\lvert \sum_{I\in P_\varepsilon} \left( \sup_{x\in I} f(x) - \sup_{x\in I} f_n(x) \right) \cdot |I| \right\rvert \\
    &\leq \sum_{I\in P_\varepsilon} \left\lvert \sup_{x\in I} f(x) - \sup_{x\in I} f_n(x) \right\rvert \cdot |I| \\
    &\leq \varepsilon \sum_{I\in P_\varepsilon} |I| \\
    &= (b-a)\varepsilon
\end{align*}
$$

同理可推出 $\lvert L(f,P_\varepsilon)-L(f_n,P_\varepsilon) \rvert\leq(b-a)\varepsilon$。

有了这两个不等式，我们就能计算 $f$ 的上下和之差：

$$
\begin{align*}
    &\mathrel{\phantom{=}}U(f,P_{\varepsilon})-L(f,P_{\varepsilon})\\
    &=\bigl(U(f,P_{\varepsilon})-U(f_n,P_{\varepsilon})\bigr)-\bigl(L(f_n,P_{\varepsilon})-L(f,P_{\varepsilon})\bigr)+\bigl(U(f_n,P_{\varepsilon})-L(f,P_{\varepsilon})\bigr)\\
    &\leq \lvert U(f,P_{\varepsilon})-U(f_n,P_{\varepsilon})\rvert+\lvert L(f_n,P_{\varepsilon})-L(f,P_{\varepsilon})\rvert+\lvert U(f_n,P_{\varepsilon})-L(f_n,P_{\varepsilon})\rvert\\
    &<\bigl(2\left(b-a\right)+1\bigr)\varepsilon
\end{align*}
$$

由 $\varepsilon$ 任意小可得 $\bigl(2\left(b-a\right)+1\bigr)\varepsilon$ 同样是任意小的（当然还可以取 $\varepsilon_1=\displaystyle\frac{\varepsilon}{2(b-a)+1}$ 来得到相同形式），所以 $f$ 在 $\left[ a,b \right]$ 上可积。

<br/>

<a id="7.2.6"></a>

!!! question "练习 7.2.6"

    
    设 $f : \left[ {a,b}\right]   \rightarrow  \mathbb{R}$ 在集合 $\left[ {a,b}\right]$ 上递增(即，当 $x < y$ 时， $f\left( x\right)  \leq$  $f\left( y\right)$ )。证明 $f$ 在 $\left[ {a,b}\right]$ 上可积。

对于 $\left[ a,b \right]$ 上的分割 $P$：

$$
P=\left\{a=x_0<x_1<\cdots<x_n=b\right\}
$$

由于单调性，我们可以很方便地写出它的上下和之差：

$$
U(f,P)-L(f,P)=\displaystyle\sum_{i=0}^{n-1}\bigl(f\left(x_{i+1}\right)-f\left(x_{i}\right)\bigr)\left(x_{i+1}-x_{i}\right)
$$

单调性可以让 $f(x_{i+1})$ 和 $f(x_{i})$ 充分接近吗？连续的情形下缩小区间即可，但不连续的时候呢？若 $\left[ x_{i},x_{i+1} \right]$ 上有跳跃间断点，那么 $f(x_{i+1})-f(x_{i})$ 就一定会大于等于那个跳跃的值。而跳跃间断点的个数和分布是难以估计的，这使得我们难以用 $P$ 把 $\left[ a,b \right]$ 分割成数个 $f$ 连续的区间。

从另一方面考虑，$f(x_{i+1})-f(x_{i})$ 的值其实是有上界的，即 $f(b)-f(a)$。事实上，$\displaystyle\sum_{i=0}^{n-1}\bigl(f\left(x_{i+1}\right)-f\left(x_{i}\right)\bigr)=f(b)-f(a)$，也就是说它们的总和也是有上界的。假设我们控制分割出的每个区间长度相同，那么上述的上下和之差就可以直接改成 $\bigl(f(b)-f(a)\bigr)(x_1-x_0)$，而通过细化分割，我们能够使 $x_1-x_0$ 任意小。

对 $\forall\ \varepsilon>0$，令分割 $P_n$ 的每个区间长度均为 $\displaystyle\frac{b-a}{n}$，即对 $\forall\ i\in [0,n-1]$，有 $x_{i+1}-x_i=\displaystyle\frac{b-a}{n}$。

则 $U(f,P_n)-L(f,P_n)=\displaystyle\sum_{i=0}^{n-1}\bigl(f\left(x_{i+1}\right)-f\left(x_{i}\right)\bigr)\left(\displaystyle\frac{b-a}{n}\right)=\displaystyle\frac{\bigl(f(b)-f(a)\bigr)\left(b-a\right)}{n}$。

由题意，$f(a)\leq f(b)$。若 $f(a)=f(b)$，则 $U(f,P_n)-L(f,P_n)=0<\varepsilon$，$f$ 可积。

若 $f(a)<f(b)$，则取 $n>\displaystyle\frac{\bigl(f(b)-f(a)\bigr)\left(b-a\right)}{\varepsilon}$，其对应的分割 $P_n$ 便满足 $U(f,P_n)-L(f,P_n)<\varepsilon$，$f$ 可积。

综上，$f$ 在 $\left[ a,b \right]$ 上可积。

<br/>

---

## 习题 7.3 具有间断点的函数的积分

!!! question "练习 7.3.1"

    
    考虑函数
    
    $$
    h\left( x\right)  = \begin{cases} 1 &   0 \leq  x < 1 \\ 2 &   x = 1 \end{cases}
    $$
    
    在区间 $\left[ {0,1}\right]$ 上。
    
    (a) 证明对于 $\left[ {0,1}\right]$ 的每个分割 $P$ ， $L\left( {f,P}\right)  = 1$ 成立。
    
    (b) 构建一个分割 $P$ ，使得 $U\left( {f,P}\right)  < 1 + 1/{10}$ 成立。
    
    给定 $\varepsilon  > 0$ ，构造一个分区 ${P}_{\varepsilon }$ ，使得 $U\left( {f,{P}_{\varepsilon }}\right)  < 1 + \varepsilon$ 。

(a) 对任意子区间 $I\in [0,1]$，必 $\exists\ x_0\in I$，使得 $x_0\neq 1$，故 $h(x_0)=1$。而 $h(x)\geq 1$，所以 $\displaystyle\inf_{x\in I}h(x)=1$。
所以 $L(f,P)=1$。

(b) 取分割 $P=\left\{0,\displaystyle\frac{19}{20},1\right\}$，则 $U(f,P)=1\times \displaystyle\frac{19}{20}+2\times \displaystyle\frac{1}{20}=1+\displaystyle\frac{1}{20}<1+\displaystyle\frac{1}{10}$。

同上，构造分割 $P_\varepsilon=\left\{0,1-\displaystyle\frac{\varepsilon}{2},1\right\}$，则 $U(f,P_\varepsilon)=1\times \left(1-\displaystyle\frac{\varepsilon}{2}\right)+2\times \displaystyle\frac{\varepsilon}{2}=1+\displaystyle\frac{\varepsilon}{2}<1+\varepsilon$。

<br/>

<a id="7.3.2"></a>

!!! question "练习 7.3.2"

    
    在例 7.3.3 中，我们了解到Dirichlet函数 $g\left( x\right)$ 不是Riemann可积的。构造一个可积函数序列 ${g}_{n}\left( x\right)$ ，使得 ${g}_{n} \rightarrow  g$ 在 $\left[ {0,1}\right]$ 上逐点收敛。这表明可积函数的逐点极限不一定可积。将此示例与练习 7.2.5 中要求的结果进行比较。

一种思路是，从 $f(x)=0$ 开始，一个一个把 $[0,1]$ 上有理数的取值从 $0$ 改为 $1$，这样每一步操作得到的函数都是可积的，只有最后的 $g(x)$ 不可积。

先构造 $[0,1]$ 上的有理数序列（因为有理数可数）：$Q=\left\{q_1,q_2,\ldots:q_n\in \mathbb{Q}\cap [0,1]\right\}$，接着定义 $g_n(x)$：

$$
g_n(x)=\begin{cases}
    0 & x\in [0,1]\setminus \{q_1,q_2,\ldots,q_n\} \\
    1 & x\in \{q_1,q_2,\ldots,q_n\}
\end{cases}
$$

这样对 $\forall\ n\in \mathbb{N^+}$，$g_n(x)$ 是可积的。

又对 $\forall\ x_0\in [0,1]$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$ 均有 $g_n(x_0)-g(x_0)=0$，所以 $g_n(x)\to g(x)$ 在 $[0,1]$ 上逐点收敛。

于是，可积函数序列 $g_n(x)$ 逐点收敛到不可积函数 $g(x)$，从而说明可积函数的逐点极限不一定可积，而 [$7.2.5$](#7.2.5) 的结论告诉我们，$[a,b]$ 上一致收敛的可积函数序列收敛到的函数仍然可积。

<br/>

<a id="7.3.3"></a>

!!! question "练习 7.3.3"

    
    这里是对为什么在 $\left[ {a,b}\right]$ 上具有有限个间断点的函数 $f$ 可积的另一种解释。补充缺失的细节。
    
    将每个不连续性嵌入足够小的开区间，并令 $O$ 为这些区间的并集。解释为什么 $f$ 在 $\left[ {a,b}\right]   \smallsetminus  O$ 上一致连续，并利用这一点完成论证。

因为 $([a,b]\setminus O)\cup O=[a,b]$ 是闭集，$O$ 是开集，所以其补集 $[a,b]\setminus O$ 是闭集，由有界进而得出是紧集。由于 $f$ 的所有间断点在 $O$ 内，所以 $f$ 在 $[a,b]\setminus O$ 上连续，进而在 $[a,b]\setminus O$ 上一致连续。

设间断点的个数为 $r$。作 $[a,b]$ 的分割 $P=\left\{a=x_0<x_1<\cdots<x_n=b\right\}$，并设包含间断点的区间为 $A_1,A_2,\ldots,A_p$，不包含间断点的区间为 $B_1,B_2,\ldots,B_q$。

此外，因为 $f$ 有界，所以 $\displaystyle\sup_{x\in [a,b]}{f(x)}$ 和 $\displaystyle\inf_{x\in [a,b]}{f(x)}$ 均存在，令 $M=\displaystyle\sup_{x\in [a,b]}{f(x)}-\displaystyle\inf_{x\in [a,b]}{f(x)}$，并对任意区间 $I$，记 $\Delta I=\displaystyle\sup_{x\in I}{f(x)}-\displaystyle\inf_{x\in I}{f(x)}$，则有 $\Delta I\leq M$。

对于 $A_i$，可以控制其区间长度，对于 $B_i$，可以控制函数值之差。我们的目的是证明

$U(f,P)-L(f,P)=\displaystyle\sum_{I\in P}^{}\Delta I\cdot \lvert I \rvert=\displaystyle\sum_{i=1}^{p}\Delta A_i \cdot \lvert A_i \rvert+\displaystyle\sum_{i=1}^{q}\Delta B_i \cdot \lvert B_i \rvert$

通过合理的选取可以任意小。令 $\displaystyle\sum_{i=1}^{p}\lvert A_i \rvert=l_1$，$\displaystyle\sum_{i=1}^{q}\lvert B_i\rvert=l_2$，则 $l_1+l_2=b-a$。上式中 $l_1$ 和 $\Delta B_i$ 都可以被控制，就依此来进行论证。

首先证明全体 $B_i$ 之并一致连续，以得到 $\Delta B_i$ 的共同上界。记间断点 $x_1,x_2,\ldots,x_r$ 与 $B_i$ 的最近距离分别为 $d_1,d_2\ldots,d_r$，取其中最小值为 $m$，则必有 $m>0$。取开区间 $I_1,I_2,\ldots, I_r\in [a,b]$ 满足 $x_i\in I_i$ 和 $\displaystyle\sup_{}{\lvert I_i \rvert}<\displaystyle\frac{m}{2}$。记 $O=\displaystyle\bigcup_{i=1}^r I_i$，则 $\displaystyle\bigcup_{i=1}^q B_i\subseteq [a,b]\setminus O$，从而 $f$ 在 $\displaystyle\bigcup_{i=1}^q B_i$ 上一致连续。

对 $\forall\ \varepsilon>0$， $\exists\ \delta>0$，使得对任意的分割 $P$，$\forall\ x,y\in \displaystyle\bigcup_{i=1}^q B_i$，当 $\lvert x-y \rvert<\delta$ 时，有 $\lvert f(x)-f(y) \rvert<\displaystyle\frac{\varepsilon}{2(b-a)}$。从而 $\Delta B_i\leq \displaystyle\frac{\varepsilon}{2(b-a)}$。

现在开始构造。由于一个点最多属于两个闭区间，所以 $p\leq 2r$。构造这样的 $P$，使得

$$
\displaystyle\sup_{I\in P}{\lvert I \rvert}<\min\left\{\delta, \displaystyle\frac{\varepsilon}{4rM}\right\}
$$

这样就有

$$
\begin{align*}
    U(f,P)-L(f,P)&=\displaystyle\sum_{I\in P}^{}\Delta I\cdot \lvert I \rvert=\displaystyle\sum_{i=1}^{p}\Delta A_i \cdot \lvert A_i \rvert+\displaystyle\sum_{i=1}^{q}\Delta B_i \cdot \lvert B_i \rvert\\
    &<M\displaystyle\sum_{i=1}^{p}\lvert A_i \rvert+\displaystyle\frac{\varepsilon}{2(b-a)}\displaystyle\sum_{i=1}^{q}\lvert B_i \rvert\\
    &<M\cdot \displaystyle\frac{p\varepsilon}{4rM}+\displaystyle\frac{\varepsilon}{2(b-a)}(b-a)\\
    &\leq \displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon
\end{align*}
$$

综上，$f$ 在 $[a,b]$ 上可积。

<br/>

!!! question "练习 7.3.4"

    
    假设 $f : \left[ {a,b}\right]   \rightarrow  \mathbb{R}$ 是可积的。
    
    (a) 证明如果在某一点 $x \in  \left[ {a,b}\right]$ 处改变 $f\left( x\right)$ 的一个值，那么 $f$ 仍然是可积的，并且积分值不变。
    
    (b) 证明如果改变 $f$ 的有限个值，(a)中的观察仍然成立。
    
    (c) 找出一个例子，说明通过改变可数个值， $f$ 可能不再可积。

(a) 为了表述方便，我们仍然把区间 $I$ 上 $f$ 上下确界之差记作 $\Delta I$。

设即将改变值的点是 $x_0$。若 $f$ 可积，则对 $\forall\ \varepsilon>0$，存在一个分割 $P$，使得 $U(f,P)-L(f,P)<\displaystyle\frac{\varepsilon}{2}$。

我们的目标是控制 $x_0$ 在分割区间上的长度，从而控制函数值改变对和式造成的影响。设值改变后的 $\Delta [a,b]=M$，则对 $\forall\ I\in [a,b]$，$\Delta I\leq M$。

细化上述的分割 $P$ 为 $P'$，使得 $x_0$ 为其中一分割点，再控制包含 $x_0$ 的分割区间总长为 $k<\displaystyle\frac{\varepsilon}{2M}$。由细化的性质，$U(f,P')-L(f,P')\leq U(f,P)-L(f,P)<\displaystyle\frac{\varepsilon}{2}$。

记值改变后的函数为 $f_1$，则 $f_1=f, x\in [a,b]\setminus \left\{x_0\right\}$。设 $P$ 中包含 $x_0$ 的分割区间为 $I_0$（若有两个也同理），则有

$$
\begin{align*}
    U(f_1,P')-L(f_1,P')&=U(f,P')-L(f,P')-\left(\Delta I_{0} \cdot |I_0|\right)+\left(M \cdot |I_0|\right)\\
    &<\displaystyle\frac{\varepsilon}{2}+M\cdot \displaystyle\frac{\varepsilon}{2M}=\varepsilon
\end{align*}
$$

综上，$f$ 可积。

由于包含 $x_0$ 的区间 $I_0$ 的长度可以任意小，足够抵消函数值变化带来的影响，故上和的变化可以任意小，这使得积分值不变。具体的说，设积分值为 $A$，并取分割 $P$ 同时满足 $U(f,P)-A<\displaystyle\frac{\varepsilon}{2}$，$\lvert I_0 \rvert<\displaystyle\frac{\varepsilon}{2\lvert f(x_0)-f_1(x_0) \rvert}$。

则 $\lvert U(f_1,P)-U(f,P) \rvert=\lvert f(x_0)-f_1(x_0) \rvert\cdot |I_0|<\displaystyle\frac{\varepsilon}{2}$，所以 $\lvert U(f_1,P)-A \rvert\leq \lvert U(f_1,P)-U(f,P) \rvert+\lvert U(f,P)-A \rvert<\displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon$。

综上，积分的值不变。

(b) 每增加一个点，都可以用 (a) 中的方法来处理，由于步骤是有限的，最终得到的函数一定也会可积且积分值不变。

(c) 见 [$7.3.2$](#7.3.2)。

<br/>

<a id="7.3.5"></a>

!!! question "练习 7.3.5"

    
    设
    
    $$
    f\left( x\right)  = \begin{cases} 1 \quad \text{if } x = 1/n,\quad n \in  \mathbb{N} \\ 0 \quad   \text{otherwise} \end{cases}
    $$
    
    证明 $f$ 在 $\left[ {0,1}\right]$ 上可积，并计算 ${\int }_{0}^{1}f$ 。

对 $\forall\ \varepsilon>0$，构造这样的分割：

选取 $N>\displaystyle\frac{2}{\varepsilon}$，取 $\left[ 0,\displaystyle\frac{1}{N} \right]$ 为第一段；

然后取 $I_1,I_2,\ldots, I_{N-1}$，使得 $x=\displaystyle\frac{1}{n}\in I_n$，并取 $\lvert I_1 \rvert=\lvert I_2 \rvert=\cdots=\lvert I_{N-1} \rvert<\min\left\{\displaystyle\frac{\varepsilon}{2(N-1)},\displaystyle\frac{1}{3}\left(\displaystyle\frac{1}{N-1}-\displaystyle\frac{1}{N}\right)\right\}$ 使得各区间均不相交；

最后填充剩下的区间，得到分割 $P$。

因为任意区间上都有无理数，所以任意区间的下确界都是 $0$，即下和为 $0$。对于上和，最后的区间上函数值恒为 $0$，计算剩余部分：

$U(f,P)=\displaystyle\frac{1}{N}+\left(N-1\right)\lvert I_1 \rvert<\varepsilon$。

所以 $f$ 在 $[0,1]$ 上可积，并且 $\displaystyle\int_{0}^{1}f=0$。

<br/>

<a id="7.3.6"></a>

!!! question "练习 7.3.6"

    
    一个集合 $A \subseteq  \left[ {a,b}\right]$ 如果对于每一个 $\varepsilon  > 0$ 都存在一个有限的开区间集合 $\left\{  {{O}_{1},{O}_{2},\ldots ,{O}_{N}}\right\}$ ，这些开区间的并集包含 $A$ 且它们的长度之和为 $\varepsilon$ 或更小，则称该集合具有零内容。用 $\left| {O}_{n}\right|$ 表示每个区间的长度，我们有
    
    $$
    A \subseteq  \mathop{\bigcup }\limits_{{n = 1}}^{N}{O}_{n}\quad  \text{and} \quad \mathop{\sum }\limits_{{n = 1}}^{N}\left| {O}_{n}\right|  \leq  \varepsilon .
    $$
    
    (a) 设 $f$ 在 $\left[ {a,b}\right]$ 上有界。证明如果 $f$ 的不连续点集具有零内容，则 $f$ 可积。
    
    (b) 证明任何有限集都具有零内容。
    
    (c) 内容为零的集合不必是有限的。它们也不必是可数的。证明第3.1节中定义的 Cantor 集 $C$ 的内容为零。
    
    (d) 证明
    
    $$
    h\left( x\right)  = \begin{cases} 1 & x \in  C \\ 0 & x \notin  C. \end{cases}
    $$
    
    是可积的，并求出积分的值。

(a) 记 $O=\displaystyle\bigcup_{n=1}^N O_n$，则此时的情形与 [$7.3.3$](#7.3.3) 上的情形几乎一致。同样能证得 $f$ 在 $[a,b]\setminus O$ 上一致连续。唯一需要改动的地方是分割 $P$ 的构造。

由于 $f$ 有界，存在 $M>\displaystyle\sup_{x\in [a,b]}{f(x)}-\displaystyle\inf_{x\in [a,b]}{f(x)}$，取其为接下来控制不连续点集上的和做准备。

对 $\forall\ \varepsilon>0$，存在开区间集 $\left\{O_1,O_2,\ldots,O_N\right\}$，使得不连续点均属于这些开区间的并集，且 $\displaystyle\sum_{n=1}^{N}\left|O_n\right|<\displaystyle\frac{\varepsilon}{2M}$。记 $O=\displaystyle\bigcup_{n=1}^N O_n$。

在 $[a,b]\setminus O$ 上，$f$ 一致连续，因此对上述的 $\varepsilon$，存在 $\delta>0$，使得对任意 $x,y\in [a,b]\setminus O$，当 $\lvert x-y \rvert<\delta$ 时，有 $\lvert f(x)-f(y) \rvert<\displaystyle\frac{\varepsilon}{2(b-a)}$。

现在，构造分割 $P=\left\{a=x_0<x_1<\ldots<x_n=b\right\}$，使得对任意开区间的顶点 $o\in [a,b]$，都 $\exists\ i\in [0,n]$ 使得 $o=x_i$，这样就把所有开区间在 $[a,b]$ 中的部分都包含进 $P$ 中了。为了满足一致连续性，同样使得对 $\forall\ i\in [0,n-1]$，$\lvert x_{i+1}-x_i \rvert<\delta$。

设 $P$ 中包含不连续点的区间为 $A_1,A_2,\ldots,A_p$，剩余的区间为 $B_1,B_2,\ldots,B_q$。前者的长度之和为开区间们在 $[a,b]$ 上的部分长度之和，因此 $\displaystyle\sum_{i=1}^{p}\lvert A_i \rvert\leq \displaystyle\sum_{i=1}^{N}\lvert O_i \rvert<\displaystyle\frac{\varepsilon}{2M}$。根据补集关系能得出 $\displaystyle\bigcup_{i=1}^q B_i\subseteq [a,b]\setminus O$，因此 $B_i$ 们的并集满足上述的一致连续不等式。

最后估计上下和之差：

$$
\begin{align*}
    U(f,P)-L(f,P)&=\displaystyle\sum_{I\in P}^{}\bigl(\displaystyle\sup_{x\in I}{f(x)}-\displaystyle\inf_{x\in I}{f(x)}\bigr)\lvert I \rvert\\
    &=\displaystyle\sum_{i=1}^{p}\left(\displaystyle\sup_{x\in A_i}{f(x)}-\displaystyle\inf_{x\in A_i}{f(x)}\right)\lvert A_i \rvert+\displaystyle\sum_{i=1}^{q}\left(\displaystyle\sup_{x\in B_i}{f(x)}-\displaystyle\inf_{x\in B_i}{f(x)}\right)\lvert B_i \rvert\\
    &< \displaystyle\sum_{i=1}^{p}M\lvert A_i \rvert+\displaystyle\sum_{i=1}^{q}\displaystyle\frac{\varepsilon}{2(b-a)}\lvert B_i \rvert\\
    &<M\cdot \displaystyle\frac{\varepsilon}{2M}+\displaystyle\frac{\varepsilon}{2(b-a)}(b-a)\\
    &=\displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon 
\end{align*}
$$

综上，$f$ 在 $[a,b]$ 上可积。

(b) 设有限集 $A=\left\{x_1,x_2,\ldots,x_n\right\}$，对 $\forall\ \varepsilon>0$，取开区间集 $\left\{O_1,O_2,\ldots,O_n\right\}$，满足 $x_i\in O_i$，且 $\lvert O_i \rvert<\displaystyle\frac{\varepsilon}{n}$，则 $A\subseteq \displaystyle\bigcup_{i=1}^{n}O_i$，且 $\displaystyle\sum_{i=1}^{n}\lvert O_i \rvert<\varepsilon$，所以有限集具有零内容。

(c) 从 Cantor 集的构造入手。事实上，$C_n$ 已经将 $[0,1]$ 分割成了 $2^n$ 个闭区间的并，且每个区间的长度为 $\displaystyle\frac{1}{3^n}$，这足以构造其上的开区间集 $\left\{O_1,O_2\ldots,O_{2^n}\right\}$，使得每一个闭区间都包含在一个开区间中。令每个开区间的长度为 $\displaystyle\frac{2}{3^n}$，则 $\displaystyle\sum_{i=1}^{2^n}\lvert O_i \rvert=2\cdot \left(\displaystyle\frac{2}{3}\right)^n$。

现在，因为对 $\forall\ n\in \mathbb{N}$，$C\subseteq C_n\subseteq \displaystyle\bigcup_{i=1}^{2^n}\lvert O_i \rvert$，所以上述开区间集总会是 $C$ 的覆盖集。现在，对 $\forall\ \varepsilon>0$，取 $N>\log_{\frac{2}{3}}\displaystyle\frac{\varepsilon}{2}$，则 $\displaystyle\sum_{i=1}^{2^N}\lvert O_i \rvert=2\cdot \left(\displaystyle\frac{2}{3}\right)^N<\varepsilon$。

所以 $C$ 的内容为零。

(d) 现在，我们知道 $C$ 是零内容的，这说明我们可以直接化用 (a) 中的操作进行计算。

首先，因为 $C$ 是紧集，故不连续点集包含于 $C$，而 $C$ 又包含于上述构造的 $\displaystyle\bigcup_{i=1}^{2^N}O_i$ 中，所以不连续点集是零内容的，所以 $f$ 可积。

接下来，又因为 $C$ 是完全不连通的，对 $\forall\ I\subseteq [0,1]$，总存在 $x_0\in I$，使得 $h(x_0)=0$。

这说明 $L(h,P)$ 恒为 $0$。即 $L(h)=0$。由 $h$ 可积，我们现在就可以得出结论：$\displaystyle\int_{0}^{1}{h(x)}\, \mathrm{d}{x}=0$。

不过我们也可以估计上和的值。(a) 告诉我们，对于任何零内容的集合，我们总能构造这样的分割 $P$，使得 $P$ 中包含该集合的区间之并长度小于 $\varepsilon$。在另外的区间上肯定有 $h(x)=0$，故

$$
U(f,P)=0+1\cdot \varepsilon=\varepsilon
$$

所以 $\displaystyle\int_{0}^{1}{h(x)}\, \mathrm{d}{x}=0$。

<br/>

---

## 习题 7.4 积分的性质

<a id="7.4.1"></a>

!!! question "练习 7.4.1"

    
    (a) 设 $f$ 为集合 $A$ 上的有界函数，并设
    
    $$
    M = \sup \{ f\left( x\right)  : x \in  A\} ,\;m = \inf \{ f\left( x\right)  : x \in  A\} ,
    $$
    
    $$
    {M}^{\prime } = \sup \{ \left| {f\left( x\right) }\right|  : x \in  A\} ,\;  \;{m}^{\prime } = \inf \{ \left| {f\left( x\right) }\right|  : x \in  A\} .
    $$
    
    证明 $M - m \geq  {M}^{\prime } - {m}^{\prime }$ 。
    
    (b) 证明如果 $f$ 在区间 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则 $\left| f\right|$ 在此区间上也可积。
    
    (c) 提供论证的细节，说明在这种情况下我们有 $\left| {{\int }_{a}^{b}f}\right|  \leq$  ${\int }_{a}^{b}\left| f\right|$ 。

(a) 若 $f(x)\geq 0$，则 $\left\lvert f(x) \right\rvert=f(x)$。所以 $M=M'$，$m=m'$，$M-m=M'-m'$ 成立。

在 $f(x)\leq 0$ 时，$\left\lvert f(x) \right\rvert=-f(x)$。所以 $M=-m'$，$m=-M'$，$M-m=M'-m'$ 成立。

现在看看 $f(x)$ 符号会发生变化的情况。因为既有正又有负，所以 $M>0$，$m<0$。而 $\left\lvert f(x) \right\rvert\geq 0$，所以 $M'\geq 0$，$m'\geq 0$。

现在，我们仔细地论证 $M'$ 该如何取值。由确界性质，$-m=\displaystyle\sup\{-f(x) : x \in A\}$，故 $\left\lvert f(x) \right\rvert$ 上确界必为 $M,-m$ 之一。又因为 $M>0$，$-m>0$，所以

$$
M-m\geq \max\left\{M,-m\right\}=M'\geq M'-m'
$$

(b) 对分割 $P$，写出上下和之差的公式：

$$
U(f,P) - L(f,P) = \sum_{A\in P}^{} (M_A - m_A) \left\lvert A \right\rvert\geq \sum_{A\in P}^{} (M_A' - m_A') \left\lvert A \right\rvert= U(\left\lvert f \right\rvert,P) - L(\left\lvert f \right\rvert,P)
$$

所以若 $f$ 可积，则对任意 $\epsilon>0$，存在分割 $P$ 使得 $U(f,P) - L(f,P)<\varepsilon$。由上式可知，$U(\left\lvert f \right\rvert,P) - L(\left\lvert f \right\rvert,P)<\varepsilon$，所以 $\left\lvert f \right\rvert$ 可积。

(c) 由前述论证，$M_A'=\max\left\{M_A,-m_A\right\}\geq M_A$ 或者 $M_A'\geq -m_A$，所以 $U(\left\lvert f \right\rvert,P)\geq U(f,P)$。或 $U(\left\lvert f \right\rvert,P)\geq -L(f,P)$。

由于总能选取合适的分割使得它们的极限为积分值，所以前者有 $\displaystyle\int_{a}^{b}{\left\lvert f(x) \right\rvert}\, \mathrm{d}{x}\geq \displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}$，后者有 $\displaystyle\int_{a}^{b}{\left\lvert f(x) \right\rvert}\, \mathrm{d}{x}\geq -\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}$。

两式合起来，得 $\left\lvert \displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x} \right\rvert\leq \displaystyle\int_{a}^{b}{\left\lvert f(x) \right\rvert}\, \mathrm{d}{x}$。

<br/>

!!! question "练习 7.4.2"

    
    回顾定义 7.4.3。证明如果 $c \leq  a \leq  b$ 和 $f$ 在区间 $\left\lbrack  {c,b}\right\rbrack$ 上可积，则 ${\int }_{a}^{b}f = {\int }_{a}^{c}f + {\int }_{c}^{b}f$ 仍然成立。

利用 $\displaystyle\int_{a}^{c}{f(x)}\, \mathrm{d}{x}=-\displaystyle\int_{c}^{a}{f(x)}\, \mathrm{d}{x}$ 的事实，有 $\displaystyle\int_{c}^{a}{f(x)}\, \mathrm{d}{x}+\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}=\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}-\displaystyle\int_{a}^{c}{f(x)}\, \mathrm{d}{x}=\displaystyle\int_{c}^{b}{f(x)}\, \mathrm{d}{x}$，移项即证明原式。

<br/>

!!! question "练习 7.4.3"

    
    证明定理7.4.4，包括对练习7.2.5的论证(如果尚未完成)。

见练习 [$7.2.5$](#7.2.5)，定理内容是，$\left\{f_n\right\}\to f$ 在 $\left\lbrack a,b \right\rbrack$ 上一致收敛，且任意 $f_n$ 是可积的，则 $f$ 也是可积的。

<a id="7.4.4"></a>

!!! question "练习 7.4.4"

    
    判断以下猜想中哪些为真，并提供简短证明。对于不成立的猜想，给出反例。
    
    (a) 如果 $\left| f\right|$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则 $f$ 在该集合上也可积。
    
    (b) 假设 $g$ 可积且 $g \geq  0$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上。如果在无限多个点 $x \in  \left\lbrack  {a,b}\right\rbrack$ 上 $g\left( x\right)  > 0$ ，则 $\int g > 0$ 。
    
    (c) 如果 $g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 和 $g \geq  0$ 上连续，并且至少存在一个点 ${x}_{0} \in  \left\lbrack  {a,b}\right\rbrack$ 使得 $g\left( {x}_{0}\right)  > 0$ ，那么 ${\int }_{a}^{b}g > 0$ 。
    
    (d) 如果 ${\int }_{a}^{b}f > 0$ ，存在一个区间 $\left\lbrack  {c,d}\right\rbrack   \subseteq  \left\lbrack  {a,b}\right\rbrack$ 和一个 $\delta  > 0$ ，使得对于所有的 $x \in  \left\lbrack  {c,d}\right\rbrack$ ， $f\left( x\right)  \geq  \delta$ 成立。

(a) 事实上这应该反过来，即 $f$ 可积 $\Rightarrow$ $\left\lvert f \right\rvert$ 可积，参照 [$7.4.1$](#7.4.1)。反例为 Diriclet 函数的变式：

$$
D(x)=\begin{cases}
    1, \quad x\in \mathbb{Q}\\
    -1, \quad x\in \mathbb{R}\setminus \mathbb{Q}
\end{cases}
$$

它是不可积的，然而 $\left\lvert D(x) \right\rvert=1$，在任意闭区间上都可积。

(b) [$7.3.5$](#7.3.5) 中的例子是一个反例。

(c) 如果函数连续，就说明 $x_0$ 附近一定有一个区间，而非一些孤立点上的函数值大于 $0$，这为整个积分值大于 $0$ 提供了可能。

首先，因为 $g$ 在 $[a,b]$ 上连续，所以 $g$ 同样在 $[a,b]$ 上可积。

若 $g$ 可积，则 $U(g)=L(g)$，现在我们只需要证明其中一个大于 $0$。

只要分割 $P$ 分得足够细，$x_0$ 周边大于 $0$ 的部分一定能被单独分出来，此时 $L(g,P)>0$，再考虑 $L(g)=\displaystyle\sup_{P}{L(g,P)}$ 即可。

因为 $g$ 在 $[a,b]$ 上连续，所以对 $g(x_0)>0$，$\exists\ \delta>0$，使得对 $\forall\ \left\lvert x-x_0 \right\rvert<\delta$，都有 $\left\lvert g(x)-g(x_0) \right\rvert<\displaystyle\frac{g(x_0)}{2}$，即 $g(x)>\displaystyle\frac{g(x_0)}{2}$。

下一步即是取一个单独分离出该邻域的分割，为了让 $\delta$ 邻域不超出 $[a,b]$ 的范围，我们取 $\delta_1=\min\left\{\displaystyle\frac{\delta}{2},\displaystyle\frac{x_0-a}{2}, \displaystyle\frac{b-x_0}{2}\right\}$。现在，我们取这样的分割 $P:\left\{a<x_0-\delta_1<x_0+\delta_1<b\right\}$，由于在 $\forall\ x\in [a,b]$ 上均有 $g(x)\geq 0$，我们有：

$$
\begin{align*}
    L(g,P)&=\displaystyle\sum_{I\in P} \displaystyle\inf_{x\in I}{g(x)}\cdot \left\lvert I \right\rvert\\
    &\geq \displaystyle\frac{g(x_0)}{2}\cdot 2\delta_{1}\\
    &=\delta_{1}g(x_0)>0
\end{align*}
$$

再根据 $L(g)\geq L(g,P)>0$，得到 $\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}>0$。

<mark>这里其实漏掉了对端点两值的考虑。</mark>


(d) 这一问可以看作上一问的逆向思考：上一问中，函数有连续的恒正区间 $\Rightarrow$ 积分大于 $0$，而这一问则思考，若积分值大于 $0$，函数是否一定有连续的恒正区间。

回忆一下，上一问我们通过估计下和的上确界，得到了积分值大于 $0$。这一问我们不妨用相同的操作：同样对下和作估计。

如果没有一个区间满足函数值恒大于某个正数，那么这些区间的下确界就只能小于等于 $0$，这说明无论怎么分割，下和的值都一定不大于 $0$，这就得到矛盾了。

假设对 $\forall\ [c,d]\subseteq [a,b]$，$\forall\ \delta>0$，$\exists\ x\in [c,d]$ 使得 $f(x)<\delta$，则 $\displaystyle\inf_{x\in [c,d]}{f(x)}\leq 0$。

对 $[a,b]$ 上的任意分割 $P$，$L(f,P)=\displaystyle\sum_{I\in P}\displaystyle\inf_{x\in I}{f(x)}\cdot \left\lvert I \right\rvert\leq \displaystyle\sum_{I\in P}^{}0\cdot \left\lvert I \right\rvert=0$。所以 $L(f)=\displaystyle\sup_{P}{L(f,P)}\leq 0$，这与 $\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}>0$ 相矛盾。

所以综上，一定存在一个区间 $[c,d]\subseteq [a,b]$ 和一个 $\delta>0$，使得 $\forall\ x\in [c,d]$，都有 $f(x)\geq \delta$。

<br/>

<a id="7.4.5"></a>

!!! question "练习 7.4.5"

    
    设 $f$ 和 $g$ 是 $\left\lbrack  {a,b}\right\rbrack$ 上的可积函数。
    
    (a) 证明如果 $P$ 是 $\left\lbrack  {a,b}\right\rbrack$ 的任意分割，则
    
    $$
    U\left( {f + g,P}\right)  \leq  U\left( {f,P}\right)  + U\left( {g,P}\right) .
    $$
    
    提供一个具体例子，其中不等式是严格的。对应的下和不等式是什么样子的？
    
    (b) 回顾定理 7.4.2 (ii) 的证明，并为该定理的 (i) 部分提供论证。

(a) 对 $\forall\ I\subseteq [a,b]$，$x\in I$ 时我们有：

$$
\begin{align*}
    &&f(x)&\leq \displaystyle\sup_{x\in I}{f(x)}\\
    &&g(x)&\leq \displaystyle\sup_{x\in I}{g(x)}\\
    &\Rightarrow& f(x)+g(x)&\leq \displaystyle\sup_{x\in I}{f(x)}+\displaystyle\sup_{x\in I}{g(x)}\\
    &\Rightarrow& \displaystyle\sup_{x\in I}{(f(x)+g(x))}&\leq \displaystyle\sup_{x\in I}{f(x)}+\displaystyle\sup_{x\in I}{g(x)}
\end{align*}
$$

根据上和的定义 $U(f,P)=\displaystyle\sum_{I\in P}^{}\displaystyle\sup_{x\in I}{f(x)}\cdot \left\lvert I \right\rvert$，我们能得到 $U(f+g,P)\leq U(f,P)+U(g,P)$。

我们通过上确界的不等式来寻找严格小于的例子。如果 $f$ 和 $g$ 的上确界正好在同一个位置取到，那么它们两相加的上确界就会是上确界的和。但是，如果 $f$ 取到上确界的时候 $g$ 没取到，甚至说特别小，那么它们加起来的上确界就会小一些。我们的思路就是这样，让 $f$ 大的时候 $g$ 小，$g$ 大的时候 $f$ 小，让它们的上确界始终凑不到一块儿，加起来的和总会因为其中一个特别小而不大。比如说：

$f(x)=x$，$g(x)=1-x$，在 $[0,1]$ 上作分割。这里我们偷点懒，直接把整个区间作为分割结果。那么此时，$f(x),g(x)$ 各自的上确界都是 $1$，所以 $U(f,P)+U(g,P)=2$。但是它们两个加起来却没法这么大，事实上它们是相互抵消的，得到 $f(x)+g(x)=1$，所以 $U(f+g,P)=1$，这样就有了 $U(f+g,P)<U(f,P)+U(g,P)$ 这个严格不等式。

对下确界的类似分析可以得到类似的结果，也就是 $L(f+g,P)\geq L(f,P)+L(g,P)$。

(b) 我们先写出这两个定理的内容：

(i) 如果 $f$ 和 $g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则 $f + g$ 在该集合上也可积，并且 ${\int }_{a}^{b}\left( {f + g}\right)  = {\int }_{a}^{b}f + {\int }_{a}^{b}g$。

(ii) 如果 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则对于任意常数 $k$，函数 $kf$ 也在该集合上可积，并且 ${\int }_{a}^{b}\left( {kf}\right)  = k{\int }_{a}^{b}f$。

通过确界的性质可以很快得出 $L(kf,P)=kL(f,P)$ 及 $U(kf,P)=kU(f,P)$，由此可以证明 (ii)。下面我们主要讨论 (i) 的证明。

当然，我们的第一步还是要证明可积性，不过这可以通过不等式快速地得出：事实上这跟 [$\left\lvert f \right\rvert$ 可积的论证](#7.4.1) 是极其类似的，都是通过原来的函数估计新函数上下和的差值。

对任意的分割 $P$，我们有：

$$
L(f,P)+L(g,P)\leq L(f+g,P)\leq U(f+g,P)\leq U(f,P)+U(g,P)
$$

当然，加上 $f+g$ 的上下积分，这个不等式可以进一步地拓展为

$$
L(f,P)+L(g,P)\leq L(f+g,P) \textcolor{red}{\leq L(f+g)\leq U(f+g)\leq} U(f+g,P)\leq U(f,P)+U(g,P)
$$

根据上下积分的确界性质（这个我们已经倒腾无数遍了），我们进一步再用 $f,g$ 的上下积分化简这个不等式：

$$
L(f)+L(g)\leq L(f+g)\leq U(f+g)\leq U(f)+U(g)
$$

最后，因为 $f,g$ 是可积的，所以上述不等式的各项其实都是相等的。所以就有：

$$
\displaystyle\int_{a}^{b}{f(x)+g(x)}\, \mathrm{d}{x}=\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}+\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}
$$

<mark>但是这里有一个问题。</mark> 所谓的 $\displaystyle\sup_{P}{\bigl(L(f,P)+L(g,P)\bigr)}=L(f)+L(g)$ 在这里并没有得到证明，事实上也很可能不成立，因为两函数的上下积分需要独立地取分割而得到，而这里强行求的是它们在同一分割下的下和。

有没有一种办法，能把两个不同的分割合并估计呢？就是它们俩的共同细化。回想一下，它们细化之后就能得到同一分割，而这个分割下的下和一定更接近于下积分，这为我们的证明提供了契机。

对任意的分割 $P_1,P_2$，取它们的共同细化 $P=P_1\cup P_2$，则：

$$
\begin{align*}
    L(f,P_1)&\leq L(f,P)\\
    L(g,P_2)&\leq L(g,P)\\
    \Rightarrow L(f,P_1)+L(g,P_2)&\leq L(f,P)+L(g,P)\leq L(f+g)
\end{align*}
$$

现在，由于 $P_1,P_2$ 是任取的，此时肯定有 $\displaystyle\sup_{P_1,P_2}{\bigl(L(f,P_1)+L(g,P_2)\bigr)}=L(f)+L(g)$，于是我们就得到了 $L(f)+L(g)\leq L(f+g)$。

对右半部分进行同样的操作，得到 $U(f+g)\leq U(f)+U(g)$，于是我们得到了证明。

<br/>

<a id="7.4.6"></a>

!!! question "练习 7.4.6"

    
    回顾定理 7.4.4 之前的讨论。
    
    (a) 构造一个序列 ${f}_{n} \rightarrow  0$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上逐点收敛的例子，其中 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{f}_{n}$ 不存在。
    
    (b) 生成另一个例子(如有必要)，其中 ${f}_{n} \rightarrow  0$ 且序列 ${\int }_{0}^{1}{f}_{n}$ 无界。
    
    (c) 在(a)和(b)部分的例子中，是否可能构造每个 ${f}_{n}$ 使其连续？
    
    (d)* 是否有可能构造序列 $\left( {f}_{n}\right)$ 使其一致有界？一致有界意味着存在一个单一的 $M > 0$ 满足 $\left| {f}_{n}\right|  \leq  M$ 对于所有 $n \in  \mathbb{N^+}$。
    
    (e) 是否有可能构造序列 $\left\{g_n\right\}$ 使得 $\displaystyle\int_{0}^{1}{g_n(x)}\, \mathrm{d}{x}\to 0$ 但是对 $\forall\ x\in [0,1]$，$g_n(x)$ 不收敛。进一步地，当 $g_{n}(x)\geq 0$ 时能不能做到？

(a) (b) 想象在越来越小的区间上，$f$ 越来越大：

$$
f_n(x)=\begin{cases}
    n^2, \quad x\in \left(0,\displaystyle\frac{1}{n}\right)\\
    0, \quad x\in \left\{0\right\} \cup \left[\displaystyle\frac{1}{n},1\right]
\end{cases}
$$

它当然逐点收敛到 $0$，有界只有两个间断点也能保证其可积，不过取分割 $P_n=\left\{0<\displaystyle\frac{1}{2n}<\displaystyle\frac{1}{n}<1\right\}$，得 $L(f_n,P_n)=n^2\cdot \displaystyle\frac{1}{2n}=\displaystyle\frac{n}{2}$，所以 $\displaystyle\int_{0}^{1}{f_n(x)}\, \mathrm{d}{x}\geq \displaystyle\frac{n}{2}$，这足以得到其无界。

(c) 连续也是可以的，这里考虑尖峰形式的函数：

$$
f_n(x)=\begin{cases}
    n^2\bigl(1-\left\lvert 1-2nx \right\rvert\bigr), \quad x\in \left\lbrack 0,\displaystyle\frac{1}{n} \right\rbrack\\
    0, \quad x\in \left( \displaystyle\frac{1}{n},1\right]
\end{cases}
$$

![](https://calculus1437-github-io.pages.dev/images/1787672901206.png)

图像如上所示。

再取分割 $P_n=\left\{0<\displaystyle\frac{1}{4n}<\displaystyle\frac{3}{4n}<1\right\}$，得 $L(f_n,P_n)=\displaystyle\frac{n^2}{2}\cdot \displaystyle\frac{1}{2n}=\displaystyle\frac{n}{4}$，照样是无界的。

(d) 有界的话，积分序列无界是不太可能了。它有没有可能不存在极限？

答案应该是不可能的。我们虽然无法找到一个统一的 $N$ 使得 $f(x)$ 均收敛，但我们肯定能找到一个 $N$ 使得绝大多数的 $f(x)$ 收敛。先控制绝大多数区域的函数值，再通过上界控制剩余区域的积分值，就能得到结论。

首先，对 $\forall\ \varepsilon>0$，令 $I_n=\left\{x\in [0,1]:\left\lvert f_n(x) \right\rvert\geq \varepsilon\right\}$，我们想证明 $\left\lvert I_n \right\rvert\to 0$，但对 $I_n$ 长度的刻画较为困难，因为我们并不知道里面的点的分布，也无法知道是否会有些点反复进入又跳出（比如说一些在不同 $f_n$ 上反复震荡的点）。这里的严格证明涉及后面章节测度论的知识，暂时不做讨论。

(e) 这里的思路是，积分是全局性质，只要让一个小区间的缩减长度总是能抵消增大高度带来的增量就能收敛。但是我们可以在 $[0,1]$ 上随便取这个小区间，而且可以从头到尾一直反复取下去，这样足以摧毁逐点收敛这一局部性质。

这里给出一个简单的例子：函数在小区间内是大于 $0$ 的常数，且让此区间每次移动完整个 $[0,1]$ 后再缩小长度。我们使用著名的示性函数（Indicator function）来构造这个小区间：

$$
\chi_{A}=\begin{cases}
    1, \quad x\in A\\
    0, \quad x\notin A
\end{cases}
$$

现在，令 $g_{1}(x)=\chi_{[0,1]}(x)$，$g_{2}(x)=\chi_{\left\lbrack 0,\frac{1}{2} \right\rbrack}(x)$，$g_{3}(x)=\chi_{\left\lbrack \frac{1}{2},1\right\rbrack}(x)$，$g_{4}(x)=\chi_{\left\lbrack 0,\frac{1}{3} \right\rbrack}$ ... 诸如此类。简单来说，就是用 $\displaystyle\frac{1}{n}$ 长度的小区间逐个覆盖整个 $[0,1]$，然后把长度缩减到 $\displaystyle\frac{1}{n+1}$ 重复过程。这样子得到的积分值确实趋于 $0$，而因为每个点总会被常数区间无限次覆盖，故也不会收敛。

<br/>

!!! question "练习 7.4.7"

    
    假设 ${g}_{n}$ 和 $g$ 是 $\left\lbrack  {0,1}\right\rbrack$ 上的一致有界可积函数，且 ${g}_{n} \rightarrow  g$ 。收敛性不是一致的；然而，在任何形式为 $\left\lbrack  {\delta ,1}\right\rbrack$ 的集合上，其中 $0 < \delta  < 1$ ，收敛性是一致的。证明 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{g}_{n} =$  ${\int }_{0}^{1}g$。

依题意，$\exists\ M>0$，使得 $M>\displaystyle\sup_{n\in \mathbb{N^+}}{\left\{|g_n|,|g|\right\}}$。

对 $\forall\ \varepsilon>0$，取 $\delta=\displaystyle\frac{\varepsilon}{4M}>0$。因为 $g_n,g$ 在 $[\delta,1]$ 上一致收敛，所以 $\displaystyle\lim_{n\to \infty}\displaystyle\int_{\delta}^{1}{g_n(x)}\, \mathrm{d}{x}=\displaystyle\int_{\delta}^{1}{g(x)}\, \mathrm{d}{x}$，即 $\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>N$，有 $\left\lvert \displaystyle\int_{\delta}^{1}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{\delta}^{1}{g(x)}\, \mathrm{d}{x} \right\rvert<\displaystyle\frac{\varepsilon}{2}$。

依题意，$\left\lvert \displaystyle\int_{0}^{\delta}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{0}^{\delta}{g(x)}\, \mathrm{d}{x} \right\rvert\leq \left\lvert \displaystyle\int_{0}^{\delta}{g_{n}(x)}\, \mathrm{d}{x} \right\rvert+\left\lvert \displaystyle\int_{0}^{\delta}{g(x)}\, \mathrm{d}{x} \right\rvert\leq 2\displaystyle\int_{0}^{\delta}{M}\, \mathrm{d}{x}=2M\delta=\displaystyle\frac{\varepsilon}{2}$，所以

$$
\begin{align*}
    &\mathrel{\phantom{=}}\left\lvert \displaystyle\int_{0}^{1}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{0}^{1}{g(x)}\, \mathrm{d}{x} \right\rvert\\
    &=\left\lvert \left(\displaystyle\int_{0}^{\delta}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{0}^{\delta}{g(x)}\, \mathrm{d}{x}\right)+\left(\displaystyle\int_{\delta}^{1}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{\delta}^{1}{g(x)}\, \mathrm{d}{x}\right) \right\rvert\\
    &\leq \left\lvert \displaystyle\int_{0}^{\delta}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{0}^{\delta}{g(x)}\, \mathrm{d}{x} \right\rvert+\left\lvert \displaystyle\int_{\delta}^{1}{g_{n}(x)}\, \mathrm{d}{x}-\displaystyle\int_{\delta}^{1}{g(x)}\, \mathrm{d}{x} \right\rvert\\
    &<\displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon
\end{align*}
$$

所以，$\displaystyle\lim_{n\to \infty}\displaystyle\int_{0}^{1}{g_{n}(x)}\, \mathrm{d}{x}=\displaystyle\int_{0}^{1}{g(x)}\, \mathrm{d}{x}$。

<br/>

---

## 习题 7.5 微积分基本定理

!!! question "练习 7.5.1"

    我们已经看到并非每个导数都是连续的，但请解释为什么我们至少知道每个连续函数都是导数。

因为连续函数是可积的，利用积分定义出来的函数即为它的原函数。

若 $g$ 在 $[a,b]$ 上连续，则 $g$ 在 $[a,b]$ 上可积。定义 $G(x)=\displaystyle\int_{a}^{x}{g(t)}\, \mathrm{d}{t}$，则由 $g$ 的连续性，$\forall\ x\in [a,b]$ 都有 $G'(x)=g(x)$。

<br/>

!!! question "练习 7.5.2"

    (a) 设 $f\left( x\right)  = \left| x\right|$ 并定义 $F\left( x\right)  = {\int }_{-1}^{x}f$ 。为所有 $x$ 找到 $F\left( x\right)$ 的公式。 $F$ 在何处连续？ $F$ 在何处可微？ ${F}^{\prime }\left( x\right)  = f\left( x\right)$ 在何处成立？
    
    (b) 对函数重复(a)部分
    
    $$
    f\left( x\right)  = \begin{cases} 1 & x < 0 \\ 2 & x \geq  0. \end{cases}
    $$

(a) 事实上，由于牛莱公式的证明中用到了中值定理，我们只需要 $\forall\ x\in (a,b)$，$F'(x)=f(x)$ 就够了，也就是我们不需要端点的可导性，也能直接使用这个公式。

所以以 $f$ 不可导的点为端点，先计算出两侧的积分值：$\displaystyle\int_{0}^{x}{f(t)}\, \mathrm{d}{t}=\displaystyle\int_{0}^{x}{t}\, \mathrm{d}{t}=\displaystyle {\displaystyle\frac{1}{2}t^2}\, \bigg|_{0}^{x}=\displaystyle\frac{1}{2}x^2$。（$x>0$）

$\displaystyle\int_{x}^{0}{f(t)}\, \mathrm{d}{t}=\displaystyle\int_{x}^{0}{-t}\, \mathrm{d}{t}=\displaystyle {-\displaystyle\frac{1}{2}t^2}\, \bigg|_{x}^{0}=\displaystyle\frac{1}{2}x^2$。（$x<0$）

所以 $x\leq 0$ 时，$F(x)=\displaystyle\int_{-1}^{0}{f(t)}\, \mathrm{d}{t}-\displaystyle\int_{x}^{0}{f(t)}\, \mathrm{d}{t}=\displaystyle\frac{1}{2}\left(1-x^2\right)$；

$x>0$ 时，$F(x)=\displaystyle\int_{-1}^{0}{f(t)}\, \mathrm{d}{t}+\displaystyle\int_{0}^{x}{f(t)}\, \mathrm{d}{t}=\displaystyle\frac{1}{2}\left(1+x^2\right)$。

综上：

$$
F(x)=\begin{cases}
    \displaystyle\frac{1}{2}\left(1-x^2\right), \quad x\leq 0\\
    \displaystyle\frac{1}{2}\left(1+x^2\right), \quad x>0
\end{cases}
$$

唯一要谨慎对待的是 $x=0$ 的位置。对连续性而言：

$$
\displaystyle\lim_{x\to 0^{-}}F(x)=\displaystyle\frac{1}{2}=\displaystyle\lim_{x\to 0^{+}}F(x)
$$

所以 $F$ 在 $0$ 处连续，进而在 $\mathbb{R}$ 上均连续。

对可导性而言：

$$
\begin{aligned}
        \displaystyle\lim_{x\to 0^{-}}\displaystyle\frac{F(x)-F(0)}{x-0}=0 & & \displaystyle\lim_{x\to 0^{+}}\displaystyle\frac{F(x)-F(0)}{x-0}=0
\end{aligned}
$$

所以 $F'(0)=0=f(0)$。

所以 $F$ 在 $\mathbb{R}$ 可导，且恒有 $F'(x)=f(x)$。

(b) 同理，$x\leq 0$ 时，$F(x)=\displaystyle\int_{-1}^{0}{f(t)}\, \mathrm{d}{t}-\displaystyle\int_{x}^{0}{f(t)}\, \mathrm{d}{t}=\displaystyle 1+x$；

$x>0$ 时，$F(x)=\displaystyle\int_{-1}^{0}{f(t)}\, \mathrm{d}{t}+\displaystyle\int_{0}^{x}{f(t)}\, \mathrm{d}{t}=\displaystyle 1+2x$。

得到：

$$
F(x)=\begin{cases}
    1+x, \quad x\leq 0\\
    1+2x, \quad x>0
\end{cases}
$$

$F$ 在 $\mathbb{R}$ 上仍然是连续的。然而，计算左右导数：

$$
\begin{aligned}
    \displaystyle\lim_{x\to 0^{-}}\displaystyle\frac{F(x)-F(0)}{x-0}=1 & & \displaystyle\lim_{x\to 0^{+}}\displaystyle\frac{F(x)-F(0)}{x-0}=2
\end{aligned}
$$

我们会发现它们并不相等，因此 $F$ 在 $0$ 处不可导。

当然，在 $x\in \mathbb{R}\setminus \left\{0\right\}$ 上，仍然有 $F'(x)=f(x)$。

<br/>

<a id="7.5.3"></a>

!!! question "练习 7.5.3"

    牛莱公式中的假设，即对于所有 ${F}^{\prime }\left( x\right)  = f\left( x\right)$ ， $x \in  \left\lbrack  {a,b}\right\rbrack$ 这一条件实际上是过于严格的。仔细阅读证明，并准确陈述在 $f$ 和 $F$ 之间的关系只需要假设什么就能使证明成立。

我们在对牛莱公式的证明中，对每个小区间上都使用了中值定理进行估计。事实上，中值定理不要求每个小区间的端点可导，所以在这些点上都可以有 $F'(x)\neq f(x)$。所以，$F$ 可以在有限个点上有 $F'(x)\neq f(x)$，在其他的点上 $F'(x)=f(x)$，使得牛莱公式仍然成立。

<mark>关于 $F$ 的连续性是不得不提的一点</mark>，事实上，中值定理仍然要求 $F$ 是连续的。若不连续，我们可以在某个不可导点左右构造无数个导数等于 $f$ 的分段函数，但牛莱公式的计算结果将会大相径庭。

<br/>

<a id="7.5.4"></a>

!!! question "练习 7.5.4（自然对数与欧拉常数）"

    设
    
    $$
    L\left( x\right)  = {\int }_{1}^{x}\frac{1}{t}{dt}
    $$
    
    其中我们仅考虑 $x > 0$ 。
    
    (a) $L\left( 1\right)$ 是什么？找出 ${L}^{\prime }\left( x\right)$ 。
    
    (b) 证明 $L$ 是严格递增的；即，证明如果 $0 < x < y$ ，则 $L\left( x\right)  < L\left( y\right)$ 。
    
    (c) 证明 $L\left( {xy}\right)  = L\left( x\right)  + L\left( y\right)$ 。(将 $y$ 视为常数并对 $g\left( x\right)  = L\left( {xy}\right)$ 进行微分。)
    
    (d) 证明 $L\left(\displaystyle\frac{x}{y}\right) = L\left( x\right) - L\left( y\right)$ 。
    
    (e) 令 
    
    $$\gamma_{n}=\displaystyle\sum_{k=1}^{n}\displaystyle\frac{1}{k}-L(n)$$
    
    证明 $\left\{\gamma_{n}\right\}$ 收敛。值得一提的是，$\gamma=\displaystyle\lim_{n\to \infty}\gamma_{n}$ 被称为欧拉常数。
    
    (f) 解释序列 $\left\{\gamma_{2n}-\gamma_{n}\right\}$ 如何得到以下的有趣结果：
    
    $$
    L(2)=1-\displaystyle\frac{1}{2}+\displaystyle\frac{1}{3}-\displaystyle\frac{1}{4}+\displaystyle\frac{1}{5}-\displaystyle\frac{1}{6}+\cdots
    $$
    
    $$
    \ln{2}=\displaystyle\lim_{n\to \infty}\displaystyle\sum_{k=n+1}^{2n}\displaystyle\frac{1}{k}
    $$

(a) $L(1)=0$。

令 $l(x)=\displaystyle\frac{1}{x}$，则 $L(x)=\displaystyle\int_{1}^{x}{l(t)}\, \mathrm{d}{t}$。

因为 $l$ 在 $(0,+\infty)$ 上连续，由微积分基本定理，$L$ 在 $(0,+\infty)$ 上可导，且 $L'(x)=l(x)=\displaystyle\frac{1}{x}$。

(b) 因为 $L'(x)>0$，且 $\exists\ \xi\in (x,y)$ 使得：

$$
L(y)-L(x)=L'(\xi)(y-x)>0
$$

所以 $L(x)<L(y)$，即 $L$ 严格递增。

(c) 令 $g(x)=L(xy)$，由复合函数求导法则，$g'(x)=yL'(xy)=\displaystyle\frac{1}{x}=L'(x)$。

所以 $g'(x)-L'(x)=0$，由中值定理可推出 $g(x)-L(x)$ 是常数函数。

又因为 $g(1)-L(1)=L(y)$，所以 $g(x)-L(x)=L(y)$。

所以 $L(xy)=L(x)+L(y)$。

<mark>这可以看作对数函数单调性与可加性的另一种解释。</mark>

(d) 由 (c) 可得：

$$
L\left(\displaystyle\frac{x}{y}\right)+L(y)=L\left(\displaystyle\frac{x}{y}\cdot y\right)=L(x)
$$

所以 $L\left(\displaystyle\frac{x}{y}\right)=L(x)-L(y)$。

(e) 估计的方法有很多，我们先分段估计一下 $L(n)$ 的大小。分段估计可得：

$$
\begin{aligned}
    L(n)&=\displaystyle\sum_{k=1}^{n-1}\displaystyle\int_{k}^{k+1}{\displaystyle\frac{1}{t}}\, \mathrm{d}{t} \\
    \displaystyle\frac{1}{k+1}&\leq \displaystyle\int_{k}^{k+1}{\displaystyle\frac{1}{t}}\, \mathrm{d}{t}\leq \displaystyle\frac{1}{k}\\
    \displaystyle\sum_{k=1}^{n-1}\displaystyle\frac{1}{k+1}&\leq L(n)\leq \displaystyle\sum_{k=1}^{n-1}\displaystyle\frac{1}{k}\\
    \displaystyle\frac{1}{n}&\leq \displaystyle\sum_{k=1}^{n}\displaystyle\frac{1}{k}-L(n)\leq 1
\end{aligned}
$$

所以 $\gamma_{n}$ 是有界的。现在就使用单调有界定理进行估计：

因为 $\gamma_{n+1}-\gamma_{n}=\displaystyle\frac{1}{n+1}-\displaystyle\int_{n}^{n+1}{\displaystyle\frac{1}{t}}\, \mathrm{d}{t}\leq 0$，所以 $\gamma_{n}$ 单调递减。由单调有界定理，$\left\{\gamma_{n}\right\}$ 收敛。

(f) $\gamma_{2n}-\gamma_{n}=\displaystyle\sum_{k=n+1}^{2n}\displaystyle\frac{1}{k}-\left(L(2n)-L(n)\right)=\displaystyle\sum_{k=n+1}^{2n}\displaystyle\frac{1}{k}-L(2)$。

如果用 $\gamma_{2n}$ 里面的 $\displaystyle\frac{1}{2k}$ 项分别减去 $\gamma_{n}$ 中的 $\displaystyle\frac{1}{k}$ 项，就会得到：

$$
\gamma_{2n}-\gamma_{n}=1-\displaystyle\frac{1}{2}+\displaystyle\frac{1}{3}-\displaystyle\frac{1}{4}+\cdots-\displaystyle\frac{1}{2n}-L(2)
$$

因为 $\left\{\gamma_{n}\right\}$ 收敛，所以 $\displaystyle\lim_{n\to \infty}\gamma_{2n}-\gamma_{n}=0$。综合上面两种形式可得结果：

$$
\ln{2}=L(2)=1-\displaystyle\frac{1}{2}+\displaystyle\frac{1}{3}-\displaystyle\frac{1}{4}+\cdots=\displaystyle\lim_{n\to \infty}\displaystyle\sum_{k=n+1}^{2n}\displaystyle\frac{1}{k}
$$

<br/>

!!! question "练习 7.5.5"

    微积分基本定理可用于在导数序列连续的附加假设下，为定理 6.3.1 提供更简短的论证。
    
    假设 ${f}_{n} \rightarrow  f$ 逐点收敛且 ${f}_{n}^{\prime } \rightarrow  g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上一致收敛。假设每个 ${f}_{n}^{\prime }$ 都是连续的，我们可以应用定理 7.5.1 (i) 得到
    
    $$
    {\int }_{a}^{x}{f}_{n}^{\prime } = {f}_{n}\left( x\right)  - {f}_{n}\left( a\right)
    $$
    
    对于所有 $x \in  \left\lbrack  {a,b}\right\rbrack$ 。证明 $g\left( x\right)  = {f}^{\prime }\left( x\right)$。

<mark>这题推导到后面的关键是意识到 $f_{n}'$ 在连续情形下相比于可积情形多出来的用途。</mark>我们现在直接来推一推：

对 $\forall\ n\in \mathbb{N^+}$，$\forall\ x\in [a,b]$，因为 $f_{n}'$ 是连续的，所以它也是可积的。由牛莱公式我们就可以知道：

$$
\displaystyle\int_{a}^{x}{f_{n}'(t)}\, \mathrm{d}{t}=f_{n}(x)-f_{n}(a)
$$

现在，因为 $f_{n}'\to g$ 一致收敛，所以上式左边可以取极限。又因为 $f_{n}\to f$ 逐点收敛，所以右边也可以取极限。于是我们有：

$$
\displaystyle\int_{a}^{x}{g(t)}\, \mathrm{d}{t}=f(x)-f(a)
$$

现在 $f$ 的可导性实际上是未知的，所以我们不能简单地把 $g(x)$ 代替成 $f'(x)$。但是，由于 $f_{n}'\to g$ 一致收敛，且 $f_{n}'$ 是连续的，所以我们能得出 $g$ 也是连续的。由微积分定理其一，即变上限积分求导定理，我们有 $\displaystyle\int_{a}^{x}{g(t)}\, \mathrm{d}{t}=f(x)-f(a)$ 是可导的，且：

$$
\begin{aligned}
    &\mathrel{\phantom{\Rightarrow}}&\left(f(x)-f(a)\right)'&=\left(\displaystyle\int_{a}^{x}{g(t)}\, \mathrm{d}{t}\right)'=g(x)\\
    &\Rightarrow& f'(x)&=g(x)
\end{aligned}
$$

这样就得到了证明。

<mark>通过连续性反向导出可导性，是这题的核心思想。</mark>

<br/>

!!! question "练习 7.5.6"

    令 $G(x)=\displaystyle\int_{a}^{x}{f(x)}\, \mathrm{d}{x}$。在假设 $f$ 在 $[a,b]$  上连续的情况下利用 $G$ 快速得出牛顿-莱布尼兹公式的定理。

若 $f$ 在 $[a,b]$ 上连续，则 $G(x)$ 在 $[a,b]$ 上可导，且 $G'(x)=f(x)$。

这样 $G$ 就是 $f$ 的一个原函数了。并且因为 $\displaystyle\int_{a}^{b}{f(x)}\, \mathrm{d}{x}=G(b)-G(a)$，所以牛顿-莱布尼兹公式相关定理得证。

<br/>

!!! question "练习 7.5.7（积分均值）"

    如果 $g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上连续，证明存在一个点 $c \in  \left( {a,b}\right)$ 使得
    
    $$
    g\left( c\right)  = \frac{1}{b - a}{\int }_{a}^{b}g
    $$

这里的叙述很有意思。积分可以看作对区间上全体函数值的一个求和，所以除以区间长度就能得到一个平均值了。这比区间上的离散均值估计 $\displaystyle\frac{1}{n}\displaystyle\sum_{i=1}^{n}f(x_{i})$ 会准确很多。

这样一来，我们就会想到，这个平均值应该在函数整个区间上的最大、最小值之间。而由介值定理，最大、最小值之间的任意值都能被函数取到，这就给我们的证明提供了一条很清晰的路线。

因为 $g$ 在 $[a,b]$ 上连续，所以 $g$ 在 $[a,b]$ 上有最大值 $M$ 和最小值 $m$。由积分不等式，我们有：

$$
\begin{aligned}
    \displaystyle\int_{a}^{b}{m}\, \mathrm{d}{x}\leq \displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}\leq \displaystyle\int_{a}^{b}{M}\, \mathrm{d}{x}\\
    m(b-a)\leq \displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}\leq M(b-a)\\
\end{aligned}
\Rightarrow
m\leq \displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}\leq M
$$

所以，$\exists\ c\in [a,b]$ 使得 $g(c)=\displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}$。

但是等等！题目里的 $c$ 要求在 $(a,b)$ 之内，这说明平均值并非普通的一个介值，我们需要更精细的估计。

如果 $c$ 正好取到了端点上，利用积分的性质，应该是能证明开区间内存在另一点 $c_1$ 使得 $g(c)=g(c_{1})$ 的。我们按照这个往下推理：

若 $\exists\ c\in (a,b)$，使得 $g(c)=\displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}$，则问题得证。

否则，$c\in \left\{a,b\right\}$。不妨令 $c=a$。若 $\exists\ x_1,x_2\in (a,b]$，$x_1<x_2$，使得 $\left(g(x_1)-g(a)\right)\left(g(x_2)-g(a)\right)<0$，则 $\exists\ c_1\in (x_1,x_2)$ 使得 $g(c_1)=g(a)$，这肯定是矛盾的。所以 $\left(g(x_1)-g(a)\right)\left(g(x_2)-g(a)\right)> 0$，这里我们不妨设 $g(x)>g(a)$ 在 $(a,b]$ 上恒成立。

因为 $g$ 是连续函数，所以由积分不等式，

$$
\displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}>\displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(a)}\, \mathrm{d}{x}=g(a)
$$

这与假设矛盾。所以一定 $\exists\ c\in (a,b)$ 使得 $g(c)=\displaystyle\frac{1}{b-a}\displaystyle\int_{a}^{b}{g(x)}\, \mathrm{d}{x}$。

<br/>

!!! question "练习 7.5.8"

    给定函数 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上，定义 $f$ 的全变差为
    
    为
    
    $$
    {Vf} = \sup \left\{  {\mathop{\sum }\limits_{{k = 1}}^{n}\left| {f\left( {x}_{k}\right)  - f\left( {x}_{k - 1}\right) }\right| }\right\}  ,
    $$
    
    其中上确界取遍 $\left\lbrack  {a,b}\right\rbrack$ 的所有分割 $P$ 。
    
    (a) 如果 $f$ 是连续可微的( ${f}^{\prime }$ 作为连续函数存在)，使用微积分基本定理证明 ${Vf} \leq  {\int }_{a}^{b}\left| {f}^{\prime }\right|$ 。
    
    (b) 使用中值定理建立反向不等式并得出结论 ${Vf} = {\int }_{a}^{b}\left| {f}^{\prime }\right|$。

(a) 由微积分基本定理，$\displaystyle\int_{x_{k-1}}^{x_{k}}{f'(x)}\, \mathrm{d}{x}=f(x_k)-f(x_{k-1})$。

所以：

$$
\begin{aligned}
    \displaystyle\sum_{k=1}^{n}\left\lvert f(x_{k}) - f(x_{k-1}) \right\rvert &= \sum_{k=1}^{n} \left| \int_{x_{k-1}}^{x_{k}} f'(x) \, dx \right| \\
    &\leq \displaystyle\sum_{k=1}^{n}\displaystyle\int_{x_{k-1}}^{x_{k}}{\left\lvert f'(x) \right\rvert}\, \mathrm{d}{x}\\
    &\leq \displaystyle\int_{a}^{b}{\left\lvert f'(x) \right\rvert}\, \mathrm{d}{x}
\end{aligned}
$$

由上确界的定义，$Vf\leq \displaystyle\int_{a}^{b}{\left\lvert f'(x) \right\rvert}\, \mathrm{d}{x}$。

(b) 由中值定理，$\exists\ \xi_k\in (x_{k-1},x_k)$，使得 $f(x_k)-f(x_{k-1})=f'(\xi_k)(x_k-x_{k-1})$。

所以，对任意的分割 $P$，有：

$$
\begin{aligned}
    \displaystyle\sum_{k=1}^{n}\left\lvert f(x_{k}) - f(x_{k-1}) \right\rvert &= \sum_{k=1}^{n} \left| f'(\xi_k)(x_k-x_{k-1}) \right| \\
    &= \sum_{k=1}^{n} \left| f'(\xi_k) \right| (x_k-x_{k-1}) \\
    &\geq L(\left\lvert f' \right\rvert,P)
\end{aligned}
$$

由上确界的定义，$Vf\geq L(\left\lvert f' \right\rvert,P)$。再由积分上确界的定义可以得到 $Vf\geq \displaystyle\int_{a}^{b}{\left\lvert f'(x) \right\rvert}\, \mathrm{d}{x}$。

<br/>

!!! question "练习 7.5.9"

    设
    
    $$
    h\left( x\right)  = \begin{cases} 1 & x\neq 1 \\ 0 & x = 1 \end{cases}
    $$
    
    并定义 $H\left( x\right)  = {\int }_{0}^{x}h$ 。证明即使 $h$ 在 $x = 1$ 处不连续， $H\left( x\right)$ 在 $x = 1$ 处仍然可微。

这里假设 $x>0$，计算 $H(x)=\displaystyle\int_{0}^{x}{h(t)}\, \mathrm{d}{t}=x$。

所以 $H'(x)=1$，在 $x=1$ 处仍然可微。事实上，$H'(1)=\displaystyle\lim_{x\to 1}h(1)\neq h(1)$。

<br/>

!!! question "练习 7.5.10"

    假设 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，并且在 $c \in  \left( {a,b}\right)$ 处有一个“跳跃间断点”。这意味着当 $x$ 从左和从右接近 $c$ 时，两个单侧极限都存在，但
    
    $$
    \mathop{\lim }\limits_{{x \rightarrow  {c}^{ - }}}f\left( x\right)  \neq  \mathop{\lim }\limits_{{x \rightarrow  {c}^{ + }}}f\left( x\right) .
    $$
    
    (这一现象在第4.6节中有更详细的讨论。)
    
    证明 $F\left( x\right)  = {\int }_{a}^{x}f$ 在 $x = c$ 处不可微。

我们分析一下 $\displaystyle\frac{F(x)-F(c)}{x-c}=\displaystyle\frac{\displaystyle\int_{c}^{x}{f(t)}\, \mathrm{d}{t}}{x-c}$ 的变化情况。

这里假设左侧极限为 $A$，右侧极限为 $B$，由题意 $A\neq B$。

$x>c$ 时，对 $\forall\ \varepsilon>0$，$\exists\ \delta>0$，对 $\forall\ x\in (c,c+\delta)$，$\left\lvert f(x)-B \right\rvert<\varepsilon$。

这样一来，$\displaystyle\int_{c}^{x}{\left\lvert f(t)-B \right\rvert}\, \mathrm{d}{t}\leq \displaystyle\int_{c}^{x}{\varepsilon}\, \mathrm{d}{t}=\left(x-c\right)\varepsilon$，即

$$
\begin{aligned}
    \left\lvert \displaystyle\frac{1}{x-c}\displaystyle\int_{c}^{x}{f(t)}\, \mathrm{d}{t}-B \right\rvert&=\displaystyle\frac{1}{x-c}\left\lvert \displaystyle\int_{c}^{x}{\left(f(t)-B\right)}\, \mathrm{d}{t} \right\rvert\\&\leq \displaystyle\frac{1}{x-c}\displaystyle\int_{c}^{x}{\left\lvert f(t)-B \right\rvert}\, \mathrm{d}{t}\\&\leq \varepsilon
\end{aligned}
$$

所以 $\displaystyle\lim_{x\to c^{+}}\displaystyle\frac{\displaystyle\int_{c}^{x}{f(t)}\, \mathrm{d}{t}}{x-c}=B$。同理可得 $\displaystyle\lim_{x\to c^{-}}\displaystyle\frac{\displaystyle\int_{c}^{x}{f(t)}\, \mathrm{d}{t}}{x-c}=A$，而 $A\neq B$。所以 $F(x)$ 在 $x=c$ 处不可微。

<br/>

<a id="7.5.11"></a>

!!! question "练习 7.5.11（连续单调函数在有理数集上不可微）"

    第5章的结语提到存在一个连续单调函数，该函数在实数集 $\mathbb{R}$ 的一个稠密子集上不可微。结合练习7.5.10和练习6.4.8的结果，展示如何构造这样的函数。

我们把 6.4.8 构造的函数和结论直接照抄过来：

令 $\{r_1, r_2, r_3, \dots\}$ 是有理数集的一个枚举。对于每个 $r_n \in \mathbb{Q}$，定义

$$
u_n(x) = \begin{cases} 1/2^n & \text{若 } x > r_n \\ 0 & \text{若 } x \le r_n \end{cases}
$$

我们的 $h(x)=\displaystyle\sum_{n=1}^{\infty}u_{n}(x)$ 是一个在 $\mathbb{Q}$ 上不连续的函数，并且每个不连续点都是跳跃间断点。

对任意一个闭区间 $[a,b]$，首先因为 $\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{1}{2^n}=1$，$h$ 是有界的。其次，由于 $h$ 的间断点集是零测的，由练习 [7.3.6](#7.3.6) 可知 $h$ 在 $[a,b]$ 上可积。<mark style="color: red;">注意这里的引用有误！现在还没有证明不连续点集能被有限开区间覆盖，要到 7.6 节 Lebesgue 定理出现后才能严格证明！</mark>

令 $H(x)=\displaystyle\int_{0}^{x}{h(t)}\, \mathrm{d}{t}$，由 $h$ 的可积性，$H$ 在 $\mathbb{R}$ 上连续。又因为 $h$ 在 $\mathbb{Q}$ 上的每个点都是跳跃间断点，由练习 [7.5.10](#7.5.10) 可知 $H$ 在 $\mathbb{Q}$ 上的每个点都不可微。

然后，因为 $h(x)\geq 0$，所以对 $\forall\ x_{1}<x_{2}$，$H(x_2)-H(x_1)=\displaystyle\int_{x_{1}}^{x_{2}}{h(t)}\, \mathrm{d}{t}\geq 0$，所以 $H$ 在 $\mathbb{R}$ 上单调递增。

<a id="7.5.12"></a>

!!! question "练习 7.5.12（变量替换定理）"

    
    假设 $f:[c,d]\to \mathbb{R}$ 是一个连续函数，$g:[a,b]\to \mathbb{R}$ 是一个连续可微函数，且 $g([a,b])\subseteq [c,d]$，以保证复合函数 $f\circ g$ 是定义良好的。
    
    (a) $f$ 是否一定是某个函数的导数？$\left(f\circ g\right)g'$ 呢？
    
    (b) 证明变量替换定理：
    
    $$
    \displaystyle\int_{a}^{b}{f\left(g(x)\right)g'(x)}\, \mathrm{d}{x}=\displaystyle\int_{g(a)}^{g(b)}{f(t)}\, \mathrm{d}{t}
    $$

(a) 因为 $f$ 是连续函数，由微积分基本定理，定义 $F(x)=\displaystyle\int_{c}^{x}{f(t)}\, \mathrm{d}{t}$，有 $F'(x)=f(x)$。

因为 $g$ 和 $g'$ 都是连续函数，由连续函数的四则运算和复合运算性质，$\left(f\circ g\right)g'$ 也是连续函数。定义 $G(x)=\displaystyle\int_{a}^{x}{f\left(g(t)\right)g'(t)}\, \mathrm{d}{t}$， 则 $G'(x)=f\left(g(x)\right)g'(x)$。

(b) 因为 $\bigl(F(g(x))\bigr)'=F'(g(x))g'(x)=f(g(x))g'(x)=G'(x)$，所以 $F(g(x))=G(x)+k$，其中 $k$ 为常数。

所以 $F(g(b))-F(g(a))=G(b)-G(a)$，即 $\displaystyle\int_{a}^{b}{f(g(x))g'(x)}\, \mathrm{d}{x}=\displaystyle\int_{g(a)}^{g(b)}{f(t)}\, \mathrm{d}{t}$。

<br/>

---

## 习题 7.6 Riemann 可积性的 Lebesgue 准则

我们现在回到对连续性与 Riemann 积分之间关系的探讨。我们已经证明了连续函数是可积的，并且积分也存在于仅有有限个间断点的函数中。在另一极端，我们看到 Dirichlet 函数在 $[0,1]$ 上的每一点都间断，因此不是 Riemann 可积的。接下来的例子表明，可积函数的间断点集可以是无限的，甚至可以是不可数的。（这些也作为 7.3 节中的练习出现。）

### 具有无限间断点的 Riemann 可积函数

回顾 4.1 节，Thomae 函数

$$
t\left( x\right)  = \begin{cases} 1 & x = 0 \\ 1/n & x = m/n \in  \mathbb{Q} \setminus  \{ 0\} ,\quad n > 0,\gcd(m,n) = 1 \\ 0 & x \notin  \mathbb{Q} \end{cases}
$$

在无理数集上连续，并且在每个有理点处间断。让我们证明 Thomae 函数在 $[0,1]$ 上可积，且 $\int_0^1 t = 0$。

设 $\epsilon > 0$。策略与往常一样，是构造 $[0,1]$ 的一个分割 $P_{\epsilon}$，使得 $U(t,P_{\epsilon}) - L(t,P_{\epsilon}) < \epsilon$。

!!! question "练习 7.6.1"

    
    (a) 首先，论证对于 $[0,1]$ 的任意分割 $P$，都有 $L(t, P) = 0$。
    
    (b) 考虑点集 $D_{\epsilon /2} = \{x:t(x)\geq \epsilon /2\}$。$D_{\epsilon /2}$ 有多大？
    
    (c) 为了完成论证，解释如何构造 $[0,1]$ 的一个分割 $P_{\epsilon}$，使得 $U(t, P_{\epsilon}) < \epsilon$。

对 $\forall\ I\in P$，由无理数的稠密性，$\exists\ x\in I$ 使得 $x$ 为无理数，所以 $t(x)=0$。又 $t(x)\geq 0$，所以 $\displaystyle\inf_{x\in I} t(x) = 0$。

所以 $L(t,P)=\displaystyle\sum_{I\in P}^{} \inf_{x\in I} t(x)\cdot \left\lvert I \right\rvert = \displaystyle\sum_{I\in P}^{} 0\cdot \left\lvert I \right\rvert = 0$。

(b) 对 $\forall\ \varepsilon>0$，满足 $\displaystyle\frac{1}{n}\geq \displaystyle\frac{\varepsilon}{2}$ 即 $n\leq \displaystyle\frac{2}{\varepsilon}$ 是有限的，所以 $D_{\frac{\varepsilon}{2}}$ 是有限集。

(c) 这里的思路与 [7.3.6](#7.3.6) 相一致，控制那些值较大的点集所在的闭区间长度大小。

对上述的 $\varepsilon>0$ 以及与之相匹配的 $D_{\frac{\varepsilon}{2}}=\left\{x_1,x_2,\cdots,x_n\right\}$，构造这样的分割 $P$，使得对 $\forall\ x_i\in D_{\frac{\varepsilon}{2}}$，$\exists\ I_{i}\in P$ 和 $\delta>0$ 使得 $V_{\delta}(x_{i})\subseteq I_{i}$，且 $\left\lvert I_i \right\rvert<\displaystyle\frac{\varepsilon}{2n}$。$\color{red}{\text{注意若}}$ $\color{red}{x}$ $\color{red}{\text{为端点，则要构造单侧邻域上的开区间。}}$

上面的叙述先控制了包含 $D_{\frac{\varepsilon}{2}}$ 的区间长度之和 $\displaystyle\sum_{i=1}^{n}\left\lvert I_i \right\rvert<\displaystyle\frac{\varepsilon}{2}$，又保证了每个 $x_{i}$ 都在唯一一个 $I_i$ 的内部，从而排除了其落在其他区间上的可能。

记 $P$ 中的剩余区间为 $B_1,B_2,\cdots,B_p$，则 $\displaystyle\sum_{i=1}^{n}\left\lvert I_i \right\rvert+\displaystyle\sum_{i=1}^{p}\left\lvert B_i \right\rvert=1$。

所以：

$$
\begin{aligned}
    U(t,P)&=\displaystyle\sum_{I\in P}^{}\displaystyle\sup_{x\in I}{t(x)}\cdot \left\lvert I \right\rvert\\
    &=\displaystyle\sum_{i=1}^{n}\displaystyle\sup_{x\in I_{i}}{t(x)}\cdot \left\lvert I_{i} \right\rvert+\displaystyle\sum_{i=1}^{p}\displaystyle\sup_{x\in B_{i}}{t(x)}\cdot \left\lvert B_i \right\rvert\\
    &< \displaystyle\sum_{i=1}^{n}1\cdot \displaystyle\frac{\varepsilon}{2n}+\displaystyle\sum_{i=1}^{p}\displaystyle\frac{\varepsilon}{2}\cdot \left\lvert B_i \right\rvert\\
    &=1\displaystyle\sum_{i=1}^{n}\displaystyle\frac{\varepsilon}{2n}+\displaystyle\frac{\varepsilon}{2}\displaystyle\sum_{i=1}^{p}\left\lvert B_i \right\rvert\\
    &<\displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon
\end{aligned}
$$

所以 $U(t)\leq 0$。又因为 $U(t)\geq L(t)=0$，所以 $U(t)=L(t)=0$。这就证明了 Thomae 函数在 $\left[0,1\right]$ 上可积，且 $\displaystyle\int_{0}^{1}{t(x)}\, \mathrm{d}{x}=0$。

<br/>

<hr>

我们首次在 3.1 节中遇到了 Cantor 集 $C$。我们随后了解到，$C$ 是区间 $[0,1]$ 的一个紧的、不可数的子集。

练习 4.3.12 的要求是证明该函数

$$
g\left( x\right)  = \begin{cases} 1 & x \in  C \\ 0 & x \notin  C \end{cases}
$$

在 $C$ 的补集的每一点上连续，并且在 $C$ 的每一点上都有间断。因此，$g$ 在一个不可数无限集上不连续。

<br/>

!!! question "练习 7.6.2"

    
    利用 $C = \mathop{\bigcap }\limits_{{n = 0}}^{\infty }{C}_{n}$ 这一事实，其中每个 ${C}_{n}$ 由有限个闭区间的并集组成，论证 $g$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上是 Riemann 可积的。

见 [7.3.6](#7.3.6)。

<br/>

<hr>

### 零测集

Thomae 函数在 $\left\lbrack  {0,1}\right\rbrack$ 中的每个有理数点处都不连续。尽管这个集合是无限的，但我们已经看到 $\mathbb{Q}$ 的任何子集都是可数的。可数无限集是最小类型的无限集。Cantor 集是不可数的，但在某种意义上它也是“小”的，我们现在可以精确地描述这一点。在第 3 章的引言中，我们提出了一个论点，即 Cantor 集的“长度”为零。这里的“长度”一词并不恰当，因为它实际上只能应用于区间或区间的并集，而 Cantor 集并非如此。有一种将长度概念推广到更一般集合的方法，称为集合的测度（measure）。在我们的讨论中，感兴趣的是测度为零的子集。

**定义 7.6.1.** 称一个集合 $A \subseteq  \mathbb{R}$ 具有零测度，如果对于所有 $\varepsilon  > 0$，存在一个可数的开区间集合 ${O}_{n}$，使得 $A$ 包含在所有区间的并集中，并且所有区间的长度之和小于或等于 $\varepsilon$。更准确地说，如果 $\left| {O}_{n}\right|$ 表示区间 ${O}_{n}$ 的长度，那么我们有

$$
A \subseteq  \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{O}_{n}\; 且\;\mathop{\sum }\limits_{{n = 1}}^{\infty }\left| {O}_{n}\right|  \leq  \varepsilon .
$$

**例 7.6.2.** 考虑一个有限集合 $A = \left\{  {{a}_{1},{a}_{2},\ldots ,{a}_{N}}\right\}$。为了证明 $A$ 具有零测度，令 $\varepsilon  > 0$ 为任意值。对于每个 $1 \leq  n \leq  N$，构造区间

$$
{G}_{n} = \left( {{a}_{n} - \frac{\varepsilon }{2N},{a}_{n} + \frac{\varepsilon }{2N}}\right) .
$$

显然，$A$ 包含在这些区间的并集中，并且

$$
\mathop{\sum }\limits_{{n = 1}}^{N}\left| {G}_{n}\right|  = \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\varepsilon }{N} = \varepsilon
$$

<br/>

!!! question "练习 7.6.3"

    
    证明任何可数集的测度为零。

对任意可数集 $A=\left\{p_1,p_2,\cdots\right\}$，和 $\forall\ \varepsilon>0$，采用如下的包含策略：

令 $\left\lvert O_{i} \right\rvert<\displaystyle\frac{\varepsilon}{2^{i}}$，且 $p_i\in O_i$，那么就有：

$$
A\subseteq \bigcup_{i=1}^{\infty} O_i  \quad \text{且} \quad \displaystyle\sum_{i=1}^{\infty}\left\lvert O_{i} \right\rvert<\varepsilon
$$

<br/>

<a id="7.6.4"></a>

!!! question "练习 7.6.4"

    
    证明 Cantor 集（不可数）的测度为零。

事实上，[7.3.6](#7.3.6) 的积分求值手段就用到了零测集的方法。同样的，对于 $C_n$，它事实上由总长度为 $\left(\displaystyle\frac{2}{3}\right)^{n}$ 的 $2^{n}$ 个闭区间组成，那么对每个闭区间取稍稍大一点的开区间来覆盖它，这个稍稍大一点可以是多出 $\displaystyle\frac{\varepsilon}{2^{n+1}}$，那么就有：

对 $\forall\ \varepsilon>0$，取 $\left(\displaystyle\frac{2}{3}\right)^{n}<\displaystyle\frac{\varepsilon}{2}$，即 $n>\displaystyle\frac{\ln{\varepsilon}-\ln{2}}{\ln{2}-\ln{3}}$，那么对应的开区间总长为：

$$
\displaystyle\sum_{i=1}^{2^{n}}\left\lvert O_{i} \right\rvert=\left(\displaystyle\frac{2}{3}\right)^{n}+2^{n}\cdot \displaystyle\frac{\varepsilon}{2^{n+1}}<\varepsilon
$$

这样就证明了 Cantor 集的测度为零。

<a id="7.6.5"></a>

<br/>

!!! question "练习 7.6.5"

    
    证明如果两个集合 $A$ 和 $B$ 的测度都为零，那么 $A \cup  B$ 的测度也为零。此外，讨论更强命题的证明，即测度为零的集合的可数并集的测度也为零。（第二个命题是正确的，但完全严格的证明需要关于第 2.8 节中讨论的双重求和的结果。）

对 $\forall\ \varepsilon>0$，

对于集合 $A$，存在一列开区间集 $\left\{O_{A,i}\right\}_{i=1}^{\infty}$，使得 $A\subseteq \displaystyle\bigcup_{i=1}^{\infty} O_{A,i}$ 且 $\displaystyle\sum_{i=1}^{\infty}\left\lvert O_{A,i} \right\rvert<\displaystyle\frac{\varepsilon}{2}$。

对于集合 $B$，存在一列开区间集 $\left\{O_{B,i}\right\}_{i=1}^{\infty}$，使得 $B\subseteq \displaystyle\bigcup_{i=1}^{\infty} O_{B,i}$ 且 $\displaystyle\sum_{i=1}^{\infty}\left\lvert O_{B,i} \right\rvert<\displaystyle\frac{\varepsilon}{2}$。

那么 $A\cup B\subseteq \left(\displaystyle\bigcup_{i=1}^{\infty}O_{A,i}\right)\cup \left(\displaystyle\bigcup_{i=1}^{\infty}O_{B,i}\right)$，且 $\displaystyle\sum_{i=1}^{\infty}\left\lvert O_{A,i} \right\rvert+\displaystyle\sum_{i=1}^{\infty}\left\lvert O_{B,i} \right\rvert<\varepsilon$。

所以 $A\cup B$ 的测度为零。

下面我们考虑一系列的零测集 $\left\{A_i\right\}_{i=1}^{\infty}$，对 $\forall\ \varepsilon>0$，对于每个 $A_{i}$，都存在相应的开区间集 $\left\{O_{A_i,j}\right\}_{j=1}^{\infty}$，满足零测的要求。

当然，这些零测集的并，包含于这些所有开区间的并。我们的目标是证明不仅两个，而是可数个可数开区间长度之和小于等于 $\varepsilon$，也就是 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}\left\lvert O_{A_{i},j} \right\rvert\leq \varepsilon$。（严格来说，这里开区间求和没有顺序，但稍后我们便会证明无序条件下求和结果依旧相等。）

在 2.8 节中我们详细地讨论了双重求和的一些问题，正好在这里复习一遍。

对 $\forall\ \varepsilon>0$ 与任意的零测集 $A_{i}$，都存在一列开区间集 $\left\{O_{A_i,j}\right\}_{j=1}^{\infty}$，使得 $A_i\subseteq \displaystyle\bigcup_{j=1}^{\infty} O_{A_i,j}$ 且 $\displaystyle\sum_{j=1}^{\infty}\left\lvert O_{A_i,j} \right\rvert=\displaystyle\frac{\varepsilon}{2^i}$。

这样，我们就能计算出 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}\left\lvert O_{A_{i},j} \right\rvert=\varepsilon$。接下来的问题是，这些开区间并不需要一个特定的顺序，所以我们需要证明这个级数的任意重排都收敛到相同的值。

这里就是 2.8 节双重级数问题的重述，在此可作简要复习用。

因为对 $\forall\ i,j\in \mathbb{N^+}$，都有 $\left\lvert O_{A_{i},j} \right\rvert > 0$，所以 $s_{nn}=\displaystyle\sum_{i=1}^{n}\displaystyle\sum_{j=1}^{n}\left\lvert O_{A_{i},j} \right\rvert$ 是单调有界的，自然能得出其收敛。

接下来的操作是分别通过 $m,n$ 来限制 $s_{nn}$ 的范围。首先，对 $\forall\ m<n$，均有

$$
\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}\left\lvert O_{A_{i},j} \right\rvert<s_{nn}<\varepsilon
$$

由极限保序性，$n\to \infty$ 我们能得到

$$
\displaystyle\sum_{i=1}^{m}\displaystyle\frac{\varepsilon}{2^{i}}=\varepsilon\left(1-\displaystyle\frac{1}{2^{m}}\right)\leq \displaystyle\lim_{n\to \infty} s_{nn}\leq \varepsilon
$$

再令 $m\to \infty$ 就能得到 $\displaystyle\lim_{n\to \infty}s_{nn}=\varepsilon$。

我们接下来通过把双重级数转化为普通级数，用普通级数上重排的性质来证明此结论。

事实上，$s_{nn}$ 可看作按如下方向相加的普通级数，即按左上到右下越来越大的正方形边缘相加：

$$
\begin{matrix}
    O_{A_{1},1} &&  O_{A_{1},2} && O_{A_{1},3} && \cdots & &O_{A_{1},n} \\
      && \uparrow && \uparrow&&&&\uparrow\\
    O_{A_{2},1} &\rightarrow& O_{A_{2},2} && O_{A_{2},3} && \cdots && O_{A_{2},n} \\
    &&&&\uparrow&&&&\uparrow\\
    O_{A_{3},1} &\rightarrow& O_{A_{3},2} &\rightarrow& O_{A_{3},3} && \cdots && O_{A_{3},n} \\
    \vdots && \vdots && \vdots && \ddots && \vdots \\
    &&&&&&&&\uparrow\\
    O_{A_{n},1} &\rightarrow& O_{A_{n},2} &\rightarrow& O_{A_{n},3} &\rightarrow& \cdots &\rightarrow& O_{A_{n},n}
\end{matrix}
$$

总共有 $n^2$ 项。将新级数记作 $\left\{b_{n}\right\}$，则 $\displaystyle\sum_{i=1}^{n^2}b_{i}=s_{nn}$，两边取极限便得 $\displaystyle\sum_{i=1}^{\infty}b_{i}=\varepsilon$。

因为它本身绝对收敛，所以它的任意重排也是收敛的。

这样，我们就证明了 $\displaystyle\sum_{\substack{i=1\\ j=1}}^{\infty}\left\lvert O_{A_{i},j} \right\rvert=\varepsilon$，这个值不因开区间的任意排列方式而改变。也就是说，可数个零测集的并集仍为零测集。

<mark>**注**：严谨的来说，开区间总长不一定能正好等于某个值，这里写为 $\displaystyle\frac{\varepsilon_{1}}{2^i}$，其中 $\varepsilon_{1}<\varepsilon$ 会更好。</mark>

<br/>

<hr>

### $\alpha$-连续性

设 $f$ 定义在 $\left\lbrack  {a,b}\right\rbrack$ 上，且令 $\alpha  > 0$。若存在 $\delta  > 0$，使得对于所有 $y,z \in  \left( {x - \delta ,x + \delta }\right)$，都有 $\left| {f\left( y\right)  - f\left( z\right) }\right|  < \alpha$，则称函数 $f$ 在 $x \in  \left\lbrack  {a,b}\right\rbrack$ 处是 $\alpha$-连续的。

设 $f$ 是定义在 $\left\lbrack  {a,b}\right\rbrack$ 上的有界函数。对于每个 $\alpha  > 0$，定义 ${D}_{\alpha }$ 为 $\left\lbrack  {a,b}\right\rbrack$ 中函数 $f$ 不满足 $\alpha$-连续性的点集；即，

$$
{D}_{\alpha } = \{ x \in  \left\lbrack  {a,b}\right\rbrack   : f \text{ 在 } x \text{ 处不 } \alpha \text{ 连续}.\} .
$$

$\alpha$-连续性的概念已在第 4.6 节中介绍。随后的几个练习也出现在本节中。

<br/>

!!! question "练习 7.6.6"

    
    如果 ${\alpha }_{1} < {\alpha }_{2}$，证明 ${D}_{{\alpha }_{2}} \subseteq  {D}_{{\alpha }_{1}}$。

对 $\forall\ x\in D_{\alpha_2}$，对 $\forall\ \delta>0$，$\exists\ y,z\in (x-\delta,x+\delta)$，使得

$$
\left\lvert f(y)-f(z) \right\rvert\geq \alpha_2\geq \alpha_1
$$

所以 $x\in D_{\alpha_1}$。这就得到了 ${D}_{{\alpha }_{2}} \subseteq  {D}_{{\alpha }_{1}}$。

<br/>

<hr>

现在，设

$$
D = \{ x \in  \left\lbrack  {a,b}\right\rbrack   : f \text{ 在 } x \text{ 处不连续}\}
$$

<br/>

!!! question "练习 7.6.7"

    
    (a) 设 $\alpha  > 0$ 给定。证明如果 $f$ 在 $x \in  \left\lbrack  {a,b}\right\rbrack$ 处连续，则它在 $x$ 处也是 $\alpha$-连续的。解释如何由此得出 ${D}_{\alpha } \subseteq  D$。
    
    (b) 证明如果 $f$ 在 $x$ 处不连续，则 $f$ 对于某个 $\alpha  > 0$ 不是 $\alpha$-连续的。现在，解释为什么这保证了
    
    $$
    D = \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{D}_{1/n}
    $$

(a) 若 $f$ 在 $x$ 处连续，则对 $\forall\ \varepsilon>0$，取 $\varepsilon<\alpha$，$\exists\ \delta>0$，对 $\forall\ y\in (x-\delta,x+\delta)$，有 $\left\lvert f(x)-f(y) \right\rvert<\displaystyle\frac{\varepsilon}{2}<\displaystyle\frac{\alpha}{2}$。

所以对 $\forall\ y,z\in (x-\delta,x+\delta)$，有：

$$
\begin{aligned}
    \left\lvert f(y)-f(z) \right\rvert&=\bigl\lvert \left(f(y)-f(x)\right)-\left(f(z)-f(x)\right) \bigr\rvert\\
    &\leq \left\lvert f(x)-f(y) \right\rvert+\left\lvert f(x)-f(z) \right\rvert\\
    &<\displaystyle\frac{\alpha}{2}+\displaystyle\frac{\alpha}{2}<\alpha
\end{aligned}
$$

所以 $f$ 在 $x$ 处也是 $\alpha$-连续的。反之，如果 $f$ 在 $x$ 处不 $\alpha$ 连续，则 $f$ 在 $x$ 处也不连续，所以 ${D}_{\alpha } \subseteq  D$。

(b) 若 $f$ 在 $x$ 处不连续，则 $\exists\ \varepsilon_0>0$，对 $\forall\ \delta>0$，$\exists\ y\in (x-\delta,x+\delta)$，使得 $\left\lvert f(x)-f(y) \right\rvert\geq \varepsilon_{0}$。

令上面的 $\varepsilon_{0}=\alpha$，这样就能得到 $f$ 对于这个 $\alpha$ 不是 $\alpha$-连续的结论。

也就是说，对 $\forall\ x\in D$，$\exists\ \alpha>0$，使得 $x\in D_{\alpha}$。

又因为 $\exists\ n\in \mathbb{N^+}$，使得 $\frac{1}{n}<\alpha$，所以 $D_{\alpha}\subseteq D_{\frac{1}{n}}$ $\Rightarrow$ $x\in D_{1/n}$。

这就说明，对 $\forall\ x\in D$，$\exists\ n\in \mathbb{N^+}$ 使得 $x\in D_{\frac{1}{n}}$，所以 $x\in \displaystyle\bigcup_{n=1}^{\infty}D_{\frac{1}{n}}$ 一定成立，即 $D\subseteq \displaystyle\bigcup_{n=1}^{\infty}D_{\frac{1}{n}}$。

又因为对 $\forall\ \alpha>0$，$D_{\alpha}\subseteq D$，所以 $\displaystyle\bigcup_{n=1}^{\infty}D_{\frac{1}{n}}\subseteq D$。

综合上面两式，即得 $D=\displaystyle\bigcup_{n=1}^{\infty}D_{\frac{1}{n}}$。

<br/>

<a id="7.6.8"></a>

!!! question "练习 7.6.8"

    
    证明对于固定的 $\alpha  > 0$，集合 ${D}_{\alpha }$ 是闭的。

我们证明它的补集，即全体满足 $\alpha$-连续性的点组成的集合是开集。

设 $x$ 是一个满足 $\alpha$-连续性的点，即存在 $\delta>0$，使得对 $\forall\ y,z\in (x-\delta,x+\delta)$，有 $\left\lvert f(y)-f(z) \right\rvert<\alpha$。

则对 $\forall\ x_0\in \left(x-\displaystyle\frac{\delta}{2},x+\displaystyle\frac{\delta}{2}\right)$，都有对 $\forall\ y,z\in \left(x_0-\displaystyle\frac{\delta}{2},x_0+\frac{\delta}{2}\right)$，$\left\lvert f(y)-f(z) \right\rvert<\alpha$。

所以 $\forall\ x_0\in \left(x-\displaystyle\frac{\delta}{2},x+\displaystyle\frac{\delta}{2}\right)$ 都满足 $\alpha$-连续性，即 $\left(x-\displaystyle\frac{\delta}{2},x+\displaystyle\frac{\delta}{2}\right)\subseteq \left(D_{\alpha}\right)^c$。

所以 $\left(D_{\alpha}\right)^c$ 是开集，即 $D_{\alpha}$ 是闭集。

<br/>

<hr>

正如连续性一样，$\alpha$-连续性是逐点定义的；也正如连续性一样，一致性将扮演重要角色。

对于固定的 $\alpha > 0$，函数 $f : A \to R$ 在 $A$ 上是一致 $\alpha$-连续的，如果存在 $\delta > 0$，使得只要 $x$ 和 $y$ 是 $A$ 中满足 $|x - y| < \delta$ 的点，就有 $|f(x) - f(y)| < \alpha$。通过模仿定理 4.4.7 的证明，可以完全直接地证明：如果 $f$ 在某个紧集 $K$ 的每一点处都是 $\alpha$-连续的，那么 $f$ 在 $K$ 上是一致 $\alpha$-连续的。

### 紧性再探

实数集的紧性可以用三种等价方式描述。以下定理出现在 3.3 节末尾。

**定理 7.6.4.** 设 $K \subseteq \mathbb{R}$。以下三个陈述全部等价，即如果其中任何一个为真，那么另外两个也为真。

(i) $K$ 中包含的每个序列都有一个收敛子序列，且该子序列收敛到 $K$ 中的一个极限。

(ii) $K$ 是闭集且有界。

(iii) 给定一列覆盖 $K$ 的开区间 $\{G_{\lambda}:\lambda \in \Lambda \}$（即 $K\subseteq \bigcup_{\lambda \in \Lambda}G_{\lambda}$），原集合存在一个有限子集 $\{G_{\lambda_1},G_{\lambda_2},G_{\lambda_3},\ldots ,G_{\lambda_N}\}$ 也覆盖 $K$。

(i) 与 (ii) 的等价性已在全书核心材料中使用。刻画 (iii) 不那么核心，但对即将到来的论证至关重要。如果以开覆盖方式给出的紧性刻画不熟悉，请花点时间复习 3.3 节后半部分等价性的证明。

### Lebesgue 定理

我们现在准备根据连续性完全刻画 Riemann 可积函数的集合。

**定理 7.6.5（Lebesgue 定理）。** 设 $f$ 是定义在区间 $[a, b]$ 上的有界函数。那么，$f$ 是 Riemann 可积的当且仅当 $f$ 不连续的点集具有零测度。

证明：设 $M > 0$ 满足 $|f(x)| \leq M$ 对所有 $x \in [a, b]$ 成立，并设 $D$ 和 $D_{\alpha}$ 如前面所定义。我们首先假设 $D$ 具有零测度，并证明我们的函数可积。

$(\Leftarrow)$ 设 $\varepsilon >0$，并令

$$
\alpha = \frac {\varepsilon}{2 (b - a)}.
$$

<br/>

!!! question "练习 7.6.9"

    
    证明存在一个由互不相交的开区间 $\{G_{1}, G_{2}, \ldots, G_{N}\}$ 组成的有限集合，其并集包含 $D_{\alpha}$，并且满足
    
    $$
    \sum_ {n = 1} ^ {N} | G _ {n} | <   \frac {\varepsilon}{4 M}.
    $$

由零测集的性质，存在可数个开区间的并集覆盖 $D$，且这些开区间的长度之和小于 $\displaystyle\frac{\varepsilon}{4M}$。因为 $D_{\alpha}\subseteq D$，所以上述开区间并集同样覆盖 $D_{\alpha}$。

由 [7.6.8](#7.6.8)，因为 $D_{\alpha}$ 是有界闭集，所以它是紧集，由有限覆盖定理，在这些开区间中，可以选出一列开区间 $\left\{F_{1},F_{2},\ldots,F_{K}\right\}$ 组成的有限集合，并集包含 $D_{\alpha}$，并且

$$
\displaystyle\sum_{n=1}^{K}\left\lvert F_{n} \right\rvert<\displaystyle\frac{\varepsilon}{4M}
$$

事实上，若有两个开区间 $F_{i},F_{j}$ 相交（多个也同理），则它们的并集依旧是一个开区间，且合并后的长度小于等于原来两个区间的长度和，即总长不会增加。所以我们将所有相交的开区间各自合并，直到剩下的开区间 $\left\{G_{1},G_{2},\ldots,G_{N}\right\}$ 互不相交。此时的 $G$ 即为所求。

<br/>

!!! question "练习 7.6.10"

    
    设 $K$ 为区间 $[a,b]$ 在开区间 $G_{n}$ 全部被移除后剩余的部分；即 $K = [a,b]\backslash\bigcup_{n=1}^{N}G_{n}$。论证 $f$ 在 $K$ 上是一致 $\alpha$-连续的。

因为 $\displaystyle\bigcup_{n=1}^{N}G_{n}$ 是开集，所以 $K=[a,b]\setminus\displaystyle\bigcup_{n=1}^{N}G_{n}$ 是闭集。又因为其有界，故 $K$ 为紧集。

首先，对 $\forall\ x\in K$，$x\notin \displaystyle\bigcup_{n=1}^{N}G_{n}$ $\Rightarrow$ $x\notin D_{\alpha}$ $\Rightarrow$ $f$ 在 $x$ 处是 $\alpha$-连续的。

假设 $f$ 在 $K$ 上不是一致 $\alpha$-连续的，则存在两个序列 $\left\{x_n\right\},\left\{y_n\right\}$，使得 $\displaystyle\lim_{n\to \infty}\left(x_n-y_n\right)=0$ 且 $\left\lvert f(x_n)-f(y_n) \right\rvert\geq \alpha$。

由 Bolzano-Weierstrass 定理，$\left\{x_{n}\right\}$ 存在收敛子列 $\left\{x_{n_{k}}\right\}$，设 $\displaystyle\lim_{k\to \infty}x_{n_{k}}=x_0$，因为 $K$ 是紧集，所以 $x_{0}\in K$。

又因为 $\displaystyle\lim_{k\to \infty}\left(x_{n_{k}}-y_{n_{k}}\right)=0$，所以 $\displaystyle\lim_{k\to \infty}y_{n_{k}}=x_0$。

现在，因为 $x_{0}\in K$，所以 $\exists\ \delta>0$，使得对 $\forall\ y,z\in (x_{0}-\delta,x_0+\delta)$，有 $\left\lvert f(y)-f(z) \right\rvert<\alpha$。

但是又因为 $\displaystyle\lim_{k\to \infty}x_{n_{k}}=\displaystyle\lim_{k\to \infty}y_{n_{k}}=x_0$，所以对上述的 $\delta>0$，$\exists\ K_1,K_2\in \mathbb{N}$，使得当 $k>K_1$ 且 $k>K_2$ 时，$x_{n_{k}}, y_{n_{k}}\in (x_0-\delta, x_0+\delta)$，这样就有 $\left\lvert f(x_{n_{k}})-f(y_{n_{k}}) \right\rvert<\alpha$，这与 $\left\lvert f(x_n)-f(y_n) \right\rvert\geq \alpha$ 矛盾。

所以 $f$ 在 $K$ 上是一致 $\alpha$-连续的。

<br/>

!!! question "练习 7.6.11"

    
    通过解释如何构造 $[a,b]$ 的一个分割 $P_{\varepsilon}$，使得 $U(f,P_{\varepsilon})-L(f,P_{\varepsilon})\leq\varepsilon$，来完成这个方向的证明。将和式
    
    $$
    U (f, P _ {\varepsilon}) - L (f, P _ {\varepsilon}) = \sum_ {k = 1} ^ {n} (M _ {k} - m _ {k}) \Delta x _ {k}
    $$
    
    分成两部分会有所帮助——一部分取在包含 $D_{\alpha}$ 中点的子区间上，另一部分取在不包含 $D_{\alpha}$ 中点的子区间上。

这里我们终于把零测集转化成了有限个开区间的并集了（当然，要用上不连续性）。这样，我们完全可以仿照 [7.3.6](#7.3.6) 的手段来得出结论。

构造这样的分割 $P$，其中包含所有开区间 $G_n$ 在 $[a,b]$ 上的端点。记那些正好为开区间闭包 与 $[a,b]$ 交集的闭区间为 $A_{1},A_{2},\ldots,A_{p}$，其余闭区间为 $B_{1},B_{2},\ldots,B_{q}$。那么我们有：

首先控制了 $\displaystyle\sum_{i=1}^{p}\left\lvert A_{i} \right\rvert<\displaystyle\sum_{n=1}^{N}\left\lvert G_{n} \right\rvert<\displaystyle\frac{\varepsilon}{4M}$；

其次用 $\alpha$-连续性控制了 $\displaystyle\sup_{x\in B_{j}}{f(x)}-\displaystyle\inf_{x\in B_{j}}{f(x)}\leq \alpha$。

现在，令 $\alpha=\displaystyle\frac{\varepsilon}{2(b-a)}$，则：

$$
\begin{aligned}
    U\left(f,P\right)-L\left(f,P\right)&=\displaystyle\sum_{I\in P}^{}\left(\displaystyle\sup_{x\in I}{f(x)}-\displaystyle\inf_{x\in I}{f(x)}\right)\cdot \left\lvert I \right\rvert\\
    &=\displaystyle\sum_{i=1}^{p}\left(\displaystyle\sup_{x\in A_{i}}{f(x)}-\displaystyle\inf_{x\in A_{i}}{f(x)}\right)\cdot \left\lvert A_{i} \right\rvert+\displaystyle\sum_{j=1}^{q}\left(\displaystyle\sup_{x\in B_{j}}{f(x)}-\displaystyle\inf_{x\in B_{j}}{f(x)}\right)\cdot \left\lvert B_{j} \right\rvert\\
    &\leq 2M\displaystyle\sum_{i=1}^{p}\left\lvert A_{i} \right\rvert+\alpha\displaystyle\sum_{j=1}^{q}\left\lvert B_{j} \right\rvert\\
    &<2M\cdot \displaystyle\frac{\varepsilon}{4M}+\displaystyle\frac{\varepsilon}{2(b-a)}\cdot (b-a)\\
    &=\varepsilon
\end{aligned}
$$

这就证明了 $f$ 在 $[a,b]$ 上可积。

<br/>

<hr>

$(\Rightarrow)$ 对于另一个方向，假设 $f$ 是 Riemann 可积的。我们必须论证 $f$ 的不连续点集 $D$ 具有零测度。

令 $\varepsilon > 0$ 任意，并固定 $\alpha > 0$。因为 $f$ 是 Riemann 可积的，所以存在 $[a, b]$ 的一个分割 $P_{\varepsilon}$，使得 $U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) < \alpha \varepsilon$。

<br/>

!!! question "练习 7.6.12"

    
    (a) 证明 $D_{\alpha}$ 具有零测度。指出可以为 $D_{\alpha}$ 选择一个由有限个开区间组成的覆盖。
    
    (b) 展示这如何推出 $D$ 具有零测度。

(a) 首先，对上述的分割 $P_{\varepsilon}$，记那些包括 $D_{\alpha}$ 中点，$\color{red}{\text{且该点非端点的}}$闭区间为 $I_{1},I_{2},\ldots,I_{k}$，则 $D_{\alpha}\subseteq \displaystyle\bigcup_{i=1}^{k}I_{i}$。

然后，每个闭区间上的上下和之差都非负，所以：

$$
\displaystyle\sum_{i=1}^{k}\left(\displaystyle\sup_{x\in I_{i}}{f(x)}-\displaystyle\inf_{x\in I_{i}}{f(x)}\right)\left\lvert I_{i} \right\rvert\leq U\left(f,P_{\varepsilon}\right)-L\left(f,P_{\varepsilon}\right)<\alpha \varepsilon
$$

因为对任意闭区间 $I_{i}$，内部都存在 $D_{\alpha}$ 上的点，由这些点的 $\alpha$-不连续性，$\displaystyle\sup_{x\in I_{i}}{f(x)}-\displaystyle\inf_{x\in I_{i}}{f(x)}\geq \alpha$，所以：

$$
\alpha\displaystyle\sum_{i=1}^{k}\left\lvert I_{i} \right\rvert\leq \displaystyle\sum_{i=1}^{k}\left(\displaystyle\sup_{x\in I_{i}}{f(x)}-\displaystyle\inf_{x\in I_{i}}{f(x)}\right)\left\lvert I_{i} \right\rvert<\alpha \varepsilon
$$

即 $\displaystyle\sum_{i=1}^{k}\left\lvert I_{i} \right\rvert<\varepsilon$。

最后，对每个闭区间 $I_{i}$，取一个包含它的，长度多 $t\varepsilon$ 的开区间 $J_{i}$（这里的 $t$ 可以取任意小的）。

取 $t=\displaystyle\frac{1}{k}$，则 $\displaystyle\sum_{i=1}^{k}\left\lvert J_{i} \right\rvert<2\varepsilon$，且 $D_{\alpha}\subseteq \displaystyle\bigcup_{i=1}^{k}J_{i}$。

所以 $D_{\alpha}$ 具有零测度。

$\color{red}{\text{事实上若}}$ $\color{red}{x\in D_{\alpha}}$ $\color{red}{\text{在某个闭区间的端点上，则有可能在左右单边是不满足}}$ $\color{red}{\alpha}\color{red}{\text{-不连续性的。}}$ 不过这些点是有限的，而零测集加上有限个点仍为零测集。所以在上述的证得的零测集上添加这有限个点，组成真正的 $D_{\alpha}$，则 $D_{\alpha}$ 为零测度。

(b) 由零测集的性质，可数个零测集的并仍为零测集。

由上面结论，对 $\forall\ \alpha>0$，$D_{\alpha}$ 均为零测集，所以 $D=\displaystyle\bigcup_{n=1}^{\infty}D_{1/n}$ 也是零测集。

<br/>

<hr>

我们在本节剩余部分的主要议程，是利用 Lebesgue 定理来寻找一个不可积的导数，但这个优雅的结果还有许多其他应用。

<br/>

!!! question "练习 7.6.13"

    
    (a) 证明如果 $f$ 和 $g$ 在 $[a, b]$ 上可积，那么乘积 $fg$ 也可积。（这个结果虽然不需要这一节的内容也能证明，但是使用 Lebesgue 定理的证明更为简洁。）
    
    (b) 证明如果 $g$ 在 $[a, b]$ 上可积，且 $f$ 在 $g$ 的值域上连续，那么复合函数 $f \circ g$ 在 $[a, b]$ 上可积。

(a) 由 Lebesgue 定理，$f$ 和 $g$ 的不连续点集 $D_f$ 和 $D_g$ 都具有零测度。

设 $D_{fg}$ 为 $fg$ 的不连续点集。因为若 $x_0$ 在 $f,g$ 都连续，它就在 $fg$ 上连续，所以 $D_{fg}$ 中的点只可能来自 $f,g$ 中本来就不连续的那些点。所以：

$$
D_{fg}\subseteq D_{f}\cup D_{g}
$$

而 $D_{f}\cup D_{g}$ 是零测的。由零测集的定义，能覆盖它的开区间肯定能覆盖它的子集，所以它的任意子集都是零测集，即 $D_{fg}$ 是零测集。

所以 $fg$ 是可积的。

(b) 由 Lebesgue 定理，$g$ 的不连续点集 $D_g$ 具有零测度。

设 $D_{f\circ g}$ 为 $f \circ g$ 的不连续点集。跟上一问同理，复合函数仍然有 $x_0$ 在 $g$ 上连续，$g(x_0)$ 在 $f$ 上连续 $\Rightarrow$ $x_0$ 在 $f \circ g$ 连续的结论。因为 $f$ 在 $g$ 的值域上连续，所以不连续点只可能来自 $g$ 的不连续点。所以同样有 $D_{f\circ g}\subseteq D_g$，$D_{f\circ g}$ 是零测集的结论。

所以 $f\circ g$ 在 $[a,b]$ 上可积。

<br/>

<hr>

<a id="7.6.13"></a>

如果我们改为假设 $f$ 可积且 $g$ 连续，那么实际上并不能推出复合函数 $f \circ g$ 可积。然而，构造一个反例还需要一些额外材料。

### 一个不可积的导数

到目前为止，我们关于不可积函数的唯一例子是 Dirichlet 的无处连续函数。我们以一个具有特殊意义的另一个例子来结束本节。微积分基本定理的内容是积分与微分是彼此互逆的过程。如果函数 $f$ 在 $[a, b]$ 上可微，那么微积分基本定理的第 (i) 部分告诉我们

$$
\int_ {a} ^ {b} f ^ {\prime} = f (b) - f (a),\tag{3}
$$

只要 $f'$ 可积。但是，$f'$ 难道不是仅凭它是导数就应当可积吗？盯着方程 (3) 看久了，会产生一种奇怪的副作用：它开始让人觉得每个导数都应该是可积的，因为我们有一个明显的候选值，知道积分值应当是什么。唉，至少对于 Riemann 积分而言，现实未能达到我们的期望。接下来构造一个可微函数 $f$，使得方程 (3) 不成立，因为 $\int_{a}^{b} f'$ 不存在。

我们将再次关注 Cantor 集

$$
C = \bigcap_ {n = 0} ^ {\infty} C _ {n},
$$

它在 3.1 节中定义。作为初始步骤，让我们构造一个在 $[0, 1]$ 上可微的函数 $f(x)$，其导数 $f'(x)$ 在 $C$ 的每一点处都不连续。这个构造的关键成分是函数

$$
g (x) =\begin{cases} x ^ {2} \sin (1 / x) & \text { if } x > 0 \\ 0 & \text { if } x \leq 0\end{cases}
$$

<br/>

<a id="7.6.14"></a>

!!! question "练习 7.6.14"

    
    (a) 求 $g'(0)$。
    
    (b) 使用标准求导法则计算 $x \neq 0$ 时的 $g'(x)$。
    
    (c) 解释为什么对于每个 $\delta > 0$，当 $x$ 取遍集合 $(- \delta, \delta)$ 时，$g'(x)$ 会取到 $1$ 与 $-1$ 之间的每一个值。由此推出 $g'$ 在 $x = 0$ 处不连续。

(a) $g'(0)=\displaystyle\lim_{x\to 0}\displaystyle\frac{g(x)-g(0)}{x-0}=\displaystyle\lim_{x\to 0}\displaystyle\frac{x^2\sin\displaystyle\frac{1}{x}}{x}=\displaystyle\lim_{x\to 0}x\sin\displaystyle\frac{1}{x}=0$。

(b) $g'(x)=2x\sin\displaystyle\frac{1}{x}-\cos\displaystyle\frac{1}{x}$。

(c) 我们看看 $g'$ 在 $0$ 邻域的上下界如何。

令 $x_{n}=\displaystyle\frac{1}{2n\pi}$，$y_{n}=\displaystyle\frac{1}{\left(2n+1\right)\pi}$，则总有 $g'(x_{n})=-1$，$g'(y_{n})=1$。

因为 $\displaystyle\lim_{n\to \infty}x_n=\displaystyle\lim_{n\to \infty}y_n=0$，且 $x_n>y_n>0$，所以对 $\forall\ \delta>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$0<y_n<x_n<\delta$。

又因为 $g'(x)$ 在 $[y_n,x_n]$ 上连续，所以 $g'$ 能取到 $[-1,1]$ 间的所有值。

因为 $\displaystyle\lim_{n\to \infty}g'(x_{n})=-1$，$\displaystyle\lim_{n\to \infty}g'(y_n)=1$，所以 $g'$ 在 $0$ 处不连续。

<br/>

<hr>

现在，我们希望把 $g$ 在零附近的行为搬运到构成 Cantor 集定义中所用集合 $C_{n}$ 的每个闭区间的端点处。公式虽然有些笨拙，但基本想法很直接。令

$$
f _ {0} (x) = 0 \quad \text{ on } \quad C _ {0} = [ 0, 1 ].
$$

要在 $[0, 1]$ 上定义 $f_{1}$，首先令

$$
f _ {1} (x) = 0 \quad \text{   for   all   } \quad x \in C _ {1} = \left[ 0, \frac {1}{3} \right] \cup \left[ \frac {2}{3}, 1 \right].
$$

在剩余的中间三分之一开区间中，放入 $g$ 的平移“副本”，使其向两个端点振荡（图 7.3）。用公式表示，我们有

$$
f _ {1} (x) = \begin{cases} 0 & \text { if } x \in [ 0, 1 / 3 ] \\ g (x - 1 / 3) & \text { if } x \text { is just to the right of } 1 / 3 \\ g (- x + 2 / 3) & \text { if } x \text { is just to the left of } 2 / 3 \\ 0 & \text { if } x \in [ 2 / 3, 1 ]. \end{cases}
$$

最后，我们将 $f_{1}$ 的两个振荡部分拼接在一起，使得 $f_{1}$ 可微，并且满足

$$
\left| f _ {1} (x) \right| \leq (x - 1 / 3) ^ {2} \quad \text { and } \quad \left| f _ {1} (x) \right| \leq (- x + 2 / 3) ^ {2}.
$$

这种拼接并非什么壮举，我们将跳过细节，以便把注意力集中在两个端点 $1/3$ 和 $2/3$ 上。这些正是 $f_{1}^{\prime}(x)$ 不连续的点。

![](https://calculus1437-github-io.pages.dev/images/9bd78930c0a9d4dd4bfad6b0f7256c7cf8936c30c3664edbe8e7544db041685c.jpg)

图 7.3：$f_{1}(x)$ 的初步草图。

为了定义 $f_{2}(x)$，我们从 $f_{1}(x)$ 开始，并像之前一样施展同样的技巧，这次是在两个开区间 $(1/9, 2/9)$ 和 $(7/9, 8/9)$ 中进行。结果（图 7.4）是一个可微函数，它在 $C_{2}$ 上为零，并且其导数在集合

$$
\left\{\frac {1}{9}, \frac {2}{9}, \frac {1}{3}, \frac {2}{3}, \frac {7}{9}, \frac {8}{9} \right\}
$$

上不连续。

继续这样做，就得到一列定义在 $[0, 1]$ 上的函数 $f_0, f_1, f_2, \ldots$。

![](https://calculus1437-github-io.pages.dev/images/4e29c17f68aac8e37899a0fe92bdbe924f05048c13f6aa61cb9025ef93ea6506.jpg)

图 7.4：$f_{2}(x)$ 的图像。

<br/>

!!! question "练习 7.6.15"

    
    (a) 如果 $c \in C$，那么 $\lim_{n \to \infty} f_n(c)$ 是什么？
    
    (b) 为什么对 $x\notin C$，$\lim_{n\to\infty}f_n(x)$ 存在？

(a) 事实上，每一次改变都在 $C_n$ 之外进行，即对 $\forall\ n\in \mathbb{N^+}$，$f_{n}(c)=0$，所以 $\displaystyle\lim_{n\to \infty}f_n(c)=0$。

(b) 若对 $\forall\ n\in \mathbb{N^+}$，$x\in C_{n}$，则 $x\in C$。反之，若 $x\notin C$，则 $\exists\ N\in \mathbb{N^+}$，使得 $x\in C_{N}$ 但对 $\forall\ n>N$，$x\notin C_{n}$。

此时我们知道，函数会对刚刚被移除的开区间做且仅做一次操作，所以在这之后 $f_{n}(x)$ 将一直保持定值，所以 $\displaystyle\lim_{n\to\infty}f_n(x)$ 存在。

<br/>

<hr>

现在，令

$$
f (x) = \lim _ {n \to \infty} f _ {n} (x).
$$

<br/>

!!! question "练习 7.6.16"

    
    (a) 解释为什么对所有 $x \notin C$，$f'(x)$ 都存在。
    
    (b) 如果 $c \in C$，论证对所有 $x \in [0,1]$，都有 $|f(x)| \leq (x - c)^2$。说明这如何推出 $f'(c) = 0$。
    
    (c) 给出一个仔细的论证，说明为什么 $f'(x)$ 在 $C$ 上不连续。记住，$C$ 除了包含构成 $C_1, C_2, C_3, \ldots$ 的区间端点之外，还包含许多其他点。

(a) 对 $\forall\ x\notin C$，$x$ 一定存在于某个在 $C$ 之外的开区间中，所以存在一个开区间 $I$，使得 $I\cap C=\varnothing$ 且 $x\in I$。

因为在某个 $f_{n}$ 之后，其在 $I$ 上的取值不再改变，所以 $\exists\ N\in \mathbb{N^+}$，使得 $f_{N}(x)=f(x)$ 在 $I$ 上恒成立。因为 $f_{N}(x)$ 本身就在 $I$ 上可微，所以 $f_{N}'(x)=f'(x)$。

所以 $f'(x)$ 存在。

(b) 对于 $\forall\ x\in [0,1]$，如果 $x\in [0,1]$，则 $f(x)=0\leq \left(x-c\right)^2$ 成立。

如果 $x\notin [0,1]$，则 $x$ 必定属于某个 $C_{n}$ 分割后多出的开区间。依照定义，在此区间上的 $f$ 要满足 $\left\lvert f(x) \right\rvert\leq \left(x-a\right)^2$，其中 $a$ 是开区间的任意一个端点。

因为 $c\in C$，所以 $c$ 必定在这个开区间的外侧，也就是 $\left\lvert x-c \right\rvert\geq \left\lvert x-a \right\rvert$，所以 $\left\lvert f(x) \right\rvert\leq \left(x-a\right)^2\leq \left(x-c\right)^2$。

接下来计算导数。首先，对 $\forall\ c\in C$，$f(c)=0$。然后，对 $\forall\ \varepsilon>0$，$\exists\ 0<\delta<\varepsilon$，使得对 $\forall\ x\in (c-\delta,c+\delta)$，有：

$$
\left\lvert \displaystyle\frac{f(x)-f(c)}{x-c} \right\rvert\leq \displaystyle\frac{\left(x-c\right)^2}{\left\lvert x-c \right\rvert}=\left\lvert x-c \right\rvert<\delta<\varepsilon
$$

所以 $f'(c)=0$。

(c) 如果 $x_{0}$ 是某个 $C_{n}$ 所属闭区间上的端点，那它当然也属于 $C$。但是在不属于 $C$ 的另一头，我们拼接了 $g$ 在 $0$ 处的副本。因此，在 $x_{0}$ 的任意邻域上，$f'(x)$ 将能取得 $[-1,1]$ 上的任意值，这导致了其在 $x_{0}$ 处不连续。

对于 $C$ 上的其他点 $c$，我们知道 $f'(c)=0$。现在要考虑的是如何将端点的性质诱导到它上面。
注意在每个 $C_{n}$ 上，$c$ 都被限制于某个越来越小的闭区间的内（这个长度是 $1/3^n$），这样，总能找到一列闭区间端点 $\left\{x_{n}\right\}$ 使得 $x_{n}\to c$。所以 $c$ 的任意邻域上存在某个 $x_{n}$，而 $x_{n}$ 的任意邻域处其导数都在 $[-1,1]$ 上都能取到，这样我们就能把这个邻域设在 $c$ 邻域内部，使得 $c$ 的邻域处导数也在 $[-1,1]$ 上都能取到，这样 $f'(x)$ 在 $c$ 处就不连续了。

数学语言：对 $\forall\ \delta>0$，$\exists\ N\in \mathbb{N^+}$，使得 $x_{N}\in (c-\delta,c+\delta)$。

取 $\delta_{1}<\min\left\{x_{N}-\left(c-\delta\right),\left(c+\delta\right)-x_{N}\right\}$，则对 $\forall\ x\in (x_{N}-\delta_{1},x_{N}+\delta_{1})$，$x\in (c-\delta,c+\delta)$。

又因为对 $\forall\ t\in [-1,1]$，$\exists\ x_1\in (x_{N}-\delta_{1},x_{N}+\delta_{1})$，使得 $f'(x_{1})=t$，所以 $f'(x)$ 在 $c$ 的邻域上能取到 $[-1,1]$ 间的任意值。由 [7.6.14](#7.6.14)， $f'(x)$ 在 $c$ 处不连续。

综上，$f'$ 在 $C$ 上的每一点都不连续。

<br/>

<hr>

让我们盘点一下当前情况。我们的目标是构造一个不可积的导数。我们的函数 $f(x)$ 可微，并且 $f'$ 在 $C$ 上不连续，不过我们还没有完全完成。

<br/>

!!! question "练习 7.6.17"

    
    为什么 $f'(x)$ 在 $[0,1]$ 上是 Riemann 可积的？

因为 $f'(x)$ 的不连续点集，即 $C$，是一个零测集，由 Lebesgue 定理可知 $f'$ 在 $[0,1]$ 上仍 Riemann 可积。

<br/>

<hr>

Cantor 集具有零测度的原因是，在每一阶段，从 $C_{n}$ 中移除 $2^{n-1}$ 个长度为 $1/3^n$ 的开区间。所得和式

$$
\sum_ {n = 1} ^ {\infty} 2 ^ {n - 1} \left(\frac {1}{3 ^ {n}}\right)
$$

收敛到一，这意味着逼近集合 $C_1, C_2, C_3, \ldots$ 的总长度趋于零。现在，与其在每一阶段移除长度为 $1/3^n$ 的开区间，让我们看看如果移除长度为 $1/3^{n+1}$ 的区间会发生什么。

<br/>

!!! question "练习 7.6.18"

    
    证明在这些情况下，构成每个 $C_{n}$ 的区间长度之和不再随着 $n \to \infty$ 趋于零。这个极限是什么？

简单替换原求和式中的区间长度，我们得到：

$$
\displaystyle\sum_{n=1}^{\infty}2^{n-1}\left(\displaystyle\frac{1}{3^{n+1}}\right)=\displaystyle\frac{1}{3}\displaystyle\sum_{n=1}^{\infty}2^{n-1}\left(\displaystyle\frac{1}{3^{n}}\right)=\displaystyle\frac{1}{3}
$$

我们需要检查这个新的集合，记作 $C'$，生成函数记作 $g(x)$，能不能用上述方法同样推导。

首先，由于 $C'$ 的操作仍然是通过不停删去区间得到，所以 $\forall\ x\notin C$ 所在的某个开区间在某个 $g_{N}$ 之后依旧会保持定值，$g_{N}'(x)=g'(x)$。

然后，仍然是对每个 $C_{n}'$ 分离出来的开区间作端点上的限值操作，并且 $c\in C$ 仍然都在开区间之外，所以这里可以同样推出 $g'(c)=0$。

接着，$g'$ 在 $C$ 的端点当然不连续。要想使得中间的 $c\in C$ 也不连续，我们着重关注 $C'$ 的闭区间端点能不能同样逼近 $c$。

因为 $C_{n}'$ 的每个闭区间长度将会变为 $\displaystyle\frac{\displaystyle\sum_{k=1}^{n}\displaystyle\frac{2^{k-1}}{3^{k+1}}}{2^{n}}=\displaystyle\frac{1}{3}\left(\displaystyle\frac{1}{2^{n-1}}+\displaystyle\frac{1}{3^{n}}\right)$，这个值是会趋于零的，所以 $c$ 一定会在一些越来越小，长度趋近于零的闭区间内，这样就可以构造相应的 $\left\{x_{n}\right\}\to c$，同样证得 $g'(x)$ 在整个 $C'$ 上不连续。

最后，$C'$ 的总长度刚刚算过了，趋近于 $\displaystyle\frac{2}{3}$，这说明 $C'$ 不能被长度比自己小的开区间覆盖，当然不是零测的了。所以，我们很高兴地宣布，$g$ 是一个处处可导，但是 $g'$ 不可积的函数！

<br/>

<hr>

![](https://calculus1437-github-io.pages.dev/images/cc4006d85bb841018a120125cf1641c7486645f925907afe213f9939513d00e5.jpg)

图 7.5：一个具有不可积导数的可微函数。

如果我们再次取交集 $\bigcap_{n=0}^{\infty} C_n$，结果是一个 Cantor 型集合，具有相同的拓扑性质——它是闭的、紧的、完美的，并且不包含任何区间。但上一个练习的一个推论是，它不再具有零测度。这正是我们定义所需函数所需要的东西。通过在这个具有严格正测度的新 Cantor 型集合上重复前述 $f(x)$ 的构造，我们得到一个可微函数，其导数有太多的间断点（图 7.5）。根据 Lebesgue 定理，这个导数不能使用 Riemann 积分进行积分。

<br/>

!!! question "练习 7.6.19"

    
    作为全书的谢幕，也跟 [7.6.13](#7.6.13) 末尾复合函数可积性的讨论遥相呼应，我们来构造一个 $f$ 可积，$g$ 连续，但 $f \circ g$ 不可积的函数。
    
    (a) 设 $F\in \mathbb{R}$ 是一个非空闭集，并定义 $g(x)=\displaystyle\inf_{a\in F}{\left\lvert x-a \right\rvert}$。证明 $g$ 在 $\mathbb{R}$ 上连续，且对 $\forall\ x\notin F$，$g(x)\neq 0$。
    
    (b) 构造一个可积函数 $f$ 和一个连续函数 $g$，使得 $f\circ g$ 不可积。

(a) 先证后面一个结论：若 $g(x)=0$，则必定存在一列 $\left\{a_{n}\right\}\subseteq F$，使得 $a_{n}\to x$，但那样 $x\in F$。所以 $x\notin F$ 时，$g(x)\neq 0$。

接着的话，对 $\forall\ x_1\neq x_2$，$\left\lvert g(x_1)-g(x_2) \right\rvert=\left\lvert \displaystyle\inf_{a_1\in F}{\left\lvert x_1-a_1 \right\rvert}-\displaystyle\inf_{a_2\in F}{\left\lvert x_2-a_2 \right\rvert} \right\rvert$，这个形式很像绝对值不等式，关键是怎么处理下确界。

固定 $x_{1},x_{2}$。对 $\forall\ a\in F$，有 $\left\lvert x_{1}-a \right\rvert\leq \left\lvert x_{1}-x_{2} \right\rvert+\left\lvert x_{2}-a \right\rvert$。因为 $\displaystyle\inf_{a_{1}\in F}{\left\lvert x_{1}-a_{1} \right\rvert}\leq \left\lvert x_{1}-a \right\rvert$，所以 $\displaystyle\inf_{a_{1}\in F}{\left\lvert x_{1}-a_{1} \right\rvert}\leq \left\lvert x_{1}-x_{2} \right\rvert+\left\lvert x_{2}-a \right\rvert$，这说明左边为右边的一个下界，由确界的定义又可得：

$$
\displaystyle\inf_{a_{1}\in F}{\left\lvert x_{1}-a_{1} \right\rvert}\leq \displaystyle\inf_{a_{2}\in F}{\left(\left\lvert x_{1}-x_{2} \right\rvert+\left\lvert x_{2}-a_{2} \right\rvert\right)}=\left\lvert x_{1}-x_{2} \right\rvert+\displaystyle\inf_{a_{2}\in F}{\left\lvert x_{2}-a_{2} \right\rvert}
$$

所以：

$$
\displaystyle\inf_{a_{1}\in F}{\left\lvert x_{1}-a_{1} \right\rvert}-\displaystyle\inf_{a_{2}\in F}{\left\lvert x_{2}-a_{2} \right\rvert}\leq \left\lvert x_{1}-x_{2} \right\rvert
$$

反向不等式也同理，即 $\left\lvert g(x_{1})-g(x_{2}) \right\rvert\leq \left\lvert x_{1}-x_{2} \right\rvert$。

对 $\forall\ \varepsilon>0$，令 $\delta=\displaystyle\frac{\varepsilon}{2}>0$，对 $\forall\ x,y\in \mathbb{R}$，$\left\lvert x-y \right\rvert<\delta$ 时，$\left\lvert g(x)-g(y) \right\rvert\leq \delta<\varepsilon$。

所以 $g$ 在 $\mathbb{R}$ 上一致连续，自然就也在 $\mathbb{R}$ 上连续了。

(b) $f$ 外层 $g$ 内层其实是有危险性的，假如 $g$ 把很多点全都正好映射到 $f$ 的不连续点上，那么不连续点集就会被放大，从而导致 $f\circ g$ 不可积。

这样的话，我们就开始构造。首先，取 $F$ 为上述改良的 Cantor 集变式 $C'$。再者，$g(x)$ 的值实际上与 $x$ 属不属于 $F$ 非常相关：

$$
\begin{cases}
    g(x)=0 \quad x\in F\\
    g(x)\neq 0 \quad x\notin F
\end{cases}
$$

所以我们构造一个 $f$，它仅在 $0$ 处不连续，以使得 $g$ 在 $F$ 上的映射全部对到 $f$ 的不连续处：

$$
f(x)=\begin{cases}
    0 \quad x=0\\
    1 \quad x\neq 0
\end{cases}
$$

当然，$f$ 在任意的 $[a,b]$ 上都可积，不过现在我们把目光放在 $f \circ g$ 上吧。

我们要证明的是，$f\circ g$ 在 $\forall\ c\in C'$ 上都不连续。

首先，$f(g(c))=f(0)=0$。但是这里的 $C'$，由上述定义，$c$ 一定会属于长度越来越小的某个闭区间 $C_{n}'$ 内。

若 $c$ 属于某个 $C_{n}'$ 刚分出来的闭区间 $[x_{1},x_{2}]$，则 $x_{2}-x_{1}=\displaystyle\frac{1}{3}\left(\displaystyle\frac{1}{2^{n-1}}+\displaystyle\frac{1}{3^{n}}\right)$，且 $x_1\leq c\leq x_2$。因为闭区间外的区域都不属于 $C'$（亦或说 $x_1$ 左邻域，$x_2$ 右邻域总存在不属于 $C'$ 中的点），所以总 $\exists\ x\in \left(c-\left(x_{2}-x_{1}\right),c+\left(x_{2}-x_{1}\right)\right)$，使得 $x\notin C'$，此时就有 $\left\lvert x-c \right\rvert<\displaystyle\frac{1}{3}\left(\displaystyle\frac{1}{2^{n-1}}+\displaystyle\frac{1}{3^{n}}\right)$ 且 $g(x)\neq 0,g(c)=0$ $\Rightarrow$ $f(g(x))=1, f(g(c))=0$。

所以可以构造出一个 $\left\{x_{n}\right\}\cap C'=\varnothing$，且 $\left\{x_n\right\}\to c$。因为 $\displaystyle\lim_{n\to \infty}f(g(x_{n}))=1\neq f(g(c))$，所以 $f\circ g$ 在 $\forall\ x\in C'$ 上都不连续。

所以 $f\circ g$ 的不连续点集至少包含 $C'$。又因为 $C'$ 不是零测集，所以 $f\circ g$ 不可积。

<br/>

---

## 习题 7.7 结语

Riemann对积分的定义是对Cauchy积分的修改，后者最初是为了积分连续函数而设计的。在这一目标上，Riemann积分取得了完全的成功。至少对于连续函数而言，积分过程现在建立在自身严格的基点上，独立于微分而定义。然而，随着分析学的发展，可积性对连续性的依赖变得有问题。第7.6节的最后一个例子突显了一种类型的弱点:并非每个导数都可以被积分。Riemann积分的另一个限制出现在与函数序列的极限相关的情况下。为了理解这一点，让我们再次考虑第4.1节中引入的Dirichlet函数 $g\left( x\right)$ 。回想一下，当 $x$ 为有理数时， $g\left( x\right)  = 1$ ；而在每个无理点， $g\left( x\right)  = 0$ 。暂时关注区间 $\left\lbrack  {0,1}\right\rbrack$ ，将其中的全体有理数枚举为

$$
\left\{  {{r}_{1},{r}_{2},{r}_{3},{r}_{4}\ldots }\right\}
$$

现在，如果 ${g}_{1}\left( x\right)  = 1$ ，则定义 $x = {r}_{1}$ ，否则定义 ${g}_{1}\left( x\right)  = 0$ 。接下来，如果 $x$ 是 ${r}_{1}$ 或 ${r}_{2}$ ，则定义 ${g}_{2}\left( x\right)  = 1$ ，在其他所有点定义 ${g}_{2}\left( x\right)  = 0$ 。一般而言，对于每个 $n \in  \mathbf{N}$ ，定义

$$
{g}_{n}\left( x\right)  = \begin{cases} 1 & x \in  \left\{  {{r}_{1},{r}_{2},\ldots ,{r}_{n}}\right\} \\ 0 &  otherwise.  \end{cases}
$$

注意到每个 ${g}_{n}$ 只有有限个间断点，因此在 ${\int }_{0}^{1}{g}_{n} = 0$ 下是Riemann可积的。但我们在区间 $\left\lbrack  {0,1}\right\rbrack$ 上也有 ${g}_{n} \rightarrow  g$ 逐点收敛。问题出现在我们想起Dirichlet的无处连续函数不是Riemann可积的时候。因此，方程

$$

\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{g}_{n} = {\int }_{0}^{1}g

$$

不成立，不是因为等号两边的值不同，而是因为右边的值不存在。定理7.4.4的内容是，当我们有 ${g}_{n} \rightarrow  g$ 一致收敛时，这个方程成立。这是解决这种情况的合理方式，但有点不令人满意，因为在这种情况下，缺陷并不完全在于收敛类型，而在于Riemann积分的强度。如果我们能通过某种其他积分定义来理解右边，那么也许方程式(eq:7.6.3)实际上会成立。

这种定义由 Henri Lebesgue 于1901年提出。一般来说，Lebesgue积分是通过一种称为集合测度的长度推广来构建的。在前一节中，我们研究了零测集。特别是，我们证明了 $\left\lbrack  {0,1}\right\rbrack$ 中的有理数(因为它们是可数的)具有零测度。 $\left\lbrack  {0,1}\right\rbrack$ 中的无理数具有测度 $1$。这并不令人惊讶，因为我们现在知道这两个不相交集合的测度加起来等于区间 $\left\lbrack  {0,1}\right\rbrack$ 的长度。Lebesgue建议通过分割 $y$ 轴来近似曲线下的面积，而不是分割 $x$ 轴。在Dirichlet函数 $g$ 的情况下，只有两个范围值——$0$和$1$。根据Lebesgue的观点，积分可以通过以下方式定义:
$$
\begin{aligned}
{\int }_{0}^{1}g = & 1 \cdot  \left\lbrack  {g^{-1}(1)的测度}\right\rbrack   + 0 \cdot  \left\lbrack  {g^{-1}(0) 的测度}\right\rbrack\\
= & 1 \cdot  0 + 0 \cdot  1 = 0.
\end{aligned}
$$

根据对 ${\int }_{0}^{1}g$ 的这种解释，方程式(eq:7.6.3)现在成立！

Lebesgue积分是目前高等数学中的标准积分。该理论被教授给所有研究生以及许多高年级本科生，并且在需要积分的多数研究论文中使用。Lebesgue积分推广了Riemann积分，因为任何Riemann可积的函数都是Lebesgue可积的，并且积分值相同。Lebesgue积分的真正优势在于可积函数的类要大得多。最重要的是，该类包括各种类型的可积函数Cauchy列的极限。这导致了一组与方程式(eq:7.6.3)相关的极其重要的收敛定理，其假设比定理7.4.4中假设的一致收敛性要弱得多。

尽管Lebesgue积分广泛使用，但它确实有一些缺点。存在一些函数的反常Riemann积分存在，但不是Lebesgue可积的。另一个失望来自于积分与微分之间的关系。即使使用Lebesgue积分，仍然无法在对 $f$ 进行一些额外假设的情况下证明

$$
{\int }_{a}^{b}{f}^{\prime } = f\left( b\right)  - f\left( a\right)
$$

大约在1960年，提出了一种新的积分，它能够比Riemann积分或Lebesgue积分积分更大类的函数，并且没有前述的缺点。值得注意的是，这种积分实际上是对Riemann原始积分技术的回归，只是在对分区的“精细度”描述上做了一些小的修改。广义Riemann积分的介绍是第8.1节的主题。

---