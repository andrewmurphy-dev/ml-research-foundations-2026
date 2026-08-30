#here we learn about model regression ! 


#what is it !?

#Regression is a type of machine learning where the model predicts a number.

#So a regression model learns the relationship between the input X and a numerical target y, then uses that relationship to predict new numbers.


#for example

#house pricing 


#1000 sq ft → $200,000
#1500 sq ft → $280,000
#2000 sq ft → $350,000




#rememebr regression = predict a numebr ! 

#how do we use linear regresssion in python ! ?

#we use scikit-learn 


#basic implementation !



from sklearn.linear_model import LinearRegression
import numpy as np


X = np.array([[1], [2], [3], [4]])
#X = input/features

y = np.array([50, 60, 70, 80])
#y = correct answers/target



model = LinearRegression()
#LinearRegression()
#= create the model

model.fit(X, y)
#model.fit(X, y)
#= train the model



prediction = model.predict([[5]])


#model.predict([[5]])
#= ask the trained model to predict y when X = 5



print(prediction)



