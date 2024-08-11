from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("day 20_21_24/scoreboard.txt") as file:
            high_score = file.read()
        self.high_score = int(high_score)

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            # self.score = str(self.score)
            with open("day 20_21_24/scoreboard.txt", 'r+') as file2:
                file2.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
