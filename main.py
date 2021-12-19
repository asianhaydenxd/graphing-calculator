import turtle as trtl
from math import *

WIDTH, HEIGHT = 500, 500

wn = trtl.Screen()
wn.setup(WIDTH, HEIGHT)

XMIN, XMAX = -20, 20
YMIN, YMAX = -20, 20

x_center = (-(XMIN + XMAX)/2) * (WIDTH/(XMAX-XMIN))
y_center = (-(YMIN + YMAX)/2) * (HEIGHT/(YMAX-YMIN))

TAKE_INPUT = False
DEFAULT_EXPRESSION = "15/x"

expression = input("y=") if TAKE_INPUT else DEFAULT_EXPRESSION

# Initialize turtle "grapher" and make as fast as possible
grapher = trtl.Turtle()
grapher.penup()
grapher.speed("fastest")

def get_val_from_pos(x_coord):
    return (x_coord-WIDTH/2) / (WIDTH/(XMAX-XMIN)) + (XMIN + XMAX)/2

def get_y(x, expression):
    substituted_expression = expression.replace("x", f"({str(x)})") # Substitute the "x" with the current x (input, independent) value
    
    # Evaluate and return
    try:
        if eval(substituted_expression) > YMAX*5 or eval(substituted_expression) < YMIN*5:
            raise ValueError
    except (ZeroDivisionError, ValueError):
        raise ValueError
    return eval(substituted_expression)

# Draw X and Y intercepts
grapher.pencolor("black")
grapher.pensize(1)

grapher.goto(x_center, y_center)
grapher.back(grapher.xcor() + WIDTH/2)
grapher.pendown()
grapher.forward(WIDTH)

grapher.goto(x_center, y_center)
grapher.setheading(90)
grapher.back(grapher.ycor() + HEIGHT/2)
grapher.pendown()
grapher.forward(HEIGHT)
grapher.penup()

# Draw graph

grapher.pencolor("blue")
grapher.pensize(2)

for x_coord in range(WIDTH):
    x = get_val_from_pos(x_coord)
    
    # Get the y (output, dependent) value; skip if undefined
    try:
        y = get_y(x, expression)
    except ValueError:
        grapher.penup()
        continue
    
    # Go to the next step
    grapher.goto((x_coord-WIDTH/2), (y/(YMAX-YMIN)*HEIGHT))
    # print(f"{x}:{y}")
    grapher.pendown()

wn.mainloop()