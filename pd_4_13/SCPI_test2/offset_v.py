import pyautogui
import time

# 1. 定义所有按键的坐标映射（根据你提供的基准坐标推算）
key_coords = {
    '7': (1091, 978),
    '8': (1229, 978),
    '9': (1367, 978),
    '4': (1091, 1078),
    '5': (1229, 1078),
    '6': (1367, 1078),
    '1': (1091, 1178),
    '2': (1229, 1178),
    '3': (1367, 1178),
    '.': (1091, 1278),
    '0': (1229, 1278),
    '-': (1367, 1278),
    '清零': (1629, 983)  # 归零键坐标
}


def press_key(char: str, delay: float = 0.1) -> None:
    """
    模拟点击单个按键
    :param char: 要点击的按键字符（数字、.、+/-、清零）
    :param delay: 点击后延迟时间（秒），避免操作过快
    """
    if char not in key_coords:
        print(f"警告：不支持的按键 '{char}'，已跳过")
        return

    x, y = key_coords[char]
    # 移动鼠标到按键位置并点击
    pyautogui.moveTo(x, y, duration=0.05)  # duration控制移动速度，更自然
    pyautogui.click()
    time.sleep(delay)  # 点击后延迟，防止系统响应不及时


def input_number_sequence(input_str: str, delay: float = 0.1) -> None:
    """
    输入一串数字（支持浮点数），遇到清零指令则执行清零
    :param input_str: 输入字符串，例如 "123.45" 或 "清零12.3"
    :param delay: 每个按键的点击间隔
    """
    # 先处理特殊指令：如果包含"清零"，则拆分执行
    if '清零' in input_str:
        parts = input_str.split('清零')
        # 处理清零前的内容
        if parts[0]:
            for char in parts[0]:
                press_key(char, delay)
        # 执行清零
        press_key('清零', delay)
        # 处理清零后的内容
        if len(parts) > 1 and parts[1]:
            for char in parts[1]:
                press_key(char, delay)
    else:
        # 无清零指令，直接逐个输入
        for char in input_str:
            press_key(char, delay)




if __name__ == "__main__":
    # 给用户5秒时间切换到目标窗口（计算器APP）
    print("⚠️  请在5秒内切换到计算器窗口，程序将自动开始操作...")
    time.sleep(5)

    # 示例1：输入浮点数 123.45
    input_number_sequence("-1")

    # 示例2：先输入678，再清零，再输入0.99
    # input_number_sequence("678清零0.99")

    # 你可以在这里修改为自己需要的输入内容
    # input_number_sequence("你的输入内容")