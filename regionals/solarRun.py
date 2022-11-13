from threading import Thread


class solarRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        # self.xlift = config.xlift
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-74)
        self.drive.moveDist(550)
        self.drive.moveLight(self.config.Llight, [0, 5])
        self.drive.turnTo(-90)
        self.drive.lineReset()
        self.drive.setHead(-90)

        self.drive.moveDist(70, heading=-90)
        self.drive.spinTo(180)
        self.drive.moveLight(self.config.Llight, [0, 5], heading=180)
        self.drive.moveDist(-400, heading=180)

        self.config.LMmotor.run_angle(800, 1000)

        self.drive.moveDist(-70, heading=180)
        self.drive.spinTo(-90)
        self.drive.moveDist(100, heading=-90)

        Thread(target=self.config.LMmotor.run_angle, args=[800, -1000]).start()
        self.config.RMmotor.run_angle(10000, 3400)

        self.drive.lineFollower(distance=300, mode=2,
                                speed=140, kp=0.3, ki=0, kd=0)

        self.config.RMmotor.run_angle(10000, -2000)

        self.drive.lineFollower(mode=2, speed=140, kp=0.3, ki=0, kd=0)
        self.drive.setHead(-90)
        self.drive.moveDist(20)

        Thread(target=self.config.RMmotor.run_angle,
               args=[10000, -1500]).start()

        for _ in range(0, 3):
            self.config.LMmotor.run_angle(800, 1000)
            self.config.LMmotor.run_angle(800, -1000)

        self.drive.moveDist(-40)

        self.drive.turnTo(-140)
        self.drive.moveDist(600, down=False, turn=False, heading=-155)

        self.config.state.setState(1)
