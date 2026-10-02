# URL Scheme
All URL Schemes support the `x-success` parameter for callback after the operation completes. For example: `egern:/start?x-success=myapp://callback`
**Start Egern VPN**
`egern:/start`
**Stop Egern VPN**
`egern:/stop`
**Add Configuration Profile**
`egern:/profiles/new?name=name&url=url`
Parameter Description:
  * `url` (required): The URL of the configuration file
  * `name` (optional): Name of the configuration
**Add Proxy Server**
`egern:/proxies/new`
**Add Policy Group**
`egern:/policy_groups/new?type=type&external_type=external_type&name=name&policy=policy&url=url`
Parameter Description:
  * `type` (optional): Policy group type, defaults to `external`
  * `external_type` (optional): External policy group type, defaults to `auto_test`
  * `name` (optional): Name of the policy group
  * `policy` (optional): Policy
  * `url` (optional): The URL of the policy
**Add Subscription**
`egern:/subscriptions/new?url=url`
Parameter Description:
  * `url` (optional): The URL of the subscription
**Add Rule**
`egern:/rules/new?type=domain&match=match&policy=DIRECT`
Parameter Description:
  * `type` (optional): Type of rule (e.g., `domain` or `domain_keyword`), defaults to `rule_set`
  * `match` (optional): Matching item (e.g., a specific domain like `example.com`)
  * `policy` (optional): Policy (e.g., `DIRECT` or `PROXY`)
**Add Module**
`egern:/modules/new?name=name&url=url`
Parameter Description:
  * `url` (required): The URL of the module file
  * `name` (optional): Module name
**Open Connections List**
`egern:/connections`
**Open Connection Details**
`egern:/connections/id`
Parameter Description:
  * `id` (required): The ID of the connection