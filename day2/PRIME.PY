import math
def is_prime(n):
    if(n%2==0):
        return False
    i=3
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        i+=2
    return True
n=int(input("enter numbrer:"))
val=is_prime(n)
print(val)
