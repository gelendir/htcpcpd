#!/usr/bin/env python2

import SocketServer
import SimpleHTTPServer
#from api import *

PORT = 8000
TEAPOT = False

class HTCPCPDImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	#pot = CoffeePot('/dev/ttyUSB0')

	def __init__(self, *args, **kwargs):
		SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, *args, **kwargs)

	def __del__(self):
		pass

	def do_GET(self):
		if self.is_bad_HTCPCP_request():
			return
	
	def do_POST(self):
		if self.is_bad_HTCPCP_request():
			return
		self.do_BREW()

	def do_PROPFIND(self):
		if self.is_bad_HTCPCP_request():
			return


	def do_WHEN(self):
		if self.is_bad_HTCPCP_request():
			return


	def do_BREW(self):
		if self.is_bad_HTCPCP_request():
			return
		
		length = int(self.headers.getheader('content-length'))        
		data_string = self.rfile.read(length).strip()
		if self.headers.getheader('content-type').strip() == "message/coffeepot":
			if data_string == "start":
				self.send_OK("The coffee pot is started.")
			elif data_string == "stop":
				self.send_OK("The coffee pot is stopped.")
			else:
				self.error("The content-type header is not correctly set for this body.")
				return
		elif self.headers.getheader('content-type').strip() == "application/coffee-pot-command":
			pass
		else:
			self.error("The content-type is not valid for this coffee pot.")
			return

	def send_OK(self, response):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(response)

	def error(self, error):
		self.send_error(400, error)
		self.end_headers()
	
	def send_safe_header(self, condition = 'yes'):
		self.send_header("Safe", condition)

	def is_bad_HTCPCP_request(self):
		return self.is_teapot() or self.is_not_acceptable()

	def is_teapot(self):
		if TEAPOT == True:
			self.send_error(418, "I'm a teapot")
			self.end_headers()
		return TEAPOT

	def is_not_acceptable(self):
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

