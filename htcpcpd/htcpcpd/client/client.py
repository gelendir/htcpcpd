#!/usr/bin/env python2
# -*- coding: utf-8 -*-
""" 
This file contains the HTCPCPClient class.
Author: Frédérik Paradis
"""

import sys
from cmd import *
from pycurl import *
import StringIO

class HTCPCPClient(Cmd):
	"""
	This class is a command line utility to communicate
	with the actual HTCPCP server.
	"""	

	def __init__(self, host):
		""" 
		Initialize the command line with the tuple in parameter.
		The tuple must have to object: (host, port).
		"""
		Cmd.__init__(self)
		self.prompt = "CoffeePot> "
		self.url = 'http://' + host[0] + ':' + str(host[1]) + '/'

	def do_brew(self, line):
		""" 
		Start the coffee brewing. There is an error
		if the coffee brewing is already started.
		"""
		self.brew_command("start")

	def do_stop(self, line):
		""" 
		Stop the coffee brewing. There is an error
		if the coffee brewing is already stopped.
		"""
		self.brew_command("stop")

	def do_status(self, line):
		""" 
		Show the brewing status of the coffee pot.
		"""
		self.curl_query("status")
	
	def do_water(self, line):
		""" 
		Show the quantity of water in litre in the
		coffee pot.
		"""
		self.curl_query("water")
	
	def do_pot(self, line):
		""" 
		Show if the pot is in the machine or not.
		"""
		self.curl_query("pot")

	def do_resume(self, line):
		""" 
		Show many information on the coffee pot.
		"""
		pass

	def do_quit(self, line):
		"""
		Exit the HTCPCP command line client.
		"""
		return True

	do_exit = do_quit
	do_EOF = do_quit

	def emptyline(self):
		""" 
		Do nothing when an empty line is submit
		"""
		pass

	def brew_command(self, command):
		"""
		This method send a BREW message to the HTCPCP server
		with the content-type header to message/coffeepot.
		"""
		c = Curl()
		c.setopt(URL, self.url)
		c.setopt(CUSTOMREQUEST, "BREW")
		c.setopt(POST, 1)
		c.setopt(POSTFIELDS, command) 
		c.setopt(HTTPHEADER, ["Content-Type: message/coffeepot"])
		print self.get_line(c)
		c.close()

	def curl_query(self, page):
		""" 
		This method call the HTCPCP server with the page
		in parameter.
		"""
		c = Curl()
		c.setopt(URL, self.url + page)
		print self.get_line(c)
		c.close()

	def get_line(self, c):
		"""
		This method call the perform method of the curl
		object in parameter and return the page result 
		associated.
		"""
		b = StringIO.StringIO()
		c.setopt(WRITEFUNCTION, b.write)
		c.perform()
		return b.getvalue()

#The default host and port
host = 'localhost'
port = 8000

#Parsing the argument of the command line
if len(sys.argv) in [2, 3]:
	host = sys.argv[1]

	if len(sys.argv) == 3:
		if sys.argv[2].isdigit():
			port = int(sys.argv[2])
		else:
			print "usage: " + sys.argv[0] + " [host [port]]"
			sys.exit(1)


if __name__ == "__main__":
    #We start the command line
    client = HTCPCPClient((host, port))
    client.cmdloop()

