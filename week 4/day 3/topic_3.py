#simulations 




#using code to imitate a random process many times.


#real process:
#roll a die

#simulation:
#make NumPy roll the die 1000 times

#Why do this?


#Because instead of only knowing the theoretical probability:

#P(rolling a 6) = 1 / 6 ≈ 16.7%

#we can test what happens in practice.


#for example 

import numpy as np 


rng = np.random.default_rng()

rolls = rng.integers(1, 7, size=1000)

print(rolls)


#Now we can count how many 6s appeared:

sixes = np.sum(rolls == 6)

print(sixes)


#rolls == 6

#checks every roll and gives True where the result was 6.



#question 1 


#Simulate 1000 die rolls and print how many times 6 appeared.


rng = np.random.default_rng()

result = rng.integers(1, 7, size=1000)

six = np.sum(result == 6)

print(six)


#question 2 


result = np.random.default_rng()

rng = result.integers(1, 7, size=1000)

six = np.sum(rng == 6)

percentage = (six / 1000) * 100

print(percentage)