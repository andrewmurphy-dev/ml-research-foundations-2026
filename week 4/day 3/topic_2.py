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