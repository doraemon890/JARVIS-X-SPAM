import logging
from os import getenv
from telethon import TelegramClient
from JARVIS.data import FRIDAY

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Environment variables and constants
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Bot tokens
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

# Sudo users and owner ID
SUDO_USERS = list(map(int, getenv("SUDO_USERS", default="6757745933").split()))
SUDO_USERS.extend(FRIDAY)
OWNER_ID = int(getenv("OWNER_ID", default="7044783841"))
SUDO_USERS.append(OWNER_ID)

# Initialize Telegram clients
clients = []
for idx, bot_token in enumerate(BOT_TOKENS, start=1):
    if bot_token:
        client = TelegramClient(f'X{idx}', API_ID, API_HASH).start(bot_token=bot_token)
        clients.append(client)
        logging.info(f'Initialized bot X{idx}')

# Assign clients to specific variables for convenience
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients[:10]

