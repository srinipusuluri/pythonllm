import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic dataset
np.random.seed(0)
data = {
    'age': np.random.randint(20, 70, 100),
    'bmi': np.random.uniform(18.5, 35, 100),
    'blood_pressure': np.random.uniform(80, 180, 100)
}
df = pd.DataFrame(data)

# Features and target
X = df[['age', 'bmi']]
y = df['blood_pressure']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared : {mse}")

# Test sample prediction
test_sample = np.array([[50, 25]])
predicted_bp = model.predict(test_sample)
print(f"Predicted Blood Pressure for age 50 and BMI 25: {predicted_bp[0]}")
