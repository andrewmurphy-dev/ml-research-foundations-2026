from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression 

data = load_diabetes(as_frame=True)

df2 = data.frame 
#gets all the data 


y = df2["target"]
#use square brackets pick a column 

X = df2.drop(columns="target")

#use circular brackets , call a method

print(y.shape)
print(X.shape)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42)

#order needs to be X on the left , y on the right 





#the baseline 
#why do we make a basline?
#to know if your model is actually any good 
#so we can compare it later 
#we use the model to see if the model can beat the baseline 




y_train_mean = y_train.mean() 

guesses = np.full(len(y_test), y_train_mean)

#this makes a list of the same number repeated
#np.full , fills an array with one number 


#what is mean squared error , how wrong the quesses are on average 
#small MSE --> guesses are close 
#big MSE ---> guesses are far off 


print (mean_squared_error(y_test, guesses))





model = LinearRegression() 

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(mean_squared_error(y_test, predictions))

#here we are comparing what the model done in comparison to the baseline 
