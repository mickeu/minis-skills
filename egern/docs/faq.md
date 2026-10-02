# Frequently Asked Questions
## The Relationship Between Rules, Proxies, and Policy Groups in Egern​
### 1\. Rules Determine Policies​
  * **Rules** are conditions used to match network requests. When a network request is made, Egern will match them sequentially according to the rules.
  * Each rule specifies a **policy** , which can be a **proxy name** , **policy group name** , or `DIRECT` and `REJECT`.
### 2\. Policies​
  * A **policy** can be a single **proxy** or a **policy group**.
  * Once a rule is matched, if the policy is a proxy name, the traffic will be forwarded through the specified proxy server.
  * If the policy is a policy group name, Egern will select an appropriate proxy server based on the type and configuration of the policy group.
### 3\. Sub-policies of Policy Groups​
  * A **policy group** can contain multiple **proxies** or **other policy groups** , forming a hierarchical structure.
  * For example, the policy group `Manual Selection` may include `VmessProxy` and `ShadowsocksProxy`, allowing users to manually choose which proxy to use.
  * In nested policy groups, the policy matched by a rule may need to go through several layers of policy groups before determining the final proxy server.
### 4\. Traffic Handling Process​
  1. **Request Initiation** : A user's network request needs to be processed.
  2. **Rule Matching** : Egern matches the configured rules from top to bottom and finds the first rule that meets the condition.
  3. **Policy Determination** : Based on the `policy` of the matched rule, the appropriate policy is determined.
  4. **Policy Parsing** :
     * If the policy is `DIRECT`, the connection is made directly without using a proxy.
     * If the policy is `REJECT`, the connection is blocked.
     * If the policy is a proxy name, that proxy server is used.
     * If the policy is a policy group, the appropriate proxy server is selected according to the policy group's type and configuration.
  5. **Request Forwarding** : The network request is processed and forwarded through the determined proxy server.
## How to Add a Rule Set​
Egern currently supports Surge rule sets. Go to Tools -> Rules -> \+ -> Select the rule-set type, then add the Surge rule set URL.
## How to Add a Module​
Egern currently supports Surge modules. You can add a Surge module URL under Tools -> Modules.