class RunButton:
    def __init__(self, button):
        self.button = button

    def pressed(self):
        return self.button.pressed()
