import pandas as pd

lst = [["Anshu", 7], ["Sneha", 24], ["Abhijeet", 27], ["Samiksha", 18]]
df = pd.DataFrame(lst, columns = ['Name', 'Number'])

print(df)