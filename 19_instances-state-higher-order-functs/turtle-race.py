from turtle import Turtle, Screen
import random

'''
    Turtle Race Game
'''

# screen setup
screen = Screen()
screen.setup(width=500, height=400)

# turtle setup
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

usr_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ").lower()
if usr_bet not in colors:
    raise ValueError("Invalid color entered. Please enter a valid color.")

# create turtles
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)
    
# add power ups that drop from the sky
power_ups = []
for i in range(6):
    new_power_up = Turtle(shape="circle")
    new_power_up.color(colors[i])
    new_power_up.penup()
    new_power_up.goto(x=random.randint(-230, 230), y=random.randint(-230, 230))
    power_ups.append(new_power_up)
    
# game loop
game_on = True
while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            winner = turtle.pencolor()
            if winner == usr_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        # move turtle a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # if the turtle is on top of a power up, move the turtle 10 spaces forward
        for power_up in power_ups:
            if turtle.distance(power_up) < 10:
                turtle.forward(20)
                power_up.goto(x=random.randint(-230, 230), y=random.randint(-230, 230))

screen.exitonclick()
