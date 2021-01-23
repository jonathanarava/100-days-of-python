from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def end_game():
    """Game ended. Ball stops moving."""
    global game_is_on
    game_is_on = False


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(end_game, "x")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Player misses ball
    if ball.out_of_bounds():
        if ball.xcor() > 0:
            # ball is on the right side when missed by paddle
            scoreboard.l_scored()

        elif ball.xcor() < 0:
            # ball is on the left side when missed by paddle
            scoreboard.r_scored()
        ball.move_speed = 0.1  # reset speed
        ball.setheading(180 - ball.heading())
        ball.goto(0, 0)

    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        print("collision")
        ball.increase_speed()
        new_heading = 180 - ball.heading()
        ball.setheading(new_heading)

screen.exitonclick()
