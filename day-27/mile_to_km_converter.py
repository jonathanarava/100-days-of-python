from tkinter import *

FONT = ("Arial", 10, "bold")


def convert_m_to_km():
    km = round(float(input.get()) * 1.609, 2)
    km_value_label['text'] = km
    return km


# Creating a new window and configurations
window = Tk()
window.title("My first GUI Program")
window.minsize(width=280, height=100)
window.config(padx=50, pady=50)

# Entry
input = Entry(width=7)
print(input.get())
input.grid(column=1, row=0)

# Labels
m_label = Label(text="Miles")
m_label.grid(column=2, row=0)

left_label = Label(text="is equal to")
left_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Buttons
calculate_button = Button(text="Calculate", font=FONT, command=convert_m_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
