import matplotlib.pyplot as plt
import timeit
    
cache = {}

def memo_func(n):                                
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        result = memo_func(n-1) + memo_func(n-2)
        cache[n] = result
        return result


def func(n):                                
    if n == 0 or n == 1:
        return n
    else:
         return func(n-1) + func(n-2)

def main():
    memo_time = []
    not_memo_time = []
    one_to_35 = []

    for i in range(35):
        memo_time.append(timeit.timeit(lambda: memo_func(i), number= 1))
        not_memo_time.append(timeit.timeit(lambda: func(i), number= 1))
        one_to_35.append(i)

    plt.plot(one_to_35, memo_time, label = "Fibonacci with Memoization")
    plt.plot(one_to_35, not_memo_time, label = "Original Fibonacci")
    plt.title("Time analysis of fibonacci functions from 1 to 35")
    plt.legend()
    plt.xlabel("Integers 1 to 35")
    plt.ylabel("Time in seconds")
    plt.show()

if __name__ == "__main__":
    main()
