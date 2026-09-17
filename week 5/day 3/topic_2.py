# distance 

#KNN needs to measure how far the new input is from the training inputs 

import numpy as np

X = np.array([1, 2, 8, 9])

new_input = 3

distances = np.abs(X - new_input)

print(distances)


##we use abs remmeber this 

#np.abs()




#smaller distance = closer neighbor


#Scikit-learn's KNN calculates these distances for us when we use predict()





X = np.array([2, 5, 10, 15])

new_input = 7 


distances = np.abs(X - new_input)


print(distances)