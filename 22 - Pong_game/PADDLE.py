from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False
        self.speed("slowest")

    def r_paddle_move_up(self):
        self.moving_up = True

    def r_paddle_stop_up(self):
        self.moving_up = False

    def r_paddle_move_down(self):
        self.moving_down = True

    def r_paddle_stop_down(self):
        self.moving_down = False

    def l_paddle_move_up(self):
        self.moving_up = True

    def l_paddle_stop_up(self):
        self.moving_up = False

    def l_paddle_move_down(self):
        self.moving_down = True

    def l_paddle_stop_down(self):
        self.moving_down = False
