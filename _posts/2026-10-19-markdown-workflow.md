---
title: 一篇 Markdown 如何变成网页
description: 从写下第一行到发布新文章，看看 GitHub Pages 和 Jekyll 怎样接力完成这件事。
topic: 开发
icon: code
---

这个博客的文章都在 `_posts` 目录中。每篇文章有一个单独的 Markdown 文件，开头用几行 YAML 记录标题等信息，后面就是正文。

## 新建一篇文章

以 `2026-10-19-markdown-workflow.md` 为例，文件名开头的日期决定了默认的发布时间。文件开头的内容可以写成这样。

```yaml
---
title: 一篇 Markdown 如何变成网页
description: 记录这篇文章要谈的内容。
topic: 开发
---
```

## 从文件到页面

1. Jekyll 从 `_posts` 发现文章，并按日期整理。
2. 构建时把 Markdown 正文转换成 HTML，并套用文章布局。
3. 首页根据相同的文章数据生成列表，访客可以直接打开每篇文章的独立地址。

[查看 GitHub 的 Jekyll 写作指南](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)。
