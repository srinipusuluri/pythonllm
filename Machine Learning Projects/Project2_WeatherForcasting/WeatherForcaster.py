from matplotlib.pylab import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

data = pd.read_csv("DailyDelhiClimateTrain.csv")
# print(data.head()) # prints the first few rows of a DataFrame
# print(data.describe()) # prints statistics of DataFrame: count, mean, standard deviation, min, 25% percentile, 50% percentile, 75% percentile, max
# print(data.info()) # prints information of DataFrame: Class Type, Index Range, Column Information, Data Type, Memory usage
# print(data.isnull().sum()) # Checks to see if there are any missing values
# figure = px.line(data, x="date",
#                  y="meantemp",
#                  title="Mean Temperature in Delhi Over the Years")
# figure.show()

# figure = px.line(data, x="date",
#                  y="humidity",
#                  title="Humidity in Delhi Over the Years")
# figure.show()

# figure = px.line(data, x="date",
#                  y="wind_speed",
#                  title="Wind Speed in Delhi Over the Years")
# figure.show()

# figure = px.scatter(data_frame = data, x="humidity",
#                     y="meantemp", size="meantemp",
#                     trendline="ols",
#                     title = "Relationship Between Temperature and Humidity")
# figure.show()

data["date"] = pd.to_datetime(data["date"], format = "%Y-%m-%d")
data["year"] = data['date'].dt.year
data["month"] = data["date"].dt.month
print(data.head())

# plt.style.use("fivethirtyeight")
# plt.figure(figsize=(15,10))
# plt.title("Temperature change in Delhi Over the Years")
# sns.lineplot(data = data, x="month", y="meantemp", hue="year")
# plt.show()

forecast_data = data.rename(columns = {"date":"ds",
                                       "meantemp": "y"})
print(forecast_data)

model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
plot_plotly(model, predictions)