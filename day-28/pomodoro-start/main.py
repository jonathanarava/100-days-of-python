from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)  # stops timer
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer", fg=GREEN)
    tick.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # 1st, 3rd, 5th, 7th
    if reps % 2 != 0:
        heading.config(text="Work", fg=GREEN)
        count_down(work_sec)


    # 2nd, 4th, 6th, 8th (special case)
    elif reps % 2 == 0:

        update_tick = tick["text"] + " ✔"
        tick.config(text=update_tick)
        if reps == 8:
            heading.config(text="Long Break", fg=RED)
            count_down(long_break_sec)
        else:
            heading.config(text="Short Break", fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = str(count % 60).zfill(2)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # 1 sec: 1000
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")  # tomato in italian
window.config(padx=100, pady=50, bg=YELLOW)

# Label: Heading
heading = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
heading.grid(column=1, row=0)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label: Tick
tick = Label(bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
tick.grid(column=1, row=3)

window.mainloop()
