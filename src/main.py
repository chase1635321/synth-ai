#!/usr/bin/env python3

import logging
import os
from set import *
from termcolor import colored

logging.basicConfig(format="%(asctime)-15s %(message)s")
logging.getLogger("live").setLevel(logging.INFO)

#------------------------------------------------------------------------
# Definitions
#------------------------------------------------------------------------

KEY = 0
BPM = random.randint(110, 145)

#------------------------------------------------------------------------
# Global variables
#------------------------------------------------------------------------

def main():
	os.system("clear")
	print(colored("Running main", "green"))

	""" chords = Sequence(length=4, note_length=(4, 4))
	print(str(chords.get()))
	melody = Sequence(length=8, note_length=(1/16, 1/16))
	print(str(melody.get())) """

	set = LiveSet()
	seek_x = (0, 0)
	seek_y = (0, 0)

	while True:
		print(colored("[", "yellow") + colored(set.tracks[seek_x[0]].name, "green") + colored("::", "yellow") + colored("chorus", "green") + colored("]> ", "yellow"), end="")
		command = input().split(" ")

		if command[0] == "q" or command[0] == "exit":
			exit()
		if command[0] == "c" or command[0] == "clear":
			os.system("clear")
		if command[0] == "tl":
			i = 0
			for track in set.tracks:
				print(colored(str(i), "yellow") + " " + colored(track.name, "white"))
				i += 1
		if command[0] == "tlv":
			i = 0
			for track in set.tracks:
				print(colored(str(i), "yellow") + " " + colored(track.name, "white"))
				j = 0
				for clip in track.clips:
					print(" " + colored(str(j), "yellow") + " " + colored(clip.name, "white"))
					j += 1
				i += 1
		if command[0] == "tn":
			if len(command) < 3:
				print("Usage: tn <index|name> <new name>")
			else:
				i = 0
				for track in set.tracks:
					if track.name == command[1] or track.name == i:
						temp = track.name
						track.name = command[2]
					i += 1
				print(temp + " -> " + command[2])
		if command[0] == "r":
			print("Unimpelemented, would start recording")
		if command[0] == "s":
			if len(command) == 2 or len(command) == 3:
				arg = "".join(command[1:])
				if "," in arg:
					string_x = arg.split(",")[0].replace(" ", "")
					string_y = arg.split(",")[1].replace(" ", "")

					i = 0
					for track in set.tracks:
						if string_x.lower() in track.name.lower():
							seek_x = (i, i)
						i += 1
				else:
					i = 0
					for track in set.tracks:
						if arg.lower() in track.name.lower():
							seek_x = (i, i)
						i += 1
		if command[0] == "rl":
			print("Listing rows")

			# Seek if arg in command, if multiple tracks match arg, fail and print those
			# Can seek in 2 dimensions, generate commands operate at seek level
			# Regenerate commands with constraints, like higher, lower, slower, faster, etc

def print_main(s):
	print(colored("[", "yellow") + "main" + colored("]", "yellow") + s)

main()