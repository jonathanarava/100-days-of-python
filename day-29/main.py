from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    generated_password = password_generator.generate_password()
    password_entry.insert(END, string=generated_password)
    pyperclip.copy(generated_password)  # copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Gets text from entry fields
    data = {
        'website': website_entry.get(),
        'email_or_username': e_and_u_entry.get(),
        'password': password_entry.get()
    }

    # Check and notify user if necessary of empty fields
    if len(data['website']) == 0 or len(data['website']) == 0 or len(data['website']) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        # Prompt user for confirmation
        msg = f"""These are the details entered:\n 
        Email: {data['email_or_username']}
        Password: {data['password']}  
        \n Is it okay to save?"""
        is_ok = messagebox.askokcancel(title=data['website'], message=msg)

        if is_ok:
            # Saves data to local .txt file
            with open(file="data.txt", mode='a')as file:
                file.write(str(data) + "\n")

            # Clear website and password fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white')

# Image
canvas = Canvas(width=150, height=185, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(75, 90, image=logo_img)  # create_image returns a item id
canvas.grid(row=0, column=1)

# Label: Tick
website_l = Label(text="Website:", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
website_l.grid(column=0, row=1)

e_and_u_l = Label(text="Email/Username:", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
e_and_u_l.grid(column=0, row=2)

password_l = Label(text="Password", bg='white', highlightthickness=0, font=(FONT_NAME, 10, "bold"))
password_l.grid(column=0, row=3)

# Entries
website_entry = Entry(width=44)

website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()  # initiates cursor on entry field

e_and_u_entry = Entry(width=44)
# Add some text to begin with
e_and_u_entry.insert(END, string="JohnDoe@example.com")
e_and_u_entry.grid(column=1, row=2, columnspan=2, sticky='w')

password_entry = Entry(width=25)
# Add some text to begin with
# password_entry.insert(END, string="****")
password_entry.grid(column=1, row=3, sticky='w')

# Buttons
g_pass_button = Button(text="Generate Password", command=generate_password)
g_pass_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", width=37, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
