#!/usr/bin/env pybricks-micropython
import sys
from threading import Thread
from modules import load_config
from modules.menu import menu


# Initialise config and main menu
config = load_config.load_config()

menu = menu(config, 20)
print("Started")

# Run menu loop
try:
    while True:
        menu.update()
except KeyboardInterrupt:
    # Effectively changes namespace to config
    # eg. config.drive.turnTo becomes drive.turnTo
    config.state.setState(3)  # type: ignore
    config.stop()  # type: ignore
    Thread(target=menu.infoLoop).start()
    contents = dir(config)
    for i in range(0, len(contents)):
        if "_" not in list(contents[i]):
            exec(contents[i] + " = config." + contents[i])
    sys.exit()
