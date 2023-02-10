cache = {}

def func(n):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        result = func(n-1) + func(n-2)
        cache[n] = result
        return result
