'''
@author: William
'''
# def h():
#     print 'start yield'
#     m = yield 5
#     print m
#     d = yield 12
#     print 'stop yield'
# 
# c = h()
# m = c.next()
# d = c.send('fighting')
# print 'We will never forget the date', m, '.', d
import struct

# test = '0x7F0x7F0x140xFFCCFFCCFFCCFFCC0x100xD0xDA00000010xB00000010xC00000010xD0000001'
# h = 0x7F7F14FFCCFFCCFFCCFFCC10DDA0000001B0000001C0000001D0000001
# h_str = '%x' % h
# h_str = h_str.upper()
# sof = h_str[:4]
# datalen = h_str[4:6]
# did = h_str[6:22]
# cmd = h_str[22:24]
# crc32 = h_str[-32:]
# data = h_str[24:(24+(int(datalen,16)-18))]
# print 'sof:',sof,',crc32:',crc32,',len:',datalen,',did:',did,',cmd:',cmd,'data:',data


b=0xFACD2D123
str = struct.pack('>l',b)
# print len(str)
# print str
# print repr(str)
# a1 = struct.unpack('>l',str)
# print 'a1:',a1
format='!HH%ds' % len(str)
print format
print struct.calcsize(format)