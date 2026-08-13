#Normal Distribution


#A normal distribution is a pattern where:

#most values are near the middle
#fewer values are far away
#it often forms a bell shape


#for example

import numpy as np

rng = np.random.default_rng()

data = rng.normal(
    loc=100,
    scale=15,
    size=1000
)

print(data)

#loc   = mean / center
#scale = standard deviation
#size  = how many values to generate


rng.normal(loc=100, scale=15, size=1000)

#generate 1000 random values centered around 100, with a standard deviation of 15.


#question 1 

rng = np.random.default_rng()

data = rng.normal(
    loc=50,
    scale=10,
    size=500
)


print(data)



#question 2 


result = np.random.default_rng()

data = result.normal(
    loc=0,
    scale=1,
    size=1000
)

print(data)
print(np.mean(data))
print(np.std(data))



#question 3 

result = np.random.default_rng()

rng = result.normal(
    loc=100,
    scale=20,
    size=1000
)



print(np.mean(rng))
print(np.std(rng))