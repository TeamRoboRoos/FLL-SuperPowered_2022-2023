from modules.components.drivebase import driveBase
from modules.components.forklift import forklift
from modules.components.lightSensor import lightSensor
from modules.components.runButton import runButton
from modules.components.runState import runState
from modules.components.motor import motor

from regionals.windmillRun import windmillRun
from regionals.powerPlantRun import powerPlantRun

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
        self.menu = {"left": []}

        self.stopList = []

        if self.name == "artemis":
            self.SPEED_LIST_COUNT = 2000
            self.ACCELERATION = 250
            self.STARTSPEED = 50
            self.TURN_SPEED_MIN = 20
            self.TURN_SPEED_MAX = 180
            self.LIGHTCAL_CONF = "artemis.cal"

            self.Lmotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
            self.Rmotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
            self.LMmotor = motor(self, Port.C)
            self.RMmotor = motor(self, Port.B)

            # self.runButton = runButton(TouchSensor(Port))
            self.gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
            self.Llight = lightSensor(ColorSensor(Port.S3))
            self.Rlight = lightSensor(ColorSensor(Port.S4))

            self.lift = forklift(self, self.RMmotor, 11, 40, 8)
            self.drive = driveBase(self, DriveBase(self.Lmotor, self.Rmotor, 56, 104),
                                   self.Lmotor, self.Rmotor, self.gyro, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

            self.menu = {
                "runs": [["powerPlantRun", "windmillRun"], [powerPlantRun(self), windmillRun(self)]],
                "left": [self.lift.initPos, None],
                "utility": [["lightCal", "gyrodrift", "tyreClean"], [self.drive.lightCal, self.drive.gyroDrift, self.drive.tyreClean]],
                "pages": ["runs", "utility"]
            }

            self.stopList = [self.drive, self.lift, self.LMmotor, self.RMmotor]

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

            self.Lmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
            self.Rmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
            self.LMmotor = motor(self, Port.A)
            self.RMmotor = motor(self, Port.D)

            # self.runButton = runButton(TouchSensor(Port))
            self.gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
            self.Llight = lightSensor(ColorSensor(Port.S3))
            self.Rlight = lightSensor(ColorSensor(Port.S4))

            self.lift = forklift(self, motor(self,
                                             Port.D, gears=[[12, 20], [28, 20], [8, 40]]), 110)
            self.leftButton = self.lift.initPos

            self.drive = driveBase(self, DriveBase(self.Lmotor, self.Rmotor, 56, 104),
                                   self.Lmotor, self.Rmotor, self.gyro, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

            self.menu = {
                "runs": [["powerPlantRun", "windmillRun"], [powerPlantRun(self), windmillRun(self)]],
                "left": [self.lift.initPos, None],
                "utility": [["lightCal", "gyrodrift", "tyreClean"], [self.drive.lightCal, self.drive.gyroDrift, self.drive.tyreClean]],
                "pages": ["runs", "utility"]
            }

            self.stopList = [self.drive, self.lift, self.LMmotor, self.RMmotor]

            # self.xlift = forklift(Motor(Port.B))
            # self.ylift = forklift(Motor(Port.C))
            # self.lift = doubleForklift(self.xlift, self.ylift)
        else:
            self.ev3.screen.clear()
            self.ev3.screen.print("Unkown robot\nNo config found")
            while True:
                wait(100)

    def stop(self):
        for module in self.stopList:
            module.stop()
