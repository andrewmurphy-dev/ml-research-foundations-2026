
#rng.choice()
#→ pick values FROM data you already have


#rng.normal()
#→ generate NEW random values from a normal distribution






#question 1 


import numpy as np 

data = np.array([10, 20, 30, 40, 50])




rng = np.random.default_rng()

result = rng.choice(
    data,
    size=10,
    replace=True
)

print(result)



#question 2 

#Using the same data, create 20 random values from the existing data, but this time do not allow duplicates.

data = np.array([10, 20, 30, 40, 50])

rng = np.random.default_rng()

r = rng.choice(
    data, 
    size=5,
    replace=False
)

print(r)


#question 3 


data = np.array([10, 20, 30, 40, 50])


rng = np.random.default_rng()


result = rng.choice(
    data,
    size=3,
    replace=False
)


print(result)


#question 4 

data = np.array([10, 20, 30, 40, 50])


rng = np.random.default_rng()


r = rng.choice(
    data,
    size=8,
    replace=True
)

print(r)


#question 5 

data = np.array([5, 10, 15, 20, 25, 30])

rng = np.random.default_rng()

r = rng.choice(data, size=4, replace=False)

print(r)


#question 6 

rng = np.random.default_rng()

r = rng.normal(loc=100, scale=15, size=500)

print(np.mean(r))


#question 7 

rng = np.random.default_rng()

r = rng.normal(loc=50, scale=5, size=1000)

print(np.std(r))


#question 8 

rng = np.random.default_rng()

r = rng.normal(loc=0, scale=2, size=200)

print(np.mean(r))
print(np.std(r))