# HOC - Python Workshop #4
# Date: 31 Jan 2021
# Graphic Simulation of Spike Protein on the surface of the Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2),
# the virus and its variants causing 2 million deaths globally, attributed to the COVID-19 disease.

# Use Random, Turtle
import random
from random import randint
import turtle as t

# Function -> Get Line Length()
# Parameter list -> Empty
# Get user input to define the line length

def get_line_length(): # alternative getLineLength()
    choice = input('Enter line length "long, medium, short":')
    print (choice)
    
    if choice == 'long':
        line = 150
    elif choice == 'medium':
        line = 100
    else:
        line = 50
        
    return line

# Function -> Get Line Width()
# Parameter list -> Empty
# User input :  (superthick, thick, thin) -> 40, 25, 10

def get_line_width():
    choice = input('Enter line width "superthick, thick, thin":')
    print (choice)
    
    if choice == 'superthick':
        line = 40
    elif choice == 'thick':
        line = 25
    else:
        line = 5
        
    return line

def inside_window():
    (x, y) = t.pos()
    #inside = 10000 < x*x + y*y < 90000
    inside = x*x + y*y < 90000
    
    return inside

def move_turtle(line_length):
    pen_color = ['red', 'orangered', 'orange', 'yellow', 'greenyellow', 'green', 'turquoise', 'blue', 'blueviolet', 'indigo', 'purple', 'violetred']
    for i in range(len(pen_color)):
        t.pencolor(pen_color[i])
        t.fillcolor(pen_color[i])
     
        if inside_window():
            value = randint(3,20)
            polygon_angle = 360/value

            rotation = randint(1,2)
            if rotation == 1:
                t.right(polygon_angle)
            else:
                t.left(polygon_angle)
            
            t.forward(line_length)
            #i = (i + 1)% 11
        

    # Give a bounding box (Spike protein) for the movement of the turtle
        else:   
            #t.pencolor('black')
            #t.fillcolor('black')
            t.right(180)
            t.forward(line_length)
            #i = i - 1

# main program
line_length = get_line_length()
line_width = get_line_width()
print('The return value is', line_length)
print('The return value is', line_width)


t.shape('turtle')
t.pensize(line_width)
t.bgcolor('black')
t.speed(0)
t.goto(200,0)


# An Infinite Loop for the turtle movement
while True:
    move_turtle(line_length)


        

    



