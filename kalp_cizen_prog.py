import turtle

turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(1)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red","#0000aa")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.62)
curve()

turtle.left(120)
curve()
turtle.forward(111.62)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()
    
