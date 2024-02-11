from rich import print

red = "[red]"
purple = "[purple]"
blue = "[blue]"
cyan = "[bright_cyan]"
clear = "[/]"
white = "[white]"

class Log:
    def info(msg):
        print(f"{white}\[{purple}clicker{white}]\[{blue}info{white}]{clear * 4} {msg}")

    def error(msg):
        print(f"{white}\[{purple}clicker{white}]\[{red}error{white}]{clear * 4} {msg}")

    def ask(msg):
        print(f"{white}\[{purple}clicker{white}]\[{cyan}ask{white}]{clear * 4} {msg}", end="")
        return input()
