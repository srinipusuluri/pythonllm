# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the dataset
df = pd.read_csv('vehicle_data.csv')

# Select the features and the target
X = df[['Make', 'Model', 'Manufacturing_Year', 'Mileage']]
y = df['Lifespan']

# Convert categorical variables into dummy/indicator variables (i.e., one-hot encoding)
X = pd.get_dummies(X, drop_first=True)

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, predictions))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, predictions))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# Now the model is ready to make predictions on new data
new_data = pd.DataFrame({
    'Make': ['Toyota'],
    'Model': ['Corolla'],
    'Manufacturing_Year': [2015],
    'Mileage': [60000]
})

# Convert new_data to match training data structure
new_data = pd.get_dummies(new_data)
missing_cols = set(X_train.columns) - set(new_data.columns)
for c in missing_cols:
    new_data[c] = 0
new_data = new_data[X_train.columns]

# Predict the lifespan of the new vehicle
predicted_lifespan = model.predict(new_data)
print('The predicted lifespan of the vehicle is:', predicted_lifespan)
