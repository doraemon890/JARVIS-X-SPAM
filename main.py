import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"JARVIS/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"JARVIS.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["JARVIS.modules." + plugin_name] = load
    print("FRIDAY has Imported " + plugin_name)


files = glob.glob("JARVIS/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\nE29594E2978CE2978BE297A6E2979DE2978CE2979EE297A5E2979DE2978CE2978BE297A6E2978CE29593
202020F09D969F20F09D9788F09D979EF09D978820F09D978EE28096F09D9788F09D979EF09D978820F09D979DE28096F09D9788F09D979EF09D978820F09D979DE28096F09D979EE28096F09D978EE28096F09D978820F09D979DE28096F09D9788F09D979EF09D978820F09D979DE28096F09D979EE28096F09D978EE28096F09D978820E2909620E29594E2978CE2978BE297A6E2979DE2978CE2979EE297A5E2979DE2978CE2978BE297A6E2978CE29593
")


async def main():
    await X1.run_until_disconnected()
    await X2.run_until_disconnected()
    await X3.run_until_disconnected()
    await X4.run_until_disconnected()
    await X5.run_until_disconnected()
    await X6.run_until_disconnected()
    await X7.run_until_disconnected()
    await X8.run_until_disconnected()
    await X9.run_until_disconnected()
    await X10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
