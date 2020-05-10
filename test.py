#!/usr/bin/env python2

from live import *
import logging
import mido
import random

# Synth, pad, bass, midrange arp, side arps
# First add code to generate several dynamics for bass, pads, etc
# Then add "play" code that triggers clips to make a recording
# Make graph of how notes naturally pull, make chords/melodies by choosing groups of 4 from the graph. Build graph programatically.

logging.basicConfig(format="%(asctime)-15s %(message)s")
logging.getLogger("live").setLevel(logging.INFO)

#------------------------------------------------------------------------
# Definitions
#------------------------------------------------------------------------

transposition = 24

ONE_CHORD = 0 + transposition
TWO_CHORD = 2 + transposition
THREE_CHORD = 4 + transposition
FOUR_CHORD = 5 + transposition
FIVE_CHORD = 7 + transposition
SIX_CHORD = 9 + transposition
SEVEN_CHORD = 11 + transposition

CHORDS = [ONE_CHORD, TWO_CHORD, THREE_CHORD, FOUR_CHORD, FIVE_CHORD, SIX_CHORD]

KEY = 0
BPM = random.randint(110, 145)

#------------------------------------------------------------------------
# Global variables
#------------------------------------------------------------------------

set = Set()
set.scan(scan_clip_names=True, scan_devices=True)
synth = set.tracks[0]
pad = set.tracks[1]
bass = set.tracks[2]
print(set.tracks)

intro_chords = [ONE_CHORD, ONE_CHORD, FOUR_CHORD, FOUR_CHORD]
verse_chords = [SIX_CHORD, SIX_CHORD, FOUR_CHORD, FOUR_CHORD]
chorus_chords = [FOUR_CHORD, FIVE_CHORD, SIX_CHORD, SIX_CHORD]

#------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------

def main():
	deleteClips()
	setBPM()
	generateLead()
	generateBass()

def setBPM():
	set.tempo = BPM
	set.time = 0

def generateLead():
	for i in range(0, 16):
		synth.create_clip(i, 16)
		synth.clips[i].name = "Default Name"

	# Adjust notes in melody to closest ones compatible with chord
	# Make melody add higher note in last iteration
	# Modulate melody repeat. Change notes in between runs
	# Chance of adding octave
	# Chance of jumping octave
	# Modulate suspensions
	# Choose from one of several note banks for melody. Second one is always higher

	melody = generateMelody()
	melody2 = generateMelody()

	for i in [3, 4, 7, 8, 9]:
		j = 0.0
		while j < 16:
			synth.clips[i].add_note(melody[int(j*4)], j, .5, 100)
			j += 0.25
	
	for i in [2, 7]:
		j = 0.0
		while j < 16:
			synth.clips[i].add_note(melody2[int(j*4)], j, .5, 100)
			j += 0.25

def generateMelody():
	notes1 = [ONE_CHORD, THREE_CHORD, SIX_CHORD, FIVE_CHORD]
	notes2 = [ONE_CHORD, THREE_CHORD, SIX_CHORD-12, SEVEN_CHORD-12]

	# Melody modulations
	# > Last round, replace high note with one of acceptable variations
	# Translate note depending on what the chord is to nearest compatible note in list

	melody = []
	for i in range(0, 16):
		melody.append(random.choice(notes2))
	if validMelody(melody):
		print("Found valid melody")
		return expandMelody(melody)
	else:
		print("Invalid melody, regenerating")
		return generateMelody()

def expandMelody(melody):
	return melody*16

def validMelody(melody):
	# Too many seven chords
	if melody.count(SEVEN_CHORD) > 2 or melody.count(SEVEN_CHORD-12) > 2:
		print(" > Too many sevens")
		return False
	# Too many two chords
	if melody.count(TWO_CHORD) > 1:
		print(" > Too many twos")
		return False
	
	for i in range(0, len(melody)):
		if melody[i] == TWO_CHORD:
			try:
				if melody[i+1] == TWO_CHORD:
					print(" > Twos folow each other")
					return False
			except:
				pass
	
	for i in range(0, len(melody)):
		if melody[i] == SEVEN_CHORD:
			try:
				if melody[i+1] == SEVEN_CHORD:
					print(" > Sevens folow each other")
					return False
			except:
				pass
	
	for i in melody:
		if melody.count(i) > 8:
			print(" > Too many duplicate notes")
			return False
	
	return True

def generateBass():
	# Will add walk downs if possible

	for i in range(0, 11):
		bass.create_clip(i, 16)
		bass.clips[i].name = "Default Name"

	for n in range(0, 4):
		bass.clips[0].add_note(intro_chords[n], n*4, 4, 100)
		bass.clips[0].name = "Intro"
	for n in range(0, 4):
		bass.clips[1].add_note(verse_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[2].add_note(verse_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[3].add_note(chorus_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[4].add_note(chorus_chords[n], n*4, 4, 100)

	for n in range(0, 4):
		bass.clips[5].add_note(intro_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[6].add_note(verse_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[7].add_note(verse_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[8].add_note(chorus_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[9].add_note(chorus_chords[n], n*4, 4, 100)
	for n in range(0, 4):
		bass.clips[10].add_note(intro_chords[n], n*4, 4, 100)

def deleteClips():
	for track in set.tracks[:3]:
		for i in range(0, 20):
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
