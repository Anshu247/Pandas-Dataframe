# Python program to convert list of nested
# dictionary into Pandas dataframe

# CODE 1

# importing pandas
import pandas as pd

# List of list of dictionary initialization
list = [{"Student": [{"Exam": 90, "Grade": "a"}, {"Exam": 99, "Grade": "b"}, {"Exam": 97, "Grade": "c"}],
		"Name": "Paras Jain"},
		{"Student": [{"Exam": 89, "Grade": "a"}, {"Exam": 80, "Grade": "b"}], "Name": "Chunky Pandey"}]

# rows list initialization
rows = []

# appending rows
for data in list:
	data_row = data['Student']
	time = data['Name']
	
	for row in data_row:
		row['Name']= time
		rows.append(row)

# using data frame
df = pd.DataFrame(rows)

# using pivot_table
df = df.pivot_table(index ='Name', columns =['Grade'],
						values =['Exam']).reset_index()

# Defining columns
df.columns =['Name', 'Maths', 'Physics', 'Chemistry']

# print dataframe
print(df)
# -------------------------------------------------------------------

# CODE 2

import pandas as pd

# Sample list of nested dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'Address': {'City': 'New York', 'State': 'NY'}},
    {'Name': 'Bob', 'Age': 30, 'Address': {'City': 'San Francisco', 'State': 'CA'}},
    {'Name': 'Charlie', 'Age': 35, 'Address': {'City': 'Los Angeles', 'State': 'CA'}}
]

# Convert the list of nested dictionaries into a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
