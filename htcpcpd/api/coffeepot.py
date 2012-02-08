#!/usr/bin/env python2
"""
This file contains the CoffeePot class.
Author: Frédérik Paradis
"""

import re
import serial
import consts

class CoffeePot:
	"""
	This class is an API to communicate with a coffee pot
	trough a Arduino device. It use the serial port with
	pyserial module.
	"""
    
	def __init__(self, device):
		"""
		This method open the serial connection with the
		Arduino serial device specified in parameter.
		"""

		self.pot = serial.Serial(device, 9600)
		if not self.pot.isOpen():
			raise Exception('Coffee pot is not connected!')
	
	def __del__(self):
		"""
		This method close the connection to the Arduino.
		"""

		self.close()

	def close(self):
		"""
		This method close the connection to the Arduino.
		"""
		
		if self.pot.isOpen():
			self.pot.close()

	def brew(self):
		"""
		This method start the coffee brewing. If the coffee
		brewing was already started, this method return
		False; otherwise True.
		"""
		
		return self.sendAndReceive(consts.BREW_COFFEE)

	def stopBrewing(self):
		"""
		This method stop the coffee brewing. If the coffee
		brewing was already stopped, this method return
		False; otherwise True.
		"""
		return self.sendAndReceive(consts.STOP_BREWING)

	def isCoffeeBrewing(self):
		"""
		This method return True if the coffee is brewing; False
		otherwise.
		"""

		return self.sendAndReceive(consts.IS_COFFEE_BREWING)

	def getNbLitres(self):
		"""
		This method return the number of litres there is
		in the recipient.
		"""
		
		self.pot.write(consts.WATER_STATUS['message'] + '\n')
		
		line = self.pot.readline().strip()
		
		if line != consts.WATER_STATUS['statuses']['bad']:
			print line
			return int(re.findall(consts.WATER_STATUS['statuses']['good'], line)[0])
		else:
			return 0
	
	def isEmpty(self):
		"""
		This method return True if there is no water in the 
		recipient of the coffee pot; otherwise False.
		"""

		return self.getNbLitres() == 0
	
	def hasPot(self):
		"""
		This method return True if the pot is in the coffee
		pot; otherwise False.
		"""
		
		return self.sendAndReceive(consts.POT_STATUS)
		
	def sendAndReceive(self, message):
		"""
		This method send the message element in the dictionnary 
		specified in parameter, receive a line from the serial 
		port and compare it to the ['statuses']['good'] element
		in the dictionnary. It return True if the if the lines
		are same; otherwise False.
		"""
		
		self.pot.write(message['message'] + '\n')
		line = self.pot.readline().strip()
		return line == message['statuses']['good']

