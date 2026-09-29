from statistics import LinearRegression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
print("Dataset:")
print(data.head())
data = pd.get_dummies(data, drop_first=True)
X = data.drop("selling_price", axis=1)
y = data["selling_price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=40)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("\nmodel Error (Mean Squared Error):")
print(mse)

