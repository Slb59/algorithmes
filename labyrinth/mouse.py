from .labyrinth import Labyrinth

class Something:
    def __init__(self, lab:Labyrinth, x, y, direction = 'N') -> None:
        self.lab = lab
        self.posx = x
        self.posy = y
        self.direction = direction

    def draw(self,t):
        t.up()
        cs = self.lab.cellsize
        t.goto(-cs*(self.lab.width/2) + self.posy*cs + cs/2,cs*(self.lab.height/2) - self.posx*cs- cs/2)
        t.down()

class Cheese(Something):
    def __init__(self, lab: Labyrinth, x, y, direction='N') -> None:
        super().__init__(lab, x, y, direction)
        self.lab.cheeses.append(self)

    def draw(self, t, cs):
        super().draw(t, cs)
        t.shape("square")
        t.color("red", "yellow")

class Mouse(Something):
    def __init__(self, lab:Labyrinth, x, y, direction = 'N') -> None:
        super().__init__(lab,x,y,direction)
        self.lab.mouses.append(self)

    def wall(self) -> bool:
        """ True if the mouse faces a wall """
        if (self.direction == "N" and self.posx==0) or (self.direction == "W" and self.posy==0):
            return True
        if self.direction == "N":
            return self.lab.cells[self.posx-1][self.posy].south
        if self.direction == "E":
            return self.lab.cells[self.posx][self.posy].east
        if self.direction == "S":
            return self.lab.cells[self.posx][self.posy].south
        if self.direction == "W":
            return self.lab.cells[self.posx][self.posy-1].east
        
    def cheeseforward(self) -> bool:
        """ True if a cheese is forward the mouse """
        ...

    def draw(self,t,cs):
        super().draw(t,cs)
        t.shape("turtle")
        t.color("red", "green")




