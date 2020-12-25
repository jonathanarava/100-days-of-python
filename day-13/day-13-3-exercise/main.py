for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:	# change: or to and
    print("FizzBuzz")
  elif number % 3 == 0:	# change: if to elif
    print("Fizz")
  elif number % 5 == 0:	# change: if to elif
    print("Buzz")
  else:
    print(number)	# change: [number] to number
