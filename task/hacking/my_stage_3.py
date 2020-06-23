# write your code here
import socket
import sys
import itertools
import string

characters = string.digits + string.ascii_lowercase
answers = []
d = {}
HOST = sys.argv[1]
PORT = int(sys.argv[2])

with open("passwords.txt", 'r') as f:
    i = 0
    for line in f:
        x = line
        d[i] = x[:-1]
        i += 1


def generate_password():
    for password in d.values():
        maps = map(''.join, itertools.product(*zip(password.upper(), password.lower())))
        for a in list(maps):
            answers.append(a)


def new_socket():
    with socket.socket() as client_socket:
        address = (HOST, PORT)
        client_socket.connect(address)
        # client_socket.bind()
        generate_password()
        for password in answers:
            client_socket.send(password.encode())
            response = client_socket.recv(4096).decode()
            if response == 'Connection success!':
                print(password)
                break


new_socket()
