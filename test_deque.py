from pythonds.basic import Deque

def green_path(map):
    green_path_queue = Deque([map[0][0]])
    i=0
    for i in range(0,len(map),2):
        green_path_queue.extend(map[i][1:])
        green_path_queue.extend(map[i+1][:0:-1])
    for i in range(len(map)-1,0,-1):
        green_path_queue.append(map[i][0])
    return green_path_queue

def forward(value,pos,path):
    try:
        new_pos = path.index(value,pos+1)
    except ValueError:
        new_pos = path.index(value,0)
    return new_pos

def main():
    map = [[1,2,3,4,5,6,1,2,3],
           [2,3,4,5,6,1,2,3,4],
           [3,4,5,6,5,2,3,4,5],
           [4,5,6,1,4,3,4,5,6],
           [5,6,1,2,1,4,5,6,1],
           [6,1,2,3,6,5,6,1,2],
           [1,2,3,4,5,6,1,2,3],
           [2,3,4,5,6,1,2,3,4]]
    green_gardian_path = green_path(map)
    green_gardian_pos=69
    print(len(green_gardian_path))
    print(green_gardian_path[71])
    print(forward(4,green_gardian_pos,green_gardian_path))

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == "__main__":
    main()