import logging
from classes.user import User
from classes.server import Server


class CustomerManagement:
    def __init__(self, umax):
        logging.basicConfig(filename='output.txt', format='', level=logging.DEBUG)
        self.servers = list()
        self.umax = umax
        self.clock_ticks = 1

    @property
    def servers_running(self) -> int:
        return len(self.servers)

    @property
    def total_users_connected(self) -> int:
        return sum(server.number_of_connected_users for server in self.servers)

    @property
    def total_capacity(self) -> int:
        return self.umax * len(self.servers)

    def allocate_user(self, new_user):
        """
        Adds the new client into the server. If not enough space, will instantiate a new server
        :param new_user: client to add
        """
        for server in self.servers:
            if server.remaining_capacity > 0:
                server.add_user(new_user)
                return
        else:
            server = Server(self.umax)
            server.add_user(new_user)
            self.servers.append(server)

    def update_ttime(self):
        """
        Calls servers to update Ttime
        """
        self.clock_ticks += 1
        for server in self.servers:
            server.update_ttask_users()

    def remove_timeout_users(self):
        """
        Will check all users of all servers to find timeout users
        """
        for server in self.servers:
            users_to_remove = []
            for user in server.users:
                if user.timeout():
                    users_to_remove.append(user)

            for user in users_to_remove:
                server.remove_user(user)

    def optimize_servers(self):
        """
        If empty slots are equal to or greater than the capacity of a server, will optimize
        :return:
        """
        empty_slots = self.total_capacity - self.total_users_connected
        servers_to_empty = int(empty_slots / self.umax)

        for i in range(servers_to_empty):
            while self.servers[0].users:

                for server in self.servers:
                    if server.remaining_capacity > 0 and self.servers[0] != server:
                        # Puts the user to this server
                        server.add_user(self.servers[0].users[0])

                        # Remove user from last server
                        self.servers[0].remove_user(self.servers[0].users[0])
                        break

            # After allocating users, shut down the server 0
            self.servers.remove(self.servers[0])

    def get_servers_status(self):
        return ''.join(f'{server.number_of_connected_users},' for server in self.servers)[:-1]

    def save_state(self):
        logging.info(f'Clock ticks: {self.clock_ticks}: {self.get_servers_status()}')
