
import socket
import sys

def solve_maths(msg):
    answer = 0

    num01,op,num02 = msg.split(" ")
    num1 = num01.strip()
    num2 = num02.strip()
    op = operator.strip()
    
    if operator == '+':
        answer = num1 + num2
    if operator == '-':
        answer = num1 + num2
    if operator == '*':
        answer = num1 + num2
    if operator == '/':
        answer = num1 + num2
    return answer
    

serverName = '127.0.0.1'
serverPort = 12000
buffmax = 4096
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
endStatus = False
endHello = False

NUID = raw_input('Input NU ID (include all leading zeros): ')
Hello = "ece2540 HELLO " + NUID
while endHello == False:
    clientSocket.send(Hello.encode('utf-8'))
    message = clientSocket.recv(buffmax)
    demessage = message.decode('utf-8')
    print demessage
    ece2540,code,payload = demessage.split(" ", 2)
    if code == 'STATUS':
        break
    
while endStatus == False:
    
    message = clientSocket.recv(buffmax)
    demessage = message.decode('utf-8')
    print demessage
    ece2540,code,payload = demessage.split(" ", 2)
    print "the split is:" + ece2540 + ", " + code + ", " + payload
    print "the strip is:" + ece2540.strip() + ", " + code.strip() + ", " + payload.strip()

    if code == 'STATUS':
        ans = solve_maths(payload)
        clientSocket.send(ans.encode('utf-8'))

    if code == 'ERROR':
        print "Error"
        end = True

    if code == 'BYE':
        print "The connection is over the secret code is: " + payload
        end = True
