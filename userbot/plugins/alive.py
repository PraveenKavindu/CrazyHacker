import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/df341e393aeda55112d3c.jpg"
pm_caption = "**ᴄʀᴀᴢʏ ʜᴀᴄᴋᴇʀ ʙᴏᴛ ɪꜱ ᴏɴʟɪɴᴇ**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴄʀᴀᴢʏʜᴀᴄᴋᴇʀ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ        :  2.7.3 \n"

pm_caption += f"**✧ Telethon version :** `{version.__version__}\n"

pm_caption += f"**✧ Uptime :** `{uptime}\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support_group)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [GNU ʟɪᴄᴇɴꜱᴇ](https://github.com/PraveenKavindu/CrazyHacker/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [ᴄʀᴀᴢʏ ʜᴀᴄᴋᴇʀ ʙᴏᴛ](https://github.com/PraveenKavindu/CrazyHacker)\n"

pm_caption += " [╔═╦═╦══╦══╦═╦╗ ╔╗╔╦══╦═╦╦╦═╦═╗\n ║╔╣╬║╔╗╠══╠╗║║ ║╚╝║╔╗║╔╣╔╣╦╣╬║\n ╚═╩╩╩╝╚╩══╩══╝ ╚╝╚╩╝╚╩═╩╩╩═╩╩╝](https://t.me/PRAVEEN_KAVINDU)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
