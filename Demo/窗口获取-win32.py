import win32gui
import win32api
import win32con
import time # 需要导入 time 模块

windows_title = 'The Witcher 3'
hwnd = win32gui.FindWindow(None, windows_title)

# 检查是否找到窗口
if hwnd:
    print(f"找到游戏窗口，句柄为: {hwnd}")
    
    # 获取窗口的矩形信息（左，上，右，下）
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    
    print(f"窗口位置: 左={left}, 上={top}")
    print(f"窗口大小: 宽度={width}, 高度={height}")

    # 目标在窗口内的相对坐标 (x, y)
    x, y = 500, 500
    lParam_pos = win32api.MAKELONG(x, y) # 将x,y坐标打包成一个lParam

    def click_mouse(window_handle, pos):
        # 发送鼠标左键按下消息
        win32api.PostMessage(window_handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
        time.sleep(0.1)
        # 发送鼠标左键释放消息
        win32api.PostMessage(window_handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos)

    def press_w(window_handle):
        # 发送按键W的按下消息
        win32api.PostMessage(window_handle, win32con.WM_KEYDOWN, ord("W"), 0)
        time.sleep(5) # 短暂延迟，避免按键瞬间释放
        # 发送按键W的释放消息
        win32api.PostMessage(window_handle, win32con.WM_KEYUP, ord("W"), 0)
    
    # 调用函数执行操作，传递 hwnd 和 lParam_pos
    click_mouse(hwnd, lParam_pos)
    press_w(hwnd)

else:
    print("未找到指定的游戏窗口，请确认游戏是否已启动且标题正确。")