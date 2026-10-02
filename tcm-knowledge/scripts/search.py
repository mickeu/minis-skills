#!/usr/bin/env python3
"""
中医知识库检索脚本
搜索45本十四五规划教材中的内容

用法:
  python3 search.py "关键词"
  python3 search.py "伤寒论" "太阳病"
  python3 search.py --list  # 列出所有教材
  python3 search.py --info "中药学"  # 查看教材信息
"""

import os, sys, glob, re

TEXTBOOKS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", "textbooks")


def list_books():
    books = sorted(glob.glob(os.path.join(TEXTBOOKS_DIR, "*.md")))
    for i, b in enumerate(books, 1):
        name = os.path.basename(b).replace(".md", "")
        size = os.path.getsize(b)
        print(f"{i:2d}. {name}  ({size/1024:.0f} KB)")
    return books


def search_book(book_path, keywords, context_lines=2):
    """在单本教材中搜索关键词"""
    name = os.path.basename(book_path).replace(".md", "")
    results = []
    try:
        with open(book_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        return results

    for i, line in enumerate(lines):
        if all(kw.lower() in line.lower() for kw in keywords):
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            snippet = "".join(lines[start:end]).strip()
            results.append((name, i + 1, snippet[:500]))
    return results


def main():
    if len(sys.argv) < 2:
        print("用法: python3 search.py <关键词1> [关键词2 ...]")
        print("       python3 search.py --list")
        print("       python3 search.py --info <教材名>")
        sys.exit(1)

    if sys.argv[1] == "--list":
        list_books()
        return

    if sys.argv[1] == "--info":
        target = " ".join(sys.argv[2:])
        books = sorted(glob.glob(os.path.join(TEXTBOOKS_DIR, "*.md")))
        for b in books:
            if target in os.path.basename(b):
                name = os.path.basename(b).replace(".md", "")
                size = os.path.getsize(b)
                print(f"📖 {name}")
                print(f"   大小: {size/1024:.0f} KB ({size:,} 字)")
                print(f"   路径: {b}")
                return
        print(f"未找到: {target}")
        return

    keywords = sys.argv[1:]
    books = sorted(glob.glob(os.path.join(TEXTBOOKS_DIR, "*.md")))

    print(f"🔍 搜索: {' '.join(keywords)}")
    print(f"📚 检索 {len(books)} 本教材...")
    print("=" * 60)

    total = 0
    for book in books:
        results = search_book(book, keywords)
        for name, line_num, snippet in results:
            total += 1
            print(f"\n📖 {name} (第{line_num}行)")
            print("-" * 40)
            print(snippet)
            print()

    print(f"=" * 60)
    print(f"共找到 {total} 条结果")


if __name__ == "__main__":
    main()