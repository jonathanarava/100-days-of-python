from turtle import Turtle as t, Screen, colormode
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

colormode(255)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

""" Painting requirements:
    dimensions: 10 (dots) x 10 (dots)
    dot size: 20 (diameter)
    distance between dots: 50 """

timmy = t()
timmy.speed('fastest')
timmy.hideturtle()
timmy.penup()


def hirst_painting(dimension, dot_size, dot_dist):

    def starting_position():
        length = ((dot_size * (dimension - 1) + (dot_dist * (dimension - 1))) / 2)
        return timmy.xcor() - length, timmy.ycor() - length

    start_x, start_y = starting_position()
    timmy.setpos(start_x, start_y)

    for _ in range(dimension):
        for _ in range(dimension):
            # draws a line of dots
            timmy.dot(dot_size, random.choice(color_list))
            timmy.forward(dot_dist)
        timmy.setpos(start_x, start_y + dot_dist)   # turtle is at the starting position of the next line
        start_y = timmy.ycor()  # starting y position is updated for next iteration


hirst_painting(dimension=10, dot_size=20, dot_dist=50)

screen = Screen()
screen.exitonclick()
