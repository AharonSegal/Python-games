import time
from turtle import Screen
from turtle import Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player(screen)
car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.player_move_up, "space")
screen.onkeyrelease(player.player_stop, "space")


intervals = 0.5
car_speed = 0.05

game_is_on = True
car_manager.make_first_screen()
car_manager.raise_level(scoreboard.level)
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #SCOREBOARD
    scoreboard.update_scoreboard()

    # MAKE AND MOVE CARS
    car_manager.make_cars()
    car_manager.move_cars()

    #MOVE PLAYER UP
    if player.moving_up:
        player.sety(player.ycor() + 15)

    #DETECT COLISSION
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    #DETECT WIN_LEVEL
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level+= 1
        car_manager.raise_level(scoreboard.level)



screen.exitonclick()







