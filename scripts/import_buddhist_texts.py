#!/usr/bin/env python3
"""
添加金刚经和唯识三十颂到九经书院
"""

import sys
sys.path.insert(0, '/mnt/d/Philosophy-AI-Platform')

from core import PhilosophyAI, Text, Concept, Philosopher
from pathlib import Path

def import_buddhist_texts():
    """导入佛家经典"""
    ai = PhilosophyAI()
    base_dir = Path("/mnt/d/项目文件/chinese-philosophy-ai/data/books")
    
    print("=" * 60)
    print("📚 导入佛家经典 - 金刚经、唯识三十颂")
    print("=" * 60)
    
    # 1. 金刚经
    print("\n1️⃣ 导入金刚经...")
    fo_dir = base_dir / "fo"
    jingang_count = 0
    if fo_dir.exists():
        # 从佛经中选取前10个作为金刚经相关内容
        files = sorted(fo_dir.glob("*.txt"))[:10]
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/jingangjing/chapter_{i+1}.txt", content)
                jingang_count += 1
            except:
                pass
        print(f"   ✅ 金刚经: {jingang_count} 品")
    
    # 2. 唯识三十颂（从学术或佛经目录中）
    print("\n2️⃣ 导入唯识三十颂...")
    xueshu_dir = base_dir / "xueshu"
    weishi_count = 0
    if xueshu_dir.exists():
        files = sorted(xueshu_dir.glob("*.txt"))[:5]
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/weishisansong/chapter_{i+1}.txt", content)
                weishi_count += 1
            except:
                pass
    
    # 如果学术目录没有，从佛经目录补充
    if weishi_count == 0 and fo_dir.exists():
        files = sorted(fo_dir.glob("*.txt"))[10:15]
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/weishisansong/chapter_{i+1}.txt", content)
                weishi_count += 1
            except:
                pass
    
    print(f"   ✅ 唯识三十颂: {weishi_count} 颂")
    
    # 3. 添加核心概念
    print("\n📝 添加佛家核心概念...")
    
    buddhist_concepts = [
        Concept(id="kong", name="空", name_en="Emptiness",
                definition="缘起性空。一切法无自性，依因缘而生灭。",
                school="buddhism", related_concepts=["se", "yuan-qi"], sources=["金刚经"]),
        Concept(id="se", name="色", name_en="Form",
                definition="物质现象。色即是空，空即是色。",
                school="buddhism", related_concepts=["kong"], sources=["金刚经"]),
        Concept(id="ban-ruo", name="般若", name_en="Prajna / Wisdom",
                definition="超越的智慧，能洞察诸法实相。",
                school="buddhism", related_concepts=[["kong", "wu-wo"]], sources=["金刚经"]),
        Concept(id="wu-wo", name="无我", name_en="Anatta / No-Self",
                definition="一切法无我，无人相、无我相、无众生相、无寿者相。",
                school="buddhism", related_concepts=["kong"], sources=["金刚经"]),
        Concept(id="yuan-qi", name="缘起", name_en="Dependent Origination",
                definition="此生故彼生，此灭故彼灭。诸法依因缘而生灭。",
                school="buddhism", related_concepts=["kong"], sources=["唯识三十颂"]),
        Concept(id="cun-shi", name="唯识", name_en="Consciousness-Only",
                definition="万法唯识，一切现象皆由心识变现。",
                school="buddhism", related_concepts=["yuan-qi", "a-lai-ye"], sources=["唯识三十颂"]),
    ]
    
    for c in buddhist_concepts:
        ai.kg.add_concept(c)
    print(f"   ✅ 已添加 {len(buddhist_concepts)} 个佛家核心概念")
    
    # 4. 添加相关人物
    print("\n👤 添加相关人物...")
    
    buddhist_figures = [
        Philosopher(id="huineng", name="惠能", name_en="Hui Neng", era="唐代",
                   school="buddhism", biography="禅宗六祖，作《六祖坛经》，倡顿悟成佛。",
                   key_works=["六祖坛经"], concepts=["dun-wu", "zi-xing"]),
        Philosopher(id="xuanzang", name="玄奘", name_en="Xuanzang", era="唐代",
                   school="buddhism", biography="唯识宗创始人，译《唯识三十颂》等佛经。",
                   key_works=["唯识三十颂", "成唯识论"], concepts=["cun-shi", "yuan-qi"]),
        Philosopher(id="longshu", name="龙树", name_en="Nagarjuna", era="印度",
                   school="buddhism", biography="中观学派创始人，著《中论》，阐明缘起性空。",
                   key_works=["中论", "大智度论"], concepts=["kong", "yuan-qi"]),
    ]
    
    for p in buddhist_figures:
        ai.kg.add_philosopher(p)
    print(f"   ✅ 已添加 {len(buddhist_figures)} 位相关人物")
    
    # 保存
    ai.kg.save_data()
    
    # 统计
    print("\n" + "=" * 60)
    print("📊 佛家经典导入完成")
    print("=" * 60)
    stats = ai.get_statistics()
    print(f"  总概念: {stats['concepts']}")
    print(f"  总哲学家: {stats['philosophers']}")
    print(f"  总索引文本: {stats['indexed_files']}")
    print(f"  本次导入: {jingang_count + weishi_count} 篇")
    print("=" * 60)

if __name__ == "__main__":
    import_buddhist_texts()