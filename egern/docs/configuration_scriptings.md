# Scripting
Egern allows users to flexibly control network request/response handling, scheduled tasks, network change events, and manually triggered generic scripts by writing JavaScript scripts.
## Script Types​
The `scriptings` configuration includes five types of scripts:
Type| Description  
---|---  
`http_request`| HTTP request script, executed before sending the request  
`http_response`| HTTP response script, executed after receiving the response  
`schedule`| Scheduled script, executed at intervals based on a cron expression  
`generic`| Generic script, manually triggered  
`network`| Network change script, executed when the network environment changes  
## HTTP Request/Response Scripts​
  * **name** (string), required
The name of the script.
  * **match** (string), required
A regular expression for URL matching.
  * **script_url** (string), required
The URL of the script file, which can be a local path or a remote link.
  * **env** (object), optional
Environment variables (key-value pairs) passed to the script, accessible via `ctx.env`. See Environment Variables for details.
  * **update_interval** (integer), optional
The update interval for the script file in seconds. Defaults to 86400 (24 hours).
  * **max_size** (integer), optional
The maximum request/response body size to process in bytes. Bodies exceeding this size will not be passed to the script. Defaults to 1048576 (1MB).
  * **timeout** (integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
  * **body_required** (boolean), optional
Whether the request/response body is needed. Defaults to `false`. Set to `true` if you need to read or modify the body.
  * **binary_body** (boolean), optional
Whether to handle the request/response body in binary mode. Defaults to `false`. Set to `true` when processing binary content such as images.
  * **disabled** (boolean), optional
Whether to disable this script.
## Scheduled Scripts​
Execute scripts at scheduled intervals based on cron expressions, suitable for scenarios such as scheduled check-ins and data synchronization.
Supports the standard 5-field format (minute, hour, day, month, weekday) and the 6-field format (second, minute, hour, day, month, weekday).
  * **name** (string), required
The name of the script.
  * **cron** (string), required
A cron expression (e.g., `0 8 * * *` means every day at 8:00 AM).
  * **script_url** (string), required
The URL of the script file, which can be a local path or a remote link.
  * **env** (object), optional
Environment variables (key-value pairs) passed to the script, accessible via `ctx.env`. See Environment Variables for details.
  * **update_interval** (integer), optional
The update interval for the script file in seconds. Defaults to 86400.
  * **timeout** (integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
  * **disabled** (boolean), optional
Whether to disable this script.
## Generic Scripts​
Manually triggered scripts, primarily used as associated scripts for Widgets.
  * **name** (string), required
The name of the script.
  * **script_url** (string), required
The URL of the script file.
  * **env** (object), optional
Environment variables (key-value pairs) passed to the script, accessible via `ctx.env`. See Environment Variables for details.
  * **update_interval** (integer), optional
The update interval for the script file in seconds. Defaults to 86400.
  * **timeout** (integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
  * **disabled** (boolean), optional
Whether to disable this script.
## Network Change Scripts​
Execute scripts when the network environment changes, such as Wi-Fi switching, cellular network connection, VPN status changes, and similar scenarios. Can be used for automatically switching proxy nodes, sending notifications, and more.
  * **name** (string), required
The name of the script.
  * **script_url** (string), required
The URL of the script file.
  * **env** (object), optional
Environment variables (key-value pairs) passed to the script, accessible via `ctx.env`. See Environment Variables for details.
  * **update_interval** (integer), optional
The update interval for the script file in seconds. Defaults to 86400.
  * **timeout** (integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
  * **disabled** (boolean), optional
Whether to disable this script.
## Configuration Example​
    scriptings:  
      - http_request:  
          name: "Modify Request Headers"  
          match: "^https://api\\.example\\.com/"  
          script_url: "https://example.com/scripts/modify-header.js"  
          env:  
            TOKEN: "my-secret-token"  
          timeout: 30  
          body_required: true  
      - http_response:  
          name: "Parse Response"  
          match: "^https://api\\.example\\.com/data"  
          script_url: "https://example.com/scripts/parse-response.js"  
          body_required: true  
          max_size: 2097152  
      - schedule:  
          name: "Daily Check-in"  
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
          name: "Network Change Notification"  
          script_url: "https://example.com/scripts/network-change.js"  
          timeout: 30