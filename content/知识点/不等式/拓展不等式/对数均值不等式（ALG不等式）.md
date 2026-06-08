---
title: 对数均值不等式（ALG不等式）（拓展）
tags:
  - 数学
  - 高中
  - 不等式
  - 拓展
aliases:
  - ALG不等式
  - 对数平均
description: 几何平均数 < 对数平均数 < 算术平均数——连接三种均值的桥梁
---


## 核心不等式

对于 $a \neq b, a > 0, b > 0$：

$$\boxed{\sqrt{ab} < \dfrac{a - b}{\ln a - \ln b} < \dfrac{a + b}{2}}$$

| 符号 | 名称 | 含义 |
|:---:|------|------|
| A | 算术平均 | $\dfrac{a+b}{2}$ |
| L | 对数平均 | $\dfrac{a-b}{\ln a - \ln b}$ |
| G | 几何平均 | $\sqrt{ab}$ |

即：$G < L < A$（**不能取等**）

## 证明要点

令 $\dfrac{a}{b} = t > 1$（不妨设 $a > b$），化为：

$$\ln t > 2\dfrac{t-1}{t+1} \quad (t > 1)$$

构造函数 $f(t) = \ln t - 2\dfrac{t-1}{t+1}$，求导证明 $f(t) > 0$。

另半部分 $\dfrac{a-b}{\ln a - \ln b} > \sqrt{ab}$ 同理可证。

## 完整均值不等式链

$$\dfrac{2}{\dfrac{1}{a} + \dfrac{1}{b}} \leq \sqrt{ab} \leq \dfrac{a-b}{\ln a - \ln b} \leq \dfrac{a+b}{2} \leq \sqrt{\dfrac{a^2 + b^2}{2}}$$

调和 ≤ 几何 < 对数 < 算术 ≤ 平方

## 应用场景

- 导数压轴题中证明含 $\ln$ 的不等式
- 比较含对数和对数的表达式大小

## 与其他概念的关系

- **上级专题**：[[知识点/不等式|不等式]]
- **相关概念**：[[放缩技巧]]、[[不等式证明（导数法）]]
