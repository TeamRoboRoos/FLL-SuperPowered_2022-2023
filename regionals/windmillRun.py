from threading import Thread


class windmillRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.flipper = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(590, heading=0)
        self.drive.moveDist(-80, heading=0, turn=False)
        self.drive.turnTo(-45)
        self.drive.moveLight(self.config.Rlight, [0, 10], heading=-40)
        self.drive.moveDist(140, heading=-40)
        self.drive.turnTo(45)

        self.drive.moveDist(80, heading=45)
        self.wait(500)
        self.drive.moveDist(-50, heading=45)
        self.wait(800)
        self.drive.moveDist(80, heading=45)
        self.wait(500)
        self.drive.moveDist(-50, heading=45)
        self.wait(800)
        self.drive.moveDist(80, heading=45)
        self.wait(500)
        self.drive.moveDist(-50, heading=45)
        self.drive.setHead(45)

        self.drive.moveDist(-170)
        self.drive.turnTo(-45)
        self.drive.moveDist(293, heading=-45)
        self.flipper.run_angle(900, 530)
        self.flipper.stop()
        self.flipper.run_angle(-900, 530)
        self.flipper.stop()
        self.drive.moveDist(-1100)

        self.config.state.setState(1)
