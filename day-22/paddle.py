from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")  # default: 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if position == "right":
            self.goto(x=350, y=0)
        elif position == "left":
            self.goto(x=-350, y=0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
