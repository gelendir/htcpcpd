#!/usr/bin/env python2
"""
This file start the HTCPCP server and deamonize it.
Author: Frédérik Paradis
"""

from server import *

try:
	httpd = SocketServer.ThreadingTCPServer(('localhost', PORT), HTCPCPDImpl)

	print "serving at port", PORT
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.socket.close() 
finally:
	httpd.server_close()

