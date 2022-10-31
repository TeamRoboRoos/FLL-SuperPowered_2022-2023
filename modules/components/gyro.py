from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Direction

class Gyro(GyroSensor):
    def __init__(self, port, positive_direction=Direction.CLOCKWISE):
        super().__init__(port, positive_direction)
