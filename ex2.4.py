
import sys
import json
import timeit
import numpy as np
import matplotlib.pyplot as plt


sys.setrecursionlimit(20000)



def func2(array, start, end):
    
    p = array[(end + start)//2]
    low = start - 1
    high = end + 1
    while True:
        low +=1
        while array[low] < p:
            low += 1
        
        high -= 1
        while array[high] > p:
            high -= 1
            
        if(low >= high):
            return high

        array[low], array[high] = array[high], array[low]

def func1(array, low, high):
    if low < high:
        mid = func2(array, low, high)
        func1(array, low, mid)
        func1(array, mid + 1, high)
   

def main(): 
    with open('array.json','r') as iF:
        array = json.load(iF)
    for arr in array:
        func1(arr, 0, len(arr) - 1)
    sorted_arrays = array
    

# write data to a new json file 
    with open("ex2.5.json", "w") as outfile:
        json.dump(sorted_arrays, outfile) 


if __name__ == "__main__":
    main()



def main(): 
    array = json.load(open('array.json'))
    times = []

    for arr in array:
        times.append(timeit.timeit(lambda : func1(arr,0,len(arr) - 1), number=1))
        
    num_elements = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    plt.xticks(num_elements)
    
    plt.plot(num_elements, times, label = "optimized algorithm")
    plt.title("Quicksort Algorithm Timing VS Number of Array Elements")
    
    plt.ylabel("Time it Takes to Sort (Seconds)")
    plt.xlabel("Number of Array Elements")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

