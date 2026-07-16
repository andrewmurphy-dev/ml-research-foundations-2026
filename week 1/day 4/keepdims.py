#keepdims=True

#THIS IS LOWER CASE !!!!!


#I get it now so keepdims includes x axis resulting in a 2d array ,
# without keepdims a collapse in x axis resulting in one axis and 3 elements

#number of dimensions = number of axis 

#so 1 dimension = 1 axis , so its a 1d array 


#so 2 dimensions = 2 acis , so its a 2d array 


#for example

import numpy as np

matrix = np.array([
    [10, 30, 50],
    [30, 56, 66],
])



result = matrix.sum(axis=0, keepdims=True)
print(result)
print(result.shape)

#[[ 40  86 116]]
#(1, 3)

#without it 


col = matrix.sum(axis=0)
print(col)
print(col.shape)


#[ 40  86 116]
#(3,)