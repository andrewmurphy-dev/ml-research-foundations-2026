import pandas as pd 


#question 1

products = pd.DataFrame({"product": ["Keyboard", "Mouse", "Monitor"],
                         "price": [80, 40, 250],
                         "stock": [12, 25, 7]})


print(products)


#question 2

#print the first 2 rows 
#so my though process is using iloc 

print(products.iloc[:2])

#or head 

print(products.head(2))


#question 3

#using products print the last 2 rows 

print(products.tail(2))




#question 4 

#Using products, print its shape.

print(products.shape)

#question 5 

#Using products, print the column names.


print(products.columns)



#question 6 

#Using products, print the index.


print(products.iloc)


#question 7 

print(products.columns.dtype)

#this is wrong 

print(products.dtypes)



#question 8 


print(products["price"])


#question 9 

print(products[["product", "stock"]])


#question 10 

#Using products, select and print the row at position 1 with iloc.

print(products.iloc[1])


#question 11 

print(products.loc[2])


#question 12 

#Using products, print only the price value from the row at position 0 with iloc.

print(products.iloc[0, 1])

#question 13 

#Using products, print only rows where price is greater than 50.


print(products[products["price"] > 50])


#question 14 

#price is greater than 50
#AND
#stock is less than 10


result = products[(products["price"] > 50) & (products["stock"] < 10)]
print(result)

#question 15 

print(products.sort_values("price", ascending=False))
#Without ascending=False, pandas sorts lowest to highest.


#question 16 

#Using products, sort the rows by stock from lowest to highest.

print(products.sort_values("stock"))



#question 17 


#Create this DataFrame called orders:

#order_id: 101, 102, 103, 104
#status:   paid, pending, paid, pending
#total:    50, None, 80, 120

#Then print how many missing values each column contains.



orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "status": ["paid", "pending", "paid", "pending"],
    "total": [50, None, 80, 120]
})


#use isna().sum()


print(orders.isna().sum())

#.isna() → mark missing values as True
#.sum()  → count the True values in each column






#question 18 

#Using orders, print a Boolean Series showing which rows are duplicates.


print(orders.duplicated())



#question 19 

#Using orders, remove the duplicate rows and print the cleaned DataFrame.

print(orders.drop_duplicates())




#question 20 


print(orders["status"].value_counts())

