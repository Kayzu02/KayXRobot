import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/98322780c3e994099402f.jpg"

@MEMEK(pattern=("/mhelp"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "** ──「 Perintah Dasar 」── ** \n\n"
  LUNA += "• /play **(nama lagu / balas ke audio) — play musik/video via YouTube** \n"
  LUNA += "• /playlist - **Untuk memutar playlist Anda atau playlist group anda** \n"
  LUNA += "• /song - ** (nama lagu) mendownload lagu via YouTube** \n\n"
  LUNA += "** ──「 Admin CMD 」── ** \n\n"
  LUNA += "• /pause - **Untuk pause musik/video yang sedang di putar** \n"
  LUNA += "• /resume - **Untuk melanjutkan musik/video yang sedang ter pause** \n"
  LUNA += "• /skip - **Untuk melewati lagu berikutnya** \n"
  LUNA += "• /end - **Untuk memberhentikan pemutaran musik/video** \n"
  LUNA += "• /reload - **Untuk memperbarui admin list** \n"

  BUTTON = [[Button.url("Bot Music", "https://t.me/MusicKay_Bot"), Button.url("Updates", "https://t.me/kayzuchannel")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
