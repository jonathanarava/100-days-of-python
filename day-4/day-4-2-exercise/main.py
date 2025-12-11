import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Generates random numbers between 0 and last item index
random_person = random.randint(0, (len(names) - 1))

print(f"{names[random_person]} is going to buy the meal today.")
