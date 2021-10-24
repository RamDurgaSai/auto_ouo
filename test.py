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






# from win32com.shell.shell import ShellExecuteEx
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

from time import sleep
from selenium.webdriver import Firefox, FirefoxOptions
from webbrowser import get, open as open_in_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from os import getcwd
from os.path import join
print(getcwd())
browser = Firefox(executable_path=join(getcwd(),"auto_ouo","tools\geckodriver.exe"))
browser.maximize_window()
browser.get("http://ouo.io/qs/PxldEKyr?s=yourdestinationlink.com")
sleep(10)

while True:
    try:
        sleep(3)
        button = browser.find_element_by_xpath( '//*[@id="btn-main"]')
        print(button.text)
        browser.execute_script("arguments[0].click();", button)
        if button.text == "GET LINK":
            browser.execute_script("arguments[0].click();", button)
            print("Successfully completed task ")
            sleep(4546556)
    except:pass