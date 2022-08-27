class runState:
    running = 0
    standby = 1
    stop = 3

    def __init__(self):
        self.state = self.standby

    def setState(self, state):
        self.state = state
