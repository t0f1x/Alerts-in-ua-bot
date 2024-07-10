from telebot import *
from alerts_in_ua import Client as AlertsClient
from datetime import datetime, timedelta
import  sqlite3
db = sqlite3.connect("Local.db", check_same_thread=False)
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS Alarms (
    Sended INT
    )""")
db.commit()
sql.execute("SELECT Sended FROM Alarms")
if sql.fetchone() is None:
        sql.execute(f"INSERT INTO Alarms VALUES(?)",("T"))
        db.commit()

bot = TeleBot("!!!!!write you token (create bot in https://t.me/BotFather)") 
alerts_client = AlertsClient(token="!!!!!!write you token (https://alerts.in.ua/api-request?)")
def main(message):
    chat_id = "!!!!!write here the id of the channel or chat in which you want to write about the air alarm (https://t.me/getmyid_bot) for find id(forward from channel for find channel id)" 
    while True:
        clock = datetime.now()
        now = clock + timedelta(hours = 3) #depending on the difference between the host time and your local time (for example, on the server GMT 0, and local time GMT +3)
        current_time = now.strftime("%H:%M")
        active_alerts = alerts_client.get_active_alerts()
        location_uid_alerts = active_alerts.get_alerts_by_location_uid('!!!!!write you uid  (https://devs.alerts.in.ua/#modeluid)')
        sql.execute(f"SELECT Sended FROM Alarms")
        check = sql.fetchone()
        if location_uid_alerts != [] and check[0] != "T":
            bot.send_message(chat_id,f"!!!!!text about the start of the air alarm {current_time}")
            chech = "T"
            sql.execute(f"UPDATE Alarms SET Sended = '{chech}'")
            db.commit()
        elif location_uid_alerts == [] and check[0] != "F":
            bot.send_message(chat_id,f"!!!!!text about the end of the air alarm {current_time}")
            chech = "F"
            sql.execute(f"UPDATE Alarms SET Sended = '{chech}'")
            db.commit()
        print("request allow")
        time.sleep(8)
@bot.message_handler(commands=["start"])
def start(message):
    print("started by user")
    print(message.chat.id)
    main(message)
print("bot_started")
bot.infinity_polling()
