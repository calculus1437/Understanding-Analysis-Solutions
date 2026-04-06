@import "style.less"

## 习题 6.6 泰勒级数

我们对幂级数的研究得出了一些关于以下形式函数的性质的有趣结论

$$
f\left( x\right)  = {a}_{0} + {a}_{1}x + {a}_{2}{x}^{2} + {a}_{3}{x}^{3} + {a}_{4}{x}^{4} + \cdots .
$$

尽管幂级数具有无限项，但它们可以像多项式一样进行各种操作。在其收敛区间内，幂级数是连续且无限可微的，并且可以通过对级数中的每一项执行所需操作来计算逐次导数，就像对多项式所做的那样。正如我们将在下一章中看到的，幂级数的积分理论同样令人满意。正如初学微积分的学生所熟知的那样，当仅应用于多项式时，积分和微分的过程以及基本的代数操作都相当直接。正是诸如 $\sin \left( x\right)$ 、 $\ln \left( x\right)$ 和 $\arctan \left( x\right)$ 等函数的引入，才需要在一、二学期的微积分课程中教授许多符号技巧。这种现象促使我们思考，像 $\arctan \left( x\right)$ 这样的函数是否具有幂级数表示。

在本节的示例中，我们将假设所有熟悉的三角函数、反三角函数、指数函数和对数函数的性质。严格定义这些函数是分析中的一个有趣练习。事实上，提供定义的最常见方法之一是通过幂级数。然而，本讨论的重点是从另一个方向来探讨这个问题。假设我们拥有一个无限可微的函数，如 $\arctan \left( x\right)$ ，我们能否找到合适的系数 ${a}_{n}$ ，使得至少对于一些非零的 $x$ 值成立：

$$
\arctan \left( x\right)  = {a}_{0} + {a}_{1}x + {a}_{2}{x}^{2} + {a}_{3}{x}^{3} + {a}_{4}{x}^{4} + \cdots
$$

### 操作级数
我们已经有一个熟悉函数的幂级数展开的例子。在第2章例2.7.5的无穷级数材料中，我们证明了 $\forall t \in  \left( {-1,1}\right)$

$$
\frac{1}{1 - t} = 1 + t + {t}^{2} + {t}^{3} + {t}^{4} + \cdots
$$

将 $- {t}^{2}$ 代入 $t$ 得到

$$
\frac{1}{1 + {t}^{2}} = 1 - {t}^{2} + {t}^{4} - {t}^{6} + {t}^{8} - \cdots .
$$

但现在我们可以利用以下事实:

$$
\arctan \left( x\right)  = {\int }_{0}^{x}\frac{1}{1 + {t}^{2}}{dt}
$$

尽管目前尚未对积分进行严格研究，但我们将在第7章中看到，如果 ${f}_{n} \rightarrow  f$ 在区间 $\left\lbrack  {a,b}\right\rbrack$ 上一致，则 ${\int }_{a}^{b}{f}_{n} \rightarrow  {\int }_{a}^{b}f$ 。这一观察结果，结合微积分基本定理，得出公式

$$
\arctan \left( x\right)  = x - \frac{1}{3}{x}^{3} + \frac{1}{5}{x}^{5} - \frac{1}{7}{x}^{7} + \cdots .
$$

> [!question] 练习 6.6.1
> 第七章即将得出的结果将证明这个方程对所有 $x \in  \left( {-1,1}\right)$ 都成立，但请注意，当 $x = 1$ 时，这个级数实际上收敛。假设 $\arctan \left( x\right)$ 是连续的，解释为什么在 $x = 1$ 处级数的值必然是 $\arctan \left( 1\right)$ 。在这种情况下，我们得到了什么有趣的身份？

<br/>

> [!question] 练习 6.6.2
> 从本节方程 (6.6.1) 中的恒等式出发，找到 $\ln \left( {1 + x}\right)$ 的幂级数表示。对于哪些 $x$ 值，这个表达式是有效的？

<br/>

### Taylor公式的系数
在17和18世纪，当无穷级数的实用性首次被认识到时，通过操作旧级数来生成新级数是一种非常熟练的技艺。但也出现了一种从“零开始”生成系数的公式——一种仅使用所讨论的函数及其导数来生成幂级数表示的方法。该技术以数学家 Brook Taylor (1685-1731)的名字命名，他于1715年发表了这一方法，尽管在此之前它肯定已经被人们所知。

给定一个在某个以零为中心的区间上定义的无限可微函数 $f$ ，其思想是假设 $f$ 具有幂级数展开，并推导出系数必须是什么；即写出

$$
f\left( x\right)  = {a}_{0} + {a}_{1}x + {a}_{2}{x}^{2} + {a}_{3}{x}^{3} + {a}_{4}{x}^{4} + {a}_{5}{x}^{5} + \cdots .
$$

在此表达式中设置 $x = 0$ 便得到 $f\left( 0\right)  = {a}_{0}$ 。

> [!question] 练习 6.6.3
> (a) 对方程(6.6.2)的每一边求导，并推导出 ${f}^{\prime }\left( 0\right)  = {a}_{1}$ 。一般来说，证明如果 $f$ 具有幂级数展开，则系数必须由公式给出
>
> $$
> {a}_{n} = \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}.
> $$
>
> 提供证明对公式(6.6.2)中级数进行操作的定理的参考文献。

<br/>

提供证明对公式(6.6.2)中级数进行操作的定理的参考文献。

> [!question] 练习 6.6.4
> 使用前一个练习中 ${a}_{n}$ 的Taylor公式来生成/验证所谓的 $\sin \left( x\right)$ 的Taylor级数，其形式为
>
> $$
> \sin \left( x\right)  \sim  x - \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} - \frac{{x}^{7}}{7!} + \cdots .
> $$

<br/>

### Lagrange余项
我们需要非常清楚到目前为止我们证明了什么。为了推导Taylor公式，我们假设 $f$ 实际上有一个幂级数表示。结论是，如果 $f$ 在以零为中心的区间上无限可微，并且如果 $f$ 可以表示为

$$
f\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}
$$

那么它必须是

$$
{a}_{n} = \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}.
$$

但反过来呢？假设 $f$ 在零的邻域内无限可微。如果我们令

$$
{a}_{n} = \frac{{f}^{\left( n\right) }\left( 0\right) }{n!},
$$

结果级数

$$
\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}
$$

是否在某些非平凡的点集上收敛到 $f\left( x\right)$ ？它是否收敛？如果它确实收敛，我们知道极限函数是一个表现良好、无限可微的函数，其在零点的导数与 $f$ 的导数完全相同。这个极限是否可能不同于 $f$ ？换句话说，函数 $f$ 的Taylor级数是否会收敛到错误的东西？令

$$
{S}_{N}\left( x\right)  = {a}_{0} + {a}_{1}x + {a}_{2}{x}^{2} + \cdots  + {a}_{N}{x}^{N}.
$$

多项式 ${S}_{N}\left( x\right)$ 是函数 $f\left( x\right)$ 的Taylor级数展开的部分和。因此，我们感兴趣的是

$$
\mathop{\lim }\limits_{{N \rightarrow  \infty }}{S}_{N}\left( x\right)  = f\left( x\right)
$$

对于除零以外的某些 $x$ 值。Joseph Louis Lagrange (1736-1813)提供了一个强大的工具来分析这个问题。这个想法是考虑差值

$$
{E}_{N}\left( x\right)  = f\left( x\right)  - {S}_{N}\left( x\right) ,
$$

它表示 $f$ 与部分和 ${S}_{N}$ 之间的误差。

**定理（Lagrange余项）**
设 $f$ 在$(-R, R)$上无限可微，定义 ${a}_{n} = {f}^{\left( n\right) }\left( 0\right) /n!$ ，并令

$$
{S}_{N} = {a}_{0} + {a}_{1}x + {a}_{2}{x}^{2} + \cdots  + {a}_{N}{x}^{N}.
$$

给定 $x \neq  0$ ，存在一个点 $c$ 满足 $\left| c\right|  < \left| x\right|$ ，其中误差函数 ${E}_{N}\left( x\right)  = f\left( x\right)  - {S}_{N}\left( x\right)$ 满足

$$
{E}_{N}\left( x\right)  = \frac{{f}^{\left( N + 1\right) }\left( c\right) }{\left( {N + 1}\right) !}{x}^{N + 1}.
$$

在开始证明之前，让我们先审视这一结果的意义。证明 ${S}_{N}\left( x\right)  \rightarrow  f\left( x\right)$ 等同于展示 ${E}_{N}\left( x\right)  \rightarrow  0$ 。对于 ${E}_{N}\left( x\right)$ 的表达式，有三个组成部分。在分母中，我们有 $\left( {N + 1}\right)$ !，这有助于使 ${E}_{N}$ 随着 $N$ 趋向于无穷大而变小。在分子中，我们有 ${x}^{N + 1}$ ，它可能会根据 $x$ 的大小而增长。因此，我们应该预期，Taylor级数在 $x$ 离原点越远时越不可能收敛。最后，我们有 ${f}^{\left( N + 1\right) }\left( c\right)$ ，这有点神秘。对于具有直接导数的函数，这一项通常可以通过使用适当的上界来处理。

**例**
  考虑之前生成的 $\sin \left( x\right)$ 的Taylor级数：
$$
{S}_{5}\left( x\right)  = x - \frac{1}{3!}{x}^{3} + \frac{1}{5!}{x}^{5}
$$
  如何很好地在区间 $\left\lbrack  {-2,2}\right\rbrack$ 上近似 $\sin \left( x\right)$ 。Lagrange余项定理断言，这两个函数之间的差为

$$
{E}_{5}\left( x\right)  = \sin \left( x\right)  - {S}_{5}\left( x\right)  = \frac{-\cos \left( c\right) }{6!}{x}^{6}
$$

对于区间 $\left( {-\left| x\right| ,\left| x\right| }\right)$ 中的某个 $c$ ，我们无法知道 $c$ 的值，但可以非常确定 $\left| {\cos \left( c\right) }\right|  \leq  1$ 。因为 $x \in  \left\lbrack  {-2,2}\right\rbrack$ ，我们有

$$
\left| {{E}_{5}\left( x\right) }\right|  \leq  \frac{{2}^{6}}{6!} \approx  {.089}
$$  

> [!question] 练习 6.6.5
> 证明 ${S}_{N}\left( x\right)$ 在 $\left\lbrack  {-2,2}\right\rbrack$ 上一致收敛于 $\sin \left( x\right)$ 。将此证明推广到证明在形如 $\left\lbrack  {-R,R}\right\rbrack$ 的任何区间上收敛是一致的。

<br/>

> [!question] 练习 6.6.6
> (a) 生成指数函数 $f\left( x\right)  = {e}^{x}$ 的Taylor系数，然后证明相应的Taylor级数在形如 $\left\lbrack  {-R,R}\right\rbrack$ 的任何区间上一致收敛于 ${e}^{x}$ 。
>
> (b) 验证公式 ${f}^{\prime }\left( x\right)  = {e}^{x}$ 。
>
> 使用代换生成 ${e}^{-x}$ 的级数，然后通过将两个级数相乘并收集 $x$ 的相同幂次来计算 ${e}^{x} \cdot  {e}^{-x}$ 。

<br/>

Lagrange余项定理的证明:回顾第5章中的广义中值定理(定理5.3.5)。

> [!question] 练习 6.6.7
> 解释为什么误差函数 ${E}_{N}\left( x\right)  = {f}_{N}\left( x\right)  - {S}_{N}\left( x\right)$ 满足
>
> $$
> {E}_{N}^{\left( n\right) }\left( 0\right)  = 0\;\text{ for all }n = 0,1,2,\ldots ,N.
> $$
>
> 为了简化符号，假设 $x > 0$ 并将广义中值定理应用于函数 ${E}_{N}\left( x\right)$ 和 ${x}^{N + 1}$ 在区间 $\left\lbrack  {0,x}\right\rbrack$ 上。因此，存在一个点 ${x}_{1} \in  \left( {0,x}\right)$ 使得
>
> $$
> \frac{{E}_{N}\left( x\right) }{{x}^{N + 1}} = \frac{{E}_{N}^{\prime }\left( {x}_{1}\right) }{\left( {N + 1}\right) {x}_{1}^{N}}.
> $$

<br/>

> [!question] 练习 6.6.8
> 完成Lagrange余项定理的证明。

<br/>

### 一个反例
Lagrange余项在确定Taylor级数的部分和如何近似原函数方面极为有用，但它未能解决核心问题，即Taylor级数是否必然收敛于生成它的函数。误差公式中出现的第 $n$ 阶导数 ${f}^{\left( n\right) }\left( c\right)$ 使得任何一般性陈述都变得不可能。事实上，还有其他几种方法可以表示部分和 ${S}_{N}\left( x\right)$ 与函数 $f\left( x\right)$ 之间的误差，但没有一种方法能够证明 ${S}_{N} \rightarrow  f$ 。这是因为这样的证明根本不存在！

考虑函数

$$
g\left( x\right)  = \left\{  \begin{array}{ll} {e}^{-1/{x}^{2}} & x \neq  0, \\  0 & x = 0. \end{array}\right\}.
$$

在接下来的练习中，我们将需要熟悉的公式 $\frac{d}{dx}{e}^{x} = {e}^{x}$ 以及 ${e}^{-x} = 1/{e}^{x}$ 的性质。(注意，我们可以使用练习6.6.6中生成的级数作为指数函数 ${e}^{x}$ 的定义。本练习的(b)和(c)部分验证了该级数具有这些性质。)尽管我们已经证明了所有标准的微分规则，但这些规则都不能直接用于计算 $g$ 在 $x = 0$ 处的导数。

> [!question] 练习 6.6.9
> 使用 $\infty /\infty$ 版本的 L'Hospital 法则(定理5.3.8)证明 ${g}^{\prime }\left( 0\right)  = 0$ 。

<br/>

> [!question] 练习 6.6.10
> 计算 ${g}^{\prime }\left( x\right)$ 对于 $x \neq  0$ 。计算 ${g}^{\prime \prime }\left( x\right)$ 和 ${g}^{\prime \prime \prime }\left( x\right)$ 对于 $x \neq  0$ 。利用这些观察结果，并发明所需的符号，给出 $n$ 阶导数 ${g}^{\left( n\right) }\left( x\right)$ 在非零点的一般描述。

<br/>

现在，

$$
{g}^{\prime \prime }\left( 0\right)  = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{{g}^{\prime }\left( x\right)  - {g}^{\prime }\left( 0\right) }{x - 0} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{{g}^{\prime }\left( x\right) }{x}.
$$

> [!question] 练习 6.6.11
> 计算 ${g}^{\prime \prime }\left( 0\right)$ 。从这个例子中，提出一个关于如何计算 ${g}^{\left( n\right) }\left( 0\right)$ 的一般论证。
> 
> 讨论此示例的后果。 $g$ 是否无限可微？它的Taylor级数是什么样子的？这个级数在哪些点收敛？收敛到什么？这个示例对每个无限可微函数都可以由其Taylor级数展开表示的猜想有何影响？

<br/>

---
