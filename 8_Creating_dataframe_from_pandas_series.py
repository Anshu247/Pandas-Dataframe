import pandas as pd

names = ['Thor', 'Steve Rogers', 'Tony Stark', 'Natasha']
srs = pd.Series(names)

frame = {"Names": srs}
df = pd.DataFrame(frame)

print(df)