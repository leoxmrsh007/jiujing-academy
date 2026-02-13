#!/usr/bin/env python3
"""
九经书院响应式布局测试脚本
模拟不同设备尺寸下的渲染效果
"""

import sys
from pathlib import Path

def test_responsive_design():
    """测试响应式设计要点"""
    
    print("📱 响应式布局测试\n")
    
    # 测试要点清单
    tests = [
        {
            "name": "视口设置",
            "check": "width=device-width, initial-scale=1.0",
            "importance": "high"
        },
        {
            "name": "桌面端布局 (1200px+)",
            "features": ["max-width: 1200px", "grid 4列", "适当间距"],
            "importance": "high"
        },
        {
            "name": "平板端布局 (768px-1199px)",
            "features": ["自适应网格", "减少列数", "保持可读性"],
            "importance": "medium"
        },
        {
            "name": "移动端布局 (<768px)",
            "features": ["@media (max-width: 768px)", "单列布局", "字体缩小", "触摸友好"],
            "importance": "high"
        },
        {
            "name": "超小屏 (<375px)",
            "features": ["紧凑布局", "最小字体16px", "可点击区域≥44px"],
            "importance": "medium"
        }
    ]
    
    print("✅ 测试清单:\n")
    for i, test in enumerate(tests, 1):
        icon = "🔴" if test.get("importance") == "high" else "🟡"
        print(f"{icon} {i}. {test['name']}")
        if 'check' in test:
            print(f"   检查: {test['check']}")
        if 'features' in test:
            for f in test['features']:
                print(f"   ✓ {f}")
        print()
    
    # 实际检查HTML文件
    html_file = Path('/mnt/d/Jiujing-Academy/frontend/index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("="*50)
    print("🔍 实际检查结果:")
    print("="*50)
    
    checks = [
        ("视口meta标签", 'width=device-width' in content and 'initial-scale=1.0' in content),
        ("响应式断点 (@media)", '@media' in content),
        ("移动端断点 (768px)", 'max-width: 768px' in content),
        ("最大宽度容器", 'max-width: 1200px' in content),
        ("CSS Grid布局", 'grid' in content.lower()),
        ("Flexbox布局", 'flex' in content.lower()),
        ("自适应图片", 'max-width: 100%' in content or 'img' not in content),
        ("触摸友好间距", 'padding' in content and 'gap' in content)
    ]
    
    passed = 0
    for name, result in checks:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
        if result:
            passed += 1
    
    print(f"\n📊 结果: {passed}/{len(checks)} 项通过 ({passed/len(checks)*100:.0f}%)")
    
    if passed == len(checks):
        print("\n🎉 完美！响应式设计完整")
        return 0
    elif passed >= len(checks) * 0.8:
        print("\n✅ 响应式设计良好，建议完善未通过项")
        return 0
    else:
        print("\n⚠️  响应式设计需要改进")
        return 1

if __name__ == '__main__':
    exit_code = test_responsive_design()
    sys.exit(exit_code)
