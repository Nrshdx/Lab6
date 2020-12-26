import socket

ClientSocket = socket.socket()
host = '192.168.43.2'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode()
print(Response)

while True:
    Input = input('Choose a mathematical function (L - Logarithmic | S - Square Root | E - Exponential) : ')
    
    if Input == 'L' :
        option = "log"
        value = input('Value : ')
        base = input('Value : ')
        l = option + '.' + value + '.' + base
        ClientSocket.send(str.encode(l))
    elif Input == 'S':
        option = "sq"
        value = input('Value : ')
        value2 = "0"
        s = option + '.' + value + '.' + value2
        ClientSocket.send(str.encode(s))
    elif Input == 'E':
        option = "exp"
        value = input('Value : ')
        value2 = "0"
        e = option + '.' + value + '.' + value2
        ClientSocket.send(str.encode(e))
    else :
        print ('Invalid funtion! Try Again \n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
