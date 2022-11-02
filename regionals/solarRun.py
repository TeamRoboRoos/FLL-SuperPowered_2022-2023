from threading import Thread


class solarRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        # self.xlift = config.xlift
        self.wait = config.timer.wait

    def run(self):
        self.drive.moveDist(550)
        self.drive.moveLight(self.config.Llight, [0, 5])
        self.drive.lineReset()
        self.drive.setHead(-90)

        self.drive.moveDist(70, heading=-90)
        self.drive.turnTo(180)
        self.drive.moveDist(-350, heading=180)

        self.config.LMmotor.run_angle(800, 500)

        self.drive.turnTo(-60)
        self.drive.moveDist(200, heading=-60)
        self.drive.turnTo(-90)
        self.config.RMmotor.run_angle(10000, 5800)

        self.drive.moveDist(300, heading=-90)
        self.config.RMmotor.run_angle(1000, -4400)
        self.drive.moveDist(150, heading=-90)

        self.config.state.setState(1)
