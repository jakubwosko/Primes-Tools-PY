#6k+-1 with loop of 12

import math

def is_prime(num):

    # 0 & 1 are not primes
    if (num==0) or (num==1) : return False

    primes_to_remove = [2, 3, 5, 7, 11]
    for prime in primes_to_remove:
        if num == prime: return True
        elif num % prime == 0: return False

    #loop limit
    limit = math.sqrt(num)

    for multiple in range(12, int(limit)+1, 12):
        for k in [1,5,7,11]:
            if num % (multiple + k) == 0:return False
    return True

# number to test
x = 211

if (is_prime(x) == True): print("PRIME")
else: print("NOT PRIME")
