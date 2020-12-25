#Calculator
from art import logo

#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def subtract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2

def initializeCalculator():
	num1 = float(input("What's the first number: "))
	for symbol in operations:
		print(symbol)
	return num1

def calculate(num1, operation_symbol, num2):
	calculation_function = operations[operation_symbol]
	return calculation_function(num1, num2)


operations = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide,
}



def calculator():
	continue_calculating = "y"
	num1 = initializeCalculator()

	while continue_calculating == "y":
		operation_symbol = input("Pick an operation from the line above: ")
		num2 = float(input("Pick the next number?: "))

		answer = calculate(num1, operation_symbol, num2) 
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start over.: ") == "y":
			num1 = answer
		else:
			calculator()

print(logo)
calculator()