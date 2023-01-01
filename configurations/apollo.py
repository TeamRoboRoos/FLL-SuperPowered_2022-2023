from pybricks.parameters import Port, Direction, Color

from worlds.powerPlantRun import powerPlantRun
from worlds.windmillRun import windmillRun
from worlds.solarRun import solarRun
from worlds.oilRun import oilRun
from worlds.hydroRun import hydroRun
from worlds.toyRun import toyRun

from modules.components.drivebase import DriveBaseFull
from modules.components.lightSensor import LightSensor
from modules.components.menuSelector import MenuSelector
from modules.components.gyro import Gyro
from modules.components.tools import RunState, Timer
from modules.components.motor import Motor

from modules.load_config import config


class apollo(config):
    def hydroRunResetArm(self):
        self.RMmotor.run_time(100, 400)

    def __init__(self):
        super().__init__()
        self.SPEED_LIST_COUNT = 2000
        self.ACCELERATION = 400
        self.STARTSPEED = 60
        self.TURN_SPEED_MIN = 20
        self.TURN_SPEED_MAX = 240
        self.LIGHTCAL_CONF = "apollo.cal"

        self.Lmotor = self.init(
            Motor, Port.A, self, Direction.COUNTERCLOCKWISE)
        self.Rmotor = self.init(
            Motor, Port.C, self, Direction.COUNTERCLOCKWISE)
        self.LMmotor = self.init(Motor, Port.B, self)
        self.RMmotor = self.init(Motor, Port.D, self)

        # self.runButton = runButton(TouchSensor(Port))
        self.gyro = self.init(Gyro, Port.S4, Direction.CLOCKWISE, self)
        self.Llight = self.init(LightSensor, Port.S2)
        self.Rlight = self.init(LightSensor, Port.S1)

        self.menuSelector = self.init(MenuSelector, Port.S3, [
                                      Color.BLACK, Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.WHITE], Color.BROWN, self.state)
        self.useMenuSelector = True
        self.leftpage = "runs"

        # self.lift = forklift(self, motor(self,
        #                                  Port.D, gears=[[12, 20], [28, 20], [8, 40]]), 110)

        self.drive = DriveBaseFull(self, self.Lmotor, self.Rmotor, self.gyro,
                                   56, 104, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

        self.menu = {
            "runs": [powerPlantRun(self), windmillRun(self), solarRun(self), oilRun(self), hydroRun(self), toyRun(self)],
            "left": [None, None, None, None, None, self.hydroRunResetArm],
            "utility": [self.drive.lightCal, self.gyro.calibrate, self.drive.tyreClean, self.drive.blank, self.menuSelector.toggle],
            "utility_name": ["LightCal", "gyroCal", "tyreClean", "blank", "toggleMenuSelector"],
            "pages": ["runs", "utility"]
        }

        self.display = [self.drive.getHead,
                        self.Llight.readLight, self.Rlight.readLight, self.menuSelector.color]
        self.stopList = [self.drive, self.LMmotor, self.RMmotor]

        # self.xlift = forklift(Motor(Port.B))
        # self.ylift = forklift(Motor(Port.C))
        # self.lift = doubleForklift(self.xlift, self.ylift)
