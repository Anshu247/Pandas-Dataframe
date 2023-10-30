import pandas as pd
import numpy as np

column = ['A', 'B', 'C', 'D', 'E']
index = ['a', 'b', 'c', 'd', 'e']

df1 = pd.DataFrame(np.random.rand(5, 5), columns = column, index = index)
print(df1)

print('\r')

df1.reindex([1, 2, 3, 4, 5])
print(df1)