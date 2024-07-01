from turtle import Turtle

class Boarder(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=80, outline=None)
        self.penup()
        self.goto(position)

