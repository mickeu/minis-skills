# HTTP Captures
In Egern, the `http_captures` configuration allows you to define specific domain wildcard patterns whose HTTP requests and responses will be recorded by the application. This is particularly useful for debugging and inspecting HTTP interactions for specific domains. Glob wildcards are supported (e.g., `*.example.com`).
tip
Capturing HTTPS traffic requires configuring MITM and installing a CA certificate.
## Configuration Details​
`http_captures` supports two formats:
### Simple Format (String Array)​
Directly specify the list of hostnames to capture:
    http_captures:  
      - "*.example.com"  
      - "test.com"  
### Structured Format (With Exclusions)​
You can specify both included and excluded hostnames:
    http_captures:  
      includes:  
        - "*.example.com"  
        - "test.com"  
      excludes:  
        - "*.internal.example.com"  
Using the exclusion list allows you to exclude specific subdomains when capturing a broad range of domains.