#!/usr/bin/env python2

from live import *
import logging
import mido

# Synth, pad, bass, midrange arp, side arps
# First add code to generate several dynamics for bass, pads, etc
# Then add "play" code that triggers clips to make a recording
# Make graph of how notes naturally pull, make chords by choosing groups of 4 from the graph

logging.basicConfig(format="%(asctime)-15s %(message)s")
logging.getLogger("live").setLevel(logging.INFO)

#------------------------------------------------------------------------
# Definitions
#------------------------------------------------------------------------

ONE_CHORD = 0
TWO_CHORD = 2
THREE_CHORD = 4
FOUR_CHORD = 5
FIVE_CHORD = 7
SIX_CHORD = 9

KEY = 0
BPM = 120

#------------------------------------------------------------------------
# Global variables
#------------------------------------------------------------------------

set = Set()
set.scan(scan_clip_names=True, scan_devices=True)
synth = set.tracks[0]
pad = set.tracks[1]
bass = set.tracks[2]
print(set.tracks)

#------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------

def main():
	deleteClips()
	setBPM()
	generateLead()

def setBPM():
	set.tempo = BPM
	set.time = 0

def generateLead():
	for i in range(0, 4):
		synth.create_clip(i, 16)
		synth.clips[i].name = "Default Name"

	for i in range(0, 4):
		j = 0.0
		while j < 16:
			synth.clips[i].add_note(50, j, .25, 100)
			j += 0.25

def deleteClips():
	for track in set.tracks:
		for i in range(0, 8):
			try:
				track.delete_clip(i)	
			except Exception as e:
				#print(e)
				pass

def printClips():
	for clip in synth.clips:
		if not clip == None:
			print("\t" + clip.name)

	print("Setting up pad track:")
	for clip in pad.clips:
		if not clip == None:
			print("\t" + clip.name)

	print("Setting up bass track:")
	for clip in bass.clips:
		if not clip == None:
			print("\t" + clip.name)

def scanDevices():
	set.dump()

main()
