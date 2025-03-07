import pandas as pd
data={
    'Name':['alice','bob','charlie','david'],
     'Age':[25,30,35,40],
     'City':['new york','los angeles','chicago','houston'] 
    }

df=pd.DataFrame(data)
print(df)
df.head()
