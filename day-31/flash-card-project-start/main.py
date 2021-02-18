from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
random_row = None
DURATION = 3

""" 
Implementation: default file 'words_to_learn.csv'. If word is not 
known, it is added to default file and drops the word from game
(only when using 'french_words.csv')
"""


# Improvement added : if button is pressed during the 3s, a new random row is selected but timer is not refreshed
# Issue: leading comma in created .csv file (fixed)
# Improvement: checks if item exists in .csv file before inserting into it

# ---------------------------- BUTTON FUNCTIONS ------------------------------- #
def correct():
    global random_row, data_df

    try:
        row_index = random_row.index.item()
        data_df = data_df.drop(row_index)

    except KeyError:
        print("Item already removed")

    next_card()


def incorrect():
    # add words to file
    with open(file="data/words_to_learn.csv", mode='a') as file:
        file.write(f"{random_row.French.item()}, {random_row.English.item()}\n")

    next_card()


# ---------------------------- CARD NEXT/FLIP and DISPLAY MECHANISM ------------------------------- #
def next_card():
    global random_row, flip_timer

    try:
        window.after_cancel(flip_timer)
    # Canceling timer throws error the first time next_card() is used as flip_timer is not initialized
    except ValueError:
        pass
    canvas.itemconfig(word, fill='black')
    canvas.itemconfig(title, fill='black')

    try:
        random_row = data_df.sample()
    except ValueError as msg:
        print(msg)

    canvas.itemconfig(card, image=card_front)
    update_info(random_row, False)

    flip_timer = window.after(3000, func=flip_card)  # 3 sec: 3000


def flip_card():
    canvas.itemconfig(word, fill='white')
    canvas.itemconfig(title, fill='white')
    canvas.itemconfig(card, image=card_back)
    update_info(random_row, True)


def update_info(selected_row, show):
    """show: boolean to show answer (english) """
    # French
    if not show:
        canvas.itemconfig(title, text="French")
        canvas.itemconfig(word, text=selected_row.French.item())
    # English
    elif show:
        canvas.itemconfig(title, text="English")
        canvas.itemconfig(word, text=selected_row.English.item())


# ------------------------ GUI SETUP ------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)

# IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)  # create_image returns a item id
title = canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right = PhotoImage(file="images/right.png")
correct_button = Button(image=right, highlightthickness=0, command=correct)
correct_button.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=incorrect)
wrong_button.grid(row=1, column=0)

# ------------------------ DATA SETUP ------------------------

try:
    data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pandas.read_csv("data/french_words.csv")

    # Creates a new csv file using pandas
    to_learn_file = pandas.DataFrame(columns=['French', 'English'])
    to_learn_file.to_csv("data/words_to_learn.csv", index=False)

if not data_df.empty:
    next_card()

window.mainloop()
