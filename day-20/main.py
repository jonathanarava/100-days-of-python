from turtle import Screen
import time, Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color: black
screen.title("My Snake Game")
screen.tracer(0)

# TODO 1: Create a snake body
snake = Snake.Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO 2: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# TODO 3: Control the snake


# TODO 4: Detect collisions with food


# TODO 5: Create a scoreboard


# TODO 6: Detect collision with wall


# TODO 7: Detect collision with tail


screen.exitonclick()
