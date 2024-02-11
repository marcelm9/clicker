from sys import exit
from pynput.mouse import Listener
from pynput import mouse
from pynput import keyboard
from ..database.database import Database
from ..log import Log
import time

name = ...
t = -1

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker record <name>")
    exit(1)

def on_click(x, y, button, pressed):
    if not pressed:
        return

    if button == mouse.Button.right:
        Log.info("Stopping")
        return False

    global name, t

    if t == -1:
        time_ = time.time()
    else:
        time_ = t

    now = time.time()
    passed = now - time_
    t = now

    Database.save_click_to(name, x, y, passed)
    Log.info(f"Saved click ({x}, {y}, {passed}) to '{name}'")

def record(args):
    global name

    if len(args) != 1:
        synopsis()

    name = args[0]

    if name + ".txt" in Database.get_all_names():
        Log.error(f"File with name '{name}' already exists")
        exit(1)

    with Listener(on_click=on_click) as listener:
        Log.info("Starting")
        listener.join()
