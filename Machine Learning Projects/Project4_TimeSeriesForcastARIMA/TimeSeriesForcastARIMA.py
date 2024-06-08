import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import warnings

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download("GOOG",
                   start = start_date,
                   end = end_date,
                   progress=False)

data["Date"] = data.index
data = data[["Date", "Close"]]
data.reset_index(drop=True, inplace=True)
print(data.tail())

plt.style.use("fivethirtyeight")
plt.figure(figsize=(15,10))
plt.plot(data["Date"], data["Close"])
plt.show()

# Calculate p
result = seasonal_decompose(data["Close"], model="multiplicative", freq=30)
fig = plt.figure()  
fig = result.plot()  
fig.set_size_inches(15, 10)
plt.show()
# Calculate q
pd.plotting.autocorrelation_plot(data["Close"])

plot_pacf(data["Close"], lags=100)

# d is 0 if data is stationary or 1 if seasonal
p, d, q = 5, 1, 2


# model = ARIMA(data["Close"], order=(p,d,q))
# fitted = model.fit(disp = -1)
# print(fitted.summary())
# predictions = fitted.predict()
# print(predictions)
# 
# # ****** ARIMA model will never work for seasonal data, thus must use SARIMA

model = sm.tsa.statespace.SARIMAX(data["Close"], order = (p, d, q), seasonal_order=(p, d, q, 12))
model = model.fit()
print(model.summary())