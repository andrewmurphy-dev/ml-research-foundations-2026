#repeat bootstrap many times 

#One bootstrap sample isn't enough. We want to repeat this process many times and collect the means.

#so my assumption is we need a sample error ?

#The reason we repeat the bootstrap many times is to estimate:

#how much our sample statistic, like the mean, would change if we had gotten a different sample.


#so the flow is 

#original sample
#↓
#bootstrap sample
#↓
#calculate mean

#repeat many times
#↓
#collect lots of bootstrap means
#↓
#see how much those means vary


#Question 1

#Using the same data, create a loop that makes 10 bootstrap samples and prints the mean of each one
import numpy as np


bootstap = []

data = np.array([10, 40, 50, 60, 23])
rng = np.random.default_rng()

for num in range(1, 11, 1):
    num = rng.choice(
        data, 
        size=len(data),
        replace=True
    )

    print(np.mean(num))

    







    