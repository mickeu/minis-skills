# HTTP 抓包
在 Egern 中，`http_captures` 配置允许您定义特定的域名通配符，这些域名通配符的 HTTP 请求和响应将被应用记录下来。这对于调试和查看特定域名的 HTTP 交互特别有用。支持 glob 通配符（如 `*.example.com`）。
提示
抓取 HTTPS 流量需要配置 MITM 并安装 CA 证书。
## 配置说明​
`http_captures` 支持两种格式：
### 简单格式（字符串数组）​
直接指定需要捕获的主机名列表：
    http_captures:  
      - "*.example.com"  
      - "test.com"  
### 结构化格式（包含排除项）​
可以同时指定包含和排除的主机名：
    http_captures:  
      includes:  
        - "*.example.com"  
        - "test.com"  
      excludes:  
        - "*.internal.example.com"  
使用排除列表可以在捕获大范围域名时排除特定的子域名。