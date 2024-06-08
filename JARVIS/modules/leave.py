from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events
from telethon.tl.functions.channels import LeaveChannelRequest

# List of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Leave function
async def leave(event):
    if event.sender_id in SUDO_USERS:
        if len(event.text) > 7:
            reply = await event.reply("» ʟᴇᴀᴠɪɴɢ ᴛʜᴇ ɢʀᴏᴜᴘ...")
            chat_id = event.text.split(" ", 1)[1]
            try:
                await event.client(LeaveChannelRequest(int(chat_id)))
            except Exception as e:
                await reply.edit(str(e))
        else:
            if event.is_private:
                message = (
                    f"**» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!**\n\n"
                    f"» {hl}leave <ᴄʜᴀɴɴᴇʟ/ᴄʜᴀᴛ ɪᴅ>\n"
                    f"» {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ."
                )
                await event.reply(message)
            else:
                reply = await event.reply("» ʟᴇᴀᴠɪɴɢ ᴛʜᴇ ɢʀᴏᴜᴘ...")
                try:
                    await event.client(LeaveChannelRequest(int(event.chat_id)))
                except Exception as e:
                    await reply.edit(str(e))

# Register event handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))(leave)
