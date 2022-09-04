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
    for i in range(0, len(dir(config))):
        if "_" not in list(dir(config)[i]):
            exec(dir(config)[i] + " = config." + dir(config)[i])
    sys.exit()
