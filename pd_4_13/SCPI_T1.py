import sys
import pyautogui
import time
import pygetwindow as gw
from datetime import datetime
import win32gui
import win32con

# 延迟设置
pyautogui.PAUSE = 0.1

# ====================== 配置区域 ======================
WINDOW_TITLE = "USB示波器：ES7336G2  编号：2108"   #"数字存储示波器" #
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

def rect_shot_pyautogui(win_left, win_top,save_path=None):
    # 找到窗口句柄
    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    time.sleep(0.5)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(2)


    left = win_left
    top =win_top
    width = 1560
    height =1211

    # 截图
    img = pyautogui.screenshot(region=(left, top, width, height))

    if not save_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"rect_shot_{timestamp}.png"

    img.save(save_path)
    print(f"✅ 矩形截图已保存：{save_path}")
    return img

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
    ":save_png": rect_shot_pyautogui,
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

    # 【关键】先初始化，获取窗口坐标
    win_left, win_top = init()

    # 循环监听指令
    while True:
        user_input = input("请输入指令：").strip().lower()

        # 退出指令
        if user_input == "exit":
            print("退出程序")
            sys.exit()

        # 匹配并执行命令
        if user_input in COMMAND_MAP:
            run_command(COMMAND_MAP[user_input], win_left, win_top)
        else:
            print(f"❌ 无效指令！可用：{', '.join(COMMAND_MAP.keys())}")


if __name__ == "__main__":
    watch_command()

#:save_png











