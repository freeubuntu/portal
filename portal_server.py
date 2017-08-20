# !/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import time
import sys
from portal_msg_hdr import *

from urllib.parse import parse_qs
class PortalServer():
    def __init__(self):
        pass

    def parse_httpreq(self):
        pass


    def req_challenge(self):
        serialNo = random.randint(pow(2,16))
        reqId = random.randint(pow(2,16))
        portalMsgHdr(Type.ACK_CHALLENGE.value, AuthType.CHAP.value, serialNo, )
        pass

    def req_auth(self):
        pass

    def ack_auth(self):
        pass


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print('receive get request')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Portal Authentication</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>Auth Form</p>", "utf-8"))
        self.wfile.write(bytes("""<form method="post">""", "utf-8"))
        self.wfile.write(bytes("""username:<input type="text" name="username"><br> """, "utf-8"))
        self.wfile.write(bytes(""" password:<input type="password" name="password"><br>""", "utf-8"))
        self.wfile.write(bytes("""<input type="submit" value="login">""", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


    def do_POST(self):
        print('receive post request')
        try:
            # bytes to str
            auth_bytes = str(self.rfile.read(int(self.headers['content-length'])), 'utf-8')
            # parse urlencoded str to dict
            auth_dict = parse_qs(auth_bytes)
            print(self.client_address)
            print('username: ', auth_dict['username'][0], 'password: ', auth_dict['password'][0])
            resp_str = 'Authenticated Successfully'
        except:
            resp_str = "Wrong Username or Password"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(resp_str, "utf-8"))

if __name__ == '__main__':
    hostName = '0.0.0.0'
    hostPort = 80
    my_server = HTTPServer((hostName,hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass
        my_server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))