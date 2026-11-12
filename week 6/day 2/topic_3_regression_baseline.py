#here we are doing a new data set
#diabetes 

#predicting a number means regression 

from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error


data = load_diabetes(as_frame=True)

df2 = data.frame 

y = df2["target"]
X = df2.drop(columns="target")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


common_mean = y_train.mean() 

guesses = np.full(len(y_test), common_mean)




#mean_squared_error(y_test, guesses) --> called MSE 
#MSE = the average of (real − guess)², across all test samples. It measures how far off the guesses are

mse = mean_squared_error(y_test, guesses)
print(mse)

#result ---> 5361.533457238513