from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from modules.components.tools import RunState, Timer
from os import popen


# Holds information for one or more robots
class config:
    def __init__(self):
        # Gets hostname to identify robot
        self.ev3 = EV3Brick()
        self.state = RunState()
        self.runButton = None
        self.menu = {"left": []}
        self.menuSelector = None

        self.stopList = []
        self.display = []

        self.timer = Timer(self)

    def stop(self):
        for module in self.stopList:
            module.stop()

    def init(self, type, port, *args, **kwargs):
        try:
            return type(port, *args, **kwargs)
        except:
            self.ev3.screen.clear()
            self.ev3.screen.print(type.__name__, "\nOn port", port)
            self.ev3.speaker.beep(500, 2000)
            while True:
                wait(1000)

def load_config():
    name = popen('hostname').read().strip()
    try:
        exec("import configurations." + name + " as config")
    except:
        brick = EV3Brick()
        brick.screen.clear()
        brick.screen.print("Unkown robot\nNo config found")
        while True:
            wait(100)

    return config
