import numpy as np
from sklearn.model_selection import train_test_split



X = np.arange(20).reshape(10, 2)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])


#The big picture

#Training a model means showing it lots of X → y pairs so it learns the pattern. Then you give it new X it’s never seen, and it guesses y.

print(X)
print(y)





#train_test_split

#this tells you the order 

#[X_train, X_test, y_train, y_test]




X_train, X_test, y_train, y_test = train_test_split(X, y)

print("X_train:\n", X_train)
print("X test:\n", X_test)
print("y_train: \n", y_train)
print("y_test: \n", y_test)


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)







X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=4)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
