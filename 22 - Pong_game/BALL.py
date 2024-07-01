from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        start_fly = self.xcor()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.x_move *= -1
        self.move_speed = 0.05

    def add_speed(self):
        self.move_speed *= 0.9

