def binary_search(arrays, search_value):
    length = len(arrays)
    low = 0
    high = length - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arrays[mid] == search_value:
            return mid
        elif arrays[mid] < search_value:
            low = mid + 1
        elif arrays[mid] > search_value:
            high = mid - 1
    return -1

def dichorec(arrays,low,high,search_value):
    if high < low : return -1
    else:
        mid = (low + high) // 2
        if arrays[mid] == search_value : return mid
        if search_value < arrays[mid]:
            return dichorec(arrays, low, mid-1, search_value)
        else:
            return dichorec(arrays, mid+1, high, search_value)


def main():
    scores = [30, 40, 50, 70, 85, 90, 100]
    search_value = 20
    position = binary_search(scores, search_value)
    print(search_value, " position:", position)
    print("-----------------------------")
    search_value = 90
    position = binary_search(scores, search_value)
    print(search_value, " position:", position)
    search_value = 20
    position = dichorec(scores,0,len(scores)-1,search_value)
    print(search_value, " position:", position)


if __name__ == "__main__":
    main()
