# File not found
# with open("a_file.txt") as file:
#    file.read()  #FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]    #KeyError: 'non_existent_key'

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]   #IndexError: list index out of range

# TypeError
# text = "abc"
# print(text + 5) #TypeError: can only concatenate str (not "int") to str

# Catching Exceptions + Raising error
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except FileNotFoundError:
    file = open("a_file.txt", mode='w')
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is a fake error.")


# Raising exception with BMI calculator example
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight/height ** 2
print(bmi)