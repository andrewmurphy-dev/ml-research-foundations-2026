import numpy as np 



#question 1 
result = np.array([10, 20 , 30, 40])

print(result)
print(result.shape)


#question 2 

result = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


print(result.shape)


#question 3 


data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])



print(data.ndim)



#question 4

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print(data[1, 1])

#question 5 

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(data[0:2])

#this is a slice , so it gives u both rows 
#to get just 30 , use row 0, column 2:

print(data[0, 2])


#question 6 

data = np.array([
    [5, 10, 15],
    [20, 25, 30]
])


print(data[1, 0])

#question 7 

data = np.array([
    [7, 14, 21],
    [28, 35, 42]
])

print(data[1, 1])


#question 8 


data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


#slice one row 


print(data[1])


#question 9 

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print(data[1, 1:])

#[50 60]


#question 10 

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print(data[:, 1])

#[20 50 80]
