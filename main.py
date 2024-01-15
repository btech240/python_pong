import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

# Create screen and configure
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
# Tracer 0 so we don't see paddle move to starting position
screen.tracer(0)

# Create both paddle objects
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Create ball object
ball = Ball()

screen.listen()

# Left paddle control
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# Right paddle control
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect ball collision with walls, changing y-direction only
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect ball collisons with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        time.sleep(1)
        ball.reset()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        time.sleep(1)
        ball.reset()

# Prevent exit until click
screen.exitonclick()
