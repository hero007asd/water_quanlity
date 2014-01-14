'''
@author: William
'''
import SocketServer
class MyStreamRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print 'connected by: %s' % self.client_address[0]
        while True:
            try:
#                 data = self.rfile.readline().strip()
#                 print 'receive from (%r) : %r' % (self.client_address,data)
#                 self.wfile.write(data.upper())
                data = self.request.recv(1024)
                if not data:
                    print 'no data received'
                    break
                print data
                print 'recv from %s:%x' % (self.client_address[0],data)
                #handle data
                self.exp_data(data)
                self.request.send('ok')
            except:
                self.request.send('error')
                print 'error happend'
                #traceback.print_exc()
                break
    def exp_data(self,data):
        print data
        
            
if __name__ == "__main__":
    host=''
    port = 21567
    addr = (host,port)
    print 'server is ready'
    server = SocketServer.ThreadingTCPServer(addr,MyStreamRequestHandler)
    server.serve_forever()