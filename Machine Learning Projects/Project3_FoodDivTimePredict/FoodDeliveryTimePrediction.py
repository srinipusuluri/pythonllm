import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM


data = pd.read_csv("deliverytime.txt")
# print(data.head())
# data.info()
# data.isnull().sum()

# Calculating distance between two latitudes and longitudes using haversine formula

# Earth Radius in kilometers
R = 6371

# Convert Degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi/180)

# Calculate distance between two points using the haversine formula
def distCalculate(lat1,lon1,lat2,lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

# Calculate distance between each pair of points
data["distance"] = np.nan

for i in range(len(data)):
    data.loc[i, "distance"] = distCalculate(data.loc[i, "Restaurant_latitude"],
                                            data.loc[i, "Restaurant_longitude"],
                                            data.loc[i, "Delivery_location_latitude"],
                                            data.loc[i, "Delivery_location_longitude"])

# print(data.head())

figure = px.scatter(data_frame = data,
                    x = "distance",
                    y = "Time_taken(min)",
                    trendline = "ols",
                    title = "Relationship between Distance and Time Taken")
# figure.show()

figure = px.scatter(data_frame = data,
                    x = "Delivery_person_Age",
                    y = "Time_taken(min)",
                    size = "Time_taken(min)",
                    color = "distance",
                    trendline = "ols",
                    title = "Relationship between Time Taken and Age")
# figure.show()

figure = px.scatter(data_frame = data,
                    x = "Delivery_person_Ratings",
                    y = "Time_taken(min)",
                    size = "Time_taken(min)",
                    color = "distance",
                    trendline = "ols",
                    title = "Relationship Between Time Taken and Ratings")
# figure.show()

fig = px.box(data,
             x = "Type_of_vehicle",
             y = "Time_taken(min)",
             color="Type_of_order")
# fig.show()

# Food Delivery Time Prediction Model
# Train ML using LSTM neural network model

# Spliting data
x = np.array(data[["Delivery_person_Age", "Delivery_person_Ratings", "distance"]])
y = np.array(data[["Time_taken(min)"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)


# Making the LSTM neural network model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape = (xtrain.shape[1], 1)))
model.add(LSTM(54, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

# Training the model
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(xtrain,ytrain, batch_size=1, epochs=9)

print("Food Delivery Time Prediction")
a = int(input("Age of Delivery Person: "))
b = float(input("Ratings of Previous Delivers: "))
c = int(input("Total Distance: "))


features = np.array(([a,b,c]))

features = features.reshape((1, 3, 1))

print("Predicted Delivery Time in Minutes = ", model.predict(features))