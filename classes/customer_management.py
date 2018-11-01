import logging
from classes.server import Server


class CustomerManagement:
    def __init__(self, umax):
        logging.basicConfig(filename='output.txt', format='', level=logging.DEBUG)
        self.servers = list()
        self.umax = umax
        self.clock_ticks = 1

    def allocate_user(self, new_user):
        """
        Adds the new client into the server. If not enough space, will instantiate a new server
        :param new_user: client to add
        """
        for server in self.servers:
            if server.remaining_capacity() > 0:
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
            users_list = []
            for user in server.get_users():
                if user.timeout():
                    users_list.append(user)

            for user in users_list:
                server.remove_user(user)

    def optimize_servers(self):
        """
        If empty slots are equal to or greater than the capacity of a server, will optimize
        :return:
        """
        users_connected = sum(server.get_number_of_connected_users() for server in self.servers)
        max_capacity = self.umax * len(self.servers)
        empty_slots = max_capacity - users_connected

        if empty_slots >= self.umax:
            servers_to_empty = int(empty_slots / self.umax)
            for i in range(0, servers_to_empty):
                for client in self.servers[0].get_users():
                    # Find new server to this user
                    for server in self.servers:
                        if server.remaining_capacity() > 0 and self.servers[0] != server:
                            # Puts the user to this server
                            server.add_user(client)
                            break
                # After allocating users, shut down the server 0
                self.servers.remove(self.servers[0])

    def get_servers_status(self):
        return ''.join('{},'.format(server.get_number_of_connected_users()) for server in self.servers)[:-1]

    def save_state(self):
        logging.info('CTicks: {}: {}'.format(self.clock_ticks, self.get_servers_status()))
