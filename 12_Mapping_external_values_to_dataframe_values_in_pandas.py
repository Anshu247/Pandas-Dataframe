import pandas as pd

data = {"First Name": ['Anshu', 'Sneha', 'Samiksha', 'Shreya', 'Sanya', 'Abhijeet'],
    "Last Name": ['Thakur', 'Patel', 'Setia', 'Thakur', 'Thakur', 'Kukrety'],
    "Age": [20, 19, 18, 18, 16, 19],
    "City": ['Chandigarh', 'Gurgaon', 'Delhi', 'Noida', 'Dehradun', 'Bhimtal']}

df = pd.DataFrame(data, columns = ["First Name", "Last Name", "Age", "City"],
    index = [1, 2, 3, 4, 5, 6])

new_data = {'Anshu': 'B.C.A', 'Sneha': 'B.C.A', 'Samiksha': 'B.C.A', 'Shreya': 'B.tech', 'Sanya': 'Class 11th',
        'Abhijeet': 'B.tech'}
df['Qualification'] = df["First Name"].map(new_data)

print(df)