import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

BOUNDARY = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color: black
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# TODO 2: Move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 15:  # snake is within 15 pixels of the food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO 6: Detect collision with wall
    if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
        game_is_on = False
        scoreboard.game_over()

    # TODO 7: Detect collision with tail
    """
    # Approach 1
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    """
    # Approach 2: slicing (skips the head)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
