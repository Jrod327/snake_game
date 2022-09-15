from turtle import Turtle

alignment = "center"
font = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-15, 260)
        self.score = 00
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=alignment, font=font)

    def increase_score(self):
        self.clear()
        self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=alignment, font=font)
        self.goto(0, -60)
        self.write(f"Press 'R' to restart or 'Q' to quit.", align=alignment, font=("Courier", 12, "normal"))
