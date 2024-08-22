import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()
# pad = Paddle()
# pad2 = CompPaddle()

game_is_on = True
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_x()

    # collision with paddle

    if ((ball.xcor() > 330 and ball.distance(r_paddle) < 50)
            or (ball.xcor() < -330 and ball.distance(l_paddle) < 50)):
        ball.bounce_y()
        ball.speedup()

    # Detect when right paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        l_paddle.reset_paddle((-350,0))
        r_paddle.reset_paddle((350,0))

        scoreboard.left_score_update()
        screen.update()

    # Detect when left paddle miss
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_score_update()
        # screen.update()
    if scoreboard.l_score == 10:
        scoreboard.game_over()
        game_is_on = False

    if scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
