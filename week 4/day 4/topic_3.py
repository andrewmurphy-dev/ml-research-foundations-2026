#standard error !

#how much we expect the sample mean to change if we took different samples.


#That is different from standard deviation:

#Standard deviation
#→ how spread out the individual values are

#Standard error
#→ how unstable the sample mean is

#for example 


#Sample 1 mean = 50
#Sample 2 mean = 52
#Sample 3 mean = 49
#Sample 4 mean = 51

#The means move around a little.


#Standard error measures that uncertainty in the mean



#small sample
#→ larger standard error
#→ mean is less stable

#large sample
#→ smaller standard error
#→ mean is more stable


#what does it tell us tho ?

#Standard error tells you how much your sample mean would typically move around if you repeated the sampling process many times.


#the formula is :

#standard error = standard deviation / √sample size

import numpy as np 


sample = np.array([10, 20, 30, 40, 50])

std = np.std(sample)

standard_error = std / np.sqrt(len(sample))

print(standard_error)




