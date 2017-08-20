import socket
import struct
from enum import Enum
import sys
import random


class Type(Enum):
    REQ_CHALLENGE = 0x01
    ACK_CHALLENGE = 0x02
    REQ_AUTH = 0x03
    ACK_AUTH = 0x04
    REQ_LOGOUT = 0x05
    ACK_LOGOUT = 0x06
    AFF_ACK_AUTH = 0x07
    NTF_LOGOUT = 0x08
    REQ_INFO = 0x09
    ACK_INFO = 0x0a

class AuthType(Enum):
    CHAP = 0x00
    PAP = 0x01



class PortalMsgHdr():
    def __init__(self, type, authType, serialNo,  reqId, userIp, userPort ,errCode, attrNum):
        self.version = 2 # 8 bits
        self.type = type # 8 bits
        self.authType = authType # 8 bits
        self.rsv = 0 # 8 bits
        self.serialNo = serialNo # 16 bits
        self.reqId = reqId # 16 bits
        self.userIp = userIp # 32 bits
        self.userPort = userPort # 16 bits
        self.errCode = errCode # 8 bits
        self.attrNum = attrNum # 8 bits
    def pack(self):
        #portalMsgHdr = struct.pack('BB', 1, 2)
        portalMsgHdr = struct.pack('!BBBBHH4sHBB', self.version,self.type,self.authType,self.rsv,self.serialNo,
                                   self.reqId,socket.inet_aton(self.userIp),self.userPort,self.errCode,self.attrNum)

        return portalMsgHdr


if __name__ == '__main__':
    address = ('1.1.1.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    portalMsgHdr = PortalMsgHdr(Type.REQ_CHALLENGE.value, AuthType.CHAP.value, 1, 1, '1.1.1.1', 80, 0,1)
    try:
        response = s.sendto(portalMsgHdr.pack(), address)
    except:
        print ('sendto error')