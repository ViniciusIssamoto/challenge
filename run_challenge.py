from classes.customer_management import CustomerManagement
from classes.user import User


class Challenge:
    def __init__(self, ttask, umax):
        self.ttask = ttask
        self.umax = umax
        self.customer_management = CustomerManagement(self.umax)

    @staticmethod
    def file_to_iter(path_file) -> iter:
        file = open(path_file)
        return (
            int(line_txt.replace('\n', ''))
            for line_txt in file
        )

    def clock_ticks_iter(self, file_iterator):
        for it in file_iterator:
            yield it

        while self.customer_management.servers_running > 0:
            yield 0

        return

    def run(self, file):
        file_iterator = self.file_to_iter(file)

        for i in self.clock_ticks_iter(file_iterator):
            self.next_clock_tick(i)

    def next_clock_tick(self, users_clock_ticks):
        for user in range(users_clock_ticks):
            self.customer_management.allocate_user(User(self.ttask))

        self.customer_management.remove_timeout_users()
        self.customer_management.optimize_servers()
        self.customer_management.save_state()
        self.customer_management.update_ttime()


challenge = Challenge(ttask=5, umax=10)
challenge.run('input1.txt', )
