import os
import sys
from ..log import Log

def get_path(name):
    return os.path.join(os.path.dirname(__file__), "files", name + ".txt")

class Database:
    def save_click_to(name, x, y, t):
        with open(get_path(name), "a") as f:
            f.write(f"{x} {y} {t}\n")

    def rename(old_name, new_name):
        with open(get_path(old_name), "r") as source, open(get_path(new_name), "w") as target:
            target.write(source.read())
        
        os.remove(get_path(old_name))

    def get_all_names():
        path = os.path.join(os.path.dirname(__file__), "files")
        return os.listdir(path)

    def delete(name):
        os.remove(get_path(name))

    def show(name):
        with open(get_path(name), "r") as f:
            lines = f.readlines()
        return lines
    
    def get_clicks(name):
        lines = Database.show(name)
        return [
            (int(line.split(" ")[0]), int(line.split(" ")[1]), float(line.split(" ")[2])) for line in lines
        ]
    
    def clear():
        for file in Database.get_all_names():
            os.remove(
                os.path.join(os.path.dirname(__file__), "files", file)
            )