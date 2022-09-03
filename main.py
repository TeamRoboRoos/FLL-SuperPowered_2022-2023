#!/usr/bin/env pybricks-micropython
import sys
from modules.load_config import config
from modules.menu import menu


config = config()

menu = menu(config, False)

try:
    while True:
        menu.update()
except KeyboardInterrupt:
    for i in range(5, len(dir(config))):
        exec(dir(config)[i] + " = config." + dir(config)[i])
    sys.exit()
