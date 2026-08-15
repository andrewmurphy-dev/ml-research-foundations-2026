#Sampling With Replacement


#With replacement means:

#after you pick a value, that value is allowed to be picked again.


#example

import numpy as np

data = np.array([10, 20, 30, 40, 50])




#a bootstrap sample could be 

[20, 20, 50, 10, 40]


#Why can 20 appear twice?

#Because after picking 20, we put it back into the pool, so it can be selected again.
#for example 

rng = np.random.default_rng()

sample = rng.choice(
    data,
    size=len(data),
    replace=True
)

print(sample)


#what is replace=True?
#means:

#sampling with replacement

#So duplicates are allowed.



#question 1 


data = np.array([10, 20, 30, 40, 50])


rng = np.random.default_rng()

result = rng.choice(data, replace=True)

print(result)

#almost. 

#your code works! but right now it only picks one value because you didnt give size= 

#so you need :

size=len(data)

#len(data) is 5, so this creates a new sample with 5 values, and duplicates are allowed.



#question 2 

data = np.array([10, 40, 50, 60, 23])

rng = np.random.default_rng()

result = rng.choice(
    data,
    size=len(data),
    replace=True
)

print(result)
print(np.mean(result))