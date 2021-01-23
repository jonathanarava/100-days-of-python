from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CAR_START_POSITION = 220
CAR_END_POSITION = -300


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.cars_speed = MOVE_INCREMENT

    def create_car(self):
        """Creates a car approximately every 1/6 time the while loop runs in the main."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = self.Car()
            new_car.speed = self.cars_speed  # sets the speed of the car
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.move()

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT    # increases the speed of the car when the next car is created
        for car in self.all_cars:       # increases the speed of the cars that are already created
            car.speed = self.cars_speed

    class Car(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.color(random.choice(COLORS))
            self.penup()
            self.setheading(180)
            self.goto(300, random.randrange(-CAR_START_POSITION, CAR_START_POSITION, 40))  # 11 lanes for cars
            self.speed = 0

        def move(self):
            if self.xcor() > CAR_END_POSITION:
                self.forward(self.speed)


