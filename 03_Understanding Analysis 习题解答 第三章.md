@import "style.less"

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
