#so here we will practice series !

import pandas as pd 


#question 1

number = pd.Series([10, 40, 50])
print(number)

#0    10
#1    40
#2    50
#dtype: int64






#question 2 


scores = pd.Series([10, 20, 40], index=["Andy", "Sarah", "Ken"])

print(scores)

#Andy     10
#Sarah    20
#Ken      40
#dtype: int64


#You can also give it custom labels:, with index= [...]


#question 3 


temperatures = pd.Series([12, 18, 25, 30])

print(temperatures)



#question 4 

series = pd.Series([85, 92, 78], index=["Andy", "Sarah", "Ken"])

print(series)

#Andy     85
#Sarah    92
#Ken      78
#dtype: int64


#question 5 

passed = pd.Series([True, False, True, False], index=["Andy", "Sarah", "Ken", "Mia"])

print(passed)


#Andy      True
#Sarah    False
#Ken       True
#Mia      False
#dtype: bool


#why do we see dtype in series always ?

#Because pandas automatically shows a Series’ dtype at the bottom when it displays the Series.
#A Series has one dtype because it is one column:
#Series = one set of values = one dtype
