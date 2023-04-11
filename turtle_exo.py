import turtle
import random

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def tree(branchLen,t,s):
    s=s-1 if s > 1 else s
    t.pensize(s)
    if branchLen > 5:
        t.forward(branchLen)
        v= random.randrange(10,30)
        t.right(v)
        tree(branchLen-random.randrange(0,20),t,s)
        t.left(2*v)
        tree(branchLen-random.randrange(0,20),t,s)
        t.right(v)
        t.backward(branchLen)
    if branchLen <= 15:
        t.color("green")
    else:
        t.color("brown")
    

# drawSpiral(myTurtle,100)

myTurtle.left(90)
myTurtle.up()
pensize = random.randrange(5,50)
myTurtle.pensize(pensize)
myTurtle.backward(100)
myTurtle.down()
myTurtle.color("brown")
tree(75,myTurtle,pensize)
myWin.exitonclick()