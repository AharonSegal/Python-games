from turtle import Screen, Turtle
from SNAKE_BODY import Snake
from SNAKE_FOOD import Food
from SNAKE_SCORE import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)



#call snake,food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # #HIT WALL GAME_OVER
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()


    # go throght wall
    if snake.head.xcor() > 280:
        snake.go_through_wall_left(snake.head.xcor(),snake.head.ycor())
    elif snake.head.xcor() < -280:
        snake.go_through_wall_right(snake.head.xcor(), snake.head.ycor())
    elif snake.head.ycor() > 280:
        snake.go_through_wall_up(snake.head.xcor(), snake.head.ycor())
    elif snake.head.ycor() < -280:
        snake.go_through_wall_up(snake.head.xcor(), snake.head.ycor())


    #detect collision with tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
