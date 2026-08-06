#question 1 

#Complete the function so it returns the square of x:

def f(x):
    return x ** 2

result = f(4)

print(result)



#question 2

def f(x):
    return x ** 2

x = 3
h = 0.001

derivative = (f(x + h) - f(x)) / h 

print(derivative)



#question 3 
#Partial Derivative with Respect to x

def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001

partial_x = (f(x + h, y) - f(x, y))/h

print(partial_x)



#question 4

#Partial Derivative with Respect to y


def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001

partial_y = (f(x, y + h) - (x, y))/ h

print(partial_y)

#this is wrong u swapped the argument positions ! 

#Question 5 
#Build the Gradient

import numpy as np

partial_x = 4.001
partial_y = 8.001

gradient = np.dot(partial_x, partial_y)

print(gradient)

#this is wrong !!!!!! 



#question 6 


#Prediction and Loss


x = 4
weight = 2
actual = 10

prediction = x * weight 
loss = (prediction - actual) ** 2

print(prediction)
print(loss)



#question 7 



x = 4
actual = 10

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

result = loss(2)

print(result)


#question 8 
# Derivative of the Loss



x = 4
actual = 10
weight = 2
h = 0.001

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

gradient = (loss(weight + h) - loss(weight)) /h

print(gradient)


#question 9 

x = 5
actual = 15
weight = 2
h = 0.001

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

gradient = (loss(weight + h) - loss(weight)) / h

print(gradient)



#question 10 

#Update the Weight

weight = 2
gradient = -49.975
learning_rate = 0.01

new_weight = weight - learning_rate * gradient 

print(new_weight)

#Question 11 
# Use the Updated Weight

x = 5
actual = 15
new_weight = 2.49975

new_prediction = x * new_weight 
new_loss = (new_prediction - actual)** 2

print(new_prediction)
print(new_loss)



#question 12 
#Positive Gradient Weight Update

weight = 4
gradient = 20
learning_rate = 0.01

new_weight = weight - learning_rate * gradient 

print(new_weight)

#Question 13 — Update the Current Weight

weight = 4
new_weight = 3.8

weight = new_weight

print(weight)


#Question 14 — Negative Gradient

gradient = -8

if gradient < 0:
    direction = "increase weight"
else:
    direction = "decrease weight"

print(direction)


#increase weight


#Question 15 — Positive Gradient


gradient = 8

if gradient < 0:
    direction = "increase weight"
else:
    direction = "decrease weight"

print(direction)


#decrease weight 


#Question 16 — Zero Gradient


weight = 3
gradient = 0
learning_rate = 0.01

new_weight = weight - learning_rate * gradient 

print(new_weight)


#Question 17 — Compare Two Learning Rates


#Complete both weight updates:

weight = 2
gradient = -10

small_learning_rate = 0.01
large_learning_rate = 0.1

small_step_weight = weight - small_learning_rate * gradient 
large_step_weight = weight - large_learning_rate * gradient 

print(small_step_weight)
print(large_step_weight)



#Question 18 — Calculate the Adjustment


gradient = -12
learning_rate = 0.05

adjustment = learning_rate * gradient

print(adjustment)


#Question 19 — Use the Adjustment

weight = 2
adjustment = -0.6

new_weight = weight - adjustment 

print(new_weight)


#Question 20 — Full Weight Update

x = 3
actual = 12
weight = 2
h = 0.001
learning_rate = 0.01

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

gradient = (loss(weight + h) - loss(weight)) / h 

weight = weight - learning_rate * gradient 

print(gradient)
print(weight)

