#mathimatical functions 


#a function is a rule that ,

#1. takes input 
#2. applies a rule 
#3. returns a output

#for example


#f(x) = 2x + 1

#f = function name
#x = input
#2x + 1 = rule


#when x = 3 

#f(3) = 2 × 3 + 1
#f(3) = 7


#in python:


def calculate_y(x):
    return 2 * x + 1

result = calculate_y(10)
print(result)
#21


#what are we trying to get at here?

#we are learning how to represent a mathematical function using python code ! 

#why does this matter for machine learning ?


#a machine learning model is essentially a mathematical function 

#input features ---> model function ---> predition 

#for example 

#hours studied --> model ---> predicition 


#We are learning to look at mathematical equations and translate them into Python.


#questions 



#question 1 


def f(x):
    return 3 * x + 2


result = f(5)
print(result)


#question 2 

def f(x):
    return x ** 2 + 3


result = f(4)
print(result)


#