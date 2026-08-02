#what is a matrix?

#A matrix is a rectangular grid of numbers containing rows and columns.

#for example

import numpy as np

patients = np.array([
    [29, 120, 72],
    [45, 135, 80],
])



#matrix shape 

print(patients.shape)

(2, 3)


print(patients.ndim)

2


#matrix = two-dimensional array
#shape = (2, 3)
#ndim = 2


#[29, 120, 72]                → vector

#[[29, 120, 72],
# [45, 135, 80]]              → matrix