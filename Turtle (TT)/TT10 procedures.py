import turtle

def triangle_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.right(120)
                
for y in range (-400,650,100):
    for x in range (-700,750,100):
        triangle_draw(x,y,100)


