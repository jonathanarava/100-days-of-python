from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal", "bold")


# TODO 5: Create a scoreboard
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1  # offset
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)  # top of the screen
        self.increase_score()

    def update_scoreboard(self):
        self.write("Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
