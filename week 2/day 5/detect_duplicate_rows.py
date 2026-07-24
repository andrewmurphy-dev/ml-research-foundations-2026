#A duplicate row means the same row appears more than once.
#we use duplicated() this is past tense 


#for example 

import pandas as pd

orders = pd.DataFrame({
    "customer": ["Andy", "Sarah", "Andy", "Ken"],
    "total": [50, 120, 50, 80]
})

print(orders)




#  customer  total
#0     Andy     50
#1    Sarah    120
#2     Andy     50
#3      Ken     80


#check for duplicates 

#print(orders.duplicated())


#0    False
#1    False
#2     True
#3    False
#dtype: bool

#False → this is the first occurrence
#True  → this row appeared earlier


#.duplicated() only detects duplicates. It does not remove them.