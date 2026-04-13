# import mss
# import mss.tools
# from datetime import datetime
#
# def rect_shot(x1, y1, x2, y2, save_path=None):
#     """
#     传入两个对角坐标，自动截取矩形区域
#     :param x1: 第一个点 x
#     :param y1: 第一个点 y
#     :param x2: 第二个点 x
#     :param y2: 第二个点 y
#     :param save_path: 保存路径，不填则自动用时间命名
#     :return: 截图对象
#     """
#     # 自动计算最小/最大坐标，确保截图正确
#     left = min(x1, x2)
#     top = min(y1, y2)
#     width = abs(x2 - x1)
#     height = abs(y2 - y1)
#
#     monitor = {
#         "top": top,
#         "left": left,
#         "width": width,
#         "height": height
#     }
#
#     with mss.mss() as sct:
#         img = sct.grab(monitor)
#
#         # 自动命名
#         if not save_path:
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             save_path = f"rect_shot_{timestamp}.png"
#
#         # 保存图片
#         mss.tools.to_png(img.rgb, img.size, output=save_path)
#         print(f"✅ 矩形截图已保存：{save_path}")
#         return img
#
# # ------------------- 使用示例 -------------------
# # 你只需要改这里的两个坐标即可！
# if __name__ == "__main__":
#     # 示例：截取 (100,100) 到 (500,500) 的矩形
#     rect_shot(x1=100, y1=100, x2=500, y2=500)






import pyautogui
from datetime import datetime

def rect_shot_pyautogui(x1, y1, x2, y2, save_path=None):
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    # 截图
    img = pyautogui.screenshot(region=(left, top, width, height))

    if not save_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"rect_shot_{timestamp}.png"

    img.save(save_path)
    print(f"✅ 矩形截图已保存：{save_path}")
    return img

# 使用示例
rect_shot_pyautogui(100, 100, 500, 500)




