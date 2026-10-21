#!/bin/sh
# 启动 Mercury 网页版桥接服务（供 Minis 自定义 provider 使用）
# 用法：sh start_bridge.sh
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
pkill -f bridge_server.py 2>/dev/null || true
sleep 1
nohup python3 -u "$SCRIPT_DIR/bridge_server.py" 18080 > /tmp/mercury_bridge.log 2>&1 &
sleep 2
echo "bridge started on :18080 (log: /tmp/mercury_bridge.log)"
curl -s http://127.0.0.1:18080/ || echo " (等待就绪...)"
echo