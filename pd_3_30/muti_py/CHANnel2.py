import sys  # 必须导入


if len(sys.argv) > 1:
    # 第一个参数是脚本名
    # 第二个参数开始是你传的命令
    cmd = sys.argv[1]
    print(f"收到命令：{cmd}")

    # 你可以根据传过来的命令执行逻辑
    if cmd == "start":
        print("执行：启动通道1")
    elif cmd == "stop":
        print("执行：停止通道1")
else:
    print("未收到任何命令")