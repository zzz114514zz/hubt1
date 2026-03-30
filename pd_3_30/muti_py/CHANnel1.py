import pyautogui
import sys
import time
import pygetwindow as gw

# 延迟设置
pyautogui.PAUSE = 0.1

WINDOW_TITLE ="数字存储示波器"#"USB示波器：ES7336G2  编号：2108"

def run_my_task(cmd):
    print("\n执行任务中...")

    # 1. 找到目标窗口
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    if not windows:
        print(f"错误：未找到标题为 '{WINDOW_TITLE}' 的窗口！")
        return

    window = windows[0]

    # 激活窗口
    if not window.isActive:
        window.activate()
        time.sleep(1)

    # 2. 获取窗口左上角坐标（自动输出）
    win_left = window.left
    win_top = window.top

    #3.执行任务
    pyautogui.click(win_left + 10, win_top + 10)
    time.sleep(1)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(1)

    if "dc" in cmd and "50" in cmd:
        pyautogui.click(win_left+1331 -510, win_top+ 1181 -195)
    elif"dc" in cmd:
        pyautogui.click(win_left + 1331 - 510, win_top + 1070 - 195)
    elif"ac" in cmd:
        pyautogui.click(win_left + 1331 - 510, win_top + 1107 - 195)
    elif"gnd" in cmd:
        pyautogui.click(win_left + 1331 - 510, win_top + 1145 - 195)
    else:
        print("任务执行失败！\n")

    #print("任务执行完成！\n")

cmd = sys.argv[1]
def cmd_select(cmd):
    print("\n",cmd)
    if "coup" in cmd:
        run_my_task(cmd)
    else:
        print("没有此命令！\n")


if __name__ == "__main__":
    cmd_select(cmd)
