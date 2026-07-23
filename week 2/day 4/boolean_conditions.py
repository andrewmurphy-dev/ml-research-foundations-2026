
import pandas as pd 


students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "age": [29, 25, 31, 27],
    "score": [80, 92, 75, 88]
})


print(students)

#    name  age  score
#0   Andy   29     80
#1  Sarah   25     92
#2    Ken   31     75
#3    Mia   27     88





print(students["score"] >= 80)


#0     True
#1     True
#2    False
#3     True
#Name: score, dtype: bool


#so this returns a boolean series 


#practice questions 


#question 1 

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "age": [29, 25, 31, 27],
    "score": [80, 92, 75, 88]
})



print(students["score"] >= 30)

#0    True
#1    True
#2    True
#3    True
#Name: score, dtype: bool



#question 2 


Products = pd.DataFrame({
    "product": ["Keyword", "Mouse", "Monitor", "Headset"],
    "price": [80, 40, 250, 65],
    "stock": [12, 25, 7, 18],
})


print(Products["price"] > 70)

#0     True
#1    False
#2     True
#3    False
#Name: price, dtype: bool