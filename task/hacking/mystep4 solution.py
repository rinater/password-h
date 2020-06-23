# write your code here
import socket
import sys
import itertools
import string
import json

characters = string.digits + string.ascii_lowercase
answers = []
d = {}
correct_login = None
login_list = []
message = {}
correct_pass = ' '

with open("passwords.txt", 'r') as f:
    i = 0
    for line in f:
        x = line
        d[i] = x[:-1]
        i += 1
#passwords = d.values()
#print(passwords)
with open('logins.txt', 'r') as login_file:
    i = 0
    for line in login_file:
        x = line
        login_list[i] = x[:-1]
        i += 1


def generate_message():
    for login in login_list:
        message = {"login": login, "password": correct_pass}
        with open('send_message.json', 'w') as json_file:
            json.dump(message, json_file)
            return json_file


def generate_password():
    #for length in range(1, len(characters) + 1):
    #    for product in itertools.product(characters, repeat=length):
    #        yield ''.join(product)
    for password in d.values():
        maps = map(''.join, itertools.product(*zip(password.upper(), password.lower())))
        for a in list(maps):
            answers.append(a)


def map_gen(maps):
    for element in maps:
        yield element


def new_socket():
    user_command = sys.argv
    with socket.socket() as client_socket:
        hostname = user_command[1]
        port = int(user_command[2])
        address = (hostname, port)
        client_socket.connect(address)
        #client_socket.bind()
        generate_password()

        for password in answers:
            client_socket.send((password).encode())
            response = client_socket.recv(4096).decode()
            if response == 'result": "Connection success!!':
                break
            elif response == 'Too many attempts':
                print(response)


new_socket()
