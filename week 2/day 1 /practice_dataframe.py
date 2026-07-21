import pandas as pd 


#question 1 
students = pd.DataFrame({"name": ["Andy", "Sarah", "Ken"],
                        "age": [29, 25, 31],
                        "score": [80, 92, 75]})

#we need to put {}

print(students)



#question 2 

products = pd.DataFrame({"product": ["Keyboard", "Mouse", "Monitor"],
                         "Price": [80, 40, 250],
                         "Stock": [12, 25, 7]})

print(products)



#question 3 

patients = pd.DataFrame({"name": ["Andy", "Sarah", "Ken"],
                         "temp": [36.5, 38.1, 37.2],
                         "has_fever": [False, True, True]})

print(patients)