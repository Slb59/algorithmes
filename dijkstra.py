def move(flags,pos1,pos2):
    flags[pos1], flags[pos2] = flags[pos2], flags[pos1]

def dijkstra(flags,n):
    b=0
    w=0
    r=n-1
    while w<=r:
        if flags[w] == 'B':
            move(flags,w,b)
            w += 1
            b += 1
        if flags[w] == "W":
            w += 1
        if flags[w] == "R":
            move(flags,w,r)
            r-=1


def main():
    flags = ['R','B','W','B','R','W']
    dijkstra(flags,len(flags))
    print(flags)

if __name__ == "__main__":
    main()