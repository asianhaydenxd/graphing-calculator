import turtle as trtl
from math import *

class Grapher:
    def __init__(self, width=500, height=500, xmin=-10, xmax=10, ymin=-10, ymax=10):
        self.width = width
        self.height = height
        
        self.wn = trtl.Screen()
        self.wn.setup(width, height)
        
        self.grapher = trtl.Turtle()
        self.grapher.penup()
        self.grapher.speed("fastest")
        self.grapher.hideturtle()
        
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        
        self.x_center = (-(self.xmin + self.xmax)/2) * (self.width/(self.xmax-self.xmin))
        self.y_center = (-(self.ymin + self.ymax)/2) * (self.height/(self.ymax-self.ymin))
    
    def get_value(self, x_coord):
        return (x_coord-self.width/2) / (self.width/(self.xmax-self.xmin)) + (self.xmin + self.xmax)/2
    
    def done(self):
        self.wn.mainloop()
    
    def draw_intercepts(self):
        self.grapher.pencolor("black")
        self.grapher.pensize(1)

        self.grapher.goto(self.x_center, self.y_center)
        self.grapher.back(self.grapher.xcor() + self.width/2)
        self.grapher.pendown()
        self.grapher.forward(self.width)

        self.grapher.goto(self.x_center, self.y_center)
        self.grapher.setheading(90)
        self.grapher.back(self.grapher.ycor() + self.height/2)
        self.grapher.pendown()
        self.grapher.forward(self.height)
        self.grapher.penup()
    
    def draw_graph(self, expression, color, precision=1):
        self.grapher.pencolor(color)
        self.grapher.pensize(2)

        for col in range(int(self.width/precision)):
            x_coord = col * precision
            x = self.get_value(x_coord)
            
            # Get the y (output, dependent) value; skip if undefined
            try:
                y = get_y(x, expression)
            except ZeroDivisionError:
                self.grapher.penup()
                continue
            
            if y > self.ymax:
                self.grapher.goto((x_coord-1-self.width/2), self.height/2)
                self.grapher.penup()
                continue
            
            if y < self.ymin:
                self.grapher.goto((x_coord-1-self.width/2), -self.height/2)
                self.grapher.penup()
                continue
            
            # Go to the next step
            self.grapher.goto((x_coord-self.width/2), (y/(self.ymax-self.ymin)*self.height))
            self.grapher.pendown()
        
        self.grapher.penup()
        
def get_y(x, expression):
    return eval(expression.replace("x", f"({str(x)})"))