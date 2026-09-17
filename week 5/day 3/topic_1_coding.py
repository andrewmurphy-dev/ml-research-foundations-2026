

import numpy as np



from sklearn.neighbors import KNeighborsClassifier


X = np.array([
    [1],
    [2],
    [8],
    [9]
])


y = np.array([0, 0, 1, 1])


model = KNeighborsClassifier(n_neighbors=1)
#n_neighbors=1


#what is this?
#KNeighborsClassifier(n_neighbors=1)
#= create KNN using the 1 closest neighbor



model.fit(X, y)

prediction = model.predict([[3]])

print(prediction)



#X us inputs 


#confusion 

#1 clostest neighbor , this means the training point clostest to the new value you want to predict for !


#X is the known input data the model already has:
#X = 1, 2, 8, 9

#y tells us the known class


#class labels are 0 and 1 


#why are they 0 and 1?

#its for the machine learning model and data represnetation

