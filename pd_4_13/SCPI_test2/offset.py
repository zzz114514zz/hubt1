import pyautogui
import keyboard
import time
import pygetwindow as gw

pyautogui.PAUSE = 0.2

print("===== 脚本已启动 =====")
print("按 F3 执行任务")
print("按 ESC 退出脚本")

# ======================
# 在这里修改你的窗口标题
# ======================
WINDOW_TITLE = "数字存储示波器"


def run_500():
    print("\n执行任务中...")

    # 1. 找到并激活窗口
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    if not windows:
        print(f"错误：未找到标题为 '{WINDOW_TITLE}' 的窗口！")
        return

    window = windows[0]
    if not window.isActive:
        window.activate()
        time.sleep(1)

    # 2. 获取窗口位置并输出
    win_left = window.left
    win_top = window.top
    print(f"窗口位置：左上角 ({win_left}, {win_top})")
    print(f"窗口尺寸：{window.width} x {window.height}")

    # =============================================
    # 在指定坐标 按住左键 持续 3 秒
    # =============================================
    hold_x = win_left + 1096-510  # 窗口内相对X，改触发电压为1206
    hold_y = win_top + 1096-195   # 窗口内相对Y，改触发电压为1096

    # 移动鼠标
    pyautogui.moveTo(hold_x, hold_y, duration=0.001)
    # 按住左键
    pyautogui.mouseDown(button='left')
    # 按住持续时间
    time.sleep(0.6)
    # 松开左键
    pyautogui.mouseUp(button='left')

    pyautogui.click(win_left + 1096 - 510, win_top + 1170 - 195)#改触发电压为1206，11701

    #用于触发时一次改变1V
    print("✅ 任务执行完成！\n")


# 绑定热键
keyboard.add_hotkey('1', run_500)
keyboard.wait('esc')