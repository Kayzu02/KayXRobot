import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/98322780c3e994099402f.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm ҡᴧʏ ✗ ʙσᴛ!** \n\n"
  LUNA += "⚡ **I'm Working Properly** \n\n"
  LUNA += "⚡ **My Master : [ҡᴀʏ-ᴇx](https://t.me/Kayzuuuuu)** \n\n"
  LUNA += f"⚡ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"⚡ **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan ҡᴧʏ ✗ ʙσᴛ 💜**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/KayXMusicBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/KayzuSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

