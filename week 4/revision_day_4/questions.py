#question 1 


import pandas as pd

products = pd.DataFrame({
    "product": ["Keyboard", "Mouse", "Monitor", "Laptop"],
    "price": [80, 40, 250, 1200],
    "stock": [12, 25, 7, 4]
})


print(products.head(2))


#question 2 


print(products.tail(2))


#question 3

print(products.iloc[1])


#question 4


print(products.iloc[0, 1])

#for multiple rows , when using iloc, we use slicing 

print(products.iloc[0:2])

#or 

print(products.iloc[:2])


#question 5

#prijnt the column names of products 

#we dont use loc 


print(products.columns)

#question 6 

print(products.index)



#question 7 

print(products.dtypes)



#question 8

print(products["price"])

#question 9 

print(products[["product", "stock"]])

#for multiple columns , u neeed to ue a list !

#question 10

print(products[["price", "stock"]])



#question 11



print(products.iloc["price"][0])

#iloc means select using number positions !

print(products.iloc[0, 1])


#question 12


print(products[products["price"] > 50])



#question 13 

print(products[products["stock"] < 10])



#question 14

product_1 = products["price"] > 50

stock_1 = products["stock"] < 10


print(products[product_1 & stock_1])


#question 15 

print(products.sort_values("price", ascending=False))







