# URL Rewriting
The URL rewriting feature supports three modes:
  * **Redirect mode** : Returns an HTTP 3xx redirect response. The client is aware of the redirect and initiates a new request.
  * **Header mode** : Directly modifies the request URI and Host header, transparently forwarding the request to the new address without the client's awareness.
  * **Reject mode** : Directly returns a specific response body to block the request, commonly used for ad filtering.
Rewriting the URL of HTTPS requests requires configuring MITM and installing a CA certificate. Below is a detailed explanation of each field:
  * **match** (string), required
A regular expression for URL matching, which matches the full request URL (including protocol, hostname, path, and query parameters). Capture groups are supported.
  * **location** (string), required
The redirect target URL. Supports referencing capture groups with `$1`, `$2`, etc. The following special values can also be used to block requests:
    * `http://reject/` — returns a 404 empty response
    * `http://reject-200/` — returns a 200 empty response
    * `http://reject-dict/` — returns an empty JSON object `{}`
    * `http://reject-array/` — returns an empty JSON array `[]`
    * `http://reject-img/` — returns a 1×1 transparent GIF
    * `http://reject-video/` — returns an empty MP4
  * **status_code** (integer), optional
The HTTP redirect status code (`301` permanent redirect, `302` temporary redirect, `307` temporary redirect preserving method, `308` permanent redirect preserving method). When omitted, header mode is used.
  * **disabled** (bool), optional
Whether to disable this rule.
## Configuration Example​
    url_rewrites:  
      # Redirect mode: returns a 307 redirect response  
      - match: "(.*google)\\.cn"  
        location: $1.com  
        status_code: 307  
      # Redirect mode: returns a 301 permanent redirect  
      - match: "^https://old\\.example\\.com/(.*)$"  
        location: "https://new.example.com/$1"  
        status_code: 301  
      # Header mode: transparent forwarding, client unaware  
      - match: "^https://api\\.example\\.com/v1/(.*)$"  
        location: "https://api.example.com/v2/$1"  
      # Reject mode: block ad requests, return an empty JSON object  
      - match: "^https://ads\\.example\\.com"  
        location: "http://reject-dict/"  
In the first example, the system will find all requests whose URL matches `(.*google)\.cn` and return a 307 redirect response to redirect them to the corresponding `.com` domain. In the third example, the system transparently forwards matching requests to the v2 API without the client being aware of the address change. In the last example, matching ad requests are blocked and an empty JSON object is returned.