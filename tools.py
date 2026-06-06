"""
Icon Tools - AI图标工具
支持图标建议、SVG生成、图标集
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class IconTools:
    """
    AI图标工具
    支持：建议、生成、图标集
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def suggest_icons(self, context: str, count: int = 5) -> List[Dict]:
        """建议图标"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为以下场景建议{count}个图标：

场景：{context}

请返回JSON格式：
[
    {{"name": "图标名", "description": "描述", "unicode": "unicode", "library": "推荐库"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"suggestion": content}]

    def generate_svg_icon(self, description: str, style: str = "outline") -> str:
        """生成SVG图标"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{style}风格的SVG图标：

描述：{description}

要求：
1. 简洁现代
2. 24x24尺寸
3. 可直接使用
4. 只返回SVG代码"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_icon_set(self, theme: str, count: int = 10) -> List[Dict]:
        """生成图标集"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请生成{theme}主题的{count}个图标：

请返回JSON格式：
[
    {{"name": "图标名", "svg": "SVG代码", "description": "描述"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"icon_set": content}]

    def convert_icon(self, icon_svg: str, target_format: str) -> str:
        """转换图标格式"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下SVG图标转换为{target_format}格式：

{icon_svg}

只返回转换后的代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_favicon(self, brand_name: str, style: str = "minimal") -> str:
        """生成Favicon"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{brand_name}生成{style}风格的favicon SVG：

要求：
1. 32x32尺寸
2. 简洁明了
3. 可识别
4. 只返回SVG代码"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> IconTools:
    """创建图标工具"""
    return IconTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Icon Tools")
    print()

    # 测试
    icons = tools.suggest_icons("电商网站导航", 5)
    print(json.dumps(icons, ensure_ascii=False, indent=2))
