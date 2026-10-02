# 脚本
Egern 允许用户通过编写 JavaScript 脚本来灵活地控制网络请求/响应的处理、定时任务、网络变化事件以及手动触发的通用脚本。
## 脚本类型​
`scriptings` 配置包含五种类型的脚本：
类型| 说明  
---|---  
`http_request`| HTTP 请求脚本，在发送请求前执行  
`http_response`| HTTP 响应脚本，在收到响应后执行  
`schedule`| 定时脚本，按 cron 表达式定时执行  
`generic`| 通用脚本，手动触发执行  
`network`| 网络变化脚本，在网络环境变化时执行  
## HTTP 请求/响应脚本​
  * **name** (string), 必填
脚本名称。
  * **match** (string), 必填
URL 匹配正则表达式。
  * **script_url** (string), 必填
脚本文件的 URL，可以是本地路径或远程链接。
  * **env** (object), 可选
传递给脚本的环境变量（键值对），在脚本中可通过 `ctx.env` 访问。详见 环境变量。
  * **update_interval** (integer), 可选
脚本文件更新间隔（秒），默认 86400（24 小时）。
  * **max_size** (integer), 可选
最大处理的请求/响应体大小（字节），超过此大小不传递给脚本，默认 1048576 (1MB)。
  * **timeout** (integer), 可选
脚本执行超时时间（秒），默认 10 秒，最大 600 秒。
  * **body_required** (boolean), 可选
是否需要请求/响应体，默认 `false`。如需读取或修改 body 需设为 `true`。
  * **binary_body** (boolean), 可选
是否以二进制方式处理请求/响应体，默认 `false`。处理图片等二进制内容时需设为 `true`。
  * **disabled** (boolean), 可选
是否禁用此脚本。
## 定时脚本​
按照 cron 表达式定时执行脚本，适用于定时签到、数据同步等场景。
支持标准 5 字段格式（分 时 日 月 周）和 6 字段格式（秒 分 时 日 月 周）。
  * **name** (string), 必填
脚本名称。
  * **cron** (string), 必填
Cron 表达式（如 `0 8 * * *` 表示每天早上 8:00）。
  * **script_url** (string), 必填
脚本文件的 URL，可以是本地路径或远程链接。
  * **env** (object), 可选
传递给脚本的环境变量（键值对），在脚本中可通过 `ctx.env` 访问。详见 环境变量。
  * **update_interval** (integer), 可选
脚本文件更新间隔（秒），默认 86400。
  * **timeout** (integer), 可选
脚本执行超时时间（秒），默认 10 秒，最大 600 秒。
  * **disabled** (boolean), 可选
是否禁用此脚本。
## 通用脚本​
手动触发执行的脚本，主要作为小组件的关联脚本使用。
  * **name** (string), 必填
脚本名称。
  * **script_url** (string), 必填
脚本文件的 URL。
  * **env** (object), 可选
传递给脚本的环境变量（键值对），在脚本中可通过 `ctx.env` 访问。详见 环境变量。
  * **update_interval** (integer), 可选
脚本文件更新间隔（秒），默认 86400。
  * **timeout** (integer), 可选
脚本执行超时时间（秒），默认 10 秒，最大 600 秒。
  * **disabled** (boolean), 可选
是否禁用此脚本。
## 网络变化脚本​
在网络环境变化时执行脚本，如 Wi-Fi 切换、蜂窝网络连接、VPN 状态变化等场景。可用于自动切换代理节点、发送通知等。
  * **name** (string), 必填
脚本名称。
  * **script_url** (string), 必填
脚本文件的 URL。
  * **env** (object), 可选
传递给脚本的环境变量（键值对），在脚本中可通过 `ctx.env` 访问。详见 环境变量。
  * **update_interval** (integer), 可选
脚本文件更新间隔（秒），默认 86400。
  * **timeout** (integer), 可选
脚本执行超时时间（秒），默认 10 秒，最大 600 秒。
  * **disabled** (boolean), 可选
是否禁用此脚本。
## 配置示例​
    scriptings:  
      - http_request:  
          name: "修改请求头"  
          match: "^https://api\\.example\\.com/"  
          script_url: "https://example.com/scripts/modify-header.js"  
          env:  
            TOKEN: "my-secret-token"  
          timeout: 30  
          body_required: true  
      - http_response:  
          name: "解析响应"  
          match: "^https://api\\.example\\.com/data"  
          script_url: "https://example.com/scripts/parse-response.js"  
          body_required: true  
          max_size: 2097152  
      - schedule:  
          name: "每日签到"  
          cron: "0 8 * * *"  
          script_url: "https://example.com/scripts/daily-checkin.js"  
          env:  
            USERNAME: "user123"  
      - generic:  
          name: "server-status"  
          script_url: "https://example.com/scripts/server-status.js"  
          env:  
            API_URL: "https://api.example.com/status"  
      - network:  
          name: "网络切换通知"  
          script_url: "https://example.com/scripts/network-change.js"  
          timeout: 30