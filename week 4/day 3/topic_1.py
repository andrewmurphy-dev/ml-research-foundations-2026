# Distribution

# A distribution tells us:
# which values can happen and how often/how likely each value is.


# Uniform Distribution

# A uniform distribution means every possible outcome
# has the same probability.

# Example: fair die

# 1 → 1/6
# 2 → 1/6
# 3 → 1/6
# 4 → 1/6
# 5 → 1/6
# 6 → 1/6

#That pattern of probabilities is the distribution.


#another example 


#data = [1, 1, 1, 2, 2, 5]

#1 appears 3 times
#2 appears 2 times
#5 appears 1 time


#distribution = how values are spread across the possible results



#question 1 
import numpy as np

data = np.array([1, 1, 2, 2, 2, 3])

#Which value appears most often?
#2

#question 2 

data = np.array([4, 4, 4, 7, 7, 9, 9, 9, 9])

#Which value appears most often?



#question 3
data = np.array([2, 2, 5, 5, 8, 8])

#Which value appears most often?

#equally common 

#2 → 2 times
#5 → 2 times
#8 → 2 times



#question 4 

#Write code that simulates 20 die rolls using NumPy.

die = np.random.default_rng()

rolls = die.integers(1, 7, size=20)

print(rolls)

#[5 6 6 6 4 4 1 4 3 5 2 5 4 1 4 6 6 1 2 6]


#question 5 

#Now simulate 100 die rolls using the same method.

rng = np.random.default_rng()

rolls = rng.integers(1, 7, size=100)

print(rolls)

