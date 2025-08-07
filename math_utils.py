
def add(a, b):
    return a + b

def square(n):
    return n * n

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)