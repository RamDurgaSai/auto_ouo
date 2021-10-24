from selenium.webdriver import Firefox, FirefoxOptions
from webbrowser import get, open as open_in_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep,time as present_time
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
                if button.text == "GET LINK":
                    sleep(5)
                    self.browser.execute_script("arguments[0].click();", button)
                    self.log.debug("Successfully clicked the get link button")
                    break
                self.browser.execute_script("arguments[0].click();", button)
        
                current_window = self.browser.current_window_handle
                windows = self.browser.window_handles
                for window in windows:
                    if current_window != window:
                        self.browser.close()
                self.browser.switch_to.window(choice(self.browser.window_handles))

            except IpNotWorking as ip_not_working:
                raise ip_not_working
            except:self.run()
        sleep(15)
        self.browser.quit()

    def set_tab(self):
        child_windows = self.browser.window_handles
        current_window = self.browser.current_window_handle
        for child_window in child_windows: 
            if current_window != child_window : self.browser.switch_to.window(child_window)


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

            

    
if __name__ == "__main__":
 
    with PidFile(pidname= "auto",piddir = jion_paths(getcwd(),"pids")) as pid_file:
        with open("data/last_used_config.txt","r") as file: config_file = file.read()
        config_file = basename(config_file).split(".")[0]
        system(f'wireguard /uninstalltunnelservice "{config_file}"')


        main() # To do Work
        
        
