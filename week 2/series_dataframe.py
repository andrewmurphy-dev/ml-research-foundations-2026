#what is a series?

#this is a column

import pandas as pd

scores = pd.Series([10, 40, 60])

print(scores)


#REMEMBER IT A CAPITAL S , Series 

#result

#0    10
#1    40
#2    60
#dtype: int64

#what is dtype?

#A property used in data science to find the data type of an entire array or DataFrame column.





#what is a dataframe? 

#this is a table with multiple labelled columns 


students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken"],
    "score": [80, 90, 75]
})

print(students)



#so lets understand this , each , "name":  , "score": forms a series 



#    name  score
#0   Andy     80
#1  Sarah     90
#2    Ken     75


#remember DataFrame , CAPITAL D, F 



#"name"  → column name
#["Andy", "Sarah", "Ken"] → column values

#"score" → column name
#[80, 90, 75]            → column values