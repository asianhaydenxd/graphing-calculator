import turtle as trtl
from math import *

WIDTH, HEIGHT = 500, 500

wn = trtl.Screen()
wn.setup(WIDTH, HEIGHT)

XMIN, XMAX = -20, 20
YMIN, YMAX = -20, 20

TAKE_INPUT = False
DEFAULT_EXPRESSION = "15/x"

expression = input("y=") if TAKE_INPUT else DEFAULT_EXPRESSION

# Initialize turtle "grapher" and make as fast as possible
grapher = trtl.Turtle()
grapher.penup()
grapher.pensize(2)
grapher.speed("fastest")

def get_y(x, expression):
    # Substitute the "x" with the current x (input, independent) value
    substituted_expression = expression.replace("x", f"({str(x)})")
    
    # Evaluate and return
    return eval(substituted_expression)

# Draw graph

grapher.pencolor("blue")
grapher.pensize(2)

for x_coord in range(WIDTH):
    x = get_val_from_pos(x_coord)
    
    # Get the y (output, dependent) value; skip if undefined
    try:
        y = get_y(x, expression)
    except ZeroDivisionError:
        grapher.penup()
        continue
    
    # Go to the next step
    grapher.goto((x_coord-WIDTH/2), (y/(YMAX-YMIN)*HEIGHT))
    # print(f"{x}:{y}")
    grapher.pendown()

wn.mainloop()