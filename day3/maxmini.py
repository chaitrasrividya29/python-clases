n=int(input("enter the range:"))
num=[int(input(f"enter the value for {i+1}:")) for i in range(n)]
num.sort(reverse=True)
print(f"minimum number: {num[0]}")
print(f"minimum number:{num[n-1]}")