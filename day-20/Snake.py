from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Creates a 3 segment snake."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Snake segments moves implicitly except head segment."""
        for seg_index in range(len(self.segments) - 1, 0, -1):  # range(2,0,-1)
            self.segments[seg_index].goto(self.segments[seg_index - 1].position())

        self.segments[0].forward(MOVE_DISTANCE)  # head of snake moved explicitly

    headings = [0, 90, 180, 270]

    def up(self):
        current_heading = self.segments[0].heading()
        if current_heading == 0:
            self.segments[0].setheading(90)  # North: 90
        elif current_heading == 180:
            self.segments[0].setheading(90)  # North: 90
        self.move()

    def down(self):
        current_heading = self.segments[0].heading()
        if current_heading == 0 or current_heading == 180:
            self.segments[0].setheading(270)  # South: 270
        self.move()

    def left(self):
        current_heading = self.segments[0].heading()
        if current_heading == 0 or current_heading == 90 or current_heading == 180:
            self.segments[0].setheading(current_heading + 90)
        elif current_heading == 270:
            self.segments[0].setheading(180)

    def right(self):
        current_heading = self.segments[0].heading()
        if current_heading == 90 or current_heading == 180:
            self.segments[0].setheading(current_heading - 90)
        elif current_heading == 0:
            self.segments[0].setheading(270)
        elif current_heading == 270:
            self.segments[0].setheading(0)
