
class User:
    def __init__(self, ttask):
        self.ttask = ttask

    def update_ttask(self):
        self.ttask -= 1

    def timeout(self):
        if self.ttask > 0:
            return False
        else:
            return True


