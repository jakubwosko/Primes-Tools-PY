# Primality test using 6k+-1 optimization
import math

def is_prime(n):

    limit = math.sqrt(n)

    if (n <=1): return False
    if (n == 2 or n==3 or n==5): return True
    if n % 2 == 0 or n % 3 == 0: return False

    for x in range(5, int(limit), 6):
        if n % (x) == 0 or n % (x+2) == 0: return False
    return True
    
x=103
if (is_prime(x) == True): print("PRIME") 
else: print("NOT PRIME")
