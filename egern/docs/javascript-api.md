# JavaScript API Reference
Egern scripts use `export default` to export an async function. The `ctx` object is injected at runtime.
    export default async function(ctx) {  
      // ...  
    }  
Five script types are supported: **Request** , **Response** , **Schedule** , **Generic** , and **Network**.
* * *
## ctx​
### ctx.script​
Script information.
Property| Type| Description  
---|---|---  
`ctx.script.name`| `string`| Script name  
### ctx.env​
`Object<string, string>` — Environment variable key-value pairs. See Environment Variables for details.
    export default async function(ctx) {  
      const apiKey = ctx.env.API_KEY;  
      const apiUrl = ctx.env.API_URL;  
    }  
### ctx.app​
Application information.
Property| Type| Description  
---|---|---  
`ctx.app.version`| `string`| App version  
`ctx.app.language`| `string`| System language  
### ctx.device​
Device network environment information.
Property| Type| Description  
---|---|---  
`ctx.device.cellular.carrier`| `string | null`| Cellular carrier  
`ctx.device.cellular.radio`| `string | null`| Cellular radio technology  
`ctx.device.wifi.ssid`| `string | null`| Wi-Fi name  
`ctx.device.wifi.bssid`| `string | null`| Wi-Fi BSSID  
`ctx.device.ipv4.address`| `string | null`| IPv4 address  
`ctx.device.ipv4.gateway`| `string | null`| IPv4 gateway  
`ctx.device.ipv4.interface`| `string | null`| Network interface  
`ctx.device.ipv6.address`| `string | null`| IPv6 address  
`ctx.device.ipv6.interface`| `string | null`| Network interface  
`ctx.device.dnsServers`| `string[]`| DNS server list  
### ctx.cron​
`string | undefined` — Only available in schedule scripts. The cron expression.
### ctx.widgetFamily​
`string | undefined` — Only available in generic scripts. The widget size family.
Possible values: `systemSmall`, `systemMedium`, `systemLarge`, `systemExtraLarge`, `accessoryCircular`, `accessoryRectangular`, `accessoryInline`.
### ctx.request​
`Object | undefined` — Only available in request/response scripts.
Property/Method| Type| Description  
---|---|---  
`method`| `string`| HTTP method  
`url`| `string`| Request URL  
`headers`| `Headers`| Request headers  
`body`| `ReadableStream | null`| Request body stream  
`json()`| `Promise<any>`| Parse as JSON  
`text()`| `Promise<string>`| Parse as text  
`arrayBuffer()`| `Promise<ArrayBuffer>`| Parse as ArrayBuffer  
`blob()`| `Promise<Blob>`| Parse as Blob  
`formData()`| `Promise<FormData>`| Parse as FormData  
> Note: The body can only be consumed once (consistent with Fetch API behavior).
### ctx.response​
`Object | undefined` — Only available in response scripts.
Property/Method| Type| Description  
---|---|---  
`status`| `number`| Status code  
`headers`| `Headers`| Response headers  
`body`| `ReadableStream | null`| Response body stream  
`json()`| `Promise<any>`| Parse as JSON  
`text()`| `Promise<string>`| Parse as text  
`arrayBuffer()`| `Promise<ArrayBuffer>`| Parse as ArrayBuffer  
`blob()`| `Promise<Blob>`| Parse as Blob  
`formData()`| `Promise<FormData>`| Parse as FormData  
> Note: The body can only be consumed once (consistent with Fetch API behavior).
### Headers Object​
`ctx.request.headers`, `ctx.response.headers`, and `ctx.http` response `headers` are all Headers objects. They support **case-insensitive** property access and the following methods:
Method| Return| Description  
---|---|---  
`headers.get(name)`| `string | null`| Get value (multiple values joined with `, `)  
`headers.getAll(name)`| `string[]`| Get all values (always returns array)  
`headers.has(name)`| `boolean`| Check existence  
`headers.set(name, value)`| `void`| Set (replaces existing)  
`headers.append(name, value)`| `void`| Append value  
`headers.delete(name)`| `void`| Delete  
All method `name` parameters are case-insensitive. Direct property access is also case-insensitive, returning `string` for single values and `string[]` for multiple values:
    // These are equivalent  
    headers['Content-Type']   // 'application/json'  
    headers['content-type']   // 'application/json'  
    // Multi-value header  
    headers['set-cookie']                // ['session=abc', 'token=xyz']  
    headers.get('set-cookie')            // 'session=abc, token=xyz'  
    headers.getAll('set-cookie')         // ['session=abc', 'token=xyz']  
    // Modification  
    headers.set('X-Custom', 'value');  
    headers.append('X-Custom', 'value2');  
    headers.delete('X-Custom');  
    headers['X-New'] = 'value';  
    delete headers['X-New'];  
* * *
## ctx.http​
Send HTTP requests. All methods return `Promise<Response>`.
### Methods​
    ctx.http.get(url, options?)  
    ctx.http.post(url, options?)  
    ctx.http.put(url, options?)  
    ctx.http.delete(url, options?)  
    ctx.http.head(url, options?)  
    ctx.http.options(url, options?)  
    ctx.http.patch(url, options?)  
### Parameters​
  * `url` — `string`, the request URL.
  * `options` — Optional object:
Field| Type| Description  
---|---|---  
`headers`| `Headers | Object<string, string | string[]>`| Request headers (multi-value headers as arrays)  
`body`| `string | Uint8Array | Object | ReadableStream`| Request body (Object is auto-serialized to JSON)  
`timeout`| `number`| Timeout in milliseconds  
`policy`| `string`| Proxy policy  
`policyDescriptor`| `string`| Policy descriptor  
`redirect`| `'follow' | 'manual' | 'error'`| Redirect policy (default `'follow'`); `manual` returns 3xx response, `error` throws on redirect  
`credentials`| `'omit' | 'include'`| Whether to include cookies (default `'include'`)  
`insecureTls`| `boolean`| Allow insecure TLS (default `false`)  
### Response Object​
Property/Method| Type| Description  
---|---|---  
`status`| `number`| Status code  
`headers`| `Headers`| Response headers  
`body`| `ReadableStream`| Response body stream  
`json()`| `Promise<any>`| Parse as JSON  
`text()`| `Promise<string>`| Parse as text  
`blob()`| `Promise<Blob>`| Parse as Blob  
`arrayBuffer()`| `Promise<ArrayBuffer>`| Parse as ArrayBuffer  
`formData()`| `Promise<FormData>`| Parse as FormData  
> Note: The `body` can only be consumed once (consistent with Fetch API behavior).
### Example​
    const resp = await ctx.http.get('https://api.example.com/data');  
    const data = await resp.json();  
* * *
## ctx.storage​
Persistent key-value storage.
Method| Return| Description  
---|---|---  
`ctx.storage.get(key)`| `string | null`| Read value  
`ctx.storage.set(key, value)`| `void`| Write value (value is string)  
`ctx.storage.getJSON(key)`| `any | null`| Read and JSON parse  
`ctx.storage.setJSON(key, value)`| `void`| JSON serialize and write  
`ctx.storage.delete(key)`| `void`| Delete key  
### Example​
    ctx.storage.set('token', 'abc123');  
    const token = ctx.storage.get('token');  // 'abc123'  
    ctx.storage.delete('token');  
    // JSON convenience methods  
    ctx.storage.setJSON('config', { theme: 'dark', lang: 'zh' });  
    const config = ctx.storage.getJSON('config');  // { theme: 'dark', lang: 'zh' }  
* * *
## ctx.notify(options)​
Send a notification.
Field| Type| Description  
---|---|---  
`title`| `string`| Title  
`subtitle`| `string`| Subtitle (optional)  
`body`| `string`| Content (optional)  
`sound`| `boolean`| Play alert sound (default `true`)  
`duration`| `number`| Display duration in seconds (optional)  
`attachment`| `Object`| Notification attachment (optional)  
`attachment.url`| `string`| Media URL, auto-downloaded as attachment (mutually exclusive with `base64`)  
`attachment.base64`| `string`| Base64-encoded media data (mutually exclusive with `url`)  
`attachment.mimeType`| `string`| MIME type (optional, gif/png/jpg/pdf auto-detected)  
`action`| `Object`| Tap action (optional)  
`action.type`| `string`| `"openUrl"` or `"clipboard"`  
`action.url`| `string`| URL to open when type is `"openUrl"`  
`action.text`| `string`| Text to copy when type is `"clipboard"`  
### Example​
    // Basic notification  
    ctx.notify({ title: 'Done', body: 'Task completed' });  
    // With attachment and tap action  
    ctx.notify({  
      title: 'Screenshot saved',  
      body: 'Tap for details',  
      sound: true,  
      duration: 5,  
      attachment: {  
        url: 'https://example.com/image.png',  
        mimeType: 'image/png',  
      },  
      action: {  
        type: 'openUrl',  
        url: 'https://example.com/details',  
      },  
    });  
    // Base64 attachment + copy to clipboard  
    ctx.notify({  
      title: 'Verification code',  
      body: '1234',  
      attachment: {  
        base64: 'iVBORw0KGgo...',  
        mimeType: 'image/png',  
      },  
      action: {  
        type: 'clipboard',  
        text: '1234',  
      },  
    });  
* * *
## ctx.lookupIP(ip)​
Look up IP address information.
  * `ip` — `string`, the IP address.
  * Returns `Object | null`:
Property| Type| Description  
---|---|---  
`country`| `string`| Country/region code  
`asn`| `number`| AS number  
`organization`| `string`| Organization name  
### Example​
    const info = ctx.lookupIP('8.8.8.8');  
    // { country: 'US', asn: 15169, organization: 'GOOGLE' }  
* * *
## ctx.compress​
Compression/decompression. Input and output are `Uint8Array`. All methods return `Promise<Uint8Array | null>`.
Method| Description  
---|---  
`ctx.compress.gzip(data)`| Gzip compress  
`ctx.compress.gunzip(data)`| Gzip decompress  
`ctx.compress.deflate(data)`| Deflate compress  
`ctx.compress.inflate(data)`| Deflate decompress  
`ctx.compress.brotli(data)`| Brotli compress  
`ctx.compress.unbrotli(data)`| Brotli decompress  
* * *
## ctx.ssh​
SSH client with remote command execution and SFTP file operations.
### ctx.ssh.connect(config)​
Connect to an SSH server. Returns `Promise<Session>`.
Field| Type| Description  
---|---|---  
`host`| `string`| Server address  
`port`| `number`| Port (default `22`)  
`username`| `string`| Username  
`password`| `string`| Password (mutually exclusive with `privateKey`)  
`privateKey`| `string`| Private key content (mutually exclusive with `password`)  
`passphrase`| `string`| Private key passphrase (optional)  
`timeout`| `number`| Connection timeout in milliseconds (default `10000`)  
### Session​
#### session.exec(command, options?)​
Execute a remote command. Returns `Promise<ExecResult>`.
**options:**
Field| Type| Description  
---|---|---  
`stdin`| `string`| Standard input (optional)  
`encoding`| `'binary'`| When set to `'binary'`, stdout/stderr return `Uint8Array` (optional)  
`env`| `Object<string, string>`| Environment variables (optional, requires server `AcceptEnv` configuration)  
**ExecResult:**
Property| Type| Description  
---|---|---  
`code`| `number`| Exit code  
`stdout`| `string | Uint8Array`| Standard output  
`stderr`| `string | Uint8Array`| Standard error  
#### session.sftp()​
Initialize the SFTP subsystem. Returns `Promise<Sftp>`. Only needs to be called once per Session.
#### session.close()​
Disconnect the SSH connection. Returns `Promise<void>`.
### Sftp​
SFTP file operations. API style aligned with Node.js `fs/promises`.
#### File Read/Write​
Method| Return| Description  
---|---|---  
`sftp.readFile(path, encoding?)`| `Promise<string | Uint8Array>`| Read file; returns `string` when `encoding` is `'utf8'`, otherwise `Uint8Array`  
`sftp.writeFile(path, data, options?)`| `Promise<void>`| Write file (overwrite); `data` can be `string`, `Uint8Array`, or `Object` (auto JSON serialized)  
`sftp.appendFile(path, data, options?)`| `Promise<void>`| Append to file; same `data` types as above  
The `encoding` parameter for `readFile` can be the string `'utf8'` or an object `{ encoding: 'utf8' }`.
`writeFile`/`appendFile` `options`:
Field| Type| Description  
---|---|---  
`mode`| `number`| File permissions (default `0o644`)  
#### Directory Operations​
Method| Return| Description  
---|---|---  
`sftp.readdir(path)`| `Promise<DirEntry[]>`| List directory contents  
`sftp.mkdir(path, options?)`| `Promise<void>`| Create directory  
`sftp.rm(path, options?)`| `Promise<void>`| Remove file or directory  
`mkdir` `options`:
Field| Type| Description  
---|---|---  
`mode`| `number`| Directory permissions (default `0o755`)  
`recursive`| `boolean`| Recursively create parent directories (default `false`)  
`rm` `options`:
Field| Type| Description  
---|---|---  
`recursive`| `boolean`| Recursively remove directory and contents (default `false`)  
`force`| `boolean`| Ignore nonexistent paths (default `false`)  
#### File Information​
Method| Return| Description  
---|---|---  
`sftp.stat(path)`| `Promise<FileAttr>`| Get file attributes (follows symlinks)  
`sftp.lstat(path)`| `Promise<FileAttr>`| Get file attributes (does not follow symlinks)  
`sftp.exists(path)`| `Promise<boolean>`| Check if path exists  
`sftp.statfs(path)`| `Promise<StatFs>`| Get filesystem information  
**FileAttr:**
Property| Type| Description  
---|---|---  
`size`| `number`| File size in bytes  
`uid`| `number`| Owner UID  
`gid`| `number`| Owner GID  
`mode`| `number`| Permission bits  
`atime`| `Date`| Last access time  
`mtime`| `Date`| Last modification time  
`isFile()`| `boolean`| Whether it is a regular file  
`isDirectory()`| `boolean`| Whether it is a directory  
`isSymbolicLink()`| `boolean`| Whether it is a symbolic link  
**DirEntry** inherits all FileAttr properties, plus:
Property| Type| Description  
---|---|---  
`name`| `string`| File name  
**StatFs:**
Property| Type| Description  
---|---|---  
`bsize`| `number`| Block size  
`frsize`| `number`| Fragment size  
`blocks`| `number`| Total blocks  
`bfree`| `number`| Free blocks  
`bavail`| `number`| Free blocks for unprivileged users  
`files`| `number`| Total inodes  
`ffree`| `number`| Free inodes  
`favail`| `number`| Free inodes for unprivileged users  
`fsid`| `number`| Filesystem ID  
`flag`| `number`| Mount flags  
`namemax`| `number`| Maximum filename length  
#### Permissions and Ownership​
Method| Return| Description  
---|---|---  
`sftp.chmod(path, mode)`| `Promise<void>`| Change permissions (`mode` is octal, e.g. `0o755`)  
`sftp.chown(path, uid, gid)`| `Promise<void>`| Change owner  
#### Links and Paths​
Method| Return| Description  
---|---|---  
`sftp.rename(oldPath, newPath)`| `Promise<void>`| Rename/move  
`sftp.symlink(target, path)`| `Promise<void>`| Create symbolic link  
`sftp.readlink(path)`| `Promise<string>`| Read symbolic link target  
`sftp.realpath(path)`| `Promise<string>`| Resolve to absolute path  
### Examples​
    // Execute remote command  
    const session = await ctx.ssh.connect({  
      host: '192.168.1.100',  
      username: 'root',  
      privateKey: ctx.env.sshKey,  
    });  
    const result = await session.exec('uname -a');  
    ctx.notify({ title: 'Server', body: result.stdout.trim() });  
    await session.close();  
    // SFTP file operations  
    const session = await ctx.ssh.connect({  
      host: '192.168.1.100',  
      username: 'deploy',  
      password: ctx.env.sshPassword,  
    });  
    const sftp = await session.sftp();  
    // Upload config  
    await sftp.writeFile('/etc/app/config.json', { port: 8080, debug: false });  
    // Read log  
    const log = await sftp.readFile('/var/log/app.log', 'utf8');  
    // Backup directory  
    const files = await sftp.readdir('/etc/app');  
    for (const f of files) {  
      if (f.isFile()) {  
        const data = await sftp.readFile(`/etc/app/${f.name}`);  
        await sftp.writeFile(`/backup/app/${f.name}`, data);  
      }  
    }  
    await session.close();  
* * *
## ctx.respond(response)​
In request scripts, return a response directly without sending the request to the upstream server.
  * `response` — Object:
Field| Type| Description  
---|---|---  
`status`| `number`| Status code  
`headers`| `Headers | Object<string, string | string[]>`| Response headers (optional, multi-value as arrays)  
`body`| `string | Uint8Array | Object | ReadableStream`| Response body (optional, Object is auto-serialized to JSON)  
    return ctx.respond({ status: 200, headers: { 'Content-Type': 'text/plain' }, body: 'blocked' });  
* * *
## ctx.abort()​
Abort the current request or response. Used in request/response scripts.
    return ctx.abort();  
* * *
## Return Values​
The function's return value determines script behavior. Different script types return different structures.
### Request Script​
Executes before an HTTP request is sent. Can modify the request, return a response directly, or abort.
Return an object to modify the request. All fields are optional; omitted fields remain unchanged.
Field| Type| Description  
---|---|---  
`method`| `string`| HTTP method  
`url`| `string`| Request URL  
`headers`| `Headers | Object<string, string | string[]>`| Request headers (multi-value as arrays)  
`body`| `string | Uint8Array | Object | ReadableStream`| Request body (Object is auto-serialized to JSON)  
You can also use `ctx.respond()` to return a response directly, `ctx.abort()` to abort, or return nothing to pass through.
    // Modify request  
    return { url: 'https://...', headers: { ... }, body: '...' };  
    // Pass through body stream  
    return { url: 'https://...', body: ctx.request.body };  
    // Return response directly  
    return ctx.respond({ status: 200, headers: {}, body: 'blocked' });  
    // Abort request  
    return ctx.abort();  
### Response Script​
Executes before an HTTP response is returned to the client. Can modify the response or abort.
Return an object to modify the response. All fields are optional; omitted fields remain unchanged.
Field| Type| Description  
---|---|---  
`status`| `number`| Status code  
`headers`| `Headers | Object<string, string | string[]>`| Response headers (multi-value as arrays)  
`body`| `string | Uint8Array | Object | ReadableStream`| Response body (Object is auto-serialized to JSON)  
You can also use `ctx.abort()` to abort, or return nothing to pass through.
    return { status: 200, headers: { ... }, body: '...' };  
    return ctx.abort();  
### Generic Script​
Return a Widget DSL JSON object. Egern renders it as an iOS widget. The root node must have `type: "widget"`.
    return {  
      type: 'widget',  
      children: [  
        { type: 'text', text: 'Status: OK', font: { size: 'headline', weight: 'semibold' }, textColor: '#FFFFFF' }  
      ],  
      backgroundColor: '#2D6A4F',  
      padding: 16,  
    };  
### Schedule / Network Script​
No return value needed.
* * *
## Full Examples​
### Request — URL Rewrite​
    export default async function(ctx) {  
      return { url: ctx.request.url.replace('http://', 'https://') };  
    }  
### Response — Modify JSON Body​
    export default async function(ctx) {  
      const data = await ctx.response.json();  
      data.ads = [];  
      return { body: data };  
    }  
### Request — Block Ads​
    export default async function(ctx) {  
      if (ctx.request.url.includes('/ads')) return ctx.abort();  
    }  
### Schedule — Scheduled Task​
    export default async function(ctx) {  
      const resp = await ctx.http.get('https://api.example.com/data');  
      const data = await resp.json();  
      ctx.storage.set('latest', JSON.stringify(data));  
      ctx.notify({ title: 'Updated', body: `${data.length} items` });  
    }  
### Generic — Widget​
    export default async function(ctx) {  
      const resp = await ctx.http.get('https://api.example.com/status');  
      const status = await resp.text();  
      return {  
        type: 'widget',  
        children: [  
          { type: 'text', text: 'Server Status', font: { size: 'headline', weight: 'bold' }, textColor: '#FFFFFF' },  
          { type: 'text', text: status, font: { size: 'body' }, textColor: '#FFFFFFCC' },  
        ],  
        backgroundColor: '#1A1A2E',  
        padding: 16,  
        gap: 8,  
      };  
    }  
### Schedule — SSH Server Monitoring​
    export default async function(ctx) {  
      const session = await ctx.ssh.connect({  
        host: ctx.env.host,  
        username: ctx.env.user,  
        privateKey: ctx.env.key,  
      });  
      const { stdout: uptime } = await session.exec('uptime -p');  
      const { stdout: disk } = await session.exec('df -h / | tail -1');  
      await session.close();  
      ctx.notify({  
        title: 'Server Status',  
        body: `${uptime.trim()}\nDisk: ${disk.trim()}`,  
      });  
    }