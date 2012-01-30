from cmd import *
from pycurl import *
import StringIO

class HTCPCPClient(Cmd):
	
	def __init__(self, host):
		Cmd.__init__(self)
		self.prompt = "CoffeePot> "
		self.url = 'http://' + host[0] + ':' + str(host[1]) + '/'

	def do_brew(self, line):
		self.brew_command("start")

	def do_stop(self, line):
		self.brew_command("stop")

	def do_status(self, line):
		pass
	
	def do_water(self, line):
		pass
	
	def do_bucket(self, line):
		pass
	
	def do_quit(self, line):
		return True

	do_exit = do_quit
	do_EOF = do_quit
	help_EOF = do_quit

	def brew_command(self, command):
		c = Curl()
		c.setopt(URL, self.url)
		c.setopt(CUSTOMREQUEST, "BREW")
		c.setopt(POST, 1)
		c.setopt(POSTFIELDS, command) 
		c.setopt(HTTPHEADER, ["Content-Type: message/coffeepot"])
		print self.get_line(c)
		c.close()

	def get_line(self, c):
		b = StringIO.StringIO()
		c.setopt(WRITEFUNCTION, b.write)
		c.perform()
		return b.getvalue()

client = HTCPCPClient(('localhost', 8000))
client.cmdloop()
