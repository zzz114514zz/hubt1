import sys
import pyautogui
import time
import pygetwindow as gw

# 延迟设置
pyautogui.PAUSE = 0.1

# ====================== 配置区域 ======================
WINDOW_TITLE = "数字存储示波器"  # #"USB示波器：ES7336G2  编号：2108"
# =====================================================

def init():
    """初始化：获取窗口坐标，返回 (win_left, win_top)"""
    print("\n执行初始化...")

    # 1. 找到目标窗口
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    if not windows:
        print(f"错误：未找到标题为 '{WINDOW_TITLE}' 的窗口！")
        return None, None

    window = windows[0]

    # 激活窗口
    if not window.isActive:
        window.activate()
        time.sleep(1)

    # 2. 获取窗口左上角坐标
    win_left = window.left
    win_top = window.top
    print(f"✅ 窗口位置：左上角 ({win_left}, {win_top})")
    print(f"✅ 窗口尺寸：{window.width} x {window.height}")

    return win_left, win_top


# ====================== 【1】命令函数（统一带 win_left, win_top 参数） ======================
def func_run(win_left, win_top):
    """主运行函数（自动接收窗口坐标）"""
    pyautogui.click(win_left + 10, win_top + 10)
    time.sleep(1)

    pyautogui.click(win_left + 1591 - 510, win_top + 257 - 195)
    pyautogui.click(win_left + 1591 - 510, win_top + 257 - 195)
    time.sleep(0.1)
    print("操作完成！")


def func_auto(win_left, win_top):
    pyautogui.click(win_left + 10, win_top + 10)
    time.sleep(1)

    pyautogui.hotkey('F3')
    print("操作完成！")


# def func_COUPling1(win_left, win_top):
#     #:CHANnel<n>:COUPling
#
#
# def func_restart(win_left, win_top):
#     """重启功能"""
#     print("\n🔄 执行：重启服务")
#     print("服务重启成功")


# ====================== 【2】命令映射 ======================
COMMAND_MAP = {
    ":run": func_run,
    ":auto": func_auto,
    # "demo": func_COUPling1,
    # "restart": func_restart
}
# ==========================================================


def run_command(func, win_left, win_top):
    """统一执行函数：自动传递窗口参数"""
    # 校验参数
    if win_left is None or win_top is None:
        print("❌ 窗口初始化失败，无法执行命令！")
        return

    try:
        func(win_left, win_top)  # 统一传递参数
        print("\n✅ 命令执行完成！")
    except Exception as e:
        print(f"\n❌ 命令执行失败：{str(e)}")


def watch_command():
    """命令监听主程序"""
    print("=== 命令监听已启动 ===")
    print(f"可用命令：{', '.join(COMMAND_MAP.keys())}")
    print("输入 exit 退出程序\n")

    # 【关键】先初始化，获取窗口坐标
    win_left, win_top = init()

    # 循环监听指令
    while True:
        user_input = input("请输入指令：").strip().lower()

        # 退出指令
        if user_input == "exit":
            print("👋 退出程序")
            sys.exit()

        # 匹配并执行命令
        if user_input in COMMAND_MAP:
            run_command(COMMAND_MAP[user_input], win_left, win_top)
        else:
            print(f"❌ 无效指令！可用：{', '.join(COMMAND_MAP.keys())}")


if __name__ == "__main__":
    watch_command()












