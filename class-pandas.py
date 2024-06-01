import pandas as pd

# 1. Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Reading and Writing Data
df.to_csv('people.csv', index=False)  # Writing to CSV
df_read = pd.read_csv('people.csv')   # Reading from CSV
print("\nDataFrame read from CSV:\n", df_read)

# 3. Inspecting Data
print("\nFirst few rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())
print("\nDataFrame info:\n", df.info())

# 4. Selecting Data
print("\nSelecting a column:\n", df['Name'])
print("\nSelecting multiple columns:\n", df[['Name', 'City']])
print("\nSelecting rows by index:\n", df.iloc[1:3])

# 5. Filtering Data
print("\nFiltering rows where Age > 25:\n", df[df['Age'] > 25])

# 6. Adding and Modifying Columns
df['Salary'] = [70000, 80000, 60000, 90000]
print("\nDataFrame with new column:\n", df)

df['Age'] += 1
print("\nDataFrame after modifying Age:\n", df)

# 7. Deleting Columns and Rows
df.drop('Salary', axis=1, inplace=True)
print("\nDataFrame after dropping column:\n", df)

df.drop(2, axis=0, inplace=True)
print("\nDataFrame after dropping row:\n", df)

# 8. Handling Missing Data
df.loc[1, 'Age'] = None
print("\nDataFrame with missing data:\n", df)

df_filled = df.fillna(df['Age'].mean())
print("\nDataFrame after filling missing data:\n", df_filled)

# 9. Grouping and Aggregation
data = {
    'Team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Points': [10, 20, 30, 40, 50, 60]
}
df_team = pd.DataFrame(data)
print("\nTeam DataFrame:\n", df_team)

grouped = df_team.groupby('Team').sum()
print("\nGrouped DataFrame:\n", grouped)

# 10. Merging and Joining
data1 = {
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}
data2 = {
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='Key')
print("\nMerged DataFrame:\n", merged_df)
