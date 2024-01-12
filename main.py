from turtle import Screen

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

screen.listen()

# Left paddle control
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# Right paddle control
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


# Prevent exit until click
screen.exitonclick()
