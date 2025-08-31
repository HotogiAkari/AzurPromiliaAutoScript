'''
查找窗口并设置为活动窗口
'''

import win32gui
import time

def open_window(): 
    game_title = "The Witcher 3"
    hwnd = win32gui.FindWindow(None, game_title)
    if hwnd:
        # 将游戏窗口带到前台
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
    else:
        print("未找到游戏窗口, 请先启动游戏.")