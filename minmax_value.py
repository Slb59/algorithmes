import sys


def max(arrays):
    length = len(arrays)
    for i in range(0, length - 1):
        if arrays[i] > arrays[i + 1]:
            temp = arrays[i]
            arrays[i] = arrays[i + 1]
            arrays[i + 1] = temp
    maxValue = arrays[length - 1]
    return maxValue

def min ( arrays):
    minIndex = 0 
    length = len( arrays) - 1
    for j in range( 0 , length):
        if ( arrays[ minIndex] > arrays[ j]):
            minIndex = j
    return arrays[ minIndex]

def main():
    scores = [60, 50, 95, 80, 70]
    maxValue = max(scores)
    minValue = min( scores)
    print("Max Value = ", maxValue)
    print ( "Min Value = " , minValue)

if __name__ == "__main__":
    main()
