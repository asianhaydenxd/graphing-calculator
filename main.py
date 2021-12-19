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

for x in range(XMIN, XMAX+1):
    # Substitute the "x" with the current x (input, independent) value
    substituted_expression = expression.replace("x", f"({str(x)})")
    
    # Get the y (output, dependent) value; skip if undefined
    try:
        y = eval(substituted_expression)
    except ZeroDivisionError:
        grapher.penup()
        continue
    
    # Go to the next step
    print(f"{x}:{y}")
    grapher.goto((x/(XMAX-XMIN)*WIDTH), (y/(YMAX-YMIN)*HEIGHT))
    grapher.pendown()

wn.mainloop()