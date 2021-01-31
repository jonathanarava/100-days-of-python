# with open("my_file.txt") as file:      # file is of type '_io.TextIOWrapper'
#     contents = file.read()      # contents is of type 'str'
#     print(contents)

with open("my_file.txt", mode="a") as file:      # file is of type '_io.TextIOWrapper'
    file.write("\nnew_text")      # contents is of type 'str'
