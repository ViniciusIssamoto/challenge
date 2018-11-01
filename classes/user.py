class User:
    def __init__(self, ttask, clock_tick=None):
        self.clock_tick = clock_tick
        self.ttask = ttask

    def update_ttask(self):
        self.ttask -= 1

    def timeout(self):
        if self.ttask <= 0:
            return True
        else:
            return False
