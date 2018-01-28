#coding: utf-8

import time
import win32gui
import ctypes
import win32com.client
import win32con
from PIL import ImageGrab
import os


screenshot_name = 'screenshot.jpg'

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long),
            ('top', ctypes.c_long),
            ('right', ctypes.c_long),
            ('bottom', ctypes.c_long)]
    def __str__(self):
        return str((self.left, self.top, self.right, self.bottom))

def screenshot_obtain(label,directory="."):
    hld = win32gui.FindWindow(label, None)
    if hld > 0:
        win32gui.ShowWindow(hld, win32con.SW_RESTORE)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hld)
        time.sleep(1)
        rect = RECT()
        ctypes.windll.user32.GetWindowRect(hld, ctypes.byref(rect))
        rangle = (rect.left + 20, rect.top + 150, rect.right - 20, 0.25 * rect.bottom)
        im = ImageGrab.grab(rangle)
        im.save(os.path.join(directory, screenshot_name), 'JPEG')
        print("screenshot success")
    else:
        print('咦，你没打开'+label+'吧!')


if __name__ == '__main__':
    screenshot_obtain('Qt5QWindowIcon')