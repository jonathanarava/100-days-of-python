# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Leap Year:
# on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also #evenly divisible by 40

if year % 4 == 0:
  if year % 100 == 0:
    if year % 40 == 0:
      print("Leap Year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not a leap year.")