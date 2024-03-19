import pandas as pd


df=pd.read_csv("/storage/emulated/0/Download/census data for project.csv")
print(df)
a=df.info()
print(a)
b=pd.isnull(df).sum()
print(b)
#Show the records related with the districts New Delhi, Lacknow, Jaipur
print("New Delhi, Lacknow, Jaipur")
c=df["District name"].isin(['New Delhi','Lacknow','Jaipur'])
print(c)
print()
#Total number of population
d=df.groupby('State name').Population.sum()
print(d)
e=df.groupby('State name').Population.sum().sort_values(ascending=False)
print()
print("Top 5 Population State")
f=e.head()
print(f)
print()
print("District name with respect to hindu Religions")
g=df.groupby('District name').Hindus.sum()
print(g)
print()
print('state wise workers')
h=df.groupby('State name').Workers.sum()
print(h)
i=df[df.State name == 'WEST BENGAL'],['Total_Education'].sum()
print(i)

