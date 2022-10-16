from pybricks.tools import StopWatch


class runState:
    running = 0
    standby = 1
    stop = 3

    def __init__(self):
        self.state = self.standby

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state


class timer(StopWatch):
    def __init__(self, config):
        self.state = config.state
        self.time = StopWatch

    def wait(self, time):
        t = super().time()
        while super().time() < time + t and self.state.getState() != 3:
            print(self.state.getState())
            pass
        print("Done")
