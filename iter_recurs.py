"""
    n! iterator vs recursively

"""
   
def factorial_iterative(n):
    for x in range(n):
        x *= x-n
    return x

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)