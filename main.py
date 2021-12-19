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

grapher = trtl.Turtle()
grapher.penup()
grapher.speed(11)

for x in range(XMIN, XMAX+1):
    substituted_expression = expression.replace("x", f"({str(x)})")
    try:
        y = eval(substituted_expression)
    except ZeroDivisionError:
        grapher.penup()
        continue
    
    grapher.goto(x*20, y*20)
    print(f"{x}:{y}")
    grapher.pendown()

wn.mainloop()