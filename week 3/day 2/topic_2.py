#linear combination 

#what is this ? 

#multiply vectors by numbers
#then add the results


#A vector is an ordered collection of numbers.


#for example
#2 * vector_a + 3 * vector_b


#@ or np.dot()
#→ dot product / matrix multiplication

#*
#→ element-by-element multiplication
#→ or scalar multiplication



#linear combination follows this pattern 
#number * vector_a + number * vector_b

#for example

#2 * vector_a + 3 * vector_b





#question 1 

import numpy as np

vector_a = np.array([1, 2])
vector_b = np.array([3, 4])




result = 2 * vector_a + 3 * vector_b

print(result)



#question 2 


vector_a = np.array([2, 5])
vector_b = np.array([4, 1])


result = 3 * vector_a + 2 * vector_b

print(result)

#question 3 

vector_a = np.array([3, 2])
vector_b = np.array([1, 4])


result = 4 * vector_a + 2 * vector_b


print(result)



#question 4


vector_a = np.array([2, 6])
vector_b = np.array([5, 3])


result = 2 * vector_a + 4 * vector_b
print(result)