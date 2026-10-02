# Environment Variables
Egern supports configuring environment variables (env) for scripts, widgets, and modules. Environment variables are passed as key-value pairs and can be accessed via `ctx.env` in scripts, allowing the same script to be flexibly configured for different scenarios without modifying the code.
## Basic Usage​
### Defining in Scripts​
All five script types support the `env` field:
    scriptings:  
      - generic:  
          name: "my-script"  
          script_url: "https://example.com/scripts/my-script.js"  
          env:  
            API_KEY: "your_api_key"  
            API_URL: "https://api.example.com"  
      - http_request:  
          name: "modify-header"  
          match: "^https://api\\.example\\.com/"  
          script_url: "https://example.com/scripts/modify-header.js"  
          env:  
            TOKEN: "my-secret-token"  
      - schedule:  
          name: "daily-checkin"  
          cron: "0 8 * * *"  
          script_url: "https://example.com/scripts/checkin.js"  
          env:  
            USERNAME: "user123"  
### Defining in Widgets​
    widgets:  
      - name: "weather-widget"  
        env:  
          CITY: "Shanghai"  
          UNIT: "celsius"  
### Defining in Module References​
    modules:  
      - url: "https://example.com/module.yaml"  
        enabled: true  
        env:  
          API_KEY: "your_api_key"  
          REGION: "cn"  
## Accessing in Scripts​
Environment variables are accessible in scripts via `ctx.env` as key-value pairs:
    export default async function(ctx) {  
      const apiKey = ctx.env.API_KEY;  
      const apiUrl = ctx.env.API_URL;  
      const resp = await ctx.http.get(apiUrl + '/data', {  
        headers: { 'Authorization': 'Bearer ' + apiKey }  
      });  
      const data = await resp.json();  
      console.log(data);  
    }  
## Priority and Merging​
When the same key exists at multiple levels, the priority from highest to lowest is:
**Module > Widget > Script**
Module-level env overrides widget-level variables with the same key, and widget-level env overrides script-level variables with the same key.
### Merging Example​
Given the following configuration:
    scriptings:  
      - generic:  
          name: "my-widget"  
          script_url: "https://example.com/scripts/widget.js"  
          env:  
            COLOR: "blue"  
            TIMEOUT: "10"  
            MODE: "default"  
    widgets:  
      - name: "my-widget"  
        env:  
          COLOR: "red"  
          REGION: "Asia"  
The actual `ctx.env` received by the script will be:
Key| Value| Source  
---|---|---  
`COLOR`| `"red"`| Widget (overrides script's `"blue"`)  
`TIMEOUT`| `"10"`| Script  
`MODE`| `"default"`| Script  
`REGION`| `"Asia"`| Widget  
If this widget comes from a module with env defined in the module reference:
    modules:  
      - url: "https://example.com/module.yaml"  
        env:  
          COLOR: "green"  
          LANG: "zh"  
The final `ctx.env` will be:
Key| Value| Source  
---|---|---  
`COLOR`| `"green"`| Module (highest priority)  
`TIMEOUT`| `"10"`| Script  
`MODE`| `"default"`| Script  
`REGION`| `"Asia"`| Widget  
`LANG`| `"zh"`| Module  
## Use Cases​
  * **API key management:** Store API keys in env so script files can be shared publicly without exposing secrets.
  * **Multi-instance reuse:** Use the same script with different env values to create multiple widgets, e.g., a single weather script displaying different cities.
  * **Module parameterization:** Module authors provide generic functionality; users pass personalized parameters via env.
  * **Environment differentiation:** Use env to distinguish between development/production API endpoints.
    # Same script, different env, displaying weather for different cities  
    scriptings:  
      - generic:  
          name: "weather"  
          script_url: "https://example.com/scripts/weather.js"  
    widgets:  
      - name: "weather-sh"  
        script_name: "weather"  
        env:  
          CITY: "Shanghai"  
      - name: "weather-bj"  
        script_name: "weather"  
        env:  
          CITY: "Beijing"