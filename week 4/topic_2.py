#median 

#this is the middle value after the numbers are arranged from largest to smallest ! 


#for example 

import numpy as np

scores = np.array([5, 10, 15, 20, 25])

median = np.median(scores)

print(median)


#15.0


#what is there are an even number of values ?

#for example 

#5, 10, 20, 30

#There isn't one middle number. The two middle values are:

#10 and 20

#so numpy takes there mean 

(10 + 20) / 2 = 15

median = 15







#how do we sort the values ?


scores = np.array([30, 10, 50, 20, 40])

scores.sort()

print(scores)


#question 1 


result = np.array([40, 10, 30, 20, 50])

result.sort()

median = np.median(result)

print(median)


#question 2 


score = np.array([50, 10, 40, 20])

score.sort()

median = np.median(score)

print(median)