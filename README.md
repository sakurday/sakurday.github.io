# 棱镜笔记

一个采用 Material Design 3 的个人博客。导航、按钮、主题开关、分隔线，以及文章卡片的点击波纹和键盘焦点指示使用 Google 的 Material Web 组件。GitHub Pages 内置的 Jekyll 在构建时读取 `_posts/` 中的 Markdown 文件，自动更新首页文章列表，并为每篇文章生成独立的页面。

## 写一篇文章

在 `_posts/` 下新建 UTF-8 文件，命名为 `YYYY-MM-DD-my-post.md`。使用当天或过去的日期。用英文短横线分隔文件名中的单词，中文标题写在文件开头。

```markdown
---
title: "我的第一篇文章"
description: "出现在首页卡片上的简短摘要"
topic: 随笔
icon: note
---

在这里写正文。

## 一个小标题

支持列表、表格和代码块。
```

`description`、`topic` 和 `icon` 都可省略。首页默认用正文首段作摘要。图标可以选 `note`、`design` 或 `code`。文章标题由页面模板显示，正文小节从二级标题开始。

站名和简介在 `_config.yml`，关于页正文在 `about.md`，主页大标题在 `index.html`。如果文章要使用本地图片，可以把图片放在 `assets/`，在 Markdown 中写 `![图片说明]({{ '/assets/photo.png' | relative_url }})`，这样项目站点的仓库路径也会自动加到图片地址上。

## 发布到 GitHub Pages

1. 把这个目录里的源文件推送到 GitHub 仓库的 `main` 分支。
2. 在仓库的 **Settings → Pages** 中选择 **Deploy from a branch**，选中 `main` 和 `/(root)` 后保存。
3. 构建完成后，在 **Pages** 设置中打开站点地址。以后把新增或修改的 Markdown 文件推送到发布分支，站点会自动重新构建。

可以使用 `用户名.github.io` 仓库，也可以使用普通项目仓库。模板中的内部链接通过 Jekyll 的 `relative_url` 适配站点路径。

[GitHub Pages 发布源文档](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## 本地预览

安装 Ruby 和 Bundler 后，在项目根目录运行下面的命令。Windows 可使用带 Devkit 的 RubyInstaller。

```sh
bundle install
bundle exec jekyll serve
```

Windows 上安装依赖后，也可以双击 `run.bat` 启动。打开 `http://127.0.0.1:4000/`。保存 Markdown 或 HTML 后，Jekyll 会重新构建，刷新浏览器即可看到更新。改动 `_config.yml` 后需要重新启动预览。

如果要模拟项目仓库的子路径，可以运行 `bundle exec jekyll serve --baseurl /my-blog`，然后打开 `http://localhost:4000/my-blog/`。

## 更新 Material Web

`assets/vendor/material-web.js` 是随站点发布的组件脚本。改文章或发布站点时可以直接使用它。要重新生成组件脚本，使用 Node.js 运行以下命令，再提交生成的脚本和许可证文件。

```sh
npm ci
npm run build:material
```
