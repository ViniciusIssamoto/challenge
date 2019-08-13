from classes.exception.exceptions import ThereIsNoSpaceException


class Server:
    def __init__(self, umax):
        self.__users = list()
        self.__umax = umax

    def add_user(self, user):
        """
        Adds the user in this server
        """
        if self.remaining_capacity > 0:
            self.__users.append(user)
        else:
            raise ThereIsNoSpaceException(f'This server support only {self.__umax} users')

    def remove_user(self, user):
        """
        Remove user, if it is not found, it will not do anything
        """
        self.__users.remove(user)

    @property
    def remaining_capacity(self):
        """
        Checks if has enough space
        """
        return self.__umax - len(self.__users)

    def update_ttask_users(self):
        """
        Updates Ttask of the users.
        """
        for user in self.users:
            user.update_ttask()

    @property
    def number_of_connected_users(self):
        return len(self.__users)

    @property
    def users(self):
        return self.__users
