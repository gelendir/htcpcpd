#!/usr/bin/env python2
"""
This file contains all constants used to communicate
with the coffee pot trough the Arduino board.
Author: Frédérik Paradis
"""

#Start request to the Arduino.
BREW_COFFEE = {
	'message' : 'BREW DIS COFFEE PLZ',
	'statuses' : {
		'good' : '200 YES DIS COFFEE POT IZ BREWINGZ',
		'bad' : '500 I HAZ ALREADY COFFEE A BREWING'
	}
}

#Used to know the brewing status of the coffee.
IS_COFFEE_BREWING = {
	'message' : 'AR U BREWING COFFEEZ ?',
	'statuses' : {
		'good' : '210 I AIN\'T BREWING COFFEEZ',
		'bad' : '220 I\'M BREWING COFFEEZ'}
}

#Used to know how much water there is in the coffee pot.
WATER_STATUS = {
	'message' : 'I CAN HAZ MOAR WATER ?',
	'statuses' : {
		'good' : '200 I HAZ ([0-9]+) LEETEARZ',
		'bad' : '400 OE NOES !1! NO MOAR WATERZ'
	}
}

#Used to know if the pot is in the coffee pot.
POT_STATUS = {
	'message' : 'O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?',
	'statuses' : {
		'good' : '200 I HAZ YUR BUKKET',
		'bad' : '404 I AINT HAZ NO BUKKET'}
}

#Stop request to the Arduino.
STOP_BREWING = {
	'message' : 'OUCH OUCH! TIZ COFFEE IZ HAWT! STOP!',
	'statuses' : {
		'good': '200 COFFEE IZ STOP',
		'bad': '400 NO COFFEE BREWIN'
	} 
}

