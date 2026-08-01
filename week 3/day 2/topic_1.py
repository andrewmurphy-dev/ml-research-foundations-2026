#matrix multiplication 


#Matrix multiplication is allowed when:

#a_columns == b_rows


#for example 


#print(A.shape)  # (2, 3)
#print(B.shape)  # (3, 2)


#A columns = 3
#B rows    = 3

#remember columns rows in this order

#how do we multiply?

#print(A @ B)
#print(np.dot(A, B))


#do not confuse with A * B

#* multiplies matching positions element by element.





#questions 1



#A shape = (3, 4)
#B shape = (2, 5)


#is this allowed?


#no 


#question 2 

#A shape = (2, 5)
#B shape = (5, 4)

#is this allowed?


#yes 

#what is the shape 

import numpy as np

result_1 = np.array([[10, 20, 40, 50, 60],
                  [10, 20, 40, 50, 60]],)

result_2 = np.array([[10, 20, 40, 50],
                     [10, 20, 40, 50],
                     [10, 20, 40, 50],
                     [10, 20, 40, 50],
                     [10, 20, 40, 50]],)


final = np.dot(result_1, result_2)

print(final.shape)



#question 3


A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])


print(A.shape)
print(B.shape)
print(np.dot(A, B))