#!/usr/bin/env python3
"""
九经书院CSS样式验证脚本
检查CSS语法、颜色对比度、响应式设计
"""

import re
import sys
from pathlib import Path

def hex_to_rgb(hex_color):
    """将十六进制颜色转换为RGB"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def luminance(rgb):
    """计算相对亮度"""
    def adjust(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def contrast_ratio(color1, color2):
    """计算两个颜色的对比度"""
    l1 = luminance(hex_to_rgb(color1))
    l2 = luminance(hex_to_rgb(color2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def validate_css_in_html(filepath):
    """验证HTML中的CSS"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    warnings = []
    suggestions = []
    
    # 提取style标签内容
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        issues.append("❌ 没有找到<style>标签")
        return 1
    
    css = style_match.group(1)
    print("✅ 找到CSS样式块\n")
    
    # 1. 检查响应式断点
    if '@media' in css:
        print("✅ 发现响应式设计 (@media查询)")
        media_queries = re.findall(r'@media[^{]+', css)
        for mq in media_queries:
            print(f"  📱 {mq.strip()}")
    else:
        warnings.append("⚠️  缺少响应式设计 (无@media查询)")
    
    # 2. 检查颜色使用
    colors = re.findall(r'#[a-fA-F0-9]{3,6}', css)
    unique_colors = list(set(c.lower() for c in colors))
    print(f"\n🎨 发现 {len(unique_colors)} 种颜色:")
    for c in unique_colors:
        print(f"   {c}")
    
    # 3. 检查关键颜色对比度
    # 背景色和文字色
    bg_colors = re.findall(r'background[^:]*:\s*(#[a-fA-F0-9]{3,6}|\w+)', css)
    text_colors = re.findall(r'color:\s*(#[a-fA-F0-9]{3,6})', css)
    
    # 检查白色背景上的棕色文字对比度
    brown_colors = ['#8b4513', '#654321', '#5d4e37']
    for brown in brown_colors:
        if brown in unique_colors:
            ratio = contrast_ratio('#ffffff', brown)
            if ratio >= 4.5:
                print(f"✅ 颜色对比度合格: {brown} on white = {ratio:.2f}:1")
            else:
                warnings.append(f"⚠️  颜色对比度偏低: {brown} on white = {ratio:.2f}:1 (建议≥4.5:1)")
    
    # 4. 检查布局使用
    print("\n📐 布局技术:")
    if 'grid' in css:
        print("  ✅ CSS Grid 布局")
    if 'flex' in css:
        print("  ✅ Flexbox 布局")
    
    # 5. 检查过渡和动画
    if 'transition' in css:
        transitions = re.findall(r'transition:\s*([^;]+)', css)
        print(f"\n✨ 发现 {len(transitions)} 个过渡效果")
    
    if 'animation' in css or '@keyframes' in css:
        print("✨ 发现动画效果")
    else:
        suggestions.append("💡 建议添加hover动画增强交互体验")
    
    # 6. 检查字体
    fonts = re.findall(r'font-family:\s*([^;]+)', css)
    if fonts:
        print(f"\n🔤 字体设置:")
        for f in fonts[:3]:  # 只显示前3个
            print(f"  {f.strip()}")
    
    # 7. 检查CSS语法问题
    # 检查是否有未闭合的括号
    open_braces = css.count('{')
    close_braces = css.count('}')
    if open_braces != close_braces:
        issues.append(f"❌ CSS括号不匹配 (开{open_braces} / 闭{close_braces})")
    else:
        print(f"\n✅ CSS语法检查通过 (括号匹配: {open_braces})")
    
    # 8. 检查!important使用
    important_count = css.count('!important')
    if important_count > 5:
        warnings.append(f"⚠️  使用了 {important_count} 个!important，建议减少")
    elif important_count > 0:
        print(f"✅ !important使用合理 ({important_count}个)")
    
    # 报告
    print("\n" + "="*50)
    print("📋 CSS验证报告")
    print("="*50)
    
    if issues:
        print(f"\n🔴 发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"  {issue}")
    
    if warnings:
        print(f"\n🟡 发现 {len(warnings)} 个警告:")
        for warning in warnings:
            print(f"  {warning}")
    
    if suggestions:
        print(f"\n💡 建议:")
        for s in suggestions:
            print(f"  {s}")
    
    if not issues and not warnings:
        print("\n🎉 CSS完美！没有发现问题")
        return 0
    elif not issues:
        print("\n✅ 没有严重问题，建议处理警告")
        return 0
    else:
        print(f"\n❌ 共有 {len(issues)} 个严重问题需要修复")
        return 1

if __name__ == '__main__':
    frontend_dir = Path('/mnt/d/Jiujing-Academy/frontend')
    html_file = frontend_dir / 'index.html'
    
    if not html_file.exists():
        print(f"❌ 找不到文件: {html_file}")
        sys.exit(1)
    
    print(f"🧪 正在验证CSS: {html_file}\n")
    exit_code = validate_css_in_html(html_file)
    sys.exit(exit_code)
