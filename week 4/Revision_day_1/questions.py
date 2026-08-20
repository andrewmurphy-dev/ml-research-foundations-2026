#question 1 


probability = 2/6 

print(probability)


#question 2 


probability = 3/6 

print(probability)

#probability to find a even number 

#2, 4, 6 

#question 3 

probability = 4/6

print(probability)

#question 4 

probability = 4/6


print(probability)

#question 5 

prob = 3/6

print(prob)


#question 6 

prob = 3/6 

print(prob)

#question 7 

p = 2/6

print(p)



#question 8 

prob = (1 / 2) * (1 / 2)

print(prob)


#question 9 

prob = (1/6) * (1/6)

print(prob)

#question 10 

prob = (1/ 2) * (1 / 6)

print(prob)


#question 11 

prob = (1 / 2) * (1 / 2)

print(prob)


#question 12 

p = (3/6) * (3/6)

print(p)

#question 13 

p = (2/6) * (2/6)

print(p)



#Bayes Institution ! 

#question 14

#A machine has a 10% chance of being faulty.

#Then a warning light appears, and warning lights are much more common when the machine is faulty.

#Should the probability that the machine is faulty:

#A. Go up
#B. Go down
#C. Stay the same

#A


#questin 15 


#A disease is initially rare.

#A test comes back positive, and positive results are much more common in people who actually have the disease.

#Should the probability that the person has the disease:

#A. Go up
#B. Go down
#C. Stay the same

#A

#question 16 

#Question 16

#A machine has a 20% chance of being faulty.

#Then it passes a diagnostic test, and passing is much more common when the machine is not faulty.

#Should the probability that the machine is faulty:

#A. Go up
#B. Go down
#C. Stay the same

#B


#question 17 

#A person has a 30% chance of having a condition.

#A test comes back negative, and negative results are much more common in people who do not have the condition.

#Should the probability that the person has the condition:

#A. Go up
#B. Go down
#C. Stay the same

#B


#question 18 
#Uniform vs Normal Distribution

#Which one describes a **uniform distribution**?

#**A.** Every possible outcome has the same probability
#**B.** Values near the mean are more common
#**C.** Extreme values are more common than middle values


#A


#question 19 

#A normal distribution means:

#values near the mean are more common

#question 20
import numpy as np

rng = np.random.default_rng()

result = rng.normal(
    loc=50,
    scale=10,
    size=1000

)

print(np.mean(result))


#i get confused when i use choice and normal 

#rng.choice()
#→ pick values FROM data you already have


#rng.normal()
#→ generate NEW random values from a normal distribution



#question 21 

data = np.array([10, 20, 30, 40, 50])

rng = np.random.default_rng()

result = rng.choice(
    data,
    size=len(data),
    replace=True
)

print(result)

