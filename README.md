# clicker
Tool for recording and replaying mouse clicks.

### installation
```bash
git clone https://github.com/marcelm9/clicker.git
cd clicker
pip install .
```

### commands
```bash
# display all commands
python -m clicker help

# list all replay files
python -m clicker list

# replay file
python -m clicker play <name>

# record new replay file
python -m clicker record <name>

# rename replay file
python -m clicker rename <old_name> <new_name>

# delete replay file
python -m clicker delete <name>
```
