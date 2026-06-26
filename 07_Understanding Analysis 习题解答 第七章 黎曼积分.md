# Riemann积分

## 习题 7.2 Riemann积分的定义

!!! question "练习 7.2.1"

    设 $f$ 是定义在 $\left\lbrack  {a,b}\right\rbrack$ 上的有界函数，且 $P$ 是 $\left\lbrack  {a,b}\right\rbrack$ 的任意分割。首先，解释为什么 $U\left( f\right)  \geq  L\left( {f,P}\right)$ 。现在，证明引理 7.2.6。

<br/>

!!! question "练习 7.2.2"

    考虑 $f\left( x\right)  = {2x} + 1$ 在区间 $\left\lbrack  {1,3}\right\rbrack$ 上的情况。设 $P$ 是由点 $\{ 1,3/2,2,3\}$ 构成的分割。
    
    (a) 计算 $L\left( {f,P}\right) ,U\left( {f,P}\right)$ 和 $U\left( {f,P}\right)  - L\left( {f,P}\right)$ 。
    
    (b) 当我们将点 $5/2$ 添加到分区时， $U\left( {f,P}\right)  - L\left( {f,P}\right)$ 的值会发生什么变化？
    
    (c) 找到一个 $\left\lbrack  {1,3}\right\rbrack$ 的分区 ${P}^{\prime }$ ，使得 $U\left( {f,{P}^{\prime }}\right)  - L\left( {f,{P}^{\prime }}\right)  < 2$ 。

<br/>

!!! question "练习 7.2.3"

    直接证明(不依赖于定理7.2)常数函数 $f\left( x\right)  = k$ 在任何闭区间 $\left\lbrack  {a,b}\right\rbrack$ 上可积。 ${\int }_{a}^{b}f$ 是什么？

<br/>

!!! question "练习 7.2.4"

    (a) 证明有界函数 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积的充分必要条件是存在一个分割序列 ${\left( {P}_{n}\right) }_{n = 1}^{\infty }$ 满足
    
    $$
    \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left\lbrack  {U\left( {f,{P}_{n}}\right)  - L\left( {f,{P}_{n}}\right) }\right\rbrack   = 0.
    $$
    
    (b) 对于每个 $n$ ，令 ${P}_{n}$ 为将 $\left\lbrack  {0,1}\right\rbrack$ 分割成 $n$ 个相等子区间的分割。如果 $f\left( x\right)  = x$ ，求 $U\left( {f,{P}_{n}}\right)$ 和 $L\left( {f,{P}_{n}}\right)$ 的公式。公式 $1 + 2 + 3 + \cdots  + n =$  $n\left( {n + 1}\right) /2$ 将会有用。
    
    使用(a)中的可积性顺序准则直接证明 $f\left( x\right)  = x$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上是可积的。

<br/>

!!! question "练习 7.2.5"

    假设对于每个 $n,{f}_{n}$ ， $\left\lbrack  {a,b}\right\rbrack$ 上的可积函数。如果 $\left( {f}_{n}\right)  \rightarrow  f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上一致收敛，证明 $f$ 在这个集合上也是可积的。(我们将看到，如果收敛是逐点的，这个结论不一定成立。)

<br/>

!!! question "练习 7.2.6"

    设 $f : \left\lbrack  {a,b}\right\rbrack   \rightarrow  \mathbf{R}$ 在集合 $\left\lbrack  {a,b}\right\rbrack$ 上递增(即，当 $x < y$ 时， $f\left( x\right)  \leq$  $f\left( y\right)$ )。证明 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积。

<br/>

---

## 习题 7.3 具有间断点的函数的积分

!!! question "练习 7.3.1"

    考虑函数
    
    $$
    h\left( x\right)  = \begin{cases} 1 &  for 0 \leq  x < 1 \\ 2 &  for x = 1 \end{cases}
    $$
    
    在区间 $\left\lbrack  {0,1}\right\rbrack$ 上。
    
    (a) 证明对于 $\left\lbrack  {0,1}\right\rbrack$ 的每个分割 $P$ ， $L\left( {f,P}\right)  = 1$ 成立。
    
    (b) 构建一个分割 $P$ ，使得 $U\left( {f,P}\right)  < 1 + 1/{10}$ 成立。
    
    给定 $\varepsilon  > 0$ ，构造一个分区 ${P}_{\varepsilon }$ ，使得 $U\left( {f,{P}_{\varepsilon }}\right)  < 1 + \varepsilon$ 。

<br/>

!!! question "练习 7.3.2"

    在例 7.3.3 中，我们了解到Dirichlet函数 $g\left( x\right)$ 不是Riemann可积的。构造一个可积函数序列 ${g}_{n}\left( x\right)$ ，使得 ${g}_{n} \rightarrow  g$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上逐点收敛。这表明可积函数的逐点极限不一定可积。将此示例与练习 7.2.5 中要求的结果进行比较。

<br/>

!!! question "练习 7.3.3"

    这里是对为什么在 $\left\lbrack  {a,b}\right\rbrack$ 上具有有限个间断点的函数 $f$ 可积的另一种解释。补充缺失的细节。
    
    将每个不连续性嵌入足够小的开区间，并令 $O$ 为这些区间的并集。解释为什么 $f$ 在 $\left\lbrack  {a,b}\right\rbrack   \smallsetminus  O$ 上一致连续，并利用这一点完成论证。

<br/>

!!! question "练习 7.3.4"

    假设 $f : \left\lbrack  {a,b}\right\rbrack   \rightarrow  \mathbf{R}$ 是可积的。
    
    (a) 证明如果在某一点 $x \in  \left\lbrack  {a,b}\right\rbrack$ 处改变 $f\left( x\right)$ 的一个值，那么 $f$ 仍然是可积的，并且积分值不变。
    
    (b) 证明如果改变 $f$ 的有限个值，(a)中的观察仍然成立。
    
    (c) 找出一个例子，说明通过改变可数个值， $f$ 可能不再可积。

<br/>

!!! question "练习 7.3.5"

    设
    
    $$
    f\left( x\right)  = \begin{cases} 1 & x = 1/n for some n \in  \mathbf{N} \\ 0 &  otherwise.  \end{cases}
    $$
    
    证明 $f$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上可积，并计算 ${\int }_{0}^{1}f$ 。

<br/>

!!! question "练习 7.3.6"

    一个集合 $A \subseteq  \left\lbrack  {a,b}\right\rbrack$ 如果对于每一个 $\varepsilon  > 0$ 都存在一个有限的开区间集合 $\left\{  {{O}_{1},{O}_{2},\ldots ,{O}_{N}}\right\}$ ，这些开区间的并集包含 $A$ 且它们的长度之和为 $\varepsilon$ 或更小，则称该集合具有零内容。用 $\left| {O}_{n}\right|$ 表示每个区间的长度，我们有
    
    $$
    A \subseteq  \mathop{\bigcup }\limits_{{n = 1}}^{N}{O}_{n}\; and \;\mathop{\sum }\limits_{{k = 1}}^{N}\left| {O}_{n}\right|  \leq  \varepsilon .
    $$
    
    (a) 设 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上有界。证明如果 $f$ 的不连续点集具有零内容，则 $f$ 可积。
    
    (b) 证明任何有限集都具有零内容。
    
    (c) 内容为零的集合不必是有限的。它们也不必是可数的。证明第3.1节中定义的Cantor集 $C$ 的内容为零。
    
    (d) 证明
    
    $$
    h\left( x\right)  = \begin{cases} 1 & x \in  C \\ 0 & x \notin  C. \end{cases}
    $$
    
    是可积的，并求出积分的值。

<br/>

---

## 习题 7.4 积分的性质

!!! question "练习 7.4.1"

    (a) 设 $f$ 为集合 $A$ 上的有界函数，并设
    
    $$
    M = \sup \{ f\left( x\right)  : x \in  A\} ,\;m = \inf \{ f\left( x\right)  : x \in  A\} ,
    $$
    
    $$
    {M}^{\prime } = \sup \{ \left| {f\left( x\right) }\right|  : x \in  A\} ,\; and \;{m}^{\prime } = \inf \{ \left| {f\left( x\right) }\right|  : x \in  A\} .
    $$
    
    证明 $M - m \geq  {M}^{\prime } - {m}^{\prime }$ 。
    
    (b) 证明如果 $f$ 在区间 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则 $\left| f\right|$ 在此区间上也可积。
    
    (c) 提供论证的细节，说明在这种情况下我们有 $\left| {{\int }_{a}^{b}f}\right|  \leq$  ${\int }_{a}^{b}\left| f\right|$ 。

<br/>

!!! question "练习 7.4.2"

    回顾定义 7.4.3。证明如果 $c \leq  a \leq  b$ 和 $f$ 在区间 $\left\lbrack  {c,b}\right\rbrack$ 上可积，则 ${\int }_{a}^{b}f = {\int }_{a}^{c}f + {\int }_{c}^{b}f$ 仍然成立。

<br/>

!!! question "练习 7.4.3"

    证明定理7.4.4，包括对练习7.2.5的论证(如果尚未完成)。练习7.4.4. 判断以下猜想中哪些为真，并提供简短证明。对于不成立的猜想，给出反例。
    
    (a) 如果 $\left| f\right|$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，则 $f$ 在该集合上也可积。
    
    (b) 假设 $g$ 可积且 $g \geq  0$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上。如果在无限多个点 $x \in  \left\lbrack  {a,b}\right\rbrack$ 上 $g\left( x\right)  > 0$ ，则 $\int g > 0$ 。
    
    如果 $g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 和 $g \geq  0$ 上连续，并且至少存在一个点 ${x}_{0} \in  \left\lbrack  {a,b}\right\rbrack$ 使得 $g\left( {x}_{0}\right)  > 0$ ，那么 ${\int }_{a}^{b}g > 0$ 。
    
    如果 ${\int }_{a}^{b}f > 0$ ，存在一个区间 $\left\lbrack  {c,d}\right\rbrack   \subseteq  \left\lbrack  {a,b}\right\rbrack$ 和一个 $\delta  > 0$ ，使得对于所有的 $x \in  \left\lbrack  {c,d}\right\rbrack$ ， $f\left( x\right)  \geq  \delta$ 成立。

<br/>

!!! question "练习 7.4.5"

    设 $f$ 和 $g$ 是 $\left\lbrack  {a,b}\right\rbrack$ 上的可积函数。
    
    (a) 证明如果 $P$ 是 $\left\lbrack  {a,b}\right\rbrack$ 的任意分割，则
    
    $$
    U\left( {f + g,P}\right)  \leq  U\left( {f,P}\right)  + U\left( {g,P}\right) .
    $$
    
    提供一个具体例子，其中不等式是严格的。对应的下和不等式是什么样子的？
    
    (b) 回顾定理 7.4.2 (ii) 的证明，并为该定理的 (i) 部分提供论证。

<br/>

!!! question "练习 7.4.6"

    回顾定理 7.4.4 之前的讨论。
    
    (a) 构造一个序列 ${f}_{n} \rightarrow  0$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上逐点收敛的例子，其中 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{f}_{n}$ 不存在。
    
    (b) 生成另一个例子(如有必要)，其中 ${f}_{n} \rightarrow  0$ 且序列 ${\int }_{0}^{1}{f}_{n}$ 无界。
    
    (c) 在(a)和(b)部分的例子中，是否可能构造每个 ${f}_{n}$ 使其连续？
    
    (d) 是否有可能构造序列 $\left( {f}_{n}\right)$ 使其一致有界？(一致有界意味着存在一个单一的 $M > 0$ 满足 $\left| {f}_{n}\right|  \leq  M$ 对于所有 $n \in  \mathbf{N}$ 。

<br/>

!!! question "练习 7.4.7"

    假设 ${g}_{n}$ 和 $g$ 是 $\left\lbrack  {0,1}\right\rbrack$ 上的有界可积函数，且 ${g}_{n} \rightarrow  g$ 。收敛性不是一致的；然而，在任何形式为 $\left\lbrack  {\delta ,1}\right\rbrack$ 的集合上，其中 $0 < \delta  < 1$ ，收敛性是一致的。证明 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{g}_{n} =$  ${\int }_{0}^{1}g$ 。

<br/>

---

## 习题 7.5 微积分基本定理

!!! question "练习 7.5.1"

    我们已经看到并非每个导数都是连续的，但请解释为什么我们至少知道每个连续函数都是导数。

<br/>

!!! question "练习 7.5.2"

    (a) 设 $f\left( x\right)  = \left| x\right|$ 并定义 $F\left( x\right)  = {\int }_{-1}^{x}f$ 。为所有 $x$ 找到 $F\left( x\right)$ 的公式。 $F$ 在何处连续？ $F$ 在何处可微？ ${F}^{\prime }\left( x\right)  = f\left( x\right)$ 在何处成立？
    
    (b) 对函数重复(a)部分
    
    $$
    f\left( x\right)  = \begin{cases} 1 & x < 0 \\ 2 & x \geq  0. \end{cases}
    $$

<br/>

!!! question "练习 7.5.3"

    定理7.5.1(i)中的假设，即对于所有 ${F}^{\prime }\left( x\right)  = f\left( x\right)$ ， $x \in  \left\lbrack  {a,b}\right\rbrack$ 的条件略强于实际需要。仔细阅读证明，并准确陈述在 $f$ 和 $F$ 之间的关系上需要假设什么才能使证明成立。

<br/>

!!! question "练习 7.5.4"

    (自然对数)。设
    
    $$
    H\left( x\right)  = {\int }_{1}^{x}\frac{1}{t}{dt}
    $$
    
    其中我们仅考虑 $x > 0$ 。
    
    (a) $H\left( 1\right)$ 是什么？找出 ${H}^{\prime }\left( x\right)$ 。
    
    (b) 证明 $H$ 是严格递增的；即，证明如果 $0 < x < y$ ，则 $H\left( x\right)  < H\left( y\right)$ 。
    
    (c) 证明 $H\left( {cx}\right)  = H\left( c\right)  + H\left( x\right)$ 。(将 $c$ 视为常数并对 $g\left( x\right)  = H\left( {cx}\right)$ 进行微分。)

<br/>

!!! question "练习 7.5.5"

    微积分基本定理可用于在导数序列连续的附加假设下，为定理 6.3.1 提供更简短的论证。
    
    假设 ${f}_{n} \rightarrow  f$ 逐点收敛且 ${f}_{n}^{\prime } \rightarrow  g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上一致收敛。假设每个 ${f}_{n}^{\prime }$ 都是连续的，我们可以应用定理 7.5.1 (i) 得到
    
    $$
    {\int }_{a}^{x}{f}_{n}^{\prime } = {f}_{n}\left( x\right)  - {f}_{n}\left( a\right)
    $$
    
    对于所有 $x \in  \left\lbrack  {a,b}\right\rbrack$ 。证明 $g\left( x\right)  = {f}^{\prime }\left( x\right)$ 。

<br/>

!!! question "练习 7.5.6"

    使用定理7.5.1的第(ii)部分，通过以下策略构造定理7.5.1的第(i)部分的另一个证明。给定 $f$ 和 $F$ 如第(i)部分所述，设 $G\left( x\right)  = {\int }_{a}^{x}f$ 。 $F$ 和 $G$ 之间有什么关系？

<br/>

!!! question "练习 7.5.7"

    (平均值)。如果 $g$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上连续，证明存在一个点 $c \in  \left( {a,b}\right)$ 使得
    
    $$
    g\left( c\right)  = \frac{1}{b - a}{\int }_{a}^{b}g.
    $$

<br/>

!!! question "练习 7.5.8"

    给定函数 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上，定义 $f$ 的全变差为
    
    为
    
    $$
    {Vf} = \sup \left\{  {\mathop{\sum }\limits_{{k = 1}}^{n}\left| {f\left( {x}_{k}\right)  - f\left( {x}_{k - 1}\right) }\right| }\right\}  ,
    $$
    
    其中上确界取遍 $\left\lbrack  {a,b}\right\rbrack$ 的所有分割 $P$ 。
    
    (a) 如果 $f$ 是连续可微的( ${f}^{\prime }$ 作为连续函数存在)，使用微积分基本定理证明 ${Vf} \leq  {\int }_{a}^{b}\left| {f}^{\prime }\right|$ 。
    
    (b) 使用中值定理建立反向不等式并得出结论 ${Vf} = {\int }_{a}^{b}\left| {f}^{\prime }\right|$ 。

<br/>

!!! question "练习 7.5.9"

    设
    
    $$
    h\left( x\right)  = \begin{cases} 1 & x < 1 or x > 1 \\ 0 & x = 1 \end{cases}
    $$
    
    并定义 $H\left( x\right)  = {\int }_{0}^{x}h$ 。证明即使 $h$ 在 $x = 1$ 处不连续， $H\left( x\right)$ 在 $x = 1$ 处仍然可微。

<br/>

!!! question "练习 7.5.10"

    假设 $f$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积，并且在 $c \in  \left( {a,b}\right)$ 处有一个“跳跃间断点”。这意味着当 $x$ 从左和从右接近 $c$ 时，两个单侧极限都存在，但
    
    $$
    \mathop{\lim }\limits_{{x \rightarrow  {c}^{ - }}}f\left( x\right)  \neq  \mathop{\lim }\limits_{{x \rightarrow  {c}^{ + }}}f\left( x\right) .
    $$
    
    (这一现象在第4.6节中有更详细的讨论。)
    
    证明 $F\left( x\right)  = {\int }_{a}^{x}f$ 在 $x = c$ 处不可微。

<br/>

!!! question "练习 7.5.11"

    第5章的结语提到存在一个连续单调函数，该函数在实数集R的一个稠密子集上不可微。结合练习7.5.10和练习6.4.8的结果，展示如何构造这样的函数。

<br/>

---

## 习题 7.6 Riemann可积性的Lebesgue准则

我们现在回到对连续性与Riemann积分之间关系的探讨。我们已经证明了连续函数是可积的，并且积分也存在于仅有有限个间断点的函数中。在另一极端，我们看到Dirichlet函数在 $\left\lbrack  {0,1}\right\rbrack$ 上的每一点都不连续，因此Riemann不可积。接下来的例子表明，可积函数的间断点集可以是无限的，甚至可以是不可数的。

### 具有无限间断点的Riemann可积函数

回顾第4.1节，Thomae函数

$$
t\left( x\right)  = \begin{cases} 1 & x = 0 \\ 1/n & x = m/n \in  \mathbf{Q} \smallsetminus  \{ 0\} ,n > 0, \gcd(m,n) = 1 \\ 0 & x \notin  \mathbf{Q} \end{cases}
$$

在无理数集上连续，并在每个有理点处不连续。让我们证明Thomae函数在 $\left\lbrack  {0,1}\right\rbrack$ 上可积，且 ${\int }_{0}^{1}t = 0$ 。

设 $\varepsilon  > 0$ 。策略与往常一样，是构造 $\left\lbrack  {0,1}\right\rbrack$ 的一个分割 ${P}_{\varepsilon }$ ，使得 $U\left( {t,{P}_{\varepsilon }}\right)  - L\left( {t,{P}_{\varepsilon }}\right)  < \varepsilon$ 。

<br/>

!!! question "练习 7.6.1"

    a) 首先，论证对于 $\left\lbrack  {0,1}\right\rbrack$ 的任何分割 $P$ ，都有 $L\left( {t,P}\right)  = 0$ 。
    
    b) 考虑点集 ${D}_{\varepsilon /2} = \{ x : t\left( x\right)  \geq  \varepsilon /2\}$ 。 ${D}_{\varepsilon /2}$ 有多大？
    
    c) 为了完成论证，解释如何构造 $\left\lbrack  {0,1}\right\rbrack$ 的一个分割 ${P}_{\varepsilon }$ ，使得 $U\left( {t,{P}_{\varepsilon }}\right)  < \varepsilon$ 。
    
    我们首次在3.1节中遇到了Cantor集 $C$ 。我们随后了解到， $C$ 是区间 $\left\lbrack  {0,1}\right\rbrack$ 的一个紧的、不可数的子集。练习4.3.12的要求是证明该函数
    
    $$
    g\left( x\right)  = \begin{cases} 1 & x \in  C \\ 0 & x \notin  C \end{cases}
    $$
    
    在 $C$ 的补集的每一点上连续，并且在 $C$ 的每一点上都有间断。因此， $g$ 在一个不可数无限集上不连续。

<br/>

!!! question "练习 7.6.2"

    利用 $C = \mathop{\bigcap }\limits_{{n = 0}}^{\infty }{C}_{n}$ 这一事实，其中每个 ${C}_{n}$ 由有限个闭区间的并集组成，论证 $g$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上是Riemann可积的。

<br/>

### 零测集

Thomae函数在 $\left\lbrack  {0,1}\right\rbrack$ 中的每个有理数点处都不连续。尽管这个集合是无限的，但我们已经看到 $\mathbf{Q}$ 的任何子集都是可数的。可数无限集是最小类型的无限集。Cantor集是不可数的，但在某种意义上它也是“小”的，我们现在可以精确地描述这一点。在第3章的引言中，我们提出了一个论点，即Cantor集的“长度”为零。这里的“长度”一词并不恰当，因为它实际上只应应用于区间或区间的并集，而Cantor集并非如此。有一种将长度概念推广到更一般集合的方法，称为集合的测度(measure)。在我们的讨论中，感兴趣的是测度为零的子集。

称一个集合 $A \subseteq  \mathbf{R}$ 具有零测度，如果对于所有 $\varepsilon  > 0$ ，存在一个可数的开区间集合 ${O}_{n}$ ，使得 $A$ 包含在所有区间的并集中，并且所有区间的长度之和小于或等于 $\varepsilon$ 。更准确地说，如果 $\left| {O}_{n}\right|$ 表示区间 ${O}_{n}$ 的长度，那么我们有

$$
A \subseteq  \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{O}_{n}\; 且\;\mathop{\sum }\limits_{{n = 1}}^{\infty }\left| {O}_{n}\right|  \leq  \varepsilon .
$$

考虑一个有限集合 $A = \left\{  {{a}_{1},{a}_{2},\ldots ,{a}_{N}}\right\}$ 。为了证明 $A$ 具有零测度，令 $\varepsilon  > 0$ 为任意值。对于每个 $1 \leq  n \leq  N$ ，构造
区间

$$
{G}_{n} = \left( {{a}_{n} - \frac{\varepsilon }{2N},{a}_{n} + \frac{\varepsilon }{2N}}\right) .
$$

显然， $A$ 包含在这些区间的并集中，并且

$$
\mathop{\sum }\limits_{{n = 1}}^{N}\left| {G}_{n}\right|  = \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\varepsilon }{N} = \varepsilon
$$

<br/>

!!! question "练习 7.6.3"

    证明任何可数集的测度为零。

<br/>

!!! question "练习 7.6.4"

    证明Cantor集(不可数)的测度为零。

<br/>

!!! question "练习 7.6.5"

    证明如果两个集合 $A$ 和 $B$ 的测度都为零，那么 $A \cup  B$ 的测度也为零。此外，讨论更强命题的证明，即测度为零的集合的可数并集的测度也为零。(第二个命题是正确的，但完全严格的证明需要关于第2.8节中讨论的双重求和的结果。)

<br/>

### \(\alpha\) -连续性

设 $f$ 定义在 $\left\lbrack  {a,b}\right\rbrack$ 上，且令 $\alpha  > 0$ 。若存在 $\delta  > 0$ ，使得对于所有 $y,z \in  \left( {x - \delta ,x + \delta }\right)$ ，都有 $\left| {f\left( y\right)  - f\left( z\right) }\right|  < \alpha$ ，则称函数 $f$ 在 $x \in  \left\lbrack  {a,b}\right\rbrack$ 处是 $\alpha$ -连续的。

设 $f$ 是定义在 $\left\lbrack  {a,b}\right\rbrack$ 上的有界函数。对于每个 $\alpha  > 0$ ，定义 ${D}_{\alpha }$ 为 $\left\lbrack  {a,b}\right\rbrack$ 中函数 $f$ 不满足 $\alpha$ -连续性的点集；即，

$$

{D}_{\alpha } = \{ x \in  \left\lbrack  {a,b}\right\rbrack   : f  在x 处不 \alpha 连续.\} .

$$

$\alpha$ -连续性的概念已在第4.6节中介绍。随后的几个练习也出现在本节中。

<br/>

!!! question "练习 7.6.6"

    如果 ${\alpha }_{1} < {\alpha }_{2}$ ，证明 ${D}_{{\alpha }_{2}} \subseteq  {D}_{{\alpha }_{1}}$ 。
    
    现在，设
    
    $$
    
    D = \{ x \in  \left\lbrack  {a,b}\right\rbrack   : f  在x 处不连续\} .
    
    $$

<br/>

!!! question "练习 7.6.7"

    (a) 设 $\alpha  > 0$ 给定。证明如果 $f$ 在 $x \in  \left\lbrack  {a,b}\right\rbrack$ 处连续，则它在 $x$ 处也是 $\alpha$ -连续的。解释如何由此得出 ${D}_{\alpha } \subseteq  D$ 。
    
    (b) 证明如果 $f$ 在 $x$ 处不连续，则 $f$ 对于某个 $\alpha  > 0$ 不是 $\alpha$ -连续的。现在，解释为什么这保证了
    
    $$
    D = \mathop{\bigcup }\limits_{{n = 1}}^{\infty }{D}_{1/n}
    $$

<br/>

!!! question "练习 7.6.8"

    证明对于固定的 $\alpha  > 0$ ，集合 ${D}_{\alpha }$ 是闭的。

<br/>

!!! question "练习 7.6.9"

    通过模仿定理 4.4.8 的证明，证明如果对于某个固定的 $\alpha  > 0,f$ ， $\alpha$ 在某个紧集 $K$ 上的每一点都是连续的，那么 $f$ 在 $K$ 上是一致 $\alpha$ 连续的。所谓一致 $\alpha$ 连续，是指存在一个 $\delta  > 0$ ，使得每当 $x$ 和 $y$ 是 $K$ 中满足 $\left| {x - y}\right|  < \delta$ 的点时，就有 $\left| {f\left( x\right)  - f\left( y\right) }\right|  < \alpha$ 。

<br/>

### 紧性再探

实数集的紧性可以用三种等价的方式来描述。以下定理出现在第3.3节的末尾。

设 $K \subseteq  \mathbf{R}$ 。以下三个陈述都是等价的，即如果其中任何一个为真，则其他两个也为真。

每个包含在 $K$ 中的序列都有一个收敛子序列，且该子序列收敛到 $K$ 中的一个极限。
$K$ 是闭集且有界的。
给定一组覆盖 $K$ 的开区间 $\left\{  {{G}_{\alpha } : \alpha  \in  \Lambda }\right\}$ ；即 $K \subseteq  \mathop{\bigcup }\limits_{{\alpha  \in  \Lambda }}{G}_{\alpha }$ ，存在原集合的一个有限子集 $\left\{  {{G}_{{\alpha }_{1}},{G}_{{\alpha }_{2}},{G}_{{\alpha }_{3}},\ldots ,{G}_{{\alpha }_{N}}}\right\}$ ，该子集也覆盖 $K$ 。

(7.6.1)和~(7.6.2)的等价性已在文本的核心材料中广泛使用。特征~(7.6.3)虽然不那么核心，但对即将进行的论证至关重要。为了使本节内容自成一体，我们快速概述~(7.6.1)和~(7.6.2)蕴含~(7.6.3)的证明。(这也作为练习3.3.8出现。)

假设 $K$ 满足~(7.6.1)和~(7.6.2)，并设 $\left\{  {{G}_{\alpha } : \alpha  \in  \Lambda }\right\}$ 是 $K$ 的一个开覆盖。为了引出矛盾，我们假设不存在有限子覆盖。

设 ${I}_{0}$ 为一个包含 $K$ 的闭区间，然后将 ${I}_{0}$ 二等分为两个闭区间 ${A}_{1}$ 和 ${B}_{1}$ 。必定存在 ${A}_{1} \cap  K$ 或 ${B}_{1} \cap  K$ (或两者)无法由 $\left\{  {{G}_{\alpha } : \alpha  \in  \Lambda }\right\}$ 中的集合构成有限子覆盖。设 ${I}_{1}$ 为 ${I}_{0}$ 的一半，包含无法被有限覆盖的 $K$ 部分。重复此构造将得到一个闭区间嵌套序列 ${I}_{0} \supseteq  {I}_{1} \supseteq  {I}_{2} \supseteq$  $\cdots$ ，其性质为，对于任何 $n,{I}_{n} \cap  K$ 都无法被有限覆盖且 $\mathop{\lim }\limits_{n}\left| {I}_{n}\right|  = 0$ 。

<br/>

!!! question "练习 7.6.10"

    (a) 证明存在一个 $x \in  K$ ，使得对于所有 $n$ ， $x \in  {I}_{n}$ 成立。
    
    (b) 由于 $x \in  K$ ，原始集合中必须存在一个包含 $x$ 作为元素的开集 ${G}_{{\alpha }_{0}}$ 。解释为什么这为我们提供了所需的矛盾。

<br/>

### Lebesgue定理

我们现在准备从连续性的角度对Riemann可积函数的集合进行完全分类。

设 $f$ 是定义在区间 $\left\lbrack  {a,b}\right\rbrack$ 上的有界函数。那么， $f$ 是Riemann可积的当且仅当 $f$ 不连续的点集测度为零。

设 $M > 0$ 满足 $\left| {f\left( x\right) }\right|  \leq  M$ 对所有 $x \in  \left\lbrack  {a,b}\right\rbrack$ 成立，并设 $D$ 和 ${D}_{\alpha }$ 如前面方程式(7.6.1)和式(7.6.2)所定义。我们首先假设 $D$ 的测度为零，并证明我们的函数是可积的。

($\Leftarrow$) 设

$$
\alpha  = \frac{\varepsilon }{2\left( {b - a}\right) }.
$$

<br/>

!!! question "练习 7.6.11"

    证明存在一个由不相交的开区间 $\left\{  {{G}_{1},{G}_{2},\ldots ,{G}_{N}}\right\}$ 组成的有限集合，其并集包含 ${D}_{\alpha }$ ，并且满足
    
    $$
    \mathop{\sum }\limits_{{n = 1}}^{N}\left| {G}_{n}\right|  < \frac{\varepsilon }{4M}
    $$

<br/>

!!! question "练习 7.6.12"

    设 $K$ 为区间 $\left\lbrack  {a,b}\right\rbrack$ 在移除所有开区间 ${G}_{n}$ 后剩余的部分；即 $K = \left\lbrack  {a,b}\right\rbrack   \smallsetminus  \mathop{\bigcup }\limits_{{n = 1}}^{N}{G}_{n}$ 。论证 $f$ 在 $K$ 上是一致 $\alpha$ 连续的。

<br/>

!!! question "练习 7.6.13"

    通过解释如何构造一个分区 ${P}_{\varepsilon }$ 来完成这个方向的证明，使得 $U\left( {f,{P}_{\varepsilon }}\right)  - L\left( {f,{P}_{\varepsilon }}\right)  \leq  \varepsilon$ 。将和式分解为两部分会有所帮助
    
    $$
    U\left( {f,{P}_{\varepsilon }}\right)  - L\left( {f,{P}_{\varepsilon }}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{M}_{k} - {m}_{k}}\right) \Delta {x}_{k}
    $$
    
    一部分包含 ${D}_{\alpha }$ 点的子区间，另一部分不包含 ${D}_{\alpha }$ 点的子区间。
    
    $\left(  \Rightarrow  \right)$ 对于另一个方向，假设 $f$ 是Riemann可积的。我们必须论证 $f$ 的不连续点集 $D$ 的测度为零。
    
    固定 $\alpha  > 0$ ，并令 $\varepsilon  > 0$ 为任意值。因为 $f$ 是Riemann可积的，存在 $\left\lbrack  {a,b}\right\rbrack$ 的一个分割 ${P}_{\varepsilon }$ ，使得 $U\left( {f,{P}_{\varepsilon }}\right)  - L\left( {f,{P}_{\varepsilon }}\right)  < {\alpha \varepsilon }$ 。

<br/>

!!! question "练习 7.6.14"

    (a) 使用分割 ${P}_{\varepsilon }$ 的子区间来证明 ${D}_{\alpha }$ 的测度为零。指出可以选择由有限个开区间组成的 ${D}_{\alpha }$ 的覆盖。(对于这种情况的集合有时被称为零内容。参见习题 7.3.6。)
    
    (b) 展示这如何意味着 $D$ 的测度为零。

<br/>

### 不可积的导数

到目前为止，我们关于不可积函数的一个例子是Dirichlet的无处连续函数。我们以另一个具有特殊意义的例子来结束本节。微积分基本定理的内容是积分和微分是彼此互逆的过程。这让我们提出了一个问题(在第7.1节讨论的最后一段中)，即我们是否可以对每一个导数进行积分。对于Riemann积分，答案是否定的。接下来是一个可微函数的构造，其导数无法用Riemann积分进行积分。

此处需在原文件中插入图片

${f}_{1}\left( x\right)$ 的初步草图。

我们将再次对在第3.1节中定义的Cantor集感兴趣

$$
C = \mathop{\bigcap }\limits_{{n = 0}}^{\infty }{C}_{n}
$$

作为第一步，让我们创建一个在 $\left\lbrack  {0,1}\right\rbrack$ 上可微的函数 $f\left( x\right)$ ，其导数 ${f}^{\prime }\left( x\right)$ 在 $C$ 的每一点都有间断。这个构造的关键成分是函数

$$
g\left( x\right)  = \begin{cases} {x}^{2}\sin \left( {1/x}\right) & x > 0 \\ 0 & x \leq  0. \end{cases}
$$

<br/>

!!! question "练习 7.6.15"

    (a) 求 ${g}^{\prime }\left( 0\right)$ 。
    
    (b) 使用微分的标准规则计算 $x\ne 0 $ 时的 ${g}^{\prime }\left( x\right)$ 。
    
    (c) 解释为什么，对于每一个 $\delta  > 0,{g}^{\prime }\left( x\right)$ ，当 $x$ 在集合 $\left( {-\delta ,\delta }\right)$ 上变化时， $\delta  > 0,{g}^{\prime }\left( x\right)$ 会取得$1$和$-1$之间的每一个值。由此得出 ${g}^{\prime }$ 在 $x = 0$ 处不连续。
    
    现在，我们希望将 $g$ 在零附近的行为转移到构成Cantor集定义中使用的闭区间 ${C}_{n}$ 的每个端点。公式虽然复杂，但基本思路是直接的。首先设定
    
    $$
    {f}_{0}\left( x\right)  = 0,\quad \forall x \in {C}_{0} = \left\lbrack  {0,1}\right\rbrack  .
    $$
    
    要在 $\left\lbrack  {0,1}\right\rbrack$ 上定义 ${f}_{1}$ ，首先赋值
    
    $$
    {f}_{1}\left( x\right)  = 0,\quad \forall x \in  {C}_{1} = \left\lbrack  {0,\frac{1}{3}}\right\rbrack   \cup  \left\lbrack  {\frac{2}{3},1}\right\rbrack  .
    $$
    
    此处需在原文件中插入图片
    
    ${f}_{2}\left( x\right)$ 的图像
    
    在剩余的开放中间三分之一处，放置 $g$ 的翻译“副本”，使其向两个端点振荡(图7.3)。用公式表示，我们有
    
    $$
    {f}_{1}\left( x\right)  = \begin{cases} 0 & x \in  \left\lbrack  {0,1/3}\right\rbrack \\ g\left( {x - 1/3}\right) & x 恰在 1/3 之右 \\ g\left( {-x + 1/3}\right) & x 恰在 2/3 之右 \\ 0 & x \in  \left\lbrack  {2/3,1}\right\rbrack  . \end{cases}
    $$
    
    最后，我们将 ${f}_{1}$ 的两个振荡部分以使其可微的方式拼接在一起。这并不是什么了不起的壮举，我们将跳过细节，以便将注意力集中在两个端点 $1/3$ 和 $2/3$ 上。这些是 ${f}_{1}^{\prime }\left( x\right)$ 不连续的点。
    
    为了定义 ${f}_{2}\left( x\right)$ ，我们从 ${f}_{1}\left( x\right)$ 开始，并采用与之前相同的技巧，这次在两个开区间 $\left( {1/9,2/9}\right)$ 和 $\left( {7/9,8/9}\right)$ 中进行。结果(图7.4)是一个在 ${C}_{2}$ 上为零的可微函数，其导数在该集合上不连续。
    
    $$
    \{ 1/9,2/9,1/3,2/3,7/9,8/9\}  . 
    $$
    
    以这种方式继续下去，会产生一系列定义在 $\left\lbrack  {0,1}\right\rbrack$ 上的函数 ${f}_{0},{f}_{1},{f}_{2},\ldots$ 。

<br/>

!!! question "练习 7.6.16"

    (a) 如果 $c \in  C$ ，那么 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{f}_{n}\left( c\right)$ 是什么？
    
    (b) 为什么 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{f}_{n}\left( x\right)$ 对 $x \notin  C$ 存在？
    
    现在，设置
    
    $$
    f\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{f}_{n}\left( x\right) .
    $$

<br/>

!!! question "练习 7.6.17"

    (a) 解释为什么 ${f}^{\prime }\left( x\right)$ 对所有 $x \notin  C$ 存在。
    
    (b) 如果 $c \in  C$ ，论证 $\left| {f\left( x\right) }\right|  \leq  {\left( x - c\right) }^{2}$ 对所有 $x \in  \left\lbrack  {0,1}\right\rbrack$ 成立。说明这如何暗示 ${f}^{\prime }\left( c\right)  = 0$ 。
    
    (c) 给出一个详细的论证，说明为什么 ${f}^{\prime }\left( x\right)$ 在 $C$ 上不连续。记住， $C$ 包含了许多除了构成 ${C}_{1},{C}_{2},{C}_{3},\ldots$ 的区间端点之外的点。
    
    让我们盘点一下当前的情况。我们的目标是创建一个不可积的导数。我们的函数 $f\left( x\right)$ 是可微的，而 ${f}^{\prime }$ 在 $C$ 上不连续。我们还没有完全完成。

<br/>

!!! question "练习 7.6.18"

    为什么 ${f}^{\prime }\left( x\right)$ 在 $\left\lbrack  {0,1}\right\rbrack$ 上是Riemann可积的？
    
    Cantor集的测度为零的原因是，在每一阶段，从 ${C}_{n - 1}$ 中移除了长度为 $1/{3}^{n}$ 的 ${2}^{n - 1}$ 个开区间。最终的和
    
    $$
    \mathop{\sum }\limits_{{n = 1}}^{\infty }{2}^{n - 1}\left( \frac{1}{{3}^{n}}\right)
    $$
    
    收敛到一，这意味着近似集 ${C}_{1},{C}_{2},{C}_{3},\ldots$ 的总长度趋向于零。与其在每一阶段移除长度为 $1/{3}^{n}$ 的开区间，让我们看看当我们移除长度为 $1/{3}^{n + 1}$ 的区间时会发生什么。

<br/>

!!! question "练习 7.6.19"

    证明在这些情况下，组成每个 ${C}_{n}$ 的区间长度之和不再随着 $n \rightarrow  \infty$ 趋于零。这个极限是什么？
    
    如果我们再次取交集 $\mathop{\bigcap }\limits_{{n = 0}}^{\infty }{C}_{n}$ ，结果是一个具有相同拓扑性质的Cantor型集合——它是闭的、紧的和完美的。但前一个练习的结果是它不再具有零测度。这正是我们定义所需函数所需要的。通过在这个新的具有正测度的Cantor型集合上重复 $f\left( x\right)$ 的构造，我们得到一个可微函数。但其导数有太多的不连续点。根据Lebesgue定理，这个导数Riemann不可积。

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
