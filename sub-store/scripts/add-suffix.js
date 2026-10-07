/**
 * Sub-Store 脚本：给订阅内所有节点名追加后缀
 *
 * 用途：两个机场订阅节点同名冲突时，给其中一个机场的节点加后缀区分
 *
 * 使用：订阅编辑页 → 节点操作 → 脚本操作 → 粘贴本脚本
 * 参数（编辑页「参数」字段，或远程链接 #suffix=xxx）：
 *   suffix:    要追加的后缀，默认 "A机场"
 *   sep:       节点名与后缀之间的分隔符，默认空格
 *   overwrite: true=强制追加（即使节点名已包含后缀），默认 false 自动跳过
 *
 * 官方文档：https://sub-store-org.github.io/doc/script/examples.html
 */
function operator(proxies) {
  const { suffix = 'A机场', sep = ' ', overwrite = 'false' } = $arguments || {};
  return proxies.map(p => {
    if (!p.name) return p;
    if (overwrite !== 'true' && p.name.includes(suffix)) return p;
    p.name = `${p.name}${sep}${suffix}`;
    return p;
  });
}