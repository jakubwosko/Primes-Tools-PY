###############################################################
# Some calculations for prime distance
###############################################################

from __future__ import division # nedded for float division
import math   # import math module

###############################################################
# is_prime(A) returns 1 when A is prime or 0 when A is 
# complex number
# brute force method is used with 6k+-1 to sqr N
###############################################################

def is_prime(my_num):

    if my_num == 3 or my_num == 5:return 1
    if my_num % 2 == 0 or my_num % 3 == 0 or my_num % 5 == 0:return 0

    sqr=int(math.sqrt(my_num))
            
    for x in range(6, sqr+2, 6):
        if my_num % (x-1) == 0 or my_num % (x+1) == 0:
            return 0
    return 1

distance = 0
lastn2 = 0

###############################################################
# twin primes  
###############################################################

twin_series = 0

for i in range (3,10000):
    if is_prime(i)==1 and is_prime(i+2)==1:
        
        distance = ((i+2)-lastn2)
        
        mynum = math.sqrt((i/(i+2))/distance)
               
        twin_series = (i+2) / i        
                          
        print '{0:8d} {1:8d} {2:8d}'.format(i, i+2, distance),"   ",
        print("%.2f" % round(mynum,2)),"   ",
        print("%.5f" % round(twin_series,5))
        
        lastn2=i+2

