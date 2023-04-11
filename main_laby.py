from labyrinth import Labyrinth
from labyrinth import Mouse, Cheese
import turtle
import random

def main(myTurtle):
    lab = Labyrinth(10, 10)
    lab.genere_lab()
    print(lab)
    lab.drawlab(myTurtle)
    lab.cheeses.append((0,lab.width-1))
    print(lab)
    mouse = Mouse(lab,lab.height-1,0)
    print('True' if mouse.wall() else False)
    mouse.draw(myTurtle)
    cheeseTurtle = myTurtle.clone()
    cheese = Cheese(lab,random.randrange(lab.height),random.randrange(lab.width))
    cheese.draw(cheeseTurtle)


if __name__ == "__main__":
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.delay(0)
    main(myTurtle)
    myWin.exitonclick()