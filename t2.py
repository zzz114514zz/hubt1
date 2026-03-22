import pyautogui
import keyboard
import time
import pygetwindow as gw

# 延迟设置
pyautogui.PAUSE = 0.5

print("===== 脚本已启动 =====")
print("按 F3 执行任务")
print("按 ESC 退出脚本")

# ======================
# 在这里修改你的窗口标题
# ======================
WINDOW_TITLE = "数字存储示波器"


def run_my_task():
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
    print(f"✅ 窗口位置：左上角 ({win_left}, {win_top})")
    print(f"✅ 窗口尺寸：{window.width} x {window.height}")

    # ======================================================
    # 【你的原始坐标 → 自动转换为窗口相对坐标】
    # 你原来的屏幕坐标：
    # 1212,1074
    # 900,900
    # 870,1135
    # 1255,1117
    # ======================================================

    # 按下 Ctrl+G
    pyautogui.click(win_left+10, win_top+10)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'g')
    time.sleep(1)

    # 点击 窗口内相对坐标（自动计算屏幕坐标）
    pyautogui.click(win_left + 1212-510, win_top + 1074-195)
    pyautogui.click(win_left + 900-510, win_top + 900-195)

    # 按下 Ctrl+S 保存
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    # 继续点击
    pyautogui.click(win_left + 870-510, win_top + 1135-195)
    pyautogui.click(win_left + 1255-510, win_top + 1117-195)

    print("✅ 任务执行完成！\n")


# 绑定热键 F3
keyboard.add_hotkey('1', run_my_task)

# 按 ESC 退出
keyboard.wait('esc')