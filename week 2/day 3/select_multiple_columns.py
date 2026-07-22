#To select more than one column, pass a list of column names:


import pandas as pd 

#think of it like this 
#students[ ["name", "score"] ]
#        └──── list ─────┘


#Outer [] selects from the DataFrame.
#Inner [] creates a list of columns to select.



#    name  score
#0   Andy     80
#1  Sarah     92
#2    Ken     75
#3    Mia     88


#important 

#students["score"]            → Series
#students[["name", "score"]]  → DataFrame


#practice 


#question 1

employees = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken"],
    "department": ["IT", "Sales", "HR"],
    "salery": [50000, 62000, 55000]
})




print(employees[["name", "salery"]])


#    name  salery
#0   Andy   50000
#1  Sarah   62000
#2    Ken   55000


#question 2


print(employees[["name", "department"]])


#0   Andy         IT
#1  Sarah      Sales
#2    Ken         HR