from turtle import Turtle

STARTING_POSITION = (0, 0)
BALL_W_BOUNDARY = 350 + 20  # paddle position (20: width of the ball)
BALL_H_BOUNDARY = 300 - 20  # half of screen height (20: width of the ball)
INCREASE_SPEED_FACTOR = 0.9  # 0.5, halves the speed each time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(40)  # arbitrary value: 40
        self.penup()
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= INCREASE_SPEED_FACTOR

    def out_of_bounds(self):
        """Player missed to hit the ball."""
        if self.xcor() < -BALL_W_BOUNDARY or self.xcor() > BALL_W_BOUNDARY:
            return True
        else:
            return False

    def move(self):
        self.forward(10)

        # Collision with the top and bottom wall
        if self.ycor() < -BALL_H_BOUNDARY or self.ycor() > BALL_H_BOUNDARY:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
