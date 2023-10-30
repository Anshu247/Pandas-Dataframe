import pandas as pd

lst = [['Lamborghini', 100000000], ['Bugatti', 200000000], ['Rolls Royce', 300000000]]
df = pd.DataFrame(lst, columns = ['Car Names', 'price'], index = [1, 2, 3])

print(df)