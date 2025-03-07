#an empty list
L1=[]
print(" 1. an empty list: ",L1)

L2=[0,1,2,3]
print(f"2.list with 4 items:{L2}")

L3=['abc',['def','ghi']]
print("3.A nested list:",L3)

L4=list('spam')
print("4.list created  from string'spam':",L4)

L5=list(range(-4,4))
print("5.list created from range(-4 to 4)",L5)

L6=[10,20,30,40]
print("6.element at index 2:",L6[2])

L7=['x',[10,20,30],'y']
print("7.Element at L7[1][2]",L7[1][2])

L8=[0,1,2,3,4,5]
print("8.slicing L8 from index 2 to 4",L8[2:5])

print("9.length of L8:",len(L8))

L9=[10,[100,200,300,400],50]     #demonstrating nested indexing and slicing together
print("10a. element at L9[1]:",L9[1])
print("10b.element at L9[1][3]:",L9[1][3])
print("10b.slicing sublist L9[1][1:3]:",L9[1][3])
