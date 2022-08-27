#!/usr/bin/env pybricks-micropython
import sys
from modules.load_config import config
from modules.menu import menu


Config = config()

menu = menu(Config)

try:
    while True:
        menu.update()
except KeyboardInterrupt:
    sys.exit()
