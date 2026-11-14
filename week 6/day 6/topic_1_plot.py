from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

data = load_diabetes(as_frame=True)

df2 = data.frame 

y = df2["target"]
X = df2.drop(columns="target")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)




model = LinearRegression() 


model.fit(X_train, y_train)

#so .fit here is different for linear regressione 

predictions = model.predict(X_test)


print("MSE:", mean_squared_error(y_test, predictions))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


plt.scatter(y_test, predictions)
#plots the data, the x axis is the actual labels, the y iswhat the model predicted 



#name the axis below 

plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Linear Regression: predicted vs actual")
plt.plot([25, 350], [25, 350], color="red")
plt.show()

#How to read it: if the model were perfect, every dot would sit on a straight diagonal line, where guess = real. The more scattered the dots, the bigger the errors.

#so looking 

#there is positive correlation 


#what does correlation mean!?

#how much two things move together 


#so how to read the graph 

#so u have a point on the grapgh , u look at the y axis , compare the y axis number (prediction) to the x axis (acutual and see if they are aligned in numbers or not 

)