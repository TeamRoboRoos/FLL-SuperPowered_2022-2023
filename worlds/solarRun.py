from threading import Thread


class solarRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        # self.xlift = config.xlift
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-90)
        # self.drive.moveDist(350)
        # self.drive.turnTo(-67)
        # self.drive.moveDist(300, heading=-67)
        self.drive.moveDist(450)
        self.drive.turnTo(-55)
        self.drive.moveDist(300, heading=-55)

        self.drive.moveLight(self.config.Llight, [0, 5])
        self.drive.turnTo(-90)
        # self.drive.lineReset()
        # self.drive.setHead(-90)

        self.drive.moveDist(80, heading=-90)
        self.drive.turnTo(180)

        # self.drive.moveLight(self.config.Llight, [0, 5], heading=180)
        self.drive.moveDist(-350, heading=180)

        self.config.LMmotor.run_angle(1000, 500)
        Thread(target=self.config.LMmotor.run_angle, args=[1000, 250]).start()

        self.drive.moveDist(-50, heading=180)
        self.drive.turnTo(-90)
        self.drive.moveDist(130, heading=-90)
        # self.drive.lineFollower(distance=90, mode=2,
                                # speed=140, kp=0.3, ki=0, kd=0)

        self.config.RMmotor.run_angle(1000, 690)
        Thread(target=self.config.LMmotor.run_angle, args=[1000, -750]).start()

        self.drive.lineFollower(distance=300, mode=2,
                                speed=120, kp=0.3, ki=0, kd=0)

        self.config.RMmotor.run_angle(1000, -420)

        self.drive.lineFollower(mode=2, speed=120, kp=0.3, ki=0, kd=0)
        # self.drive.setHead(-90)
        self.drive.moveDist(20)

        Thread(target=self.config.RMmotor.run_angle,
               args=[10000, -450]).start()

        for _ in range(0, 3):
            self.config.LMmotor.run_angle(1000, 400)
            self.config.LMmotor.run_angle(1000, -400)

        self.drive.moveDist(-40)

        self.drive.turnTo(-136)
        self.drive.moveDist(600, down=False, turn=False, heading=-155)

        self.config.state.setState(1)
