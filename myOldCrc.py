'''
@author: William
'''
import struct
dwPolynomial = 0x04C11DB7
def cal_crc(ptr, len):
    crc = 0xFFFFFFFF
    for i in range(0, len):
        xbit = 1 << 31
        data = ptr[i]
        for bits in range(0, 32):
            if(crc & 0x80000000):
                crc <<= 1
                crc ^= dwPolynomial
            else:
                crc <<= 1
            if(data & xbit):
                crc ^= dwPolynomial
            xbit >>= 1
    my_crc = '%08x' %  (crc & 0xffffffff)
    return my_crc
# print cal_crc([0x7F,0x7F,0x0A,0x10,0xA8,0x03,0xEF,0x09,0x80,0x59,0x56,0x75], 12)

def exp_data(data):
    data_len = len(data)
    sof0 = ord(data[0])
    sof1 = ord(data[1])    
    lenth = ord(data[2])
    did0 = ord(data[3])
    did1 = ord(data[4])
    did2 = ord(data[5])
    did3 = ord(data[6])
    did4 = ord(data[7])
    did5 = ord(data[8])
    did6 = ord(data[9])
    did7 = ord(data[10])
    cmd = ord(data[11])
    crc0 = '%02x' % ord(data[-4])
    crc1 = '%02x' % ord(data[-3])
    crc2 = '%02x' % ord(data[-2])
    crc3 = '%02x' % ord(data[-1])
    #match 0x7f 0x7f #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if((sof0 != 0x7f) or (sof1 != 0x7f)):
        print 'wrong head'
#         return struct.pack('iiiiiiiiiiiiiiiii',0x7f,0x7f,0x0a,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x02,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x0a,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x02,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
    #match len #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if(lenth != data_len-7):
        print 'wrong lenth'
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x0a,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x03,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
 
    lenth_data = lenth - 9
    my_crc = [lenth, did0, did1, did2, did3, did4, did5, did6, did7, cmd]
    for x in range(lenth_data):
        my_crc.append(ord(data[11 + x + 1]))
#             print 'data%s:%s' % (x, hex(ord(data[11 + x + 1])))
    mycrc32 = cal_crc(my_crc, lenth + 1)
    mycrc0 = mycrc32[6:8]
    mycrc1 = mycrc32[4:6]
    mycrc2 = mycrc32[2:4]
    mycrc3 = mycrc32[0:2]
#     print mycrc3
#     print crc3
#     print mycrc0 != crc0
#     print mycrc1 != crc1
#     print mycrc2 != crc2
#     print mycrc3 != crc3
    #match crc32 #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if (mycrc0 != crc0) or (mycrc1 != crc1) or (mycrc2 != crc2) or (mycrc3 != crc3):
        print 'wrong crc'
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x0a,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x01,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
    cmd = hex(cmd)
    #match cmd=0x10
    if(cmd == '0x10'):
        print 'did is online'
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x09,did0,did1,did2,did3,did4,did5,did6,did7,0x10,0x01,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
    #match cmd=0x20 data=null len = 0x09
    elif(cmd == '0x20'):
        print 'did is sending data'
        return struct.pack('BBBBBBBBBBBBBBBB',0x7f,0x7f,0x09,did0,did1,did2,did3,did4,did5,did6,did7,0x20,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
    
    return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x09,did0,did1,did2,did3,did4,did5,did6,did7,0x11,0x01,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))

