import pyautogui
import time

def go_forward(time):
    '''
    Press the 'w' key at the specified time.
    按下指定时间的'w'
    '''
    pyautogui.keyDown('w')
    time.sleep(time)
    pyautogui.keyUp('w')

def move_cursor(x, y, time=1):
    '''
    Move the cursor a specified distance in the designated direction.
    向指定方向移动指定距离的光标
    '''
    pyautogui.moveRel(x, y, time)

def click_mode(mode, x=None, y=None, button='left'):
    """
    Different mouse click mode according to the pattern.
    根据模式执行不同的鼠标点击操作. 

    :param mode: 0 - Free click. 1 - Click the specified coordinates. 
    :param button: cliked button in mode 0('left', 'middle', 'right'). 
    :param x: x coordinates in mode 1. 
    :param y: y coordinates in mode 1. 
    """
    if mode == 0:
        # mode 0
        pyautogui.click(button=button)
        
    elif mode == 1:
        # 模式1: 指定坐标点击, 只执行左键点击
        if x is None or y is None:
            raise TypeError("click_mode: Mode 1 must provide x and y coordinates.")
        pyautogui.click(x=x, y=y)
        
    else:
        raise TypeError("click_mode: Invalid mode, the mode parameter should be 0 or 1.")
