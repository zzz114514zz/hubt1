import pyautogui
import sys
import time
import pygetwindow as gw
import re

# 延迟设置
pyautogui.PAUSE = 0.1

WINDOW_TITLE ="USB示波器：ES7336G2  编号：2108"#"数字存储示波器"

def find_position(arr, num):
    if num not in arr:
        return "不存在"
    idx = arr.index(num)
    return idx  # 返回第几个（从0开始）

def long_press(x, y,hold_duration):
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.mouseDown(button='left')
        time.sleep(hold_duration)
        pyautogui.mouseUp(button='left')

def coup(cmd):
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
        time.sleep(0.5)

    # 2. 获取窗口左上角坐标（自动输出）
    win_left = window.left
    win_top = window.top

    #3.执行任务
    pyautogui.click(win_left + 10, win_top + 10)
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.5)

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

    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)#关闭菜单
    #print("任务执行完成！\n")

def display(cmd):
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
        time.sleep(0.5)

    # 2. 获取窗口左上角坐标（自动输出）
    win_left = window.left
    win_top = window.top

    #3.执行任务
    pyautogui.click(win_left + 10, win_top + 10)
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.5)

    pyautogui.click(win_left + 593 - 510, win_top + 1102 - 195)

    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)#关闭菜单
def scale(cmd):
    print("\n执行任务中...")

    scal_lut=[5,2,1,0.5,0.2,0.1,0.05,0.02,0.01,0.005,0.002,0.001]

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
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.5)

    nums = re.findall(r'\d+\.?\d*', cmd)
    num = float(nums[0]) if nums else 0.0  # 没匹配到默认给 0.0，避免报错

    times = find_position(scal_lut, num)

    print(times)

    for i in range(12):
        pyautogui.click(win_left + 825 - 510, win_top + 1100 - 195)  # 增加

    for i in range(times):
        pyautogui.click(win_left + 825 - 510, win_top + 1170 - 195)  # 减少

    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
def offset(cmd):
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
        time.sleep(0.5)

    # 2. 获取窗口左上角坐标（自动输出）
    win_left = window.left
    win_top = window.top

    #3.执行任务
    pyautogui.click(win_left + 10, win_top + 10)
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.5)

    nums = re.findall(r'[+-]?\d+\.?\d*', cmd)
    num = float(nums[0]) if nums else 0.0  # 没匹配到默认给 0.0，避免报错

    times=int((abs(num)//0.003125))


    pyautogui.click(win_left + 996 - 510, win_top + 1170 - 195)  # 归零

    if abs(num)>=0.5 and num>=0:
        hold_duration=int(num//0.5)
        click_u=int((abs(num)%0.5)//0.003125)
        plus_x = win_left + 1096 - 510
        plus_y = win_top + 1096 - 195
        for i in range (hold_duration) :
            long_press(plus_x,plus_y,0.7)
            pyautogui.click(win_left + 1096 - 510, win_top + 1170 - 195)
            time.sleep(0.01)
        for i in range (click_u) :
            pyautogui.click(plus_x, plus_y)  #剩余次数

    elif abs(num)>=0.5 and num<0:
        hold_time=abs(int(num//0.5))
        click_u=int((abs(num)%0.5)//0.003125)
        low_x = win_left + 1096 - 510
        low_y = win_top + 1170 - 195
        for i in range(hold_time):
            long_press(low_x, low_y, 0.7)
            pyautogui.click(win_left + 1096 - 510, win_top + 1096 - 195)
            time.sleep(0.01)
        for i in range (click_u) :
            pyautogui.click(low_x, low_y)  #剩余次数

    elif abs(num)<0.5:
        if num>=0 :
            for i in range(times):
                pyautogui.click(win_left + 1096 - 510, win_top + 1096 - 195)  # 500格以内只用短按
        elif num<0 :
            for i in range(times):
                pyautogui.click(win_left + 1096 - 510, win_top + 1170 - 195)  # 500格以内只用短按

    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    print(times)
def offset(cmd):
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

    nums = re.findall(r'\d+\.?\d*', cmd)
    num = float(nums[0]) if nums else 0.0  # 没匹配到默认给 0.0，避免报错

    times=int((num//0.003125)+1)

    print(times)

    pyautogui.click(win_left + 996 - 510, win_top + 1170 - 195)  # 归零

    if times>=0:
        for i in range(times):
            pyautogui.click(win_left + 1096 - 510, win_top + 1096 - 195)  # 增加

    elif times<0:
        for i in range(abs(times)):
            pyautogui.click(win_left + 1096 - 510, win_top + 1170 - 195)  # 减少

    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单

def offset_v(cmd):
    print("\n执行任务中...")

    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    if not windows:
        print(f"错误：未找到标题为 '{WINDOW_TITLE}' 的窗口！")
        return

    window = windows[0]

    if not window.isActive:
        window.activate()
        time.sleep(0.5)

    win_left = window.left
    win_top = window.top

    pyautogui.click(win_left + 10, win_top + 10)
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.5)

    nums = re.findall(r'[+-]?\d+\.?\d*', cmd)
    if not nums:
        print("任务执行失败：未检测到有效数值！\n")
        return

    input_str = nums[0]

    key_coords = {
        '7': (581, 783),
        '8': (719, 783),
        '9': (857, 783),
        '4': (581, 883),
        '5': (719, 883),
        '6': (857, 883),
        '1': (581, 983),
        '2': (719, 983),
        '3': (857, 983),
        '.': (581, 1083),
        '0': (719, 1083),
        '-': (857, 1083),
        '清零': (1119, 788)
    }

    def press_key(char):
        if char not in key_coords:
            print(f"警告：不支持的按键 '{char}'，已跳过")
            return
        x, y = key_coords[char]
        pyautogui.moveTo(win_left + x, win_top + y, duration=0.05)
        pyautogui.click()
        time.sleep(0.1)

    # 先清零，再按字符串逐位输入（支持负号和小数点）
    pyautogui.click(win_left + 1224 - 510, win_top + 1103 - 195)  # 打开键盘
    press_key('清零')
    for char in input_str:
        press_key(char)

    pyautogui.click(win_left + 1161 - 510, win_top + 1381 - 195)  # 确定
    pyautogui.click(win_left + 2025 - 510, win_top + 991 - 195)  # 关闭菜单


cmd = sys.argv[1]

def cmd_select(cmd):
    state = [False, 0]
    print("\n",cmd)
    if "coup" in cmd:
        coup(cmd)
    elif "disp" in cmd:
        display(cmd)
    elif "scal" in cmd:
        scale(cmd)
    elif "offset_v" in cmd:
        offset_v(cmd)
    elif "offs" in cmd:
        offset(cmd)
    else:
        print("没有此命令！\n")


if __name__ == "__main__":
    cmd_select(cmd)
