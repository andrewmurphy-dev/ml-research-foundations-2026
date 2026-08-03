#gradient 


#A gradient simply puts all partial derivatives together:

#for example



def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001

partial_x = (f(x + h, y) - f(x, y))/ h
partial_y = (f(x, y + h) - f(x, y))/h

print(partial_x)
print(partial_y)




import numpy as np

gradient = np.array([partial_x, partial_y])
print(gradient)

#[4.001 8.001]



#first value  = partial derivative for x
#second value = partial derivative for y


#We use a gradient because a function can have several inputs, and we want to know how sensitive the output is to each one.

#partial derivatives → measure each input separately
#gradient → stores all those measurements together

#In real-world ML, the gradient is mainly used while training the model.









#In real-world ML, the gradient is mainly used while training the model.

#Suppose a model predicts bar sales:

#prediction = customers * weight_1 + average_spend * weight_2

#The model then compares its prediction with the real sales and calculates an error, also called a loss.

#prediction = ¥80,000
##real sales = ¥100,000
#error exists

#The model needs to know:

#Which weight caused the error?
#How much should each weight change?

#So it calculates partial derivatives:

##partial derivative for weight_1
##partial derivative for weight_2

#Then stores them together:

#gradient = np.array([partial_weight_1, partial_weight_2])

#For example:

#gradient = [4, 8]

#This tells the model that the second weight currently affects the error more strongly than the first.