# 导入键盘控制模块
# from pynput.keyboard import Key, Controller
# import time

# # 初始化键盘控制器
# keyboard = Controller()
#
# # # 【示例1：模拟输入普通字符】
# # print("1秒后输入：Hello World")
# time.sleep(1)
# # keyboard.type("Hello World")  # 直接输入字符串
# #
# # # 【示例2：模拟组合键 Ctrl+1】
# print("\n1秒后按下组合键：Ctrl+1")
# time.sleep(1)
# # 核心写法：按下Ctrl -> 按下1 -> 松开1 -> 松开Ctrl
# with keyboard.pressed(Key.ctrl):  # 按住Ctrl键
#     keyboard.press('1')           # 按下1键
#     keyboard.release('1')         # 松开1键
#
# print("\n1秒后按下组合键：F3")
# time.sleep(1)
# # 核心写法：按下Ctrl -> 按下1 -> 松开1 -> 松开Ctrl
# with keyboard.pressed('F3'):  # 按住F3键
#     keyboard.release('F3')         # 松开
#
# #【示例3：其他常用组合键参考】
# #Ctrl+C 复制
# with keyboard.pressed(Key.ctrl):
#     keyboard.press('s')
#     keyboard.release('s')



# import pyautogui
# import pygetwindow as gw
# import time
#
# # 配置参数
# WINDOW_TITLE = "USB示波器: ES7336G2 编号: 2108"  # 你的窗口标题
# pyautogui.PAUSE = 5  # 动作间隔，防止过快
#
# print("===== 脚本已启动 =====")
# print(f"目标窗口：{WINDOW_TITLE}")
# print("按 ESC 退出脚本")
#
# def run_my_task():
#     try:
#         # 1. 找到目标窗口
#         windows = gw.getWindowsWithTitle(WINDOW_TITLE)
#         if not windows:
#             print(f"错误：未找到标题为 '{WINDOW_TITLE}' 的窗口！")
#             return
#         window = windows[0]
#         if not window.isActive:
#             window.activate()  # 激活窗口
#             time.sleep(10)     # 等待窗口激活
#
#         # 2. 获取窗口左上角坐标
#         win_left = window.left
#         win_top = window.top
#         print(f"窗口位置：左上角({win_left}, {win_top})，尺寸：{window.width}x{window.height}")
#
#         # 3. 窗口内相对坐标 → 转换为屏幕绝对坐标
#         rel_x1, rel_y1 = 1000, 1000
#         rel_x2, rel_y2 = 2000, 2000
#         abs_x1 = win_left + rel_x1
#         abs_y1 = win_top + rel_y1
#         abs_x2 = win_left + rel_x2
#         abs_y2 = win_top + rel_y2
#
#         # 4. 执行操作
#         pyautogui.click(abs_x1, abs_y1)
#         pyautogui.hotkey('ctrl', 's')
#         pyautogui.click(abs_x2, abs_y2)
#         print("✅ 任务执行完成！")
#     except Exception as e:
#         print(f"❌ 执行失败：{e}")






# import pyautogui
# import keyboard  # 监听热键
# import time
#
# # 防止点击过快导致程序没反应，可根据需要调整延迟
# pyautogui.PAUSE = 2  # 每个动作间隔0.2秒
#
# print("===== 脚本已启动 =====")
# print("按 F3 执行：点击(1000,1000) → Ctrl+S → 点击(2000,2000)")
# print("按 ESC 退出脚本")
#
#
# # 定义 F3 触发的函数
# def run_my_task():
#     print("执行任务中...")
#     time.sleep(10)
#
#
#     # 1. 按下 Ctrl + g
#     pyautogui.hotkey('ctrl', 'g')
#
#     # 2. 鼠标点击 屏幕坐标 (1000, 1000)
#     pyautogui.click(1212, 1074)
#
#     # 2. 鼠标点击 屏幕坐标 (1000, 1000)
#     pyautogui.click(900, 900)
#
#     # 3. 按下 Ctrl + S 保存
#     pyautogui.hotkey('ctrl', 's')
#
#     # 4. 鼠标点击 屏幕坐标 (2000, 2000)
#     pyautogui.click(870, 1135)
#
#     # 5. 鼠标点击 屏幕坐标 (2000, 2000)
#     pyautogui.click(1255, 1117)
#
#     print("任务执行完成！\n")
#
#
# # 绑定热键 F3
# keyboard.add_hotkey('f3', run_my_task)
#
# # 按 ESC 退出程序
# keyboard.wait('esc')






# import pygetwindow as gw
#
# # ======================
# # 在这里改你的窗口标题
# # ======================
# WINDOW_TITLE = "数字存储示波器"  # 可写部分标题，如：Chrome、Excel、微信
#
# try:
#     # 获取窗口
#     window = gw.getWindowsWithTitle(WINDOW_TITLE)[0]
#
#     # 输出窗口位置信息（核心）
#     print("===== 窗口位置信息 =====")
#     print(f"窗口左上角 X：{window.left}")
#     print(f"窗口左上角 Y：{window.top}")
#     print(f"窗口右下角 X：{window.right}")
#     print(f"窗口右下角 Y：{window.bottom}")
#     print(f"窗口宽度：{window.width}")
#     print(f"窗口高度：{window.height}")
#     print(f"完整坐标：({window.left}, {window.top})")
#
# except IndexError:
#     print(f"错误：未找到标题包含【{WINDOW_TITLE}】的窗口！")





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