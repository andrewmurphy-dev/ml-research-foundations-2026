#.columns shows the column names in a DataFrame.
#remember the names of the dataframe 
#it is columns with an "s"

#for example 
import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})


print(students)
print(students.columns)

#Index(['name', 'age', 'score'], dtype='str')


#some versions may show dtype='object'


