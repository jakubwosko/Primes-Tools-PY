def test_6kpm1(num):
    # Every prime number is of form 6n+-1
    # Then test if num is 6n+-1 form, if NOT simply exit
           
    n = num//6
    if ((6*n)+1 == num): return '6n+1', n  
    if ((6*n)+5 == num): return '6n-1', n+1
    print ("COMPOSITE")
    exit (0)
    
def prime_test_6np1(n):
    # 6n+1 number is NOT a prime then and only then when
    # one number I=(3n-r)/(2r+1) for r=1,2....,n-1 is INTEGER
    
    for r in range(1, n-1, 1):
        I=(3*n-r)/(2*r+1)
        if (I % 1) == 0: return "COMPOSITE"
    return "PRIME"

def prime_test_6nm1(n):
    # 6n-1 number is NOT a prime then and only then when
    # one number I=(3n-r)/(2r-1) for r=2,3....,n-1 is INTEGER
    
    for r in range(2, n-1, 1):
        I=(3*n-r)/(2*r-1)
        if (I % 1) == 0: return "COMPOSITE"
    return "PRIME"

# x is your number for determining whether an input number is prime
x=953

if x==1: 
    print ("NOT A PRIME") 
    exit (0)
if x==2 or x==3: 
    print ("PRIME")
    exit (0)

result = test_6kpm1(x)

if result[0] == '6n+1': print (prime_test_6np1(result[1]))
if result[0] == '6n-1': print (prime_test_6nm1(result[1]))
