from turtle import Turtle
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        # time.sleep(0.1)
        new_ycor = self.ycor()+20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        # time.sleep(0.1)
        new_ycor = self.ycor()-20
        self.goto(self.xcor(), new_ycor)

    def reset_paddle(self,pos):
        self.goto(pos)


