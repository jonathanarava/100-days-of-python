import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=750, height=550)
screen.title("U.S. States Game")

# Register new shape (map of America)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")
data['guessed'] = False

typing_turtle = turtle.Turtle()
typing_turtle.penup()
typing_turtle.hideturtle()


def label_state(para_state, para_x_cor, para_y_cor):
    typing_turtle.goto(para_x_cor, para_y_cor)
    typing_turtle.write(para_state, align="center")


game_is_on = True
count = 0
limit = len(data)

while game_is_on:

    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"What's another state's name? {count}/{limit}").title()
    match = data[data.state == answer_state]
    if answer_state == "Exit":
        """ Display all the states. """
        typing_turtle.color('red')
        unmatched = data[data.guessed == False]

        unmatched.to_csv("states_to_learn.csv")

        for index, row in unmatched.iterrows():
            label_state(row['state'], row['x'], row['y'])

        screen.exitonclick() #waits for user to  click screen to exit (does not prompt user again)

    elif match.empty:
        """User inputted word is NOT a country."""
        pass

    else:
        """User inputted word IS a country."""
        count += 1
        """
        For debugging:
        print(type(match.index))
        print(match.index)
        print(match.index[0])  # match.index.item()
        print(type(match.index[0]))
        """

        index = match.index[0]  # <class 'numpy.int64'>

        state = match.state.item()  # match.values[0][0] or answer_state
        x_cor = int(match.x)  # match.values[0][1]
        y_cor = int(match.y)  # match.values[0][2]

        data.loc[index, 'guessed'] = True
        # print(data)

        label_state(str(state), x_cor, y_cor)

    if count == limit:
        game_is_on = False


# turtle.mainloop()