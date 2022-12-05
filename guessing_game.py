
import random

print("Hello brave soul! I see you are on a quest to guess the random number!")
high_score = 100

def start_game():
	global high_score # w3schools.com/python/python_variables_global.asp
	num = random.randint(1, 50) 
	guess_count = 1
	guess = input("I invite thee to guess a number between 1 and 50.  ")
	
	while True:
		try:
			guess = int(guess)
			if guess < 1 or guess > 50:
				raise IndexError("Oops! Make sure to enter a number between 1 and 50! Please do try again.  ")
			
		except IndexError as err:
			guess = input(f"{err}")

		except ValueError:
			guess = input("Oops! Make sure to enter whole numbers only! Please do try again.  ")

		else:	
			if guess > num:
				guess = input("'Tis lower! Guess again!  ")
			elif guess < num:
				guess = input("'Tis higher! Guess again!  ")
			elif guess == num:
				print(f"Huzzah! Thou hast guessed the random number in just {guess_count} attempts!")
				break
			guess_count += 1 	
	
	while True:
		try:
			guess_again = input("Wouldst thou like to guess another number? (Enter 'yes' or 'no')  ").lower()

			if guess_again == "yes": 
				if guess_count <= high_score:
					high_score = guess_count
				print(f"Thy current best score is {high_score}!")
				start_game() 
				break
			elif guess_again =="no": 
				print("Your quest for the random number has ended in triumph! Go forth this day with your head held high!") 
				break
			else:
				raise IndexError
		
		except IndexError:
			print("Please answer 'yes' or 'no'.  ") 


start_game()
