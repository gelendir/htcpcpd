#!/usr/bin/env python2

import SocketServer
import SimpleHTTPServer
import urllib
import ConfigParser
from api import *

config = ConfigParser.RawConfigParser()
config.read('htcpcpd.ini')

SERIAL_DEVICE = config.get('htcpcpd', 'device')
PORT = config.getint('htcpcpd', 'port') #8000
TEAPOT = config.getboolean('htcpcpd', 'teapot') #False

class HTCPCPDImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	#pot = CoffeePot(SERIAL_DEVICE)

	def do_GET(self):
		if self.is_bad_HTCPCP_request():
			return
		page = self.get_called_page()
		if page == "status":
			self.send_OK("The coffee is not brewing.")
		elif page == "water":
			#self.send_OK("There is no water in the coffee pot.")
			self.send_OK("There is 2 litres of water in the coffee pot.")
		elif page == "bucket":
			self.send_OK("The bucket is in position.")
		else:
			self.send_error(404, "This page is unavailable")
			self.end_headers()
			self.wfile.write("""<p>Here is different link that you maybe want: </p>
			<ul>
				<li><a href="/status">Status of brewing</a></li>
				<li><a href="/water">Quantity of water in the coffee cup</a></li>
				<li><a href="/bucket">Status of the bucket</a></li>
			</ul>
			""")
			
	def do_POST(self):
		if self.is_bad_HTCPCP_request():
			return
		self.do_BREW()

	def do_PROPFIND(self):
		if self.is_bad_HTCPCP_request():
			return
		self.send_OK()

	def do_WHEN(self):
		if self.is_bad_HTCPCP_request():
			return
		self.send_OK()


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
		elif self.headers.getheader('content-type').strip() == "application/coffee-pot-command":
			pass
		else:
			self.error("The content-type is not valid for this coffee pot.")

	def send_OK(self, response = ''):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(response)

	def error(self, error, message = ""):
		self.send_error(400, error)
		self.end_headers()
		self.wfile.write(message)
	
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

	def get_called_page(self):
		p = urllib.unquote_plus(self.path)
		p = p.strip()
		p = p.strip("/")
		return p

#try:
#	httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),HTCPCPDImpl)
#	
#	print "serving at port", PORT
#	httpd.serve_forever()
#except KeyboardInterrupt:
#	httpd.socket.close() 
#finally:
#	httpd.server_close()

