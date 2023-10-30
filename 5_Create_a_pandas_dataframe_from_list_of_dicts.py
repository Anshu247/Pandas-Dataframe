import pandas as pd

data = [{"Apple": 10, "Banana": 20, "Orange": 30, "Mango": 40, "Pineapple": 50},
    {"Apple": 100, "Banana": 200, "Orange": 300, "Mango": 400, "Pineapple": 500}]

# df = pd.DataFrame(data, index = [1, 2])
df = pd.DataFrame.from_dict(data)
print(df)