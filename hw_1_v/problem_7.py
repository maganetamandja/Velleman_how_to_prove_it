""" 
A pair of distinct positive integers (m , n) is called amicable if the sum of
all positive integers smaller than n that divide n is m , and the sum of all
positive integers smaller than m that divide m is n . Show that (220, 284)
is amicable.

"""
from sympy import Mod

def f_1(n):
    l_1 = []
    for i in range (1,n):
        if (Mod(n,i) == 0):
            l_1.append(i)
    return l_1

l220 = f_1(220)
l284 = f_1(284)

print(sum(l284),sum(l220))

if (sum(l220)==284 and sum(l284) == 220):
    print("success")