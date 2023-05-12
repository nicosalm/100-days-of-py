import turtle
import random

skk = turtle.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
skk.pensize(15)
skk.speed("fastest")

for _ in range(200):
    skk.color(random.choice(colors))
    skk.forward(30)
    skk.setheading(random.choice(directions))