#so this is day 4 , we are just doing some revision of day 3!

#remmeber axis in numpy refer to structural level 


import numpy as np



matrix = np.array([
    [10, 30, 59],
    [34, 33, 10]
])




col = matrix.sum(axis=0)
print(col)

#this finds the columns 


#[44 63 69]

row = matrix.sum(axis=1)
print(row)

#[99 77]

#this finds the rows 



#to find the sum ??

total = matrix.sum()
print(total)

#176



#to find the mean 


mean = matrix.mean()
print(mean)

#29.333333333333332



mean_col = matrix.mean(axis=0)
print(mean_col)


#[22.  31.5 34.5]


mean_row = matrix.mean(axis=1)
print(mean_row)

#[33.         25.66666667]



#what is min?


#smallest value 

#min --> minimum value , i.e lowest value 




#standard deviation 

#calculate this with std 