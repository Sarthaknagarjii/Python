import numpy as np
import pandas as pd

Dict1 = {
    "name": ['ajay', 'balak', 'chitu', 'dhanraj', 'golu'],
    "age": [18, 15, 2, 45, 7],
    "city": ['nasik', 'indore', 'badbeli', 'bhopal', 'singroli']
}
df = pd.DataFrame(Dict1)

print(df.describe())
# print(df)
 
# df.to_csv('main.csv')
