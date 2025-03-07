import math 
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True

start=int(input("enter the star value: "))
end=int(input("enter the end number: "))
list_prime=[]
print(f"the prime numbers in range {start} to {end} are:")
for num in range(start,end+1):
    if is_prime(num):
        list_prime.append(num)
print(f"the prime numbers are: {list_prime}")
print(f"minimum of the given range: {list_prime[0]}")
print(f"maximum of the given range: {list_prime[-1]}")
