from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    # Create the paddle object
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # Make paddle move up by 20 units
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Make paddle move down by 20 units
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
