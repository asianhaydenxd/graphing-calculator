import turtle as trtl
from math import *

WIDTH, HEIGHT = 500, 500

wn = trtl.Screen()
wn.setup(WIDTH, HEIGHT)

XMIN, XMAX = -20, 20
YMIN, YMAX = -20, 20
PRECISION = 1

x_center = (-(XMIN + XMAX)/2) * (WIDTH/(XMAX-XMIN))
y_center = (-(YMIN + YMAX)/2) * (HEIGHT/(YMAX-YMIN))

TAKE_INPUT = False
DEFAULT_EXPRESSION = "15/x"

expression = input("y=") if TAKE_INPUT else DEFAULT_EXPRESSION

# Initialize turtle "grapher" and make as fast as possible

grapher = trtl.Turtle()
grapher.penup()
grapher.speed("fastest")
grapher.hideturtle()

def get_val_from_pos(x_coord):
    return (x_coord-WIDTH/2) / (WIDTH/(XMAX-XMIN)) + (XMIN + XMAX)/2

def get_y(x, expression):
    substituted_expression = expression.replace("x", f"({str(x)})") # Substitute the "x" with the current x (input, independent) value
    
    # Evaluate and return
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

def draw_graph(expression, color):
    grapher.pencolor(color)
    grapher.pensize(2)

    for col in range(int(WIDTH/PRECISION)):
        x_coord = col * PRECISION
        x = get_val_from_pos(x_coord)
        
        # Get the y (output, dependent) value; skip if undefined
        try:
            y = get_y(x, expression)
        except ZeroDivisionError:
            grapher.penup()
            continue
        
        if y > YMAX:
            grapher.goto((x_coord-1-WIDTH/2), HEIGHT/2)
            grapher.penup()
            continue
        
        if y < YMIN:
            grapher.goto((x_coord-1-WIDTH/2), -HEIGHT/2)
            grapher.penup()
            continue
        
        # Go to the next step
        grapher.goto((x_coord-WIDTH/2), (y/(YMAX-YMIN)*HEIGHT))
        grapher.pendown()
    
    grapher.penup()
    
draw_graph(expression, "blue")

wn.mainloop()