def fibonacii(rang,list):
    sum=0
    for i in range(2,rang):
        sum=list[i-2]+list[i-1]
        list.append(sum)
    print(list)

rang=int(input("enter the range: "))
list=[]
if(rang==0):
    print("the range is invalid!!")
elif rang==1:
    print(1)
elif rang==2:
    print(1,1)
else:
    list.append(1)
    list.append(1)
    fibonacii(rang,list)