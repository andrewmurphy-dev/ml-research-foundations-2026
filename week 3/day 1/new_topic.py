#a row is a vector 

import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
])



print(data[0])


#[10 20 30 40]

print(data.shape[0])

#3 

#you are printing the orgional matrix shape


#but if you go 

first_row = data[0]
print(first_row.shape)

(4,)

print(first_row.ndim)

#1

