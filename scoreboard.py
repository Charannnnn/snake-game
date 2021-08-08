from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.bestScore = self.getBestScore()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}. Best Score: {self.bestScore}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}. Best Score: {self.bestScore}", align="center", font=("Arial", 24, "normal"))

    def endGame(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
        self.writeBestScore()

    def writeBestScore(self):
        with open("Snake-Game/score.txt", mode = "w") as f:
            f.write(str(self.score))

    def getBestScore(self):
        with open("Snake-Game/score.txt") as f:
            highScore = f.read()
            if highScore == "":
                return 0
            return highScore