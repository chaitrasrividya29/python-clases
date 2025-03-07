# D1={}
# print("empty dictionary",D1)

# d2={'spam': 1,'eggs':2}
# print("two numbers in dictionary",d2)

# d3={'food':{'hen': 1,'egg':2}}
# print("nested dictionary",d3)

# keylist=['spam','hen','b','apple','chocolate']
# valslist=[9,8,5,7,6]
# d4=dict(zip(keylist,valslist))
# print("zipper",d4)

D={'spam': 1,'eggs':2}
D2={'hen':3,'b':4,'apple':5}
D.update(D2)
print(D)

list1=list(D.keys())
print("keys",list1)


a=D.get('spam',10)
print("value",a)





