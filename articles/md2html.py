#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把当前目录下所有 .md 文件转换为 .html 文件。

规则：
- 只改后缀名，如 1.md -> 1.html；已存在的 html 文件直接覆盖。
- <title> 使用 markdown 中第一个一级标题(#)的文字；若没有一级标题则用 "title"。
- markdown 元素通过 markdown 库转换为 html 元素。
"""

import html
import os
import re

import markdown


def extract_title(md_text):
    """取第一个一级标题(#)的文字，去掉常见行内 markdown 符号；找不到返回 None。"""
    m = re.search(r"^#\s+(.+?)\s*$", md_text, re.MULTILINE)
    if not m:
        return None
    title = m.group(1).strip()
    title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", title)  # [文字](url) -> 文字
    for ch in ("**", "*", "`", "_", "\\"):
        title = title.replace(ch, "")
    return title.strip()


def md_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    title = html.escape(extract_title(md_text) or "title")
    body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "sane_lists"],
    )
    return f"""<html>

<head>
<link rel="stylesheet" href="../style.css">
<meta charset="utf-8">
<title>{title}</title>
</head>

<body>
<a href="../">返回主页</a>
{body}
</body>

</html>
"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__)) or os.getcwd()
    md_files = [
        name for name in os.listdir(script_dir) if name.lower().endswith(".md")
    ]
    if not md_files:
        print("没有找到 markdown 文件。")
        return

    for name in sorted(md_files):
        md_path = os.path.join(script_dir, name)
        html_name = os.path.splitext(name)[0] + ".html"
        html_path = os.path.join(script_dir, html_name)
        html_text = md_to_html(md_path)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_text)
        print(f"{name} -> {html_name}")


if __name__ == "__main__":
    main()
