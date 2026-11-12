from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 

#day 3 import 
from sklearn.linear_model import LinearRegression 



data = load_diabetes(as_frame=True)

df2 = data.frame 

y = df2["target"]
X = df2.drop(columns="target")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)






#day 3 part 

model = LinearRegression() 


model.fit(X_train, y_train)

#so .fit here is different for linear regressione 

predictions = model.predict(X_test)


print("MSE:", mean_squared_error(y_test, predictions))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)