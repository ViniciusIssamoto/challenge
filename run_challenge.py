import time
from classes.server import Server

input = open('input1.txt')
input_list = []
for line_txt in input:
    number_formated = int(line_txt.replace('\n', ''))
    input_list.append(number_formated)

servers = list()
servers.append(Server(10))
print(input_list)
