import dis
# def multiply(a,b):
#     mul=a*b
#     return mul
    
# a=5
# b=3
# mul=multiply(a,b)
# dis.dis(multiply)
# print(f"value:{mul}")

def test(n):
    for i in range (1,n):
        a=i
        print(a)
    
n=int(input("enter number:"))
test(n)
dis.dis(test)
    
