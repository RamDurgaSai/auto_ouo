from pyrogram import Client
from json import load, loads as load_json
from pid import PidFile
from os.path import join as join_paths
from os import getcwd

class Bot:

    def __init__(self,api_id, api_hash, token) -> None:
        

        self.bot = Client(session_name = "ouo_bot",api_id= api_id,api_hash = api_hash, bot_token=token)

        @self.bot.on_message()
        def on_message(client, message) : self.on_message(client,message)
    
    def on_message(self, client, message):
        text:str = message.text

        if text.startswith("#add_url"):
            links = text.splitlines()[1:]
            with open("data\links.txt","a") as link_file:
                link_file.write("\n"+"\n".join(links))
            text = 'following links added \n'+"\n".join(links)
            self.send_message(message,text)

        if "alive" in text : self.send_message(message, "Yes I am Alive")
    
    def send_message(self,message,text) : self.bot.send_message(chat_id=message.from_user.id,text=text)

    def run(self) : self.bot.run()

if __name__ == "__main__":
    with open("data/config.secret","r") as config_file:
        configurations = load_json(config_file.read())
    bot = Bot(configurations["api_id"],
              configurations["api_hash"],
              configurations["bot_token"])
    with PidFile(pidname="bot",piddir= join_paths(getcwd(),"pids")) as pid_file : 
        while True:pass # bot.run()
        # Bot is deprecated in upcoming versions 
