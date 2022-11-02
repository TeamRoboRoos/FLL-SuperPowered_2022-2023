from pybricks.ev3devices import GyroSensor
from threading import Thread

class gyroSensor(GyroSensor):
    cal = 0
    ang = 0

    def __init__(self, config, port, direction):
        super().__init__(port, direction)
        self.config = config

    def angle(self):
        return self.ang

    def calibrate(self):
        initial_time = self.config.timer.time()
        average = 0
        count = 0
        while self.config.timer.time() < initial_time + 1000 and self.config.state.getState() != 3:
            average += self.speed()
            count += 1

        self.cal = average / count
        print(self.cal)

    def run(self):
        last_time = self.config.timer.time()
        s = 0
        count = 0
        while self.config.state.getState() != 3:
            if self.config.timer.time() > last_time + 10:
                self.ang += (round(s/count) - self.cal) / 10
                s = 0
                count = 0
                last_time = self.config.timer.time()

            s += self.speed()
            count += 1

    def start(self):
        print("started")
        Thread(target=self.run).start()
