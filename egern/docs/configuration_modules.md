# Modules
In Egern, modules are preset configuration snippets that allow users to conveniently enable or disable a specific set of network processing rules. Modules cover a wide range of functionality and can include rules, URL rewrites, header rewrites, body rewrites, Map Local, scripts, MITM, HTTP captures, and widgets. When a module is enabled, its configuration is merged into Egern's main configuration.
## Module Reference Configuration​
Referencing modules in the main configuration file:
  * **name** (string), optional
The display name of the module, overriding the name defined within the module file. When not set, the `name` field from the module file or the URL is used.
  * **url** (string), required
The address of the module file, which can be a local file path or a remote URL.
  * **compat_arguments** (object), optional
Arguments passed to the module, used to override the default argument values defined in the module file. Arguments are substituted as variables when the module is parsed. See Argument Substitution for the placeholder syntax and rules.
  * **env** (object), optional
Environment variables (key-value pairs) passed to scripts and widgets in the module. Module-level env has the highest priority and overrides variables with the same key in widgets and scripts. See Environment Variables for details.
  * **update_interval** (integer), optional
When the module file is a remote URL, this parameter specifies the update interval (in seconds) for the module. The default value is 86400 (24 hours).
  * **enabled** (boolean), optional
Controls whether the module is enabled. The default value is `true`.
### Configuration Example​
    modules:  
      - name: "Ad Blocking"  
        url: "https://example.com/adblock.yaml"  
        enabled: true  
        update_interval: 86400  
      - url: "https://example.com/custom.yaml"  
        compat_arguments:  
          API_KEY: "your_api_key"  
          REGION: "cn"  
        env:  
          REFRESH_INTERVAL: "300"  
## Module File Format​
A module file itself is a YAML-formatted file containing metadata and configuration content.
### Metadata Fields​
  * **name** (string), optional
Module name.
  * **description** (string), optional
Module description.
  * **author** (string), optional
Module author.
  * **homepage** (string), optional
Module homepage URL.
  * **manual** (string), optional
Usage instructions URL.
  * **icon** (string), optional
Module icon, supporting SF Symbols names or URLs.
  * **open_url** (string), optional
URL to open the settings page.
  * **compat_arguments** (object), optional
Default values for module arguments. See Argument Substitution for how to reference them with placeholders.
  * **compat_arguments_desc** (string), optional
Documentation for module arguments.
  * **env_schema** (object), optional
Declares the available environment variables for the module and their types. Egern will automatically generate corresponding UI controls on the module settings page. Keys are environment variable names, and values are descriptor objects with the following fields:
    * **name** (string), optional — Display name shown in the UI. Falls back to the key name if not set.
    * **description** (string), optional — Descriptive text displayed below the control.
    * **default_value** (string), optional — Default value, shown as placeholder text in the input field. Not written to env unless the user explicitly sets a value.
    * **options** (array), optional — List of allowed values.
      * `["true", "false"]` generates a Toggle switch.
      * Other values generate a Picker.
      * When not set, a TextField is generated.
        env_schema:  
      TITLE:  
        name: Title  
        description: The title text to display  
        default_value: "Default Title"  
      ENABLE_FEATURE:  
        name: Enable Feature  
        options:  
          - "true"  
          - "false"  
      THEME:  
        name: Theme  
        options:  
          - light  
          - dark  
          - auto  
### Configuration Content Fields​
A module file can contain the following configuration items, which are merged with the main configuration:
  * **dns** (object), optional
DNS configuration.
  * **rules** (array), optional
Rule list.
  * **url_rewrites** (array), optional
URL rewrite list.
  * **header_rewrites** (array), optional
Header rewrite list.
  * **body_rewrites** (array), optional
Body rewrite list.
  * **map_locals** (array), optional
Map Local list.
  * **scriptings** (array), optional
Script list.
  * **mitm** (object), optional
MITM configuration.
  * **http_captures** (array), optional
HTTP capture hostname list.
  * **widgets** (array), optional
Widget list.
  * **bypass_tunnel_proxy** (array), optional
List of domains that bypass the tunnel proxy.
  * **real_ip_domains** (array), optional
List of domains that use real IP addresses (instead of Fake IP).
### Configuration Example​
    name: "Ad Blocking Module"  
    description: "Filters common ads and trackers"  
    author: "module-author"  
    homepage: "https://github.com/example/adblock-module"  
    icon: "shield.fill"  
    compat_arguments:  
      BLOCK_MODE: "reject"  
    rules:  
      - domain_suffix:  
          match: "ad.example.com"  
          policy: REJECT  
    url_rewrites:  
      - match: "^https://ads\\.example\\.com"  
        location: "https://reject/"  
        status_code: 307  
    mitm:  
      hostnames:  
        - "*.example.com"  
    widgets:  
      - name: adblock-info  
## Argument Substitution​
A module file can expose configurable arguments through `compat_arguments`, letting users customize the module without editing its source. The module file declares the arguments and their defaults and references them with placeholders; the module reference in the main configuration overrides the values. Substitution happens when the module is parsed.
How it works:
  1. The **module file** declares each argument and its default value under `compat_arguments`, then references it elsewhere with the `{{{ARGUMENT_NAME}}}` placeholder.
  2. The **module reference** in the main configuration overrides an argument through its own `compat_arguments`.
  3. On load, every `{{{ARGUMENT_NAME}}}` placeholder is replaced with the user-provided value, falling back to the default declared in the module file.
### Example​
Module file (`custom.yaml`):
    name: "Custom Module"  
    compat_arguments:  
      REGION: "cn"            # default value  
      BLOCK_POLICY: "REJECT"  
      TIMEOUT: 30             # numeric default  
    rules:  
      - domain_suffix:  
          match: "{{{REGION}}}.example.com"   # string field → quote the placeholder  
          policy: "{{{BLOCK_POLICY}}}"  
    scriptings:  
      - http_request:  
          name: "Example"  
          match: "^https://example\\.com"  
          script_url: "https://example.com/s.js"  
          timeout: {{{TIMEOUT}}}              # numeric field → leave it unquoted  
Module reference in the main configuration:
    modules:  
      - url: "https://example.com/custom.yaml"  
        compat_arguments:  
          REGION: "us"        # overrides the default  
          TIMEOUT: 60         # overrides the numeric default  
          # BLOCK_POLICY is not set, so it falls back to "REJECT"  
After substitution the module is parsed as:
    rules:  
      - domain_suffix:  
          match: "us.example.com"  
          policy: "REJECT"  
    scriptings:  
      - http_request:  
          name: "Example"  
          match: "^https://example\\.com"  
          script_url: "https://example.com/s.js"  
          timeout: 60          # parsed as a real number  
### Rules and Limitations​
  * **Declare every argument.** Only keys present in the module file's `compat_arguments` are substituted. A key supplied only in the reference but not declared in the module file is ignored.
  * **Quote a placeholder exactly as you would the literal value.** Substitution preserves your quoting, and YAML infers the type from it:
    * **String** field — quote it: `match: "{{{REGION}}}.example.com"`, `name: "{{{LABEL}}}"`. Quoting keeps the result a string even when the value is all-digits or contains `:`.
    * **Number** or **boolean** field — leave it unquoted: `timeout: {{{TIMEOUT}}}`, `enabled: {{{FLAG}}}`. The substituted value is then parsed as a real number or boolean.
  * **Avoid quote-breaking characters in string values.** A quoted placeholder is filled by plain text replacement inside the surrounding quotes, so a value containing a double quote (`"`), a backslash (`\`), or a newline breaks the quotes and yields invalid YAML. (A value containing `:` or `,` is fine.)