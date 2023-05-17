from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Create a screen object
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

# Create a paddle object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create a ball object
ball = Ball()

# Create a score object
scoreboard = Score()
    
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        time.sleep(0.03)
    
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        time.sleep(0.03)
        
screen.exitonclick()