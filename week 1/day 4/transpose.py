#what is transpose ?

#lol reminds me of Blackmage in FFXIV !

#Transpose swaps an array’s axes.

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])


#for a 2D matrix , (rows, columns) → (columns, rows)


#.T stands for transpose.


#But technically, .T is an attribute/property, not a method, because there are no parentheses.

matrix.T        # property
matrix.sum()    # method


numbers = np.array([1, 2, 3])

print(numbers.T)
# [1 2 3]



#for 2D

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

transposed = matrix.T


#before 

#[[1 2 3]
# [4 5 6]]

#shape: (2, 3)

#after 

#[[1 4]
# [2 5]
# [3 6]]

#shape: (3, 2)


#.T swaps the rows and columns of a 2D array.


#so it flips 

#remmeber this 
