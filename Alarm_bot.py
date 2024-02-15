#project by t0f1x


from telebot import *
from alerts_in_ua import Client as AlertsClient
from datetime import datetime
bot = TeleBot("") #write you token (create bot in https://t.me/BotFather)
alerts_client = AlertsClient(token="") #write you token (https://alerts.in.ua/api-request?)
now = datetime.now()
def main(message):
    chat_id = "00000000" #write here the id of the channel or chat in which you want to write about the air alarm (https://t.me/getmyid_bot) for find id(forward from channel for find channel id)
    check = 1
    while True:
        current_time = now.strftime("%H:%M")
        active_alerts = alerts_client.get_active_alerts()
        location_uid_alerts = active_alerts.get_alerts_by_location_uid('write you uid  (https://devs.alerts.in.ua/#modeluid)')
        if location_uid_alerts != [] and check == 1:
            bot.send_message(chat_id,f"text about the start of the air alarm {current_time}")
            check = 0
        elif location_uid_alerts == [] and check == 0:
            bot.send_message(chat_id,f"text about the end of the air alarm {current_time}")
            check = 1
        time.sleep(60)
@bot.message_handler(commands=["start"])
def start(message):
    print("started by user")
    print(message.chat.id)
    main(message)
print("bot_started")
bot.infinity_polling()
