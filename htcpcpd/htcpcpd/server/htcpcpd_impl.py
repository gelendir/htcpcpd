#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This file contains the HTCPCPDImpl class, used
to recieve and interpret HTCPCP requests.
Author: Frédérik Paradis
"""

import SocketServer
import SimpleHTTPServer
import urllib
import ConfigParser
from htcpcpd.api import *

class HTCPCPDImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	"""
	This class is used to implement the HTCPCP protocol which is
	an update of the HTTP protocol. The HTCPCP protocol is used to
	control a coffee pot trough the HTTP protocol. Check the
	RFC (http://tools.ietf.org/html/rfc2324) for more detais.
	"""

	@classmethod
	def initconfig(cls, config):

		cls.SERIAL_DEVICE = config.get('htcpcpd', 'device')
		cls.TEAPOT = config.getboolean('htcpcpd', 'teapot')
		cls.pot = CoffeePot(cls.SERIAL_DEVICE)
		"""
		The static CoffeePot instance for the HTCPCP server.
        Used to communicate with the coffeepot API.
		"""

	def do_GET(self):
		"""
		This method implements the GET HTTP method. The actual
		available pages are 'status', 'water' and 'pot'.

		The 'status' page gets the brewing status of the coffee pot
		from self.pot.
		
		The 'water' page gets how much water is left in the coffee pot
		from self.pot.

		The 'pot' page gets the pot status of the coffee pot
		from self.pot.

		If the page called doesn't exist, a 404 error is sent
		with the available page on this server.
		"""

		#If the request is bad, the headers are already sent,
		#so we can return.
		if self.is_bad_HTCPCP_request():
			return

		#We get the called page
		page = self.get_called_page()

		#We called the specified page.
		if page == "status":
			if self.pot.isCoffeeBrewing():
				self.send_OK("The coffee is brewing.")
			else:
				self.send_OK("The coffee is not brewing.")	
		elif page == "water":
			litres = self.pot.getNbLitres()
			if litres == 0:
				self.send_OK("There is no water in the coffee pot.")
			else:
				self.send_OK("There is " + str(litres) + " litres of water in the coffee pot.")
		elif page == "pot":
			if self.pot.hasPot():
				self.send_OK("The coffee pot is in position.")
			else:
				self.send_OK("The coffee pot is not in position.")
		elif page == "water_reading":
			self.send_OK(self.pot.waterReading())
		elif page == "time_left":
			self.send_OK(self.pot.timeLeft())
		else:
			self.send_error(404, "This page is unavailable")
			self.end_headers()
			self.wfile.write("""<p>Here is different link that you maybe want: </p>
			<ul>
				<li><a href="/status">Status of brewing</a></li>
				<li><a href="/water">Quantity of water in the coffee cup</a></li>
				<li><a href="/pot">Status of the coffee pot</a></li>
			</ul>
			""")
			
	def do_POST(self):
		"""
		This method implements the POST HTTP method. It 
		only calls the do_BREW method as specified in 
		the HTCPCP RFC.
		"""

		#If the request is bad, the headers are already sent,
		#so we can return.
		if self.is_bad_HTCPCP_request():
			return

		self.do_BREW()

	def do_PROPFIND(self):
		"""
		This method implements the PROPFIND HTTP method. It is supposed 
		to send metadata on the coffee pot. For now, it returns a 
		not implemented error.
		"""

		#If the request is bad, the headers are already sent,
		#so we can return.
		if self.is_bad_HTCPCP_request():
			return
		
		self.send_not_implemented("This coffee pot has no metadata associated.")

	def do_WHEN(self):
		"""
		This method implements the WHEN HTCPCP method. It is supposed 
		to send when the milk will be added to the coffee. For now, it
		sends a not implemented error.
		"""
		
		#If the request is bad, the headers are already sent,
		#so we can return.
		if self.is_bad_HTCPCP_request():
			return
		
		self.send_not_implemented("This coffee pot isn't able to add milk to your coffee.")


#TODO: GREG GO ON FROM HERE
	def do_BREW(self):
		"""
		This method implements the BREW HTCPCP method. This
		method is use to send command to the coffee pot. There 
		is actualy only the start and stop command wich are
		implemented with the messsage/coffeepot content-type.

		If the content-type header is set to 
		application/coffee-pot-command, a not implemented error
		is sent.

		If the content-type header is set to another type,
		a 400 error is sent.
		"""

		#If the request is bad, the headers are already sent,
		#so we can return.
		if self.is_bad_HTCPCP_request():
			return
		
		length = int(self.headers.getheader('content-length'))        
		data_string = self.rfile.read(length).strip()
		if self.headers.getheader('content-type').strip() == "message/coffeepot":
			if data_string == "start":
				if self.pot.brew():
					self.send_OK("The coffee is started.")
				else:
					self.error("The coffee pot is already started.")
			elif data_string == "stop":
				if self.pot.stopBrewing():
					self.send_OK("The coffee pot is stopped.")
				else:
					self.error("The coffee pot is already stopped.")
			else:
				self.error("The content-type header is not correctly set for this body.")
		elif self.headers.getheader('content-type').strip() == "application/coffee-pot-command":
			self.send_not_implemented("There is no coffee-pot-command available.")
		else:
			self.error("The content-type is not valid for this coffee pot.")

	def send_OK(self, response = ''):
		"""
		This method send the 200 code, end the headers
		and write the message in the page.
		"""

		self.send_response(200)
		self.end_headers()
		self.wfile.write(response)

	def error(self, error, message = ""):
		"""
		This method send the 400 error code, end the headers
		and write the message in the error page.
		"""

		self.send_error(400, error)
		self.end_headers()
		self.wfile.write(message)

	def send_not_implemented(self, error, message = ""):
		"""
		This method send the 501 error code, end the headers
		and write the message in the error page.
		"""

		self.send_error(501, error)
		self.end_headers()
		self.wfile.write(message)
	
	def send_safe_header(self, condition = 'yes'):
		"""
		This method send the Safe header with the condition
		in parameter. The default condition is 'yes'.
		"""

		self.send_header("Safe", condition)

	def is_bad_HTCPCP_request(self):
		"""
		This method is used in all HTTP method to know if the
		query of the client is bad with this implementation
		of the HTCPCP protocol. If the request is bad, it send
		the HTTP error to the client and end the headers.

		For example, if the TEAPOT configuration is set to True,
		the 418 code is sent and the headers are ended.

		If the headers are bad, this method return False; in 
		other case True.
		"""

		return self.is_teapot() or self.is_not_acceptable()

	def is_teapot(self):
		"""
		This method verify if the TEAPOT configuration is set to
		True. If yes, the 418 error code is sent and headers are
		ended. This method return True if TEAPOT is set to True;
		False in other case.
		"""

		if self.TEAPOT == True:
			self.send_error(418, "I'm a teapot")
			self.end_headers()
		return self.TEAPOT

	def is_not_acceptable(self):
		"""
		This implementation of HTCPCP doesn't support additions.
		So, if Accept-Addtions header is set to a not empty string, 
		this method send the 406 error code, end the headers and 
		return True. If Accept-Additions is not set or is set to
		an empty string, this method only return False.
		"""

		accept_additions = self.headers.getheader("Accept-Additions")
		if accept_additions is not None and accept_additions.strip():
			self.send_error(406, "Not Acceptable")
			self.end_headers()
			return True
		
		return False

	def get_called_page(self):
		"""
		This method return the page called by the client without
		any slash in the begining or the end of the name page. The
		name is also url decoded.
		"""

		p = urllib.unquote_plus(self.path)
		p = p.strip()
		p = p.strip("/")
		return p

