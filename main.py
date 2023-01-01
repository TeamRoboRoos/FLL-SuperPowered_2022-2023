#!/usr/bin/env pybricks-micropython
import sys
from threading import Thread
from modules import load_config
from modules.menu import menu
from pybricks.hubs import EV3Brick


# Initialise config and main menu
config = load_config.load_config()
if type(config) == str:
    ev3 = EV3Brick()
    ev3.speaker.beep(600, 1000)
    ev3.screen.clear()
    ev3.screen.print(config)
    while len(ev3.buttons.pressed()) == 0:  # type: ignore
        pass
    sys.exit()

menu = menu(config, 100)
print("{} started with {}V".format(
    config.name.title(), config.ev3.battery.voltage()))  # type: ignore

# Run menu loop
try:
    while True:
        menu.update()
except KeyboardInterrupt:
    # Effectively changes namespace to config
    # eg. config.drive.turnTo becomes drive.turnTo
    config.state.setState(3)  # type: ignore
    config.stop()  # type: ignore
    config.ev3.screen.clear()  # type: ignore
    Thread(target=menu.infoLoop).start()
    contents = dir(config)
    for i in range(0, len(contents)):
        if "_" not in list(contents[i]):
            exec(contents[i] + " = config." + contents[i])
    config.state.setState(1)  # type: ignore
    sys.exit()
