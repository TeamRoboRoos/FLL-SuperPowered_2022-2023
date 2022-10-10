from pybricks._common import Motor
from pybricks.parameters import Direction, Stop
import pybricks.tools


class motor():
    def __init__(self, config, port,
                 positive_direction=Direction.CLOCKWISE,
                 gears=None,
                 reset_angle=True):
        self.config = config
        self.m = Motor(port, positive_direction, gears, reset_angle)

    def angle(self):
        return self.m.angle()

    def speed(self):
        return self.m.speed()

    def reset_angle(self, angle):
        self.m.reset_angle(angle)

    def hold(self):
        self.m.hold()

    def run(self, speed):
        self.m.run(speed)

    def run_time(self, speed, time, then=Stop.HOLD, wait=True):
        self.m.run_time(speed, time, then, False)
        while wait and self.m.control.done() == False and self.config.state.getState() == 0:
            pybricks.tools.wait(10)

    def run_angle(self, speed, rotation_angle, then=Stop.HOLD, wait=True):
        self.m.run_angle(speed, rotation_angle, then, False)
        while wait and self.m.control.done() == False and self.config.state.getState() == 0:
            pybricks.tools.wait(10)

    def run_target(self, speed, target_angle, then=Stop.HOLD, wait=True):
        self.m.run_target(speed, target_angle, then, False)
        while wait and self.m.control.done() == False and self.config.state.getState() == 0:
            pybricks.tools.wait(10)

    def run_until_stalled(self, speed, then=Stop.COAST, duty_limit=None):
        self.m.run_until_stalled(speed, then, duty_limit)
        while self.m.control.done() == False and self.config.state.getState() == 0:
            pybricks.tools.wait(10)

    def track_target(self, target_angle):
        self.m.track_target(target_angle)

    def dc(self, duty):
        self.m.dc(duty)

    def stop(self):
        self.m.stop()
