#!/usr/bin/env pybricks-micropython
import sys
from modules.load_config import config
from modules.menu import menu


config = config()

menu = menu(config)

try:
    while True:
        menu.update()
except KeyboardInterrupt:
    sys.exit()
