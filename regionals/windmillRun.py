from threading import Thread
from pybricks.tools import wait


class windmillRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.flipper = config.RMmotor

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(580, heading=0)
        self.drive.moveDist(-80, heading=0, turn=False)
        self.drive.turnTo(-45)
        self.drive.moveLight(self.config.Rlight, [0, 10], heading=-40)
        self.drive.moveDist(140, heading=-40)
        self.drive.turnTo(45)

        for i in range(0, 3):
            self.drive.moveDist(80, heading=45)
            wait(500)
            self.drive.moveDist(-50, heading=45)
            wait(800)

        self.drive.moveDist(-190)
        self.drive.turnTo(-45)
        self.drive.moveDist(290, heading=-45)
        self.flipper.run_angle(400, 500)
        self.flipper.stop()

        self.config.state.setState(1)
