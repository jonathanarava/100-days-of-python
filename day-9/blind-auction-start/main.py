from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

auction_tracker = {}
response = "yes"

def auction_winner(dictionary):
	winner = "" 
	max = 0
	for key in dictionary:
		if dictionary[key] > max:
		 	winner = key
		 	max = dictionary[key]

	print(f"The winner is {winner} with a bid of ${dictionary[winner]}")

print(logo)
print("Welcome to the secret auction program.")
    
while response == "yes":
	key = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))

	auction_tracker[key] = bid

	response = input("Are there any other bidders? Type 'yes' or 'no'.\n")

	if response == "yes":
		clear()
	
auction_winner(auction_tracker)