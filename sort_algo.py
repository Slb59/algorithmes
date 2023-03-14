
from time import time
from functools import wraps

def timer_calc(func):
    """ time execution of a function """
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        t1=time()
        result = func(*args,  **kwargs)
        t2=time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrapper_function

@timer_calc
def quick_sort(data: list, lo: int, hi: int) -> list:
    """ Quick sorting algorithme """
    
    def partition(data: list, lo: int, hi: int) -> int:
        pivot = data[hi]  # Choose the last element as the pivot
        i = lo - 1  # Temporary pivot index

        for j in range(lo, hi):
            ...


    if lo >= hi or lo < 0:  # Ensure indices are in correct order
        return
    p = partition(data, lo, hi)  # Partition array and get the pivot index

    # Sort the two partitions
    quick_sort(data, lo, p - 1)  # Left side of pivot
    quick_sort(data, p + 1, hi)  # Right side of pivot
    
    print("quick_sort")

if __name__ == '__main__':
    data = [38, 27, 43, 3, 9, 82, 10]
    data_sorted = quick_sort(data, 0, len(data) - 1)
    print(data)
    print(data_sorted)