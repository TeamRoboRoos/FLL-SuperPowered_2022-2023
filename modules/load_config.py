from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from modules.components.tools import RunState, Timer
from os import popen


class PortError(Exception):
    def __init__(self, message):
        print(message)
        self.message = message
        super().__init__(message)

# Holds information for one or more robots


class config:
    def __init__(self):
        # Gets hostname to identify robot
        self.ev3 = EV3Brick()
        self.state = RunState()
        self.runButton = None
        self.menu = {"left": []}
        self.menuSelector = None
        self.leftpage = None

        self.stopList = []
        self.display = []

        self.timer = Timer(self)
        self.name = popen('hostname').read().strip()

    def stop(self):
        for module in self.stopList:
            module.stop()

    def init(self, type, port, *args, **kwargs):
        try:
            return type(port, *args, **kwargs)
        except:
            print("hii")
            message = "{}\nOn port {}".format(type.__name__, port)
            raise PortError(message)


def load_config():
    name = popen('hostname').read().strip()
    message = ""
    try:
        robot_config = getattr(
            getattr(__import__("configurations." + name), name), name)()
    except PortError as e:
        message = e.message
        print("hi")
    except:
        if message == "":
            message = "Unkown robot\nNo config found"
    else:
        return robot_config
    return message
