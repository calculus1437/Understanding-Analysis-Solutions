@import "style.less"

[5.极限平均值定理与反向情况下的反例](#4)(2.3.11)
[6.实数几大基本定理的互证](#5)(2.6.6)
[7.几何级数与 $\mathrm{p}$ 级数间的转换](#6)(2.7.7)
[8.绝对收敛重排定理的证明](#7)(2.7.14)

# 数列与级数

## 习题 2.2 序列的极限

!!! question "练习 2.2.1"
    使用序列收敛的定义，验证以下序列收敛于所提出的极限。
    
    (a) \(\lim \frac{1}{\left( 6{n}^{2} + 1\right) } = 0\) .
    
    (b) \(\lim \frac{{3n} + 1)}{\left( 2n + 5\right) } = \frac{3}{2}\) .
    
    (c) \(\lim \frac{2}{\sqrt{n + 3}} = 0\) .

(a) 选取一个 $\varepsilon>0$，我们寻找 $N\in \mathbb{N^+}$ 使得 $\displaystyle\frac{1}{6N^2+1}<\varepsilon$。事实上，因为 $\displaystyle\frac{1}{6N^2+1}<\frac{1}{N}$，令 $\displaystyle \frac{1}{N}<\varepsilon$，得出 $\displaystyle N>\frac{1}{\varepsilon}$ 即可，于是对 $\forall\ n>N$，都有 $\displaystyle\frac{1}{6n^2+1}-0<\varepsilon$。

(b) 相似地，令 $\displaystyle \left|\frac{3N+1}{2N+5}-\frac{3}{2}\right|=\frac{13}{4N+10}<\frac{13}{4N}<\varepsilon$，得出 $\displaystyle N>\frac{13}{4\varepsilon}$。

(c) 同理。

<br/>


!!! question "练习 2.2.2"
    如果我们在定义2.2.3中颠倒量词的顺序，会发生什么？
    
    定义:一个序列 \(\left( {x}_{n}\right)\) verconges到 \(x\) ，如果存在一个 \(\varepsilon  > 0\) ，使得对于所有 \(N \in  \mathbb{N}\) ， \(n \geq  N\) 蕴含 \(\left| {{x}_{n} - x}\right|  < \varepsilon\) 成立。
    
    给出一个vercongent序列的例子。你能给出一个发散但vergonent序列的例子吗？这个奇怪的定义到底在描述什么？

$\exists\ \varepsilon>0$，对 $\forall\ N\in \mathbb{N^+}$，只要 $n\geq N$ 就有 $|a_n-a|<\varepsilon$。

其实这就是说 $a_n$ 是有界的。

例如：$\displaystyle a_n=(-1)^n$，取 $\varepsilon=1.1$，$a=0$。

<br/>


!!! question "练习 2.2.3"
    描述为了反驳以下每个陈述，我们需要证明什么。
    
    (a) 在美国的每一所大学里，都有一个至少七英尺高的学生。
    
    (b) 对于美国的所有大学，都存在一位教授给每个学生A或B的成绩。
    
    在美国有一所大学，那里的每个学生都至少有六英尺高。

(a) 在美国某一所大学里，有一个没有七英尺高的学生。

(b) 在美国某一所大学里，没有一位给学生 $A$ 或 $B$ 成绩的教授。

(c) 在美国所有大学里，都有一位没有六英尺高的学生。

<br/>


!!! question "练习 2.2.4"
    论证该序列
    
    $$
    1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,\left( {5\text{ zeros }}\right) ,1,\ldots
    $$
    
    不收敛于零。对于哪些 \(\varepsilon  > 0\) 值存在响应 \(N\) 。对于哪些 \(\varepsilon  > 0\) 值没有合适的响应？

我们假设它以 $0$ 为极限，那么对于 $\varepsilon\geq 1$ 有效，对于 $\varepsilon<1$ 无效。事实上，由于这个数列永远都会在 $0,1$ 之间跳动，所以不可能以 $0$ 为极限。

<br/>


!!! question "练习 2.2.5"
    设 \(\left\lbrack  \left\lbrack  x\right\rbrack  \right\rbrack\) 为小于或等于 \(x\) 的最大整数。例如， \(\left\lbrack  \left\lbrack  \pi \right\rbrack  \right\rbrack   = 3\) 和 \(\left\lbrack  \left\lbrack  3\right\rbrack  \right\rbrack   = 3\) 。求 \(\lim {a}_{n}\) 并为每个结论提供证明，如果
    
    (a) \({a}_{n} = \left\lbrack  \left\lbrack  {1/n}\right\rbrack  \right\rbrack\) ,
    
    (b) \({a}_{n} = \left\lbrack  \left\lbrack  {\left( {{10} + n}\right) /{2n}}\right\rbrack  \right\rbrack\) .
    
    反思这些例子，评论定义 2.2.3 之后的陈述:“ \(\varepsilon\) -邻域越小， \(N\) 可能需要越大。”

(a) 对于 $\displaystyle a_n=[[\frac{1}{n}]]$，除了 $a_1=1$，其余项均为 $0$，所以它以 $0$ 为极限。

(b) 对于 $\displaystyle a_n=[[\frac{10+n}{2n}]]$， 当 $n>10$ 时均为 $0$，所以它以 $0$ 为极限。

“$\varepsilon$-邻域越小，$N$ 可能需要越大”是对所有收敛数列的普遍刻画，但并不是说 $N$ 一定会随着 $\varepsilon$ 的减小而增大。

<br/>


!!! question "练习 2.2.6"
    假设对于特定的 \(\varepsilon  > 0\) ，我们已经找到了一个合适的 \(N\) 值，该值在定义2.2.3的意义上对给定序列“有效”。
    
    (a) 那么，任何更大/更小(选择一个)的 \(N\) 也将对相同的 \(\varepsilon  > 0\) 有效。
    
    (b) 那么，相同的 \(N\) 也将对任何更大/更小的 \(\varepsilon\) 值有效。

(a) (b) 均为更大，用不等式的传递性得出结论。

<br/>


!!! question "练习 2.2.7"
    非正式地说，序列 \(\sqrt{n}\) “收敛到无穷大”。
    
    (a) 模仿定义2.2.3的逻辑结构，为数学陈述 \(\lim {x}_{n} = \infty\) 创建一个严格的定义。使用这个定义来证明 \(\lim \sqrt{n} = \infty\) 。
    
    (b) 你在(a)中的定义对特定序列 \(\left( {1,0,2,0,3,0,4,0,5,0,\ldots }\right)\) 说了什么？

(a) 对 $\forall\ G>0$，$\exists\ N\in \mathbb{N^+}$ 使得 $\forall\ n\geq N$，都有 $a_n>G$。

对于 $a_n=\sqrt{n}$，取 $N>G^2$ 即可。

(b) 因为总 $\exists\ k\in \mathbb{N^+}$ 使得 $a_k=0$，所以它不满足 (a) 中定义，不收敛到无穷大。

<br/>


!!! question "练习 2.2.8"
    这里有两个有用的定义:
    
    (i) 一个序列 \(\left( {a}_{n}\right)\) 最终在一个集合 \(A \subseteq  \mathbb{R}\) 中，如果存在一个 \(N \in  \mathbb{N}\) 使得对于所有 \(n \geq  N\) ， \({a}_{n} \in  A\) 。
    
    (ii) 一个序列 \(\left( {a}_{n}\right)\) 频繁在一个集合 \(A \subseteq  \mathbb{R}\) 中，如果对于每一个 \(N \in  \mathbb{N}\) ，存在一个 \(n \geq  N\) 使得 \({a}_{n} \in  A\) 。
    
    (a) 序列 \({\left( -1\right) }^{n}\) 是最终还是频繁在集合 \(\{ 1\}\) 中？
    
    (b) 哪个定义更强？频繁是否意味着最终，还是最终意味着频繁？
    
    (c) 使用频繁或最终重新表述定义 2.2.3B。我们想要的是哪个术语？
    
    (d) 假设一个序列 \(\left( {x}_{n}\right)\) 的无限多项等于2。 \(\left( {x}_{n}\right)\) 是否必然最终在区间(1.9,2.1)内？它是否频繁出现在(1.9,2.1)内？

(a) 频繁。

(b) (i) 定义更强，最终也意味着频繁。

(c)  使用“最终”术语：$(a_n)$ 收敛于 $a$，若对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$ 使得 $\forall\ n\geq N$，都有 $a_n\in (a-\varepsilon,a+\varepsilon)$。

(d) 如果它还在其它数上跳跃，那么可能不最终，但因为总有 $a_k=2\in (1.9,2.1)$，所以频繁。

---

## 习题 2.3 代数极限定理与序极限定理

!!! question "练习 2.3.1"
    证明常数序列 \(\left( {a,a,a,a,\ldots }\right)\) 收敛到 \(a\) 。

 严谨地写一遍，对 $\forall\ \varepsilon>0$，$|a_n-a|=0<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty} a_n=a$。

<br/>


!!! question "练习 2.3.2"
    设 \({x}_{n} \geq  0\) 对于所有 \(n \in  \mathbb{N}\) 。
    
    (a) 如果 \(\left( {x}_{n}\right)  \rightarrow  0\) ，证明 \(\left( \sqrt{{x}_{n}}\right)  \rightarrow  0\) 。
    
    (b) 如果 \(\left( {x}_{n}\right)  \rightarrow  x\) ，证明 \(\left( \sqrt{{x}_{n}}\right)  \rightarrow  \sqrt{x}\) 。

(a) 由题意，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$， 使得对 $\forall\ n>N$，有 $|x_n-0|<\varepsilon^2$。即 $|\sqrt{x_n}-0|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty} \sqrt{x_n}=0$。

(b) 由 (a) 同样的操作，可得对某个 $n>N_1$，$|x_n-x|<C\varepsilon$，其中 $C$ 可以是大于 $0$ 的任意常数。由 $\displaystyle|\sqrt{x_n}-\sqrt{x}|=\frac{|x_n-x|}{\sqrt{x_n}+\sqrt{x}}$，考虑 $\sqrt{x_n}+\sqrt{x}$ 的下界即可。

由于 $\displaystyle\lim_{n\to \infty}x_n=x$，那么 $\exists\ N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_2$，有 $\displaystyle x_n>\frac{x}{2}$。所以取 $C=\displaystyle\frac{1}{\sqrt{\displaystyle\frac{x}{2}}+\sqrt{x}}$，并让 $N>\max\{N_1,N_2\}$，则有 $\displaystyle|\sqrt{x_n}-\sqrt{x}|=\frac{|x_n-x|}{\sqrt{x_n}+\sqrt{x}}<\varepsilon$。这样就得到 $\displaystyle\lim_{n\to\infty}\sqrt{x_n}= \sqrt{x}$。

<br/>


!!! question "练习 2.3.3"
    (夹逼定理)。证明如果对于所有 \(n \in\)  \(\mathbb{N}\) 有 \({x}_{n} \leq  {y}_{n} \leq  {z}_{n}\) ，且如果 \(\lim {x}_{n} = \lim {z}_{n} = l\) ，则 \(\lim {y}_{n} = l\) 也成立。

使用两次序极限定理，得到 $\displaystyle\lim_{n\to\infty}x_n\leq\lim_{n\to\infty}y_n\leq\lim_{n\to\infty}z_n$。由此可得 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=\lim_{n\to\infty}z_n=l$。

<br/>


!!! question "练习 2.3.4"
    证明极限如果存在，则必须是唯一的。换句话说，假设 \(\lim {a}_{n} = {l}_{1}\) 和 \(\lim {a}_{n} = {l}_{2}\) ，并证明 \({l}_{1} = {l}_{2}\) 。

不失一般性，不妨设 $l_1>l_2$，利用 $l_1,l_2$ 的间距，以及数列与极限间距离随项数增大会小于任何间距得出矛盾。

由定义，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，有 $\displaystyle|a_n-l_1|<\frac{l_1-l_2}{2}$，因此 $\displaystyle a_n>\frac{l_1+l_2}{2}$，所以 $\displaystyle\lim_{n\to\infty} a_n\geq \frac{l_1+l_2}{2}>l_2$，这与 $\displaystyle\lim_{n\to\infty} a_n=l_2$ 矛盾。

所以 $l_1=l_2$，极限有唯一性。

<br/>

$2.3.5.$<a id="2.3.5."></a>

$\Rightarrow$) 若 $\{z_n\}$ 收敛，则 $\exists\ z\in \mathbb{R}$，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，有 $|z_n-z|<\varepsilon$。即 $|x_n-z|<\varepsilon$ 和 $|y_n-z|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=z$。

$\Leftarrow)$ 若 $\displaystyle\lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n=z$，则对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，有 $|x_n-z|<\varepsilon$，对 $\forall\ n>N_2$，有 $|y_n-z|<\varepsilon$。取 $N=\max\{N_1,N_2\}$，则对 $\forall\ n>N$，有 $|x_{2n}-z|<\varepsilon$ 和 $|y_{2n}-z|<\varepsilon$，即 $|z_n-z|<\varepsilon$，所以 $\{z_n\}$ 收敛。

<br/>


!!! question "练习 2.3.6"
    (a) 证明如果 \(\left( {b}_{n}\right)  \rightarrow  b\) ，则绝对值序列 \(\left| {b}_{n}\right|\) 收敛到 \(\left| b\right|\) 。
    
    (b) 部分(a)的逆命题是否成立？如果我们知道 \(\left| {b}_{n}\right|  \rightarrow  \left| b\right|\) ，能否推断出 \(\left( {b}_{n}\right)  \rightarrow  b\) ？

(a)  对于单独的绝对值，尝试使用绝对值不等式 $||b_n|-|b||\leq |b_n-b|<\varepsilon$，所以 $\displaystyle \lim_{n\to\infty}|b_n|=|b|$。

(b) 不等式的反向是不成立的。考虑 $b_n=(-1)^n$，则 $\displaystyle\lim_{n\to\infty}|b_n|=1$，但 $\{b_n\}$ 发散。

<br/>


!!! question "练习 2.3.7"
    (a) 设 \(\left( {a}_{n}\right)\) 为有界(不一定收敛)序列，并假设 \(\lim {b}_{n} = 0\) 。证明 \(\lim \left( {{a}_{n}{b}_{n}}\right)  = 0\) 。为什么我们不能使用代数极限定理来证明这一点？
    
    (b) 如果我们假设 \(\left( {b}_{n}\right)\) 收敛到某个非零极限 \(b\) ，能否得出关于 \(\left( {{a}_{n}{b}_{n}}\right)\) 收敛性的任何结论？
    
    (c) 使用(a)来证明定理2.3.3的第(iii)部分，当 \(a = 0\) 时的情况。

(a) $\{a_n\}$ 发散的情况下并不能使用代数极限定理。这里利用有界性进行证明。

$\{a_n\}$ 有界即 $\exists\ M>0$，对 $\forall\ n\in \mathbb{N^+}$，有 $|a_n|<M$。所以 $|a_nb_n|=|a_n||b_n|<M|b_n|$，再令 $\displaystyle|b_n-b|<\frac{\varepsilon}{M}$ 即得 $\displaystyle\lim_{n\to\infty}a_nb_n=0$。

(b) 不能，$\{a_n\}$ 任意跳动的情况下，$\{a_nb_n\}$ 也会任意跳动。

(c) $\{b_n\}$ 收敛即有界，使用 (a) 的结论即可。

<br/>


!!! question "练习 2.3.8"
    给出以下每种情况的例子，或通过引用适当的定理说明这样的请求是不可能的:
    
    (a) 序列 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) ，两者都发散，但它们的和 \(\left( {{x}_{n} + {y}_{n}}\right)\) 收敛；
    
    (b) 序列 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) ，其中 \(\left( {x}_{n}\right)\) 收敛， \(\left( {y}_{n}\right)\) 发散，且 \(\left( {{x}_{n} + }\right.\)  \(\left. {y}_{n}\right)\) 收敛；
    
    (c) 一个收敛的序列 \(\left( {b}_{n}\right)\) ，对于所有 \(n\) 满足 \({b}_{n} \neq  0\) ，使得 \(\left( {1/{b}_{n}}\right)\) 发散；
    
    (d) 一个无界序列 \(\left( {a}_{n}\right)\) 和一个收敛序列 \(\left( {b}_{n}\right)\) ，其中 \(\left( {{a}_{n} - }\right.\)  \(\left. {b}_{n}\right)\) 有界；
    
    (e) 两个序列 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) ，其中 \(\left( {{a}_{n}{b}_{n}}\right)\) 和 \(\left( {a}_{n}\right)\) 收敛但 \(\left( {b}_{n}\right)\) 不收敛。

(a) $x_n=n$，$y_n=-n$ 是可能的。

(b) 由代数极限定理，两个收敛数列的和或差一定收敛，所以不可能。

(c) $b_n=\displaystyle\frac{1}{n}$ 是可能的。

(d) 用绝对值不等式 $|a_n|=|(a_n-b_n)+b_n|\leq |a_n-b_n|+|b_n|$，如果 $\{a_n-b_n\}$ 和 $\{b_n\}$ 都有界，则 $\{a_n\}$ 必有界，所以不可能。

(e) $a_n=0$ 是可能的。

<br/>


!!! question "练习 2.3.9"
    如果所有不等式都假设为严格不等式，定理 2.3.4 是否仍然成立？例如，如果我们假设一个收敛序列 \(\left( {x}_{n}\right)\) 对所有 \(n \in  \mathbb{N}\) 满足 \({x}_{n} > 0\) ，我们可以得出关于极限的什么结论？

不成立。

如果 $x_n>0$，沿用定理的证明，则极限 $x=0$ 的时候也能成立。所以 $x\geq 0$。

<br/>


!!! question "练习 2.3.10"
    如果 \(\left( {a}_{n}\right)  \rightarrow  0\) 且 \(\left| {{b}_{n} - b}\right|  \leq  {a}_{n}\) ，则证明 \(\left( {b}_{n}\right)  \rightarrow  b\) 。

由题，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|a_n|<\varepsilon$，所以 $|b_n-b|\leq |a_n|<\varepsilon$。所以 $\displaystyle\lim_{n\to\infty}b_n=b$。

<br/>


!!! question "练习 2.3.11"
    (切萨罗均值)。证明如果 \(\left( {x}_{n}\right)\) 是一个收敛序列，则由平均值给出的序列
    
    $$
    {y}_{n} = \frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n}
    $$
    
    也收敛到相同的极限。
    
    举一个例子说明，即使 \(\left( {x}_{n}\right)\) 不收敛，平均值序列 \(\left( {y}_{n}\right)\) 也可能收敛。

<a id="4">极限平均值定理与反向情况下的反例</a>

假设 $\displaystyle\lim_{n\to\infty}x_n=x$，考虑将平均值转化为极限的形式：

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|
$$

我们以 $N$ 为界限进行拆分：假设 $N$ 是满足对 $\forall\ n>N$，有 $|x_n-x|<\varepsilon$ 的正整数，则有

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|<\frac{1}{n}(\sum_{k=1}^N|x_k-x|+(n-N)\varepsilon)
$$

再利用有界性，$\exists\ M>0$，使得对 $\forall\ k\in \mathbb{N^+}$，有 $|x_k|<M$，则有 $|x_k-x|\leq |x_k|+|x|<M+|x|$。所以

$$\begin{align*}
    |\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|&<\frac{1}{n}(N(M+|x|)+(n-N)\varepsilon)\\
    &<\frac{1}{n}(N(M+|x|))+\varepsilon
\end{align*}
$$

当然，$\exists\ N_1\in \mathbb{N^+}$，$N_1>N$，使得对 $\forall\ n>N_1$，有 $\displaystyle\frac{1}{n}(N(M+|x|))<\varepsilon$，所以

$$
|\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|<2\varepsilon
$$

所以 $\displaystyle\lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=x=\displaystyle\lim_{n\to\infty}x_n$。

对于下一个问题，我先考虑了 $\{x_n\}$ 的增长度小于 $n$ 的情况，比如 $x_n=\sqrt{n}$，但这并不能说明问题。后来我尝试反向证明，得到了这样一串式子：

$$
\begin{align*}
     |\displaystyle\frac{x_1+x_2+\cdots+x_n}{n}-x|&=\frac{1}{n}|\displaystyle\sum_{k=1}^n(x_k-x)|\\
     &\leq \frac{1}{n}\displaystyle\sum_{k=1}^n|x_k-x|\\
     &\leq \frac{1}{n}|x_n-x|\\
     &<\frac{1}{n}n\varepsilon=\varepsilon
\end{align*}
$$

这个式子是不成立的，但它的确给了我启发：对于 $\{x_n\}$ 单调递增（趋近于 $x$）的情况， 貌似可以符合上面的条件。我没有直接证明这一点，但我想到了另外一种思路来构造反例 $\{x_n\}$：让它左右跳动，连上面的式子都不成立。比如 $\displaystyle x_n=(-1)^n$。不难得出 $\displaystyle\lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=0$，但是 $\{x_n\}$ 发散。

<br/>


!!! question "练习 2.3.12"
    考虑双索引数组 \({a}_{m,n} = m/\left( {m + n}\right)\) 。
    
    (a) 直观地说， \(\mathop{\lim }\limits_{{m,n \rightarrow  \infty }}{a}_{m,n}\) 应该代表什么？计算“迭代”极限
    
    $$
    \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\lim }\limits_{{m \rightarrow  \infty }}{a}_{m,n}\;\text{ and }\;\mathop{\lim }\limits_{{m \rightarrow  \infty }}\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{m,n}.
    $$
    
    (b) 以定义2.2.3的风格为以下陈述制定一个严格的定义
    
    $$
    \mathop{\lim }\limits_{{m,n \rightarrow  \infty }}{a}_{m,n} = l
    $$

(a) 直观来讲，$\displaystyle\lim_{m,n\to\infty}a_{m,n}$ 应当表示 $m,n$ 同时趋于无穷时 $\{a_n\}$ 的极限。

$\displaystyle\lim_{n\to\infty}\displaystyle\lim_{m\to\infty}a_{m,n}=\displaystyle\lim_{n\to\infty}1=1$，$\displaystyle\lim_{m\to\infty}\displaystyle\lim_{n\to\infty}a_{m,n}=\displaystyle\lim_{m\to\infty}0=0$。

所以上面的直观难以给我们一个准确的答案，我们需要更清晰的定义，例如规定 $m,n$ 的取极限顺序。

(b) 若对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，对 $\forall\ n>N_1$，$m>N_2$，$|a_{m,n}-b_m|<\varepsilon$，$|b_m-l|<\varepsilon$，则有 $\displaystyle\lim_{m,n\to\infty}a_{m,n}=l$。

---

## 习题 2.4 单调收敛定理与无穷级数初探

!!! question "练习 2.4.1"
    通过证明如果级数 \(\mathop{\sum }\limits_{{n = 0}}^{\infty }{2}^{n}{b}_{{2}^{n}}\) 发散，那么 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\) 也发散，来完成定理2.4.6的证明。示例2.4.5可能是一个有用的参考。

若级数 $\displaystyle\sum_{n=0}^{\infty}2^nb_{2^n}$ 发散，则考虑在 $\displaystyle\sum_{n=1}^{\infty}b_n$ 中构造该级数以证明其发散。

固定 $m\in \mathbb{N^+}$，则总存在 $t\in \mathbb{N}$ 使 $2^t\leq m$，因此

$$
\begin{align*}
    \displaystyle\sum_{n=1}^{m}b_n&=b_1+b_2+\cdots+b_m\\
    &\geq b_1+b_2+\cdots+b_{2^t}\\
    &=b_1+b_2+(b_3+b_4)+\cdots+(b_{2^{t-1}+1}+b_{2^{t-1}+2}+\cdots+b_{2^t})\\
    &\geq b_1+b_2+2b_4+4b_8+\cdots+2^{t-1}b_{2^t}\\
    &=\displaystyle\frac{1}{2}b_1+\displaystyle\frac{1}{2}\displaystyle\sum_{n=0}^{t}2^nb_{2^n}\\
    &\geq \displaystyle\frac{1}{2}\displaystyle\sum_{n=0}^{t}2^nb_{2^n}.
\end{align*}
$$

对 $\forall\ G>0$，$\exists\ t\in \mathbb{N}$ 使 $\displaystyle\sum_{n=0}^{t}2^nb_{2^n}>2G$，即 $\exists\ m\in \mathbb{N^+}$ 使 $\displaystyle\sum_{n=1}^{m}b_n>G$。

所以 $\displaystyle\sum_{n=1}^{\infty}b_n$ 发散。

<br/>

$2.4.2.$<a id="2.4.2"></a>

(a) 计算可得 $x_2=1<x_1$，$x_3=\displaystyle\frac{1}{3}<x_2$，$\cdots$ 大胆猜想 $\{x_n\}$ 是单调递减的，配合单调有界定理证明其收敛。

假设 $x_{n+1}<x_n$，即 $\displaystyle\frac{1}{4-x_n}<x_n$，整理得 $\displaystyle\frac{x_n^2-4x_n+1}{4-x_n}<0$，考虑到原题中 $x_1=3<4$，可得 $x_n^2-4x_n+1<0$。设 $x^2-4x+1=0$ 两根分别为 $t_1<t_2$，那么 $x_n\in (t_1,t_2)$。

下面证明 $x_{n+2}<x_{n+1}$，利用同样的方法化简得到 $\displaystyle\frac{x_{n+1}^2-4x_{n+1}+1}{4-x_{n+1}}<0$。下面判断这个不等式的正负。

要判断它的正负，关键是求解 $x_{n+1}$ 的范围，而 $x_{n+1}$ 的范围又由 $x_{n}$ 所控制，所以我们考虑 $x_n\in (t_1,t_2)$ 时对 $x_{n+1}$ 的影响。

分析 $x^2-4x+1=0$ 解的范围，可知 $0<t_1<t_2<4$。由于 $x_{n+1}=\displaystyle\frac{1}{4-x_n}$，所以 $x_{n+1}\in (\displaystyle\frac{1}{4-t_1},\displaystyle\frac{1}{4-t_2})$。此时直接化简有些困难，于是我思考了这一方程的来历，发现这一方程就是 $x=\displaystyle\frac{1}{4-x}$ 的变形，于是 $x_{n+1}\in (t_1,t_2)$。

上面由 $x_{n+2}<x_{n+1}$ 得到的那个不等式因为形式完全一致，所以成立。

所以 $x_{n+2}<x_{n+1}$。

由数学归纳法可得 $\{x_n\}$ 单调递减。又因为 $x_n\in (t_1,t_2)$ 对 $\forall\ n\in \mathbb{N^+}$ 成立，所以 $\{x_n\}$ 有界，由单调有界定理可知其收敛。

(b) $\displaystyle\lim_{n\to\infty}x_n$ 与 $\displaystyle\lim_{n\to\infty}x_{n+1}$ 的意义是相同的。下面我们用极限定义严格地说明一下这一点。

设 $\displaystyle\lim_{n\to\infty}x_n=A$，即对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$, $|x_n-A|<\varepsilon$。取 $N_2=N_1-1$，则对 $\forall\ n>N_2$，$|x_{n+1}-A|<\varepsilon$。所以 $\displaystyle\lim_{n\to\infty}x_{n+1}=A$。

反向的证明可以使用同样的操作。

对 (a) 中递推公式左右取极限，可得 $A=\displaystyle\frac{1}{4-A}$，解得 $A=2-\sqrt{3}$ 或 $A=2+\sqrt{3}$，考虑原式里 $x_n$ 始终小于 $3$ 的事实，由序极限定理可知 $A\leq 3<2+\sqrt{3}$，所以 $\displaystyle\lim_{n\to\infty}x_n=A=2-\sqrt{3}$。

<br/>


!!! question "练习 2.4.3"
    按照练习2.4.2的模型，证明由 \({y}_{1} = 1\) 和 \({y}_{n + 1} = 4 - 1/{y}_{n}\) 定义的序列收敛并求出极限。

使用 [$2.4.2$](#2.4.2) 中完全一致的方法就可以得出结论。

其一：$y_n$ 是单调递增的，且 $y_n<4$，所以 $y_n$ 收敛。

其二：两边同时取极限得到 $A=4-\displaystyle\frac{1}{A}$，其实这个方程的两解跟上一题完全一样，不过这次因为 $y_n>1$ 是恒成立的，所以 $\displaystyle\lim_{n\to\infty}y_n=A=2+\sqrt{3}$。

<br/>


!!! question "练习 2.4.4"
    证明
    
    $$
    \sqrt{2},\sqrt{2\sqrt{2}},\sqrt{2\sqrt{2\sqrt{2}}},\ldots
    $$
    
    收敛并求出极限。

把它写成数列形式如下：

$$
    x_{n+1}=\sqrt{2x_n},\quad x_1=\sqrt{2}\,.
$$

先试探数列单调性，假设 $x_{n+1}>x_n$，化简得到 $x_n<2$，从而 $x_{n+1}=\sqrt{2x_n}<2$，所以 $x_{n+2}=\sqrt{2x_{n+1}}<x_{n+1}$。又因为 $x_1=\sqrt{2}<2$，假设成立，数列单调递增。

又因为对 $\forall\ n\in \mathbb{N^+}$，$\sqrt{2}\leq x_n<2$，由单调有界定理知其收敛。

两边同时取极限得到 $A=\sqrt{2A}$，解得 $A=2$ 或 $A=0$，又因为 $\sqrt{2}\leq x_n$，由序极限定理 $\displaystyle\lim_{n\to\infty}x_n=A=2$。

<br/>


!!! question "练习 2.4.5"
    (计算平方根)。设 \({x}_{1} = 2\) ，并定义
    
    $$
    {x}_{n + 1} = \frac{1}{2}\left( {{x}_{n} + \frac{2}{{x}_{n}}}\right) .
    $$
    
    (a) 证明 \({x}_{n}^{2}\) 总是大于2，然后利用这一点证明 \({x}_{n} - {x}_{n + 1} \geq  0\) 。由此得出结论 \(\lim {x}_{n} = \sqrt{2}\) 。
    
    (b) 修改序列 \(\left( {x}_{n}\right)\) 使其收敛到 \(\sqrt{c}\) 。

(a) 若 $x_n>0$，则 $x_{n+1}=\displaystyle\frac{1}{2}(x_n+\frac{2}{x_n})>0$。考虑均值不等式 

$$
    \displaystyle\frac{1}{2}(x_n+\frac{2}{x_n})\geq \sqrt{x_n\cdot\frac{2}{x_n}}=\sqrt{2}
$$

所以 $x_{n+1}\geq \sqrt{2}$。又因为 $x_1=2$，$x_n\neq \sqrt{2}$ 时 $x_{n+1}\neq \sqrt{2}$，所以无法取等， $x_n^2>2$。

下面借助这一点证明其单调性。令 $x_{n+1}-x_n$ 得到

$$
    x_{n+1}-x_n=\displaystyle\frac{1}{2}(x_n+\displaystyle\frac{2}{x_n})-x_n=\displaystyle\frac{2-x_n^2}{2x_n}<0
$$

所以 $\{x_n\}$ 单调递减。由之前不等式知其有界，由单调有界定理可知其收敛。

两边同时取极限，利用 $x_n>0$ 舍去一根解出 $\displaystyle\lim_{n\to\infty}x_n=\sqrt{2}$。

(b) $x_{n+1}=\displaystyle\frac{1}{2}(x_n+\displaystyle\frac{c}{x_n})$ 其中 $c>0$。再规定 $x_1>0$。

<br/>


!!! question "练习 2.4.6"
    (上极限)。设 \(\left( {a}_{n}\right)\) 是一个有界序列。
    
    (a) 证明由 \({y}_{n} = \sup \left\{  {{a}_{k} : k \geq  n}\right\}\) 定义的序列收敛。
    
    (b) \(\left( {a}_{n}\right)\) 的上极限，或 \(\limsup {a}_{n}\) ，定义为
    
    $$
    \lim \sup {a}_{n} = \lim {y}_{n},
    $$
    
    其中 \({y}_{n}\) 是本练习部分 (a) 中的序列。为 \(\liminf {a}_{n}\) 提供一个合理的定义，并简要解释为什么它对任何有界序列总是存在。
    
    (c) 证明对于每个有界序列 \(\liminf {a}_{n} \leq  \limsup {a}_{n}\) ，并给出一个不等式严格成立的序列示例。
    
    证明 \(\liminf {a}_{n} = \limsup {a}_{n}\) 当且仅当 \(\lim {a}_{n}\) 存在。在这种情况下，三者共享相同的值。

(a) 用单调有界定理证明。

如果对 $\forall\ n\in \mathbb{N^+}$，$\exists\ G>0$ 使得 $|x_n|<G$，则 $|y_n|<G$ 同样成立，故 $\{y_n\}$ 有界。

若 $\exists\ k>n$ 使 $x_k\geq x_n$ 则有 $y_n=y_{n+1}$，否则 $y_n=x_n>y_{n+1}$，所以 $\{y_n\}$ 单调递减。

由单调有界定理可知 $\{y_n\}$ 收敛。

(b) 令 $z_n=\inf \{a_k:k\geq n\}$，$\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}z_n$。

同 (a)，它是单调的，又因为它有界，所以它收敛。

(c) $z_n\leq a_n\leq y_n$，得出 $z_n\leq y_n$，利用序极限定理即可证明。

例如 $a_n=(-1)^n$ 时不等式会严格成立。

$\Rightarrow$) 若 $\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}\sup a_n$，则由夹逼定理可知 $\{a_n\}$ 收敛。

$\Leftarrow$) 若 $\{a_n\}$ 收敛，设 $\displaystyle\lim_{n\to\infty}a_n=A$。

首先，$\{a_n\}$ 有界，$\displaystyle\lim_{n\to\infty}z_n$ 与 $\displaystyle\lim_{n\to\infty}y_n$ 均存在。

然后，对 $\forall\ \varepsilon>0$，$\exists\ N>0$ 使得对 $\forall\ n>N$，$|a_n-A|<\displaystyle\frac{\varepsilon}{2}$，即 $A-\displaystyle\frac{\varepsilon}{2}<a_n<A+\displaystyle\frac{\varepsilon}{2}$。

若 $\exists\ k>N$ 使得 $z_k<A-\displaystyle\frac{\varepsilon}{2}$，则由下确界的性质可知 $\exists\ m\geq k$ 使得 $a_m\leq A-\displaystyle\frac{\varepsilon}{2}$，矛盾，所以：

$$
    A-\varepsilon<A-\displaystyle\frac{\varepsilon}{2}\leq z_n\leq a_n<A+\varepsilon\\
    |z_n-A|<\varepsilon
$$

所以 $\displaystyle\lim_{n\to\infty}z_n=A$。同理反向可证 $\displaystyle\lim_{n\to\infty}y_n=A$。

综上，$\displaystyle\lim_{n\to\infty}\inf a_n=\displaystyle\lim_{n\to\infty}\sup a_n$ 当且仅当 $\displaystyle\lim_{n\to\infty}a_n$ 存在。

---

## 习题 2.5 子列与 Bolzano-Weierstrass 定理

!!! question "练习 2.5.1"
    证明定理2.5.2。

设 $\displaystyle\lim_{n\to\infty}a_n=L$，则对 $\forall\ \varepsilon>0$，$\exists\ N>0$，使得 当 $n>N$ 时，$|a_n-L|<\varepsilon$。考虑子列 $a_{n_k}$，由于 $n_k\geq k$，所以对 $\forall\ k>N$，有 $n_k>N$，从而 $|a_{n_k}-L|<\varepsilon$。因此 $\displaystyle\lim_{k\to\infty}a_{n_k}=L$。

<br/>


!!! question "练习 2.5.2"
    (a) 证明如果一个无穷级数收敛，则结合律成立。假设 \({a}_{1} + {a}_{2} + {a}_{3} + {a}_{4} + {a}_{5} + \cdots\) 收敛到极限 \(L\) (即，部分和序列 \(\left( {s}_{n}\right)  \rightarrow  L\) )。证明任何对项的重组
    
    $$
    \left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{{n}_{1}}}\right)  + \left( {{a}_{{n}_{1} + 1} + \cdots  + {a}_{{n}_{2}}}\right)  + \left( {{a}_{{n}_{2} + 1} + \cdots  + {a}_{{n}_{3}}}\right)  + \cdots
    $$
    
    都会导致一个同样收敛到 \(L\) 的级数。
    
    (b) 将此结果与第2.1节末尾讨论的例子进行比较，其中无穷加法被证明不满足结合律。为什么我们在(a)中的证明不适用于这个例子？

(a) 定义 $s_{n_k}=\displaystyle\sum_{i=1}^{n_k}a_i$，$k\in \mathbb{N^+}$，则 $\{s_{n_k}\}$ 是 $\{s_n\}$ 的子列。所以 $\displaystyle\lim_{k\to\infty}s_{n_k}=\displaystyle\lim_{n\to\infty}s_n=L$。

别看错了，这不是黎曼重排定理，事实上，级数的结合律只是把相邻的数加在一起而已，甚至没有改变顺序，所以敛散性和原级数应该一致。

举个例子，$\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2}+\displaystyle\frac{1}{4}+\displaystyle\frac{1}{4}+\cdots=\left(\displaystyle\frac{1}{2}+\displaystyle\frac{1}{2}\right)+\left(\displaystyle\frac{1}{4}+\displaystyle\frac{1}{4}\right)+\cdots=1+\displaystyle\frac{1}{2}+\cdots$。

(b) 因为那个级数是不收敛的。

<br/>


!!! question "练习 2.5.3"
    给出以下每种情况的例子，或论证这样的请求是不可能的。
    
    (a) 一个不包含0或1作为项的序列，但包含收敛到这些值的子列。
    
    (b) 一个单调但发散的序列，且具有收敛的子列。
    
    (c) 一个包含收敛到无限集 \(\{ 1,1/2,1/3,1/4,1/5,\ldots \}\) 中每个点的子列的序列。
    
    一个具有收敛子列的无界序列。
    
    一个具有有界子列但不包含任何收敛子列的序列。

(a) 构造交替子列，极限分别为 $0,1$ 即可。例如 $\{\displaystyle\frac{1}{2n}\}$ 和 $\{1-\displaystyle\frac{1}{2n}\}$。放 $2n$ 的目的是防止 $0,1$ 出现在其中。

(b) 这是不可能的。不妨设它单调递增，因为原数列的任意序列到最后都会变得很大，因此发散，下面我们来证明这一点。

其实要证的就是对 $\forall\ G>0$，存在 $N>0$，使得当 $n\geq N$ 时，$a_n>G$。首先，$\exists\ N>0$ 使得 $a_N>G$，是无误的，然后由原数列单调递增，$\forall\ n\geq N$，都有 $a_n\geq a_N>G$，从而对任何一个 $\{a_{n_k}\}$ 子列都有 $k>N$ 时，$a_{n_k}>G$，因此发散。

(c) 可能。考虑一种分别构造的方式，使得数列里面 $1,1/2,1/3,\ldots$ 都出现无穷多次。

直接按顺序排会让它们无法出现第二次，因此尝试交替排列，例如 $\{1,1/2,1,1/2,1/3,1,1/2,1/3,1/4,\ldots\}$，符合要求。

可能。构造两个子列交替排列，一个收敛，一个发散。

不可能，因为由 Bolzano-Weierstrass 定理，这个有界子列里存在一个更小的收敛子列。

<br/>

$2.5.4.$<a id="2.5.4."></a>

由 Bolzano-Weierstrass 定理，有界数列一定有收敛子列，但是这并不意味着所有所有子列都是收敛的，所以想通过数列每项都属于某个收敛子列来证明数列收敛是行不通的。

那我们来考察一下，假如 $\{a_n\}$ 有界，且要么子列不收敛，要么子列都收敛到同一个极限 $a$ 呢?

比如说 $(-1)^n$，如果它是 $\{a_n\}$ 的子列，那么它确实不收敛。但是它也有自己的两个子列，并且这两个子列收敛到的极限不相同，那么就矛盾了。

所以，如果子列都收敛到同一个极限 $a$，那么 $\{a_n\}$ 就不能有不收敛的子列。事实上，因为 $\{a_n\}$ 有界，那么子列也有界，符合 Bolzano-Weierstrass 定理的要求，所以可以利用这个定理在发散子列里面创造两个更小的收敛子列，从而导致矛盾。这就是我们的证明逻辑。

我们用反证法。假设 $\{a_n\}$ 发散，因为 $\{a_n\}$ 有界，故由 Bolzano-Weierstrass 定理知，$\{a_n\}$ 有收敛子列，设该子列为 $\{a_{n_k}\}$，且 $\displaystyle\lim_{k\to\infty}a_{n_k}=a$。

下面我们创造第二个收敛子列，并且让它的极限不等于 $a$。因为 $\{a_n\}$ 发散，所以肯定有无穷多项不在 $\{a_n\}$ 的邻域里面，不然 $\{a_n\}$ 就收敛了。又因为这无穷多项是有界的，所以它肯定有一个不收敛到 $a$ 的子列，这样就得出了矛盾。用数学语言来说就是：

 $\exists\ \varepsilon>0$，使得对 $\forall\ N>0$，$\exists\ n>N$，使得 $|a_n-a|\geq \varepsilon$。也就是 $a_n\notin (a-\varepsilon,a+\varepsilon)$。

取 $n_1>N$ 满足上述条件，由 $N$ 的任意性，可以取到 $n_2>n_1$ 满足上述条件。以此类推，对 $\forall\ k\in \mathbb{N^+}$，都可以取到 $n_{k+1}>n_{k}$ 满足上述条件。所以我们得到了 $\{a_n\}$ 的一个子列 $\{a_{n_k}\}$。由于 $\{a_n\}$ 有界，所以 $\{a_{n_k}\}$ 也有界，由 Bolzano-Weierstrass 定理知，$\{a_{n_k}\}$ 有收敛子列，设该子列为 $\{a_{n_{k_j}}\}$，且 $\displaystyle\lim_{j\to\infty}a_{n_{k_j}}=b$。由于 $\forall\ k\in \mathbb{N^+}$，都有 $a_{n_k}\notin (a-\varepsilon,a+\varepsilon)$，所以由序极限定理 $b\notin (a-\varepsilon,a+\varepsilon)$，从而 $b\neq a$，这就得到了矛盾。

综上所述，$\{a_n\}$ 必须收敛。由收敛数列子列的极限和原数列极限相同可知 $\displaystyle\lim_{n\to\infty}a_n=a$。

<br/>


!!! question "练习 2.5.5"
    将例 2.5.3 中证明的结果推广到 \(\left| b\right|  < 1\) 的情况。证明当 \(- 1 < b < 1\) 时， \(\lim \left( {b}^{n}\right)  = 0\) 成立。

可以看出，$-1<b<0$ 时，$\{b^n\}$ 正负交错并不单调。但是我们可以把它的正负项分别提取成两个子列，并且这两个子列都收敛到 $0$。再利用 [$2.3.5.$](#2.3.5.) 的结论，我们就可以进行证明。

正数项子列的收敛性书上已证，现在证明负数项子列的收敛性。令 $c_n=b^{2n-1}$，则 $\{c_n\}$ 为 全体负数项组成的子列。因为 $-1<b<0$，所以 $b<b^3<b^5<\cdots<0$，由单调有界定理 $\{c_n\}$ 收敛。记 $\displaystyle\lim_{n\to\infty}c_n=c$，则 $\{c_n\}$ 的子列 $\{c_{2n}\}$ 也应当收敛到 $c$，而 $c_{2n}=b^{4n-1}=b(c_n)^2$，所以 $c=bc^2$，从而 $c=0$ 或 $\displaystyle\frac{1}{b}$，但是 $\displaystyle\frac{1}{b}<-1<c_n$，所以 $c=0$。

所以这两个子列的极限都为 $0$。由于这两个子列交替构成了 $\{b^n\}$，由 [$2.3.5.$](#2.3.5.) 的结论可知，$\{b^n\}$ 也收敛到 $0$。


<br/>


!!! question "练习 2.5.6"
    设 \(\left( {a}_{n}\right)\) 是一个有界序列，并定义集合
    
    $$
    S = \left\{  {x \in  \mathbb{R} : x < {a}_{n}\text{ for infinitely many terms }{a}_{n}}\right\}  .
    $$
    
    证明存在一个子列 \(\left( {a}_{{n}_{k}}\right)\) 收敛于 \(s = \sup S\) 。(这是利用完备性公理对Bolzano-Weierstrass定理的直接证明。)

只需要证明 $s$ 的任意邻域都存在 $\{a_n\}$ 中的项，便能构造出收敛到 $s$ 的子列。

假设存在 $\varepsilon>0$，使得 $\forall\ n\in \mathbb{N^+}$，$a_n\notin (s-\varepsilon,s+\varepsilon)$。那么 $\{a_n\}$ 中就有无限多项大于 $s+\varepsilon$，或小于 $s-\varepsilon$。

若有无限多项大于 $s+\varepsilon$，则 $x=s+\displaystyle\frac{\varepsilon}{2}\in S$，与 $s=\sup S$ 矛盾。

若只有无限多项小于 $s-\varepsilon$，则不存在 $x>s-\varepsilon$，使得 $x\in S$，与 $s=\sup S$ 矛盾。

所以 $\forall\ \varepsilon>0$，$\exists\ n\in \mathbb{N^+}$，使得 $a_n\in (s-\varepsilon,s+\varepsilon)$。由此便能构造出收敛到 $s$ 的子列。

首先，$\exists\ n_1\in \mathbb{N^+}$，使得 $a_{n_1}\in (s-1,s+1)$；

然后，$\exists\ n_2\in \mathbb{N^+}$，$n_2>n_1$，使得 $a_{n_2}\in (s-\displaystyle\frac{1}{2},s+\displaystyle\frac{1}{2})$；

依此类推，对 $\forall\ k\in \mathbb{N^+}$，$\exists\ n_k\in \mathbb{N^+}$，$n_k>n_{k-1}$，使得 $a_{n_k}\in (s-\displaystyle\frac{1}{k},s+\displaystyle\frac{1}{k})$。

这样便构造出了 $\{a_{n_k}\}$。

对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，$N>\displaystyle\frac{1}{\varepsilon}$，对 $\forall\ k>N$，有 $|a_{n_k}-s|<\displaystyle\frac{1}{k}<\varepsilon$。

所以 $\displaystyle\lim_{k\to\infty}a_{n_k}=s$。

---

## 习题 2.6 Cauchy 准则

!!! question "练习 2.6.1"
    给出以下每种情况的例子，或者论证这样的请求是不可能的。
    
    (a) 一个不是单调的Cauchy列(Cauchy sequence)。
    
    (b) 一个不是Cauchy的单调序列。
    
    (c) 一个具有发散子列的Cauchy列。
    
    (d) 一个包含Cauchy子列的无界序列。

(a) $a_n=(-1)^n\displaystyle\frac{1}{n}$。

(b) $a_n=n$。

(c) 不存在，因为柯西列一定收敛，所有子列都必须收敛。

(d) 让 $\{1\}$ 和 $\{n\}$ 交替组成  $\{a_n\}$ 即可。

<br/>


!!! question "练习 2.6.2"
    为定理2.6.2提供证明。

定理 $2.6.2$ 的证明利用了原数列的极限作为中间量，关键如下：在 $n$ 足够大时，每个 $a_n$ 都靠近极限 $a$ $\Rightarrow$ $a_n$ 之间都相互靠近。接下来定量证明即可 $\forall\ \varepsilon>0$，$\exists\ N>0$，$\forall\ m,n>N$，$|a_m-a|<\varepsilon$，$|a_n-a|<\varepsilon$，也就是说，$a_m,a_n$ 最多都只离 $a$ 有 $\varepsilon$ 的距离，因此它们两之间最多也只有 $2\varepsilon$ 的距离，用三角不等式得出 $   |a_m-a_n|\leq|a_m-a|+|a_n-a|<2\varepsilon$。这就证明了收敛数列都是柯西列。

<br/>


!!! question "练习 2.6.3"
    (a) 解释以下伪Cauchy性质与Cauchy列的正确定义有何不同:一个序列 \(\left( {s}_{n}\right)\) 是伪Cauchy的，如果对于所有 \(\varepsilon  > 0\) ，存在一个 \(N\) ，使得如果 \(n \geq  N\) ，则 \(\left| {{s}_{n + 1} - {s}_{n}}\right|  < \varepsilon\) 。
    
    (b) 如果可能，给出一个发散序列 \(\left( {s}_{n}\right)\) 的例子，该序列是伪Cauchy的。

(a) 伪柯西列的定义仅要求相邻项的距离足够小，而柯西列的定义要求任意两项的距离都足够小。

(b) 一个发散序列是有可能是伪柯西列的，对它的一个直观想法是：它是单调递增的，在增长量越来越小（趋于 $0$）的情况下无限增大。由于 $\{n\}$ 是一个典型的增长量不变的数列，所以我们可以考虑那些增长小于 $\{n\}$ 的数列，比如 $\{\sqrt{n}\}$。因为 $\displaystyle\lim_{n\to\infty}(\sqrt{n+1}-\sqrt{n})=\lim_{n\to\infty}\frac{1}{\sqrt{n+1}+\sqrt{n}}=0$，所以 $\{\sqrt{n}\}$ 是一个伪柯西列。

<br/>


!!! question "练习 2.6.4"
    假设 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) 是Cauchy列。使用三角不等式论证证明 \({c}_{n} = \left| {{a}_{n} - {b}_{n}}\right|\) 是Cauchy的。

$|c_m-c_n|=\big||a_m-b_m|-||a_n-b_n|\big|\leq |(a_m-a_n)-(b_m-b_n)|\leq |a_m-a_n|+|b_m-b_n|$，依此即可证明。

<br/>


!!! question "练习 2.6.5"
    如果 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 是Cauchy列，那么证明 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是Cauchy列的一个简单方法是使用Cauchy准则。根据定理 2.6.4， \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 必须是收敛的，而代数极限定理则意味着 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是收敛的，因此是Cauchy列。
    
    (a) 给出一个直接论证，证明 \(\left( {{x}_{n} + {y}_{n}}\right)\) 是Cauchy列，而不使用Cauchy准则或代数极限定理。
    
    (b) 对乘积 \(\left( {{x}_{n}{y}_{n}}\right)\) 做同样的论证。

(a) 与 $2.6.4.$ 类似，令 $z_n=x_n+y_n$，则有 $|z_m-z_n|=|(x_m+y_m)-(x_n+y_n)|\leq |x_m-x_n|+|y_m-y_n|$，依此即可证明。

(b) 令 $w_n=x_ny_n$，则有 $|w_m-w_n|=|x_my_m-x_ny_n|=|x_my_m-x_ny_m+x_ny_m-x_ny_n|=|(x_m-x_n)y_m+(y_m-y_n)x_n|\leq |y_m||x_m-x_n|+|x_n||y_m-y_n|$。

对 $\forall\ \varepsilon>0$，$\exists\ N_1,N_2\in \mathbb{N^+}$，对 $\forall\ m,n\geq N_1$，$|x_m-x_n|<\varepsilon$；对 $\forall\ m,n\geq N_2$，$|y_m-y_n|<\varepsilon$。取 $N\in \mathbb{N^+}$，$N>\max\{N_1,N_2\}$，则对 $\forall\ m,n\geq N$，上述两式均成立。

又因为柯西列是有界的，所以 $\exists\ M_1,M_2>0$，对 $\forall\ n\in \mathbb{N^+}$，$|x_n|\leq M_1$，$|y_n|\leq M_2$。因此对 $\forall\ m,n\geq N$，有 $|w_m-w_n|<M_2\varepsilon+M_1\varepsilon=(M_1+M_2)\varepsilon$。这就证明了 $\{w_n\}$ 是柯西列。

<br/>

$2.6.6.$<a id="5">实数几大基本定理的互证</a>

(a) 闭区间套定理 $\Rightarrow$ 完备性公理

闭区间套定理其实揭示了实数的连续性，也就是说，实数轴上不存在空隙。使用无限的闭区间嵌套，在闭区间长度减小（趋于 $0$）的情况下，一定会正好落在某个实数上，这就像拿越来越细的刀去切实数轴，当它的厚度趋于 $0$ 时，一定会切到某个实数上。

从刀的比喻拓展来看，闭区间套定理最终能够把实数轴切成两个部分，而完备性公理正好就描述了这一性质：通过上确界的存在唯一性，将实数轴上所有点都划分成要么属于集合，要么属于上界的两部分（当然这里不严谨，我们只考虑切右边即上确界，下确界在这里忽略了）。

所以它们两个说明的是同一个性质，下面考虑用数学语言严谨地证明。

考虑有上界的非空集合 $A$。如果 $a\in A$ 为它的上界，那么 $a=\sup A$。具体来讲，任何一个元素都小于等于 $a$，而且 $a-\varepsilon<a$，满足上确界两条性质。实际上这个在第一章证明过了。

如果任何一个元素都不是 $A$ 的上界，那么这时我们就要用闭区间套定理把 $\sup A$ “切”出来了。我们可以仿照书上 Bolzano-Weierstrass 定理的证明思路，这样构造：

(i) 闭区间的左端点属于 $A$，右端点是 $A$ 的上界。

(ii) 下一个闭区间的长度是上一个的 $\displaystyle\frac{1}{2}$，以达到长度趋于 $0$ 的效果。

如此一来，闭区间“切出来”的实数应该就是“属于”和“上界”的分界点，即 $\sup A$。

理论存在，操作开始：

设 $A$ 的一个上界是 $M$，且有 $a\in A$。因为任何元素都不是 $A$ 的上界，所以 $a<M$。令 $a_1=a$，$b_1=M$，构造第一个闭区间 $[a_1,b_1]$。

现在，考虑 $[a_1,b_1]$ 的中点 $c_1=\displaystyle\frac{a_1+b_1}{2}$。按照这个形式操作:

(i) 若 $c_1$ 不是 $A$ 的上界，则令 $a_2=c_1$，$b_2=b_1$，构造下一个闭区间 $[a_2,b_2]$。

(ii) 若 $c_1$ 是 $A$ 的上界，则令 $a_2=a_1$，$b_2=c_1$，构造下一个闭区间 $[a_2,b_2]$。

$c_1$ 能且仅能满足其一，由此可得到下一个闭区间 $[a_2,b_2]$。

接下来，考虑 $[a_2,b_2]$ 的中点 $c_2=\displaystyle\frac{a_2+b_2}{2}$。按照完全相同的形式操作...

也就是说，对 $\forall\ n\in \mathbb{N^+}$，我们对 $[a_n,b_n]$ 的中点 $c_n=\displaystyle\frac{a_n+b_n}{2}$ 进行相同的操作；

(i) 若 $c_n$ 不是 $A$ 的上界，则令 $a_{n+1}=c_n$，$b_{n+1}=b_n$，构造下一个闭区间 $[a_{n+1},b_{n+1}]$。

(ii) 若 $c_n$ 是 $A$ 的上界，则令 $a_{n+1}=a_n$，$b_{n+1}=c_n$，构造下一个闭区间 $[a_{n+1},b_{n+1}]$。

得到下一个闭区间 $[a_{n+1},b_{n+1}]$。

如此一来，我们便得到一个闭区间套。由闭区间套定理，一定存在一个实数 $c$，使得 $c\in\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]$。

下面我们证明 $c=\sup A$。

$c$ 的特殊之处在哪呢？它的左边 $a_n$ 不是 $A$ 的上界，而右边 $b_n$ 都是 $A$ 的上界，而且 $a_n,b_n$ 之间会随 $n$ 增大任意接近，这说明 $a_n,c,b_n$ 三者也能在后面任意接近。把这个“任意接近”和上确界定义里面的“任意接近”联系起来，就能得到证明。

(i) 先证明 $c$ 是 $A$ 的上界，也就是说任何一个大于 $c$ 的数字都是 $A$ 的上界，这一点利用右边。如果 $c$ 不是一个上界，则 $\exists\ x\in A$，$c<x$。因为 $c,b_n$ 之间的距离能任意小，所以它们肯定能小于 $c,x$ 之间的距离，也就是说 $x$ 会大于某个 $b_n$，这样就矛盾了。数学语言说法如下：

取 $\varepsilon=x-c$，因为 $b_n-c\leq b_n-a_n=\displaystyle\frac{b_1-a_1}{2^{n-1}}$，而令 $n>\log_2(\displaystyle\frac{b_1-a_1}{\varepsilon})+1$ 时，$b_n-c<\varepsilon$，即 $x>b_n>x$，矛盾。（一个元素不能大于上界，不然就大于自身）

所以 $c$ 是 $A$ 的上界。

(ii) 再证明 $c$ 是 $A$ 的最小上界，也就是说任何一个小于 $c$ 的数字都不是 $A$ 的上界，这一点利用左边。如果 $c$ 不是最小上界，则 $\exists\ y<c$，使得 $y$ 是 $A$ 的上界。同上分析，取 $\varepsilon=c-y$，因为 $c-a_n\leq b_n-a_n=\displaystyle\frac{b_1-a_1}{2^{n-1}}$，而令 $n>\log_2\left(\displaystyle\frac{b_1-a_1}{\varepsilon}\right)+1$ 时，$c-a_n<\varepsilon$，即 $a_n<y<a_n$，矛盾。（其实跟上面一样）

综上所述 ，$c=\sup A$。

这就证明了完备性公理。

(b) 单调有界定理 $\Rightarrow$ 闭区间套定理

单调有界定理说明，一列一直增加的数列，如果有上界，那么它一定会收敛到某个实数。如果不收敛到某个上界，肯定也会收敛到更小的一个上界。这就像打到了一堵墙上，数列会越来越靠近墙，但不会穿过墙。

“墙”与“切”的关系其实很紧密，事实上，闭区间套定理用刀切出来的实数正好就可以看作分开左右端点的一堵墙。所以左/右端点的极限就是切出来的实数。

下面用数学语言证明。

设 $\{[a_n,b_n]\}$ 是闭区间套，则对 $\forall\ n\in \mathbb{N^+}$，$a_n\leq a_{n+1}\leq b_1$，这说明 $\{a_n\}$ 单调递增有上界，由单调有界定理，$\{a_n\}$ 有极限，设 $\displaystyle\lim_{n\to\infty}a_n=a$。

下面证明 $a\in [a_n,b_n]$ 对 $\forall\ n\in \mathbb{N^+}$ 成立。由于右边端点全是上界，即对 $\forall\ m,n\in \mathbb{N^+}$，$a_m\leq b_n$，由序极限定理 $a\leq b_n$。

对于左边，我们固定一个 $n$，因为 $\{a_n\}$ 单调递增，所以对 $\forall\ m\geq n$，$a_n\leq a_m$，由序极限定理 $a_n\leq a$。

所以对 $\forall\ n\in \mathbb{N^+}$，$a\in [a_n,b_n]$。即 $\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]=\{a\}\neq \varnothing$。

这就证明了闭区间套定理。

(c) Bolzano-Weierstrass 定理 $\Rightarrow$ 闭区间套定理

Bolzano-Weierstrass 定理可以在任何一个有界序列里面找到一个极限，而闭区间套的左右端点都是有界的，所以我们可以用前者来生成一个极限，由 (b) 问的证明可知，这个极限就是闭区间套切出来的实数。

总之，由 (b) 问的概述，$\{a_n\}$ 是有界的，所以由 Bolzano-Weierstrass 定理，$\{a_n\}$ 有一个收敛子列 $\{a_{n_k}\}$，设 $\displaystyle\lim_{k\to\infty}a_{n_k}=a$。

其实对这个子列的分析与 (b) 问的分析是一样的，同样由序极限定理得出 $a\leq b_n$。

左边同样固定 $n$，并使 $m>n$，则 $n_m\geq m>n$，所以 $a_n\leq a_{n_m}$，由序极限定理 $a_n\leq a$。

所以对 $\forall\ n\in \mathbb{N^+}$，$a\in [a_n,b_n]$。即 $\displaystyle\bigcap_{n=1}^{\infty}[a_n,b_n]=\{a\}\neq \varnothing$。

这就证明了闭区间套定理。

(d) Cauchy 准则 $\Rightarrow$ Bolzano-Weierstrass 定理

Cauchy 准则在不知道极限，只需要知道数列的项彼此之间足够接近的情况下，就能判断数列收敛。所以我们需要用它来构造一个收敛子列。而 Bolzano-Weierstrass 定理的条件是有界。有界和足够接近...要怎么结合到一起呢？我们可以仿照书上的证明思路，因为它有界，所以我们可以不断的选取更小区间范围里的项，从而使它们彼此足够接近。

设 $\{a_n\}$ 有界，$\exists\ M>0$，对 $\forall\ n\in \mathbb{N^+}$，$a_n\in [-M,M]$。

选取第一个 $a_{n_1}\in [-M,M]$，记 $b_1=-M,c_1=M$，则 $a_{n_1}\in [b_1,c_1]$。

选取第二个 $a_{n_2}$，$n_2>n_1$：

若 $[b_1,\displaystyle\frac{b_1+c_1}{2}]$ 有 $\{a_n\}$ 的无限项，则 $a_{n_2}\in [b_1,\displaystyle\frac{b_1+c_1}{2}]$，否则 $a_{n_2}\in [\displaystyle\frac{b_1+c_1}{2},c_1]$，记 $a_{n_2}$ 属于的新闭区间为 $[b_2,c_2]$。

选取第三个 $a_{n_3}$，$n_3>n_2$：

若 $[b_2,\displaystyle\frac{b_2+c_2}{2}]$ 有 $\{a_n\}$ 的无限项，则 $a_{n_3}\in [b_2,\displaystyle\frac{b_2+c_2}{2}]$，否则 $a_{n_3}\in [\displaystyle\frac{b_2+c_2}{2},c_2]$，记 $a_{n_3}$ 属于的新闭区间为 $[b_3,c_3]$。

$\cdots$

依此类推，对 $\forall\ k\in \mathbb{N^+}$，都可以选取出一个闭区间，$a_{n_k}\in [b_k,c_k]$。

这样就构造出了一个子列 $\{a_{n_k}\}$。

依据选取方式，$c_k-b_k=\displaystyle\frac{M}{2^{k-2}}$，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，$N>\log_2\left(\displaystyle\frac{M}{\varepsilon}\right)+2$，对 $\forall\ p,q>N$，都有 $b_N\leq a_{n_p}\leq c_N$，$b_N\leq a_{n_q}\leq c_N$，所以 $|a_{n_p}-a_{n_q}|\leq c_N-b_N=\displaystyle\frac{M}{2^{N-2}}<\varepsilon$，$\{a_{n_k}\}$ 收敛。

这就证明了 Bolzano-Weierstrass 定理。

---

## 习题 2.7 无穷级数的性质

!!! question "练习 2.7.1"
    证明交错级数判别法(定理2.7.7)相当于证明部分和序列
    
    $$
    {s}_{n} = {a}_{1} - {a}_{2} + {a}_{3} - \cdots  \pm  {a}_{n}
    $$
    
    收敛。(第2.1节中的开篇例子包括 \(\left( {s}_{n}\right)\) 的典型说明。)完备性的不同特征导致不同的证明。
    
    (a) 通过证明 \(\left( {s}_{n}\right)\) 是Cauchy列来证明交错级数判别法。
    
    (b) 使用嵌套区间性质(定理1.4.1)为该结果提供另一种证明。
    
    (c) 考虑子列 \(\left( {s}_{2n}\right)\) 和 \(\left( {s}_{{2n} + 1}\right)\) ，并展示单调收敛定理如何为交错级数检验提供第三种证明。

因为 $s_n=\displaystyle\sum_{k=1}^{n}(-1)^{k+1}a_k$，所以证明 $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}a_n$ 收敛相当于证明 $\{s_n\}$ 收敛。

我们以 $a_k=\displaystyle\frac{1}{k}$ 为例，生成 $s_n$ 的一份点列图：

![](https://img-cdn.lusyoe.cn/images/HuangTianye/2025/10/12/kvjr23rpdi.png)

可以看到，奇数项和偶数项各自单调，且摆动区间越来越小，这将为我们接下来的证明提供参考。

(a) 由于 $\displaystyle\lim_{n\to\infty}a_n=0$，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|a_n|<\varepsilon$。

所以对 $\forall\ n>m>N$，$|s_m-s_n|=\left|\displaystyle\sum_{k=m+1}^n a_k\right| \leq \sum_{k=m+1}^n |a_k| < (n-m)\varepsilon$。

这样子不足以控制它的大小。

再考虑没有用上的 $\{a_n\}$ 单调递减，则有 $a_{k}-a_{k+1}\geq 0$，这个不等式正反用可得 $0\leq a_k-(a_{k+1}-a_{k+2})\leq a_{k}$。事实上，$a_k$ 后面所有摆动项加起来的威力，都无法让它脱离这个区间。因此，我们最终的目的是证明 $0\leq \displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}$。

若 $a_n$ 前为正号，则 $\displaystyle\sum_{k=m+1}^{n}a_k=a_{m+1}-(a_{m+2}-a_{m+3})-(a_{m+4}-a_{m+5})-\cdots-(a_{n-1}-a_{n})\leq a_{m+1}$，

$\displaystyle\sum_{k=m+1}^{n}a_k=(a_{m+1}-a_{m+2})+(a_{m+3}-a_{m+4})+\cdots+(a_{n-2}+a_{n-1})+a_n\geq 0$，

所以 $0\leq \displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}$。

若 $a_n$ 前为负号，用同样的方法两次组合分别证明。

所以 $|s_m-s_n|=\displaystyle\sum_{k=m+1}^{n}a_k\leq a_{m+1}<\varepsilon$，由 Cauchy 准则可知 $\{s_n\}$ 收敛。

(b) 考虑到 $\{s_n\}$ 是在越来越小的区间里面摆动的，所以利用闭区间套定理可以追踪到它的极限，再进行证明。

若 $s_k\leq s_{k+1}$ 即 $a_{k+1}$ 前面为正号，则 $s_{k+2}=s_{k+1}-a_{k+2}\leq s_{k+1}$，$s_{k+2}=s_k+(a_{k+1}-a_{k+2})\geq s_k$，得到 $s_k\leq s_{k+2}\leq s_{k+1}$。

若 $s_k\geq s_{k+1}$ 即 $a_{k+1}$ 前面为负号，用同样的方法可得 $s_k \leq s_{k+2}\leq s_{k+1}$。

这说明 $\{s_n\}$ 在越来越小的区间内摆动，下面构造闭区间套。

设 $I_k=[s_k,s_{k+1}]$，则由上述分析可知 $I_{k+1}\subset I_k$。

所以 $\{I_k\}$ 是一个闭区间套，由闭区间套定理，$\exists\ s\in \displaystyle\bigcap_{k=1}^{\infty}I_k$。

下面证明 $\displaystyle\lim_{n\to\infty}s_n=s$。

因为 $\displaystyle\lim_{n\to\infty}|s_{n+1}-s_{n}|=\displaystyle\lim_{n\to\infty}|a_{n+1}|=0$，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$|s_{n+1}-s_n|<\varepsilon$。

又因为 $s\in I_n$，所以 $|s_n-s|\leq |s_{n+1}-s_n|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}s_n=s$。

所以 $\{s_n\}$ 收敛。

(c) 我们这里让 $n$ 从 $1$ 开始计数，这样 $\{s_{2n-1}\}$ 作为子列比 $\{s_{2n+1}\}$ 更为合适。

$s_{2n+1}=s_{2n-1}-(a_{2n}-a_{2n+1})\leq s_{2n-1}$，所以 $\{s_{2n-1}\}$ 单调递减。

$s_{2n+2}=s_{2n}+a_{2n+1}-a_{2n+2}\geq s_{2n}$，所以 $\{s_{2n}\}$ 单调递增。

又因为 $s_{2n-1}-s_{2n}=a_{2n}\geq 0$，所以 $s_1\geq s_{2n-1}\geq s_{2n}\geq s_2$，这说明 $\{s_{2n-1}\}$ 和 $\{s_{2n}\}$ 都是有界的。

由单调有界定理可知 $\{s_{2n-1}\}$ 和 $\{s_{2n}\}$ 都收敛。

设 $\displaystyle\lim_{n\to\infty}s_{2n-1}=s$，则对 $\forall\ \varepsilon>0$，$\exists\ N_1\in \mathbb{N^+}$，使得对 $\forall\ n>N_1$，$|s_{2n-1}-s|<\displaystyle\frac{\varepsilon}{2}$。

又 $\displaystyle\lim_{n\to\infty}a_{2n}=\displaystyle\lim_{n\to\infty}|s_{2n-1}-s_{2n}|=0$，所以对 $\forall\ \varepsilon>0$，$\exists\ N_2\in \mathbb{N^+}$，使得对 $\forall\ n>N_2$，$|s_{2n-1}-s_{2n}|<\displaystyle\frac{\varepsilon}{2}$。

取 $N=\max\{N_1,N_2\}$，则对 $\forall\ n>N$，$|s_{2n}-s|=|s_{2n}-s_{2n-1}+s_{2n-1}-s|\leq |s_{2n}-s_{2n-1}|+|s_{2n-1}-s|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}s_{2n}=s$。

由 [$2.3.5.$](#2.3.5.)，$\displaystyle\lim_{n\to\infty}s_n=s$。

<br/>


!!! question "练习 2.7.2"
    (a) 使用级数的Cauchy准则为比较检验(定理2.7.4)的证明提供详细步骤。
    
    (b) 使用单调收敛定理为比较判别法提供另一种证明。

令 $s_n=\displaystyle\sum_{k=1}^{n}a_k$，$t_n=\displaystyle\sum_{k=1}^{n}b_k$，那么判断它们的敛散性就相当于判断原级数的敛散性了。

由于对 $\forall\ k\in \mathbb{N^+}$，$0\leq a_k\leq b_k$，所以 $s_n\leq t_n$，且它们都是单调递增的。

(a) (i) 若 $\{t_n\}$ 收敛，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n>N$，$|t_m-t_n|<\varepsilon$，即 $\displaystyle\sum_{k=m+1}^{n}b_k<\varepsilon$。

所以 $|s_m-s_n|=\displaystyle\sum_{k=m+1}^{n}a_k\leq \displaystyle\sum_{k=m+1}^{n}b_k<\varepsilon$，由 Cauchy 准则可知 $\{s_n\}$ 收敛。

(ii) 若 $\{s_n\}$ 发散，则 $\exists\ \varepsilon>0$，对 $\forall\ N\in \mathbb{N^+}$，$\exists\ m,n>N$，使得 $|s_m-s_n|\geq \varepsilon$，即 $\displaystyle\sum_{k=m+1}^{n}a_k\geq \varepsilon$。

所以 $|t_m-t_n|=\displaystyle\sum_{k=m+1}^{n}b_k\geq \displaystyle\sum_{k=m+1}^{n}a_k\geq \varepsilon$，由 Cauchy 准则可知 $\{t_n\}$ 发散。

(b) (i) 若 $\{t_n\}$ 收敛，则 $\{t_n\}$ 有界，$\exists\ M>0$，使得对 $\forall\ n\in \mathbb{N^+}$，$|t_n|\leq M$。

又因为 $s_n\leq t_n\leq M$，所以 $\{s_n\}$ 也有界，又因为 $\{s_n\}$ 单调递增，所以由单调有界定理可知 $\{s_n\}$ 收敛。

(ii) 若 $\{s_n\}$ 发散，则对 $\forall\ M>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n>N$，$s_n>M$。

所以 $t_n\geq s_n>M$，$\{t_n\}$ 发散。

<br/>


!!! question "练习 2.7.3"
    设 \(\sum {a}_{n}\) 给定。对于每个 \(n \in  \mathbb{N}\) ，如果 \({a}_{n}\) 为正，则赋值 \({p}_{n} = 0\) ；如果 \({a}_{n}\) 为负，则赋值 \({q}_{n} = {a}_{n}\) 。类似地，如果 \({a}_{n}\) 为负，则赋值 \({q}_{n} = 0\) ；如果 \({a}_{n}\) 为正，则赋值 [latex7]。
    
    (a) 论证如果 \(\sum {a}_{n}\) 发散，则 \(\sum {p}_{n}\) 或 \(\sum {q}_{n}\) 中至少有一个发散。
    
    (b) 证明如果 \(\sum {a}_{n}\) 条件收敛，则 \(\sum {p}_{n}\) 和 \(\sum {q}_{n}\) 都发散。

译本的题目有点问题，这里我按照自己的想法修正一下：

对于每个 $n\in \mathbb{N^+}$，

$$
    p_n=\begin{cases}
        0,\quad &a_n\geq 0\\
        a_n,\quad &a_n<0
    \end{cases}
$$

$$
    q_n=\begin{cases}
        a_n,\quad &a_n\geq 0\\
        0,\quad &a_n<0
    \end{cases}
$$

由此定义，$\sum a_n=\sum p_n+\sum q_n$。

(a) 若 $\{\sum a_n\}$ 发散，由 $\sum a_n=\sum p_n+\sum q_n$ 可知 $\sum p_k,\sum q_k$ 必有其一发散。

(b) 若 $\sum a_n$ 条件收敛，则 $\sum |a_n|$ 发散。

由 $\sum a_n=\sum p_n+\sum q_n$ 收敛，$\sum p_n,\sum q_n$ 要么都收敛，要么都发散；

由 $\sum |a_n|=-\sum p_n+\sum q_n$ 发散，$\sum p_n,\sum q_n$ 必有其一发散。

综合两条，即得 $\sum p_n$ 和 $\sum q_n$ 均发散。

<br/>


!!! question "练习 2.7.4"
    给出一个例子，说明 \(\sum {x}_{n}\) 和 \(\sum {y}_{n}\) 都发散，但 \(\sum {x}_{n}{y}_{n}\) 收敛的情况是可能的。

考虑构造交错级数，用它乘上另一个级数就可能让它项与项之间相互抵消，进而收敛。

$x_n=1$，$y_n=(-1)^n$ 可以吗？$\sum x_ny_n$ 永远在 $0,1$ 上摆动，不收敛。

所以另一个级数还得单调递减，让抵消后的值越来越小。

比如说，$x_n=\displaystyle\frac{1}{n}$，$y_n=(-1)^n$，那么 $x_ny_n=(-1)^n\displaystyle\frac{1}{n}$ 就是一个交错级数，由判别法可知它收敛。

<br/>


!!! question "练习 2.7.5"
    (a) 证明如果 \(\sum {a}_{n}\) 绝对收敛，则 \(\sum {a}_{n}^{2}\) 也绝对收敛。这个命题在没有绝对收敛的情况下是否成立？(b) 如果 \(\sum {a}_{n}\) 收敛且 \({a}_{n} \geq  0\) ，我们能否得出关于 \(\sum \sqrt{{a}_{n}}\) 的任何结论？

(a) 若 $\sum a_n$ 绝对收敛，要证 $\sum a_n^2$ 收敛，一个可能的想法是 $a_n^2\leq |a_n|$ 即 $|a_n|<1$，而这在绝对收敛的条件下是做得到的（事实上 $a_n$ 可以任意小）。

由 Cauchy 准则，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n\geq N$，$\displaystyle\sum_{k=m+1}^{n}|a_k|<\varepsilon$。我们取 $\varepsilon<1$，$m=n-1$，就有 $\forall\ n>N$， $|a_n|<\varepsilon<1$，所以 $a_n^2\leq |a_n|$。

所以 $\displaystyle\sum_{k=n+1}^{n}a_k^2\leq \displaystyle\sum_{k=m+1}^{n}|a_k|<\varepsilon$，由 Cauchy 准则可知 $\sum a_n^2$ 收敛。由非负性可得 $\sum a_n^2$ 绝对收敛。

(b) 不能。由 (a) 的分析，$0\leq a_n<1$ 时 $a_n\leq \sqrt{a_n}$，所以 $\sqrt{a_n}$ 的值增大了，那它的和就不一定收敛。

比如令 $a_n=\displaystyle\frac{1}{n^2}$，则 $\sum a_n$ 收敛，但 $\sum \sqrt{a_n}=\sum \displaystyle\frac{1}{n}$ 发散。

<br/>


!!! question "练习 2.7.6"
    (a) 证明如果 \(\sum {x}_{n}\) 绝对收敛，且序列 \(\left( {y}_{n}\right)\) 有界，则和 \(\sum {x}_{n}{y}_{n}\) 收敛。
    
    (b) 找出一个反例，证明如果 \(\sum {x}_{n}\) 的条件收敛，则(a)部分并不总是成立。

(a) 用绝对值不等式将 $|\sum x_ny_n|$ 拆开，再用 $\{y_n\}$ 有界进行估计，最后用绝对收敛的条件得出结论。

由 $\{y_n\}$ 有界，$\exists\ M>0$，使得对 $\forall\ n\in \mathbb{N^+}$，$|y_n|\leq M$。

又因为 $\sum x_n$ 绝对收敛，所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ m,n>N$，$\displaystyle\sum_{k=m+1}^{n}|x_k|<\displaystyle\frac{\varepsilon}{M}$。

所以对 $\forall\ m,n>N$，$|\displaystyle\sum_{k=m+1}^{n}x_ky_k|\leq \displaystyle\sum_{k=m+1}^{n}|x_k||y_k|\leq M\displaystyle\sum_{k=m+1}^{n}|x_k|<M\displaystyle\frac{\varepsilon}{M}=\varepsilon$，由 Cauchy 准则可知 $\sum x_ny_n$ 收敛。

(b) 考虑 $\sum x_n,\sum y_n$ 都是交错级数的情况，那么它们相乘后可能抵消符号，变成正项级数，从而发散。

比如说，$x_n=(-1)^{n+1}\displaystyle\frac{1}{n}$，$y_n=(-1)^{n+1}$，则满足题意，但 $x_ny_n=\displaystyle\frac{1}{n}$，$\sum x_ny_n$ 发散。

<br/>

$2.7.7.$<a id="6">几何级数与 $\mathrm{p}$ 级数间的转换</a>

题目让我们用几何级数的敛散性证明 $\mathrm{p}$ 级数的敛散性。也就是

$$
    \sum ar^n \Rightarrow \sum \frac{1}{n^p}
$$

这两个级数的变化量一个在指数上，一个在底数上，所以需要想一个转换的方法。

有什么办法能将变化量这样转换，而不改变原级数的敛散性呢？我没有想到，问了 deepseek 后，它为我提供了 Cauchy 判敛法，在 $2.4$ 节提过：

$$
    a_n\ \text{单调递减且非负}\Rightarrow \sum a_n\ \text{收敛}\Leftrightarrow \sum 2^na_{2^n}\ \text{收敛}
$$

由此可见，$\sum \displaystyle\frac{1}{n^p}$ 是否收敛等价于 $\sum 2^n\displaystyle\frac{1}{(2^n)^p}=\sum (2^{(1-p)})^n$ 是否收敛，这就把变量转移到指数上来了。

由几何级数的敛散性可知，当且仅当 $|2^{1-p}|<1$ 即 $p>1$ 时 $\sum (2^{(1-p)})^n$ 收敛。

所以 $\sum \displaystyle\frac{1}{n^p}$ 当且仅当 $p>1$ 时收敛。

<br/>


!!! question "练习 2.7.8"
    证明定理2.7.1的第(ii)部分。

我们要论证部分和序列

$$
    \begin{align*}
        s_n&=(a_1+b_1)+(a_2+b_2)+\cdots (a_n+b_n)\\
        &=(a_1+a_2+\cdots +a_n)+(b_1+b_2+\cdots +b_n)\\
    \end{align*}
$$

收敛，则令 $p_n=a_1+a_2+\cdots +a_n$，$q_n=b_1+b_2+\cdots +b_n$，则 $s_n=p_n+q_n$。

由 $p_n,q_n$ 收敛可知 $s_n$ 收敛。

<br/>


!!! question "练习 2.7.9"
    (比值判别法). 给定一个级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) ，其中 \({a}_{n} \neq  0\) ，比值判别法指出，如果 \(\left( {a}_{n}\right)\) 满足
    
    $$
    \lim \left| \frac{{a}_{n + 1}}{{a}_{n}}\right|  = r < 1
    $$
    
    则该级数绝对收敛。
    
    (a) 设 \({r}^{\prime }\) 满足 \(r < {r}^{\prime } < 1\) 。(为什么这样的 \({r}^{\prime }\) 必须存在？)解释为什么存在一个 \(N\) ，使得 \(n \geq  N\) 蕴含 \(\left| {a}_{n + 1}\right|  \leq  \left| {a}_{n}\right| {r}^{\prime }\) 。
    
    (b) 为什么 \(\left| {a}_{N}\right| \sum {\left( {r}^{\prime }\right) }^{n}\) 必然收敛？
    
    (c) 现在，证明 \(\sum \left| {a}_{n}\right|\) 收敛。

(a) 由实数稠密性可知 $r'$ 必须存在。

由 $\displaystyle\lim_{n\to\infty}|\displaystyle\frac{a_{n+1}}{a_n}|=r<r'$，则对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n\geq N$，$|\displaystyle\frac{a_{n+1}}{a_n}-r|\leq \varepsilon$。

取 $\varepsilon=r'-r$，则对 $\forall\ n>N$，$|\displaystyle\frac{a_{n+1}}{a_n}|\leq r+\varepsilon=r'$。所以 对 $\forall\ n\geq N$，$|a_{n+1}|\leq |a_n|r'$。

(b) 因为 $|\displaystyle\frac{a_{n+1}}{a_n}|\geq 0$，由序极限定理可知 $\displaystyle\lim_{n\to\infty}|\displaystyle\frac{a_{n+1}}{a_n}|=r\geq 0$。所以 $0<r'<1$，由几何级数的敛散性可知 $|a_N|\sum (r')^n$ 收敛。

(c) 结合前两问我们可以把 $\{a_n\}$ 放缩成一个收敛的几何级数，从而证明 $\sum a_n$ 收敛。

对 $\forall\ n\in \mathbb{N}$，由上面递推式得出 $|a_{n+N}|\leq |a_N|(r')^{n}$。所以 $\displaystyle\sum_{n=N}^{\infty}|a_n|\leq \displaystyle\sum_{n=0}^{\infty}|a_N|(r')^{n}=|a_N|\sum_{n=0}^{\infty}(r')^{n}=\frac{|a_N|}{1-r'}$。由此可知 $\displaystyle \sum_{n=N}^{\infty}|a_n|$ 收敛。

由于收敛级数的前有限项和不影响其敛散性（Cauchy 收敛准则），所以 $\sum |a_n|$ 收敛。

<br/>


!!! question "练习 2.7.10"
    (a) 证明如果 \({a}_{n} > 0\) 和 \(\lim \left( {n{a}_{n}}\right)  = l\) 且 \(l \neq  0\) ，则级数 \(\sum {a}_{n}\) 发散。
    
    (b) 假设 \({a}_{n} > 0\) 和 \(\lim \left( {{n}^{2}{a}_{n}}\right)\) 存在。证明 \(\sum {a}_{n}\) 收敛。

(a) 通过 $\displaystyle\lim_{n\to\infty}(na_n)=l$ 估计 $a_n$ 的下界即可。这里我们用 $2.7.9.$ 的类似操作。

首先，由 $a_n>0$，$l>0$（题目中给出了 $l\neq 0$），所以对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，使得对 $\forall\ n\geq N$，$|na_n-l|<\varepsilon$。

取 $\varepsilon=\displaystyle\frac{l}{2}$，则对 $\forall\ n\geq N$，$|na_n-l|<\displaystyle\frac{l}{2}$，即 $-\displaystyle\frac{l}{2}<na_n-l<\displaystyle\frac{l}{2}$，所以 $na_n>\displaystyle\frac{l}{2}$，即 $a_n>\displaystyle\frac{l}{2n}$。

所以 $\displaystyle\sum_{n=N}^{\infty} a_n>\displaystyle\frac{l}{2}\sum_{n=N}^{\infty} \displaystyle\frac{1}{n}$，由 $\mathrm{p}$ 级数的敛散性和比较判别法可知 $\sum a_n$ 发散。

(b) 同样的方法，这次估计上界。

记 $\displaystyle\lim_{n\to\infty}(n^2a_n)=l$，由 (a) 问同样的操作最终可得出 $\exists\ N\in \mathbb{N^+}$，对 $\forall\ n\geq N$，$a_n<\displaystyle\frac{3l}{2n^2}$

还是对 $n\geq N$ 的项进行求和放缩，同样的操作即可知 $\sum a_n$ 收敛。

<br/>


!!! question "练习 2.7.11"
    找出两个级数 \(\sum {a}_{n}\) 和 \(\sum {b}_{n}\) 的例子，它们都发散，但 \(\sum \min \left\{  {{a}_{n},{b}_{n}}\right\}\) 收敛。为了使问题更具挑战性，请给出 \(\left( {a}_{n}\right)\) 和 \(\left( {b}_{n}\right)\) 为正且递减的例子。

一般的例子可以这么构造：$0,n$ 奇偶交替，另外一个级数 $n,0$ 奇偶交替，这样它们的最小值永远是 $0$ 即可收敛。

全都为正项递减的例子太难了，问了 deepseek 也构造不出来。

问了 Gemini 2.5 pro 后，它给了我一个思路：

$a_n,b_n$ 都要一段递减，一段常数，交替进行，使得 $\min(a_n,b_n)$ 永远在递减。

首先我们选取递减部分，它肯定要收敛，所以我们选取 $\displaystyle\frac{1}{n^2}$，并先让 $a_n=\displaystyle\frac{1}{n^2}$ 一段距离。

$a_1=1$，$a_2=\displaystyle\frac{1}{4}$ 时，让 $b_1=b_2=1$，接下来让 $a_3$ 到 $a_6$ 都等于 $\displaystyle\frac{1}{4}$，而 $b_3$ 到 $b_6$ 按接下来的 $\displaystyle\frac{1}{n^2}$ 序列递减，一直递减到 $\displaystyle\frac{1}{36}$，

然后让 $a_7$ 到 $a_{42}$ 的值都等于 $\displaystyle\frac{1}{36}$，而 $b_7$ 到 $b_{42}$ 按接下来的 $\displaystyle\frac{1}{n^2}$ 序列递减，一直递减到 $\displaystyle\frac{1}{42^2}$。

接下来就让从 $a_{43}$ 开始的 $42^2$ 项按 $\displaystyle\frac{1}{n^2}$ 通项递减，而从 $b_{43}$ 开始的 $42^2$ 项值都等于 $\displaystyle\frac{1}{42^2}$。

所以，我们的操作流程如下：每次常数段的前一项记作 $a_k$，那么下一段常数段每一项的值就为 $a_k$，而长度为 $\displaystyle\frac{1}{a_k}$，这样这一段所有常数的和就为 $1$。常数段结束之后，紧接着按 $\displaystyle\frac{1}{n^2}$ 的通项递减，而常数段的最后一项 $a_s$ 的下标作为另一个数列常数段的前一项下标，即 $b_s$ 为 $\{b_n\}$ 常数段的前一项。而 $a_2$ 作为 $\{a_n\}$ 的第一个常数段的前一项，$b_1$ 到 $b_2$ 作为 $\{b_n\}$ 的第一个常数段。再规定 $b_1=b_2=a_1=1$。

这样子就能保证 $\{a_n\}$ 和 $\{b_n\}$ 永远在递减，而且都有无穷多个常数段，这样级数和里面就有无穷多个 $1$ 的和，这就保证了级数发散。

而交替递减的形式保证了 $\{\min(a_n,b_n)\}=\{\displaystyle\frac{1}{n^2}\}$，所以 $\sum \min(a_n,b_n)$ 收敛。

下为 $\{a_n\},\{b_n\}$ 的示意图，使用对数坐标轴让交替单调递减的性质更清晰可见：

![](https://img-cdn.lusyoe.cn/images/HuangTianye/2025/10/13/pgkfkj1l92.png)

<br/>


!!! question "练习 2.7.12"
    (分部求和法)。设 \(\left( {x}_{n}\right)\) 和 \(\left( {y}_{n}\right)\) 为序列，且令 \({s}_{n} = {x}_{1} + {x}_{2} + \cdots  + {x}_{n}\) 。利用 \({x}_{j} = {s}_{j} - {s}_{j - 1}\) 的观察来验证公式
    
    $$
    \mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j} = {s}_{n}{y}_{n + 1} - {s}_{m}{y}_{m + 1} + \mathop{\sum }\limits_{{j = m + 1}}^{n}{s}_{j}\left( {{y}_{j} - {y}_{j + 1}}\right) .
    $$

我们主要分析这个式子：

$$
    \displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})
$$

由题目给出的提示，我们考虑产生 $\{s_j\}$ 的相邻项再作差。因为上面这个求和每一项里都有 $\{y_j\}$ 相邻项的差，所以求和的项与项之间是有公因式 $y_j$ 的，将不同的 $s_j$ 都提取成它的系数即可构造：

$$
    \begin{align*}
    &s_j(y_j-y_{j+1})+s_{j+1}(y_{j+1}-y_{j+2})+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+(s_{j+1}-s_j)y_{j+1}-s_{j+1}y_{j+2}+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}-s_{j+1}y_{j+2}+s_{j+2}(y_{j+2}-y_{j+3})+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+(s_{j+2}-s_{j+1})y_{j+2}-s_{j+2}y_{j+3}+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+x_{j+2}y_{j+2}-s_{j+2}y_{j+3}+\cdots\\
    =\ &s_jy_j+x_{j+1}y_{j+1}+x_{j+2}y_{j+2}+\cdots+x_ny_n-s_ny_{n+1}\\
    \end{align*}
$$

所以

$$
    \begin{align*}
        &s_ny_{n+1}-s_my_{m+1}+\displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})\\
        =\ &s_ny_{n+1}-s_my_{m+1}+s_{m+1}y_{m+1}-s_ny_{n+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &(s_{m+1}-s_m)y_{m+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &x_{m+1}y_{m+1}+\displaystyle\sum_{j=m+2}^{n}x_jy_j\\
        =\ &\displaystyle\sum_{j=m+1}^{n}x_jy_j\\
    \end{align*}
$$

<br/>


!!! question "练习 2.7.13"
    (Dirichlet判别法)。Dirichlet判别法用于判断级数收敛性，它指出如果 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 的部分和有界(但不一定收敛)，且如果 \(\left( {y}_{n}\right)\) 是一个满足 \({y}_{1} \geq  {y}_{2} \geq  {y}_{3} \geq  \cdots  \geq  0\) 且 \(\lim {y}_{n} = 0\) 的序列，那么级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}{y}_{n}\) 收敛。
    
    (a) 设 \(M > 0\) 为 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 的部分和的上界。利用习题 2.7.12 证明
    
    $$
    \left| {\mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j}}\right|  \leq  {2M}\left| {y}_{m + 1}\right| .
    $$
    
    (b) 证明上述Dirichlet判别法。
    
    展示如何将交替级数判别法(定理2.7.7)作为Dirichlet判别法的特例推导出来。

记 $\displaystyle\sum_{j=1}^{n}x_j=s_n$。

(a) 由题意 $s_n\leq M$ 总是成立。

由 $\{y_n\}$ 正项递减，$y_j-y_{j+1}\geq 0$ 总是成立。

由 $2.7.12.$ 可得

$$
    \begin{align*}
        \displaystyle\sum_{j=m+1}^{n}x_jy_j
        &=s_ny_{n+1}-s_my_{m+1}+\displaystyle\sum_{j=m+1}^{n}s_j(y_j-y_{j+1})\\
        &\leq |s_n||y_{n+1}|+|s_m||y_{m+1}|+\displaystyle\sum_{j=m+1}^{n}|s_j||y_j-y_{j+1}|\\
        &\leq M|y_{n+1}|+M|y_{m+1}|+M\displaystyle\sum_{j=m+1}^{n}|y_j-y_{j+1}|\\
        &=M(y_{n+1}+y_{m+1}+\displaystyle\sum_{j=m+1}^{n}(y_j-y_{j+1}))\\
        &=2My_{m+1}=2M|y_{m+1}|\\
    \end{align*}
$$

(b) 由 $\displaystyle\lim_{n\to\infty}y_n=0$ 可知对 $\forall \ \varepsilon>0$，$\exists\ N\in\mathbb{N^+}$，当 $n>N$ 时，有 $|y_n|<\displaystyle\frac{\varepsilon}{2M}$。

即对 $\forall\ m,n>\mathbb{N^+}$，有 $\displaystyle\sum_{j=m+1}^{n}x_jy_j\leq 2M|y_{m+1}|<2M\cdot \frac{\varepsilon}{2M}=\varepsilon$。

所以 $\displaystyle\sum_{n=1}^{\infty}x_ny_n$ 收敛。

取 $x_n=(-1)^{n+1}$，$y_n$ 正项递减且趋于 $0$，则 $\sum x_n y_n$ 符合交错级数判别法的条件，由 Dirichlet 判别法知其收敛。

<br/>


!!! question "练习 2.7.14"
    (Abel判别法)。Abel判别法用于判断级数收敛性，其指出如果级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}\) 收敛，且 \(\left( {y}_{n}\right)\) 是一个满足以下条件的序列:
    
    $$
    {y}_{1} \geq  {y}_{2} \geq  {y}_{3} \geq  \cdots  \geq  0
    $$
    
    那么级数 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n}{y}_{n}\) 收敛。
    
    (a)仔细指出Abel判别法的假设与练习2.7.13中Dirichlet判别法的假设有何不同。
    
    (b) 假设 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) 的部分和有界于常数 \(A > 0\) ，并假设 \({b}_{1} \geq  {b}_{2} \geq  {b}_{3} \geq  \cdots  \geq  0\) 。使用练习 2.7.12 来证明
    
    $$
    \left| {\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{j}{b}_{j}}\right|  \leq  {2A}{b}_{1}
    $$
    
    (c) 通过以下策略证明Abel判别法(Abel’s Test)。对于固定的 \(m \in  N\) ，将部分 (b) 应用于 \(\mathop{\sum }\limits_{{j = m + 1}}^{n}{x}_{j}{y}_{j}\) ，通过设置 \({a}_{n} = {x}_{m + n}\) 和 \({b}_{n} = {y}_{m + n}\) 。(论证 \(\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}\) 的部分和的上界可以通过取 \(m\) 为任意大而变得任意小。)

(a) Abel 判别法将收敛的条件从 $\{y_n\}$ 转移到了 $\{x_n\}$ 上，并且对收敛的要求变弱了，不需要指出收敛于某个具体值。

(b) 用 $2.7.13.$ 完全一样的证明方法。

(c) 由题意可知 $\sum x_n$ 收敛，所以由 Cauchy 收敛准则，对任意 $\varepsilon>0$，存在 $N\in \mathbb{N^+}$，对任意 $n>m>N$，$\left|\displaystyle\sum_{j=m+1}^{n}x_n\right|=\left|\displaystyle\sum_{j=1}^{n-m}a_n\right|<\displaystyle\frac{\varepsilon}{2b_1}$。

所以有 $\left|\displaystyle\sum_{j=m+1}^{n}x_ny_n\right|=\left|\displaystyle\sum_{j=1}^{n-m}a_nb_n\right|\leq 2b_1\cdot \displaystyle\frac{\varepsilon}{2b_1}=\varepsilon$，由 Cauchy 收敛准则可知 $\sum x_ny_n$ 收敛。

<br/>

附录：<a id="7">绝对收敛重排定理的证明</a>

定理复述：若 $\displaystyle\sum_{n=1}^{\infty}a_n$ 绝对收敛，则它的任意重排都收敛到相同的极限。

注：证明有点画蛇添足，想看收敛同极限的证明直接跳到“接下来证明极限是同一个”这一段。

证明：这里用一种跟书上不同的证明。

我的考虑是这样的：如果原数列的项是有正有负的，那么重排可以把正项和负项打乱，假设前面全排正项（或负项）部分和就会变得很大（小），难以估计重排后的部分和的范围，于是难以用 $\varepsilon-\delta$ 语言说明（这也许就是条件收敛级数重排不一定收敛的原因）。但是我们可以利用绝对收敛的性质进行估计，因为它的项全都是非负的，重排之后部分和的性质仍然好掌握，再由绝对收敛得出原重排级数收敛即可。

设 $\displaystyle\sum_{n=1}^{\infty}b_n$ 为 $\displaystyle\sum_{n=1}^{\infty}a_n$ 的一个重排。由绝对收敛的性质，$\displaystyle\sum_{n=1}^{\infty}|a_n|$ 收敛，因为它的部分和单调递增，所以它一定有界，不妨设 $\displaystyle\sum_{n=1}^{\infty}|a_n|<M$。因为 $\{b_n\}$ 中的项均为 $\{a_n\}$ 中的项，所以 $\displaystyle\sum_{n=1}^{\infty}|b_n|<M$，由其单调的性质得到 $\displaystyle\sum_{n=1}^{\infty}|b_n|$ 收敛。也就是说 $\displaystyle\sum_{n=1}^{\infty}b_n$ 绝对收敛，所以它本身也必定收敛。

接下来证明极限为同一个，利用 Cauchy 收敛准则和绝对收敛的性质打出组合拳。

我想利用的性质是，通过两级数之差为 $0$ 证明它们收敛到同一个极限。因为 $\{a_n\}$ 中的项在 $\{b_n\}$ 中均出现，所以肯定 $\exists\ N,T\in \mathbb{N^+}$，$\{a_1,\ldots,a_N\}\subseteq \{b_1,\ldots,b_T\}$。这样 $|a_T-b_T|$ 留下来的项其下标均大于 $N$，再利用绝对收敛性质得以证明。

对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ n>m>N$，都有 $\displaystyle\sum_{k=m}^{n}|a_k|<\varepsilon$。同时又 $\exists\ T>N$，使得 ，$\{a_1,\ldots,a_N\}\subseteq \{b_1,\ldots,b_T\}$。所以对 $\forall\ n>T$，

$$
    \begin{align*}
        |\displaystyle\sum_{k=1}^{n}a_k-\displaystyle\sum_{k=1}^{n}b_k|&\leq|a_{r_1}|+|a_{r_2}|+\cdots+|a_{r_m}| \qquad r_1<r_2<\cdots<r_m，r_i>N\\
        &\leq \displaystyle\sum_{k=r_1}^{r_m}|a_k|<\varepsilon
    \end{align*}
$$

所以 $\displaystyle\sum_{n=1}^{\infty}a_n-\displaystyle\sum_{n=1}^{\infty}b_n=0$。又因为它们均收敛，所以它们的极限相同。

---

## 习题 2.8 双重求和与无穷级数的乘积

$2.8$ 节的习题旨在探索级数乘积的求和条件，我会在对应习题的后面简要说明它对应的探索步骤。

!!! question "练习 2.8.1"
    使用第2.1节中的特定数组 \(\left( {a}_{ij}\right)\) ，计算 \(\mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn}\) 。这个值与已经计算的两个迭代和值相比如何？
    
    如何定义双重求和的问题与第2.7节末尾讨论的重排主题之间存在深刻的相似性。两者都涉及到无限设置中加法的交换性。对于重排，解决方案是增加了绝对收敛的假设，同样的方法适用于双重求和也就不足为奇了。在绝对收敛的假设下，讨论的每种计算双重和值的方法都会得到相同的结果。

$s_{nn}=-1\left(1+\displaystyle\frac{1}{2}+\displaystyle\frac{1}{4}+\cdots+\displaystyle\frac{1}{2^{n-1}}\right)=-2+\displaystyle\frac{1}{2^{n-1}}$

所以 $\displaystyle\lim_{n\to\infty}s_n=-2=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_{ij}$。

<br/>

!!! question "练习 2.8.2"
    （双重级数绝对收敛 $\Rightarrow$ 本身收敛）
    
    证明如果迭代级数
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {a}_{ij}\right|
    $$
    
    收敛(意味着对于每个固定的 $i \in  \mathbb{N}$ ，级数 $\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {a}_{ij}\right|$ 收敛到某个实数 ${b}_{i}$ ，并且级数 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{b}_{i}$ 也收敛)，则迭代级数
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{ij}
    $$
    
    收敛。


下为二维数列 $\{a_{ij}\}$ 的无限方形数表，其中把每一行的和记为 $c_{i}$：

| $a_{11}$ | $a_{12}$ | $a_{13}$ | $a_{14}$ | $a_{15}$ | $\cdots$ | $c_{1}$  |

| -------- | -------- | -------- | -------- | -------- | -------- | -------- |

| $a_{21}$ | $a_{22}$ | $a_{23}$ | $a_{24}$ | $a_{25}$ | $\cdots$ | $c_{2}$  |

| $a_{31}$ | $a_{32}$ | $a_{33}$ | $a_{34}$ | $a_{35}$ | $\cdots$ | $c_{3}$  |

| $a_{41}$ | $a_{42}$ | $a_{43}$ | $a_{44}$ | $a_{45}$ | $\cdots$ | $c_{4}$  |

| $a_{51}$ | $a_{52}$ | $a_{53}$ | $a_{54}$ | $a_{55}$ | $\cdots$ | $c_{5}$  |

| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

首先，由定义可得 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}=\displaystyle\sum_{i=1}^{\infty}c_i$，所以我们要证明：

1. $c_i$ 的存在性，即 $\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 对任意 $i\in \mathbb{N^+}$ 收敛。

2. $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

因为 $\displaystyle\sum_{j=1}^{\infty}|a_{ij}|$ 收敛到 $b_i$，由绝对收敛的性质可知 $\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 也收敛，所以 $c_i$ 存在。

又因为 $\displaystyle\sum_{i=1}^{\infty}b_i$ 收敛，且 $|c_i|=\left|\displaystyle\sum_{j=1}^{\infty}a_{ij}\right| \leq \displaystyle\sum_{j=1}^{\infty}|a_{ij}|=b_i$，所以 $0\leq \displaystyle\sum_{i=1}^{\infty}|c_i|\leq \displaystyle\sum_{i=1}^{\infty}b_i$，$\displaystyle\sum_{i=1}^{\infty}|c_i|$ 收敛，所以 $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

综上所述，$\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}$ 收敛。

<br/>

!!! question "练习 2.8.3"
    （考察 $n\times n$  区域求和的收敛性）
    
    (a) 证明集合 $\left\{  {{t}_{mn} : m,n \in  \mathbb{N}}\right\}$ 有上界，并利用这一事实得出结论:序列 $\left( {t}_{nn}\right)$ 收敛。
    
    (b) 现在，利用 $\left( {t}_{nn}\right)$ 是Cauchy列这一事实，论证 $\left( {s}_{nn}\right)$ 也是Cauchy列，因此收敛。


(a) 使用 $2.8.2.$ 中一样的条件，则 $\displaystyle\sum_{i=1}^{\infty}b_i$ 是有界的，即存在 $M>0$，使得对任意的 $m\in \mathbb{N^+}$，都有 $\displaystyle\sum_{i=1}^{m}b_i \leq M$。

所以 $t_{mn}=\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_{ij}| \leq \displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{\infty}|a_{ij}| \leq \displaystyle\sum_{i=1}^{m}b_i \leq M$。

这就得到 $\{t_{mn}\}$ 有界。

又因为对 $\forall\ n\in \mathbb{N^+}$，$t_{n+1,n+1}=\displaystyle\sum_{i=1}^{n+1}\displaystyle\sum_{j=1}^{n+1}|a_{ij}|=\displaystyle\sum_{i=1}^{n}\displaystyle\sum_{j=1}^{n}|a_{ij}|+\displaystyle\sum_{j=1}^{n+1}|a_{n+1,j}|+\displaystyle\sum_{i=1}^{n}|a_{i,n+1}|\geq t_{nn}$，所以 $\{t_{nn}\}$ 单调递增。由单调有界定理可知 $\{t_{nn}\}$ 收敛。

(b) 对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\  n>m>N$，有 $|t_{mm}-t_{nn}|<\varepsilon$。

由绝对值不等式，$|s_{mm}-s_{nn}|=\left|\displaystyle\sum_{i=m+1}^{n}\displaystyle\sum_{j=1}^{n}a_{ij}+\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=m+1}^{n}a_{ij}\right|\leq \displaystyle\sum_{i=m+1}^{n}\displaystyle\sum_{j=1}^{n}|a_{ij}|+\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=m+1}^{n}|a_{ij}|=|t_{mm}-t_{nn}|<\varepsilon$。

所以 $\{s_{nn}\}$ 也是 Cauchy 列，故收敛。

<br/>

!!! question "练习 2.8.4"
    （说明 $m\times n$ 区域求和的有界性）
    
    (a) 论证存在一个 ${N}_{1} \in  \mathbb{N}$ ，使得 $m,n \geq  {N}_{1}$ 蕴含 $B - \frac{\varepsilon }{2} < {t}_{mn} \leq  B$ 。
    
    (b) 现在，证明存在一个 $N$ ，使得
    
    $$
    \left| {{s}_{mn} - S}\right|  < \varepsilon
    $$
    
    对于所有 $m,n \geq  N$ 。


(a) 取 $N_1>\max\{m_0,n_0\}$，由 $|a_{ij}|$ 的非负性可得 $\forall\ m,n>N_1$，$B-\displaystyle\frac{\varepsilon}{2}<t_{m_0n_0}\leq t_{mn}\leq B$。

(b) 一个想法是 $|s_{mn}-S|\leq |s_{mn}-s_{nn}|+|s_{nn}-S|$，并估计 $|s_{mn}-s_{nn}|$ 的大小。

绝对值不等式可得 $|s_{mn}-s_{nn}|\leq |t_{mn}-t_{nn}|$，再利用 (a) 中的结论限制 $t_{mn}$ 的范围完成证明。

首先，对 $\forall\ \varepsilon>0$，$\exists\ N_2\in \mathbb{N^+}$，对 $\forall\ n>N_2$，都有 $|s_{nn}-S|<\displaystyle\frac{\varepsilon}{2}$。

由 (a)，对 $\forall\ m,n>N_1$，$B-\displaystyle\frac{\varepsilon}{2}<t_{mn}\leq B$，$B-\displaystyle\frac{\varepsilon}{2}<t_{nn}\leq B$，所以 $|t_{mn}-t_{nn}|<\displaystyle\frac{\varepsilon}{2}$。

取 $N=\max\{N_1,N_2\}$，则对 $\forall\ m,n>N$，都有

$$
    \begin{align*}
        |s_{mn}-S| &\leq |s_{mn}-s_{nn}|+|s_{nn}-S| \\
                   &\leq |t_{mn}-t_{nn}|+|s_{nn}-S| \\
                   &< \displaystyle\frac{\varepsilon}{2}+\displaystyle\frac{\varepsilon}{2}=\varepsilon
    \end{align*}
$$

<br/>

!!! question "练习 2.8.5"
    （利用上题估计出的界限，横纵求两次极限得出结论）
    
    (a) 使用代数极限定理(定理 2.3.3)和序极限定理(定理 2.3.4)来证明对于所有 $m \geq  N$
    
    $$
    \left| {\left( {{r}_{1} + {r}_{2} + \cdots  + {r}_{m}}\right)  - S}\right|  \leq  \varepsilon .
    $$
    
    得出结论，迭代和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{ij}$ 收敛于 $S$ 。


因为 $|s_{mn}-S|<\varepsilon$，所以由序极限定理，对 $\forall\ m>N$，

$\displaystyle\lim_{n\to\infty}|s_{mn}-S|\leq \varepsilon$，即 $-\varepsilon\leq \displaystyle\lim_{n\to\infty}(s_{mn}-S)\leq \varepsilon$。

而

$$
    \begin{align*}
        \displaystyle\lim_{n\to\infty}(s_{mn}-S)&=\displaystyle\lim_{n\to\infty}s_{mn}-S\\
        &=\displaystyle\lim_{n\to\infty}(\displaystyle\sum_{j=1}^{n}a_{1j}+\displaystyle\sum_{j=1}^{n}a_{2j}+\cdots+\displaystyle\sum_{j=1}^{n}a_{mj})-S\\
        &=(\displaystyle\sum_{j=1}^{\infty}a_{1j}+\displaystyle\sum_{j=1}^{\infty}a_{2j}+\cdots+\displaystyle\sum_{j=1}^{\infty}a_{mj})-S\\
        &=(r_1+r_2+\cdots+r_m)-S
    \end{align*}
$$

所以 $|(r_1+r_2+\cdots+r_m)-S|\leq \varepsilon$，由此可得 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_{ij}=\displaystyle\sum_{i=1}^{\infty}r_i=S$。

<br/>

!!! question "练习 2.8.6"
    （运用前面所有的结论，纵横求两次极限，得到横纵求和与纵横求和结果相同的结论）
    
    通过证明另一个迭代和 $\mathop{\sum }\limits_{{j = 1}}^{\infty }\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{ij}$ 也收敛于 $S$ 来完成证明。
    注意，一旦确定对于每个固定列 $j$ ，和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{ij}$ 收敛于某个实数 ${c}_{i}$ ，就可以使用相同的论证。


仿照上题，首先对 $\forall\ n>N$，$\displaystyle\lim_{m\to\infty}|s_{mn}-S|\leq \varepsilon$；

然后把 $s_{mn}$ 逐列拆解，$s_{mn}=\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{m}a_{ij}=(\displaystyle\sum_{i=1}^{m}a_{i1}+\displaystyle\sum_{i=1}^{m}a_{i2}+\cdots+\displaystyle\sum_{i=1}^{m}a_{in})$；

根据 $t_{mn}$ 的有界性，得到 $\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}|a_{ij}|$ 有界收敛，所以对 $\forall\ k\in \mathbb{N^+}$，$\displaystyle\sum_{i=1}^{\infty}|a_{ik}|$ 收敛 $\Rightarrow$ $\displaystyle\sum_{i=1}^{\infty}a_{ik}$ 收敛。

所以 $|\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{\infty}a_{ij}-S|\leq \varepsilon$，$\displaystyle\lim_{n\to\infty}\displaystyle\sum_{j=1}^{n}\displaystyle\sum_{i=1}^{\infty}a_{ij}=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_{ij}=S$。

<br/>

!!! question "练习 2.8.7"
    （这一题为下面叙述级数之积求和做铺垫）
    
    (a) 假设定理 2.8.1 的假设——以及结论——成立，证明 $\mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k}$ 绝对收敛。
    
    (b) 模仿定理 2.8.1 证明中的策略，证明 $\mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k}$ 收敛于 $S = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn}$ 。


(a) 由绝对值不等式，$0\leq \displaystyle\sum_{k=2}^{n+1}|d_k|\leq t_{nn}$。

因为 $\{t_{nn}\}$ 收敛，所以 $\displaystyle\sum_{k=2}^{\infty}d_k$ 绝对收敛。

(b) 由 (a)，$\displaystyle\sum_{k=2}^{\infty}d_k$ 收敛。

我们要得出 $\displaystyle\lim_{n\to\infty}\displaystyle\sum_{k=2}^{n}d_k=S=\displaystyle\lim_{n\to\infty}s_{nn}$，仿照前面的做法，我们可以估计 $\left|\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right|$ 的范围。

绘制一个简单的图来说明这个范围包括的区域：

![](https://img-cdn.lusyoe.com/images/HuangTianye/2025/10/21/bj2bcdcuyp.png)

（这里假设 $n=4$）

- 红色：$s_{nn}-\displaystyle\sum_{k=2}^{n}d_k$ 剩余的元素求和；

- 红色+蓝色：$\displaystyle\sum_{k=2}^{2n}d_k-\displaystyle\sum_{k=2}^{n}d_k$ 剩余的元素求和；

因为 $\displaystyle\sum_{k=2}^{\infty}|d_k|$ 收敛，所以由 Cauchy 收敛准则，红色+蓝色区域的各元素绝对值的和可以被限制，于是可以进一步限制红色，进而得到证明。

由 $\displaystyle\sum_{k=2}^{\infty}|d_k|$ 收敛，对 $\forall\ \varepsilon>0$，$\exists\ N\in \mathbb{N^+}$，对 $\forall\ m,n>N$，$\left|\displaystyle\sum_{k=2}^{m}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$。

取 $m=2n$ 有 $\left|\displaystyle\sum_{k=2}^{2n}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$。

又 $\left|\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right|\leq \left|\displaystyle\sum_{k=2}^{2n}|d_k|-\displaystyle\sum_{k=2}^{n}|d_k|\right|<\varepsilon$，所以 $\displaystyle\lim_{n\to\infty}\left(\displaystyle\sum_{k=2}^{n}d_k-s_{nn}\right)=0$。

所以 $\displaystyle\lim_{n\to\infty}\displaystyle\sum_{k=2}^{\infty}d_k=\displaystyle\lim_{n\to\infty}s_{nn}=S$。

<br/>

!!! question "练习 2.8.8"
    假设 $\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{i}$ 绝对收敛于 $A$ ，且 $\mathop{\sum }\limits_{{j = 1}}^{\infty }{b}_{j}$ 绝对收敛于 $B$ 。
    
    (a) 证明该集合
    
    $$
    \left\{  {\mathop{\sum }\limits_{{i = 1}}^{m}\mathop{\sum }\limits_{{j = 1}}^{n}\left| {{a}_{i}{b}_{j}}\right|  : m,n \in  \mathbb{N}}\right\}
    $$
    
    是有界的。利用这一点来证明迭代和 $\mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }\left| {{a}_{i}{b}_{j}}\right|$ 收敛，从而我们可以应用定理2.8.1。
    
    (b) 设 ${s}_{nn} = \mathop{\sum }\limits_{{i = 1}}^{n}\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i}{b}_{j}$ ，并利用代数极限定理证明 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{s}_{nn} = {AB}$ 。由此得出结论
    
    $$
    \mathop{\sum }\limits_{{i = 1}}^{\infty }\mathop{\sum }\limits_{{j = 1}}^{\infty }{a}_{i}{b}_{j} = \mathop{\sum }\limits_{{j = 1}}^{\infty }\mathop{\sum }\limits_{{i = 1}}^{\infty }{a}_{i}{b}_{j} = \mathop{\sum }\limits_{{k = 2}}^{\infty }{d}_{k} = {AB},
    $$
    
    其中，如前所述， ${d}_{k} = {a}_{1}{b}_{k - 1} + {a}_{2}{b}_{k - 2} + \cdots  + {a}_{k - 1}{b}_{1}$ 。


（这一题其实可以把 $a_ib_j$ 看作 $c_{ij}$，这样所有的结论可以通过双重求和的性质给出）

(a) 由题知 $\displaystyle\sum_{i=1}^{\infty}a_i=A$，$\displaystyle\sum_{j=1}^{\infty}b_j=B$。（绝对收敛于 $A$ 指的是它本身收敛于 $A$，且是绝对收敛的）

由绝对收敛级数的单调性，可得 $\exists\ M,N>0$, 对 $\forall\ m,n\in \mathbb{N^+}$，$\displaystyle\sum_{i=1}^{m}|a_i|\leq M$，$\displaystyle\sum_{j=1}^{n}|b_j|\leq N$。

再利用绝对值的性质，可得

$$
    \begin{align*}
        \displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_ib_j|&=\displaystyle\sum_{i=1}^{m}(|a_ib_1|+|a_ib_2|+\cdots+|a_ib_n|)\\
        &=\displaystyle\sum_{i=1}^{m}(|a_i|(|b_1|+|b_2|+\cdots+|b_n|))\\
        &=\displaystyle\sum_{i=1}^{m}|a_i|\displaystyle\sum_{j=1}^{n}|b_j|\\
        &\leq MN
    \end{align*}
$$

所以 $\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}|a_ib_j|$ 是有界的。

由单调有界定理，对 $\forall\ i\in \mathbb{N^+}$，$|a_i|\displaystyle\sum_{j=1}^{n}|b_j|$ 收敛于 $c_i\geq 0$，所以 $\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{\infty}|a_ib_j|=\displaystyle\sum_{i=1}^{m}c_i$，又由单调有界定理知 $\displaystyle\sum_{i=1}^{\infty}c_i$ 收敛。

所以 $\displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}|a_ib_j|$ 收敛。

(b) 根据 (a) 中一样的方法可以将双重求和拆开，所以

$\displaystyle\lim_{n\to\infty}s_{nn}=\displaystyle\lim_{n\to\infty}\left(\displaystyle\sum_{i=1}^{n}a_i\displaystyle\sum_{j=1}^{n}b_j\right)=\displaystyle\sum_{i=1}^{\infty}a_i\displaystyle\sum_{j=1}^{\infty}b_j=AB$。

再运用书上定理 $2.8.1.$ 即可得到结论

$$
    \displaystyle\sum_{i=1}^{\infty}\displaystyle\sum_{j=1}^{\infty}a_ib_j=\displaystyle\sum_{j=1}^{\infty}\displaystyle\sum_{i=1}^{\infty}a_ib_j=\displaystyle\sum_{k=2}^{\infty}d_k=AB
$$

---
