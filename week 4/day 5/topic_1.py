#what is bootstrap?


#repeatedly creating new samples from the data you already have, so you can see how much your result might vary.


#for example

import numpy as np


data = np.array([10, 20, 30, 40, 50])


#We might create a bootstrap sample like:

#[20, 20, 50, 10, 40]

#Notice 20 appears twice.

#That is allowed because bootstrap uses sampling with replacement.