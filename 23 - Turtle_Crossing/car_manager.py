import random
import time
from turtle import Turtle
import datetime
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100

#difficulty parameters
start_screen = 30



class CarManager:

    def __init__(self):
        self.all_cars = []
        # difficulty parameters
        self.chance = set()
        self.start_screen = 30
        # self.time_last_make = datetime.datetime.now()    ------ set car spawn by time not by chance


    def make_cars(self):
        # if datetime.datetime.now()- self.time_last_make >= datetime.timedelta(seconds=1):
        random_chance = random.randint(1,6)
        if random_chance in self.chance:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.penup()
            new_car.goto(x=230, y=random.randint(-250, 250))
            self.all_cars.append(new_car)
            self.level_spawn = 1
            # self.time_last_make = datetime.datetime.now()

            # difficulty parameters
            self.start_screen = 30

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def make_first_screen(self):
        for i in range(start_screen):
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.penup()
            new_car.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def raise_level(self,scoreboard_level):
        self.chance.add(scoreboard_level)
        print(self.chance)



