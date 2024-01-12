from turtle import Screen, Turtle

# Creat starting variables
game_is_on = True

# Create screen and configure
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
# Tracer 0 so we don't see paddle move to starting position
screen.tracer(0)

# Create paddles
player = Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=5, stretch_len=1)
player.penup()
player.goto(350, 0)


def go_up():
    new_y = player.ycor() + 20
    player.goto(player.xcor(), new_y)


def go_down():
    new_y = player.ycor() - 20
    player.goto(player.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


while game_is_on:
    screen.update()


# Prevent exit until click
screen.exitonclick()
