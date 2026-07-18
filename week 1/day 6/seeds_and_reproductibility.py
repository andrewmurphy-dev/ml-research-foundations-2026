#what is a seed?

#a seed lets the random generatpr produce the same sequence again 

#for example


import numpy as np

rng = np.random.default_rng(42)
numbers = rng.integers(1, 11, size=5)
print(numbers)


#[1 8 7 5 5]

#[1 8 7 5 5]

#np.random.default_rng(seed) accepts a non-negative integer seed, including 0. NumPy’s seed machinery requires integer values to be non-negative.

#And:

#Recreating a generator with the same seed and making the same method calls, with the same arguments and in the same order, reproduces the same sequence.


#so remember 

#Create generator again with same seed
#+ same calls in same order
#= same results




#practice questions 

#question 1

obj = np.random.default_rng(7)
result = obj.integers(1, 10, size=5)
print(result)

#[9 6 7 9 6]
#[9 6 7 9 6]



#question 2 

rng1 = np.random.default_rng(20)
rng2 = np.random.default_rng(20)

result_rng1 = rng1.integers(1, 50, size=4)
result_rng2 = rng2.integers(1, 50, size=4)

print(result_rng1)
#[44 14 13 23]
print(result_rng2)
#[44 14 13 23]


#question 3


obj = np.random.default_rng(15)
result = obj.integers(1, 20, size=4)
print(result)


#[18 14 14 16]
#[18 14 14 16]



#question 4 

rng1 = np.random.default_rng(5)
rng2 = np.random.default_rng(6)

result = rng1.integers(1, 20, size=5)
res = rng2.integers(1, 20, size=5)

print(result)
#[13 16  1 16  9]




print(res)
#[ 9 11 10  7 18]




#question 5


rng1 = np.random.default_rng(100)
result = rng1.integers(10, 30, size=(2, 3))
print(result)

#[[25 26 12]
# [21 11 15]]


#[[25 26 12]
# [21 11 15]]

rng2 = np.random.default_rng(100)
result = rng2.integers(10, 30, size=(2, 3))
print(result)


#[[25 26 12]
# [21 11 15]]

#[[25 26 12]
# [21 11 15]]