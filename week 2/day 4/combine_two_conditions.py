#for this the most important thing is the syntax 


#&  → both conditions must be True
#|  → at least one condition must be True

#& / |        → operators that combine Boolean conditions



#practice question


#question 1
import pandas as pd


employees = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "salary": [50000, 72000, 68000, 81000],
    "remote": [True, False, True, True]
})



print(employees[(employees["salary"] >= 70000) & (employees["remote"] == True)])


#  name  salary  remote
#3  Mia   81000    True




#question 2 


products = pd.DataFrame({
    "product": ["Keyboard", "Mouse", "Monitor", "Headset"],
    "price": [80, 40, 250, 65],
    "stock": [12, 25, 7, 5]
})



#filter products where 

#price is greater than 100
#OR
#stock is less than 10


print(products[(products["price"] > 100) | (products["stock"] < 10)])

#   product  price  stock
#2  Monitor    250      7
#3  Headset     65      5