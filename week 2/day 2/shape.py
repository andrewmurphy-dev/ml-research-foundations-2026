#what is .shape?

#this tells you the number of rows and columns !

import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})



print(students.shape)

#(6, 3)


#.shape is a property

#we do not use () 


#practice 


char = pd.DataFrame({"students": ["Andrew", "Jack", "Mary"],
                     "Grade": ["A+", "B", "A"]})


print(char)


#  students Grade
#0   Andrew    A+
#1     Jack     B
#2     Mary     A


print(char.head(1))
print(char.tail(1))
print(char.shape)

#0   Andrew    A+
# 2     Mary     A
(3, 2)


