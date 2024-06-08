from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/JARVIS_V_SUPPORT/5"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Dora_Hub")
    ],
    [Button.url("• ʀᴇᴘᴏ •", "https://github.com/doraemon890/JARVIS-X-SPAM")]
]

# Define a list of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Register event handlers
for handler in handlers:
    @handler.on(events.NewMessage(pattern="/start"))
    async def start(event):
        if event.is_private:
            ANNIE = await event.client.get_me()
            bot_name = ANNIE.first_name
            bot_id = ANNIE.id

            TEXT = (
                f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n"
                f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
                f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [JARVIS](https://t.me/JARVIS_V2)**\n\n"
                f"» **ᴊᴀʀᴠɪs V2 :** `M 1.8.31`\n"
                f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
                f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
            )

            await event.client.send_file(
                event.chat_id,
                "https://github.com/doraemon890/JARVIS-X-SPAM/assets/155803358/f30a5777-9823-45d0-9860-342eceadb774",
                caption=TEXT,
                buttons=START_BUTTON
            )
