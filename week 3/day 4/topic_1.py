#partial derivitves


#an ordinary dirivative uses one input 

def f(x):
    return x ** 2


#an parital derivative uses multiple inputs 


def f(x, y):
    return x ** 2 + y ** 2




#in code for example


def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 3
h = 0.001

partial_x = (f(x + h, y) - f(x, y)) / h

print(partial_x)




#notice the difference with normal derivatives

f(x + h, y)


#x receives the tiny change, but y stays exactly the same.




#formula for normal 

derivative = (f(x + h) - f(x)) / h


#formula for partial derivatives 
partial_x = (f(x + h, y) - f(x, y)) / h



#coding questions 


#question 1 


def f(x, y):
    return x ** 2 + y ** 2

x = 3
y = 4
h = 0.001

partial_x = (f(x + h, y) - f(x, y)) / h

print(partial_x)



#understanding 


#The derivative formula uses that function

#it calls the function twice 


#f(x + h, y)   # slightly changed x
#f(x, y)       # original x





#how is it callig the fucntion tho  if its not matching the function parameters?
#It does match the function parameters.

#it needs two seperate arguments ! 

#f(first argument, second argument)

#Python calculates x + h before entering the function.


#def f(x,     y):
#      ↑      ↑
#f(2.001,     3)

#then python runs 

#return x ** 2 + y ** 2






#question 2 

def f(x, y):
    return x ** 2 + y ** 2

x = 4
y = 2
h = 0.001

partial_x = (f(x + h, y) - f(x, y))/h

print(partial_x)



#remember 

#(nearby output - original output) / tiny change



#question 3 
def f(x, y):
    return x ** 2 + y ** 2

x = 5
y = 3
h = 0.001

partial_x = (f(x + h, y) - f(x, y))/h

print(partial_x)




#question 4 - change y 


def f(x, y):
    return x ** 2 + y ** 2

x = 5
y = 3
h = 0.001

partial_y = (f(x, y + h) - f(x, y))/h

print(partial_y)



#question 5 both 

def f(x, y):
    return x ** 2 + y ** 2

x = 2
y = 4
h = 0.001

partial_x = (f(x + h, y) - f(x, y))/ h
partial_y = (f(x, y + h) - f(x, y))/h

print(partial_x)
print(partial_y)