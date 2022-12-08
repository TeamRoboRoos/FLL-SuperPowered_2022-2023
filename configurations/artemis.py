from pybricks.parameters import Port, Direction, Color

from worlds.powerPlantRun import powerPlantRun
from worlds.windmillRun import windmillRun
from worlds.solarRun import solarRun
from worlds.oilRun import oilRun
from worlds.toyRun import toyRun

from modules.components.drivebase import DriveBaseFull
from modules.components.lightSensor import LightSensor
from modules.components.menuSelector import MenuSelector
from modules.components.forklift import Forklift
from modules.components.gyro import Gyro
from modules.components.tools import RunState, Timer
from modules.components.motor import Motor

from modules.load_config import config

SPEED_LIST_COUNT = 2000
ACCELERATION = 380
STARTSPEED = 60
TURN_SPEED_MIN = 20
TURN_SPEED_MAX = 200
LIGHTCAL_CONF = "apollo.cal"

class apollo(config):
    def __init__(self):
        self.SPEED_LIST_COUNT = 2000
        self.ACCELERATION = 380
        self.STARTSPEED = 60
        self.TURN_SPEED_MIN = 20
        self.TURN_SPEED_MAX = 200
        self.LIGHTCAL_CONF = "artemis.cal"

        self.Lmotor = self.init(
            Motor, Port.B, self, Direction.COUNTERCLOCKWISE)
        self.Rmotor = self.init(
            Motor, Port.C, self, Direction.COUNTERCLOCKWISE)
        self.LMmotor = self.init(Motor, Port.A, self)
        self.RMmotor = self.init(Motor, Port.D, self)

        # self.runButton = runButton(TouchSensor(Port))
        self.gyro = self.init(Gyro, Port.S1, Direction.CLOCKWISE, self)
        self.Llight = self.init(LightSensor, Port.S3)
        self.Rlight = self.init(LightSensor, Port.S4)

        self.lift = Forklift(self, self.RMmotor, 11, 40, 8)
        self.drive = DriveBaseFull(self, self.Lmotor, self.Rmotor, self.gyro,
                                   56, 104, self.runButton, Llight=self.Llight, Rlight=self.Rlight)

        self.menu = {
            "runs": [powerPlantRun(self), windmillRun(self), solarRun(self), oilRun(self), toyRun(self)],
            "left": [None, None, None, None, None],
            "utility": [self.drive.lightCal, self.gyro.calibrate, self.drive.tyreClean, self.drive.blank],
            "utility_name": ["LightCal", "gyroCal", "tyreClean", "blank"],
            "pages": ["runs", "utility"]
        }

        self.display = [self.drive.getHead,
                        self.Llight.readLight, self.Rlight.readLight]
        self.stopList = [self.drive, self.lift, self.LMmotor, self.RMmotor]

        # self.xlift = forklift(Motor(Port.B))
        # self.ylift = forklift(Motor(Port.C))
        # self.lift = doubleForklift(self.xlift, self.ylift)
