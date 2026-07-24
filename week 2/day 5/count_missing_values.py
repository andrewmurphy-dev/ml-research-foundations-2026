#count missng values 

import pandas as pd 

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken"],
    "score": [80, None, 75]
})

print(students.isna())


#0  False  False
#1  False  False
#2  False   True
#3  False  False





#so we do , 


print(students.isna().sum())

#counts the missing values in each column , i know it looks like index , casue wuth 0, 1 , but its actually the result of the series 

#think of it like students["name"] = 




#practice question 




orders = pd.DataFrame({
    "customer": ["Andy", None, "Ken", "Mia"],
    "total": [50, 120, None, 80]
})



print(orders.isna().sum())

#customer    1
#total       1
#dtype: int64