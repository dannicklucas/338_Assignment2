
import sys
import json
import timeit
import numpy as np
import matplotlib.pyplot as plt



sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high




def main(): 
    array = json.load(open('array.json'))

    times = []
    for arr in array:
        times.append(timeit.timeit(lambda : func1(arr,0,len(arr) - 1), number=1))
        
        
    num_elements = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    plt.xticks(num_elements)
    
    plt.plot(num_elements, times, label = "original algorithm")
    plt.title("Quicksort Algorithm Timing VS Number of Array Elements")
    
    plt.ylabel("Time it Takes to Sort (Seconds)")
    plt.xlabel("Number of Array Elements")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()
