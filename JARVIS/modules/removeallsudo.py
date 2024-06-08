## Copy Paster Must Give Credit...
## @JARVIS_V2

import heroku3
from telethon import events
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
)

# Define the handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Remove all sudo users function
async def remove_all_sudo_users(event):
    if event.sender_id == OWNER_ID:
        heroku_conn = heroku3.from_key(HEROKU_API_KEY)
        if HEROKU_APP_NAME is not None:
            app = heroku_conn.app(HEROKU_APP_NAME)
        else:
            await event.reply("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return

        heroku_var = app.config()
        heroku_var["SUDO_USERS"] = ""
        await event.reply("All sudo users have been removed.")
    else:
        await event.reply("Only the owner can remove all sudo users.")

# Register Event Handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sremoveallsudo(?: |$)(.*)" % hl))(lambda e, b=handler: remove_all_sudo_users(e))

