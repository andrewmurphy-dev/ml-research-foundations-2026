
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

print(products.head(3))

#question 4

print(products.iloc[1])

#question 5

print(products.columns)

#question 6 

print(products.index)

#question 7 

print(products.dtypes)


#question 8 

print(products["price"])

#question 9 

print(products[["product", "stock"]])

#question 10 

print(products["stock"])

#question 11

print(products[["price", "stock"]])

#question 12

#Using products, print only the price value from row position 0 using iloc.

print(products.iloc[0, 1])

#question 13

print(products[products["price"] > 50])

