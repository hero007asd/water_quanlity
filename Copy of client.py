'''
@author: William
'''
import socket
import datetime

HOST = 'localhost'#''#'192.168.8.27'#'27.115.49.11'#'localhost'#'192.168.20.113'
PORT = 21567#
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpClient.connect(ADDR)

print 'client is ready to send'
while True:
    senddate = raw_input('input:')
    if senddate:
        tcpClient.sendall('%s' % (senddate))
    recvdate = tcpClient.recv(BUFSIZ)
    #curTime = datetime.datetime.now()
    #curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')
    #print '%s %s' % (HOST,curTime)
    print recvdate
    if recvdate == '88':
        break
    
print 'client close'
tcpClient.close()