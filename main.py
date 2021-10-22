import sys
from os.path import join as jion_paths, exists as exists_of
from subprocess import Popen
from os import getcwd
from psutil import process_iter
from time import sleep
from Log import Log

def launch_auto(): auto = Popen([sys.executable,jion_paths(getcwd(),"auto.py")],stdout=sys.stdout,bufsize=0)
def launch_bot(): bot = Popen([sys.executable,jion_paths(getcwd(),"bot.py")], stdout=sys.stdout, bufsize=0)

def main():
       log = Log("log.txt")
       auto_pid, bot_pid =  jion_paths(getcwd(),'pids','auto.pid'),  jion_paths(getcwd(),'pids','bot.pid')

       while True : # to keep alive
              if not exists_of(auto_pid) :
                     log.debug("Launching Auto....")
                     launch_auto()
              if not exists_of(bot_pid) : 
                     log.debug("Launching bot...")
                     launch_bot()
              sleep(60) # To rest the Cpu

              

if __name__ == "__main__":
    main()