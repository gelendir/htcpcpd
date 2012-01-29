#!/usr/bin/env python2

import SocketServer
import SimpleHTTPServer

PORT = 8000
TEAPOT = False

class HTCPCPDImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, *args, **kwargs)

	def __del__(self):
		pass

	def do_GET(self):
		if self.isBadHTCPCPRequest():
			return
	
	def do_POST(self):
		if self.isBadHTCPCPRequest():
			return
		self.do_BREW()

	def do_PROPFIND(self):
		if self.isBadHTCPCPRequest():
			return


	def do_WHEN(self):
		if self.isBadHTCPCPRequest():
			return


	def do_BREW(self):
		if self.isBadHTCPCPRequest():
			return
		
		#print self.headers.getheader('content-type')

		length = int(self.headers.getheader('content-length'))        
		data_string = self.rfile.read(length)
		if data_string not in ["start", "stop"]:
			self.send_error(400, 'The data must be "start" or "stop" for this method.')
			self.end_headers()
			return
		elif self.headers.getheader('content-type').strip() != "message/coffeepot":
			self.send_error(400, "The content-type header is not correctly setted.")
			self.end_headers()
			return
			
		self.send_response(200)
		self.end_headers()

		if data_string == "start":
			pass
		elif data_string == "stop":
			pass

	def isBadHTCPCPRequest(self):
		return self.isTeapot() or self.isNotAcceptable()

	def isTeapot(self):
		if TEAPOT == True:
			self.send_error(418, "I'm a teapot")
			self.end_headers()
		return TEAPOT

	def isNotAcceptable(self):
		accept_additions = self.headers.getheader("Accept-Additions")
		if accept_additions is not None and accept_additions.strip():
			self.send_error(406, "Not Acceptable")
			self.end_headers()
			return True
		
		return False

try:
	httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),HTCPCPDImpl)
	
	print "serving at port", PORT
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.socket.close() 
finally:
	httpd.server_close()

