from threading import Thread

from pybricks.parameters import Stop


class hydroRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        # self.drive.moveDist(445, heading=90)
        # self.drive.turnTo(45)
        # self.drive.moveDist(200, heading=45)

        # self.config.LMmotor.run_angle(500, 400)
        # self.config.RMmotor.run_angle(100, 150)
        # self.drive.moveDist(-80)
        # self.config.RMmotor.run_angle(500, 200)
        # self.drive.moveDist(80)
        # self.config.RMmotor.run_angle(500, -350)
        # self.drive.moveDist(-400)
        # self.drive.moveDist(-300, down=False, heading=90)
        self.drive.setHead(0)
        self.arm.run_time(100, 1000, then=Stop.BRAKE, wait=False)

        self.drive.moveDist(480, heading=0)
        self.drive.turnTo(50)
        self.drive.moveDist(320, heading=50)
        self.arm.run_angle(200, -100)
        self.drive.moveDist(-60, heading=50)
        self.arm.run_angle(200, -60)
        self.drive.moveDist(50)
        self.arm.run_angle(200, 170)
        self.drive.moveDist(-560, heading=50, down=True)

        self.drive.turnTo(0)
        self.drive.moveDist(135, heading=0)
        self.drive.moveDist(-300, down=False)

        self.config.state.setState(1)
