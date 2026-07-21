#.dtypes shows the data type of each column:
#.dtypes is with an "s" , please remember this 

#for example 
import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})



print(students.dtypes)


#name       str
#age      int64
#score    int64
#dtype: object

#name  → string
#age   → integers
#score → integers


#remember 

#DataFrame → .dtypes
#Series    → .dtype