import pandas as pd

df=pd.read_csv('C:/Users/Ira/Desktop/Університет/ВКН/Лаб17/17.1 текст.csv', sep=',')
print(df)

df['Листопад']=[50000]
df['Грудень']=[40000]
print(df)

df.to_csv('текст2',sep=',')