# JavaScript API 参考
Egern 脚本使用 `export default` 导出一个 async 函数，运行时会将 `ctx` 对象注入该函数。
    export default async function(ctx) {  
      // ...  
    }  
支持五种脚本类型：**Request** 、**Response** 、**Schedule** 、**Generic** 和 **Network** 。
* * *
## ctx​
### ctx.script​
脚本信息。
属性| 类型| 说明  
---|---|---  
`ctx.script.name`| `string`| 脚本名称  
### ctx.env​
`Object<string, string>` — 环境变量键值对。详见 环境变量。
    export default async function(ctx) {  
      const apiKey = ctx.env.API_KEY;  
      const apiUrl = ctx.env.API_URL;  
    }  
### ctx.app​
应用信息。
属性| 类型| 说明  
---|---|---  
`ctx.app.version`| `string`| 应用版本  
`ctx.app.language`| `string`| 系统语言  
### ctx.device​
设备网络环境信息。
属性| 类型| 说明  
---|---|---  
`ctx.device.cellular.carrier`| `string | null`| 蜂窝运营商  
`ctx.device.cellular.radio`| `string | null`| 蜂窝网络制式  
`ctx.device.wifi.ssid`| `string | null`| Wi-Fi 名称  
`ctx.device.wifi.bssid`| `string | null`| Wi-Fi BSSID  
`ctx.device.ipv4.address`| `string | null`| IPv4 地址  
`ctx.device.ipv4.gateway`| `string | null`| IPv4 网关  
`ctx.device.ipv4.interface`| `string | null`| 网络接口  
`ctx.device.ipv6.address`| `string | null`| IPv6 地址  
`ctx.device.ipv6.interface`| `string | null`| 网络接口  
`ctx.device.dnsServers`| `string[]`| DNS 服务器列表  
### ctx.cron​
`string | undefined` — 仅在 schedule 类型脚本中可用，值为 cron 表达式。
### ctx.widgetFamily​
`string | undefined` — 仅在 generic 类型脚本中可用，表示小组件尺寸系列。
可能的值：`systemSmall`、`systemMedium`、`systemLarge`、`systemExtraLarge`、`accessoryCircular`、`accessoryRectangular`、`accessoryInline`。
### ctx.request​
`Object | undefined` — 仅在 request/response 脚本中可用。
属性/方法| 类型| 说明  
---|---|---  
`method`| `string`| HTTP 方法  
`url`| `string`| 请求 URL  
`headers`| `Headers`| 请求头  
`body`| `ReadableStream | null`| 请求体流  
`json()`| `Promise<any>`| 解析为 JSON  
`text()`| `Promise<string>`| 解析为文本  
`arrayBuffer()`| `Promise<ArrayBuffer>`| 解析为 ArrayBuffer  
`blob()`| `Promise<Blob>`| 解析为 Blob  
`formData()`| `Promise<FormData>`| 解析为 FormData  
> 注意：body 只能消费一次（与 Fetch API 行为一致）。
### ctx.response​
`Object | undefined` — 仅在 response 脚本中可用。
属性/方法| 类型| 说明  
---|---|---  
`status`| `number`| 状态码  
`headers`| `Headers`| 响应头  
`body`| `ReadableStream | null`| 响应体流  
`json()`| `Promise<any>`| 解析为 JSON  
`text()`| `Promise<string>`| 解析为文本  
`arrayBuffer()`| `Promise<ArrayBuffer>`| 解析为 ArrayBuffer  
`blob()`| `Promise<Blob>`| 解析为 Blob  
`formData()`| `Promise<FormData>`| 解析为 FormData  
> 注意：body 只能消费一次（与 Fetch API 行为一致）。
### Headers 对象​
`ctx.request.headers`、`ctx.response.headers`、`ctx.http` 响应的 `headers` 均为 Headers 对象，支持**大小写无关** 的属性访问和以下方法：
方法| 返回值| 说明  
---|---|---  
`headers.get(name)`| `string | null`| 获取值（多值用 `, ` 合并）  
`headers.getAll(name)`| `string[]`| 获取所有值（始终返回数组）  
`headers.has(name)`| `boolean`| 是否存在  
`headers.set(name, value)`| `void`| 设置（替换已有值）  
`headers.append(name, value)`| `void`| 追加值  
`headers.delete(name)`| `void`| 删除  
所有方法的 `name` 参数均大小写无关。直接属性访问同样大小写无关，单值返回 `string`，多值返回 `string[]`：
    // 以下访问等价  
    headers['Content-Type']   // 'application/json'  
    headers['content-type']   // 'application/json'  
    // 多值 header  
    headers['set-cookie']                // ['session=abc', 'token=xyz']  
    headers.get('set-cookie')            // 'session=abc, token=xyz'  
    headers.getAll('set-cookie')         // ['session=abc', 'token=xyz']  
    // 修改  
    headers.set('X-Custom', 'value');  
    headers.append('X-Custom', 'value2');  
    headers.delete('X-Custom');  
    headers['X-New'] = 'value';  
    delete headers['X-New'];  
* * *
## ctx.http​
发送 HTTP 请求。所有方法返回 `Promise<Response>`。
### 方法​
    ctx.http.get(url, options?)  
    ctx.http.post(url, options?)  
    ctx.http.put(url, options?)  
    ctx.http.delete(url, options?)  
    ctx.http.head(url, options?)  
    ctx.http.options(url, options?)  
    ctx.http.patch(url, options?)  
### 参数​
  * `url` — `string`，请求 URL。
  * `options` — 可选对象：
字段| 类型| 说明  
---|---|---  
`headers`| `Headers | Object<string, string | string[]>`| 请求头（多值 header 为数组）  
`body`| `string | Uint8Array | Object | ReadableStream`| 请求体（Object 会自动 JSON 序列化）  
`timeout`| `number`| 超时时间（毫秒）  
`policy`| `string`| 代理策略  
`policyDescriptor`| `string`| 策略描述符  
`redirect`| `'follow' | 'manual' | 'error'`| 重定向策略（默认 `'follow'`）；`manual` 返回 3xx 响应，`error` 遇到重定向时抛异常  
`credentials`| `'omit' | 'include'`| 是否携带 Cookie（默认 `'include'`）  
`insecureTls`| `boolean`| 是否允许不安全的 TLS（默认 `false`）  
### Response 对象​
属性/方法| 类型| 说明  
---|---|---  
`status`| `number`| 状态码  
`headers`| `Headers`| 响应头  
`body`| `ReadableStream`| 响应体流  
`json()`| `Promise<any>`| 解析为 JSON  
`text()`| `Promise<string>`| 解析为文本  
`blob()`| `Promise<Blob>`| 解析为 Blob  
`arrayBuffer()`| `Promise<ArrayBuffer>`| 解析为 ArrayBuffer  
`formData()`| `Promise<FormData>`| 解析为 FormData  
> 注意：`body` 只能消费一次（与 Fetch API 行为一致）。
### 示例​
    const resp = await ctx.http.get('https://api.example.com/data');  
    const data = await resp.json();  
* * *
## ctx.storage​
持久化键值存储。
方法| 返回值| 说明  
---|---|---  
`ctx.storage.get(key)`| `string | null`| 读取值  
`ctx.storage.set(key, value)`| `void`| 写入值（value 为 string）  
`ctx.storage.getJSON(key)`| `any | null`| 读取值并 JSON 解析  
`ctx.storage.setJSON(key, value)`| `void`| JSON 序列化后写入  
`ctx.storage.delete(key)`| `void`| 删除键  
### 示例​
    ctx.storage.set('token', 'abc123');  
    const token = ctx.storage.get('token');  // 'abc123'  
    ctx.storage.delete('token');  
    // JSON 便捷方法  
    ctx.storage.setJSON('config', { theme: 'dark', lang: 'zh' });  
    const config = ctx.storage.getJSON('config');  // { theme: 'dark', lang: 'zh' }  
* * *
## ctx.notify(options)​
发送通知。
字段| 类型| 说明  
---|---|---  
`title`| `string`| 标题  
`subtitle`| `string`| 副标题（可选）  
`body`| `string`| 内容（可选）  
`sound`| `boolean`| 是否播放提示音（默认 `true`）  
`duration`| `number`| 通知展示时长，单位为秒（可选）  
`attachment`| `Object`| 通知附件（可选）  
`attachment.url`| `string`| 媒体 URL，自动下载作为附件（与 `base64` 二选一）  
`attachment.base64`| `string`| Base64 编码的媒体数据（与 `url` 二选一）  
`attachment.mimeType`| `string`| MIME 类型（可选，gif/png/jpg/pdf 可自动检测）  
`action`| `Object`| 点击通知时的行为（可选）  
`action.type`| `string`| `"openUrl"` 或 `"clipboard"`  
`action.url`| `string`| type 为 `"openUrl"` 时打开的 URL  
`action.text`| `string`| type 为 `"clipboard"` 时复制的文本  
### 示例​
    // 基本通知  
    ctx.notify({ title: 'Done', body: 'Task completed' });  
    // 带附件和点击行为  
    ctx.notify({  
      title: '截图已保存',  
      body: '点击查看详情',  
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
    // 使用 base64 附件 + 复制到剪贴板  
    ctx.notify({  
      title: '验证码',  
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
查询 IP 地址信息。
  * `ip` — `string`，IP 地址。
  * 返回 `Object | null`：
属性| 类型| 说明  
---|---|---  
`country`| `string`| 国家/地区代码  
`asn`| `number`| AS 号  
`organization`| `string`| 组织名称  
### 示例​
    const info = ctx.lookupIP('8.8.8.8');  
    // { country: 'US', asn: 15169, organization: 'GOOGLE' }  
* * *
## ctx.compress​
压缩/解压缩，输入输出均为 `Uint8Array`。所有方法返回 `Promise<Uint8Array | null>`。
方法| 说明  
---|---  
`ctx.compress.gzip(data)`| Gzip 压缩  
`ctx.compress.gunzip(data)`| Gzip 解压  
`ctx.compress.deflate(data)`| Deflate 压缩  
`ctx.compress.inflate(data)`| Deflate 解压  
`ctx.compress.brotli(data)`| Brotli 压缩  
`ctx.compress.unbrotli(data)`| Brotli 解压  
* * *
## ctx.ssh​
SSH 客户端，支持远程命令执行  和 SFTP 文件操作。
### ctx.ssh.connect(config)​
连接到 SSH 服务器，返回 `Promise<Session>`。
字段| 类型| 说明  
---|---|---  
`host`| `string`| 服务器地址  
`port`| `number`| 端口（默认 `22`）  
`username`| `string`| 用户名  
`password`| `string`| 密码（与 `privateKey` 二选一）  
`privateKey`| `string`| 私钥内容（与 `password` 二选一）  
`passphrase`| `string`| 私钥密码（可选）  
`timeout`| `number`| 连接超时（毫秒，默认 `10000`）  
### Session​
#### session.exec(command, options?)​
执行远程命令，返回 `Promise<ExecResult>`。
**options：**
字段| 类型| 说明  
---|---|---  
`stdin`| `string`| 标准输入（可选）  
`encoding`| `'binary'`| 设为 `'binary'` 时 stdout/stderr 返回 `Uint8Array`（可选）  
`env`| `Object<string, string>`| 环境变量（可选，需服务端 `AcceptEnv` 配置）  
**ExecResult：**
属性| 类型| 说明  
---|---|---  
`code`| `number`| 退出码  
`stdout`| `string | Uint8Array`| 标准输出  
`stderr`| `string | Uint8Array`| 标准错误  
#### session.sftp()​
初始化 SFTP 子系统，返回 `Promise<Sftp>`。每个 Session 只需调用一次。
#### session.close()​
断开 SSH 连接，返回 `Promise<void>`。
### Sftp​
SFTP 文件操作，API 风格对齐 Node.js `fs/promises`。
#### 文件读写​
方法| 返回值| 说明  
---|---|---  
`sftp.readFile(path, encoding?)`| `Promise<string | Uint8Array>`| 读取文件；`encoding` 为 `'utf8'` 时返回 `string`，否则返回 `Uint8Array`  
`sftp.writeFile(path, data, options?)`| `Promise<void>`| 写入文件（覆盖）；`data` 可为 `string`、`Uint8Array` 或 `Object`（自动 JSON 序列化）  
`sftp.appendFile(path, data, options?)`| `Promise<void>`| 追加写入；`data` 类型同上  
`readFile` 的 `encoding` 参数可为字符串 `'utf8'` 或对象 `{ encoding: 'utf8' }`。
`writeFile`/`appendFile` 的 `options`：
字段| 类型| 说明  
---|---|---  
`mode`| `number`| 文件权限（默认 `0o644`）  
#### 目录操作​
方法| 返回值| 说明  
---|---|---  
`sftp.readdir(path)`| `Promise<DirEntry[]>`| 列出目录内容  
`sftp.mkdir(path, options?)`| `Promise<void>`| 创建目录  
`sftp.rm(path, options?)`| `Promise<void>`| 删除文件或目录  
`mkdir` 的 `options`：
字段| 类型| 说明  
---|---|---  
`mode`| `number`| 目录权限（默认 `0o755`）  
`recursive`| `boolean`| 递归创建父目录（默认 `false`）  
`rm` 的 `options`：
字段| 类型| 说明  
---|---|---  
`recursive`| `boolean`| 递归删除目录及内容（默认 `false`）  
`force`| `boolean`| 忽略不存在的路径（默认 `false`）  
#### 文件信息​
方法| 返回值| 说明  
---|---|---  
`sftp.stat(path)`| `Promise<FileAttr>`| 获取文件属性（跟随符号链接）  
`sftp.lstat(path)`| `Promise<FileAttr>`| 获取文件属性（不跟随符号链接）  
`sftp.exists(path)`| `Promise<boolean>`| 检查路径是否存在  
`sftp.statfs(path)`| `Promise<StatFs>`| 获取文件系统信息  
**FileAttr：**
属性| 类型| 说明  
---|---|---  
`size`| `number`| 文件大小（字节）  
`uid`| `number`| 所有者 UID  
`gid`| `number`| 所有者 GID  
`mode`| `number`| 权限位  
`atime`| `Date`| 最后访问时间  
`mtime`| `Date`| 最后修改时间  
`isFile()`| `boolean`| 是否为普通文件  
`isDirectory()`| `boolean`| 是否为目录  
`isSymbolicLink()`| `boolean`| 是否为符号链接  
**DirEntry** 继承 FileAttr 的所有属性，并额外包含：
属性| 类型| 说明  
---|---|---  
`name`| `string`| 文件名  
**StatFs：**
属性| 类型| 说明  
---|---|---  
`bsize`| `number`| 块大小  
`frsize`| `number`| 片段大小  
`blocks`| `number`| 总块数  
`bfree`| `number`| 可用块数  
`bavail`| `number`| 非特权用户可用块数  
`files`| `number`| 总 inode 数  
`ffree`| `number`| 可用 inode 数  
`favail`| `number`| 非特权用户可用 inode 数  
`fsid`| `number`| 文件系统 ID  
`flag`| `number`| 挂载标志  
`namemax`| `number`| 最大文件名长度  
#### 权限与所有权​
方法| 返回值| 说明  
---|---|---  
`sftp.chmod(path, mode)`| `Promise<void>`| 修改权限（`mode` 为八进制数，如 `0o755`）  
`sftp.chown(path, uid, gid)`| `Promise<void>`| 修改所有者  
#### 链接与路径​
方法| 返回值| 说明  
---|---|---  
`sftp.rename(oldPath, newPath)`| `Promise<void>`| 重命名/移动  
`sftp.symlink(target, path)`| `Promise<void>`| 创建符号链接  
`sftp.readlink(path)`| `Promise<string>`| 读取符号链接目标  
`sftp.realpath(path)`| `Promise<string>`| 解析为绝对路径  
### 示例​
    // 执行远程命令  
    const session = await ctx.ssh.connect({  
      host: '192.168.1.100',  
      username: 'root',  
      privateKey: ctx.env.sshKey,  
    });  
    const result = await session.exec('uname -a');  
    ctx.notify({ title: 'Server', body: result.stdout.trim() });  
    await session.close();  
    // SFTP 文件操作  
    const session = await ctx.ssh.connect({  
      host: '192.168.1.100',  
      username: 'deploy',  
      password: ctx.env.sshPassword,  
    });  
    const sftp = await session.sftp();  
    // 上传配置  
    await sftp.writeFile('/etc/app/config.json', { port: 8080, debug: false });  
    // 读取日志  
    const log = await sftp.readFile('/var/log/app.log', 'utf8');  
    // 备份目录  
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
在 request 脚本中直接返回响应，不将请求发送到上游服务器。
  * `response` — 对象：
字段| 类型| 说明  
---|---|---  
`status`| `number`| 状态码  
`headers`| `Headers | Object<string, string | string[]>`| 响应头（可选，多值 header 为数组）  
`body`| `string | Uint8Array | Object | ReadableStream`| 响应体（可选，Object 会自动 JSON 序列化）  
    return ctx.respond({ status: 200, headers: { 'Content-Type': 'text/plain' }, body: 'blocked' });  
* * *
## ctx.abort()​
中止当前请求或响应，用于 request/response 脚本。
    return ctx.abort();  
* * *
## 返回值​
函数的返回值决定脚本行为，不同脚本类型返回不同结构。
### Request 脚本​
执行于 HTTP 请求发送之前，可修改请求、直接返回响应或中止请求。
返回对象修改请求，所有字段均可选，省略的字段保持原值不变。
字段| 类型| 说明  
---|---|---  
`method`| `string`| HTTP 方法  
`url`| `string`| 请求 URL  
`headers`| `Headers | Object<string, string | string[]>`| 请求头（多值 header 为数组）  
`body`| `string | Uint8Array | Object | ReadableStream`| 请求体（Object 会自动 JSON 序列化）  
也可使用 `ctx.respond()` 直接返回响应、`ctx.abort()` 中止请求，或不返回以透传。
    // 修改请求  
    return { url: 'https://...', headers: { ... }, body: '...' };  
    // 透传 body 流  
    return { url: 'https://...', body: ctx.request.body };  
    // 直接返回响应  
    return ctx.respond({ status: 200, headers: {}, body: 'blocked' });  
    // 中止请求  
    return ctx.abort();  
### Response 脚本​
执行于 HTTP 响应返回给客户端之前，可修改响应或中止连接。
返回对象修改响应，所有字段均可选，省略的字段保持原值不变。
字段| 类型| 说明  
---|---|---  
`status`| `number`| 状态码  
`headers`| `Headers | Object<string, string | string[]>`| 响应头（多值 header 为数组）  
`body`| `string | Uint8Array | Object | ReadableStream`| 响应体（Object 会自动 JSON 序列化）  
也可使用 `ctx.abort()` 中止，或不返回以透传。
    return { status: 200, headers: { ... }, body: '...' };  
    return ctx.abort();  
### Generic 脚本​
返回 Widget DSL JSON 对象，Egern 将其渲染为 iOS 小组件。根节点必须为 `type: "widget"`。
    return {  
      type: 'widget',  
      children: [  
        { type: 'text', text: 'Status: OK', font: { size: 'headline', weight: 'semibold' }, textColor: '#FFFFFF' }  
      ],  
      backgroundColor: '#2D6A4F',  
      padding: 16,  
    };  
### Schedule / Network 脚本​
无需返回值。
* * *
## 完整示例​
### Request — 重写 URL​
    export default async function(ctx) {  
      return { url: ctx.request.url.replace('http://', 'https://') };  
    }  
### Response — 修改 JSON 响应体​
    export default async function(ctx) {  
      const data = await ctx.response.json();  
      data.ads = [];  
      return { body: data };  
    }  
### Request — 拦截广告​
    export default async function(ctx) {  
      if (ctx.request.url.includes('/ads')) return ctx.abort();  
    }  
### Schedule — 定时任务​
    export default async function(ctx) {  
      const resp = await ctx.http.get('https://api.example.com/data');  
      const data = await resp.json();  
      ctx.storage.set('latest', JSON.stringify(data));  
      ctx.notify({ title: 'Updated', body: `${data.length} items` });  
    }  
### Generic — 小组件​
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
### Schedule — SSH 服务器监控​
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