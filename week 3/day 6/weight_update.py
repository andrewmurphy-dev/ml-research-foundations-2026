#update weight 


#We now use the gradient to create a better weight:


#learning rate controls the size of the weight-update step.
#the flow below:


#1. Start with input, actual target, and an initial weight
#2. Make a prediction
#3. Calculate the loss
#4. Calculate the gradient
#5. Use the learning rate to update the weight
#6. Repeat
#7 new weight → new prediction → new loss → new gradient → update weight again

#h             = tiny test change used to calculate the gradient
#learning rate = controls the real weight update



#formula 


new_weight = weight - learning_rate * gradient


#the learning rate controls how cautiously the model moves:

#small learning rate → small, careful updates
#large learning rate → large updates that may overshoot


#practice questions 

#question 1 

weight = 2
gradient = -11.991
learning_rate = 0.01

new_weight = weight - learning_rate * gradient

print(new_weight)

#question 2 

x = 3
actual = 8
new_weight = 2.11991

new_prediction = x * new_weight 
new_loss = (new_prediction - actual) ** 2

print(new_prediction)
print(new_loss)




