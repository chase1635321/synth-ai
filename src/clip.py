#!/usr/bin/env python2

import logging
import mido
import random

class Clip:
	notes = []
	ableton_clip = None
	name = "Untitled"

	def __init__(self, ableton_clip):
		self.ableton_clip = ableton_clip
		self.name = self.ableton_clip.name
	
	


	
