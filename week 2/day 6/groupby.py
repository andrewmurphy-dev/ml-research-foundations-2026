#what is groupby()?

#groupby() puts rows with the same category into groups.

#groupby() sorts the group labels by default.

#pandas arranges the age groups numerically:


import pandas as pd

students = pd.read_csv("/Users/andrewmurphy/ML Foundations/ml-research-foundations-2026/week 2/day 6/students.csv")





#    name  age  score
#0   Andy   29     80
#1  Sarah   25     92
#2    Ken   31     75


print(students.groupby("age"))

#returns
#<pandas.api.typing.DataFrameGroupBy object at 0x1067b1a90>


#why Because groupby() does not return a DataFrame of results., It returns a GroupBy object that stores the grouping instructions.


#what is a groupbyobject ?










#mean


#nect we can choose which column we want to calculate 


print(students.groupby("age")["score"].mean())

#age
#25    92.0
#29    80.0
#31    75.0
#Name: score, dtype: float64



#So Sarah’s group appears first because 25 is the smallest age. It does not mean Sarah moved to row 0 in the original DataFrame



#you can rearrange the defaule , print(students.groupby("age", sort=False)["score"].sum())

#sort=False is origional order 


#students
#→ DataFrame

#.groupby("age")
#→ group rows by age

#["score"]
#→ choose the score column

#.mean()
#→ calculate the average score in each age group





#sum



import pandas as pd

students = pd.read_csv("/Users/andrewmurphy/ML Foundations/ml-research-foundations-2026/week 2/day 6/students.csv")


print(students.groupby("age")["score"].sum())


#group rows by age
#        ↓
#select score
#        ↓
#add the scores inside each age group

#25    92
#29    80
#31    75
#Name: score, dtype: int64




#for example 


students.groupby("age", sort=False)["score"].sum()



#age
#25    92
#29    80
#31    75
#Name: score, dtype: int64






#count 


#count() tells you how many rows are inside each group.




import pandas as pd

students_1 = pd.read_csv("/Users/andrewmurphy/ML Foundations/ml-research-foundations-2026/week 2/day 6/studnets_1.csv")




print(students_1)

#    name  age  score
#0   Andy   29     80
#1  Sarah   25     92
#2    Ken   29     75
#3   Emma   25     88


print(students_1.groupby("age")["score"].count())

#age
#25    2
#29    2

#two people are 25, 2 people are 29 



