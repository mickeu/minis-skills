# HTTP 消息体重写
消息体重写允许用户修改匹配特定 URL 的 HTTP 请求或响应的消息体。支持正则替换和 jq 过滤器两种方式。需要 MITM 解密才能修改 HTTPS 流量。
## 正则替换​
通过正则表达式查找并替换消息体中的内容。
### 请求体正则替换 (request_regex)​
  * **match** (string), 必填
URL 匹配正则表达式。
  * **find** (string), 必填
在消息体中查找的正则表达式，支持捕获组。
  * **replace** (string), 必填
替换内容，支持 `$1`、`$2` 等引用捕获组。
  * **disabled** (bool), 可选
是否禁用此规则。
### 响应体正则替换 (response_regex)​
字段与请求体正则替换相同，作用于响应体。
    body_rewrites:  
      - response_regex:  
          match: "^https://api\\.example\\.com/data"  
          find: '"status":\s*"pending"'  
          replace: '"status": "completed"'  
      - request_regex:  
          match: "^https://api\\.example\\.com/submit"  
          find: '"version":\s*"1.0"'  
          replace: '"version": "2.0"'  
## jq 过滤器​
使用 jq 表达式处理 JSON 格式的消息体，适合对 JSON 数据进行结构化的修改。
### 请求体 jq 过滤器 (request_jq)​
  * **match** (string), 必填
URL 匹配正则表达式。
  * **filter** (string), 必填
jq 过滤器表达式（如 `.data.field = "value"` 或 `del(.unwanted)`）。
  * **disabled** (bool), 可选
是否禁用此规则。
### 响应体 jq 过滤器 (response_jq)​
字段与请求体 jq 过滤器相同，作用于响应体。
    body_rewrites:  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.timestamp = now | .data.version = "2.0"'  
      - response_jq:  
          match: "^https://api\\.example\\.com/data"  
          filter: 'del(.tracking) | .data.processed = true'  
## 配置示例​
    body_rewrites:  
      # 响应体正则替换  
      - response_regex:  
          match: "^https://api\\.example\\.com/data"  
          find: '"status":\s*"pending"'  
          replace: '"status": "completed"'  
      # 请求体 jq 过滤器  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.timestamp = now | .data.version = "2.0"'  
      # 响应体 jq 过滤器  
      - response_jq:  
          match: "^https://api\\.example\\.com/config"  
          filter: '.settings.theme = "dark"'