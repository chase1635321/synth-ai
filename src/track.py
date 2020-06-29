#!/usr/bin/env python2

import logging
import mido
import random
from clip import *

class Track:
	clips = []
	ableton_track = None
	name = "Untitled"

	def __init__(self, ableton_track):
		self.ableton_track = ableton_track
		self.name = self.ableton_track.name

		for ableton_clip in ableton_track.clips:
			if not ableton_clip == None:
				self.clips.append(Clip(ableton_clip))
	
	


	
