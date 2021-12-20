import grapher as grafr

grapher = grafr.Grapher()
grapher.draw_graph("x", "blue", 5)
grapher.draw_graph("x**2", "red")

grapher.done()