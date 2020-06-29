#!/usr/bin/env python2

from live import *
from track import *

class LiveSet:
	tracks = []
	def __init__(self):
		set = Set()
		set.scan(scan_clip_names=True, scan_devices=True)

		for track in set.tracks:
			self.tracks.append(Track(track))

		print(set.tracks)
		print("Initialized set")

	


	
