# URL Scheme
所有 URL Scheme 均支持 `x-success` 参数，用于操作完成后的回调。例如：`egern:/start?x-success=myapp://callback`
**启动 Egern VPN**
`egern:/start`
**停止 Egern VPN**
`egern:/stop`
**添加配置文件**
`egern:/profiles/new?name=name&url=url`
参数说明：
  * `url`（必填）：配置文件的 URL
  * `name`（可选）：配置名称
**添加代理服务器**
`egern:/proxies/new`
**添加策略组**
`egern:/policy_groups/new?type=type&external_type=external_type&name=name&policy=policy&url=url`
参数说明：
  * `type`（可选）：策略组类型，默认为 `external`
  * `external_type`（可选）：外部策略组类型，默认为 `auto_test`
  * `name`（可选）：策略组名称
  * `policy`（可选）：策略
  * `url`（可选）：策略的 URL
**添加订阅**
`egern:/subscriptions/new?url=url`
参数说明：
  * `url`（可选）：订阅的 URL
**添加规则**
`egern:/rules/new?type=domain&match=match&policy=DIRECT`
参数说明：
  * `type`（可选）：规则类型（如 `domain` 或 `domain_keyword`），默认为 `rule_set`
  * `match`（可选）：匹配项（如具体域名 `example.com`）
  * `policy`（可选）：策略（如 `DIRECT` 或 `PROXY`）
**添加模块**
`egern:/modules/new?name=name&url=url`
参数说明：
  * `url`（必填）：模块文件的 URL
  * `name`（可选）：模块名称
**打开连接列表**
`egern:/connections`
**打开连接详情**
`egern:/connections/id`
参数说明：
  * `id`（必填）：连接的 ID