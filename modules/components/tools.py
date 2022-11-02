from pybricks.tools import StopWatch


# Holds state of robot
# Is necessary to stop robot without exiting program
class RunState:
    running = 0
    standby = 1
    stop = 3

    def __init__(self):
        self.state = self.standby

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state


# Wrapper class for timer to allow for a wait function that will skip itself
# if robot state is in stop
class Timer(StopWatch):
    def __init__(self, config):
        self.state = config.state

    def wait(self, time):
        t = super().time()
        while super().time() < time + t and self.state.getState() != 3:
            pass
