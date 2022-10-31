from threading import Thread


def runify(func, config):
    class temp(Thread):
        def __init__(self, config, func):
            self.config = config
            self.func = func

        def run(self):
            self.func()
            self.config.state.setState(1)

    return temp(config, func)
