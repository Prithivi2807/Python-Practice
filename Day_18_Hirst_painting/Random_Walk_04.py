import turtle as t
import random
tim = t.Turtle()

colours = ['red', 'blue', 'green', 'cyan', 'DarkOrchid', 'IndianRed', 'Wheat', 'SeaGreen']
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
