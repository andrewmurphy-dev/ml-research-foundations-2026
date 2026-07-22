#what is .loc?


#this selects data using labels !

import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "age": [29, 25, 31, 27],
    "score": [80, 92, 75, 88]
}, index=["a", "b", "c", "d"])

print(students)
#    name  age  score
#a   Andy   29     80
#b  Sarah   25     92
#c    Ken   31     75
#d    Mia   27     88




print(students.loc["b"])
#name     Sarah
#age         25
#score       92
#Name: b, dtype: object




print(students.loc["b", "score"])

#92


#question 1 

employees = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken"],
    "department": ["IT", "Sales", "HR"],
    "salary": [50000, 62000, 55000]
}, index=["a", "b", "c"])

print(employees)

#    name department  salary
#a   Andy         IT   50000
#b  Sarah      Sales   62000
#c    Ken         HR   55000

print(employees.loc["c"])

#name            Ken
#department       HR
#salary        55000
#Name: c, dtype: object

print(employees.loc["c", "salary"])

#55000

