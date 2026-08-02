#derivatives

#it tells us 
#At this particular x-value,
#how quickly is y changing?


#for a straight line !


#y = 2x + 1

#the slope is always 2, so the derivative is always 2.




#but for a curved function 


#y = x²


#the slope changes depending on where you are on the curve.


#for example 


def f(x):
    return x ** 2

x = 2
h = 0.001

derivative = (f(x + h) - f(x)) / h

print(derivative)


#what is h?

## h is a tiny change in x




#x = original input
#h = tiny step in the x-direction
#x + h = nearby input


#what is nearby input?

#nearby input means another x value that is extremely close to the original x.



#original input = x     = 2
#nearby input   = x + h = 2.001

#2.001 is “nearby” because it is only 0.001 away from 2.


#2 ●────● 2.001
#   0.001


#whats the benefit of this ?

#we use h so we can asnwer 

# At this particular x-value,
# how quickly is y changing?

#for a curve like 

#f(x) = x ** 2

#the slope is different at different places. There is no single slope for the whole curve

#At x = 2, we need two points to calculate a change:

#original input: x     = 2
#nearby input:   x + h = 2.001

#Then we measure:

#change in y
#───────────
#change in x

#large h → slope across a wider section
#tiny h  → slope very close to the exact point


#change a model value slightly
#→ see how much the error changes




#questions




def f(x):
    return x ** 2

x = 2
h = 0.1 

derivative = (f(x + h) - f(x)) / h

print(derivative)

#you really need to understand the formula 