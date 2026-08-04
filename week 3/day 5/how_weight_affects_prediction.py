#How a weight affects prediction?


#keep input fixed 


x = 3


#now change only weight !


weight = 2
prediction = x * weight   # 6




#weight changes → prediction changes

#what defines weight ? we just try to giess to reach to the target ?


#x       = input data — fixed
#actual  = correct answer — fixed
#weight  = adjustable number the model is trying to learn



#weight = the adjustable knob

#start with one weight
##→ calculate the loss
##→ use the gradient to see which direction lowers the loss
##→ move the weight in that direction
## repeat





#so what creates the gradient in our code though 


x = 3
actual = 8

def loss(weight):
    prediction = x * weight
    return (prediction - actual) ** 2



#Now calculate the gradient:

weight = 2
h = 0.001

gradient = (loss(weight + h) - loss(weight)) / h

print(gradient)



#this line creates the gradient ! 

gradient = (loss(weight + h) - loss(weight)) / h


