import argparse
import os

if os.name == "nt":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

from clicker.src.commands.help import help
from clicker.src.commands.list import list_
from clicker.src.commands.play import play
from clicker.src.commands.record import record
from clicker.src.commands.rename import rename
from clicker.src.commands.delete import delete
from clicker.src.commands.show import show
from clicker.src.commands.clear import clear
from clicker.src.commands.repeat import repeat
from clicker.src.log import Log

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("args", nargs="*")

args = parser.parse_args()

match args.command:
    case "help":
        help(args.args)
    case "list":
        list_(args.args)
    case "play":
        play(args.args)
    case "record":
        record(args.args)
    case "rename":
        rename(args.args)
    case "delete":
        delete(args.args)
    case "show":
        show(args.args)
    case "clear":
        clear(args.args)
    case "repeat":
        repeat(args.args)
    case _:
        Log.error("unknown command")
        exit(1)