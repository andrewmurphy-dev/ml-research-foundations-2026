import numpy as np


#question 1
numbers = np.array([10, 20, 30, 40, 50])

result = numbers[numbers >= 30]

multiply = result * 2

print(multiply)

#[ 60  80 100]



#question 2 

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


col = matrix.sum(axis=0)
print(col)

print(col.shape)


#[50 70 90]
#(3,)


#question 3 

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


row = matrix.sum(axis=1)
print(row)

print(row.shape)

#[ 60 150]
#(2,)


#question 4 

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


mean = matrix.mean(axis=0)
print(mean)

print(mean.shape)

#[25. 35. 45.]
#(3,)


#question 5 


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])


result = matrix + values 
print(result) 

print(result.shape)


#[[11 22 33]
# [41 52 63]]
#(2, 3)



#question 6 

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([
    [1],
    [2]
])



add = matrix + values 
print(add)

print(add.shape)

#[[11 21 31]
# [42 52 62]]
#(2, 3)


#question 7 
#reshape into a 2 x 3 array 
numbers = np.array([1, 2, 3, 4, 5, 6])

#i found this one hard to remmeber 
#you need to use the reshape() method 


numbers = np.array([1, 2, 3, 4, 5, 6])

reshaped = numbers.reshape(2, 3)

print(reshaped)
print(reshaped.shape)




#question 8 

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])



reshapes = numbers.reshape(4, 2)
print(reshapes)

print(reshapes.shape)




#[[10 20]
# [30 40]
# [50 60]
#[70 80]]
#(4, 2)


#question 9 

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


num = numbers.reshape(3, 4)
print(num)
print(num.shape)





#question 10 

#transpose 

#you also forgot this too !


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transposed = matrix.T

print(transposed)
print(transposed.shape)





#question 11 


matrix = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])


transposed = matrix.T
print(transposed)

print(transposed.shape)



#question 12 


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])



result = matrix.sum(axis=0, keepdims=True)
print(result)


print(result.shape)


#[[50 70 90]]
#(1, 3)



#question 13

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


rows = matrix.sum(axis=1, keepdims=True)
print(rows)
print(rows.shape)





#question 14



rng = np.random.default_rng(25)
result = rng.integers(1, 20, size=6)
reshape_result = result.reshape(2, 3)

print(reshape_result)
print(reshape_result.shape)




#question 15 

rng1 = np.random.default_rng(10)
rng2 = np.random.default_rng(10)

gen1 = rng1.integers(0, 101, size=5)
gen2 = rng2.integers(0, 101, size=5)

print(gen1)
print(gen2)


#[78 96 26 20 80]
#[78 96 26 20 80]

#question 16 

rng = np.random.default_rng(10)

first = rng.integers(0, 101, size=5)
second = rng.integers(0, 101, size=5)

print(first)
print(second)



#question 17 

numbers = np.array([10, 20, 30, 40, 50])
rng = np.random.default_rng(7)

rng.shuffle(numbers)

print(numbers)
print(numbers.shape)



#question 18 

numbers = np.array([5, 10, 15, 20, 25, 30])

result = numbers[numbers >= 20]

values = result * 3 

print(values)



#question 19 

matrix = np.array([
    [2, 4, 6],
    [8, 10, 12]
])



mean = matrix.mean(axis=1)

print(mean)

print(mean.shape)


#question 20 

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print(matrix[:,1])