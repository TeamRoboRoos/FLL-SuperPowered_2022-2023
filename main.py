#!/usr/bin/env pybricks-micropython
import sys
from modules.load_config import config
from modules.menu import menu


# Initialise config and main menu
config = config()

menu = menu(config, 20)
print("Started")

# Run menu loop
try:
    while True:
        menu.update()
except KeyboardInterrupt:
    # Effectively changes namespace to config
    # eg. config.drive.turnTo becomes drive.turnTo
    config.stop()
    contents = dir(config)
    for i in range(0, len(contents)):
        if "_" not in list(contents[i]):
            exec(contents[i] + " = config." + contents[i])
    sys.exit()
