import pandas as pd

data = [("Anshu", 100), ("Sneha", 200), ("Abhijeet", 300), ("Samiksha", 400), ("Pradeep", 500), ("Shivangi", 600)]
df = pd.DataFrame(data, columns = ["Candidate Name", "Candidate ID"], index = [1, 2, 3, 4, 5, 6])

# print(df)
print(df.transpose())