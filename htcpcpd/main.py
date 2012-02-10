#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This file start the HTCPCP server and deamonize it.
Author: Frédérik Paradis
"""

import fcntl
import os

class PidFile(object):
	"""Context manager that locks a pid file.  Implemented as class
	not generator because daemon.py is calling .__exit__() with no parameters
	instead of the None, None, None specified by PEP-343.
	Author: http://code.activestate.com/recipes/577911-context-manager-for-a-daemon-pid-file/ """
	# pylint: disable=R0903
	
	def __init__(self, path):
		self.path = path
		self.pidfile = None

	def __enter__(self):
		self.pidfile = open(self.path, "a+")
		try:
			fcntl.flock(self.pidfile.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
		except IOError:
			raise SystemExit("Already running according to " + self.path)
		self.pidfile.seek(0)
		self.pidfile.truncate()
		self.pidfile.write(str(os.getpid()))
		self.pidfile.flush()
		self.pidfile.seek(0)
		return self.pidfile

	def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
		try:
			self.pidfile.close()
		except IOError as err:
			# ok if file was just closed elsewhere
			if err.errno != 9:
				raise
		os.remove(self.path)

from server import *
import daemon

#PID_FILE = '/var/run/htcpcpd.pid'
PID_FILE = '/home/fredy/htcpcpd.pid'

with daemon.DaemonContext(files_preserve=[HTCPCPDImpl.pot.pot.fileno()], pidfile=PidFile(PID_FILE), stderr=open("/home/fredy/log.txt", "w+")):
	try:
		httpd = SocketServer.ThreadingTCPServer(('localhost', PORT), HTCPCPDImpl)
	
		#print "serving at port", PORT
		httpd.serve_forever()
	except KeyboardInterrupt:
		httpd.socket.close() 
	finally:
		httpd.server_close()

