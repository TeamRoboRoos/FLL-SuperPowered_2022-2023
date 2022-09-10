from modules.components.drivebase import driveBase
from modules.components.forklift import forklift
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

        if self.name == "artemis":
            self.SPEED_LIST_COUNT = 2000
            self.ACCELERATION = 250
            self.STARTSPEED = 50
            self.TURN_SPEED_MIN = 20
            self.TURN_SPEED_MAX = 180
            self.LIGHTCAL_CONF = "artemis.cal"

            self.Lmotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
            self.Rmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
            self.LMmotor = Motor(Port.B)
            self.RMmotor = Motor(Port.D)

            # self.runButton = runButton(TouchSensor(Port))
            self.gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
            self.Llight = lightSensor(ColorSensor(Port.S3))
            self.Rlight = lightSensor(ColorSensor(Port.S4))

            self.lift = forklift(self, self.RMmotor, 11, 40, 8)
            self.drive = driveBase(self, DriveBase(self.Lmotor, self.Rmotor, 56, 104),
                                   self.Lmotor, self.Rmotor, self.gyro, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

            self.menu = {
                "runs": [["run1", "run2", "run3"], [run1(self), run2(self), run3(self)]],
                "utility": [["lightCal", "gyrodrift", "tyreClean"], [self.drive.lightCal, self.drive.gyroDrift, self.drive.tyreClean]],
                "pages": ["runs", "utility"]
            }

            # self.xlift = forklift(Motor(Port.B))
            # self.ylift = forklift(Motor(Port.C))
            # self.lift = doubleForklift(self.xlift, self.ylift)

        elif self.name == "apollo":
            self.SPEED_LIST_COUNT = 2000
            self.ACCELERATION = 250
            self.STARTSPEED = 50
            self.TURN_SPEED_MIN = 20
            self.TURN_SPEED_MAX = 180
            self.LIGHTCAL_CONF = "apollo.cal"

            self.Lmotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
            self.Rmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
            self.LMmotor = Motor(Port.B)
            self.RMmotor = Motor(Port.D)

            # self.runButton = runButton(TouchSensor(Port))
            self.gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
            self.Llight = lightSensor(ColorSensor(Port.S3))
            self.Rlight = lightSensor(ColorSensor(Port.S4))

            self.lift = forklift(self, self.RMmotor, 11, 40, 8)
            self.drive = driveBase(self, DriveBase(self.Lmotor, self.Rmotor, 56, 104),
                                   self.Lmotor, self.Rmotor, self.gyro, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

            self.menu = {
                "runs": [["run1", "run2", "run3"], [run1(self), run2(self), run3(self)]],
                "utility": [["lightCal", "gyrodrift", "tyreClean"], [self.drive.lightCal, self.drive.gyroDrift, self.drive.tyreClean]],
                "pages": ["runs", "utility"]
            }

            # self.xlift = forklift(Motor(Port.B))
            # self.ylift = forklift(Motor(Port.C))
            # self.lift = doubleForklift(self.xlift, self.ylift)
        else:
            self.ev3.screen.clear()
            self.ev3.screen.print("Unkown robot\nNo config found")
            while True:
                wait(100)
