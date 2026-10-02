# HTTP Message Body Rewriting
Message body rewriting allows users to modify the body of HTTP requests or responses that match specific URLs. It supports two methods: regex replacement and jq filters. MITM decryption is required to modify HTTPS traffic.
## Regex Replacement​
Find and replace content in the message body using regular expressions.
### Request Body Regex Replacement (request_regex)​
  * **match** (string), required
A regular expression for URL matching.
  * **find** (string), required
A regular expression to search for in the message body. Capture groups are supported.
  * **replace** (string), required
The replacement content. Supports referencing capture groups with `$1`, `$2`, etc.
  * **disabled** (bool), optional
Whether to disable this rule.
### Response Body Regex Replacement (response_regex)​
The fields are the same as request body regex replacement, but apply to the response body.
    body_rewrites:  
      - response_regex:  
          match: "^https://api\\.example\\.com/data"  
          find: '"status":\s*"pending"'  
          replace: '"status": "completed"'  
      - request_regex:  
          match: "^https://api\\.example\\.com/submit"  
          find: '"version":\s*"1.0"'  
          replace: '"version": "2.0"'  
## jq Filter​
Use jq expressions to process JSON-formatted message bodies, suitable for making structured modifications to JSON data.
### Request Body jq Filter (request_jq)​
  * **match** (string), required
A regular expression for URL matching.
  * **filter** (string), required
A jq filter expression (e.g., `.data.field = "value"` or `del(.unwanted)`).
  * **disabled** (bool), optional
Whether to disable this rule.
### Response Body jq Filter (response_jq)​
The fields are the same as request body jq filter, but apply to the response body.
    body_rewrites:  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.timestamp = now | .data.version = "2.0"'  
      - response_jq:  
          match: "^https://api\\.example\\.com/data"  
          filter: 'del(.tracking) | .data.processed = true'  
## Configuration Example​
    body_rewrites:  
      # Response body regex replacement  
      - response_regex:  
          match: "^https://api\\.example\\.com/data"  
          find: '"status":\s*"pending"'  
          replace: '"status": "completed"'  
      # Request body jq filter  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.timestamp = now | .data.version = "2.0"'  
      # Response body jq filter  
      - response_jq:  
          match: "^https://api\\.example\\.com/config"  
          filter: '.settings.theme = "dark"'