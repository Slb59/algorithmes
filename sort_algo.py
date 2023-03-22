from time import time
from functools import wraps
import numpy as np
import matplotlib.pyplot as plt


def timer_calc(func):
    """time execution of a function"""

    @wraps(func)
    def wrapper_function(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result

    return wrapper_function


def quick_sort(data: list, lo: int, hi: int) -> list:
    """Quick sorting algorithme O(nlogn)"""

    def partition(data: list, lo: int, hi: int) -> int:
        pivot = data[hi]  # Choose the last element as the pivot
        i = lo - 1  # Temporary pivot index

        for j in range(lo, hi):
            # If current element is smaller than or
            # equal to pivot
            if data[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[hi] = data[hi], data[i + 1]
        return i + 1

    if lo >= hi or lo < 0:  # Ensure indices are in correct order
        return
    p = partition(data, lo, hi)  # Partition array and get the pivot index

    # Sort the two partitions
    quick_sort(data, lo, p - 1)  # Left side of pivot
    quick_sort(data, p + 1, hi)  # Right side of pivot


def selection_sort(data: list):
    """selection sort algorithme O(n**2)"""
    for i in range(len(data)):
        # Find the minimum element in remaining
        minPosition = i

        for j in range(i + 1, len(data)):
            if data[minPosition] > data[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        if i != minPosition:
            temp = data[i]
            data[i] = data[minPosition]
            data[minPosition] = temp


def insertion_sort(data: list):
    """insertion sort algorithme O(n**2)"""
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
        key = data[i]

        # Move elements of data[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def counting_sort(data):
    """counting sort alogorithme O(n)"""
    max_val = max(data)
    m = max_val + 1
    count = [0] * m

    for a in data:
        # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            data[i] = a
            i += 1


def merge_sort(data: list, left, right):
    """merge sort algorithme O(nlogn)
    l is for left index and r is right index of the
    sub-array of data to be sorted
    """

    def merge(data, left, medium, right):
        n1 = medium - left + 1
        n2 = right - medium

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = data[left + i]

        for j in range(0, n2):
            R[j] = data[medium + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            data[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            data[k] = R[j]
            j += 1
            k += 1

    if left < right:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = left + (right - left) // 2

        # Sort first and second halves
        merge_sort(data, left, m)
        merge_sort(data, m + 1, right)
        merge(data, left, m, right)


def bubble_sort(data: list):
    length = len(data)
    for i in range( 0 , length- 1 ):
        for j in range( 0 , length- i- 1 ):
            if data[ j] > data[ j+ 1 ]:
                flag = data[ j]
                data[ j] = data[ j+ 1 ]
                data[ j+ 1 ] = flag


@timer_calc
def call_sort(sort: dict, data: list):
    print(f"{sort['name']} ({len(data)}): ", end="")
    sort["sort"](data)


def main():
    sorts = [
        {"name": "Selection Sort", "sort": lambda arr: selection_sort(data)},
        {"name": "Insertion Sort", "sort": lambda arr: insertion_sort(data)},
        {"name": "Counting Sort", "sort": lambda arr: counting_sort(data)},
        {"name": "Merge Sort", "sort": lambda arr: merge_sort(arr, 0, len(arr) - 1)},
        {"name": "Quick Sort", "sort": lambda arr: quick_sort(data, 0, len(data) - 1)},
        {"name": "Bubble Sort", "sort": lambda arr: bubble_sort(data)}
    ]

    # 1000 elements to 10000 elements
    x_axe = np.array([i * 1000 for i in range(1, 10)])
    plt.xlabel("List Length")
    plt.ylabel("Time Complexity")

    for sort in sorts:
        times = []
        start_all = time()
        for i in range(1, 10):
            start = time()
            data = np.random.randint(100, size=i * 1000)
            call_sort(sort, data)
            end = time()
            times.append(end - start)
        end_all = time()
        print(f"{sort['name']} sorted elements in {(end_all-start_all):.4f} s")
        plt.plot(x_axe, times, label=sort["name"])

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
