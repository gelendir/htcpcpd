from cmd import *
from pycurl import *
import StringIO

class HTCPCPClient(Cmd):
	
	def __init__(self, host):
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
	
	def do_bucket(self, line):
		""" 
		Show if the bucket is in the coffee pot or not.
		"""
		self.curl_query("bucket")

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

	def brew_command(self, command):
		c = Curl()
		c.setopt(URL, self.url)
		c.setopt(CUSTOMREQUEST, "BREW")
		c.setopt(POST, 1)
		c.setopt(POSTFIELDS, command) 
		c.setopt(HTTPHEADER, ["Content-Type: message/coffeepot"])
		print self.get_line(c)
		c.close()

	def curl_query(self, page):
		c = Curl()
		c.setopt(URL, self.url + page)
		print self.get_line(c)
		c.close()

	def get_line(self, c):
		b = StringIO.StringIO()
		c.setopt(WRITEFUNCTION, b.write)
		c.perform()
		return b.getvalue()

client = HTCPCPClient(('localhost', 8000))
client.cmdloop()
