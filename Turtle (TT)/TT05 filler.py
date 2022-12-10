import turtle
colors = ["black","navy","dark blue","medium blue","blue","dodger blue","royal blue","cornflower blue","sky blue","light steel blue"]
 
turtle.penup()
 
turtle.goto(-450,100)
 
for i in range(10):
    turtle.color(colors[i])
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(100)
 
turtle.goto(-450,100)
for i in range(10):
    turtle.color(colors[i])
    turtle.write(colors[i])
    turtle.forward(100)
