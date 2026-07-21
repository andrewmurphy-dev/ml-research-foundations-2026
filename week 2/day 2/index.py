#.index shows the row labels of a DataFrame.


#for example 

import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})


print(students.columns)
#Index(['name', 'age', 'score'], dtype='str')



print(students.shape)
#(6, 3)




print(students.index)
#RangeIndex(start=0, stop=6, step=1)



#so index, is like range(start :  stop(dont include) :  steps)


