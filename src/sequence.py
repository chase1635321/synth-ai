#!/usr/bin/env python2

from live import *
import logging
import mido
import random
from notes import *

class Sequence:
	sequence = []
	length = 0
	note_lengths = [1, 2, 3, 4, 5, 6, 7, 8]

	ONE = 1; TWO = 2; THREE = 3; FOUR = 4; FIVE = 5; SIX = 6; SEVEN = 7
	SCALE = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN]

	# Moods: dark/bright, 
	def __init__(self, length=8, note_length=(1/16, 1/4)):
		print(" > Created note sequence object")
		self.length = length
		self.note_lengths = self.note_lengths[0:1]
		self.generate()

		notes = Notes()

	
	def generate(self):
		print(" >> Generating notes")
		self.sequence = []
		i = 0
		for i in range(0, self.length):
			self.sequence.append((random.choice(self.SCALE), 1./16))
	
	def get(self):
		return self.sequence
	