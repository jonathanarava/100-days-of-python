import random
import my_module

# Random whole number
# 1 - 10 (including intervals)
random_integer = random.randint(1,10)
print(random_integer)

#print(my_module.pi)

# Random floating point numbers
# 0.00000000 - 0.9999999... (not including 1)
random_float = random.random()
print(random_float)

# expand random floating point number range
random_number = random_float*5
print(random_number)