from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self ,screen):
        super().__init__()
        self.shape("turtle")
        self.color("gold")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.penup()
        self.go_to_start()
        self.moving_up = False
        self.speed("fastest")
        self.screen = screen
        self.left(90)

    def player_move_up(self):
        self.moving_up = True

    def player_stop(self):
        self.moving_up = False

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)




