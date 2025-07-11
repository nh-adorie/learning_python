from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("project/Snake_Game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(10,270)
        self.pendown()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("project/Snake_Game/data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
