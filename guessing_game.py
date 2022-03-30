"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

print("Hello brave soul! I see you are on a quest to guess the random number!")

num = random.randint(1, 50)

def start_game():
	guess_count = 1
	guess = (input("I invite thee to guess a number between 1 and 50.  "))
	while True:
		try:
			guess = int(guess)
			if guess < 1 or guess > 50:
				raise IndexError(("Oops! Make sure to enter a number between 1 and 50! Please do try again.  "))
			
		except IndexError as err:
			guess = input(f"{err}")

		except ValueError:
			guess = input("Oops! Make sure to enter numbers only! Please do try again.  ")

		else:	
			if guess > num:
				guess = input("'Tis lower! Guess again!  ")
			elif guess < num:
				guess = input("'Tis higher! Guess again!  ")
			elif guess == num:
				print(f"Huzzah! Thou hast guessed the random number in just {guess_count} attempts!")
				break
			guess_count += 1


start_game()

print("Your quest for the random number has ended in triumph! Go forth this day with your head held high!")





	#"""Psuedo-code Hints
	
	#When the program starts, we want to:
   # ------------------------------------
	#1. Display an intro/welcome message to the player.
	#2. Store a random number as the answer/solution.
	#3. Continuously prompt the player for a guess.
	  #a. If the guess greater than the solution, display to the player "It's lower".
	  #b. If the guess is less than the solution, display to the player "It's higher".
	
	#4. Once the guess is correct, stop looping, inform the user they "Got it"
		# and show how many attempts it took them to get the correct number.
	#5. Let the player know the game is ending, or something that indicates the game is over.
	
	#( You can add more features/enhancements if you'd like to. )
   # """
	# write your code inside this function.



# Kick off the program by calling the start_game function.
