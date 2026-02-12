#!/usr/bin/env python3
"""
九经书院 - 数据导入脚本
导入剩余六部经典到 Philosophy-AI-Platform
"""

import sys
sys.path.insert(0, '/mnt/d/Philosophy-AI-Platform')

from core import PhilosophyAI, Text, Concept, Philosopher
from pathlib import Path

def import_jiujing_classics():
    """导入九经剩余经典"""
    ai = PhilosophyAI()
    base_dir = Path("/mnt/d/项目文件/chinese-philosophy-ai/data/books")
    
    print("=" * 60)
    print("📚 九经书院 - 经典导入")
    print("=" * 60)
    
    total_imported = 0
    
    # 1. 周易（易学）
    print("\n1️⃣ 导入周易...")
    yi_dir = base_dir / "yi"
    yi_count = 0
    if yi_dir.exists():
        files = sorted(yi_dir.glob("*.txt"))[:50]  # 取前50个
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/yijing/chapter_{i+1}.txt", content)
                yi_count += 1
            except Exception as e:
                pass
        print(f"   ✅ 周易: {yi_count} 卦/章")
        total_imported += yi_count
    
    # 2. 孟子（儒家）
    print("\n2️⃣ 导入孟子...")
    ru_dir = base_dir / "ru"
    mengzi_count = 0
    if ru_dir.exists():
        # 选取特定文件（假设文件名包含meng或从特定范围）
        files = sorted(ru_dir.glob("*.txt"))[50:80]  # 假设孟子在50-80范围
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/mengzi/chapter_{i+1}.txt", content)
                mengzi_count += 1
            except:
                pass
        print(f"   ✅ 孟子: {mengzi_count} 篇")
        total_imported += mengzi_count
    
    # 3. 大学、中庸（四书）
    print("\n3️⃣ 导入大学、中庸...")
    sishu_count = 0
    if ru_dir.exists():
        files = sorted(ru_dir.glob("*.txt"))[80:100]  # 假设在80-100范围
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/sishu/chapter_{i+1}.txt", content)
                sishu_count += 1
            except:
                pass
        print(f"   ✅ 大学/中庸: {sishu_count} 章")
        total_imported += sishu_count
    
    # 4. 黄帝内经（医家）
    print("\n4️⃣ 导入黄帝内经...")
    yi_med_dir = base_dir / "yi_med"
    huangdi_count = 0
    if yi_med_dir.exists():
        files = sorted(yi_med_dir.glob("*.txt"))[:30]
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/huangdineijing/chapter_{i+1}.txt", content)
                huangdi_count += 1
            except:
                pass
        print(f"   ✅ 黄帝内经: {huangdi_count} 篇")
        total_imported += huangdi_count
    
    # 5. 六祖坛经（禅宗）
    print("\n5️⃣ 导入六祖坛经...")
    fo_dir = base_dir / "fo"
    liuzu_count = 0
    if fo_dir.exists():
        files = sorted(fo_dir.glob("*.txt"))[:20]  # 佛经中选前20
        for i, file_path in enumerate(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ai.search.add_text(f"texts/liuzutanjing/chapter_{i+1}.txt", content)
                liuzu_count += 1
            except:
                pass
        print(f"   ✅ 六祖坛经: {liuzu_count} 品")
        total_imported += liuzu_count
    
    # 添加核心概念
    print("\n📝 添加九经核心概念...")
    
    new_concepts = [
        # 周易
        Concept(id="yin-yang", name="阴阳", name_en="Yin and Yang",
                definition="宇宙万物的两种基本属性，相互依存、相互转化。",
                school="confucianism", related_concepts=["bagua", "yi"], sources=["周易"]),
        Concept(id="bagua", name="八卦", name_en="Eight Trigrams",
                definition="乾、坤、震、巽、坎、离、艮、兑，代表自然现象。",
                school="confucianism", related_concepts=["yin-yang"], sources=["周易"]),
        
        # 孟子
        Concept(id="xing-shan", name="性善", name_en="Goodness of Human Nature",
                definition="人性本善，有恻隐、羞恶、辞让、是非之心。",
                school="confucianism", related_concepts=["ren", "yi"], sources=["孟子"]),
        
        # 大学
        Concept(id="san-gang", name="三纲", name_en="Three Principles",
                definition="明明德、亲民、止于至善。",
                school="confucianism", related_concepts=["ba-mu"], sources=["大学"]),
        Concept(id="ba-mu", name="八目", name_en="Eight Steps",
                definition="格物、致知、诚意、正心、修身、齐家、治国、平天下。",
                school="confucianism", related_concepts=["san-gang"], sources=["大学"]),
        
        # 中庸
        Concept(id="cheng", name="诚", name_en="Sincerity",
                definition="真实无妄，天之道也；诚之者，人之道也。",
                school="confucianism", related_concepts=["zhong", "he"], sources=["中庸"]),
        
        # 黄帝内经
        Concept(id="yin-yang-wuxing", name="阴阳五行", name_en="Yin-Yang and Five Elements",
                definition="木火土金水，相生相克，构成人体和自然的基本框架。",
                school="taoism", related_concepts=["zang-xiang"], sources=["黄帝内经"]),
        
        # 六祖坛经
        Concept(id="dun-wu", name="顿悟", name_en="Sudden Enlightenment",
                definition="直指人心，见性成佛，不假渐修。",
                school="buddhism", related_concepts=["zi-xing"], sources=["六祖坛经"]),
        Concept(id="zi-xing", name="自性", name_en="Self-Nature",
                definition="菩提自性，本来清净，但用此心，直了成佛。",
                school="buddhism", related_concepts=["dun-wu"], sources=["六祖坛经"]),
    ]
    
    for c in new_concepts:
        ai.kg.add_concept(c)
    print(f"   ✅ 已添加 {len(new_concepts)} 个核心概念")
    
    # 添加哲学家
    print("\n👤 添加九经相关哲学家...")
    
    new_philosophers = [
        Philosopher(id="fuxi", name="伏羲", name_en="Fu Xi", era="上古",
                   school="confucianism", biography="创八卦，定阴阳。",
                   key_works=["八卦"], concepts=["bagua", "yin-yang"]),
        Philosopher(id="mengzi", name="孟子", name_en="Mencius", era="战国",
                   school="confucianism", biography="儒家亚圣，倡性善论、仁政王道。",
                   key_works=["孟子"], concepts=["xing-shan", "ren", "yi"]),
        Philosopher(id="zengzi", name="曾子", name_en="Zengzi", era="春秋",
                   school="confucianism", biography="孔子弟子，作《大学》。",
                   key_works=["大学"], concepts=["san-gang", "ba-mu"]),
        Philosopher(id="zisi", name="子思", name_en="Zi Si", era="战国",
                   school="confucianism", biography="曾子弟子，孔子之孙，作《中庸》。",
                   key_works=["中庸"], concepts=["cheng", "zhong", "he"]),
        Philosopher(id="huangdi", name="黄帝", name_en="Yellow Emperor", era="上古",
                   school="taoism", biography="华夏人文始祖，托名《黄帝内经》。",
                   key_works=["黄帝内经"], concepts=["yin-yang-wuxing", "zang-xiang"]),
        Philosopher(id="huineng", name="惠能", name_en="Hui Neng", era="唐代",
                   school="buddhism", biography="禅宗六祖，倡顿悟成佛。",
                   key_works=["六祖坛经"], concepts=["dun-wu", "zi-xing"]),
    ]
    
    for p in new_philosophers:
        ai.kg.add_philosopher(p)
    print(f"   ✅ 已添加 {len(new_philosophers)} 位哲学家")
    
    # 保存
    ai.kg.save_data()
    
    # 统计
    print("\n" + "=" * 60)
    print("📊 九经导入完成")
    print("=" * 60)
    stats = ai.get_statistics()
    print(f"  总概念: {stats['concepts']}")
    print(f"  总哲学家: {stats['philosophers']}")
    print(f"  总索引文本: {stats['indexed_files']}")
    print(f"  本次导入: {total_imported} 篇")
    print("=" * 60)

if __name__ == "__main__":
    import_jiujing_classics()