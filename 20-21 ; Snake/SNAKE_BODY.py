from turtle import Turtle

STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """- make the snake move as a whole, chain them together.
    - iterating over the segments and make the last in chain to go to the location of the one before it.
    - iterate over range of (refers to the last segment of the chain, stop at the first seg, step of -1 meaning the iteration will -1 the num of len(segments)
    - if we had started from the first then by default it would continue +1 but because we are starting at the end we need to tell it to move backwards.
    - (time of iteration, where to start, were to end)"""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            #get cordination of the seg in front
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            #sending the current segment to the location of the seg in front
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def go_through_wall_left(self,x,y):
        self.head.goto(x-585,y)

    def go_through_wall_right(self,x,y):
        self.head.goto(x+585,y)

    def go_through_wall_up(self,x,y):
        self.head.goto(x, y -585)

    def go_through_wall_down(self, x, y):
        self.head.goto(x, y +585)
