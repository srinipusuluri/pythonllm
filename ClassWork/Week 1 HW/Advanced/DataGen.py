import pandas as pd
import numpy as np
import random

# List of some real vehicle brands
brands = ['Toyota', 'Ford', 'Chevrolet', 'Honda', 'Nissan']

# List of some real vehicle models
models = ['Corolla', 'Camry', 'Highlander', 'Rav4', 'Tacoma','F-150', 'Escape', 'Explorer', 'Mustang', 'Ranger','Civic', 'Accord', 'CR-V', 'Pilot', 'Odyssey','Silverado', 'Equinox', 'Malibu', 'Traverse', 'Colorado', 'Altima', 'Rogue', 'Sentra', 'Murano', 'Frontier']

# Function to generate a random year between 2000 and 2024
def random_year():
    return random.randint(2000, 2024)

# Function to generate a random mileage between 0 and 300000
def random_mileage():
    return random.randint(0, 300000)

# Function to generate a random lifespan based on mileage and manufacturing year
def random_lifespan(row):
    mileage = row['Mileage']
    year = row['Manufacturing_Year']
    current_year = 2024  # You can replace this with the current year
    age = current_year - year

    if mileage < 50000 and age <= 5:
        return random.randint(15, 20)
    elif mileage < 100000 and age <= 7:
        return random.randint(10, 15)
    elif mileage < 150000 and age <= 10:
        return random.randint(7, 10)
    else:
        return random.randint(1, 7)

# Create a DataFrame with 2000 rows of sample data
data = {'Make': [random.choice(brands) for _ in range(2000)],
        'Model': [random.choice(models) for _ in range(2000)],
        'Manufacturing_Year': [random_year() for _ in range(2000)],
        'Mileage': [random_mileage() for _ in range(2000)]}

df = pd.DataFrame(data)

# Calculate lifespan based on mileage and manufacturing year
df['Lifespan'] = df.apply(random_lifespan, axis=1)

# Save the DataFrame to a CSV file
df.to_csv('vehicle_data.csv', index=False)