#what is head()?

#this shows the first rows of the dataframe 


import pandas as pd


students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})



print(students)
print(students.head())
#so the default for .head() is the first 5 rows 







#so head starts at 0 obviously but for head() we count at 1 , so it finishes at 4 so its essetencially len(index) - 1


#we can also adjust the amount of rows we want to see 



print(students.head(2))


#0   Andy   29     80
#1  Sarah   25     92




#practice questions 


#question 1
students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia", "John", "Emma"],
    "age": [29, 25, 31, 27, 35, 24],
    "score": [80, 92, 75, 88, 70, 95]
})


print(students.head(3))

#0   Andy   29     80
#1  Sarah   25     92
#2    Ken   31     75