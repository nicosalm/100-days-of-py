'''
    demo of pandas library in python
'''

import pandas as pd

# create a series
s = pd.Series([1, 3, 5, 6, 8])
# print(s)

# create a dataframe
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
# print(df)

# create a dataframe from a dictionary
df = pd.DataFrame({'a': [1, 3, 5, 6, 8], 'b': [2, 4, 6, 8, 10]})
# print(df)

# create a dataframe from a list of dictionaries
df = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
# print(df)

# create a dataframe from a list of tuples
df = pd.DataFrame([(1, 2), (3, 4)], columns=['a', 'b'])
# print(df)

import numpy as np

# create a dataframe from a numpy array
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
# print(df)

# print the first 10 rows
# print(df.head(10))

# print the last 10 rows
# print(df.tail(10))

# print the column names
# print(df.columns)

# print the index
# print(df.index)

# print the data types
# print(df.dtypes)

# print the shape
# print(df.shape)
 
# print the values
# print(df.values)