from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import html
import time
import random

app = Client("my_account")
# Команда .id 
@app.on_message(filters.command("id", prefixes="."))
def delete(client, message):
      #client.delete_messages(message.chat.id,message.message_id)
      message.reply_text(f"<b>Sizning ID raqamingiz</b> <code>{message.from_user.id}</code>",reply_to_message_id=message.message_id)
# Команда .gid 
@app.on_message(filters.command("gid", prefixes="."))
def delete(client, message):
      #client.delete_messages(message.chat.id,message.message_id)
      message.reply_text(f"<b>Guruhning id raqami</b> <code>{message.chat.id}</code>",reply_to_message_id=message.message_id)
# Команда .pin 
@app.on_message(filters.command("pin", prefixes=".") & filters.me)
async def pin(client, msg):
	await client.delete_messages(msg.chat.id,msg.message_id)
	await msg.reply_to_message.pin(msg.chat.id,msg.reply_to_message.message_id)
# Команда .unpin 
@app.on_message(filters.command("unpin", prefixes=".") & filters.me)
async def pin(client, msg):
	await client.delete_messages(msg.chat.id,msg.message_id)
	await msg.reply_to_message.unpin(msg.chat.id,msg.reply_to_message.message_id)
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message(filters.private)
async def hello(client, message):
	await message.reply_text(f"<b>{message.from_user.mention}</b> \nSizga avtobot javob bermoqda\nMurojaatingizni qoldiring admin tez orada javob beradi")

app.run()
