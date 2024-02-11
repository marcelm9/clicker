from sys import exit
from ..log import Log
from ..database.database import Database
import time
from pynput.mouse import Button, Controller

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker play <name>")
    exit(1)

def play(args):
    if len(args) != 1:
        synopsis()

    name = args[0]

    if name + ".txt" not in Database.get_all_names():
        Log.error(f"No file with name '{name}' found in database")
        exit(1)

    # replay clicks
    mouse = Controller()
    clicks = Database.get_clicks(name)
    Log.info(f"Replaying mouse clicks from '{name}'")
    for click in clicks:
        time.sleep(click[2])
        mouse.position = (click[0], click[1])
        mouse.click(Button.left)
    Log.info("Replay done")
