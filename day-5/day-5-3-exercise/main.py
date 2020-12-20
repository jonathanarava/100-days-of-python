#Write your code below this row 👇
sum = 0

for number in range(1, 101):
  if number % 2 == 0:
    sum += number
print(sum)

# Less robust solution
total = 0
for number in range(2, 101, 2):
  total += number
print(total)