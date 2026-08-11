#probability 

#How likely something is to happen.


#0   = impossible

#0.5 = 50/50 chance

#1   = certain


#for example 

import numpy as np


die = np.array([1, 2, 3, 4, 5, 6])


probability = 1 / 6 

print(probability)


#that means about a 16.7% chance of rolling a 6.


#we can convert this into a percentage 

percentage = probability * 100 

print(percentage)

#16.666666666666664%

#you can also round it ! 


print(round(percentage, 1))




