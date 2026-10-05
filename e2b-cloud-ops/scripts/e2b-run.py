#!/usr/bin/env python3
"""E2B 云沙箱派单工具 —— Minis 全自动调度免费云服务器

用法:
  python3 e2b-run.py --cmd "shell 命令"           # 执行任意命令
  python3 e2b-run.py --py "python 代码"           # 在云端执行 Python 代码
  python3 e2b-run.py --file 本地.py --cmd "python3 /home/user/本地.py"  # 上传脚本后执行
  python3 e2b-run.py --keep --cmd "..."          # 任务后保留沙箱（打印 sandbox_id）
  python3 e2b-run.py --kill <sandbox_id>         # 销毁指定沙箱
  python3 e2b-run.py --cmd "..." --kill-after N  # N 秒后自动销毁

依赖: pip install e2b，环境变量 E2B_API_KEY
"""
import argparse
import os
import sys
import time

from e2b import Sandbox


def main():
    p = argparse.ArgumentParser(description="E2B 云沙箱派单")
    p.add_argument("--cmd", help="在沙箱中执行的 shell 命令")
    p.add_argument("--py", help="在沙箱中执行的 Python 代码")
    p.add_argument("--file", action="append", default=[], help="上传的本地文件（可多次）")
    p.add_argument("--keep", action="store_true", help="任务后保持沙箱存活")
    p.add_argument("--kill", metavar="ID", help="销毁指定沙箱")
    p.add_argument("--max-time", type=int, default=300, help="命令超时秒数（默认300）")
    args = p.parse_args()

    if args.kill:
        try:
            sbx = Sandbox.connect(args.kill)
            sbx.kill()
            print("已销毁沙箱:", args.kill)
        except Exception as e:
            print("销毁失败:", e)
        return

    cmd = args.cmd or ""
    sbx = Sandbox.create()
    print("沙箱已创建:", sbx.sandbox_id)
    try:
        for fp in args.file:
            if not os.path.exists(fp):
                print("本地文件不存在:", fp)
                continue
            name = os.path.basename(fp)
            with open(fp, "rb") as f:
                sbx.files.write("/home/user/" + name, f.read())
            print("已上传:", name)

        if args.py:
            sbx.files.write("/home/user/task.py", args.py)
            cmd = "cd /home/user && python3 task.py"

        if cmd:
            print(">>> 执行命令:", cmd)
            res = sbx.commands.run(cmd, timeout=args.max_time * 1000)
            if res.stdout:
                print("--- 标准输出 ---")
                print(res.stdout)
            if res.stderr:
                print("--- 错误输出 ---")
                print(res.stderr)
            print("--- 退出码:", res.exit_code, "---")

    finally:
        if not args.keep:
            sbx.kill()
            print("沙箱已销毁（不产生费用）")
        else:
            print("沙箱保持运行:", sbx.sandbox_id, "（记得用 --kill 销毁）")


if __name__ == "__main__":
    main()