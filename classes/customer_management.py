from classes.server import Server


class CustomerManagement:
    def __init__(self, ttask, umax):
        self.servers = list()
        self.ttask = ttask
        self.umax = umax

    def add_client(self, new_client):
        for server in self.servers:
            if server.remaining_capacity() > 0:
                server.add_user(new_client)
                return
        else:
            server = Server(self.umax)
            server.add_user(new_client)
            self.servers.append(server)

    def update_ttime(self):
        for server in self.servers:
            server.update_ttask_users()
