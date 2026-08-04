#Prediction

#A model uses an input and a weight to make a prediction.


#We multiply by the weight because it is the mathematically simplest way to scale an input up or down to match a target output.


x = 3
weight = 5

prediction = x * weight

print(prediction)


#x = 2              → input information
#weight = 4         → number the model uses to control the input
#prediction = 8     → the model’s guess



#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.
#The weight helps create the guess. Gradient descent will later adjust the weight so that the guess becomes closer to the actual answer.





###ACTUAL VALUE 

#The actual value is the correct answer from the real data.


x = 2
weight = 4

prediction = x * weight
actual = 10



print(prediction)
print(actual)

prediction = 3 * 2
prediction = 6

actual = 10 



###LOSS 

#Loss measures how far the prediction is from the actual value:


loss = (prediction - actual) ** 2



print(loss)



#for example


prediction = 6
actual = 8

loss = (actual - prediction) ** 2

print(loss)



