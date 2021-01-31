# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

with open("Input/Names/invited_names.txt") as names:
    mailing_list = names.readlines()

for name in mailing_list:
    name = name.strip()  # strips '\n' at the end of each element
    new_letter = content.replace("[name]", name)
    file_name = "Output/ReadyToSend/" + "letter_for_" + str(name) + ".txt"
    with open(file_name, mode="w") as outbox:
        outbox.write(new_letter)
