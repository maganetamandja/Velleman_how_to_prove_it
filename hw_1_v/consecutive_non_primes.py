from sympy import factorial

def x(n):
    return factorial(n+1) + 2

def list_of_no_primes(i):
    for n in range (i):
        print(x(n))


list_of_no_primes(6)