from pyrogram import __version__ as pyrover
from telethon import Button
from telethon import __version__ as thlver

PHOTO = "https://te.legra.ph/file/61bbf07e33a148006dc67.jpg"

START_OREKI = f"""
Prince Oreki 왕자 Is Started!

➪ Uptime:<b><code>{}<b><code>
➪ Python Version:<b><code>{}<b><code>
➪ Pyrogram Version: {pyrover}
➪ Telethon Version: {thlver}
"""

START_BUTTON = [
    [
        Button.url("Help 🎗️", "https://t.me/orekixprorobot?start=help"),
    ]
]
await tbot.send_file(-1001878260997, PHOTO, caption=OREKI, buttons=BUTTON),
