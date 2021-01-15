from turtle import Turtle
import random

FOOD_BOUNDARY = 270


class Food(Turtle):
    def __init__(self):
        super().__init__()  # inherits attributes and methods from Turtle super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(
            "fastest")  # speeds up the process of seeing the food getting created and moving to specified position
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY), random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY))
