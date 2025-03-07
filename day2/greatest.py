def display(val):
    print(f"greatest of 3 numbers is{val}")

def get_input():
    a=input("enter first no:")
    b=input("enter first no:")
    c=input("enter first no:")
    return(a,b,c)

def find_largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

def main():
    a,b,c=get_input()
    val=find_largest(a,b,c)
    display(val)
main()