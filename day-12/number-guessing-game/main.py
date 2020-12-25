from art import logo
import random

#### House Rules ###
# 1. User needs to guess number between 0 and 100
# 2. Difficulty:
#		a) Easy - User has 10 tries to guess number
#		b) Hard - User has 5 tries to guess number
# 3. After every guess, user is given hint on which 
#    direction to make next guess

NUM_EASY_ATTEMPTS = 10
NUM_HARD_ATTEMPTS = 5

def welcome_msg():
	print(logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")

def update_num_attempts(attempts):
	return attempts - 1

def direction_hint(number, guess, attempts):
	# Hints to the direction of the number
	if number > guess:
		msg = "Too low. "
	elif number < guess:
		msg = "Too high. "
	else:
		msg = "Number out of range 0 - 100. "
	
	if attempts == 0:
		# Last attempt used therfore reveal answer
		msg = msg + (f"The amswer was {number}.")
	else:
		msg = msg + ("\nGuess again.")
	print(msg)

def Number_Guessing_Game():
	welcome_msg()
	number = random.randint(0, 100)

	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

	if difficulty == "easy":
		attempts = NUM_EASY_ATTEMPTS
	elif difficulty == "hard":
		attempts = NUM_HARD_ATTEMPTS

	while attempts > 0:
		print(f"You have {attempts} attempts remaing to guess the number.")
		guess = int(input("Make aguess: "))
		attempts = update_num_attempts(attempts)
		if number == guess:
			# User guessed the correct number
			print(f"You got it! The number is {number}")
			return
		direction_hint(number, guess, attempts)

Number_Guessing_Game()


