import time
from classes.server import Server
from classes.user import User
from classes.customer_management import CustomerManagement
input = open('input1.txt')
input_list = []
for line_txt in input:
    number_formated = int(line_txt.replace('\n', ''))
    input_list.append(number_formated)

servers = list()
for index, input in enumerate(input_list):
    for user in range(0, input):
        CustomerManagement
        servers.append(Server(10))
        servers.append(Server(10))
        servers[0].add_user(User(1))
        servers[0].users[0].update_ttask_users()
        servers[0].users[0].update_ttask_users()
print(input_list)
