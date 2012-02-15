#!/usr/bin/env python2
# -*- coding: utf-8 -*-
""" 
This file contains the HTCPCPClient class, used
to send requests to the HTCPCPD server.
Author: Frédérik Paradis
"""

import sys
from cmd import *
from pycurl import *
import StringIO

class HTCPCPClient(Cmd):
	"""
	This class is a command line utility to communicate
	with the actual HTCPCPD server.
	"""	

	def __init__(self, host):
		""" 
		Initialize the command line with the tuple as first parameter.
		The tuple must have the following form: (host, port).
		"""
		Cmd.__init__(self)
		self.prompt = "CoffeePot> "
		self.url = 'http://' + host[0] + ':' + str(host[1]) + '/'

	def do_brew(self, line):
		""" 
		Start the coffee brewing. Shows an error
		if the coffee pot is already brewing.
		"""
		self.brew_command("start")

	def do_stop(self, line):
		""" 
		Stop the coffee brewing. Shows an error
		if the coffee pot is not already brewing.
		"""
		self.brew_command("stop")

	def do_status(self, line):
		""" 
		Show the brewing status of the coffee pot.
		"""
		self.curl_query("status")
	
	def do_water(self, line):
		""" 
		Show the quantity of water litres left in the
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
		Display various information about the coffee pot.
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
		Do nothing when an empty line is submitted
		"""
		pass

	def brew_command(self, command):
		"""
		This method sends a BREW message to the HTCPCP server
		with the content-type header set to message/coffeepot.
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
		This method sends a request the HTCPCP server on the page
		specified as a parameter.
		"""
		c = Curl()
		c.setopt(URL, self.url + page)
		print self.get_line(c)
		c.close()

	def get_line(self, c):
		"""
		This method calls the perform method of the curl
		object in parameter and returns the result associated
		to the page."""
		b = StringIO.StringIO()
		c.setopt(WRITEFUNCTION, b.write)
		c.perform()
		return b.getvalue()


def main():
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

    #We start the command line
	client = HTCPCPClient((host, port))
	client.cmdloop()

if __name__ == "__main__":
	main()
