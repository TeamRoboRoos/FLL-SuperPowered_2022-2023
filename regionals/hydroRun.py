from threading import Thread


class hydroRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(90)
        self.drive.moveDist(425, heading=90)
        self.drive.turnTo(45)
        self.drive.moveDist(180, heading=45)

        self.config.LMmotor.run_angle(500, 400)
        self.config.RMmotor.run_angle(100, 150)
        self.drive.moveDist(-80)
        self.config.RMmotor.run_angle(500, 200)
        self.drive.moveDist(80)
        self.config.RMmotor.run_angle(500, -350)
        self.drive.moveDist(-400)
        self.drive.moveDist(-300, down=False, heading=90)

        self.config.state.setState(1)
