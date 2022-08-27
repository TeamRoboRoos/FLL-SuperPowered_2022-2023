#!/usr/bin/env pybricks-micropython
from modules.load_config import config
from modules.menu import menu


config = config()

menu = menu(config.ev3, config.menu, config.runButton)
