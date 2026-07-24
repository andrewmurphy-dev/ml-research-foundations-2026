#.value_counts() counts how many times each value appears in one column.




#for example 

import pandas as pd 

employees = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John"],
    "department": ["IT", "Sales", "IT", "HR", "IT"]
})


print(employees["department"].value_counts())



#department
#IT       3
#Sales    1
#HR       1
#Name: count, dtype: int64


#creates a series 



