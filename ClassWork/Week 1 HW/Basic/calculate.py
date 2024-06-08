import pandas as pd
from scipy import stats

# Load the CSV file
df = pd.read_csv('student_data.csv')

# Calculate the GPA for each student
df['GPA'] = (df[['Maths', 'English', 'Science']].mean(axis=1) / 100 * 4).round(3)

# Calculate statistical metrics for each subject
# metrics = df[['Maths', 'English', 'Science']].describe()

# Compute the class rank for each student based on GPA
df['Rank'] = df['GPA'].rank(method='min', ascending=False).astype(int)

# Save the original student data with additional columns for class rank and GPA
df.to_csv('processed_student_data.csv', index=False)

# print("Statistical Metrics for each subject:")
# print(metrics)

print("Processed student data with GPA and Rank:")
print(df)
