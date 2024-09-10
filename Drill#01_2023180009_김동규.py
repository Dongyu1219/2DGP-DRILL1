import turtle

def move_up_turtle():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_down_turtle():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def move_right_turtle():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def move_left_turtle():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()


turtle.shape("turtle")
turtle.onkey(move_up_turtle, 'w')
turtle.onkey(move_down_turtle, 's')
turtle.onkey(move_right_turtle, 'd')
turtle.onkey(move_left_turtle, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()
            
