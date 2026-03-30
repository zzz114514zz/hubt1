import pyautogui
import mouse  # 监听鼠标按键
import time

print("=== 鼠标坐标显示工具 ===")
print("按住【鼠标左键】显示坐标，松开停止")
print("按 Ctrl + C 退出程序\n")

try:
    while True:
        # 检测鼠标左键是否按住
        if mouse.is_pressed("left"):
            x, y = pyautogui.position()  # 获取当前鼠标坐标
            print(f"\r鼠标坐标：X = {x:4d} , Y = {y:4d}", end="")  # \r 让文字不换行刷屏
        time.sleep(0.05)  # 降低CPU占用

except KeyboardInterrupt:
    print("\n\n程序已退出")