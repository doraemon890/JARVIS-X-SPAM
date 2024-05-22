import asyncio
import heroku3
from pymongo import MongoClient
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError

# MongoDB configuration
MONGO_URI = "mongodb+srv://JARVIS:SPAMX10@jarvisspam.2wmzbix.mongodb.net/?retryWrites=true&w=majority&appName=JarvisSpam"
client = MongoClient(MONGO_URI)
db = client["telegram_bot_db"]
chat_ids_collection = db["chat_ids"]
users_collection = db["users"]
stats_collection = db["stats"]

# Function to add a chat ID to the database
def add_chat_id(chat_id, bot_name):
    if chat_ids_collection.count_documents({"chat_id": chat_id, "bot_name": bot_name}) == 0:
        chat_ids_collection.insert_one({"chat_id": chat_id, "bot_name": bot_name})

# Function to load all chat IDs for a specific bot from the database
def load_chat_ids(bot_name):
    return [doc["chat_id"] for doc in chat_ids_collection.find({"bot_name": bot_name})]

# Function to add a user to the database
def add_user(user_id, username, bot_name):
    if users_collection.count_documents({"user_id": user_id, "bot_name": bot_name}) == 0:
        users_collection.insert_one({"user_id": user_id, "username": username, "bot_name": bot_name})

# Function to update statistics for a bot
def update_stats(bot_name, field, value):
    stats_collection.update_one({"bot_name": bot_name}, {"$inc": {field: value}}, upsert=True)

# Function to get statistics for all bots
def get_stats():
    return list(stats_collection.find())

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
                "First Set These Vars In Heroku: `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
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
        ms = (end - start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(ANNIE.chat_id, "JARVISlogs.txt", caption=f"⚡ **JARVIS BOTS LOGS** ⚡\n  » **Time Taken:** `{ms} seconds`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

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

    bot_name = event.client.me.username
    chat_ids = load_chat_ids(bot_name)

    if not chat_ids:
        await event.reply("» No chat IDs found for broadcasting.")
        return

    for chat_id in chat_ids:
        try:
            await event.client.send_message(chat_id, message)
            await asyncio.sleep(0.1)  # Sleep to avoid hitting rate limits
        except ForbiddenError:
            continue
        except Exception as e:
            print(f"Error broadcasting to {chat_id}: {e}")

    await event.reply("» Broadcast message sent to all available chats.")

# Store chat IDs and users when receiving messages
@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def store_chat_id(event):
    bot_name = event.client.me.username
    add_chat_id(event.chat_id, bot_name)
    add_user(event.sender_id, event.sender.username, bot_name)
    update_stats(bot_name, "messages", 1)

# Stats command handler
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def stats(event):
    if event.sender_id != OWNER_ID:
        await event.reply("» Only the owner can use this command.")
        return

    stats_data = get_stats()
    if not stats_data:
        await event.reply("» No statistics available.")
        return

    message = "**Bot Statistics:**\n\n"
    for stat in stats_data:
        message += f"**Bot:** {stat['bot_name']}\n"
        message += f"**Messages:** {stat.get('messages', 0)}\n"
        message += "\n"

    await event.reply(message)
