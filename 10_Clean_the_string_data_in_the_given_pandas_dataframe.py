import pandas as pd

data = {"Product": ["Phones  ", "  Laptops", " Desktops ", "  Play Station  ", " Cars "],
    "ID": [101, 102, 103, 104, 105]}
df = pd.DataFrame(data, index = [1, 2, 3, 4, 5])

df["Product"] = df["Product"].str.strip()
df["Product"] = df["Product"].str.upper()

print(df)
