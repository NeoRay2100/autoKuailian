import ctypes
import os
import sys
import pyautogui
import subprocess
import time

# 如果不是管理员权限，则重新启动脚本并请求管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
else:
    # 启动需要管理员权限的程序
    subprocess.Popen(['C:\\Program Files (x86)\\letsvpn\\LetsPRO.exe'])

    # 等待程序启动
    time.sleep(5)

    # 找到包含
    tool_group_location = pyautogui.locateOnScreen('kaiqibutton.png')

    if tool_group_location:
        # 点击
        pyautogui.click(tool_group_location)

        # 等待打开
        time.sleep(3)

        # 点击关闭按钮
        close_button_location = pyautogui.locateOnScreen('guanbibutton.png')
        if close_button_location:
            pyautogui.click(close_button_location)
        else:
            print("未找到关闭按钮")
    else:
        print("未找到包含“连接”字样的标签组")
