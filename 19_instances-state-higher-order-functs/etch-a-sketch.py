from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

screen.listen()

''' Etch-a-Sketch '''

def move_forwards():
    t.forward(10)
    
def move_backwards():
    t.backward(10)
    
def turn_left():
    t.left(10)
    
def turn_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    

# move turtle with WASD
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

# clear screen with C
screen.onkey(key="c", fun=clear)

screen.exitonclick()