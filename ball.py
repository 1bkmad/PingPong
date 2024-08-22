from turtle import Turtle
from paddle import Paddle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.speed = 0
        # self.ballspeed = 0.01
    def move(self):
        # time.sleep(self.ballspeed)
        new_x = self.xcor()+self.xmove + self.speed
        new_y = self.ycor()+self.ymove + self.speed
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.ymove *= -1
        # self.goto(new_x, new_y)

    def bounce_y(self):
        self.xmove *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_y()
        # self.ballspeed = 0.01
        self.xmove, self.ymove = 10, 10

    def speedup(self):
        # self.ballspeed *= 0.9
        self.xmove *= 1.1
        self.ymove *= 1.1
