'''
@author: William
'''
import struct
dwPolynomial = 0x04C11DB7
def cal_crc(ptr):
    crc = 0xFFFFFFFF
    for i in ptr:
        xbit = 1 << 31
        data = i
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
    all_len = len(data)
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
    # crc 7F 7F 0a 11 22 33 44 55 66 77 88 10 01 FD 0E 3C 53
    lenth_data = all_len - 7 - 9
    my_crc = [lenth, did0, did1, did2, did3, did4, did5, did6, did7, cmd]
    for x in range(lenth_data):
        my_crc.append(ord(data[11 + x + 1]))
    mycrc32 = cal_crc(my_crc)
    mycrc3 = mycrc32[0:2]
    mycrc2 = mycrc32[2:4]
    mycrc1 = mycrc32[4:6]
    mycrc0 = mycrc32[6:8]
    #match 0x7f 0x7f #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if((sof0 != 0x7f) or (sof1 != 0x7f)):
        print 'wrong head'
        #return crc
        return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,0x02]
        rtncrc32 = cal_crc(return_crc)
        rtncrc3 = rtncrc32[0:2]
        rtncrc2 = rtncrc32[2:4]
        rtncrc1 = rtncrc32[4:6]
        rtncrc0 = rtncrc32[6:8]
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x02,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))
    #match len #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if(lenth != all_len-7):
        print 'wrong lenth'
        #return crc
        return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,0x01]
        rtncrc32 = cal_crc(return_crc)
        rtncrc3 = rtncrc32[0:2]
        rtncrc2 = rtncrc32[2:4]
        rtncrc1 = rtncrc32[4:6]
        rtncrc0 = rtncrc32[6:8]
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x03,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))
    #match crc32 #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if (mycrc3 != crc0) or (mycrc2 != crc1) or (mycrc1 != crc2) or (mycrc0 != crc3):
        print 'wrong crc'
        #return crc
        return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,0x01]
        rtncrc32 = cal_crc(return_crc)
        rtncrc3 = rtncrc32[0:2]
        rtncrc2 = rtncrc32[2:4]
        rtncrc1 = rtncrc32[4:6]
        rtncrc0 = rtncrc32[6:8]
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x01,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))
#         return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,0x0a,did0,did1,did2,did3,did4,did5,did6,did7,0x91,0x01,ord(data[-4]),ord(data[-3]),ord(data[-2]),ord(data[-1]))
    cmd = hex(cmd)
    #match cmd=0x10
    if(cmd == '0x10'):
        print 'did is online'
        #return crc
        return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,0x01]
        rtncrc32 = cal_crc(return_crc)
        rtncrc3 = rtncrc32[0:2]
        rtncrc2 = rtncrc32[2:4]
        rtncrc1 = rtncrc32[4:6]
        rtncrc0 = rtncrc32[6:8]
        return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x10,0x01,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))
    #match cmd=0x20 data=null len = 0x09
    elif(cmd == '0x20'):
        print 'did is sending data'
        #return crc
        return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,0x01]
        rtncrc32 = cal_crc(return_crc)
        rtncrc3 = rtncrc32[0:2]
        rtncrc2 = rtncrc32[2:4]
        rtncrc1 = rtncrc32[4:6]
        rtncrc0 = rtncrc32[6:8]
        #TODO add to mysql
        return struct.pack('BBBBBBBBBBBBBBBB',0x7f,0x7f,0x09,did0,did1,did2,did3,did4,did5,did6,did7,0x20,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))
    
    return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x11,0x01,int(mycrc0,16),int(mycrc1,16),int(mycrc2,16),int(mycrc3,16))

def ret_crc(raw_data,data):
    did0 = ord(raw_data[3])
    did1 = ord(raw_data[4])
    did2 = ord(raw_data[5])
    did3 = ord(raw_data[6])
    did4 = ord(raw_data[7])
    did5 = ord(raw_data[8])
    did6 = ord(raw_data[9])
    did7 = ord(raw_data[10])
    return_crc = [0x0A, did0, did1, did2, did3, did4, did5, did6, did7, 0x91,data]
    rtncrc32 = cal_crc(return_crc)
    rtncrc3 = int(rtncrc32[0:2],16)
    rtncrc2 = int(rtncrc32[2:4],16)
    rtncrc1 = int(rtncrc32[4:6],16)
    rtncrc0 = int(rtncrc32[6:8],16)
    return [rtncrc3,rtncrc2,rtncrc1,rtncrc0]

def ret_pack(raw_data,data):   
    lenth = ord(raw_data[2])
    did0 = ord(raw_data[3])
    did1 = ord(raw_data[4])
    did2 = ord(raw_data[5])
    did3 = ord(raw_data[6])
    did4 = ord(raw_data[7])
    did5 = ord(raw_data[8])
    did6 = ord(raw_data[9])
    did7 = ord(raw_data[10])
    mycrc3 = ret_crc(raw_data,data)[0]
    mycrc2 = ret_crc(raw_data,data)[1]
    mycrc1 = ret_crc(raw_data,data)[2]
    mycrc0 = ret_crc(raw_data,data)[3]
    struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,lenth,did0,did1,did2,did3,did4,did5,did6,did7,0x10,data,mycrc0,mycrc1,mycrc2,mycrc3)