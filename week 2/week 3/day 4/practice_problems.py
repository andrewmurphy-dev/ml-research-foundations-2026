import pandas as pd 

#question 1 

orders = pd.DataFrame({
    "order_id": [102, 202, 203, 202, 205],
    "status": ["paid", "pending", "paid", "pending", "cancelled"],
    "total": [75, None, 110, None, 95]
})



print(orders)



#question 2 

print(orders.isna())


#question 3 --> struggled 

#so sum() this counts the true values in each column or rows 


print(orders.isna().sum())


#question 4 

print(orders.duplicated)

#duplicated needs parenthesis


print(orders.duplicated())




#question 5 

print(orders.duplicated().sum())



#question 6 

print(orders.drop_duplicates())


#question 7 

print(orders["status"].value_counts())

#not sort_values

#question 8

print(orders.isna())
#this is boolean 

#question 9 

print(orders.isna().sum())

#this is not boolean , this is value 


#question 10 


clean_orders = orders.drop_duplicates()

print(clean_orders)


#question 11

print(clean_orders["status"].value_counts())

#question 12 

print(orders.duplicated())


#question 13 

print(orders.duplicated().sum())


#question 14

clean_df = orders.drop_duplicates()

print(clean_df)

#question 15 

print(orders["status"].value_counts())