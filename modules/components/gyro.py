from pybricks.ev3devices import GyroSensor


class Gyro(GyroSensor):
    def __init__(self, config, port, direction):
        super().__init__(port, direction)
        self.config = config
