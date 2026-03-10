"""
program: music_player.py
3/9/2026

***MUST INSTALL PYGAME-CE before running this app!!!!***

at command prompt / terminal run: python3 -m pip install pygame-ce

simple command-line based music player that can play a standard .mp3 audio file.
"""

import pygame
import os

# Initialize the mixer module from pygame
pygame.mixer.init()

# Display a menu for our user interface
print("\nWelcome to the Python Music Player!")
print("Enter 1 to select a song file.")
print("Enter 2 to begin playing the chosen song.")
print("Enter 3 to pause  song.")
print("Enter 4 to unpause the song.")
print("Enter any other key to exit the program.")

# Loop and logic statements that determine which optio was entered and what to do.
while True:
	fileDir= os.path.dirname(os.path.abspath(__file__))

	menuChoice = input("Please select a menu option >>").strip()
	#Decision making that triggers the various features
	if menuChoice == "1":
		songFile= input("Please enter the song's filename >>")
		filePath= os.path.join(fileDir,songFile)
		pygame.mixer.music.load(filePath)
		print(f"song {songFile} loaded successfully!")
	elif menuChoice == "2":
		pygame.mixer.music.play()
	elif menuChoice == "3":
		pygame.mixer.music.pause()
	elif menuChoice == "4":
		pygame.mixer.music.unpause()
	else:
		pygame.mixer.music.stop()
		input("\n Thank you for using the music player. Press ENTER to exit.")
		break


		input()
