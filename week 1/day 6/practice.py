#question 1
#here we practice random generator numbers 

import numpy as np 

rng = np.random.default_rng()
numbers = rng.integers(1, 5)
print(numbers)


#1
#4
#3

#question 2 
ring = np.random.default_rng()
numbers = ring.integers(10, 20)
print(numbers)

#12
#16
#14


#question 3

obj = np.random.default_rng()
result = obj.integers(1, 10, size=4)
print(result)


#[9 4 8 6]
#[3 6 3 7]
#[8 3 6 5]


#size=4
#│    │
#│    └── argument value
#└────── parameter name

#question 4

#question 
#write code that generaates 6 random integers from 50 to 100 and prints them !

obj = np.random.default_rng()
result = obj.integers(50, 101, size=6)
print(result)

#[ 54  82 100  65  84  51]
#[75 76 55 82 99 68]
#[88 91 92 94 66 57]



#question 5

obj = np.random.default_rng()
result = obj.integers(1, 9, size=(2, 3))
print(result)

#[[8 1 5]
# [8 8 3]]

#[[6 1 3]
# [8 3 2]]


#question 6 

result = np.random.default_rng()
obj = result.integers(10, 20, size=(3, 2))
print(obj)

#[[17 14]
# [14 17]
# [15 18]]



#question 7 

obj = np.random.default_rng()
result = rng.random()
print(result)

#0.4829329369286607

