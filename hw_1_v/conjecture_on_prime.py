from sympy import isprime
def compute_3_to_the_n_minus_1(n):
    return 3**n -1

def compute_3_to_the_n_minus_2_to_the_n(n):
    return (3**n) -(2**n)

def my_is_prime(n):
    return_value = "default"
    if isprime(n):
        return_value = "yes"
    else:
        return_value = "no"
    return return_value

print("n , Is n prime? ,  3^n - 1 ,  Is 3^n - 1 prime? ,  3^n - 2^n  , Is 3^n - 2^n prime? , ")
for n in range(30):
    
    print(n,",", my_is_prime(n) , "," ,  compute_3_to_the_n_minus_1(n), "," ,my_is_prime(compute_3_to_the_n_minus_1(n)), "," ,compute_3_to_the_n_minus_2_to_the_n(n), "," ,my_is_prime(compute_3_to_the_n_minus_2_to_the_n(n)), ","  )
    pass

