from turtle import Turtle
## CONSTANTS IN CAPS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    # Highscore code
    with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game_Added_features\Snake\data.txt", mode="r") as data:
      self.high_score = int(data.read())
    self.color("White")
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.update_scoreboard()
  
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game_Added_features\Snake\data.txt", mode="w") as data:
        data.write(f"{self.high_score}")
    self.score = 0
    self.update_scoreboard()


  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("GAME OVER", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()