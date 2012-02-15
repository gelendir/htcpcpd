#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This file contains the CoffeePot class, the API for
controlling the coffee pot plugged onto the Arduino board.
Author: Frédérik Paradis
"""

import re
import serial
import consts

class CoffeePot:
	"""
	This class is an API to communicate with a coffee pot
	trough an Arduino device. It uses the pyserial module to
	communicate with the Arduino through a serial port.
	"""
    
	def __init__(self, device):
		"""
		This method opens the serial connection with the
		Arduino serial port. The serial port can be
		specified with the `device` parameter
		"""

		self.pot = serial.Serial(device, 9600)
		if not self.pot.isOpen():
			raise Exception('Coffee pot is not connected!')

	def __del__(self):
		"""
		This method deletes the CoffeePot instance
		"""

		self.close()

	def close(self):
		"""
		This method closes the connection to the Arduino.
		"""
		
		if self.pot.isOpen():
			self.pot.close()

	def brew(self):
		"""
		This method starts the coffee brewing. If the
		brewing has already been started, then
		False is returned; otherwise True.
		"""
		
		return self.sendAndReceive(consts.BREW_COFFEE)

	def stopBrewing(self):
		"""
		This method stops the coffee brewing. If the coffee
		pot is not brewing, then False is returned; 
		otherwise True.
		"""
		return self.sendAndReceive(consts.STOP_BREWING)

	def isCoffeeBrewing(self):
		"""
		This method returns True if the coffee pot is brewing; False
		otherwise.
		"""

		return self.sendAndReceive(consts.IS_COFFEE_BREWING)

	def getNbLitres(self):
		"""
		This method returns the number of water litres that
		are left in the water container.
		"""
		
		self.pot.write(consts.WATER_STATUS['message'] + '\n')
		
		line = self.pot.readline().strip()
		
		if line != consts.WATER_STATUS['statuses']['bad']:
			print line
			return int(re.findall(consts.WATER_STATUS['statuses']['good'], line)[0])
		else:
			return 0
	
	def	waterReading(self):
		"""
		Debug method to know the analogic reading
		of the captor of water.
		"""

		self.pot.write("WATER READING\n")
		return self.pot.readline().strip()

	def timeLeft(self):
		"""
		Debug function to know the time left of 
		the brewing timer.
		"""

		self.pot.write("TIME LEFT\n")
		return int(self.pot.readline().strip())

	def isEmpty(self):
		"""
		This method returns True if there is no water in the 
		water container of the coffee pot; otherwise False.
		"""

		return self.getNbLitres() == 0
	
	def hasPot(self):
		"""
		This method returns True if there is a pot
		on the coffee pot's sockle; otherwise False
		"""
		
		return self.sendAndReceive(consts.POT_STATUS)
		
	def sendAndReceive(self, message):
		"""
		This method is used to send and receive a message
		from the Arduino's serial port. The Arduino's response is compared
		to a dictionnary of statuses to check if it is valid or not.
		The method returns True if the response is valid, False otherwise.
		"""
		
		self.pot.write(message['message'] + '\n')
		line = self.pot.readline().strip()
		return line == message['statuses']['good']

