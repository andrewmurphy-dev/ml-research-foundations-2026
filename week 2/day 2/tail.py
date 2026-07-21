#what is .tail()? 



#this shows the last rows of the DataFrame 
#you can also choose how many 


#for example 

import pandas as pd


students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})



print(students)


#    name  age  score
#0   Andy   29     80
#1  Sarah   25     92
#2    Ken   31     75
#3    Mia   27     88
#4   John   35     70
#5   Emma   24     95



print(students.tail())



#    name  age  score
#1  Sarah   25     92
#2    Ken   31     75
#3    Mia   27     88
#4   John   35     70
#5   Emma   24     95




print(students.tail(2))


#   name  age  score
#4  John   35     70
#5  Emma   24     95