from modules.components.drivebase import driveBase
from modules.components.lightSensor import lightSensor
from modules.components.runButton import runButton
from modules.components.runState import runState

from test.run1 import run1
from test.run2 import run2
from test.run3 import run3

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font, SoundFile, ImageFile

from os import popen


class config:
    def __init__(self):
        self.name = popen('hostname').read().strip()

        self.ev3 = EV3Brick()
        self.state = runState()
        self.runButton = None
        self.leftButton = None

        if self.name == "ev3dev":
            self.SPEED_LIST_COUNT = 2000
            self.ACCELERATION = 250
            self.STARTSPEED = 50
            self.TURN_SPEED_MIN = 20
            self.TURN_SPEED_MAX = 180
            self.LIGHTCAL_CONF = "ev3dev.cal"

            self.Lmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
            self.Rmotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
            self.LMmotor = Motor(Port.A)
            self.RMmotor = Motor(Port.C)

            # self.runButton = runButton(TouchSensor(Port))
            self.gyro = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)
            self.Llight = lightSensor(ColorSensor(Port.S4))
            self.Rlight = lightSensor(ColorSensor(Port.S3))

            self.drive = driveBase(self, DriveBase(self.Lmotor, self.Rmotor, 78.4, 104),
                                   self.Lmotor, self.Rmotor, self.gyro, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

            self.menu = {
                "runs": [["run1", "run2", "run3"], [run1(self), run2(self), run3(self)]],
                "utility": [["lightCal", "gyrodrift", "tyreClean"], [self.drive.lightCal, self.drive.gyroDrift, self.drive.tyreClean]],
                "pages": ["runs", "utility"]
            }

            # self.xlift = forklift(Motor(Port.B))
            # self.ylift = forklift(Motor(Port.C))
            # self.lift = doubleForklift(self.xlift, self.ylift)
