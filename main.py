import turtle
turtle.Screen().bgcolor('Red')
t=turtle.Turtle()
t.shape('turtle')
t.color('yellow')
size=0
while True:
    for c in range(4):
        t.forward(size+1)
        t.left(90)
        size=size-5
    size=size+1

turtle.done()