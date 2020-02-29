import sys

def factorial(n):
    if n > 999:
        sys.setrecursionlimit(5000)
    if n == 2:
        return 2
    else:
        return n * factorial(n-1)

print(factorial(100))