from classes.exception.exceptions import ThereIsNoSpaceException


class Server:
    def __init__(self, umax):
        self.users = list()
        self.umax = umax

    def add_user(self, user):
        """
        Adds the user in this server
        """
        if self.remaining_capacity() > 0:
            self.users.append(user)
        else:
            raise ThereIsNoSpaceException('This server support only {} users'.format(self.umax))

    def remove_user(self, user):
        """
        Remove user, if it is not found, it will not do anything
        """
        try:
            self.users.remove(user)
        except Exception:
            msg = 'Failed do remove this user {}'.format(user)
            print(msg)

    def remaining_capacity(self):
        """
        Checks if has enough space
        """
        return self.umax - len(self.users)

    def update_ttask_users(self):
        """
        Updates Ttask of the users.
        """
        for user in self.get_users():
            user.update_ttask()

    def get_number_of_connected_users(self):
        return len(self.users)

    def get_users(self):
        return self.users
