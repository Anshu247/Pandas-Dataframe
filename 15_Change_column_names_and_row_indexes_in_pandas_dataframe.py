import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Change column names and row indexes
df.rename(columns={'A': 'NewColumn1', 'B': 'NewColumn2'}, inplace = True)
df.index = ['Row1', 'Row2', 'Row3']

print(df)
