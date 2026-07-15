

#1. sum()

#what is it?

#this is just the total!



#for example 

import numpy as np

matrix = np.array([
    [10, 20, 50],
    [30, 56, 40]
])


total_sum = matrix.sum(axis=0)
print(total_sum)
#sum goes down
#[40 76 90]


total_sum_one = matrix.sum(axis=1)
print(total_sum_one)

#so sum goes arcoss 
#[ 80 126]


total = matrix.sum()
print(total)
#206 


#so PLEASE PLEASE REMEMBER THIS , 

#when doing sum(axis=0) and sum(axis=1)
#THEY ARE INVERTED 

#if you want to calculate the column , you need to go down , i.e, axis=0

#if you want to calculate the row you need to go across, i.e axis=1









#2 mean 


#what is the mean 

#gives the average 


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])



overall_mean = matrix.mean()

print(overall_mean)
# 50.0

#how does numpy do this ?

#Total = 450
#Number of values = 9

#450 ÷ 9 = 50


#axis=0 (column) 

column_means = matrix.mean(axis=0)

print(column_means)
# [40. 50. 60.]

#column 0: (10 + 40 + 70) ÷ 3 = 40
#column 1: (20 + 50 + 80) ÷ 3 = 50
#column 2: (30 + 60 + 90) ÷ 3 = 60


#down





#acis=1 (row)

row_means = matrix.mean(axis=1)

print(row_means)
# [20. 50. 80.]


#row 0: (10 + 20 + 30) ÷ 3 = 20
#row 1: (40 + 50 + 60) ÷ 3 = 50
#row 2: (70 + 80 + 90) ÷ 3 = 80


#across





#3 min 

#what is min()?

#this returns the smallest value !

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])


overall_min = matrix.min()

print(overall_min)
# 10


#how ?

#NumPy searches all nine values and returns the smallest:


#axis=0 

column_mins = matrix.min(axis=0)

print(column_mins)
# [10 20 30]


#column 0: min(10, 40, 70) = 10
#column 1: min(20, 50, 80) = 20
#column 2: min(30, 60, 90) = 30

#finds the smallest per Row for column 
#remember down 



#axis=1 

#row 0: min(10, 20, 30) = 10
#row 1: min(40, 50, 60) = 40
#row 2: min(70, 80, 90) = 70


#remember across 




##4 max 

#max() returns the largest value.

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])


overall_max = matrix.max()

print(overall_max)
# 90



#how?
#NumPy checks every value and returns the largest one:
#90





###standard deviation 

#what Standard deviation tells you how spread out the values are around their mean.

#Small standard deviation → values are close together.
#Large standard deviation → values are spread far apart.
#Standard deviation of 0 → every value is identical.



numbers = np.array([10, 20, 30])

#The mean is:

#(10 + 20 + 30) ÷ 3 = 20

#Distances from the mean:

#10 is 10 below the mean
#20 is 0 away from the mean
#30 is 10 above the mean

#NumPy calculates it with:

numbers.std()




#for example 

overall_std = matrix.std()

print(overall_std)
# 25.819888...