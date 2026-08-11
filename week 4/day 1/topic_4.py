#standard deviation ! 


#Standard deviation tells us how far values typically are from the mean.

#its basically the square root of variance 

#variance forced us to square the distances, and standard deviation wants to convert that result back to the original scale.


#DISTANCES FROM MEAN
#        ↓
#square them
#        ↓
#VARIANCE
#        ↓
#square root
#        ↓
#STANDARD DEVIATION

#The reason this is useful is that standard deviation is back on the same scale as the original data.


#for example 


#data               → kilograms
#variance           → kilograms²
#standard deviation → kilograms


#Both tell you about the same underlying thing: how spread out the data is.

#The difference is how easy the number is to interpret.



#Because variance was calculated using squared distances, if the original data is in kilograms, that's effectively:

#64 kg²

#That tells us the spread is larger or smaller than another variance, but 64 kg² is not a normal distance you can picture.

#Take the square root:

#√64 = 8

#Now:

#standard deviation = 8 kg

#And 8 kg is directly interpretable as a typical distance from the mean.




#VARIANCE
#64 kg²
#→ tells us how much spread there is

#STANDARD DEVIATION
#8 kg
#→ expresses that spread in a scale we can interpret directly



#how to write this in code ! 

import numpy as np 


data = np.array([4, 5, 6])

std = np.std(data)

print(std)



#0.816496580927726

