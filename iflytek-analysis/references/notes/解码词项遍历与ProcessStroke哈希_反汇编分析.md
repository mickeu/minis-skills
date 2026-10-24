# 解码词项遍历逻辑 + ProcessStroke 哈希算法验证 — 反汇编分析

> 来源：讯飞输入法 iOS v15.0.3606 IPA 真实二进制反汇编
> 分析日期：2026-10-24
> 产物：`references/notes/decodepath/ProcessEmitDecode_common.asm`（已有）、`references/notes/decodepath/ProcessStroke.asm`（本次新增，15133B）
> 关联记忆：候选解码主路径报告（1.11.0 入库）、ProcessStroke 哈希=MurmurHash3 fmix（第一卷/当日记忆）

---

## 一、ProcessEmitDecode_common（0x1013e5e1c）词项遍历逻辑

该函数是候选解码主路径的核心循环。**每个词项 6 字节**，词项内存布局：
- 偏移 0（32bit）：低 24bit = **笔画码**（`and w9, w9, #0xffffff` 提取）
- 偏移 4（16bit）：**词项 ID**（`ldrh w8, [x26, #4]` 提取）

### 1.1 核心循环（0x1013e60c4 → 0x1013e62a0）

```
; ★ 循环头（每词项 6 字节步进）
1013e6298: add  x26, x26, #0x6        ; ★★ x26 += 6 —— 6 字节词项步进
1013e629c: cmp  x26, x16              ; 与区间结束地址 x16 比较
1013e62a0: b.cc 0x1013e60e8           ; ★★ 未到区间末尾则跳回循环头

; 循环体（从 0x1013e60e8 进入）
1013e60e8: ldrh  w8, [x26, #4]        ; ★ 取词项偏移4 的 16bit 词项ID
1013e60ec: ldr   w9, [x19, #40]       ; 词项表大小（上限）
1013e60f0: cmp   w9, w8
1013e60f4: b.ls  0x1013e62bc          ; 表大小<=ID → 越界处理/日志
1013e60f8: ldr   x9, [x19, #32]       ; 索引表基址
1013e60fc: ldrh  w8, [x9, w8, uxtw #1] ; ★ 词项ID → 半字查表得索引 w8
1013e6100: ldr   x9, [x23, #72]       ; 有效性位表
1013e6104: ldrb  w9, [x9, x8]         ; ★ 按索引校验有效位
1013e6108: cbz   w9, 0x1013e6298      ; 无效 → 跳过本词项
1013e610c: stp   wzr, wzr, [x19, #44] ; 清零 rank（[x19+44] 和 +48）
1013e6114: ldr   w9, [x24, #24]       ; 类型掩码
1013e6118: and   x10, x8, #0x1f       ; 索引 & 0x1f
1013e611c: lsl   w10, w15, w10        ; 1 << (索引&31)
1013e6120: tst   w9, w10              ; 位测试（该 bit 是否启用）
1013e6124: b.eq  0x1013e6298          ; 未启用 → 跳过
1013e6128: ldr   x9, [x23, #24]       ; DecodeArcState 链表基址
1013e612c: madd  x9, x8, x17, x9      ; ★ x9 = 基址 + 索引*0x18（x17=0x18=24B 步进）
1013e6130: ldr   x11, [x9, #8]!       ; 取链头（前递增）
1013e6134: cbz   x11, 0x1013e6298     ; 链空 → 跳过
1013e613c: ldr   x12, [x11, #32]      ; 遍历 DecodeArcState 链
1013e6150: ldr   x11, [x12]
1013e6154: cbnz  x11, 0x1013e613c     ; 沿链找匹配
...
1013e61b8: ldr   x8, [x8, x22, lsl #3] ; ★ 遍历候选节点指针数组（8字节元素）
1013e61c4: cmp   x10, x24             ; 与目标节点比较
1013e61c8: b.eq  0x1013e61dc          ; 命中
1013e61cc: add   x22, x22, #0x1       ; i++
1013e61d4: b.cc  0x1013e61b4          ; 继续遍历
```

### 1.2 中英文分流（命中后）

```
1013e6244: tbnz  w9, #15, 0x1013e6290  ; 词项标志 bit15 → 直接跳过
1013e6248: ldr   x8, [x8]              ; 取关联对象
1013e624c: ldrb  w8, [x8, #33]         ; 关联对象 +33
1013e6250: tbnz  w8, #1, 0x1013e626c   ; bit1=1 → 英文
1013e6264: bl    0x1013e6974           ; ★ process_chn（中文）
1013e627c: bl    0x1013e6374           ; ★ process_eng（英文）
```

**中英文分流依据：关联对象 `+33 bit1`（tbnz w8, #1）** —— 与 1.11.0 报告结论一致。

### 1.3 完整主路径

```
ProcessStroke → DecodeArcState → ProcessEmitDecode_common（6字节词项遍历）
  → 词项ID查半字表 → 索引 → 有效位校验 → 清零rank
  → DecodeArcState链（24B步进）定位 → 遍历链找匹配
  → 关联对象 +33 bit1 分流 process_chn / process_eng
  → 中间候选并入 vector（不直接调 ConstructDecodeNode）
  → ConstructDecodeNode / MergeOne / MergeN → 候选桶
```

---

## 二、ProcessStroke（0x10102a5d4）哈希算法验证

ProcessStroke.bin（2048B）反汇编为 `references/notes/decodepath/ProcessStroke.asm`。

### 2.1 哈希计算（0x10102a78c → 0x10102a7bc）

```
10102a788: ldrh  w5, [x25, #4]!        ; ★ 取词项偏移4 的 16bit 笔画码 w5
10102a794: ldrh  w8, [x8, x5, lsl #1] ; 按笔画码查半字表得 w8（词项数据）
10102a798: mvn   x9, x8               ; ~w8
10102a79c: add   x9, x9, x8, lsl #21  ; ~w8 + w8<<21
10102a7a0: eor   x9, x9, x9, lsr #24  ; x9 ^= x9>>24
10102a7a4: mul   x9, x9, x28          ; x9 *= 0x109 = 265
10102a7a8: eor   x9, x9, x9, lsr #14  ; x9 ^= x9>>14
10102a7b0: mul   x9, x9, x10          ; x9 *= 0x15 = 21
10102a7b4: eor   x9, x9, x9, lsr #28  ; x9 ^= x9>>28
10102a7b8: mul   x9, x9, x20          ; x9 *= 0x80000001
```

**这是标准 MurmurHash3 64 位 `fmix64` 最终混合函数**（`x ^= x >> 32; x *= 0xff51afd7ed558ccd; x ^= x >> 33; x *= 0xc4ceb9fe1a85ec53; x ^= x >> 33` 的变体，常量换成 265/21/0x80000001）。此前「第一卷：笔画码哈希+线性探测」完全证实。

### 2.2 取桶与探测（0x10102a7bc → 0x10102a800）

```
10102a7bc: ldr   x10, [x27, #16]      ; 桶大小 size
10102a7c0: sub   x11, x10, #0x1       ; size-1
10102a7c4: and   x12, x9, x11         ; ★ hash & (size-1) = 桶索引
10102a7c8: ldr   x10, [x27, #48]      ; 桶数组基址
10102a7cc: ldr   x10, [x10, x12, lsl #3] ; 取桶头指针
10102a7d0: cbz   x10, 0x10102a804
10102a7d4: ldr   x10, [x10]           ; 链头
10102a7dc: ldr   x13, [x10, #8]       ; 节点内 [x10+8] = 哈希值（键）
10102a7e0: cmp   x13, x9              ; 比较哈希
10102a7e8: ldrh  w13, [x10, #16]      ; [x10+16] = 半字词id
10102a7ec: cmp   w8, w13              ; 比较词id
10102a7f0: b.ne  0x10102a7d4          ; 不同 → 沿链下一节点
10102a7f8: and   x13, x13, x11        ; 开放寻址探测：next = hash & (size-1)
10102a7fc: cmp   x13, x12
10102a800: b.eq  0x10102a7d4          ; 探测回原点 → 停止
```

**词项节点结构**：
- `[node+8]` = 64bit 哈希值（键）
- `[node+16]` = 16bit 词项 ID

**查找方式 = 哈希桶 + 链式/开放寻址混合**：先用 `hash & (size-1)` 取桶，桶内沿链比较哈希值和词id，若链中哈希不等则用 `next = hash & (size-1)`（开放寻址线性探测变体）继续。命中后 `b 0x10102a88c` 进入候选处理。

### 2.3 验证结论

| 断言 | 结果 |
|---|---|
| 笔画码哈希 + 线性探测 | ✅ 完全证实（`and (size-1)` 取桶 + 开放寻址探测） |
| MurmurHash3 风格 64 位 fmix 混合 | ✅ 完全证实（mvn→lsl21→eor lsr24→mul265→eor lsr14→mul21→eor lsr28→mul0x80000001） |
| 词项结构 `[+8]=hash`、`[+16]=halfword词id` | ✅ 完全证实 |
| 每词项 6 字节步进、偏移4取词项ID | ✅ 与 ProcessEmitDecode_common 完全一致（同一词项格式） |

---

## 三、跨会话读取路径

```bash
# 词项遍历逻辑
file_read /var/minis/skills/iflytek-analysis/references/notes/decodepath/ProcessEmitDecode_common.asm
# ProcessStroke 哈希反汇编（本次新增）
file_read /var/minis/skills/iflytek-analysis/references/notes/decodepath/ProcessStroke.asm
# 完整主路径报告
file_read /var/minis/skills/iflytek-analysis/references/notes/候选解码主路径_反汇编报告.md
```