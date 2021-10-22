from selenium.webdriver import Firefox, FirefoxOptions
from webbrowser import get, open as open_in_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep,time as present_time
from pyautogui import locateOnScreen,click as click_on_screen
# from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
from subprocess import Popen
from random import choice
from os.path import join as jion_paths, isfile, basename
from os import getcwd, listdir, system, rename
from json import load, loads as load_json_data
from pid import PidFile
from Log import Log
from requests import get
from socket import gethostname, gethostbyname

class IpNotWorking(Exception):pass

class Auto:

    ButtonMain = '//*[@id="btn-main"]' # xpath for both IamHUman and GetLink Buttons
    ouo_link = "http://ouo.io/qs/PxldEKyr?s=yourdestinationlink.com"

    def __init__(self,link) -> None:
        self.log = Log("log.txt")
        self.link  = self.ouo_link.replace("yourdestinationlink.com",link)
        self.browser = Firefox(executable_path="tools\geckodriver.exe")
        self.browser.maximize_window()


    

    def run(self):
        self.browser.get(self.link)
        while True:
            try:
                sleep(5)
                content = self.browser.page_source

                if "Checking" in content: raise IpNotWorking("Current Ip not Working --- Try New") # May be Site not Working ----> change ip now 

                self.wait_for_element(self.ButtonMain)
                button = self.browser.find_element_by_xpath(self.ButtonMain)
                self.set_center_of_screen(button)
                if self.click_image() == "images\getLinkButtonNew.PNG" : break
                current_window = self.browser.current_window_handle
                windows = self.browser.window_handles
                for window in windows:
                    if current_window != window:
                        self.browser.close()
                self.browser.switch_to.window(choice(self.browser.window_handles))

            except IpNotWorking as ip_not_working:
                raise ip_not_working
            except:self.run()
        sleep(10)
        self.browser.quit()

    def set_tab(self):
        child_windows = self.browser.window_handles
        current_window = self.browser.current_window_handle
        for child_window in child_windows: 
            if current_window != child_window : self.browser.switch_to.window(child_window)

    def click_image(self,timeout=60) -> str:
        images = ["images\getLinkButtonNew.PNG","images\IamHumanButtonNew.PNG"]
        starting_time = present_time()
        while True:
            sleep(1)
            image = choice(images)
            self.log.debug(f"waiting for images  since {int(present_time()-starting_time)}s")
            location = locateOnScreen(image,grayscale = True,confidence = 0.5)
            if location: break

            if int(present_time() - starting_time) > timeout:
                raise TimeoutError(f"Timeout Exceed for image {image}")


        left, top, width, height = location
        if image == images[0]:sleep(3)
        click_on_screen(x = left+width//2, y = top + height//2)
        return image


    def wait_for_element(self,xpath:str,timeout=60):
            element = WebDriverWait(self.browser, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath)))



    def set_center_of_screen(self, element:WebElement) -> None:
        self.browser.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"})',element)
    def close(self):
        if self.browser : self.browser.quit()
def get_ip_details():
    responce = get("https://geolocation-db.com/json/")
    return  load_json_data(responce.content.decode('utf-8'))


def main_nord(vpn=True,retries = 5):
    try: 
        while True:
            with open("links.txt","r") as file:
                links = file.read().splitlines()
            if vpn:
                if retries > 3:
                    retries = 1
                    rotate_VPN()
                else:retries += 1

                
            link = choice(links)
            print(f"Doing work for {link}")
            auto = Auto(link)
            auto.run()
            sleep(5)
    except Exception as e:
        print(f"Wtf happen ...\n{str(e)}")
        sleep(120)
        main(vpn,retries)
        
def main(config_file = None, retries = 5):
    log = Log("log.txt")
    config_path = "C:\\Program Files\\Wireguard\\Data\\Configurations"
    config_path = jion_paths(getcwd(),"confs")
    try:
        while True:
            with open("data\links.txt","r") as file:
                links = file.read().splitlines()
            if retries > 3:
                if config_file : 
                    config_file = basename(config_file).split(".")[0]
                    system(f'wireguard /uninstalltunnelservice "{config_file}"')
                config_file = choice([jion_paths(config_path,config_file) for config_file in listdir(config_path)])
                log.debug(f"Trying to Change Ip --- with config {basename(config_file)}")
                system(f'wireguard /installtunnelservice "{config_file}"')
                #save config_file in somewhere
                with open("data\last_used_config.txt","w") as file: file.write(str(config_file))
                sleep(2)
                ip_detials = get_ip_details()
                log.debug("Ip Changed Successfully ... ")
                log.debug(f"\nip : {ip_detials['IPv4']}\ncity : {ip_detials['city']}\nstate : {ip_detials['state']}\ncountry : {ip_detials['country_name']}({ip_detials['country_code']})")

                retries = 1
            else: retries += 1

            link = choice(links)
            log.debug(f"Doing work for {link} at retires {retries}")
            auto = Auto(link)
            try: auto.run()
            except IpNotWorking as ip_not_working:
                log.error("Ip not Working ...")
                retries = 5
            #sleep(5)
            auto.close()
            auto = None
    except Exception as e:
        raise e
        print(f"Due to following Error Trying meee... \n{str(e)}")
        main(config_file, retries)

def rearrangetunnels():
    pass
    # for index,tunnel in enumerate(listdir(jion_paths(getcwd(),"confs"))):
    #     tunnel = jion_paths(getcwd(),"confs",tunnel)
    #     with open(tunnel,"r+") as tunnel:
    #         lines = [line for line in tunnel.read().splitlines()]
    #         for line in lines:
    #             if "Allo"

    #rename(jion_paths(getcwd(),"confs",tunnel),jion_paths(getcwd(),"confs",tunnel.replace(")","")))
            

    
if __name__ == "__main__":
    # with open("config.secret","r") as config_file:
    #     configurations = load_json_data(config_file.read())
    # vpn = configurations["vpn"]
    # if vpn :
    #     initialize_VPN(save=1,area_input=["United States","Australia"])
    #     main_nord(vpn)
    # rearrangetunnels()
    
    # main()
    with PidFile(pidname= "auto",piddir = jion_paths(getcwd(),"pids")) as pid_file:
        with open("data/last_used_config.txt","r") as file: config_file = file.read()
        config_file = basename(config_file).split(".")[0]
        system(f'wireguard /uninstalltunnelservice "{config_file}"')


        main()
        # print("auto started")
        # sleep(5)
        # print("auto ended")
        
