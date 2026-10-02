# generic Script

A generic script has no automatic trigger. Use it for utility scripts that you run on demand, or as the data source of an [Information Panel](../tools/panel.md).

```
[Script]
my-tool = type=generic,script-path=my-tool.js
```

`generic` is also the default type: a [Script] line without a `type` parameter is treated as a generic script.

## Trigger

A generic script only runs when invoked by name:

* Surge iOS: long-press the script, or run it from the system Shortcuts app.
* Script editor: evaluate the script directly in the editor of either app.
* [HTTP API](../tools/http-api.md): `POST /v1/scripting/evaluate` evaluates the given script text.
* Information Panel: a `[Panel]` entry with `script-name=` runs the script to render the panel content.

## Input

There is no type-specific input. The [common globals](api.md) are available as usual (`$network`, `$environment`, `$script`, `$argument`, …), plus context globals describing how the script was launched:

| Field | Type | Description |
| --- | --- | --- |
| `$trigger` | String | How the script was launched: `editor` (script editor), `http-api` (HTTP API), `intent` (Shortcuts), `button` (panel tapped), or `auto-interval` (periodic panel refresh). |
| `$intent.parameter` | String | The parameter passed from the Shortcuts app. Only present when triggered by a Shortcut. |
| `$input` | Object | Panel context, only present when triggered by a panel: `{purpose: "panel", position, panelName}`. |

## Result

For a plain manual run, the result passed to `$done()` is ignored; a bare `$done()` is enough.

When the script backs an Information Panel, return the panel content:

```
$done({
    title: 'My Panel',        // required
    content: 'Hello, Surge',  // optional
});
```

The result object may contain `title` (required), `content`, `style`, `icon`, and `icon-color`. See [Information Panel](../tools/panel.md) for details.

## Example

```
// my-tool = type=generic,script-path=my-tool.js

$httpClient.get('https://api.ipify.org', function(error, response, data) {
  if (error) {
    console.log('Request failed: ' + error);
  } else {
    console.log('Current public IP: ' + data);
  }
  $done();
});
```
