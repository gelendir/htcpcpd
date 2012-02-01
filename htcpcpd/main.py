#!/usr/bin/env python2

#from api import *
from server import *

try:
	httpd = SocketServer.ThreadingTCPServer(('localhost', PORT), HTCPCPDImpl)

	print "serving at port", PORT
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.socket.close() 
finally:
	httpd.server_close()

