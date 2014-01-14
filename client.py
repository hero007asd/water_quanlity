'''
@author: William
'''
import socket
import datetime
import struct

HOST = 'localhost'#''#'192.168.8.27'#'27.115.49.11'#'localhost'#'192.168.20.113'
PORT = 21567#
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpClient.connect(ADDR)

print 'client is ready to send'
# senddate = raw_input('input:')

senddate = struct.pack('BBBBBBBBBBBBBBBBB',0x7F,0x7F,0x0a,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x10,0x01,0xFD,0x0E,0x3C,0x53)
if senddate:
    tcpClient.send(senddate)
recvdate = tcpClient.recv(BUFSIZ)
#curTime = datetime.datetime.now()
#curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')
#print '%s %s' % (HOST,curTime)
print repr(recvdate)
print hex(ord(recvdate[0]))
print hex(ord(recvdate[1]))
print hex(ord(recvdate[2]))
print hex(ord(recvdate[3]))
print hex(ord(recvdate[4]))
print hex(ord(recvdate[5]))
print hex(ord(recvdate[6]))
print hex(ord(recvdate[7]))
print hex(ord(recvdate[8]))
print hex(ord(recvdate[9]))
print hex(ord(recvdate[10]))
print hex(ord(recvdate[11]))
print hex(ord(recvdate[12]))
print hex(ord(recvdate[13]))
print hex(ord(recvdate[14]))
print hex(ord(recvdate[15]))
print hex(ord(recvdate[16]))
# if recvdate == '88':
#     break
    
print 'client close'
tcpClient.close()