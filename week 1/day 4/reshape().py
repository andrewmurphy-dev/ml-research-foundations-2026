#what is reshape()?

#changes the structure of an array without changing its values or total number of elements.


#for example


import numpy as np


numbers = np.array([1, 2, 3, 4, 5, 6])

print(numbers.shape)
# (6,)


matrix = numbers.reshape(2, 3)


#[[1 2 3]
 #[4 5 6]]


print(matrix.shape)
# (2, 3)



#before: 1 2 3 4 5 6
#after:  1 2 3
#        4 5 6


#it needs to be valid 

#6 elements

#2 × 3 = 6

#below is also valid ! 

numbers.reshape(3, 2)
numbers.reshape(1, 6)
numbers.reshape(6, 1)



#Before every reshape, calculate:

#rows × columns

#It must equal the array’s .size.