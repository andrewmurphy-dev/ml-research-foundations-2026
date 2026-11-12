from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
import numpy as np 
from sklearn.metrics import accuracy_score 

data = load_iris(as_frame=True)

df = data.frame

print(df.head())
#shows the first 5 , goes from 0 -4

print(df.describe())


print(df.shape)



#so today is real data from csv , you need to pick the columns yourself 

y = df["target"]
X = df.drop(columns="target")

print(y)
print(X)

print(y.shape)
print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)



common_class = y_train.value_counts()


print(common_class)

guesses = np.full(len(y_test), 1)


#so why do we do the guesses first before doing the model?
#We do the baseline first, on purpose. It sets the bar that the real model has to beat.


accuracy = accuracy_score(y_test, guesses) 

print(accuracy)


