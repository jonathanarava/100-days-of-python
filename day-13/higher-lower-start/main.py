from art import logo, vs
from game_data import data
from random import choice
from replit import clear

correct_response = True
score = 0

def correct_response(account1, account2, response):
	"""Takes the user's guess and account1 and account2 follower count"""
	# Assuming no 2 account have the same follower count
	if account1['follower_count'] > account2['follower_count']:
		return response  == 'a'
	else:
		return response  == 'b'


def display_person_info(person):
	"""Format the account data into printable format."""
	return f"{person['name']}, {person['description']}, from {person['country']}."

# Main
print(logo)
account_1 = choice(data)
print(f"Compare A: {display_person_info(account_1)}")

while True:
	account_2 = choice(data)

	# In case the randomly selected acc. 2 is the same as acc. 1
	while account_1 == account_2:
		account_2 = choice(data)
	
	print(vs)
	print(f"Against B: {display_person_info(account_2)}")
	response  = input("Who has more followers? Type 'A' or 'B': ").lower()

	clear()
	print(logo)

	# Correct repsonse
	if correct_response(account_1, account_2, response):
		score += 1
		print(f"You're right! Current score: {score}")
	
	# Incorrect response
	else:
		print(f"Sorry, that's wrong. Final score: {score}")
		break

	# Swap previous round's acc. 2 to be next round's acc. 1
	account_1 = account_2
	print(f"Compare A: {display_person_info(account_1)}")