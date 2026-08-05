#Repeat Gradient Descent with a Loop

#So the improved weight becomes the weight used in the next round.

#for example 



x = 3
actual = 8
weight = 2

h = 0.001
learning_rate = 0.01

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

for step in range(5):
    gradient = (loss(weight + h) - loss(weight)) / h
    weight = weight - learning_rate * gradient

    prediction = x * weight
    current_loss = loss(weight)

    print(weight, prediction, current_loss)


    #range(5) means the training process repeats five times.



    new_weight = weight - learning_rate * gradient

    #you really need to rememver the formulas 




    #practice question 


    x = 3
actual = 8
weight = 2

h = 0.001
learning_rate = 0.01

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2

for step in range(5):
    gradient = (loss(weight + h) - loss(weight)) / h

    weight = weight = learning_rate * gradient 

    print(weight)