import sys
import glob
import asyncio
import logging
import importlib
import urllib3

from pathlib import Path
from config import (
    X1, X2, X3, X4, X5, 
    X6, X7, X8, X9, X10
)

# Configure logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', 
    level=logging.WARNING
)

# Disable urllib3 warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    """Load a plugin by its name."""
    path = Path(f"JARVIS/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"JARVIS.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[f"JARVIS.modules.{plugin_name}"] = load
    print(f"FRIDAY has Imported {plugin_name}")


def import_plugins():
    """Import all plugins from the modules directory."""
    files = glob.glob("JARVIS/modules/*.py")
    for file_path in files:
        plugin_name = Path(file_path).stem
        load_plugins(plugin_name)


async def run_all():
    """Run all configured modules until disconnected."""
    await asyncio.gather(
        X1.run_until_disconnected(),
        X2.run_until_disconnected(),
        X3.run_until_disconnected(),
        X4.run_until_disconnected(),
        X5.run_until_disconnected(),
        X6.run_until_disconnected(),
        X7.run_until_disconnected(),
        X8.run_until_disconnected(),
        X9.run_until_disconnected(),
        X10.run_until_disconnected()
    )


def main():
    """Main entry point for the script."""
    import_plugins()
    print("\n𝐉𝐀𝐑𝐕𝐈𝐒 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @JARVIS_V2")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_all())

