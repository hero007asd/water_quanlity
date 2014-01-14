'''
tcp server
@author: William
'''
import socket
import datetime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(10)

print 'server is ready'
while True:
    tcpCliSocket, addr = tcpSerSocket.accept()
    print 'connected by: %s' % addr[0]
    while True:
        try:
            date = tcpCliSocket.recv(BUFSIZ)
            if date:
                #curTime = datetime.datetime.now()
                #curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')
                #print '%s %s' % (addr,curTime)
                print date
                sendDate = 'i have received'#raw_input('input:')
                tcpCliSocket.send('%s' % (sendDate))
                if date == '88':
                    break
            else: 
                print 'error string'
                break
        except:
            print 'time out'
            break
    tcpCliSocket.close()

print 'server close'
tcpSerSocket.close()

