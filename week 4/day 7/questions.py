#questions 


import numpy as np

#question 1 

data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))

#question 2 

data = np.array([5, 10, 15, 20, 25])

print(np.median(data))


#question 3

data = np.array([5, 5, 5, 5])

print(np.var(data))

#question 4 

data = np.array([10, 20, 30, 40, 50])

print(np.std(data))

#question 5 

#A fair die has 6 possible outcomes.
#What is the probability of rolling a 4?

probability = 1/6 

print(probability)


#question 6 

probability = 1/6

percentage = probability * 100

print(percentage)


#question 7
probability = 3 / 6

percentage = probability * 100

print(percentage)

#question 8

probability = (1 / 2) * (1 * 2)

print(probability)

#question 9

#A machine has a 10% chance of being faulty.
#Then a warning light appears, and warning lights are much more common when the machine is faulty.
# Should your probability that the machine is faulty:

#A. Go up
#B. Go down
#C. Stay the same


#QUESTION 10

#Which one is a uniform distribution?

#A. Every possible outcome has the same probability
#B. Values near the mean are more common
#C. One outcome is much more likely than the others


#question 11 

rng = np.random.default_rng()

result = rng.normal(
    loc=50,
    scale=10,
    size=1000  
)

print(np.mean(result))


#question 12 


rng = np.random.default_rng()

rolls = rng.integers(1, 7, size=1000)

print(rolls)


sixes = np.sum(rolls == 6)

print(sixes)


#question 13

probability = sixes / 1000
percentage = probability * 100

print(percentage)


# Question 14 

#A population has `10,000` people.

#You randomly select `100` people and calculate their average height.

#Which is the **sample**?

##**A.** All `10,000` people
##**B.** The `100` selected people


#question 15 hard
#in common problems!



#question 16


data = np.array([10, 20, 30, 40, 50])

rng = np.random.default_rng()

result = rng.choice(
    data,
    size=len(data),
    replace=True
)


print(result)



#question 17

data = np.array([10, 20, 30, 40, 50])
rng = np.random.default_rng()
bootstrap_means = []


for i in range(1, 101, 1):
    sample = rng.choice(
        data,
        size=len(data),
        replace=True
    )

    mean = np.mean(sample)

    bootstrap_means.append(mean)

print(bootstrap_means)
print(np.std(bootstrap_means))



#quesdtion 18

lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print(lower)
print(upper)
