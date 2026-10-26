#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gongwen.py — GB/T 9704-2012《党政机关公文格式》工具

子命令：
  make   生成符合版式的 HTML 公文页（浏览器预览 / 打印导出 PDF）
  check  校验公文 JSON 配置是否合规

用法：
  python3 gongwen.py make --demo                          # 生成示例公文
  python3 gongwen.py make --config 公文.json --out 公文.html
  python3 gongwen.py check --config 公文.json

JSON 配置字段（均可选，缺省自动省略该版式要素）：
  份号, 密级, 紧急程度, 发文机关标志, 发文字号, 签发人,
  标题, 主送机关, 正文(list[str]), 发文机关署名, 成文日期, 附注,
  抄送机关, 印发机关, 印发日期, 页码起始
"""
import argparse
import json
import os
import re
import sys

# 字号（pt）对应关系：二号22 / 三号16 / 四号14
FONT_2 = "22pt"    # 标题
FONT_3 = "16pt"    # 正文/发文字号/主送机关
FONT_4 = "14pt"    # 版记/抄送/印发

FONT_STACK = (
    "'FangSong','仿宋','STFangsong','SimSun','Songti SC','Noto Serif CJK SC',serif"
)
HEITI = "'SimHei','黑体','Heiti SC','Noto Sans CJK SC',sans-serif"
KAI = "'KaiTi','楷体','STKaiti','Kaiti SC','Noto Serif CJK SC',serif"
XBS = "'STZhongsong','华文中宋','SimSun','Songti SC','Noto Serif CJK SC',serif"

CSS_TPL = """\
@page {
  size: A4 portrait;
  margin: 37mm 26mm 35mm 28mm; /* 上 下 左 右，版心 156x225mm */
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: @@f3@@;
  font-size: @@font3@@;
  line-height: 1.55;         /* 22行/面 */
  color: #000;
}
.ban-tou { text-align: center; }
.feng { font-family: @@h@@; font-size: @@font3@@; text-align: left; }
.mi-ji { font-family: @@h@@; font-size: @@font3@@; text-align: left; }
.jin-ji { font-family: @@h@@; font-size: @@font3@@; text-align: left; }
.red-head {
  font-family: @@xbs@@;
  font-size: 34pt;
  font-weight: 700;
  color: #e70012;
  letter-spacing: 4px;
  line-height: 1.4;
  margin-top: 6mm;
}
.fa-zi { font-size: @@font3@@; }
.qian-fa { text-align: right; }
.red-line {
  border: 0;
  border-top: 2.5px solid #e70012;
  margin: 4mm 0 14mm 0;
}
.biao-ti {
  font-family: @@xbs@@;
  font-size: @@font2@@;
  font-weight: 700;
  text-align: center;
  line-height: 1.4;
  margin: 0 0 8mm 0;
}
.zhu-song { font-size: @@font3@@; }
.body { text-indent: 2em; margin: 0 0 3mm 0; text-align: justify; }
.h1 { font-family: @@h@@; font-weight: 400; }
.h2 { font-family: @@k@@; }
.h3 { font-family: @@f3@@; font-weight: 700; }
.sign-wrap { margin-top: 12mm; text-align: right; }
.sign-name { text-align: center; margin-bottom: 2mm; }
.sign-date { padding-right: 4em; }
.fu-zhu { margin-top: 4mm; }
.fujian { margin-top: 6mm; }
.ji-ji { margin-top: 8mm; }
.ji-line-thick { border: 0; border-top: 2px solid #000; margin: 2mm 0 0 0; }
.ji-line-thin  { border: 0; border-top: 0.8px solid #000; margin: 0; }
.ji-row { font-size: @@font4@@; padding: 1mm 0; }
.ye-ma { font-family: 'Times New Roman',serif; font-size: @@font4@@; text-align: center; margin-top: 8mm; }
"""


def _fmt_para(p):
    """按 GB/T 9704 标题分级识别正文段落（一、/（一）/1./（1）），返回带 class 的 HTML。"""
    if re.match(r"^\s*[一二三四五六七八九十]+、", p):
        return f'<p class="body h1">{p}</p>'
    if re.match(r"^\s*（[一二三四五六七八九十]+）", p):
        return f'<p class="body h2">{p}</p>'
    if re.match(r"^\s*\d+\.", p):
        return f'<p class="body h3">{p}</p>'
    return f'<p class="body">{p}</p>'


def render(cfg):
    parts = []

    # 版头
    head_lines = []
    if cfg.get("份号"):
        head_lines.append(f'<div class="feng">份号：{cfg["份号"]}</div>')
    if cfg.get("密级"):
        head_lines.append(f'<div class="mi-ji">{cfg["密级"]}</div>')
    if cfg.get("紧急程度"):
        head_lines.append(f'<div class="jin-ji">{cfg["紧急程度"]}</div>')
    head_lines.append(
        f'<div class="red-head">{cfg.get("发文机关标志", "×××文件")}</div>'
    )
    fa_line = f'<div class="fa-zi">{cfg.get("发文字号", "")}</div>'
    if cfg.get("签发人"):
        qf = f'<span class="qian-fa">签发人：{cfg["签发人"]}</span>'
        fa_line = f'<div class="fa-zi" style="text-align:left">{fa_line}　　{qf}</div>'
    head_lines.append(fa_line)
    head_lines.append('<hr class="red-line" />')
    parts.append(f'<div class="ban-tou">{"".join(head_lines)}</div>')

    # 主体
    main = []
    main.append(f'<div class="biao-ti">{cfg.get("标题", "")}</div>')
    if cfg.get("主送机关"):
        main.append(f'<div class="zhu-song">{cfg["主送机关"]}</div>')
    for para in cfg.get("正文", []):
        main.append(_fmt_para(para))
    if cfg.get("发文机关署名") or cfg.get("成文日期"):
        sign = '<div class="sign-wrap">'
        if cfg.get("发文机关署名"):
            sign += f'<div class="sign-name">{cfg["发文机关署名"]}</div>'
        if cfg.get("成文日期"):
            sign += f'<div class="sign-date">{cfg["成文日期"]}</div>'
        sign += "</div>"
        main.append(sign)
    if cfg.get("附注"):
        main.append(f'<div class="fu-zhu">{cfg["附注"]}</div>')
    if cfg.get("附件"):
        main.append(f'<div class="fujian">附件：{cfg["附件"]}</div>')
    parts.append(f'<div class="zhu-ti">{"".join(main)}</div>')

    # 版记
    if cfg.get("抄送机关") or cfg.get("印发机关"):
        ji = ['<div class="ji-ji">', '<div class="ji-line-thick"></div>']
        if cfg.get("抄送机关"):
            ji.append(f'<div class="ji-row">抄送：{cfg["抄送机关"]}</div>')
        ji.append('<div class="ji-line-thin"></div>')
        if cfg.get("印发机关") or cfg.get("印发日期"):
            yinfa = cfg.get("印发机关", "")
            rq = cfg.get("印发日期", "")
            ji.append(
                f'<div class="ji-row" style="overflow:hidden">'
                f'<span style="float:left">{yinfa}</span>'
                f'<span style="float:right">{rq}</span></div>'
            )
        ji.append('<div class="ji-line-thick"></div>')
        ji.append("</div>")
        parts.append("".join(ji))

    # 页码
    pn = int(cfg.get("页码起始", 1))
    parts.append(f'<div class="ye-ma">— {pn} —</div>')

    css = CSS_TPL
    for tag, val in [
        ("@@font2@@", FONT_2), ("@@font3@@", FONT_3), ("@@font4@@", FONT_4),
        ("@@f3@@", FONT_STACK), ("@@h@@", HEITI), ("@@k@@", KAI), ("@@xbs@@", XBS),
    ]:
        css = css.replace(tag, val)
    html = (
        "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8' />"
        "<title>" + cfg.get("标题", "公文") + "</title><style>" + css
        + "</style></head><body>" + "".join(parts) + "</body></html>"
    )
    return html


def cmd_make(args):
    if args.demo:
        cfg = {
            "份号": "000001",
            "密级": "★机密★1年",
            "紧急程度": "特急",
            "发文机关标志": "×××人民政府文件",
            "发文字号": "×政发〔2012〕1号",
            "标题": "关于××××工作的通报",
            "主送机关": "各省、自治区、直辖市人民政府，国务院各部委、各直属机构：",
            "正文": [
                "现将××××工作情况通报如下。",
                "一、总体情况",
                "（一）××××。今年以来，各地各部门认真贯彻落实……",
                "二、下一步工作要求",
                "（一）加强组织领导。各地区、各部门要……",
            ],
            "发文机关署名": "×××人民政府",
            "成文日期": "2012年7月1日",
            "附注": "（此件公开发布）",
            "抄送机关": "×××办公厅，×××部。",
            "印发机关": "×××人民政府办公厅",
            "印发日期": "2012年7月1日印发",
        }
    else:
        if not args.config:
            sys.exit("请用 --config 指定 JSON 配置文件，或 --demo 生成示例。")
        with open(args.config, "r", encoding="utf-8") as f:
            cfg = json.load(f)
    out = args.out or (os.path.splitext(args.config or "gongwen")[0] + ".html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(cfg))
    print(f"已生成：{out}")
    print("浏览器打开预览；打印时选择 A4、边距设为无，可导出符合版式的 PDF。")


def cmd_check(args):
    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    problems = []
    ok = lambda cond, msg: problems.append(msg) if not cond else None

    # 必填要素
    for k in ("发文机关标志", "标题"):
        if not cfg.get(k):
            ok(False, f"[必填] 缺少「{k}」")

    # 发文字号：年份六角括号+4位数字
    fz = cfg.get("发文字号", "")
    if fz:
        if not re.search(r"〔\d{4}〕", fz):
            ok(False, "[发文字号] 年份应为〔4位数字〕六角括号，如「×政发〔2012〕1号」")
        if not re.search(r"\d+号$", fz):
            ok(False, "[发文字号] 应以「N号」结尾")

    # 主送机关：以全角冒号结尾
    zs = cfg.get("主送机关", "")
    if zs and not zs.endswith("："):
        ok(False, "[主送机关] 应以全角冒号「：」结尾")

    # 成文日期：阿拉伯数字年月日
    rq = cfg.get("成文日期", "")
    if rq and not re.match(r"^\d{4}年\d{1,2}月\d{1,2}日$", rq):
        ok(False, "[成文日期] 应为阿拉伯数字，如「2012年7月1日」")

    # 附注：圆括号
    fz2 = cfg.get("附注", "")
    if fz2 and not (fz2.startswith("（") and fz2.endswith("）")):
        ok(False, "[附注] 应加全角圆括号，如「（此件公开发布）」")

    # 正文：列表或字符串
    zw = cfg.get("正文", [])
    if isinstance(zw, str):
        ok(False, "[正文] 应为字符串数组（按段落划分）")
    elif not zw:
        ok(False, "[正文] 不能为空")

    # 版记：抄送以句号结尾
    cs = cfg.get("抄送机关", "")
    if cs and not cs.endswith("。"):
        ok(False, "[抄送机关] 末尾应加句号「。」")

    if problems:
        print("❌ 校验未通过：")
        for p in problems:
            print("  -", p)
        return 1
    print("✅ 校验通过：公文配置符合 GB/T 9704-2012 基本要求")
    return 0


def main():
    ap = argparse.ArgumentParser(description="GB/T 9704-2012 公文格式工具")
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make", help="生成 HTML 公文页")
    m.add_argument("--config", help="公文 JSON 配置")
    m.add_argument("--out", help="输出 HTML 路径")
    m.add_argument("--demo", action="store_true", help="生成示例公文")
    m.set_defaults(func=cmd_make)
    c = sub.add_parser("check", help="校验公文配置")
    c.add_argument("--config", required=True, help="公文 JSON 配置")
    c.set_defaults(func=cmd_check)
    args = ap.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()