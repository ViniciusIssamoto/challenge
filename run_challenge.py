from classes.customer_management import CustomerManagement
from classes.user import User


class Challenge:
    def __init__(self, input_file, ttask, umax):
        # region import Input
        input = open(input_file)
        self.input_list = [
            int(line_txt.replace('\n', ''))
            for line_txt in input
        ]
        # endregion

        # region Variables
        self.ttask = ttask
        self.umax = umax
        self.index_input = 0
        self.customer_management = CustomerManagement(self.umax)
        # endregion

    def run(self):
        # Run challenge
        while True:
            if self.index_input < len(self.input_list):
                for user in range(0, self.input_list[self.index_input]):
                    self.customer_management.allocate_user(User(self.ttask))
                self.index_input += 1
            elif len(self.customer_management.servers) <= 0:
                break

            self.customer_management.remove_timeout_users()
            self.customer_management.optimize_servers()
            self.customer_management.save_state()
            self.customer_management.update_ttime()


challenge = Challenge('input1.txt', ttask=5, umax=10)
challenge.run()
