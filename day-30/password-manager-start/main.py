from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

FILE = "data.json"


# Possible improvements: error msg when password is attempted to be re-written

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    generated_password = password_generator.generate_password()
    password_entry.insert(END, string=generated_password)
    pyperclip.copy(generated_password)  # copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Gets text from entry fields
    website = website_entry.get().title()
    credentials = {'email_or_username': e_and_u_entry.get(),
                   'password': password_entry.get()}

    # Check and notify user if necessary of empty fields
    if len(website) == 0 or len(credentials['email_or_username']) == 0 or len(credentials['password']) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        data = {website: credentials}
        # Prompt user for confirmation
        msg = f"""These are the details entered:\n 
        Email: {data[website]['email_or_username']}
        Password: {credentials['password']}  
        \n Is it okay to save?"""
        is_ok = messagebox.askokcancel(title=website, message=msg)

        if is_ok:
            try:
                # # Saves data to local .txt file (optional)
                # with open(file="data.txt", mode='a')as file:
                #     file.write(str(data) + "\n")

                # Opens json file in read mode (json.load and json.update uses read mode)
                with open(FILE, 'r') as data_file:
                    # json.load
                    json_data = json.load(
                        data_file)  # Reading: gets data from json file (data_file), json_data type: dict

                    # json.update
                    json_data.update(data)  # Updating: added data (website, username, password) to variable (json_data)

            except FileNotFoundError:
                json_data = data

            finally:
                # Opens json file in write mode (json.dump uses write mode)
                # Writing: converts python dict (json_data) to json and saves to data_file
                with open(FILE, 'w') as data_file:
                    # json.dump
                    json.dump(json_data, data_file, indent=4)  # indent=4 : makes the file more human readable

                # Clear website and password fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def find_password():
    try:
        with open(FILE, "r") as data_file:
            json_data = json.load(data_file)

        website = website_entry.get().title()
        website_credentials = json_data[website]

    # Error Handling: Data File not found
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found.")

    # Error Handling: website details not found in Data File (website entry does not exist)
    except KeyError:
        messagebox.showerror(title="Oops", message="No details for the website exists.")

    else:
        msg = f"username: {website_credentials['email_or_username']} \n password: {website_credentials['password']}"
        messagebox.showerror(title=website, message=msg)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white')

# Image
canvas = Canvas(width=150, height=185, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(75, 90, image=logo_img)  # create_ima5ge returns a item id
canvas.grid(row=0, column=1)

# Label: Tick
website_l = Label(text="Website:", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
website_l.grid(column=0, row=1)

e_and_u_l = Label(text="Email/Username:", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
e_and_u_l.grid(column=0, row=2)

password_l = Label(text="Password", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
password_l.grid(column=0, row=3)

# Entries
website_entry = Entry(width=25)

website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()  # initiates cursor on entry field

e_and_u_entry = Entry(width=44)
e_and_u_entry.insert(END, string="JohnDoe@example.com")  # Add some text to begin with
e_and_u_entry.grid(column=1, row=2, columnspan=2, sticky='w')

password_entry = Entry(width=25)
# password_entry.insert(END, string="****")   # Add some text to begin with
password_entry.grid(column=1, row=3, sticky='w')

# Buttons
g_pass_button = Button(text="Generate Password", command=generate_password)
g_pass_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", width=37, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

search_button = Button(text="Search", width=14, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1, sticky='w')

window.mainloop()
