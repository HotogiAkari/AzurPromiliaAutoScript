import win32gui
import pyautogui
import time

game_title = "The Witcher 3"
hwnd = win32gui.FindWindow(None, game_title)

if hwnd:
    # 将游戏窗口带到前台
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1) # 给窗口一些时间来激活
else:
    print("未找到游戏窗口。")
    # 这里可以添加退出或重试逻辑

# 模拟按住 W 键一秒
pyautogui.keyDown('w')
time.sleep(1)
pyautogui.keyUp('w')

# 模拟鼠标左键点击
pyautogui.click()

# 模拟鼠标移动到坐标 (100, 200)
pyautogui.moveTo(100, 200, duration=0.25)