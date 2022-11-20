import socket 
import smtplib

host = socket.gethostname()  # as both code is running on same pc
port = 3000 

sockclient = socket.socket()  # instantiate
sockclient.connect((host, port))  # connect to the server
message = input(" -> ")  # take input
sockclient.send(message.encode())  # send message

while message.upper().strip() != 'JHAWAR':
    data = sockclient.recv(3072).decode()  # receive response

    print('Data Received: ' + data)  # show in terminal
    message = input(" -> ")  # again take input
    sockclient.send(message.encode())