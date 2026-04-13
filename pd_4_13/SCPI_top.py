import subprocess

def run_python_script(py_exe, script_path,user_input):
    try:
        subprocess.Popen([py_exe, script_path,user_input])
        # 关键：开启 stdout 和 stderr 重定向 → 输出到当前终端
        process = subprocess.run(
            [py_exe, script_path],
            input=user_input,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        #process.wait()  # 等待脚本执行完毕
        print(f"\n 脚本执行完成")
    except Exception as e:
        print(f"❌ 启动失败：{str(e)}")



PYTHON_PATH = r"D:\.project\python\1.0\venv\Scripts\python.exe"
TARGET_SCRIPT1 = r"D:\.project\python\1.0\SCPI_test\CHANnel1.py"
TARGET_SCRIPT2 = r"D:\.project\python\1.0\SCPI_test\CHANnel2.py"
TARGET_SCRIPT = None


def get_after_nth_char_then_colon(s, split_char, n):
    # 按字符分割
    parts = s.split(split_char)
    if len(parts) <= n:
        return ""
    # 第n个字符之后的部分
    sub = parts[n]
    # 取冒号后内容
    return sub.split(':', 1)[-1].strip()

def command():

    while True:
        user_input = input("请输入指令：").strip().lower()

        # 退出指令
        if user_input == "1":
            print("退出程序")
            break

        # 匹配通道指令（统一小写，所以判断小写）
        if "channel1" in user_input:
            TARGET_SCRIPT = TARGET_SCRIPT1
        elif "channel2" in user_input:
            TARGET_SCRIPT = TARGET_SCRIPT2
        else:
            print("❌ 无效指令！")
            continue  # 跳过执行脚本

        cmd_in=get_after_nth_char_then_colon(user_input,':',2)
        print(cmd_in)
        # 只有有效指令才执行
        if TARGET_SCRIPT:
            run_python_script(PYTHON_PATH, TARGET_SCRIPT,cmd_in)


if __name__ == "__main__":
    command()
    #:channel1:DISPlay
    #:channel1:COUPling DC 50
    #:channel1:SCALe 0.2
    #:channel1:OFFSet 2
    #:channel1:OFFSet_v 0.2
    #import re

# s = "温度：-5.5℃，涨幅：+3.2%"
# nums = re.findall(r'[+-]?\d+\.?\d*', s)
# print(nums)  # ['-5.5', '+3.2']

