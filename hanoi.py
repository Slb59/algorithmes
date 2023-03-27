def deplacer(x,y):
    print(f'Move: {x}->{y}')

def hanoi(n:int, a,b,c):
    if n == 0:
        pass
    if n == 1:
        deplacer(a,c)
    if n>1:
        hanoi(n-1,a,c,b)
        deplacer(a,c)
        hanoi(n-1,b,a,c)

def main():
    hanoi(3,'A','B','C')

if __name__ == "__main__":
    main()