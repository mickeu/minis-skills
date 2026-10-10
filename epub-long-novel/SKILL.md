# 超长章节书籍 EPUB 转换（Apple Books 兼容）

## 触发场景

用户要求把**超长章节小说**（章节数 >1000，如 4000+ 章的网络小说）转换为 EPUB 并在 **Apple Books** 中阅读时，按本技能方案执行。特别适用于"目录打不开/点击无反应/页码对不上"的 Apple Books 兼容问题。

## 核心痛点（实测结论）

Apple Books 对 EPUB 目录的支持：
- **超长扁平目录**（如 4825 条 `<li><a>`）→ 目录 0% 转圈、点击跳回书开头
- **超长嵌套目录**（如 49 卷 + 4825 章，`<li><span>` 包 `<ol>`）→ 能展开但**子项点击无反应**
- **搜索跳转正常**（走全文索引）→ 说明正文锚点定位本身没问题，问题出在 TOC 视图

结论：Apple Books 的目录视图对几千条链接的点击处理不可靠，但**正文内的 HTML 锚点链接完全支持**。

## 最终方案（已验证可用）

1. **每 100 章合并为一个卷文件**（如 4825 章 → 49 个卷文件）
2. **EPUB 目录（nav.xhtml / toc.ncx）只放顶层卷条目**（49 条，点击可靠）
3. **每个卷文件开头放「卷首目录」**：`<section id="vol-tocXX">`，内含本卷章节的**正文 HTML 锚点链接** `<a href="#ch00001">第X章 ...</a>`，Apple Books 阅读界面内可直接点击跳转
4. 章节结构：`<section id="ch00001"><h2>第X章 标题</h2><p>...</p></section>`
5. 章节编号按**内容位置**修正（若源数据编号错乱/有补位章节，重新编号保证 1~N 连续无重复）

### 使用方式（两步直达章节）

打开 Apple Books 目录 → 点卷（如"第3卷 第201-300章"）→ 在卷首目录点章节标题 → 跳转

## 关键脚本

- `/var/minis/workspace/novel_gscr/make_epub_full.py`（TXT 解析、章节编号修正、分卷生成、卷首目录、nav/ncx/opf/container 生成）
- 脚本核心参数：`VOL_SIZE = 100`（每卷章数，可按需调整）、`TITLE`、源 TXT 路径、输出 EPUB 路径
- 注意：生成后必须立即 `zipfile.testzip()` 验证完整性；复制到 iCloud 同步目录后**再次验证**（曾出现过生成时完好、同步后损坏的情况）

## 验证清单

```python
import zipfile, re
z = zipfile.ZipFile(epub_path)
assert z.testzip() is None              # zip 完整性
nav = z.read('OEBPS/nav.xhtml').decode()
assert len(re.findall(r'<li><a href=', nav)) == 卷数  # 目录只放卷
# 每卷检查卷首目录与锚点
for gi in range(1, 卷数+1):
    c = z.read(f'OEBPS/text/vol{gi:02d}.xhtml').decode()
    assert f'id="vol-toc{gi:02d}"' in c
    for a in re.findall(r'<a href="#(ch\d+)">', c):
        assert f'id="{a}"' in c
```

## 参考资料（来源）

- 实测项目：《高手下山，我有九个无敌师父》4825 章 EPUB 转换（2026-10-10）
- 源数据：365小说网（shukuge.com）官方打包 TXT，番茄小说官方源章节编号为准
- 脚本与成品：`/var/minis/workspace/novel_gscr/`
- 用户确认：2026-10-10 用户反馈"现在好了"，并确认以后转换超长章节书籍按此格式