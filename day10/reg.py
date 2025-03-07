import pandas as pd

data={
    'Region':['North','North','South','South','South','East'],
    'State':['Delhi','Punjab','Tamil Nadu','Karnataka','Telangana','Odisha'],
    'Year':[2022,2021,2022,2021,2022,2021],
    'sales':[75000,820000,690000,720000,670000,710000],
    'profits':[100000,91000,90000,105000,77000,88000]
}

df=pd.DataFrame(data)
print(df)
df.set_index(['Region','State','Year'], inplace=True)
print(df.sort_values(['Region','Year'],ascending=True))
print(df)
print(df.loc[('South','Tamil Nadu',2022),'sales'])

df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','Telangana'],'sales':[1570000,1410000,1380000]})
df_profits=pd.DataFrame({'State':['Delhi','Tamil Nadu','Telangana'],'profits':[1850000,1650000,1550000]})
df_merged=pd.merge(df_sales,df_profits,on='State', how='inner')
print(df_merged)