
## 6.7 魏尔斯特拉斯逼近定理 (The Weierstrass Approximation Theorem)

卡尔·魏尔斯特拉斯 (Karl Weierstrass) 的名字与我们已经讨论过的许多重要结果联系在一起。波尔查诺-魏尔斯特拉斯定理对于理解前面章节中得出的收敛性、完备性和紧致性之间的关系至关重要。在本章中，魏尔斯特拉斯 M-判别法作为证明无穷级数一致收敛的主要工具出现。

正如在 5.4 节中所讨论的，魏尔斯特拉斯还在 1872 年给出了最早的连续但处处不可导函数的例子之一。

1885 年，魏尔斯特拉斯证明了一个结果，这与他那个处处不可导的函数形成了一个有趣的对比。这个以他名字命名的定理，后来成为了被称为“逼近论”这一新分析学分支的催化剂。

**定理 6.7.1 (魏尔斯特拉斯逼近定理/Weierstrass Approximation Theorem)**. 设 $f : [a, b] \rightarrow \mathbb{R}$ 是连续的。给定 $\epsilon > 0$，存在一个多项式 $p(x)$ 满足
$$ |f(x) - p(x)| < \epsilon $$
对所有 $x \in [a, b]$ 成立。

不用所有这些符号来重述魏尔斯特拉斯逼近定理 (WAT) 的话，那就是：闭区间上的每一个连续函数都可以被多项式一致逼近。

<br/>

> [!question] 练习 6.7.1
> 
> 假设 WAT 成立，证明如果 $f$ 在 $[a, b]$ 上连续，那么存在一个多项式序列 $(p_n)$，使得 $p_n \rightarrow f$ 在 $[a, b]$ 上一致收敛。

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

> [!question] 练习 6.7.2
> 
> 证明定理 6.7.3。
>
> 定理 6.7.3 证明的策略是首先在 $f$ 的图像上选择适当数量的点，然后证明对这些点进行折线插值能达到目的。

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

> [!question] 练习 6.7.3
> 
> (a) 找到二次多项式 $p(x) = q_0 + q_1x + q_2x^2$，插值 $g(x) = |x|$ 图像上的三个点 $(-1, 1), (0, 0)$ 和 $(1, 1)$。在同一坐标系上画出 $[-1, 1]$ 上的 $g(x)$ 和 $p(x)$。
> 
> (b) 找到插值 $g(x) = |x|$ 在点 $x = -1, -1/2, 0, 1/2$ 和 $1$ 处的四次多项式。将其略图添加到 (a) 中的图上。

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

> [!question] 练习 6.7.4
> 
> 证明 $f(x) = \sqrt{1 - x}$ 具有泰勒级数系数 $a_n$，其中 $a_0 = 1$ 以及
> 
> $$ a_n = \frac{-1 \cdot 3 \cdot 5\cdots (2n - 3)}{2 \cdot 4 \cdot 6\cdots 2n} $$
>
> 对于 $n \geq 1$ 成立。

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

> [!question] 练习 6.7.5
> 
> (a) 听从练习 6.6.9 的建议证明余项的柯西形式：
> 
> $$ E_N(x) = \frac{f^{(N+1)}(c)}{N!}(x - c)^N x $$
> 
> 其中 $c$ 在 $0$ 和 $x$ 之间。
> 
> (b) 利用这个结果证明公式 (1) 对所有 $x \in (-1, 1)$ 是成立的。

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

<br>

---

尽管柯西余项定理没有告诉我们，但公式 (1) 在 $x = \pm 1$ 处也是成立的。

> [!question] 练习 6.7.6
> 
> (a) 令
> $$ c_n = \frac{1 \cdot 3 \cdot 5\cdots (2n - 1)}{2 \cdot 4 \cdot 6\cdots 2n} $$
> 证明 $c_n < \displaystyle\frac{2}{\sqrt{2n + 1}}$。
> 
> (b) 利用 (a) 来证明 $\sum_{n=0}^{\infty} a_n$ 收敛 (此处事实上是绝对收敛)，其中 $a_n$ 是练习 6.7.4 中生成的泰勒系数序列。
> 
> (c) 仔细解释这如何验证了公式 $(1)$ 对所有的 $x \in [-1, 1]$ 成立。

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

> [!question] 练习 6.7.7
> 
> (a) 利用 $|x| = \sqrt{x^2}$ 这一事实证明，给定 $\varepsilon > 0$，存在一个多项式 $q(x)$ 满足
> 
> $$ \big| |x| - q(x) \big| < \varepsilon $$
> 
> 对于所有的 $x \in [-1, 1]$ 成立。
> 
> (b) 将此结论推广到任意区间 $[a, b]$。

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

> [!question] 练习 6.7.8
> 
> (a) 固定 $a \in [-1, 1]$ 并画出
> $$ h_a(x) = \frac{1}{2}(|x - a| + (x - a)) $$
> 在 $[-1, 1]$ 上的图像。注意 $h_a$ 是一个折线函数，且对于所有 $x \in [-1, a]$，都有 $h_a(x) = 0$。
> 
> (b) 解释为什么我们能确定 $h_a(x)$ 可以在 $[-1, 1]$ 上被一个多项式一致逼近。
> 
> (c) 令 $\phi$ 是一个折线函数，它在由下列分割所产生的每一个子区间上为线性：
> 
> $$ -1 = a_0 < a_1 < a_2 < \dots < a_n = 1. $$
> 
> 证明存在常数 $b_0, b_1, \dots, b_{n-1}$ 使得
> 
> $$ \phi(x) = \phi(-1) + b_0 h_{a_0}(x) + b_1 h_{a_1}(x) + \dots + b_{n-1} h_{a_{n-1}}(x) $$
> 
> 对于所有 $x \in [-1, 1]$ 成立。
> 
> (d) 完成区间 $[-1, 1]$ 上的 WAT 的证明，并接着将其推广到一般的任意区间 $[a, b]$。

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

> [!question] 练习 6.7.9
> 
> (a) 找一个反例表明如果我们将闭区间 $[a, b]$ 替换为开区间 $(a, b)$，则 WAT 不再成立。
> 
> (b) 如果我们将 $[a, b]$ 替换为闭集 $[a, \infty)$ 会怎样？定理仍然成立吗？

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

> [!question] 练习 6.7.10
> 
> 是否存在多项式的一个可数子集 $\mathcal{C}$，具有能够让 $[a, b]$ 上的每个连续函数都能被 $\mathcal{C}$ 中的多项式一致逼近的性质？

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

> [!question] 练习 6.7.11
> 
> 假设 $f$ 在 $[a, b]$ 上有连续的导数。证明存在一个多项式 $p(x)$ 使得
> 
> $$ |f(x) - p(x)| < \varepsilon \quad \text{并且} \quad |f'(x) - p'(x)| < \varepsilon $$
> 
> 对所有 $x \in [a, b]$ 成立。

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

---

## 6.8 结语 (Epilogue)

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