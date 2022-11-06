#!/usr/bin/env pybricks-micropython
import sys
from threading import Thread
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
    config.state.setState(0)
    Thread(target=menu.infoLoop).start()
    contents = dir(config)
    for i in range(0, len(contents)):
        if "_" not in list(contents[i]):
            exec(contents[i] + " = config." + contents[i])
    sys.exit()
