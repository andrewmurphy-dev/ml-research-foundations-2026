
#question 1 


import pandas as pd 



orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 102],
    "status": ["paid", "pending", "paid", "cancelled", "pending"],
    "total": [50, None, 80, 120, None]
})


print(orders)


#question 2
print(orders.isna())


#question 3 


print(orders.duplicated())


#question 4

print(orders.drop_duplicates())



#question 5 

print(orders["status"].value_counts())



#question 6 

print(orders.isna().sum())


#question 7 

print(orders.isna().duplicated())


#question 8

print(orders.drop_duplicates())


#question 9 


print(orders["status"].value_counts())

#question 10 

print(orders.isna())


#question 11 


print(orders["total"].isna().sum())


#question 12
clean_orders = orders.drop_duplicates()
print(clean_orders)

#question 13 

print(clean_orders["status"].value_counts())


#question 14 

print(orders.duplicated().sum())

#question 15 

clean_orders = orders.drop_duplicates()


print(clean_orders["status"].value_counts())