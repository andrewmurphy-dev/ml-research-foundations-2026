#variance 



#what is this ?

#Variance measures how far the numbers are from the mean. To calculate it, we:

#1. Find the mean
#2. Find how far each number is from the mean
#3. Square those distances
#4. Take their average

# Square those distances
#what does this mean ?
#Square means raise to the power of 2.

#why do we square ?

#Squaring turns every distance positive, so we can actually measure how far the values are from the mean.




#in numpy we right ! 
import numpy as np 

variance = np.var(data)



#LOW variance  → values are close together
#HIGH variance → values are spread apart
#ZERO variance → every value is identical



#question 1 


data = np.array([5, 5, 5, 5])

varience = np.var(data)

print(varience)


#varience = 0 
#all are identical ! 


#question 2 


data = np.array([4, 5, 6])

vars = np.var(data)

print(vars)

#varuence is small ! 