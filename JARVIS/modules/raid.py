# © @JARVIS_V2
import asyncio
from random import choice
from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from JARVIS.data import RAID, REPLYRAID, FRIDAY, MRAID, SRAID, QRAID

REPLY_RAID = []

# List of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Helper function to get user ID from message
async def get_user_id(e, text, index):
    if len(text) == 3:
        entity = await e.client.get_entity(text[index])
        return entity.id, entity
    elif e.reply_to_msg_id:
        msg = await e.get_reply_message()
        entity = await e.client.get_entity(msg.sender_id)
        return entity.id, entity
    return None, None

# Raid function
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid, entity = await get_user_id(e, xraid, 2)

        if uid in FRIDAY:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
        elif uid == OWNER_ID:
            await e.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ...")
        elif uid in SUDO_USERS:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ...")
        else:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            try:
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
            except (IndexError, ValueError, NameError):
                await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
            except Exception as e:
                print(e)

# Reply raid function
async def reply_raid(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message=choice(REPLYRAID),
            reply_to=event.message.id,
        )

# Function to start reply raid
async def start_reply_raid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        uid, entity = await get_user_id(e, mkrr, 1)

        if uid in FRIDAY:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
        elif uid == OWNER_ID:
            await e.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ...")
        elif uid in SUDO_USERS:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ...")
        else:
            check = f"{uid}_{e.chat_id}"
            if check not in REPLY_RAID:
                REPLY_RAID.append(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀs ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")

# Function to stop reply raid
async def stop_reply_raid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)
        uid, entity = await get_user_id(e, text, 1)

        check = f"{uid}_{e.chat_id}"
        if check in REPLY_RAID:
            REPLY_RAID.remove(check)
        await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀs ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")

# Mraid function
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid, entity = await get_user_id(e, xraid, 2)
        
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        try:
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗠𝗥𝗮𝗶𝗱\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)

# Sraid function
async def sraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid, entity = await get_user_id(e, xraid, 2)
        
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        try:
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗦𝗥𝗮𝗶𝗱\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)

# Qraid function
async def qraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        uid, entity = await get_user_id(e, xraid, 2)

        if uid in FRIDAY:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
        elif uid == OWNER_ID:
            await e.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ...")
        elif uid in SUDO_USERS:
            await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ...")
        else:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            try:
                for _ in range(counter):
                    reply = choice(QRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
            except (IndexError, ValueError, NameError):
                await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐐𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
            except Exception as e:
                print(e)

# Register event handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))(raid)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))(start_reply_raid)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))(stop_reply_raid)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))(mraid)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))(sraid)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sqraid(?: |$)(.*)" % hl))(qraid)
    handler.on(events.NewMessage(incoming=True))(reply_raid)
