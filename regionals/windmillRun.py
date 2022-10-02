from threading import Thread


class windmillRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.flipper = config.RMmotor

    def run(self):
        self.drive.moveDist(580, heading=0)
        self.drive.moveDost(-60, heading=0)
        self.drive.turnTo(-40)
        self.drive.moveLight(self.config.Rlight, [0, 10], heading=-40)
        self.drive.turnTo(45)

        self.config.state.setState(1)
