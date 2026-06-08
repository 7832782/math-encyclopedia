---
title: y=Asin(ωx+φ)的图象变换
tags:
  - 数学
  - 高中
  - 三角函数
aliases:
  - 三角函数图象变换
  - 振幅变换
  - 相位变换
  - 周期变换
description: 正弦型函数 y=Asin(ωx+φ) 的振幅、周期、相位和图象变换规律
---


## 参数含义

$$y = A\sin(\omega x + \varphi) + k$$

| 参数 | 含义 | 影响 |
|------|------|------|
| $A$ | **振幅** | 最大位移 $|A|$ |
| $\omega$ | **角频率** | 周期 $T = \dfrac{2\pi}{|\omega|}$ |
| $\varphi$ | **初相** | 左右平移量 |
| $k$ | **竖直偏移** | 上下平移量 |

## 由 $y = \sin x$ 到 $y = A\sin(\omega x + \varphi) + k$

### 变换顺序（先平移后伸缩）

1. **左右平移**：$y = \sin(x + \varphi)$（左加右减）
2. **横向伸缩**：$y = \sin(\omega x + \varphi)$（横坐标变为 $\dfrac{1}{\omega}$）
3. **纵向伸缩**：$y = A\sin(\omega x + \varphi)$（纵坐标变为 $A$ 倍）
4. **上下平移**：$y = A\sin(\omega x + \varphi) + k$（上加下减）

> [!warning] 注意
> 先伸缩后平移时，平移量为 $\dfrac{\varphi}{\omega}$ 而非 $\varphi$！

## 典型例题

**例**：将 $y = \sin x$ 的图象向右平移 $\dfrac{\pi}{3}$ 个单位，再将横坐标压缩为原来的 $\dfrac{1}{2}$，求所得函数解析式

> [!details]- 解答
> 右移 $\dfrac{\pi}{3}$：$y = \sin(x - \dfrac{\pi}{3})$  
> 横坐标 $\times \dfrac{1}{2}$：$y = \sin(2x - \dfrac{\pi}{3})$
