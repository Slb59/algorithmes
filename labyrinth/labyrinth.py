import random
import turtle
import math

class Cell:
    def __init__(self,zone) -> None:
        self.east = True
        self.south = True
        self.zone = zone 
        self.is_cheese = False
        self.is_mouse = False

    def __str__(self) -> str:
        result = ''
        result += f"{'_' if self.south else ' '}" + f"{'|' if self.east else ' '}" 
        return result
    
    def drawcell(self,t:turtle.Turtle,s):
        if self.south:
            t.pensize(10)
        else:
            t.pensize(1)
        t.forward(s)
        t.left(90)
        if self.east:
            t.pensize(10)
        else:
            t.pensize(1)
        t.forward(s)
    

class Labyrinth:

    cellsize=50

    def __init__(self, h, w) -> None:
        self.height = h
        self.width = w
        self.cells = []
        for i in range(self.height):
            line = [Cell(i*self.width+j) for j in range(self.width)]
            self.cells.append(line) 

        self.mouses = []
        self.cheeses = []

    def lab(self) -> list:
        return self.cells
    
    def __str__(self) -> str:
        result =''.join(' _' for _ in range(self.width)) +'\n'
        for i in range(self.height):
            for j in range(self.width):
                if j==0:
                    result +='|'
                result += str(self.cells[i][j])
            result += ('\n')
        return result
    
    def drawlab(self,t:turtle.Turtle):
        
        t.up()
        pos = (-self.cellsize*(self.width/2),self.cellsize*(self.height/2))
        t.goto(pos)
        t.down()
        # draw up wall
        t.pensize(10)
        for _ in range(self.width):
            t.forward(self.cellsize)
        
        for i in range(self.height):
            for j in range(self.width):
                t.up()
                t.goto(pos[0]+self.cellsize*j,pos[1]-self.cellsize*i)
                t.setheading(270)
                if j==0:
                    t.pensize(10)
                else:
                    t.pensize(1)
                    
                t.down()
                t.forward(self.cellsize)
                # draw cell
                t.setheading(0)
                self.cells[i][j].drawcell(t,self.cellsize)

    def all_walls(self) ->list:
        """ Give the list of all walls """
        walls = []
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].east and j < self.width-1:
                    walls.append((i,j,"east"))
                if self.cells[i][j].south and i < self.height-1:
                    walls.append((i,j,"south")) 
        return walls

    def modify_zone(self,i,j,value):
        """ modify the value of a zone """
        old_zone = self.cells[i][j].zone
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].zone == old_zone:
                    self.cells[i][j].zone = value

    def genere_lab(self):
        walls = self.all_walls()
        random.shuffle(walls)
        for i in range(len(walls)):
            cell1 = self.cells[walls[i][0]][walls[i][1]]
            if walls[i][2] == "east":            
                cell2 = self.cells[walls[i][0]][walls[i][1]+1]
                if cell1.zone != cell2.zone:
                    cell1.east = False
                    self.modify_zone(walls[i][0],walls[i][1]+1,cell1.zone)
            if walls[i][2] == "south":
                cell2 = self.cells[walls[i][0]+1][walls[i][1]]
                if cell1.zone != cell2.zone:
                    cell1.south = False
                    self.modify_zone(walls[i][0]+1,walls[i][1],cell1.zone)