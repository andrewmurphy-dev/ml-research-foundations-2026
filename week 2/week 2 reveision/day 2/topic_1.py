import pandas as pd 


#question 1 
products = pd.DataFrame({
    "product": ["Keyboard", "Mouse", "Monitor", "Headset", "Webcam"], 
    "price": [80, 40, 250, 65, 125],
    "stock": [12, 25, 7, 18, 5]
})


print(products)


#question 2 


result = products[products["price"] > 70]

print(result)



#question 3 


print(products[products["stock"] < 15])



#question 4 

result = products[products["price"] <= 80]

print(result)


#question 5 

result = products[products["stock"] >= 12]

print(result)


#question 6 


result = products[products["product"] == "Mouse"]

print(result)



#question 7

result = products[products["product"] != "Mouse"]

print(result)



#question 8 

result = products[(products["price"] > 70) & (products["stock"] < 15)]

print(result)



#question 9 


result = products[(products["price"] <= 125) & (products["stock"] >= 12)]

print(result)


#question 10 


result = products[(products["product"] != "Keyboard") & (products["price"] > 60)]

print(result)


#question 11 

result = products[(products["stock"] <= 12) & (products["price"] >= 80)]

print(result)


#question 12 

#i think its sort_values()

result = products.sort_values("price")

print(result)


#question 13 

result = products.sort_values("price", ascending=False)

print(result)



#question 14 


result = products.sort_values("stock", ascending=False)
print(result)


#question 15 


result = products.sort_values("stock")
print(result)


#question 16 


result = products[(products["price"] < 200) & (products["stock"] > 10)]
print(result)



#question 17 

result = products[(products["price"] >= 65) & (products["stock"] != 7)]
print(result)


#question 18



result = products[products["price"] > 60]
print(result)