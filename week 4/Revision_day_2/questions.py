

#quesion 1 

def f(x):
    return x ** 2

result = f(5)

print(result)


#question 2 

#calculate the numerical derivative ! 


def f(x):
    return x ** 2

x = 4
h = 0.04 

result = (f(x + h) - f(x)) / h 

print(result)


#question 3 

def f(x):
    return x ** 2

x = 4
h = 0.001

result = (f(x + h) - f(x)) / h

print(result)


#question 4 

def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001


result_x = (f(x + h, y) - f(x, y)) / h 

print(result_x)


#question 5 

def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001

result_y = (f(x, y + h) - f(x, y)) / h

print(result_y)


#question 6

def make_gradient(partial_x, partial_y):
    return np.array([partial_x, partial_y])

partial_x = 4.001
partial_y = 8.001

gradient = make_gradient(partial_x, partial_y)

print(gradient)


#question 7

def f(x, y):
    return x ** 2 + 3 * y ** 2

x = 3
y = 2
h = 0.001

partial_x = (f(x + h, y) - f(x, y)) / h
partial_y = (f(x, y + h) - f(x, y)) / h

print(partial_x)
print(partial_y)



#question 8
#Create a NumPy gradient vector containing both values, then print it.

import numpy as np

def f(partial_x, partial_y):
    return np.array([partial_x, partial_y])

gradient = f(partial_x, partial_y)

print(gradient)


#question 9 

partial_x = 10.002
partial_y = -6.004

#Create a NumPy gradient vector containing both values, then print it.


def f(partial_x, partial_y):
    return np.array([partial_x, partial_y])

gradient = f(partial_x, partial_y)
print(gradient)

#question 10

#prediction = x * weight
#loss = (prediction - actual) ** 2


x = 4
weight = 2
actual = 10

prediction = x * weight 
loss = (prediction - actual) ** 2



#question 11

x = 4
actual = 10

def loss(weight):
    return x * weight 

prediction = loss(2)


loss = (prediction - actual) ** 2

print(loss)

#this is wrong , we can do this better , as ur fucntion is loss function , so we can put everything there


def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

result = loss(2)

print(result)

#question 12 

x = 5
actual = 15
weight = 2
h = 0.001

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2
#Calculate the numerical derivative of the loss at weight = 2 and print it.

result = (f(x, weight + h) - f(x, weight)) / h

print(result)

#we need to use the loss function !! 

result = (loss(weight + h) - loss(weight)) / h

print(result)

