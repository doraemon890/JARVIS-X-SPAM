import logging
from os import getenv
from telethon import TelegramClient
from JARVIS.data import FRIDAY

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 24509589
API_HASH = "717cf21d94c4934bcbe1eaa1ad86ae75"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
MONGO_DB_URI = getenv("MONGO_DB_URI")


BOT_TOKENS = [
    getenv("BOT_TOKEN", default=None),
    getenv("BOT_TOKEN2", default=None),
    getenv("BOT_TOKEN3", default=None),
    getenv("BOT_TOKEN4", default=None),
    getenv("BOT_TOKEN5", default=None),
    getenv("BOT_TOKEN6", default=None),
    getenv("BOT_TOKEN7", default=None),
    getenv("BOT_TOKEN8", default=None),
    getenv("BOT_TOKEN9", default=None),
    getenv("BOT_TOKEN10", default=None),
]

OWNER_ID = int(getenv("OWNER_ID", default="7044783841"))

clients = []
for idx, bot_token in enumerate(BOT_TOKENS, start=1):
    if bot_token:
        client = TelegramClient(f'X{idx}', API_ID, API_HASH).start(bot_token=bot_token)
        clients.append(client)
        logging.info(f'Initialized bot X{idx}')

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients[:10]

