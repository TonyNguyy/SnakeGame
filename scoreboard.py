from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt') as data:
            self.highs_score = int(data.read())

        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=(f"Score: {self.score} High Score: {self.highs_score}"), move=False, align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highs_score:
           self.highs_score = self.score
           with open('data.txt', mode='w') as data:
                data.write(f"{self.highs_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=("Game Over."), move=False, align=ALIGNMENT, font=FONT)
