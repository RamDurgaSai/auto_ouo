# from time import sleep
# import time
# import pyautogui
# import pywinauto
# from pyautogui import locateOnScreen,click, locateOnWindow
# from pyautogui import locateOnScreen,click as click_on_screen
# from pywinauto.application import Application
# # app = Application(backend="win32").start("C:\\Program Files\\WireGuard\\wireguard.exe",  wait_for_idle=False)

# # d = app["WireGuard.*"].print_control_identifiers()
# sleep(5)
# from lackey import *
# click("deactivate.PNG")
# def click_image(image,timeout=60):
#     starting_time = time.time()
#     while True:
#         location = locateOnScreen(image,grayscale = True,confidence = 0.5)
#         print(location)
#         if location : break
#         elif int(time.time()-starting_time)> timeout:
#             raise TimeoutError(f"Time out {timeout}s for {image}")
        
#         sleep(1)
#     left, top, width, height = location
#     print(left+width//2,top+height//2)
#     x, y = left+width//2,top+height//2
#     # pyautogui.moveTo(x = left + width // 2,y = top + height // 2)
#     # click_on_screen(x = left+width//2, y = top+height//2)
#     pyautogui.moveTo(x,y)    # move mouse to the window
#     pyautogui.dragTo(x,y, button = 'left')    # focus the window
#     pyautogui.click(x,y,clicks=2, button = 'left')     # simulate left click

#     # pywinauto.mouse.click(button="left", coords = (left+width//2,top+height//2))

# click_image("deactivate.PNG")






from win32com.shell.shell import ShellExecuteEx
# import sys
# command = 'wireguard /installtunnelservice "C:\Program Files\Wireguard\Data\Configurations\config.conf.dpapi"'
# ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=command)

# import ctypes, sys
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
# if is_admin():
#     pass
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# command = 'wireguard /installtunnelservice "C:\Program Files\Wireguard\Data\Configurations\config.conf.dpapi"'
# ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=command)
# # Code of your program here

