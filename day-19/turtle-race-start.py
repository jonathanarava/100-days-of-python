from turtle import Turtle, Screen
import random

""" Different from tutorial code (Dr. Angela Yu). In this code, the race does not stop when 
the winner reaches the finish line but when all the players have 
reached/ passed the finish line. In addition, each turtle is initiated with a unique name."""

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
john = Turtle(shape="turtle")
jane = Turtle(shape="turtle")
eric = Turtle(shape="turtle")
tribore = Turtle(shape="turtle")

turtles = [tim, tom, john, jane, eric, tribore]
i = 0
initial_position = -100
start_line = -230
end_line = 200

# Turtles are put in the starting position
for turtle in turtles:
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(start_line, y=initial_position)
    initial_position += 50
    i += 1

race_finished = False

while not race_finished:
    # Choose a turtle at random to move forward towards the finish line
    current_turtle = random.choice(turtles)
    current_turtle.forward(random.randint(0, 10))

    # Stops turtle at finish line
    if current_turtle.xcor() > end_line:    # '>' because of randint(0, 10)
        # first turtle to reach the finish line
        if len(turtles) == 6:
            winner = current_turtle
        turtles.remove(current_turtle)

    # All the turtles have reached the finish line
    if len(turtles) == 0:

        race_finished = True

if user_bet == winner.pencolor():
    print("Right bet!")
else:
    print(f"Wrong bet. The winner is the {winner.pencolor()} turtle.")

screen.exitonclick()
