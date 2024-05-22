import asyncio
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl

from datetime import datetime

from telethon import events
from telethon.errors import ForbiddenError

# Logs command handler
@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(ANNIE):
    if ANNIE.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await ANNIE.reply(
                "First Set These Vars In Heroku :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await ANNIE.reply(
                "Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await ANNIE.reply(f"__Fetching Logs...__")
    
        with open("JARVISlogs.txt", "w") as logfile:
            logfile.write("⚡ JARVISBOTS ⚡ [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(ANNIE.chat_id, "JARVISlogs.txt", caption=f"⚡ **JARVIS BOTS LOGS** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"An Exception Occured!\n\n**ERROR:** {str(e)}")

    elif ANNIE.sender_id in SUDO_USERS:
        await ANNIE.reply("» BSDK..ISKO SIRF OWNER USE KR SKTA HAI...")

# Broadcast command handler
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
async def broadcast(event):
    if event.sender_id != OWNER_ID:
        await event.reply("» Only the owner can use this command.")
        return

    message = event.pattern_match.group(1)
    if not message:
        await event.reply("» Please provide a message to broadcast.")
        return

    try:
        # Fetch all dialogs (chats, groups, channels)
        async for dialog in event.client.iter_dialogs():
            try:
                await event.client.send_message(dialog.id, message)
                await asyncio.sleep(0.1)  # Sleep to avoid hitting rate limits
            except ForbiddenError:
                # Skip if the bot is not allowed to send messages to this chat
                continue
            except Exception as e:
                # Log other exceptions
                print(f"Error broadcasting to {dialog.id}: {e}")

        await event.reply("» Broadcast message sent to all available dialogs.")
    except Exception as e:
        await event.reply(f"An error occurred: {e}")

