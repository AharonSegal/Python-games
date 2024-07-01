from turtle import Screen
#Makes paddles and controls movement
from PADDLE import Paddle
#Makes ball, moves ball,
#bonces ball from top botom edges, bounces from paddles,
# refreshes when out od bound,
# increases speed when hit.
from BALL import Ball
#boarder blue art
from BOARDER import Boarder
#makes scoreboard, adds points
from ScoreBoard import Scoreboard
#to manage the game speed
import time


def stop_game():
    global game_on
    game_on = False
    screen.bye()

#Make screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0.1)
#show scoreboard
scoreboard = Scoreboard()
#show boarders
border_top = Boarder((0,300))
border_bottom = Boarder((0,-292))
#show paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#show ball
ball = Ball()

#set screen to listen to input
screen.listen()

#long code to be able to have continues movement
# Bind the functions to the key press and release events using instance methods
screen.onkeypress(r_paddle.r_paddle_move_up, "Up")
screen.onkeyrelease(r_paddle.r_paddle_stop_up, "Up")
screen.onkeypress(r_paddle.r_paddle_move_down, "Down")
screen.onkeyrelease(r_paddle.r_paddle_stop_down, "Down")

screen.onkeypress(l_paddle.l_paddle_move_up, "w")
screen.onkeyrelease(l_paddle.l_paddle_stop_up, "w")
screen.onkeypress(l_paddle.l_paddle_move_down, "s")
screen.onkeyrelease(l_paddle.l_paddle_stop_down, "s")

# Listen for closing event
screen.onkeypress(stop_game, "Escape")


#START GAME
game_on = True
while game_on:
    screen.update()
    #game speed
    time.sleep(ball.move_speed)

    #PADDLE MOVEMENT
    if r_paddle.moving_up:
        r_paddle.sety(r_paddle.ycor() + 10)
    elif r_paddle.moving_down:
        r_paddle.sety(r_paddle.ycor() - 10)
    if l_paddle.moving_up:
        l_paddle.sety(l_paddle.ycor() + 10)
    elif l_paddle.moving_down:
        l_paddle.sety(l_paddle.ycor() - 10)


    #BALL PHYSICS
    ball.move_ball()
    #top collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #paddle collission
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.add_speed()

    #ball pass paddle
    if ball.xcor() > 360:
        #add point
        scoreboard.l_point()
        #reset ball
        ball.home()
        ball.reset()
        ball.move_ball()

    if  ball.xcor() < -360:
        scoreboard.r_point()
        ball.home()
        ball.reset()
        ball.move_ball()

screen.mainloop()
