#sampling variablility 

#different samples from the same population can give different results.

#for example  

import numpy as np 

population = np.array([10, 20, 30, 40, 50, 60])


#Now imagine we take two different samples:
sample_1 = np.array([10, 20, 30])
sample_2 = np.array([40, 50, 60])

#their means 

#sample_1 mean = 20
#sample_2 mean = 50


#generally 

#small sample
#→ more unstable result

#large sample
#→ usually more stable result