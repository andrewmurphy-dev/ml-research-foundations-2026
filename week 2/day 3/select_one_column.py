
import pandas as pd 

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "age": [29, 25, 31, 27],
    "score": [80, 92, 75, 88]
})

print(students["name"])

#result 

#0     Andy
#1    Sarah
#2      Ken
#3      Mia
#Name: name, dtype: str


#students["name"]
#    │         │
#DataFrame   column label


#selecting one column returns a series 



#practice 


#question 1 

Products = pd.DataFrame({
    "product": ["keyboard", "mouse", "monitor", "headset"],
    "price": [80, 40, 250, 65],
    "stock": [12, 25, 7, 18]
})


print(Products["product"])



#0    keyboard
#1       mouse
#2     monitor
#3     headset
#Name: product, dtype: str



#question 2

print(Products["price"])

#Name: product, dtype: str
#0     80
#1     40
#2    250
#3     65
#Name: price, dtype: int64


#question 3

print(Products["stock"])

#0    12
#1    25
#2     7
#3    18
#Name: stock, dtype: int64




