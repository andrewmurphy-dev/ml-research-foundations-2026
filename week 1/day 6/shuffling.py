#what is shuffling?

#changing the order of values randomly !


#for example 

import numpy as np 



rng = np.random.default_rng()
numbers = np.array([10, 20, 30, 40, 50])

rng.shuffle(numbers)

print(numbers)


#[20 30 50 40 10]


#the important part is !

#rng.shuffle(numbers)
#Randomly rearrange the values inside numbers.

#Before: [10 20 30 40 50]
#After:  [30 10 50 20 40]


#practice questions

#question 1 

rng = np.random.default_rng()

numbers = np.array([10, 50, 55, 77])

rng.shuffle(numbers)
print(numbers)


#question 2 


obj = np.random.default_rng(42)

letters = np.array(["A", "B", "C", "D", "E"])

obj.shuffle(letters)

print(letters)

#['E' 'C' 'D' 'B' 'A']

#['E' 'C' 'D' 'B' 'A']


#question 3 

numbers = np.array([10, 20, 30, 40, 50, 60])
print(numbers)

#[10 20 30 40 50 60]

rng = np.random.default_rng()
rng.shuffle(numbers)
print(numbers)

#[60 50 40 10 20 30]