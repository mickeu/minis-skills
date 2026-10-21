---
name: minis-avatar-sources
description: Minis 应用透明背景 PNG 头像素材来源库。包含 GitHub 开源透明 PNG 素材仓库（monsstudio/stickers 221张透明精灵贴纸 CC BY 4.0、darshitshah8/Avatars 办公卡通头像）、批量生成圆形透明头像的处理脚本、已归档素材位置。当用户要 Minis 头像、透明背景头像、找头像 PNG 素材、圆形透明头像、精灵贴纸头像时触发。
---

# Minis 透明头像素材来源

## 来源仓库

### monsstudio/stickers（推荐，221张透明精灵贴纸）
- 仓库：https://github.com/monsstudio/stickers
- 内容：EtherFantasy/Ethermon 游戏精灵，die-cut 透明 PNG，白色描边，CC BY 4.0 许可（个人可商用无忧）
- 下载：`git clone --depth 1 https://github.com/monsstudio/stickers`（约 190MB，221 张高分辨率原图）
- 文件名格式：`pets/<Pet>_sticker.png`（注意个别特殊大小写如 `KahukelE`、`MalakelE`）
- 已精选适合做头像：Yarmeow（粉白伊布）、Kelpony（蓝白飞马小鹿）、Pudde（蓝蘑菇）、Kyari（红精灵）、Mianari（黄电鼠）、Mirrie（紫章鱼）、Elekitt、Mizumi、Candeliria、Dynamouse、Foxeez、Roichirp、Qairrel 等

### darshitshah8/Avatars（办公卡通头像，备用）
- 仓库：https://github.com/darshitshah8/Avatars
- 内容：AI 生成办公角色卡通头像 512×512，男/女 owner/manager/employee/guest/custom/hr/sales
- 路径：`raw.githubusercontent.com/darshitshah8/Avatars/main/Avatars/Office/<M|F>ale/<role>.png`
- ⚠️ 注意：圆内实色背景、圆外透明（圆形卡片式），**不是整体全透明**；用户明确要"没有人物位置也透明"时不要用这类

## 已归档素材（2026-10-21）
- `/var/minis/shared/avatar-candidates/circle/`：30 张 512×512 圆形透明头像（圆外 alpha=0，每张 `circle_<Pet>_sticker.png`）
- `/var/minis/shared/avatar-candidates/circle_preview.png`：30 张预览网格图（棋盘格背景展示透明效果）
- `/var/minis/shared/avatar-candidates/minis-avatar-circle-30.zip`：整包 zip（5.9MB）
- 原始精灵大图也在 `/var/minis/shared/avatar-candidates/` 备份

## 批量生成圆形透明头像
用 `scripts/make_circle_avatars.py`：
```sh
python3 make_circle_avatars.py <候选文件名列表.txt>
```
- 输入：候选文件名列表（每行一个 `<Pet>_sticker.png`）
- 输出：512×512 圆形透明头像，保存到 `/var/minis/shared/avatar-candidates/circle/`
- 处理逻辑：居中偏上裁剪成方形（top = h*0.15，让头部居中）→ resize 512 → 套圆形遮罩（圆内保留原 alpha，圆外 alpha=0）
- 透明验证：检查图片四角 alpha 必须为 0，才算"圆外全透明"

## 生成预览图
用 `scripts/gen_preview.py`：把圆形头像拼成带名字的棋盘格预览大图（6 列），方便用户一次性挑选。透明区域用棋盘格展示。

## 工作流
1. 用户要透明头像 → 先推荐 `monsstudio/stickers` 精灵贴纸（整体透明、可爱、CC BY 4.0）
2. 克隆仓库或用 raw 链接下载候选
3. 用 `make_circle_avatars.py` 批量生成圆形透明头像
4. 用 `gen_preview.py` 生成预览图 → 在对话里展示预览图+编号清单让用户挑
5. 用户选定后打包 zip 提供下载，或在对话里逐张贴图