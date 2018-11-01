from classes.exception.exceptions import ThereIsNoSpaceException

class Server:
    def __init__(self, umax):
        self.users = list()
        self.umax = umax

    def add_user(self, user):
        if self.remaining_capacity() > 0:
            self.users.append(user)
        else:
            raise ThereIsNoSpaceException('This server support only {} users'.format(self.umax))

    def remaining_capacity(self):
        return self.umax - len(self.users)

    def update_ttask_users(self):
        for user in self.users:
            user.update_ttask()
            if user.timeout():
                del user
