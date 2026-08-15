#bootstrap confidence interval 

#A bootstrap confidence interval tells us:

#a range of values our estimate could reasonably fall around, based on the bootstrap samples.

#for example ]


32
35
36
38
39
40
42
43
45
47

#Instead of only saying:

#mean ≈ 40


#we might say:

#bootstrap confidence interval ≈ 34 to 46


#In code, we use:

#np.percentile()

#A percentile is just a cutoff point in sorted data.

#For a common 95% bootstrap confidence interval, we keep the middle 95% of our bootstrap means:

#for example


import numpy as np

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


#HERE!!!!
lower = np.percentile(boot_mean, 2.5)
upper = np.percentile(boot_mean, 97.5)

print(lower)
print(upper)

