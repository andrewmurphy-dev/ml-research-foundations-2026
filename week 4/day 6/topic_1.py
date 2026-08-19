#correlation 

#Correlation tells us whether two variables tend to change together.

#hours studied ↑
#exam score    ↑

#as study hours increase , exam scores tend to be positive 

#this is positive correlation 


#another example

#outside temp   (high)
#heating usage  (low)



#One goes up while the other tends to go down.

#this is negative correlation


#correlation is usually between 

#-1 and +1 

#+1  → very strong positive correlation

# 0  → no clear correlation

#-1  → very strong negative correlation

#formula

#np.corrcoef

#for example

import numpy as np


hours = np.array([1, 2, 3, 4, 5])
scores = np.array([50, 60, 70, 80, 90])

correlation = np.corrcoef(hours, scores)

print(correlation)

#np.corrcoef(hours, scores) creates a 2 × 2 matrix.

#              column 0   column 1
#                 ↓          ↓
#row 0 →        [1.0,       1.0]
#row 1 →        [1.0,       1.0]

#so 

#correlation[0, 1]

#For exactly two variables, yes — the correlation between them will be at:

#correlation[0, 1]