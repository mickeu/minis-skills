# HTTP Header Rewriting
The HTTP header rewriting feature allows users to add, replace, or delete headers in HTTP requests or responses that match specific URLs. MITM decryption is required to modify HTTPS traffic.
## Adding Header Information​
If the header already exists, it will be replaced; if it does not exist, it will be added.
  * **match** (string), required
A regular expression for URL matching.
  * **name** (string), required
The name of the header to add.
  * **value** (string), required
The value of the header to add.
  * **type** (string), optional
Applies to `request` or `response`. Defaults to `request`.
  * **disabled** (bool), optional
Whether to disable this rule.
### Configuration Example​
    header_rewrites:  
      - add:  
          match: "^https://example\\.com"  
          name: X-Custom-Header  
          value: custom-value  
          type: request  
## Replacing Header Information​
Semantically intended for replacing the value of an existing header. The actual behavior is the same as `add`: if the header exists, it will be replaced; if it does not exist, it will be added.
  * **match** (string), required
A regular expression for URL matching.
  * **name** (string), required
The name of the header to replace.
  * **value** (string), required
The new value of the header.
  * **type** (string), optional
Applies to `request` or `response`. Defaults to `request`.
  * **disabled** (bool), optional
Whether to disable this rule.
### Configuration Example​
    header_rewrites:  
      - replace:  
          match: "^https://api\\.example\\.com"  
          name: Cache-Control  
          value: no-cache  
          type: response  
## Deleting Header Information​
  * **match** (string), required
A regular expression for URL matching.
  * **name** (string), required
The name of the header to delete.
  * **type** (string), optional
Applies to `request` or `response`. Defaults to `request`.
  * **disabled** (bool), optional
Whether to disable this rule.
### Configuration Example​
    header_rewrites:  
      - delete:  
          match: ".*"  
          name: X-Tracking-Id  
          type: request