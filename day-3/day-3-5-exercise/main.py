# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name= (name1 +name2).lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

digit_one = t+r+u+e
digit_two = l+o+v+e

score = (digit_one*10) + digit_two

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score < 50 or score > 40:
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")