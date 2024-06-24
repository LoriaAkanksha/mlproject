import pandas as pd

df= pd.read_csv("/home/akanksha/Desktop/mlproject/mlproject/notebook/data/raw.csv",header=0)


#print(df.columns)
for i in df.head():
    print(df[i])
