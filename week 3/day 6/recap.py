#question 1 




x = 3
actual = 8
weight = 2

prediction = x * weight
loss = (prediction - actual) ** 2

print(prediction)
print(loss)


#Prepare to calculate the gradient
x = 3
actual = 8
h = 0.001

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2


gradient = (loss(weight + h) - loss(weight))/ h


print(gradient) 




#question 2 
x = 3
actual = 8
weight = 2
h = 0.001

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

gradient = (loss(weight + h) - loss(weight)) / h

print(gradient)


#-11.991000000000529


#so what does negative mean and psitive in terms of gradient 

#so i assume negative we need to increase to get to the target and vice versa