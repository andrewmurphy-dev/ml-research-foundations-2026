#rememeber .duplicated() only finds duplicate rows.
#to remove them .drop_duplicates()

import pandas as pd

customers = pd.DataFrame({
    "name": ["Andy", "Sarah", "Andy", "Ken"],
    "city": ["Sapporo", "Tokyo", "Sapporo", "Osaka"]
})

print(customers)
#    name     city
#0   Andy  Sapporo
#1  Sarah    Tokyo
#2   Andy  Sapporo
#3    Ken    Osaka

#we want to save this in memory so we can call the clean data again 

clean_customers = customers.drop_duplicates()

print(clean_customers)


#    name     city
#0   Andy  Sapporo
#1  Sarah    Tokyo
#3    Ken    Osaka



#.duplicated()       → detects duplicates
#.drop_duplicates()  → removes duplicates




#practice question 


orders = pd.DataFrame({
    "customer": ["Andy", "Mia", "Andy", "Ken"],
    "total": [50, 90, 50, 120]
})


print(orders.duplicated())


#0    False
#1    False
#2     True
#3    False
#dtype: bool


clean_orders = orders.drop_duplicates()

print(clean_orders)


#  customer  total
#0     Andy     50
#1      Mia     90
#3      Ken    120