class Connector():
    def __init__(self):
        self.pipes = {}

    def register(self, _name, _callback):
        self.pipes[_name] = _callback

    def update(self, _name=None, args=None):
        self.pipes[_name](args)
