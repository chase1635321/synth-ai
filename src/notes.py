#!/usr/bin/env python2

from live import *
import logging
import mido
import random

class Notes:
	def __init__(self):
		ONE = Note("ONE", 0)
		TWO = Note("TWO", 1)
		THREE = Note("THREE", 2)
		FOUR = Note("FOUR", 3)
		FIVE = Note("FIVE", 4)
		SIX = Note("SIX", 5)
		SEVEN = Note("SEVEN", 6)

class Note:
	# Note pull/sequence tendencies graph
	# Dissonance value with each note

	def __init__(self, name, value):
		print("Created note " + name)

	
