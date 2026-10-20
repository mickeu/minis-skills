#!/bin/sh
# railway_api.sh - Railway GraphQL API 辅助脚本
# 用法:
#   RAILWAY_TOKEN=<token> ./railway_api.sh '<graphql query or mutation>'
# 示例:
#   RAILWAY_TOKEN=$RAILWAY_TOKEN ./railway_api.sh 'query { projects { edges { node { id name } } } }'
#
# 端点: https://backboard.railway.app/graphql/v2
# 认证: Authorization: Bearer <token>
# Token 从环境变量 RAILWAY_TOKEN 读取，绝不硬编码。

set -e

ENDPOINT="${RAILWAY_API_ENDPOINT:-https://backboard.railway.app/graphql/v2}"

if [ -z "$RAILWAY_TOKEN" ]; then
  echo "错误: 环境变量 RAILWAY_TOKEN 未设置。" >&2
  echo "请先设置: export RAILWAY_TOKEN=<你的token>" >&2
  exit 1
fi

if [ $# -lt 1 ]; then
  echo "用法: $0 '<graphql query or mutation>'" >&2
  exit 1
fi

QUERY="$1"

# 构造 JSON payload（用 python 避免转义问题）
PAYLOAD=$(python3 -c "import json,sys; print(json.dumps({'query': sys.argv[1]}))" "$QUERY")

curl -s -m 30 -X POST "$ENDPOINT" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD"
echo