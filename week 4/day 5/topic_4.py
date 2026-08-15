#Bootstrap Standard Error


import numpy as np 

bootstrap_means = []

data = np.array([10, 40, 50, 60, 23])

rng = np.random.default_rng()

for i in range(1000):
    sample = rng.choice(
        data,
        size=len(data),
        replace=True
    )

    mean = np.mean(sample)
    bootstrap_means.append(mean)

standard_error = np.std(bootstrap_means)


print(bootstrap_means)
print(standard_error)


#small bootstrap standard error
#→ means stay fairly close together
#→ estimate is more stable

#large bootstrap standard error
#→ means move around a lot
#→ estimate is less stable




#question 1 
boot_mean = []

data = np.array([10, 40, 50, 60, 23])

rng = np.random.default_rng()

for i in range(1, 101, 1):
    sample = rng.choice(
        data,
        size=len(data),
        replace=True
    )

    mean = np.mean(sample)
    boot_mean.append(mean)

standard_error = np.std(boot_mean)

print(boot_mean)
print(standard_error)


#stabdard_error needs to be outside the loop !