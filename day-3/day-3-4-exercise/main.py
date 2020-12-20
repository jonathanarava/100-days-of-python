# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small_pizza_cost = 15
med_pizza_cost = 20
large_pizza_cost = 25
extra_cheese_cost = 1

bill = 0

if size == "S":
  bill += small_pizza_cost
  if add_pepperoni == "Y":
    bill +=2

elif size == "M":
  bill += med_pizza_cost
  if add_pepperoni == "Y":
    bill +=3

elif size == "L":
  bill += large_pizza_cost
  if add_pepperoni == "Y":
    bill +=3

if extra_cheese == "Y":
  bill +=1

print(f"Your final bill is: {bill}")



