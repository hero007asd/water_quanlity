'''
@author: William
'''
import SocketServer
import myCrc
class MyStreamRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print 'connected by: %s' % self.client_address[0]
        while True:
#             try:
                data = self.request.recv(1024)
                if not data:
                    print 'no data received'
                    break
                result = myCrc.exp_data(data)
                self.request.send(result)
#             except:
#                 print 'except happend'
#                 #traceback.print_exc()
#                 break

            
if __name__ == "__main__":
    host = ''
    port = 21567
    addr = (host, port)
    print 'server is ready'
    server = SocketServer.ThreadingTCPServer(addr, MyStreamRequestHandler)
    server.serve_forever()
