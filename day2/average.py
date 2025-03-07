def display(val):
    print(f"average of 4 numbers is{val}")

def get_input():
    a=input("enter first no:")
    b=input()
    c=input()
    d=input()
    return(a,b,c,d)

def get_avg(a,b,c,d):
    val=(int(a)+int(b)+int(c)+int(d))/4
    return val

def main():
    a,b,c,d=get_input()
    val=get_avg(a,b,c,d)
    display(val)
main()
    

