#A dot product takes two vectors of the same length, multiplies matching values, and adds the results.

#The two vectors must have the same number of values:


#question 1 


import numpy as np


vector_a = np.array([2, 4, 6])


vector_b = np.array([3, 5, 7])


result = np.dot(vector_a, vector_b)

print(result)

#68


#how did numpy do this ?


#2 × 3 = 6
#4 × 5 = 20
#6 × 7 = 42

#6 + 20 + 42 = 68



#question 2 


import numpy as np

features = np.array([5, 10, 2])
weights = np.array([2, 3, 4])



prediction = features @ weights

print(prediction)



#so we can use either np.dot() or @