#!/usr/bin/env python3
"""
九经书院前端HTML验证脚本
检查HTML结构、标签闭合、属性规范
"""

import re
import sys
from pathlib import Path

def validate_html(filepath):
    """验证HTML文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    warnings = []
    
    # 1. 检查文档类型
    if not content.strip().startswith('<!DOCTYPE html>'):
        issues.append("❌ 缺少或错误的DOCTYPE声明")
    else:
        print("✅ DOCTYPE声明正确")
    
    # 2. 检查charset
    if 'charset="UTF-8"' not in content and "charset='UTF-8'" not in content:
        issues.append("❌ 缺少charset=UTF-8声明")
    else:
        print("✅ Charset声明正确")
    
    # 3. 检查viewport
    if 'viewport' not in content:
        issues.append("❌ 缺少viewport meta标签")
    else:
        print("✅ Viewport meta标签存在")
    
    # 4. 检查lang属性
    if '<html lang="zh-CN"' not in content:
        warnings.append("⚠️  建议为html标签添加lang='zh-CN'属性")
    else:
        print("✅ HTML lang属性正确")
    
    # 5. 检查标题
    title_match = re.search(r'<title>(.*?)</title>', content)
    if not title_match:
        issues.append("❌ 缺少title标签")
    else:
        print(f"✅ Title存在: '{title_match.group(1)}'")
    
    # 6. 检查标签闭合
    self_closing = ['meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'area', 'base', 'col', 'embed', 'param', 'track', 'wbr']
    
    # 统计开闭标签
    open_tags = re.findall(r'<([a-z][a-z0-9]*)[^>]*?(?<!/)>', content, re.IGNORECASE)
    close_tags = re.findall(r'</([a-z][a-z0-9]*)>', content, re.IGNORECASE)
    self_close = re.findall(r'<([a-z][a-z0-9]*)[^>]*?/>', content, re.IGNORECASE)
    
    # 过滤自闭合标签
    open_tags = [t for t in open_tags if t.lower() not in self_closing]
    
    from collections import Counter
    open_count = Counter(t.lower() for t in open_tags)
    close_count = Counter(t.lower() for t in close_tags)
    
    unclosed = []
    for tag, count in open_count.items():
        if count > close_count.get(tag, 0):
            unclosed.append(f"<{tag}> 标签未闭合 (开{count} / 闭{close_count.get(tag, 0)})")
    
    if unclosed:
        for u in unclosed:
            issues.append(f"❌ {u}")
    else:
        print("✅ 所有标签正确闭合")
    
    # 7. 检查alt属性（图片相关）
    if '<img' in content:
        imgs = re.findall(r'<img[^>]*>', content)
        missing_alt = [img for img in imgs if 'alt=' not in img]
        if missing_alt:
            warnings.append(f"⚠️  发现 {len(missing_alt)} 个img标签缺少alt属性")
        else:
            print("✅ 所有img标签都有alt属性")
    
    # 8. 检查语义化标签
    semantic_tags = ['header', 'nav', 'main', 'article', 'section', 'aside', 'footer']
    found_semantic = [tag for tag in semantic_tags if f'<{tag}' in content.lower()]
    if len(found_semantic) >= 3:
        print(f"✅ 语义化标签使用良好 ({', '.join(found_semantic)})")
    else:
        warnings.append(f"⚠️  建议增加语义化标签 (当前: {', '.join(found_semantic) if found_semantic else '无'})")
    
    # 报告
    print("\n" + "="*50)
    print("📋 HTML验证报告")
    print("="*50)
    
    if issues:
        print(f"\n🔴 发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"  {issue}")
    
    if warnings:
        print(f"\n🟡 发现 {len(warnings)} 个警告:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not issues and not warnings:
        print("\n🎉 完美！没有发现任何问题")
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
    
    print(f"🧪 正在验证: {html_file}\n")
    exit_code = validate_html(html_file)
    sys.exit(exit_code)
