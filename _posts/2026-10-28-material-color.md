---
title: 用 Material 3 给界面配色
description: 从主色出发，用颜色角色组织按钮、卡片和背景，让浅色与深色主题保持一致。
topic: 设计
icon: design
---

给界面配色时，先想清楚每个颜色在页面上负责什么。主色可以标出最重要的动作，卡片与背景则用不同的表面色建立层次。

## 从颜色角色开始

| 角色 | 在本站的用法 |
| --- | --- |
| `primary` 与 `on-primary` | 首页主按钮的背景与文字 |
| `primary-container` | 首页介绍区域的底色 |
| `surface-container-low` | 文章卡片的底色 |
| `on-surface-variant` | 日期和摘要等辅助文字 |

在 CSS 里，用变量保存角色的颜色。组件可以沿用同一组变量名，切换主题时只需改变变量的取值。

```css
.button {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
}
```

## 在真实内容上检查

把一篇较长的文章放进页面，再看正文、代码和辅助文字在两种主题下是否都清楚。键盘操作时，也留意焦点轮廓能否从相邻的表面色中辨认出来。

延伸阅读 [Material Design 3 的颜色角色](https://m3.material.io/styles/color/the-color-system/)。
