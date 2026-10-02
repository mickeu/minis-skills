# URL 重写
URL 重写功能支持三种模式：
  * **重定向模式** ：返回 HTTP 3xx 重定向响应，客户端会感知到重定向并发起新请求。
  * **Header 模式** ：直接修改请求的 URI 和 Host 头，透明地将请求转发到新地址，客户端无感知。
  * **Reject 模式** ：直接返回特定响应体来拦截请求，常用于广告过滤。
重写 HTTPS 请求的 URL 需要配置 MITM 并安装 CA 证书。以下是各字段的详细解释：
  * **match** (string), 必填
URL 匹配正则表达式，匹配完整请求 URL（含协议、主机名、路径和查询参数）。支持捕获组。
  * **location** (string), 必填
重定向目标 URL，支持使用 `$1`、`$2` 等引用捕获组。也可以使用以下特殊值来拦截请求：
    * `http://reject/` — 返回 404 空响应
    * `http://reject-200/` — 返回 200 空响应
    * `http://reject-dict/` — 返回空 JSON 对象 `{}`
    * `http://reject-array/` — 返回空 JSON 数组 `[]`
    * `http://reject-img/` — 返回 1×1 透明 GIF
    * `http://reject-video/` — 返回空 MP4
  * **status_code** (integer), 可选
HTTP 重定向状态码（`301` 永久重定向、`302` 临时重定向、`307` 临时重定向保持方法、`308` 永久重定向保持方法）。省略此字段时使用 header 模式。
  * **disabled** (bool), 可选
是否禁用此规则。
## 配置示例​
    url_rewrites:  
      # 重定向模式：返回 307 重定向响应  
      - match: "(.*google)\\.cn"  
        location: $1.com  
        status_code: 307  
      # 重定向模式：返回 301 永久重定向  
      - match: "^https://old\\.example\\.com/(.*)$"  
        location: "https://new.example.com/$1"  
        status_code: 301  
      # Header 模式：透明转发，客户端无感知  
      - match: "^https://api\\.example\\.com/v1/(.*)$"  
        location: "https://api.example.com/v2/$1"  
      # Reject 模式：拦截广告请求，返回空 JSON 对象  
      - match: "^https://ads\\.example\\.com"  
        location: "http://reject-dict/"  
在第一个示例中，系统将查找所有 URL 匹配 `(.*google)\.cn` 的请求，并返回 307 重定向响应将其引导至对应的 `.com` 域名。在第三个示例中，系统将匹配的请求透明地转发到 v2 API，客户端不会感知到地址变化。在最后一个示例中，匹配到的广告请求会被直接拦截并返回空 JSON 对象。