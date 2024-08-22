from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("square")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.hideturtle()
        # self.goto(position)

        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def right_score_update(self):
        self.r_score += 1
        self.update_scoreboard()

    def left_score_update(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !! ", move=False, align="center", font=("Courier", 50, "normal"))
