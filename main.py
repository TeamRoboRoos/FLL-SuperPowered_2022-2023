#!/usr/bin/env pybricks-micropython
import sys
from modules.load_config import config
from modules.menu import menu


config = config()

menu = menu(config, False)
print("Started")

try:
    while True:
        menu.update()
except KeyboardInterrupt:
    config.stop()
    contents = dir(config)
    for i in range(0, len(contents)):
        if "_" not in list(contents[i]):
            exec(contents[i] + " = config." + contents[i])
    sys.exit()
