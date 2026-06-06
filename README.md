# 🎯 Icon Tools

AI图标工具，支持图标建议、SVG生成、图标集。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💡 图标建议
- 🎨 SVG图标生成
- 📦 图标集生成
- 🔄 格式转换
- 🌐 Favicon生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from icon_tools import create_tools

tools = create_tools()

# 建议图标
icons = tools.suggest_icons("电商网站", 5)

# 生成SVG
svg = tools.generate_svg_icon("购物车", "outline")

# 生成图标集
icon_set = tools.generate_icon_set("社交媒体", 10)

# 转换格式
react = tools.convert_icon(svg, "React组件")

# 生成Favicon
favicon = tools.generate_favicon("MyBrand", "minimal")
```

## 📁 项目结构

```
icon-tools/
├── tools.py       # 图标工具核心
└── README.md
```

## 📄 许可证

MIT License
