# -*- coding: utf-8 -*-
import re, html, zipfile, uuid, os
from collections import defaultdict

TXT = '/var/minis/workspace/novel_gscr/高手下山_我有九个无敌师父.txt'
EPUB = '/var/minis/workspace/novel_gscr/高手下山_我有九个无敌师父_修订版.epub'
TITLE = '高手下山，我有九个无敌师父！'
AUTHOR = '小殇殇'
VOL_SIZE = 100

CN = {'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'百':100,'千':1000,'两':2}
def cn2num(s):
    if not s: return None
    if s.isdigit(): return int(s)
    if len(s) == 1: return CN.get(s, None)
    if '十' in s:
        parts = s.split('十')
        left = CN.get(parts[0], 1) if parts[0] else 1
        right = CN.get(parts[1], 0) if len(parts) > 1 and parts[1] else 0
        return left * 10 + right
    return None

chap_re = re.compile(r'^第([0-9一二三四五六七八九十百千零两]+)章\s*(.*)$')
skip_re = re.compile(r'^-{3,}$|^第[一二三四五六七八九十百千零两]+卷')

# ---- 第一遍：解析元数据（位置、标题编号、标题） ----
metas = []
position = 0
cur_title = None
cur_num = None
def flush_meta():
    global position, cur_title, cur_num
    if cur_title is None: return
    position += 1
    metas.append((position, cur_num, cur_title))
    cur_title = None
    cur_num = None
for line in open(TXT, encoding='utf-8', errors='replace'):
    s = line.strip()
    if not s or skip_re.match(s): continue
    if not line[:1].isspace() and chap_re.match(line):
        flush_meta()
        m = chap_re.match(line)
        cur_title = s
        cur_num = cn2num(m.group(1))
flush_meta()
print('章节总数:', len(metas))
num_positions = defaultdict(list)
for pos, num, _ in metas:
    if num is not None:
        num_positions[num].append(pos)
# 补位位置：重复编号中，位置 != 编号 的（标题编号错乱，按位置修正为正确编号）
fix_positions = set()
for num, poss in num_positions.items():
    if len(poss) > 1:
        for p in poss:
            if p != num:
                fix_positions.add(p)
print('修正编号章节数:', len(fix_positions))

# ---- 打开 zip ----
uid = uuid.uuid4().hex.upper()
zf = zipfile.ZipFile(EPUB, 'w', zipfile.ZIP_DEFLATED)
zf.writestr('mimetype', 'application/epub+zip', zipfile.ZIP_STORED)
zf.writestr('META-INF/container.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n  <rootfiles>\n    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n  </rootfiles>\n</container>')

# ---- 第二遍：流式解析并写入卷文件 ----
para_cache = {}
vol_buf = []
vol_written = 0
position = 0
cur_title = None
cur_paras = []

def fix_title(pos, title):
    m = chap_re.match(title)
    if m:
        return f'第{pos}章' + (m.group(2) if m.group(2) else '')
    return title

def write_vol(gi, items):
    vhref = f'text/vol{gi:02d}.xhtml'
    sections = []
    # 卷首目录：正文 HTML 锚点链接，供 Apple Books 内点击跳转
    toc_li = '\n'.join(
        f'<li><a href="#ch{pos:05d}">{html.escape(title)}</a></li>'
        for pos, title in items)
    first_t = items[0][1]
    last_t = items[-1][1]
    mm1 = re.match(r'^第(\d+)章', first_t)
    mm2 = re.match(r'^第(\d+)章', last_t)
    if mm1 and mm2:
        vol_head = f'第{gi}卷（第{mm1.group(1)}-{mm2.group(1)}章）'
    else:
        vol_head = f'第{gi}卷'
    sections.append(f'<section id="vol-toc{gi:02d}">\n<h2>{html.escape(vol_head)}</h2>\n<p>本卷目录，点击章节跳转</p>\n<ol>\n{toc_li}\n</ol>\n</section>')
    for pos, title in items:
        pid = f'ch{pos:05d}'
        paras = para_cache.get(pos, [])
        body = '\n'.join(f'<p>{html.escape(p)}</p>' for p in paras)
        sections.append(f'<section id="{pid}">\n<h2>{html.escape(title)}</h2>\n{body}\n</section>')
    content = ('<?xml version="1.0" encoding="utf-8"?>\n'
               '<html xmlns="http://www.w3.org/1999/xhtml">\n'
               f'<head><title>{html.escape(TITLE)}</title></head>\n'
               '<body>\n' + ''.join(sections) + '\n</body>\n</html>')
    zf.writestr(f'OEBPS/{vhref}', content)
    print(f'已写 {vhref} ({len(items)} 章)')

for line in open(TXT, encoding='utf-8', errors='replace'):
    s = line.strip()
    if not s or skip_re.match(s):
        continue
    if not line[:1].isspace() and chap_re.match(line):
        if cur_title is not None:
            position += 1
            t = fix_title(position, cur_title) if position in fix_positions else cur_title
            vol_buf.append((position, t))
            para_cache[position] = cur_paras
            if len(vol_buf) >= VOL_SIZE:
                vol_written += 1
                write_vol(vol_written, vol_buf)
                for pos, _ in vol_buf:
                    para_cache.pop(pos, None)
                vol_buf = []
        m = chap_re.match(line)
        cur_title = s
        cur_paras = []
    else:
        cur_paras.append(s)
# 最后 flush
if cur_title is not None:
    position += 1
    t = fix_title(position, cur_title) if position in fix_positions else cur_title
    vol_buf.append((position, t))
    para_cache[position] = cur_paras
if vol_buf:
    vol_written += 1
    write_vol(vol_written, vol_buf)
    for pos, _ in vol_buf:
        para_cache.pop(pos, None)
    vol_buf = []
print('总卷数:', vol_written)# ---- 分组（用于目录） ----
groups = [metas[i:i+VOL_SIZE] for i in range(0, len(metas), VOL_SIZE)]

def _fix(pos, t):
    return fix_title(pos, t) if pos in fix_positions else t

def vol_label(gi, g):
    m1 = re.match(r'^第(\d+)章', _fix(g[0][0], g[0][2]))
    m2 = re.match(r'^第(\d+)章', _fix(g[-1][0], g[-1][2]))
    if m1 and m2:
        return f'第{gi}卷 第{m1.group(1)}-{m2.group(1)}章'
    return f'第{gi}卷'

# ---- nav.xhtml（顶层只放49个卷，避免超长嵌套目录点击失效） ----
nav_parts = []
for gi, g in enumerate(groups, 1):
    vhref = f'text/vol{gi:02d}.xhtml'
    nav_parts.append(f'<li><a href="{vhref}">{html.escape(vol_label(gi,g))}</a></li>')
nav = ('<?xml version="1.0" encoding="utf-8"?>\n'
       '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n'
       '<head><title>目录</title></head>\n<body>\n<nav epub:type="toc">\n<h1>目录</h1>\n<ol>\n'
       + '\n'.join(nav_parts) + '\n</ol>\n</nav>\n</body>\n</html>')
zf.writestr('OEBPS/nav.xhtml', nav)

# ---- toc.ncx（顶层只放49个卷） ----
ncx_parts = []
play = 0
for gi, g in enumerate(groups, 1):
    vhref = f'text/vol{gi:02d}.xhtml'
    play += 1
    ncx_parts.append(f'<navPoint id="vol{gi}" playOrder="{play}">\n'
                     f'<navLabel><text>{html.escape(vol_label(gi,g))}</text></navLabel>\n'
                     f'<content src="{vhref}"/>\n</navPoint>')
ncx = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
       '<head>\n<meta name="dtb:uid" content="urn:uuid:' + uid + '"/>\n'
       '<meta name="dtb:depth" content="1"/>\n'
       '<meta name="dtb:totalPageCount" content="0"/>\n'
       '<meta name="dtb:maxPageNumber" content="0"/>\n</head>\n'
       f'<docTitle><text>{html.escape(TITLE)}</text></docTitle>\n'
       '<navMap>\n' + '\n'.join(ncx_parts) + '\n</navMap>\n</ncx>')
zf.writestr('OEBPS/toc.ncx', ncx)

# ---- content.opf ----
manifest = [
    '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
    '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
]
spine = []
for gi in range(1, len(groups)+1):
    cid = f'vol{gi:02d}'
    manifest.append(f'<item id="{cid}" href="text/vol{gi:02d}.xhtml" media-type="application/xhtml+xml"/>')
    spine.append(f'<itemref idref="{cid}"/>')
opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
       '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">\n'
       '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
       f'<dc:identifier id="bookid">urn:uuid:{uid}</dc:identifier>\n'
       f'<dc:title>{html.escape(TITLE)}</dc:title>\n'
       f'<dc:creator>{html.escape(AUTHOR)}</dc:creator>\n'
       '<dc:language>zh-CN</dc:language>\n'
       '<meta property="dcterms:modified">2026-10-10T00:00:00Z</meta>\n'
       '</metadata>\n<manifest>\n' + '\n'.join(manifest) + '\n</manifest>\n'
       '<spine toc="ncx">\n' + '\n'.join(spine) + '\n</spine>\n</package>')
zf.writestr('OEBPS/content.opf', opf)

zf.close()
print('EPUB 大小: %.1f MB' % (os.path.getsize(EPUB)/1048576))
print('EPUB:', EPUB)