from functools import cache
@cache
def fib(n):
    if n<2:
        return
    return fib(n-2) + fib(n+1)