# 节点订阅（proxy-providers）

来源：`Hako/docs/config.yaml` 1772-1897 行

## 基本配置

### HTTP 订阅（最常用）

```yaml
proxy-providers:
  provider1:
    type: http
    url: "https://example.com/subscribe"
    interval: 3600                 # 更新间隔（秒）
    path: ./provider1.yaml         # 缓存路径（默认只允许 mihomo Home Dir）
    proxy: DIRECT                  # 下载订阅时走的代理
    size-limit: 10240              # 下载文件大小限制（KB），0=不限制
    header:
      User-Agent:
        - "Clash/v1.18.0"
        - "mihomo/1.18.3"
      Accept:
        - 'application/vnd.github.v3.raw'
      Authorization:
        - 'token 1231231'
      X-Age-Public-Key:
        - 'age1xh86kh9v23vattr58yedspm3f57sxvnswu9krr6ns438amekx5gsd09uma'
    health-check:
      enable: true
      interval: 600
      lazy: true                   # 延迟健康检查（首次使用前才测）
      url: https://cp.cloudflare.com/generate_204
      expected-status: 204         # 期望状态码，不符则视为不可用
    override: {}                   # 节点字段覆写，见下文
    filter: {}                     # 节点过滤，见下文
```

**缓存路径说明**：默认只允许存 mihomo Home Dir 下的 proxies 文件夹，文件名为 URL 的 md5。要存到其他位置，设置 `SAFE_PATHS` 环境变量（语法同系统 PATH：Windows 分号分隔，其他系统冒号分隔）。

### 加密订阅（age 格式）

```yaml
proxy-providers:
  encrypted:
    type: http
    url: "https://example.com/encrypted-sub"
    age-secret-key: AGE-SECRET-KEY-1ZTQLLN0A4U3ZTT3DCZKYN0CGZEZQLWX2DFTXUWMT4ZHR0N2UG6LSW9NT0N
```

**age 加密工具**：

```sh
mihomo age keygen              # 生成 x25519 key
mihomo age keygen-pq          # 生成 mlkem768-x25519 后量子 key
mihomo age convert <secret>    # 从 secret 导出 public key
mihomo age decrypt <secret> <in> <out>   # 解密（- 表示 stdin/stdout）
mihomo age encrypt <public> <in> <out>   # 加密
```

**age 支持格式**：仅 `age-encryption.org/v1` official ASCII armor；key 仅支持 x25519 和 mlkem768-x25519 hybrid post-quantum。

### File 订阅（本地文件）

```yaml
proxy-providers:
  test:
    type: file
    path: /test.yaml
    health-check:
      enable: true
      interval: 36000
      url: https://cp.cloudflare.com/generate_204
```

### Inline 订阅（内联节点）

```yaml
proxy-providers:
  provider2:
    type: inline
    dialer-proxy: proxy        # 内联节点用哪个代理拨号
    payload:
      - name: "ss1"
        type: ss
        server: server
        port: 443
        cipher: chacha20-ietf-poly1305
        password: "password"
```

## 节点字段覆写（override）

```yaml
proxy-providers:
  provider1:
    override:
      skip-cert-verify: true   # 跳过证书校验
      name-cert-verify: example.com  # 仅修改证书 DNSName 校验目标，不修改 SNI
      udp: true                # 强制开启 UDP
      down: "50 Mbps"          # 下行限速
      up: "10 Mbps"            # 上行限速
      dialer-proxy: proxy      # 拨号代理
      interface-name: tailscale0  # 出口网卡
      routing-mark: 233        # fwmark，仅 Linux
      ip-version: ipv4-prefer  # IP 版本偏好
      additional-prefix: "[provider1]"  # 节点名前缀
      additional-suffix: "test"         # 节点名后缀
      proxy-name:              # 名字替换，支持正则
        - pattern: "test"
          target: "TEST"
        - pattern: "IPLC-(.*?)倍"
          target: "iplc x $1"
```

## 表达式覆写（override-expr）

yq v4 风格的节点覆写子集。数组项按顺序执行，**晚于固定字段 override**。

```yaml
proxy-providers:
  provider1:
    override-expr:
      - '.name = "[provider1] " + .name'                   # 普通赋值
      - '.plugin-opts.mode = "tls"'                        # 自动创建缺失的 mapping
      - '.alpn[] |= upcase'                                # 更新数组中每一项
      - 'del(.skip-cert-verify)'                           # 删除字段
      - '.name = (.name | trim | upcase)'                  # 管道需加括号
      - '.name = "[\(.type)] \(.name):\(.port)"'           # 字符串插值
      - '(select(.port == 443) | .tls) = true'             # 条件不匹配时不修改
      - '.tags |= (unique | sort)'                         # 去重后排序
      - '.names = [.servers[] | select(.enabled) | .name]' # 收集多个结果
      - '.servers |= map(select(.enabled))'                # 筛选数组
      - '.options |= with_entries(.key |= upcase)'         # 转换 mapping
```

### 路径语法

- `.` 根、`.name`、`."a.b"`、`.["a.b"]`
- `.items[0]`、`.items[-1]`
- `[]` 遍历数组或 mapping
- 读取缺失路径或穿过标量返回 `null`
- 赋值创建缺失的 mapping 和非负数组索引，但不穿过标量

### 运算符

- **赋值**：`=`、`|=`、`+=`、`-=`、`*=`
- **删除**：`del(.field)`、`del(.a, .b)`
- **算术**：`+`、`-`、`*`、`/`、`%`
- **比较**：`==`、`!=`、`<`、`<=`、`>`、`>=`
- **逻辑**：`and`、`or`、`//`（默认值）
- **特殊**：`+` 可拼接字符串/数组或浅合并 mapping；`*` 可做数乘、字符串重复、数组替换或深合并 mapping；`/` 分割字符串

### 流操作

- 管道 `|`、逗号 union、`select`
- `[...]` 将零到多个结果收集为数组

### 内置函数

| 类别 | 函数 |
|---|---|
| 查询 | `length`、`keys`、`has(key/index)`、`contains(value)`、`select(condition)` |
| 数组 | `reverse`、`sort`、`unique`、`flatten([depth])`、`any`、`all` |
| 转换 | `map`、`map_values`、`filter`、`to_entries`、`from_entries`、`with_entries`、`any_c`、`all_c` |
| 字符串 | `test(pattern[, "g"])`、`sub(pattern, replacement)`、`split(separator)`、`join(separator)`、`upcase`、`downcase`、`trim` |
| 类型 | `tostring`、`tonumber`、`type`、`not` |

**类型限制**：
- `sort` 只支持标量数组
- `any`/`all` 只支持无参数形式
- `map`/`filter`/`map_values` 支持数组或 mapping
- `with_entries` 只支持 mapping，`any_c`/`all_c` 只支持数组
- `tonumber` 支持十进制、`0x` 十六进制、`0o` 八进制、浮点字符串
- 字符串 `length` 按 UTF-8 字节数计算
- `split(null)` 不产生结果，`join` 只接受数组
- `from_entries` 只接受字符串 key
- `map`/`filter` 返回数组，`map_values` 保持输入集合类型
- `to_entries(null)` 不产生结果
- `==`/`!=` 按 yq 标量文本值比较，不做结构化比较
- `<`/`<=`/`>`/`>=` 只支持数字、字符串、null
- 只有 `false` 和 `null` 按假值处理

**求值规则**：
- 采用值语义
- 越界读取不扩展源数组；右侧 `flatten`/`map_values` 不隐式修改源路径
- 修改源路径必须用 `|=`
- 右侧无结果时保留目标原值，不自动创建 null
- mapping 流、keys、entries 按 key 排序（因 `map[string]any` 不保留 YAML key 顺序）
- 字符串支持 `"[\(.type)] \(.name)"` 插值，多结果时用第一个
- 字符串外的 `#` 忽略该数组项后续内容

**不支持**：变量（`as`/`$x`）、`reduce`、动态路径（`.[$key]`）、递归下降（`..`）、多文档、文件/环境访问、YAML tag/样式/注释处理、yq CLI 参数。

## 节点过滤（filter）

```yaml
proxy-providers:
  provider1:
    filter:
      include: "^(?!.*日本|JP).*"    # 包含匹配的节点（正则）
      exclude: "^直连"               # 排除匹配的节点
    exclude-filter:                   # 仅排除
      - "^直连"
      - "IPv6"
```

## 在策略组中引用

```yaml
proxy-groups:
  - name: "MySub"
    type: select
    use: [provider1]           # 引用 provider，自动导入其节点
    proxies: [DIRECT]
    filter: "HK|TW"           # 组级别过滤（正则）
    empty-fallback: DIRECT    # 组为空时的回退（只支持 proxy 名）
```

## 常用订阅配置模板

### 完整订阅配置

```yaml
proxy-providers:
  sub-main:
    type: http
    url: "https://example.com/sub"
    interval: 21600          # 6小时
    path: ./providers/sub-main.yaml
    proxy: DIRECT
    header:
      User-Agent:
        - "Clash/1.0.0"
    health-check:
      enable: true
      interval: 600
      url: https://cp.cloudflare.com/generate_204
      lazy: true
    override:
      udp: true
      skip-cert-verify: false
    override-expr:
      - '.name = "[订阅] \(.name)"'
    filter:
      exclude: "^直连|IPv6"
```

### 订阅转换常用技巧

| 需求 | override-expr |
|---|---|
| 加前缀 | `'.name = "[机场] " + .name'` |
| 加后缀 | `'.name = .name + " (代理)"'` |
| 加协议标签 | `'.name = "[\(.type)] \(.name)"'` |
| 加端口 | `'.name = "\(.name):\(.port)"'` |
| 强制UDP | `'.udp = true'` |
| 强制证书校验 | `'.skip-cert-verify = false'` |
| 删除字段 | `'del(.plugin)'` |
| 条件过滤 | `'(select(.port != 443) | .udp) = false'` |

## 与 Clash 格式的区别

1. **MRS 格式**：mihomo 规则集用 `.mrs` 二进制（Clash 用 `.list`/`.yaml`）
2. **override-expr**：yq 表达式覆写，Clash 只有固定字段覆写
3. **age 加密**：mihomo 原生支持 age 加密订阅
4. **empty-fallback**：Clash 无此字段
5. **size-limit**：下载大小限制，Clash 无此字段
6. **header 多值**：header 值可以是数组（多个 User-Agent 轮询）
