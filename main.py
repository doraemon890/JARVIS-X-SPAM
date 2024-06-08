import sys
import glob
import asyncio
import logging
import importlib
import urllib3
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Disable warnings from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to load plugins
def load_plugins(plugin_name):
    path = Path(f"JARVIS/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"JARVIS.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[f"JARVIS.modules.{plugin_name}"] = load
    print(f"FRIDAY has Imported {plugin_name}")

# Load all plugins from the modules directory
def load_all_plugins():
    files = glob.glob("JARVIS/modules/*.py")
    for name in files:
        with open(name) as file:
            plugin_name = Path(file.name).stem
            load_plugins(plugin_name)

# Start all Telegram clients
async def start_clients():
    clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

if __name__ == "__main__":
    # Load all plugins
    load_all_plugins()

    # Print deployment success message
    print("\n𝐉𝐀𝐑𝐕𝐈𝐒 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @JARVIS_V2")

    # Start event loop and run clients
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_clients())
