import base64
import time
from socket import *
import smtplib


def send_password(receiver, password):
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login("cs1340.networks@outlook.com", "boBhik-johmo6-jysbig")
    message = f"""From: From Person <cs1340.networks@outlook.com>
    To: To Person <{receiver}>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: SMTP HTML e-mail test


    <b>Welcome to the networks assignment</b>
    <h1>Password enclosed | DO NOT SHARE <h1>
    <p>Your account information is:\nEmail address: {receiver} \nPassword: {password}</p>


    """
    s.sendmail("cs1340.networks@outlook.com", receiver, msg=message)
    
    # terminating the session
    s.quit()

import socket 
import smtplib

COURSES = {
    'CS1101': "\nNo Prerequisites",
    'CS1104': "\nNo Prerequisites",
    'CS1205': "\nPrerequisites:\nCS-1101\nCS-1104",
    'CS1216': "\nPrerequisites:\nCS-1101\nCS-1104",
    'CS1217': "\nPrerequisites:\nCS-1101\nCS-1104 ",
    'CS1203': "\nPrerequisites:\nCS-1101\nCS-1104",
    'CS1390': "\nPrerequisites:\nCS-1205\nCS-1216\nCS-1217\nCS-1203",
    'CS1340': "\nPrerequisites:\nCS-1205\nCS-1216\nCS-1217\nCS-1203",
    'CS1319': "\nPrerequisites:\nCS-1205\nCS-1216\nCS-1217\nCS-1203",
}

SEMESTER = {
    'MONSOON': "\nUse of Approximate Computing in Federated Learning [CS-IS-5005], \nSymbolic Logic [PHI-1060/ CS-2160], \nStatistics for Economics [ECO-1400/ CS-1207], \nReading, reviewing, and presenting scientific papers [CS-IS-4020], \nRapid Prototyping and Experimentation [CS-IS-4026], \nQuantum Complexity Theory [CS-IS-4022], \nProgramming Language Design and Implementation [CS-1319], \nProgramming Language Design and Implementation [CS-1319], \nProbability and Statistics [MAT-2020/ CS-1209/ PHY-1208], \nMultimodal Analysis for Content Classification [CS-IS-4021], \nMachine Learning for Finance [CS-2466], \nLinear Algebra [MAT-1001/ CS-2210/ PHY-1001], \nIntroduction to Machine Learning [CS-1390/ PHY-1390], \nIntroduction to Computer Programming [CS-1101/ PHY-1101], \nInformation and Coding Theory [CS-2462], \nFairness of AI [CS-2464], \nEmbedded systems firmware security [CS-IS-4024], \nDistributed Network Algorithms [CS-2450], \nDatabase Management Systems [CS-2375], \nData Structures [CS-1203], \nComputing in the Cloud [CS-2465], \nComputer Vision [CS-2467], \nComputer Organization and Systems [CS-1216], \nComputer Networks [CS-1340], \nComputational/Mathematical Biology [BIO-3513/ BIO-4313/ BIO-6513/ PHY-3513/ PHY-6313/ CS-2456], \nComputational Systems Medicine at Single Cell Resolution [CS-3032], \nBuilding a Mental Wellbeing App [CS-IS-4023], \nBiostatistics and Bioinformatics [BIO-3005/ BIO-6009/ CS-2455], \nAn overview of usable privacy and security [CS-2463], \nAdvanced Topics in Cryptography [CS-IS-4025], \nAdvanced Algorithms [CS-2446]",
    'SPRING': "Advanced Algorithmic Economics [CS-IS-4013], \nAdvanced Machine Learning [CS-2490], \nAdvanced Topics in Probability [CS-2470/ MAT-4050], \nAlgorithm Design and Analysis [CS-1205], \nBlockchain and Cryptocurrencies [CS-2361], \nCapstone Thesis [CS-4999], \nComputer Security and Privacy [CS-2362], \nData Analytics for Air Quality Assessment [CS-IS-3024], \nData Mining and Warehousing [CS-2376/ PSY-2376], \nData Science: Sports [CS-IS-3023], \nDiscrete Mathematics [CS-1104\n],Fuzzy Cartographies [ENG-3340/ CS-2209], \nHardware-based Memory Encryption: Primitives, Modules and Intel SGX [CS-IS-3025], \nHuman-AI Assisted Sports Coaching: Computer Vision and Transfer Learning [CS-IS-3030], \nHuman-Computer Interaction [CS-IS-2006], \nIntroduction to Computer Programming [CS-1101/ PHY-1101], \nItemset Placement in Retail [CS-IS-4015], \nLinear Algebra [MAT-1001/ CS-2210/ PHY-1001], \nMachine Learning for Healthcare [CS-IS-4017], \nMathematical Foundations of Data Sciences [MAT-4020/ CS-2380], \nMLOps [CS-IS-4014], \nOperating Systems [CS-1217], \nQuantitative Portfolio Construction [CS-IS-3028], \nThe Internet and CSAM [CS-IS-3029], \nThe New Geography of the Information Age [CS-2378/ POL-2070], \nTheory of Computation [CS-2349], \nTopics in Quantum Computation and Quantum Information [CS-IS-4016], \nWeb Exploitation [CS-IS-3026]\n",            
}
USERS = {
    'usr1':"passwd",
    'usr2':"passwd",
}

host = socket.gethostname()
port = 3000

sockserver = socket.socket()
sockserver.bind((host, port))  
sockserver.listen(2)

connection, address = sockserver.accept()
print(str(address)+ "connected.")

logged_in = False
while True:
    data = connection.recv(3072).decode()
    if data == 'logout':
        logged_in = False
        connection.send("Logged Out\n\nPlease enter your email address to login/ register\n".encode())
        continue
    if logged_in:
        if not data:
            break
        elif 'cs' in data.lower():
            data = data.upper()
            if data in COURSES:
                connection.send(COURSES[data].encode())
            else:
                connection.send("Course not found".encode())
        elif 'monsoon' in data.lower() or 'spring' in data.lower():
            X = data.upper()[1:-1].split(',')[0]
            Y = data.upper()[1:-1].split(',')[1]
            if X in SEMESTER.keys() and Y =='2022':
                connection.send(SEMESTER[X].encode())
            else:
                connection.send("Please enter the correct semester or year\n".encode())
        else:
            connection.send("Invalid input entered".encode())
        print("From connected user: " + data)
    else:
        if '@ashoka.edu.in' in data:
            if data in USERS.keys():
                connection.send("Enter password".encode())
                password = connection.recv(3072).decode()
                if password == USERS[data]:
                    connection.send("Login Successful. \n\nEnter course code to find prerequisites or (semester,year) to see the course-list\n".encode())
                    logged_in = True
                else:
                    connection.send("Incorrect Email ID or Password\n\nPlease enter your email address to login/ register\n".encode())
            else:
                connection.send("A password has been sent to your email, please checck your spam folder and enter the password below\n".encode())
                password = data.split('@')[0].upper().split('.')[0]
                send_password(data, password)
                USERS[data] = password
                password = connection.recv(3072).decode()
                if password == USERS[data]:
                    connection.send("Login Successful. \n\nEnter course code to find prerequisites or (semester,year) to see the course-list\n".encode())
                    logged_in = True
                else:
                    connection.send("Incorrect Email ID or Password\n\nPlease enter your email address to login/ register\n".encode())
        else:
            connection.send("Invalid Email Address Entered\n\nPlease enter your email address to login/ register\n".encode())
    data = data.upper()