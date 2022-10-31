from threading import Thread


def runify(func):
    class temp(Thread):
        def __init__(self, config):
            self.config = config

        def run(self):
            func()
            self.config.state.setState(1)
    return temp
