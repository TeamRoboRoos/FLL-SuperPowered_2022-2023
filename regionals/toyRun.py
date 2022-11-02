from threading import Thread


class toyRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(220, heading=0)

        self.drive.turnTo(25)
        self.drive.moveDist(620)
        self.drive.turnTo(0)

        self.drive.moveDist(150, heading=0)

        self.drive.moveDist(-222, heading=0)
        self.drive.spinTo(90)

        self.drive.lineFollower(mode=1, speed=180, kp=0.3, ki=0, kd=0)
        self.drive.setHead(90)

        self.drive.moveLight(self.config.Rlight, [0, 10], heading=90)
        self.drive.moveDist(270, heading=90)
        self.drive.turnTo(130)

        self.drive.moveDist(80, heading=135)

        self.drive.moveDist(-100)
        self.drive.turnTo(90)
        self.drive.moveDist(400)
        self.drive.spinTo(180)

        self.drive.moveDist(-150)
        self.drive.turnTo(160)

        self.config.state.setState(1)
