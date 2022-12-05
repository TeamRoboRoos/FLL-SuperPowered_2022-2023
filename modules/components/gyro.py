from pybricks.ev3devices import GyroSensor
from pybricks.iodevices import Ev3devSensor


class Gyro(GyroSensor):
    def __init__(self, port, direction, config):
        super().__init__(port, direction)
        self.a = Ev3devSensor(port)
        self.config = config
        self.calibrate()

    def calibrate(self):
        self.a.read("GYRO-CAL")  # type: ignore
        self.a.read("GYRO-ANG")  # type: ignore
        self.reset_angle(0)
