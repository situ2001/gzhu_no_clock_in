import os
import time
from datetime import datetime
import telegram

token = str(os.environ['TOKEN'])
chat_id = str(os.environ['CHAT_ID'])

def bot_succeeded(token, chat_id):
    bot = telegram.Bot(token)
    today = datetime.today()
    bot.send_message(chat_id, text=str(today.month)+"月"+str(today.day)+"日的远程打卡成功！")
    
    
bot_succeeded(token, chat_id)
