#!/usr/bin/env python2

import SocketServer
import SimpleHTTPServer

PORT = 8000
TEAPOT = False

class HTCPCPDImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	
	def do_GET(self):
		if self.isBadHTCPCPRequest():
			return
	
	def do_POST(self):
		if self.isBadHTCPCPRequest():
			return


	def do_PROPFIND(self):
		if self.isBadHTCPCPRequest():
			return


	def do_WHEN(self):
		if self.isBadHTCPCPRequest():
			return


	def do_BREW(self):
		if self.isBadHTCPCPRequest():
			return

	def isBadHTCPCPRequest(self):
		return self.isTeapot() or self.isNotAcceptable()

	def isTeapot(self):
		if TEAPOT == True:
			self.send_error(418, "I'm a teapot")
			self.end_headers()
		return TEAPOT

	def isNotAcceptable(self):
		accept_additions = self.headers.getrawheader("Accept-Additions")
		if accept_additions is not None and accept_additions.strip():
			self.send_error(406, "Not Acceptable")
			self.end_headers()
			return True
		
		return False

try:
	httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),HTCPCPDImpl)
	
	print "serving at port", PORT
	httpd.serve_forever()
except Exception:
	pass
finally:
	httpd.server_close()

