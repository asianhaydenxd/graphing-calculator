import turtle as trtl

XMIN = -20
XMAX = 20
YMIN = -20
YMAX = 20

expression = input("y=")

grapher = trtl.Turtle()
grapher.penup()
grapher.speed(11)

for x in range(XMIN, XMAX+1):
    substituted_expression = expression.replace("x", f"({str(x)})")
    try:
        y = eval(substituted_expression)
    except ZeroDivisionError:
        pass
    
    grapher.goto(x*20, y*20)
    print(f"{x}:{y}")
    grapher.pendown()

trtl.done()