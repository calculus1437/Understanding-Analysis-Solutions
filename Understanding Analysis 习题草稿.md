## 7.6 Riemann 可积性的 Lebesgue 准则

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

