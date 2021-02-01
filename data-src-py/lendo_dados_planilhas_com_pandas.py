import pandas as pd
import numpy as np
from datetime import datetime

dir = dir(pd)
print(dir)
data_file = pd.read_excel('C:\git\Data-Science\data-src-py\planilha_vendas.xlsx')
print(data_file)
print(data_file.columns.ravel())
print(f"{data_file.columns.ravel()[3]} : {data_file['LojaID'].tolist()}")
print(len(data_file.columns.ravel())-1)
for i in range(0, len(data_file.columns.ravel())):
    data_1 = data_file.columns.ravel()[i]
    data_2 = data_file[data_file.columns.ravel()[i]].tolist()
    print(f"{data_1} : {data_2}")
print('\n')

df = data_file.head()
print(df)
df = data_file.dtypes
print(df)
data_file["LojaID"] = data_file["LojaID"].astype("object") 
print(data_file)
df = data_file.dtypes
print(df)

mult = df["Receitas"] = data_file["Vendas"].mul(data_file["Qte"])
print(mult)
mult2 = data_file.tail()
print(mult2)
