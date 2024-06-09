## Copy Paster Must Give Credit...
## @JARVIS_V2

import asyncio
import heroku3
from pymongo import MongoClient
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from telethon.tl.custom import Button
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    MONGO_DB_URI, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
)

# MongoDB configuration
client = MongoClient(MONGO_DB_URI)

# Define individual databases for each bot
db_names = [
    'bot_database_1', 'bot_database_2', 'bot_database_3', 'bot_database_4', 'bot_database_5', 
    'bot_database_6', 'bot_database_7', 'bot_database_8', 'bot_database_9', 'bot_database_10'
]

# Define the handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Map the handlers to their respective databases
db_map = {handler: client[db_name] for handler, db_name in zip(handlers, db_names)}

# Heroku logs URL
AYU = "https://graph.org/file/3a93e14b4e1c6c1d031e7.mp4"

# Fetch Heroku logs
async def fetch_heroku_logs(event, bot):
    if not HEROKU_APP_NAME or not HEROKU_API_KEY:
        await event.reply("First set these vars in Heroku: `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
        return None

    try:
        heroku_conn = heroku3.from_key(HEROKU_API_KEY)
        app = heroku_conn.app(HEROKU_APP_NAME)
        return app.get_log()
    except Exception:
        await event.reply("Make sure your Heroku API Key and App Name are configured correctly in Heroku.")
        return None

# Write logs to file
async def write_logs_to_file(logs):
    with open("Jarvislogs.txt", "w") as logfile:
        logfile.write("𖤍 ᴊᴀʀᴠɪs 𖤍 [ ʙᴏᴛ ʟᴏɢs ]\n\n" + logs)

# Send logs file
async def send_logs_file(event, ms, bot):
    try:
        await bot.send_file(event.chat_id, "Jarvislogs.txt", caption=f"𝗝𝗔𝗥𝗩𝗜𝗦 𝗕𝗢𝗧𝗦 𝗟𝗢𝗚𝗦 📨\n\n  » **Time Taken:** `{ms} seconds`")
    except Exception as e:
        await event.reply(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

# Logs command
async def logs(event, bot):
    if event.sender_id == OWNER_ID:
        start = datetime.now()
        fetch = await event.reply("__Fetching Logs...__")
        logs = await fetch_heroku_logs(event, bot)

        if logs:
            await write_logs_to_file(logs)
            end = datetime.now()
            ms = (end - start).seconds
            await asyncio.sleep(1)
            await send_logs_file(event, ms, bot)
            await fetch.delete()
    elif event.sender_id in SUDO_USERS:
        await event.reply("**»** ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ...")

# Track stats
async def track_stats(event, bot):
    stats_collection = db_map[bot]['stats']
    if event.is_group:
        group_id = event.chat_id
        stats_collection.update_one(
            {'type': 'group', 'id': group_id},
            {'$set': {'id': group_id}},
            upsert=True
        )
    elif event.is_private:
        user_id = event.sender_id
        stats_collection.update_one(
            {'type': 'user', 'id': user_id},
            {'$set': {'id': user_id}},
            upsert=True
        )

# Check stats
async def check_stats(event, bot):
    stats_collection = db_map[bot]['stats']
    if event.sender_id in SUDO_USERS or event.sender_id == OWNER_ID:
        user_count = stats_collection.count_documents({'type': 'user'})
        group_count = stats_collection.count_documents({'type': 'group'})
        stats_message = f"⚔️ 𝗝𝗔𝗥𝗩𝗜𝗦 𝗕𝗢𝗧𝗦 𝗦𝗧𝗔𝗧𝗦 ⚔️\n\n"
        stats_message += f"**Bot {handlers.index(bot) + 1} Stats:**\n"
        stats_message += f"Users: {user_count}\nGroups: {group_count}\n\n"
        
        # Collect stats from other bots
        other_stats = []
        for other_bot in handlers:
            if other_bot != bot:
                other_stats_collection = db_map[other_bot]['stats']
                other_user_count = other_stats_collection.count_documents({'type': 'user'})
                other_group_count = other_stats_collection.count_documents({'type': 'group'})
                other_stats.append(f"**Bot {handlers.index(other_bot) + 1}**: Users: {other_user_count}, Groups: {other_group_count}")
        
        stats_message += "\n".join(other_stats)
        
        await event.reply(stats_message, file=AYU, buttons=[
            [Button.inline("ᴜsᴇʀs", data="user_stats"), Button.inline("ᴄʜᴀᴛs", data="group_stats")],
            [Button.inline("ᴏᴠᴇʀᴀʟʟ", data="overall_stats")]
        ])
    else:
        await event.reply("ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴍᴇɴᴜ.")

# Handle callback query
async def callback(event, bot):
    stats_collection = db_map[bot]['stats']
    data = event.data.decode('utf-8')
    if data == "user_stats":
        user_count = stats_collection.count_documents({'type': 'user'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs: {user_count}", buttons=buttons)
    elif data == "group_stats":
        group_count = stats_collection.count_documents({'type': 'group'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴄʜᴀᴛs: {group_count}", buttons=buttons)
    elif data == "overall_stats":
        user_count = stats_collection.count_documents({'type': 'user'})
        group_count = stats_collection.count_documents({'type': 'group'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs: {user_count}\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs: {group_count}", buttons=buttons)
    elif data == "back_to_stats":
        user_count = stats_collection.count_documents({'type': 'user'})
        group_count = stats_collection.count_documents({'type': 'group'})
        stats_message = f"⚔️ 𝗝𝗔𝗥𝗩𝗜𝗦 𝗕𝗢𝗧𝗦 𝗦𝗧𝗔𝗧𝗦 ⚔️\n\n"
        stats_message += f"**Bot {handlers.index(bot) + 1} Stats:**\n"
        stats_message += f"Users: {user_count}\nGroups: {group_count}\n\n"

        other_stats = []
        for other_bot in handlers:
            if other_bot != bot:
                other_stats_collection = db_map[other_bot]['stats']
                other_user_count = other_stats_collection.count_documents({'type': 'user'})
                other_group_count = other_stats_collection.count_documents({'type': 'group'})
                other_stats.append(f"**Bot {handlers.index(other_bot) + 1}**: Users: {other_user_count}, Groups: {other_group_count}")
        
        stats_message += "\n".join(other_stats)

        buttons = [
            [Button.inline("ᴜsᴇʀs", data="user_stats"), Button.inline("ᴄʜᴀᴛs", data="group_stats")],
            [Button.inline("ᴏᴠᴇʀᴀʟʟ", data="overall_stats")]
        ]
        await event.edit(stats_message, file=AYU, buttons=buttons)

# Broadcast command
async def broadcast(event, bot):
    stats_collection = db_map[bot]['stats']
    if event.sender_id == OWNER_ID:
        reply = await event.get_reply_message()
        message = event.pattern_match.group(1)

        if not message and not reply:
            await event.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.")
            return
        
        user_count = 0
        group_count = 0

        users = stats_collection.find({'type': 'user'})
        groups = stats_collection.find({'type': 'group'})
        
        for user in users:
            try:
                if reply:
                    await bot.send_message(user['id'], message or reply.message, file=reply.media)
                else:
                    await bot.send_message(user['id'], message)
                user_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is blocked
            except Exception as e:
                print(f"Error sending message to {user['id']}: {str(e)}")
        
        for group in groups:
            try:
                if reply:
                    await bot.send_message(group['id'], message or reply.message, file=reply.media)
                else:
                    await bot.send_message(group['id'], message)
                group_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is removed from the group
            except Exception as e:
                print(f"Error sending message to {group['id']}: {str(e)}")
        
        await event.reply(f"Broadcast has been completed.\n\nMessage sent to:\n- {user_count} users\n- {group_count} chats")
    else:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ.")

# Register Event Handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))(lambda e, b=handler: logs(e, b))
    handler.on(events.NewMessage(incoming=True))(lambda e, b=handler: track_stats(e, b))
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))(lambda e, b=handler: check_stats(e, b))
    handler.on(events.CallbackQuery)(lambda e, b=handler: callback(e, b))
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))(lambda e, b=handler: broadcast(e, b))
