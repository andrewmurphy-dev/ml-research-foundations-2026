#these are operators used in boolean conditions 


#>   greater than
#>=  greater than or equal to
#<   less than
#<=  less than or equal to
#==  equal to
#!=  not equal to



#for example 

import pandas as pd 


orders = pd.DataFrame({
    "customer": ["Andy", "Sarah", "Ken", "Mia"],
    "total": [45, 120, 75, 200],
    "paid": [True, True, False, True]
})




print(orders["total"] > 100)


#    False
#1     True
#2    False
#3     True
#Name: total, dtype: bool



print(orders["total"] <= 75)

#0     True
#1    False
#2     True
#3    False
#Name: total, dtype: bool


print(orders["paid"] == True)

#0     True
#1     True
#2    False
#3     True
#Name: paid, dtype: bool


#### IMPORTANT !!!!!


#=   assigns a value
#==  compares two values


print(orders["customer"] != "Ken")

#0     True
#1     True
#2    False
#3     True
#Name: customer, dtype: bool



#practice question


#question 1 

orders = pd.DataFrame({
    "customer": ["Andy", "Sarah", "Ken", "Mia"],
    "total": [45, 120, 75, 200],
    "paid": [True, True, False, True]
})



#Using the orders DataFrame, create and print a Boolean Series that checks which orders are not paid.

print(orders["paid"] == False)


#0    False
#1    False
#2     True
#3    False
#Name: paid, dtype: bool