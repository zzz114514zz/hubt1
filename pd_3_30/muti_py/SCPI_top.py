import subprocess
import sys

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
def command():

    while True:
        user_input = input("请输入指令：").strip().lower()

        # 退出指令
        if user_input == "exit":
            print("退出程序")
            break

        # 匹配通道指令（统一小写，所以判断小写）
        if "channel1" in user_input:
            TARGET_SCRIPT = TARGET_SCRIPT1
        elif "channel2" in user_input:
            TARGET_SCRIPT = TARGET_SCRIPT2
        else:
            print("❌ 无效指令！支持：channel1 / channel2 / exit")
            continue  # 跳过执行脚本

        # 只有有效指令才执行
        if TARGET_SCRIPT:
            run_python_script(PYTHON_PATH, TARGET_SCRIPT,user_input)


if __name__ == "__main__":
    command()#channel1:COUPling DC 50
