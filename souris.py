class Cell:
    def __init__(self,zone) -> None:
        self.east = True
        self.south = True
        self.zone = zone 

    def __str__(self) -> str:
        result = ''
        # result += str(self.zone)
        result += f"{'_' if self.south else ' '}" + f"{'|' if self.east else ' '}" 
        return result
    

class Labyrinth:
    def __init__(self, h, w) -> None:
        self.height = h
        self.width = w
        self.cells = []
        for i in range(self.height):
            line = [Cell(i*self.width+j) for j in range(self.width)]
            self.cells.append(line) 

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

def main():
    lab = Labyrinth(4,10)
    print(lab.lab()[2][7])
    print(lab)
        

if __name__ == "__main__":
    main()

